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


if __name__ == "__main__":
    unittest.main()
