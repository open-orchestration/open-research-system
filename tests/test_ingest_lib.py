import unittest, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import ingest_lib as il


class TestDetectType(unittest.TestCase):
    def test_links(self):
        self.assertEqual(il.detect_type("https://example.com/a"), "link")
        self.assertEqual(il.detect_type("source.url"), "link")
        # YouTube is a link here; the flow re-routes it to transcription after reading the URL.
        self.assertEqual(il.detect_type("https://www.youtube.com/watch?v=abc"), "link")

    def test_rawtext(self):
        self.assertEqual(il.detect_type("notes.md"), "rawtext")
        self.assertEqual(il.detect_type("paste.txt"), "rawtext")

    def test_document(self):
        self.assertEqual(il.detect_type("report.pdf"), "document")
        self.assertEqual(il.detect_type("scan.png"), "document")
        self.assertEqual(il.detect_type("clip.mp4"), "document")
        self.assertEqual(il.detect_type("mystery.bin"), "document")


if __name__ == "__main__":
    unittest.main()
