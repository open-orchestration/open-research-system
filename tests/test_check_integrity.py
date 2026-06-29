import json, tempfile, unittest, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import check_integrity as ci
import assertions
import state as state_mod


def _write_state(root, corpus):
    p = Path(root) / ".research"; p.mkdir(parents=True, exist_ok=True)
    base = {"budget": {}, "gaps": [], "inbox": [], "corpus": corpus,
            "graph": {}, "assertions": {}, "drafts": []}
    (p / "state.json").write_text(json.dumps(base), encoding="utf-8")


def _write_state_drafts(root, corpus, drafts):
    p = Path(root) / ".research"; p.mkdir(parents=True, exist_ok=True)
    base = {"budget": {}, "gaps": [], "inbox": [], "corpus": corpus,
            "graph": {}, "assertions": {}, "drafts": drafts}
    (p / "state.json").write_text(json.dumps(base), encoding="utf-8")


class TestIntegrity(unittest.TestCase):
    def test_absent_state_is_healthy(self):
        with tempfile.TemporaryDirectory() as t:
            self.assertEqual(ci.check(t), [])

    def test_healthy_when_files_exist(self):
        with tempfile.TemporaryDirectory() as t:
            (Path(t) / ".research/docs").mkdir(parents=True)
            (Path(t) / ".research/docs/x.md").write_text("hi", encoding="utf-8")
            _write_state(t, [{"id": "c1", "extracted_path": ".research/docs/x.md"}])
            self.assertEqual(ci.check(t), [])

    def test_flags_missing_file(self):
        with tempfile.TemporaryDirectory() as t:
            _write_state(t, [{"id": "c1", "extracted_path": ".research/docs/missing.md"}])
            probs = ci.check(t)
            self.assertTrue(any("missing.md" in p for p in probs))

    def test_flags_duplicate_id(self):
        with tempfile.TemporaryDirectory() as t:
            (Path(t) / ".research/docs").mkdir(parents=True)
            (Path(t) / ".research/docs/x.md").write_text("hi", encoding="utf-8")
            _write_state(t, [{"id": "c1", "extracted_path": ".research/docs/x.md"},
                             {"id": "c1", "extracted_path": ".research/docs/x.md"}])
            self.assertTrue(any("duplicate" in p.lower() for p in ci.check(t)))

    def test_flags_dangling_draft_cite(self):
        with tempfile.TemporaryDirectory() as t:
            drafts = Path(t) / ".research/docs/findings/_drafts"; drafts.mkdir(parents=True)
            (drafts / "dX.md").write_text("x [cffffffff]", encoding="utf-8")
            _write_state_drafts(t, [], [{"id": "dX", "status": "draft",
                "path": ".research/docs/findings/_drafts/dX.md", "cites": ["cffffffff"]}])
            probs = ci.check(t)
            self.assertTrue(any("dangling cite: cffffffff" in p for p in probs))

    def test_flags_missing_draft_file(self):
        with tempfile.TemporaryDirectory() as t:
            _write_state_drafts(t, [], [{"id": "dG", "status": "draft",
                "path": ".research/docs/findings/_drafts/gone.md", "cites": []}])
            probs = ci.check(t)
            self.assertTrue(any("dG missing file" in p for p in probs))

    def test_promoted_draft_skips_file_check(self):
        with tempfile.TemporaryDirectory() as t:
            _write_state_drafts(t, [], [{"id": "dP", "status": "promoted",
                "path": ".research/docs/findings/_drafts/moved.md", "cites": []}])
            self.assertEqual(ci.check(t), [])

    def test_flags_dangling_candidate_dimension_cite(self):
        with tempfile.TemporaryDirectory() as t:
            p = Path(t) / ".research"; p.mkdir(parents=True, exist_ok=True)
            base = {"budget": {}, "gaps": [], "inbox": [], "corpus": [],
                    "graph": {}, "assertions": {}, "drafts": [],
                    "plan": {"entities": [], "dimensions": [], "topics": [],
                             "candidate_dimensions": [
                                 {"name": "x", "evidence_cites": ["cNOPE"], "corroboration": 1}],
                             "rejected_dimensions": []}}
            (p / "state.json").write_text(json.dumps(base), encoding="utf-8")
            self.assertTrue(any("cNOPE" in x for x in ci.check(t)))

    def test_clean_when_candidate_cite_resolves(self):
        with tempfile.TemporaryDirectory() as t:
            (Path(t) / ".research/docs").mkdir(parents=True)
            (Path(t) / ".research/docs/x.md").write_text("hi", encoding="utf-8")
            p = Path(t) / ".research"; p.mkdir(parents=True, exist_ok=True)
            base = {"budget": {}, "gaps": [], "inbox": [],
                    "corpus": [{"id": "cREAL", "extracted_path": ".research/docs/x.md"}],
                    "graph": {}, "assertions": {}, "drafts": [],
                    "plan": {"entities": [], "dimensions": [], "topics": [],
                             "candidate_dimensions": [
                                 {"name": "x", "evidence_cites": ["cREAL"], "corroboration": 1}],
                             "rejected_dimensions": []}}
            (p / "state.json").write_text(json.dumps(base), encoding="utf-8")
            self.assertEqual(ci.check(t), [])


class AssertionIntegrity(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        st = state_mod.load(self.tmp)
        st["corpus"].append({
            "id": "c0000aaaa", "title": "t", "source": "s", "topic": "t",
            "lifecycle": "active", "native_path": "n",
            "extracted_path": "e.md", "lossy": False, "ingested_at": "now",
        })
        (Path(self.tmp) / "e.md").write_text("x", encoding="utf-8")
        state_mod.save(st, self.tmp)
        gp = Path(self.tmp) / ".graphify" / "graph.json"
        gp.parent.mkdir(parents=True, exist_ok=True)
        gp.write_text(json.dumps({
            "nodes": [{"id": "node_x"}, {"id": "node_y"}], "links": [],
        }), encoding="utf-8")

    def test_clean_assertion_passes(self):
        assertions.add_assertion(
            root=self.tmp, frm="node_x", to="node_y", relation="bridges",
            rationale="r", cites=["c0000aaaa"])
        self.assertEqual(ci.check(self.tmp), [])

    def test_missing_node_flagged(self):
        assertions.add_assertion(
            root=self.tmp, frm="node_x", to="ghost", relation="bridges",
            rationale="r", cites=["c0000aaaa"])
        probs = ci.check(self.tmp)
        self.assertTrue(any("missing node: ghost" in p for p in probs))

    def test_node_check_skipped_without_graph(self):
        (Path(self.tmp) / ".graphify" / "graph.json").unlink()
        assertions.add_assertion(
            root=self.tmp, frm="node_x", to="ghost", relation="bridges",
            rationale="r", cites=["c0000aaaa"])
        probs = ci.check(self.tmp)
        self.assertFalse(any("missing node" in p for p in probs))

    def test_dangling_cite_flagged(self):
        line = json.dumps({"id": "a0000dead", "from": "node_x", "to": "node_y",
                           "relation": "bridges", "rationale": "r",
                           "cites": ["c9999dead"], "author": "ai",
                           "confidence": 0.8, "created_at": "now"})
        op = assertions.overlay_path(self.tmp)
        op.parent.mkdir(parents=True, exist_ok=True)
        op.write_text(line + "\n", encoding="utf-8")
        probs = ci.check(self.tmp)
        self.assertTrue(any("dangling cite: c9999dead" in p for p in probs))

    def test_corrupt_graph_reported_not_crashed(self):
        (Path(self.tmp) / ".graphify" / "graph.json").write_text(
            "{ this is not json", encoding="utf-8")
        assertions.add_assertion(
            root=self.tmp, frm="node_x", to="node_y", relation="bridges",
            rationale="r", cites=["c0000aaaa"])
        probs = ci.check(self.tmp)  # must not raise
        self.assertTrue(any("graph.json unreadable" in p for p in probs))


if __name__ == "__main__":
    unittest.main()
