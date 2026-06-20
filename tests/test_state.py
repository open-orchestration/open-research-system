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
            self.assertTrue(
                {"budget", "gaps", "inbox", "corpus", "graph", "assertions", "drafts"}
                .issubset(st.keys())
            )

    def test_state_path(self):
        self.assertEqual(
            state.state_path("/tmp/x"),
            Path("/tmp/x/.research/state.json"),
        )

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
        self.assertEqual(st["corpus"][0]["title"], "T")

    def test_set_graph_updates_named_fields_only(self):
        st = state.load_default()
        state.set_graph(st, dirty=False, node_count=42)
        self.assertFalse(st["graph"]["dirty"])
        self.assertEqual(st["graph"]["node_count"], 42)
        self.assertEqual(st["graph"]["edge_count"], 0)

    def test_budget_reset_zeroes_spent(self):
        st = state.load_default()
        st["budget"]["spent"]["sources"] = 5
        state.budget_reset(st, now="t")
        self.assertEqual(st["budget"]["spent"], {"tokens": 0, "sources": 0, "cycle_started_at": "t"})

    def test_budget_remaining_sources(self):
        st = state.load_default()
        self.assertEqual(state.budget_remaining_sources(st), 8)  # default sources_per_cycle
        state.budget_spend_source(st, 3)
        self.assertEqual(state.budget_remaining_sources(st), 5)
        state.budget_spend_source(st, 99)
        self.assertEqual(state.budget_remaining_sources(st), 0)  # floored at 0

    def test_subagent_count_follows_phase_weights(self):
        st = state.load_default()  # phase "gather": search 0.7, process 0.0; max_subagents 8
        self.assertEqual(state.subagent_count(st, "search"), 6)   # round(8*0.7)=6 (banker's: round(5.6)=6)
        self.assertEqual(state.subagent_count(st, "process"), 0)
        st["budget"]["phase"] = "synthesize"
        self.assertEqual(state.subagent_count(st, "process"), 6)  # round(8*0.8)=6

    def test_add_gap_dedups_on_topic_desc(self):
        st = state.load_default()
        g1 = state.add_gap(st, topic="06-rag", desc="hybrid retrieval rerank")
        g2 = state.add_gap(st, topic="06-rag", desc="hybrid retrieval rerank")
        self.assertEqual(len(st["gaps"]), 1)
        self.assertEqual(g1["id"], g2["id"])
        self.assertEqual(g1["status"], "queued")
        self.assertEqual(g1["attempts"], 0)

    def test_next_queued_gap_skips_non_queued(self):
        st = state.load_default()
        state.add_gap(st, topic="a", desc="one")
        g2 = state.add_gap(st, topic="b", desc="two")
        st["gaps"][0]["status"] = "done"
        self.assertEqual(state.next_queued_gap(st)["id"], g2["id"])
        self.assertEqual(state.next_queued_gap(st, topic="b")["id"], g2["id"])
        self.assertIsNone(state.next_queued_gap(st, topic="a"))  # a's only gap is done

    def test_set_gap_status_requeue_increments_attempts(self):
        st = state.load_default()
        g = state.add_gap(st, topic="a", desc="one")
        state.set_gap_status(st, g["id"], "x", requeue=True)
        self.assertEqual(st["gaps"][0]["status"], "queued")
        self.assertEqual(st["gaps"][0]["attempts"], 1)
        state.set_gap_status(st, g["id"], "failed")
        self.assertEqual(st["gaps"][0]["status"], "failed")

    def test_list_gaps_filters_by_topic_and_status(self):
        st = state.load_default()
        g1 = state.add_gap(st, topic="a", desc="one")
        g2 = state.add_gap(st, topic="a", desc="two")
        g3 = state.add_gap(st, topic="b", desc="three")
        st["gaps"][1]["status"] = "done"
        all_gaps = state.list_gaps(st)
        self.assertEqual(len(all_gaps), 3)
        by_topic = state.list_gaps(st, topic="a")
        self.assertEqual({g["id"] for g in by_topic}, {g1["id"], g2["id"]})
        by_status = state.list_gaps(st, status="queued")
        self.assertEqual({g["id"] for g in by_status}, {g1["id"], g3["id"]})
        both = state.list_gaps(st, topic="a", status="queued")
        self.assertEqual(len(both), 1)
        self.assertEqual(both[0]["id"], g1["id"])

    def test_budget_spend_leaves_tokens_untouched(self):
        st = state.load_default()
        st["budget"]["spent"]["tokens"] = 42
        state.budget_spend_source(st, 3)
        self.assertEqual(st["budget"]["spent"]["tokens"], 42)
        self.assertEqual(st["budget"]["spent"]["sources"], 3)

    def test_add_gap_id_override(self):
        st = state.load_default()
        g = state.add_gap(st, topic="a", desc="x", id="gFIXED")
        self.assertEqual(g["id"], "gFIXED")
        self.assertEqual(st["gaps"][0]["id"], "gFIXED")


if __name__ == "__main__":
    unittest.main()
