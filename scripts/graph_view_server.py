#!/usr/bin/env python3
"""Realtime knowledge-graph view (stdlib only).

Run:  python3 scripts/graph_view_server.py   then open http://127.0.0.1:8000
Serves a cytoscape canvas and pushes each new line of
.research/graph-events.jsonl to the browser over a hand-rolled WebSocket.
Read-only on engine artifacts; never part of a loop.
"""
import base64
import hashlib
import json
import os
import struct
import sys
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

_WS_GUID = "258EAFA5-E914-47DA-95CA-C5AB0DC85B11"


def ws_accept(key):
    """RFC6455 Sec-WebSocket-Accept for a client's Sec-WebSocket-Key."""
    digest = hashlib.sha1((key + _WS_GUID).encode("ascii")).digest()
    return base64.b64encode(digest).decode("ascii")


def ws_frame(text):
    """A single unmasked FIN+text WebSocket frame carrying a UTF-8 string."""
    payload = text.encode("utf-8")
    n = len(payload)
    header = bytearray([0x81])
    if n < 126:
        header.append(n)
    elif n < 65536:
        header.append(126)
        header += struct.pack(">H", n)
    else:
        header.append(127)
        header += struct.pack(">Q", n)
    return bytes(header) + payload


_POLL = 0.25  # seconds between tail polls


class _Handler(BaseHTTPRequestHandler):
    def _send_bytes(self, body, content_type):
        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        if self.path == "/ws":
            return self._serve_ws()
        if self.path == "/graph":
            p = Path(self.server.graph_path)
            body = p.read_bytes() if p.is_file() else b"{}"
            return self._send_bytes(body, "application/json; charset=utf-8")
        if self.path in ("/", "/index.html"):
            p = Path(self.server.html_path)
            body = p.read_bytes() if p.is_file() else b"<h1>view html missing</h1>"
            return self._send_bytes(body, "text/html; charset=utf-8")
        self.send_error(404)

    def _serve_ws(self):
        key = self.headers.get("Sec-WebSocket-Key")
        if not key:
            return self.send_error(400)
        self.send_response(101)
        self.send_header("Upgrade", "websocket")
        self.send_header("Connection", "Upgrade")
        self.send_header("Sec-WebSocket-Accept", ws_accept(key))
        self.end_headers()
        self.wfile.flush()   # flush handshake before raw frames go out on self.connection
        self._tail_loop()

    def _tail_loop(self):
        events = Path(self.server.events_path)
        pos = events.stat().st_size if events.is_file() else 0
        buf = b""
        conn = self.connection
        while True:
            try:
                size = events.stat().st_size if events.is_file() else 0
                if size < pos:            # truncated/rotated -> restart from top
                    pos, buf = 0, b""
                if size > pos:
                    with events.open("rb") as fh:
                        fh.seek(pos)
                        chunk = fh.read()
                    pos += len(chunk)
                    buf += chunk
                    while b"\n" in buf:
                        line, buf = buf.split(b"\n", 1)
                        line = line.strip()
                        if not line:
                            continue
                        try:
                            text = line.decode("utf-8")
                        except UnicodeDecodeError:
                            continue   # skip a corrupt log line rather than crash the client
                        conn.sendall(ws_frame(text))
                time.sleep(_POLL)
            except (BrokenPipeError, ConnectionResetError, OSError):
                return

    def log_message(self, *args):
        pass


def make_server(host, port, events_path, graph_path, html_path):
    srv = ThreadingHTTPServer((host, port), _Handler)
    srv.daemon_threads = True
    srv.events_path = events_path
    srv.graph_path = graph_path
    srv.html_path = html_path
    return srv


def _main(argv):
    import argparse
    root = Path(__file__).resolve().parent.parent
    ap = argparse.ArgumentParser(description="Realtime knowledge-graph view (read-only).")
    ap.add_argument("--host", default=os.environ.get("GV_HOST", "127.0.0.1"))
    ap.add_argument("--port", type=int, default=int(os.environ.get("GV_PORT", "8000")))
    ap.add_argument("--events",
                    default=os.environ.get("GV_EVENTS", str(root / ".research/graph-events.jsonl")))
    ap.add_argument("--graph",
                    default=os.environ.get("GV_GRAPH", str(root / ".graphify/graph.json")))
    ap.add_argument("--html",
                    default=os.environ.get("GV_HTML", str(root / "public/index.html")))
    args = ap.parse_args(argv)
    srv = make_server(args.host, args.port, args.events, args.graph, args.html)
    host, port = srv.server_address[:2]   # actual bound port (resolves --port 0)
    print(f"graph view on http://{host}:{port}  (events: {args.events})", flush=True)
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        srv.shutdown()
    return 0


if __name__ == "__main__":
    sys.exit(_main(sys.argv[1:]))
