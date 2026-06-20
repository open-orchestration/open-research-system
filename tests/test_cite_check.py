import unittest, subprocess, tempfile
from pathlib import Path
import sys
SCRIPTS = Path(__file__).resolve().parent.parent / "scripts"
sys.path.insert(0, str(SCRIPTS))
import cite_check
import state


class TestCiteCheck(unittest.TestCase):
    def test_find_cites_extracts_markers(self):
        text = "claim one [c1a2b3c4d]. claim two [cdeadbeef]. not a cite [c12]."
        self.assertEqual(cite_check.find_cites(text), ["c1a2b3c4d", "cdeadbeef"])

    def test_check_draft_flags_missing_citations(self):
        self.assertEqual(cite_check.check_draft("no cites here", {"c1a2b3c4d"}),
                         ["no [corpus_id] citations found"])

    def test_check_draft_flags_dangling_once(self):
        text = "a [c1a2b3c4d] b [cffffffff] c [cffffffff]"
        probs = cite_check.check_draft(text, {"c1a2b3c4d"})
        self.assertEqual(probs, ["dangling citation: cffffffff"])

    def test_check_draft_clean(self):
        self.assertEqual(cite_check.check_draft("a [c1a2b3c4d] b [cdeadbeef]",
                                                {"c1a2b3c4d", "cdeadbeef"}), [])

    def test_cli_exit_codes(self):
        with tempfile.TemporaryDirectory() as d:
            st = state.load(d)
            state.add_corpus_entry(st, title="T", source="s", topic="t",
                                   native_path="n.md", extracted_path="e.md", id="c1a2b3c4d")
            state.save(st, d)
            good = Path(d) / "good.md"; good.write_text("claim [c1a2b3c4d]", encoding="utf-8")
            bad = Path(d) / "bad.md"; bad.write_text("claim [cffffffff]", encoding="utf-8")
            r_good = subprocess.run(["python3", str(SCRIPTS / "cite_check.py"),
                                     str(good), "--root", d], capture_output=True, text=True)
            r_bad = subprocess.run(["python3", str(SCRIPTS / "cite_check.py"),
                                    str(bad), "--root", d], capture_output=True, text=True)
            self.assertEqual(r_good.returncode, 0)
            self.assertIn("citations OK", r_good.stdout)
            self.assertEqual(r_bad.returncode, 1)
            self.assertIn("dangling", r_bad.stdout)


if __name__ == "__main__":
    unittest.main()
