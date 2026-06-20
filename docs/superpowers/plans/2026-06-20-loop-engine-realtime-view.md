# Realtime Graph View (sub-project #5) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** A browser view that animates the knowledge graph as it grows, streaming each new `graph-events.jsonl` delta over a stdlib-only WebSocket, rendering AI-asserted edges distinctly from corpus-extracted ones.

**Architecture:** A separate, manually-started `ThreadingHTTPServer` serves a cytoscape canvas, a `/graph` snapshot, and a hand-rolled RFC6455 WebSocket endpoint that tail-polls the append-only event log (one thread per client, each tailing independently). The event payload is enriched upstream with per-edge provenance so the stream is self-describing. The view is strictly read-only on engine artifacts and never part of a loop.

**Tech Stack:** Python 3 stdlib (`http.server`, `socket`, `hashlib`, `base64`, `struct`); cytoscape.js via CDN; `unittest` + bash for tests.

## Global Constraints

- **Python 3 stdlib only** — no pip, no pytest. Tests are `unittest` + bash `test_*.sh`.
- **No lint/type suppression comments** (`# noqa`, `# type: ignore`, etc.) — fix the code.
- **The view is read-only** — never writes `.research/` or `.graphify/`, never part of a loop, started manually.
- **Bind localhost only by default** (`127.0.0.1`) — the server is unauthenticated.
- **Asserted edges are tagged `_origin: "asserted"`** in `graph.json` `links` (NOT `source`). Default/extracted edges have no `_origin`.
- **Tests import scripts by alias** after `sys.path.insert(0, .../scripts)` (e.g. `import graph_events as ge`).
- **Commits:** Conventional Commits, selectively staged (never `git add .`/`-A`), no co-author / "Generated with" trailers.
- Running `state.py`/`assertions.py`/`check_integrity.py` seeds a default `.research/state.json` as a side effect — do not stage that artifact if it appears.

---

### Task 1: Enrich `graph_events` with per-edge provenance

**Files:**
- Modify: `scripts/graph_events.py`
- Test: `tests/test_graph_events.py`

**Interfaces:**
- Consumes: nothing new.
- Produces: `diff(old, new)` now returns a third key `edge_origins: dict[str, str]` mapping `"<source>|<target>"` → origin string, populated only for new edges whose new-graph link carries a truthy `_origin`. `append_event` writes `edge_origins` (defaulting `{}`) into each JSONL record alongside `new_nodes`/`new_edges`.

- [ ] **Step 1: Write the failing test**

First, `diff` will gain an always-present `edge_origins` key, so update the existing
full-dict-equality test (`tests/test_graph_events.py:27`) to expect it:

```python
    def test_missing_keys_tolerated(self):
        self.assertEqual(ge.diff({}, {}),
                         {"new_nodes": [], "new_edges": [], "edge_origins": {}})
```

Then add to `tests/test_graph_events.py` (inside `class TestGraphEvents`):

```python
    def test_diff_tags_asserted_edge_origin(self):
        old = {"nodes": [{"id": "a"}, {"id": "b"}], "links": []}
        new = {"nodes": [{"id": "a"}, {"id": "b"}, {"id": "c"}],
               "links": [{"source": "a", "target": "b", "_origin": "asserted"},
                         {"source": "a", "target": "c"}]}
        d = ge.diff(old, new)
        self.assertEqual(d["new_edges"], [["a", "b"], ["a", "c"]])
        self.assertEqual(d["edge_origins"], {"a|b": "asserted"})

    def test_append_writes_edge_origins(self):
        with tempfile.TemporaryDirectory() as t:
            ev = Path(t) / "graph-events.jsonl"
            ge.append_event(ev, {"new_nodes": [], "new_edges": [["a", "b"]],
                                 "edge_origins": {"a|b": "asserted"}},
                            now="2026-06-20T00:00:00Z")
            rec = json.loads(ev.read_text(encoding="utf-8").strip())
            self.assertEqual(rec["edge_origins"], {"a|b": "asserted"})
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m unittest tests.test_graph_events -v`
Expected: FAIL — `KeyError: 'edge_origins'` (diff has no such key).

- [ ] **Step 3: Write minimal implementation**

In `scripts/graph_events.py`, add a helper after `node_edge_sets`:

```python
def _edge_origins(graph):
    out = {}
    for e in graph.get("links", graph.get("edges", [])):
        s, t, o = e.get("source"), e.get("target"), e.get("_origin")
        if s is not None and t is not None and o:
            out[(s, t)] = o
    return out
```

Replace `diff` with:

```python
def diff(old, new):
    on, oe = node_edge_sets(old)
    nn, ne = node_edge_sets(new)
    new_edges = sorted(ne - oe)
    origins = _edge_origins(new)
    edge_origins = {f"{s}|{t}": origins[(s, t)]
                    for (s, t) in new_edges if (s, t) in origins}
    return {
        "new_nodes": sorted(nn - on),
        "new_edges": [list(p) for p in new_edges],
        "edge_origins": edge_origins,
    }
```

Replace the `rec = {...}` dict in `append_event` with:

```python
    rec = {"ts": now or datetime.now(timezone.utc).isoformat(),
           "new_nodes": delta.get("new_nodes", []),
           "new_edges": delta.get("new_edges", []),
           "edge_origins": delta.get("edge_origins", {})}
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python3 -m unittest tests.test_graph_events -v`
Expected: PASS (all existing + 2 new tests).

- [ ] **Step 5: Commit**

```bash
git add scripts/graph_events.py tests/test_graph_events.py
git commit -m "feat: graph_events delta carries per-edge provenance"
```

---

### Task 2: WebSocket protocol helpers (handshake + frame encoding)

**Files:**
- Create: `scripts/graph_view_server.py`
- Test: `tests/test_graph_view_server.py`

**Interfaces:**
- Consumes: nothing.
- Produces: module-level pure functions `ws_accept(key: str) -> str` (RFC6455 `Sec-WebSocket-Accept`) and `ws_frame(text: str) -> bytes` (single unmasked FIN+text frame, UTF-8 payload, correct length encoding for `<126`, `126..65535`, `≥65536`). Module constant `_WS_GUID`.

- [ ] **Step 1: Write the failing test**

Create `tests/test_graph_view_server.py`:

```python
import struct, sys, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import graph_view_server as gv


class TestWsHelpers(unittest.TestCase):
    def test_accept_matches_rfc6455_vector(self):
        # RFC6455 §1.3 canonical example.
        self.assertEqual(gv.ws_accept("dGhlIHNhbXBsZSBub25jZQ=="),
                         "s3pPLMBiTxaQ9kYGzzhZRbK+xOo=")

    def test_frame_short_payload(self):
        self.assertEqual(gv.ws_frame("hi"), b"\x81\x02hi")

    def test_frame_medium_payload(self):
        payload = "x" * 200
        f = gv.ws_frame(payload)
        self.assertEqual(f[0], 0x81)
        self.assertEqual(f[1], 126)
        self.assertEqual(struct.unpack(">H", f[2:4])[0], 200)
        self.assertEqual(f[4:], payload.encode("utf-8"))


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m unittest tests.test_graph_view_server -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'graph_view_server'`.

- [ ] **Step 3: Write minimal implementation**

Create `scripts/graph_view_server.py` with just the helpers (the server comes in Task 4):

```python
#!/usr/bin/env python3
"""Realtime knowledge-graph view (stdlib only)."""
import base64
import hashlib
import struct

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
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `python3 -m unittest tests.test_graph_view_server -v`
Expected: PASS (3 tests).

- [ ] **Step 5: Commit**

```bash
git add scripts/graph_view_server.py tests/test_graph_view_server.py
git commit -m "feat: stdlib WebSocket handshake + frame helpers for graph view"
```

---

### Task 3: Browser canvas (`public/index.html`)

**Files:**
- Create: `public/index.html`
- Test: `tests/test_graph_view_html.sh`

**Interfaces:**
- Consumes: `GET /graph` (snapshot, NetworkX node_link JSON: `nodes[].id`, `links[].{source,target,_origin}`) and the WebSocket at `/ws` (delta records `{new_nodes, new_edges, edge_origins}`).
- Produces: a static page. No code interface for later tasks; Task 4's smoke serves this file via `GET /`.

- [ ] **Step 1: Write the failing test**

Create `tests/test_graph_view_html.sh`:

```bash
#!/usr/bin/env bash
# Static checks: the canvas wires up cytoscape, the WS-first/buffer/seed
# sequence, and a distinct asserted-edge style. No browser automation.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
H="$ROOT/public/index.html"

[ -f "$H" ] || { echo "FAIL: $H missing"; exit 1; }
need(){ grep -qF "$1" "$H" || { echo "FAIL: index.html missing: $1"; exit 1; }; }

need "cytoscape"
need 'integrity="sha512-'   # CDN script must carry Subresource Integrity
need 'new WebSocket("ws://" + location.host + "/ws")'
need 'fetch("/graph")'
need "buffer.push"
need 'edge[origin = "asserted"]'

echo "PASS graph view html"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `bash tests/test_graph_view_html.sh`
Expected: FAIL — `FAIL: .../public/index.html missing`.

- [ ] **Step 3: Write the implementation**

Create `public/index.html`:

```html
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Knowledge graph — live</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/cytoscape/3.30.2/cytoscape.min.js"
        integrity="sha512-EY3U1MWdgKx0P1dqTE4inlKz2cpXtWpsR1YUyD855Hs6RL/A0cyvrKh60EpE8wDZ814cTe1KgRK+sG0Rn792vQ=="
        crossorigin="anonymous" referrerpolicy="no-referrer"></script>
<style>
  html, body { margin: 0; height: 100%; background: #0e1116; }
  #cy { width: 100vw; height: 100vh; }
  #status { position: fixed; top: 8px; left: 12px; color: #8b949e;
            font: 12px ui-monospace, monospace; z-index: 1; }
</style>
</head>
<body>
<div id="status">connecting…</div>
<div id="cy"></div>
<script>
const cy = cytoscape({
  container: document.getElementById("cy"),
  style: [
    { selector: "node", style: {
        "label": "data(id)", "font-size": 8, "color": "#c9d1d9",
        "background-color": "#388bfd", "width": 14, "height": 14 } },
    { selector: "edge", style: {
        "width": 2, "line-color": "#30363d",
        "target-arrow-color": "#30363d", "target-arrow-shape": "triangle",
        "curve-style": "bezier" } },
    { selector: 'edge[origin = "asserted"]', style: {
        "line-color": "#f778ba", "target-arrow-color": "#f778ba",
        "line-style": "dashed", "width": 2 } },
  ],
  layout: { name: "grid" },
});

const status = document.getElementById("status");
let seeded = false;
const buffer = [];

function addNode(id) {
  if (id != null && cy.getElementById(String(id)).empty())
    cy.add({ group: "nodes", data: { id: String(id) } });
}
function addEdge(s, t, origin) {
  if (s == null || t == null) return;
  const id = s + "|" + t;
  if (cy.getElementById(s).empty() || cy.getElementById(t).empty()) return;
  if (cy.getElementById(id).empty())
    cy.add({ group: "edges",
      data: { id, source: s, target: t, origin: origin || "extracted" } });
}

function addDelta(d) {
  (d.new_nodes || []).forEach(addNode);
  const origins = d.edge_origins || {};
  (d.new_edges || []).forEach(([s, t]) => addEdge(s, t, origins[s + "|" + t]));
  relayout();
}

let relayoutPending = false;
function relayout() {              // coalesce bursty deltas into one layout pass
  if (relayoutPending) return;
  relayoutPending = true;
  setTimeout(() => {
    relayoutPending = false;
    cy.layout({ name: "cose", animate: false }).run();
  }, 150);
}

// Open the WS first and buffer deltas so none are lost during the snapshot fetch.
const ws = new WebSocket("ws://" + location.host + "/ws");
ws.onmessage = (ev) => {
  const d = JSON.parse(ev.data);
  if (seeded) addDelta(d); else buffer.push(d);
};
ws.onopen = () => { status.textContent = "live"; };
ws.onclose = () => { status.textContent = "disconnected"; };

fetch("/graph").then(r => r.json()).then(g => {
  (g.nodes || []).forEach(n => addNode(n.id));
  (g.links || g.edges || []).forEach(e => addEdge(e.source, e.target, e._origin));
  seeded = true;
  buffer.splice(0).forEach(addDelta);
  cy.layout({ name: "cose", animate: false }).run();
}).catch(() => { seeded = true; });   // no snapshot yet — run on live deltas only
</script>
</body>
</html>
```

- [ ] **Step 4: Run test to verify it passes**

Run: `bash tests/test_graph_view_html.sh`
Expected: `PASS graph view html`.

- [ ] **Step 5: Commit**

```bash
git add public/index.html tests/test_graph_view_html.sh
git commit -m "feat: cytoscape canvas for live graph view"
```

---

### Task 4: The server (routes + WS upgrade + tail loop), README, e2e smoke

**Files:**
- Modify: `scripts/graph_view_server.py`
- Modify: `README.md`
- Test: `tests/test_graph_view_server.py` (add e2e class), `tests/test_graph_view_smoke.sh` (create)

**Interfaces:**
- Consumes: `ws_accept`, `ws_frame` (Task 2); `public/index.html` (Task 3).
- Produces: `make_server(host, port, events_path, graph_path, html_path) -> ThreadingHTTPServer` (bind `port=0` for an ephemeral port; read `srv.server_address[1]` for the actual port). CLI entrypoint `python3 scripts/graph_view_server.py [--host --port --events --graph --html]` with env fallbacks `GV_HOST/GV_PORT/GV_EVENTS/GV_GRAPH/GV_HTML` and repo-relative defaults (`.research/graph-events.jsonl`, `.graphify/graph.json`, `public/index.html`, `127.0.0.1`, `8000`). Routes: `GET /` → html, `GET /graph` → graph JSON (`{}` if absent), `GET /ws` → handshake then per-client tail of the events file (only lines appended after connect).

- [ ] **Step 1: Write the failing test**

First make the test file's top-of-file imports read exactly (extends Task 2's line — no duplicates):

```python
import json, socket, struct, sys, tempfile, threading, time, unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import graph_view_server as gv
```

Then append this class to `tests/test_graph_view_server.py`:

```python
class TestServerE2E(unittest.TestCase):
    def _start(self, tmp):
        events = Path(tmp) / "graph-events.jsonl"
        events.write_text("", encoding="utf-8")
        graph = Path(tmp) / "graph.json"
        graph.write_text('{"nodes":[{"id":"seed"}],"links":[]}', encoding="utf-8")
        html = Path(tmp) / "index.html"
        html.write_text("<html>cytoscape</html>", encoding="utf-8")
        srv = gv.make_server("127.0.0.1", 0, str(events), str(graph), str(html))
        threading.Thread(target=srv.serve_forever, daemon=True).start()
        return srv, srv.server_address[1], events

    def test_ws_handshake_and_delta(self):
        with tempfile.TemporaryDirectory() as tmp:
            srv, port, events = self._start(tmp)
            self.addCleanup(srv.shutdown)
            s = socket.create_connection(("127.0.0.1", port), timeout=5)
            self.addCleanup(s.close)
            s.sendall(
                b"GET /ws HTTP/1.1\r\nHost: x\r\nUpgrade: websocket\r\n"
                b"Connection: Upgrade\r\nSec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==\r\n"
                b"Sec-WebSocket-Version: 13\r\n\r\n")
            resp = s.recv(1024).decode("latin-1")
            self.assertIn("101", resp)
            self.assertIn("s3pPLMBiTxaQ9kYGzzhZRbK+xOo=", resp)
            # Handshake received -> the handler thread has captured end-of-file.
            # Sleep one poll interval so the append below is seen as a NEW line.
            time.sleep(0.3)
            with events.open("a", encoding="utf-8") as fh:
                fh.write('{"new_nodes":["a"],"new_edges":[],"edge_origins":{}}\n')
            s.settimeout(5)
            frame = s.recv(4096)
            self.assertEqual(frame[0], 0x81)
            payload = frame[2:] if frame[1] < 126 else frame[4:]
            self.assertEqual(json.loads(payload.decode("utf-8"))["new_nodes"], ["a"])
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m unittest tests.test_graph_view_server -v`
Expected: FAIL — `AttributeError: module 'graph_view_server' has no attribute 'make_server'`.

- [ ] **Step 3: Write the implementation**

In `scripts/graph_view_server.py`, make the **top of the file** read exactly this — shebang, docstring, then one grouped stdlib import block (this replaces the Task 2 imports; `base64`/`hashlib`/`struct` stay, the rest are added — no duplicates, no imports below code):

```python
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
```

Keep the existing `ws_accept`/`ws_frame`/`_WS_GUID` definitions, then append the server below them:

```python
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
```

- [ ] **Step 4: Run the unit + e2e tests**

Run: `python3 -m unittest tests.test_graph_view_server -v`
Expected: PASS (helpers + e2e).

- [ ] **Step 5: Write the bash smoke (real subprocess launch)**

Create `tests/test_graph_view_smoke.sh`:

```bash
#!/usr/bin/env bash
# End-to-end against the real CLI: launch the server on a free port over temp
# artifacts, assert GET / serves the canvas, GET /graph serves the snapshot,
# and an appended event line arrives over the WebSocket. Stdlib only.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
TMP="$(mktemp -d)"
SRV_PID=""
cleanup() { [ -n "$SRV_PID" ] && kill "$SRV_PID" 2>/dev/null || true; rm -rf "$TMP"; }
trap cleanup EXIT

printf '' > "$TMP/events.jsonl"
echo '{"nodes":[{"id":"seed"}],"links":[]}' > "$TMP/graph.json"
LOG="$TMP/server.log"

# Bind an ephemeral port (--port 0); the server prints the actual port it bound,
# so there is no free-port race.
python3 "$ROOT/scripts/graph_view_server.py" --host 127.0.0.1 --port 0 \
  --events "$TMP/events.jsonl" --graph "$TMP/graph.json" \
  --html "$ROOT/public/index.html" >"$LOG" 2>&1 &
SRV_PID=$!

PORT=""
for _ in $(seq 1 50); do
  PORT="$(sed -n 's#.*http://127.0.0.1:\([0-9][0-9]*\).*#\1#p' "$LOG" | head -1)"
  [ -n "$PORT" ] && break
  sleep 0.1
done
[ -n "$PORT" ] || { echo "FAIL: server did not report a port"; cat "$LOG"; exit 1; }

python3 - "$PORT" "$TMP" "$ROOT" <<'PY'
import json, socket, sys, time, urllib.request
port, tmp, root = int(sys.argv[1]), sys.argv[2], sys.argv[3]

html = urllib.request.urlopen(f"http://127.0.0.1:{port}/").read().decode("utf-8")
assert "cytoscape" in html, "GET / did not serve the canvas"

graph = json.load(urllib.request.urlopen(f"http://127.0.0.1:{port}/graph"))
assert graph["nodes"][0]["id"] == "seed", "GET /graph snapshot wrong"

s = socket.create_connection(("127.0.0.1", port), timeout=5)
s.sendall(b"GET /ws HTTP/1.1\r\nHost: x\r\nUpgrade: websocket\r\n"
          b"Connection: Upgrade\r\nSec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==\r\n"
          b"Sec-WebSocket-Version: 13\r\n\r\n")
time.sleep(0.1)
resp = s.recv(1024).decode("latin-1")
assert "101" in resp and "s3pPLMBiTxaQ9kYGzzhZRbK+xOo=" in resp, "bad handshake"

with open(f"{tmp}/events.jsonl", "a", encoding="utf-8") as fh:
    fh.write('{"new_nodes":["live1"],"new_edges":[],"edge_origins":{}}\n')

s.settimeout(5)
frame = s.recv(4096)
assert frame[0] == 0x81, "not a text frame"
payload = frame[2:] if frame[1] < 126 else frame[4:]
assert json.loads(payload.decode("utf-8"))["new_nodes"] == ["live1"], "delta not received"
s.close()
print("PASS graph view smoke")
PY
```

- [ ] **Step 6: Run the bash smoke**

Run: `bash tests/test_graph_view_smoke.sh`
Expected: `PASS graph view smoke`.

- [ ] **Step 7: Add the README section**

Append to the end of `README.md` as a new top-level section — `## Realtime graph view`, a peer of `## Quickstart` (NOT a `###` subsection of it):

```markdown
## Realtime graph view

Watch the knowledge graph grow live in a browser. The view is read-only and
runs beside the engine — start it whenever you want to watch:

    python3 scripts/graph_view_server.py
    # then open http://127.0.0.1:8000

It seeds from the current `.graphify/graph.json`, then animates each new
`.research/graph-events.jsonl` delta over a WebSocket as ingest cycles land.
AI-asserted edges (sub-project #4) render dashed and tinted, distinct from
corpus-extracted edges. Binds localhost only (unauthenticated). Flags:
`--host --port --events --graph --html` (or `GV_*` env vars).
```

- [ ] **Step 8: Commit**

```bash
git add scripts/graph_view_server.py tests/test_graph_view_server.py tests/test_graph_view_smoke.sh README.md
git commit -m "feat: stdlib WebSocket server streaming live graph deltas"
```

---

### Task 5: Full regression + integrity check

**Files:** none (verification only).

- [ ] **Step 1: Run the whole test suite**

Run:
```bash
python3 -m unittest discover -s tests -p 'test_*.py' -v
for t in tests/test_*.sh; do echo "== $t =="; bash "$t"; done
```
Expected: all Python tests OK; every bash test prints its `PASS` line; no failures.

- [ ] **Step 2: Integrity gate still clean**

Run: `python3 scripts/check_integrity.py`
Expected: no problems reported (the view changes nothing the integrity gate inspects).

- [ ] **Step 3: Discard the side-effect state file if it appeared**

Run: `git status --short`
If `.research/state.json` shows as a new/untracked side effect of running the scripts, do **not** stage it. Leave the working tree otherwise clean.

---

## Self-Review

**Spec coverage:**
- §Components 1 (graph_events enrichment) → Task 1. ✓
- §Components 2 (server: routes, WS upgrade, per-client tail, configurable paths, localhost) → Task 4. ✓
- §Components 3 (cytoscape canvas, WS-first/buffer/seed, snapshot `_origin`, asserted style) → Task 3. ✓
- §Testing (handshake vector, frame short/medium, diff provenance, e2e smoke) → Tasks 1, 2, 4. ✓
- §Conventions (README section, new artifacts) → Task 4 + file list. ✓

**Placeholder scan:** no TBD/TODO; all steps carry concrete code/commands. ✓

**Type consistency:** `ws_accept`/`ws_frame`/`make_server`/`diff`/`append_event`/`edge_origins` named identically across tasks; event keys `new_nodes`/`new_edges`/`edge_origins` consistent between Python and HTML; `_origin` (graph) vs `origin` (cytoscape data field) used deliberately and consistently. ✓
