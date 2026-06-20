import unittest
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import state


class TestDraftOps(unittest.TestCase):
    def test_add_draft_assigns_deterministic_id(self):
        st = state.load_default()
        d = state.add_draft(
            st, topic="05-ai", title="Deep research systems",
            path="docs/findings/_drafts/dXXX-deep.md", cites=["c001", "c002"],
            now="2026-06-20T00:00:00+00:00",
        )
        self.assertEqual(d["id"], state.gen_id("d", "05-ai|Deep research systems"))
        self.assertTrue(d["id"].startswith("d"))
        self.assertEqual(d["status"], "draft")
        self.assertEqual(d["cites"], ["c001", "c002"])
        self.assertIsNone(d["promoted_path"])
        self.assertEqual(st["drafts"], [d])

    def test_add_draft_is_idempotent_on_id(self):
        st = state.load_default()
        a = state.add_draft(st, topic="t", title="x", path="p.md", cites=[])
        b = state.add_draft(st, topic="t", title="x", path="p2.md", cites=["c9"])
        self.assertEqual(a["id"], b["id"])
        self.assertEqual(len(st["drafts"]), 1)
        self.assertEqual(st["drafts"][0]["path"], "p.md")  # first write wins

    def test_list_drafts_filters_by_status_and_topic(self):
        st = state.load_default()
        state.add_draft(st, topic="a", title="1", path="1.md", cites=[], status="draft")
        state.add_draft(st, topic="a", title="2", path="2.md", cites=[], status="promoted")
        state.add_draft(st, topic="b", title="3", path="3.md", cites=[], status="draft")
        self.assertEqual(len(state.list_drafts(st)), 3)
        self.assertEqual(len(state.list_drafts(st, status="draft")), 2)
        self.assertEqual(len(state.list_drafts(st, topic="a")), 2)
        self.assertEqual(len(state.list_drafts(st, status="draft", topic="a")), 1)

    def test_get_and_set_draft_status(self):
        st = state.load_default()
        d = state.add_draft(st, topic="t", title="x", path="p.md", cites=[])
        self.assertEqual(state.get_draft(st, d["id"])["id"], d["id"])
        self.assertIsNone(state.get_draft(st, "dffffffff"))
        state.set_draft_status(st, d["id"], "in_review")
        self.assertEqual(state.get_draft(st, d["id"])["status"], "in_review")
        self.assertIsNone(state.set_draft_status(st, "dffffffff", "x"))


class TestCandidates(unittest.TestCase):
    def _corpus(self, st, topic, n):
        for i in range(n):
            state.add_corpus_entry(
                st, title=f"{topic}-{i}", source=f"src://{topic}/{i}", topic=topic,
                native_path=f"ingest/{topic}-{i}.md",
                extracted_path=f"docs/{topic}/sources/{topic}-{i}.md",
                now="2026-06-20T00:00:00+00:00",
            )

    def test_cited_ids_excludes_rejected(self):
        st = state.load_default()
        state.add_draft(st, topic="t", title="ok", path="a.md", cites=["c1"], status="draft")
        state.add_draft(st, topic="t", title="no", path="b.md", cites=["c2"], status="rejected")
        self.assertEqual(state._cited_ids(st), {"c1"})
        self.assertEqual(state._cited_ids(st, exclude_rejected=False), {"c1", "c2"})

    def test_unprocessed_sources_skips_cited(self):
        st = state.load_default()
        self._corpus(st, "05-ai", 3)
        cited_id = st["corpus"][0]["id"]
        state.add_draft(st, topic="05-ai", title="d", path="d.md", cites=[cited_id])
        un = state.unprocessed_sources(st, "05-ai")
        self.assertEqual(len(un), 2)
        self.assertNotIn(cited_id, [e["id"] for e in un])

    def test_process_candidates_empty_in_gather_phase(self):
        st = state.load_default()  # phase defaults to "gather" -> process weight 0.0
        self._corpus(st, "05-ai", 5)
        self.assertEqual(state.process_candidates(st), [])

    def test_process_candidates_ranks_richest_first_when_phase_open(self):
        st = state.load_default()
        state.set_phase(st, "synthesize")
        self._corpus(st, "05-ai", 5)
        self._corpus(st, "06-rag", 3)
        self._corpus(st, "07-orch", 2)  # below min_sources
        self.assertEqual(state.process_candidates(st), [("05-ai", 5), ("06-rag", 3)])

    def test_set_phase_rejects_unknown(self):
        st = state.load_default()
        self.assertEqual(state.set_phase(st, "deepen"), "deepen")
        self.assertEqual(st["budget"]["phase"], "deepen")
        with self.assertRaises(ValueError):
            state.set_phase(st, "bogus")


if __name__ == "__main__":
    unittest.main()
