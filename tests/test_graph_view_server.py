import json, socket, struct, sys, tempfile, threading, time, unittest
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

    def test_frame_large_payload(self):
        payload = "x" * 65536
        f = gv.ws_frame(payload)
        self.assertEqual(f[0], 0x81)
        self.assertEqual(f[1], 127)
        self.assertEqual(struct.unpack(">Q", f[2:10])[0], 65536)
        self.assertEqual(f[10:], payload.encode("utf-8"))


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


if __name__ == "__main__":
    unittest.main()
