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
