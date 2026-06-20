import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import assertions
import state as state_mod


def _seed_corpus(root, ids):
    st = state_mod.load(root)
    for cid in ids:
        st["corpus"].append({
            "id": cid, "title": cid, "source": cid, "topic": "t",
            "lifecycle": "active", "native_path": "n", "extracted_path": "e",
            "lossy": False, "ingested_at": "now",
        })
    state_mod.save(st, root)


class AddAndLoad(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        _seed_corpus(self.tmp, ["c0000aaaa", "c0000bbbb"])

    def test_add_appends_active_assertion_with_durable_id(self):
        a = assertions.add_assertion(
            root=self.tmp, frm="node_x", to="node_y", relation="bridges",
            rationale="both describe provenance", cites=["c0000aaaa"],
        )
        self.assertEqual(a["id"], state_mod.gen_id("a", "node_x|node_y|bridges"))
        self.assertTrue(a["id"].startswith("a"))
        self.assertEqual(len(a["id"]), 9)
        loaded = assertions.load_overlay(root=self.tmp)
        self.assertEqual([x["id"] for x in loaded], [a["id"]])
        self.assertEqual(loaded[0]["relation"], "bridges")
        self.assertEqual(loaded[0]["author"], "ai")
        self.assertEqual(loaded[0]["confidence"], 0.8)

    def test_add_rejects_unknown_relation(self):
        with self.assertRaises(ValueError):
            assertions.add_assertion(
                root=self.tmp, frm="a", to="b", relation="causes",
                rationale="r", cites=["c0000aaaa"])

    def test_add_rejects_dangling_cite(self):
        with self.assertRaises(ValueError):
            assertions.add_assertion(
                root=self.tmp, frm="a", to="b", relation="supports",
                rationale="r", cites=["c9999dead"])

    def test_count_synced_into_state(self):
        assertions.add_assertion(
            root=self.tmp, frm="a", to="b", relation="bridges",
            rationale="r", cites=["c0000aaaa"])
        st = state_mod.load(self.tmp)
        self.assertEqual(st["assertions"]["count"], 1)


class Prune(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        _seed_corpus(self.tmp, ["c0000aaaa"])

    def test_prune_removes_from_active_set_but_file_stays_append_only(self):
        a = assertions.add_assertion(
            root=self.tmp, frm="a", to="b", relation="bridges",
            rationale="r", cites=["c0000aaaa"])
        lines_before = assertions.overlay_path(self.tmp).read_text().count("\n")
        ok = assertions.prune_assertion(root=self.tmp, assertion_id=a["id"])
        self.assertTrue(ok)
        self.assertEqual(assertions.load_overlay(root=self.tmp), [])
        lines_after = assertions.overlay_path(self.tmp).read_text().count("\n")
        self.assertEqual(lines_after, lines_before + 1)  # tombstone appended, nothing deleted
        st = state_mod.load(self.tmp)
        self.assertEqual(st["assertions"]["count"], 0)

    def test_readd_after_prune_reactivates(self):
        a = assertions.add_assertion(
            root=self.tmp, frm="a", to="b", relation="bridges",
            rationale="r", cites=["c0000aaaa"])
        assertions.prune_assertion(root=self.tmp, assertion_id=a["id"])
        assertions.add_assertion(
            root=self.tmp, frm="a", to="b", relation="bridges",
            rationale="r2", cites=["c0000aaaa"])
        loaded = assertions.load_overlay(root=self.tmp)
        self.assertEqual(len(loaded), 1)
        self.assertEqual(loaded[0]["rationale"], "r2")

    def test_prune_unknown_id_is_noop(self):
        path = assertions.overlay_path(self.tmp)
        before = path.read_text() if path.exists() else ""
        ok = assertions.prune_assertion(root=self.tmp, assertion_id="a00000000")
        self.assertFalse(ok)
        after = path.read_text() if path.exists() else ""
        self.assertEqual(before, after)  # nothing appended


class Replay(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        _seed_corpus(self.tmp, ["c0000aaaa"])
        gp = Path(self.tmp) / ".graphify" / "graph.json"
        gp.parent.mkdir(parents=True, exist_ok=True)
        gp.write_text(json.dumps({
            "directed": False, "multigraph": False, "graph": {},
            "nodes": [{"id": "node_x"}, {"id": "node_y"}],
            "links": [{"source": "node_x", "target": "node_y",
                       "relation": "contains", "weight": 1.0}],
        }), encoding="utf-8")
        self.gp = gp

    def _links(self):
        return json.loads(self.gp.read_text())["links"]

    def test_replay_merges_asserted_link_tagged_origin(self):
        a = assertions.add_assertion(
            root=self.tmp, frm="node_x", to="node_y", relation="bridges",
            rationale="r", cites=["c0000aaaa"])
        res = assertions.replay(root=self.tmp)
        self.assertEqual(res["asserted"], 1)
        asserted = [l for l in self._links() if l.get("_origin") == "asserted"]
        self.assertEqual(len(asserted), 1)
        self.assertEqual(asserted[0]["source"], "node_x")
        self.assertEqual(asserted[0]["target"], "node_y")
        self.assertEqual(asserted[0]["assertion_id"], a["id"])
        observed = [l for l in self._links() if l.get("_origin") != "asserted"]
        self.assertEqual(len(observed), 1)  # original observed link preserved

    def test_replay_is_idempotent(self):
        assertions.add_assertion(
            root=self.tmp, frm="node_x", to="node_y", relation="bridges",
            rationale="r", cites=["c0000aaaa"])
        assertions.replay(root=self.tmp)
        first = self._links()
        assertions.replay(root=self.tmp)
        second = self._links()
        self.assertEqual(first, second)
        self.assertEqual(
            len([l for l in second if l.get("_origin") == "asserted"]), 1)

    def test_pruned_assertion_disappears_on_replay(self):
        a = assertions.add_assertion(
            root=self.tmp, frm="node_x", to="node_y", relation="bridges",
            rationale="r", cites=["c0000aaaa"])
        assertions.replay(root=self.tmp)
        assertions.prune_assertion(root=self.tmp, assertion_id=a["id"])
        res = assertions.replay(root=self.tmp)
        self.assertEqual(res["asserted"], 0)
        self.assertEqual(
            [l for l in self._links() if l.get("_origin") == "asserted"], [])

    def test_replay_no_graph_is_noop(self):
        empty = tempfile.mkdtemp()
        res = assertions.replay(root=empty)
        self.assertEqual(res["asserted"], 0)
        self.assertIn("no graph", res["skipped"])


if __name__ == "__main__":
    unittest.main()
