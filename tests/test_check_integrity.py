import json, tempfile, unittest, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import check_integrity as ci


def _write_state(root, corpus):
    p = Path(root) / ".research"; p.mkdir(parents=True, exist_ok=True)
    base = {"budget": {}, "gaps": [], "inbox": [], "corpus": corpus,
            "graph": {}, "drafts": []}
    (p / "state.json").write_text(json.dumps(base), encoding="utf-8")


class TestIntegrity(unittest.TestCase):
    def test_healthy_when_files_exist(self):
        with tempfile.TemporaryDirectory() as t:
            (Path(t) / "docs").mkdir()
            (Path(t) / "docs/x.md").write_text("hi", encoding="utf-8")
            _write_state(t, [{"id": "c1", "extracted_path": "docs/x.md"}])
            self.assertEqual(ci.check(t), [])

    def test_flags_missing_file(self):
        with tempfile.TemporaryDirectory() as t:
            _write_state(t, [{"id": "c1", "extracted_path": "docs/missing.md"}])
            probs = ci.check(t)
            self.assertTrue(any("missing.md" in p for p in probs))

    def test_flags_duplicate_id(self):
        with tempfile.TemporaryDirectory() as t:
            (Path(t) / "docs").mkdir()
            (Path(t) / "docs/x.md").write_text("hi", encoding="utf-8")
            _write_state(t, [{"id": "c1", "extracted_path": "docs/x.md"},
                             {"id": "c1", "extracted_path": "docs/x.md"}])
            self.assertTrue(any("duplicate" in p.lower() for p in ci.check(t)))


if __name__ == "__main__":
    unittest.main()
