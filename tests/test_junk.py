import unittest, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import junk


class TestIsJunk(unittest.TestCase):
    def test_clean_long_content_is_not_junk(self):
        self.assertFalse(junk.is_junk("# Real Article\n\n" + ("word " * 200)))

    def test_empty_is_junk(self):
        self.assertTrue(junk.is_junk(""))
        self.assertTrue(junk.is_junk("   \n  "))

    def test_too_short_is_junk(self):
        self.assertTrue(junk.is_junk("# Title\nthin"))

    def test_js_shell_markers_are_junk(self):
        body = "x" * 300
        self.assertTrue(junk.is_junk("Just a moment... " + body))
        self.assertTrue(junk.is_junk("Please enable JavaScript " + body))
        self.assertTrue(junk.is_junk("Uh oh! There was an error " + body))
        self.assertTrue(junk.is_junk("403 Forbidden " + body))


if __name__ == "__main__":
    unittest.main()
