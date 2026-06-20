import json, tempfile, unittest
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import state


class TestStateCore(unittest.TestCase):
    def test_gen_id_is_deterministic_and_prefixed(self):
        a = state.gen_id("c", "https://example.com/x")
        b = state.gen_id("c", "https://example.com/x")
        self.assertEqual(a, b)
        self.assertTrue(a.startswith("c"))
        self.assertEqual(len(a), 9)  # 1 prefix + 8 hex

    def test_gen_id_differs_by_seed(self):
        self.assertNotEqual(state.gen_id("c", "a"), state.gen_id("c", "b"))

    def test_load_seeds_when_missing(self):
        with tempfile.TemporaryDirectory() as d:
            st = state.load(d)
            self.assertIn("budget", st)
            self.assertEqual(st["corpus"], [])
            self.assertTrue((Path(d) / ".research/state.json").exists())

    def test_save_then_load_roundtrips(self):
        with tempfile.TemporaryDirectory() as d:
            st = state.load(d)
            st["corpus"].append({"id": "c001"})
            state.save(st, d)
            again = state.load(d)
            self.assertEqual(again["corpus"], [{"id": "c001"}])

    def test_add_corpus_assigns_deterministic_id_and_sets_dirty(self):
        st = state.load_default()
        e = state.add_corpus_entry(
            st, title="T", source="src://a", topic="11-x",
            native_path="ingest/a.md", extracted_path="docs/11-x/sources/cXXXX-t.md",
            now="2026-06-19T00:00:00+00:00",
        )
        self.assertEqual(e["id"], state.gen_id("c", "src://a"))
        self.assertEqual(e["lifecycle"], "active")
        self.assertTrue(st["graph"]["dirty"])
        self.assertEqual(len(st["corpus"]), 1)

    def test_add_corpus_is_idempotent(self):
        st = state.load_default()
        state.add_corpus_entry(st, title="T", source="src://a", topic="11-x",
                               native_path="n", extracted_path="e", now="t")
        state.add_corpus_entry(st, title="T2", source="src://a", topic="11-x",
                               native_path="n", extracted_path="e", now="t")
        self.assertEqual(len(st["corpus"]), 1)  # same source -> same id -> no dup

    def test_set_graph_updates_named_fields_only(self):
        st = state.load_default()
        state.set_graph(st, dirty=False, node_count=42)
        self.assertFalse(st["graph"]["dirty"])
        self.assertEqual(st["graph"]["node_count"], 42)
        self.assertEqual(st["graph"]["edge_count"], 0)


if __name__ == "__main__":
    unittest.main()
