import os
import sys
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import state as st
import orchestrator as orch


def _corpus(state, topic, n, start=0):
    """Add n corpus entries on `topic` with distinct sources; return their ids."""
    ids = []
    for i in range(start, start + n):
        e = st.add_corpus_entry(
            state, title=f"t{i}", source=f"http://x/{topic}/{i}",
            topic=topic, native_path="n", extracted_path="e",
        )
        ids.append(e["id"])
    return ids


class RecommendPhase(unittest.TestCase):
    def test_gather_when_nothing_processable(self):
        s = st.load_default()
        st.add_gap(s, topic="t", desc="q")          # queued gap, no corpus
        self.assertEqual(orch.recommend_phase(s), "gather")

    def test_deepen_when_processable_but_graph_dirty(self):
        s = st.load_default()
        _corpus(s, "t", 3)                           # add_corpus sets graph.dirty
        self.assertTrue(s["graph"]["dirty"])
        self.assertEqual(orch.recommend_phase(s), "deepen")

    def test_synthesize_when_drained(self):
        s = st.load_default()
        _corpus(s, "t", 3)
        s["graph"]["dirty"] = False                  # graph merged, no queued gaps
        self.assertEqual(orch.recommend_phase(s), "synthesize")

    def test_reopened_gap_flips_synthesize_back_to_deepen(self):
        s = st.load_default()
        _corpus(s, "t", 3)
        s["graph"]["dirty"] = False
        self.assertEqual(orch.recommend_phase(s), "synthesize")
        st.add_gap(s, topic="t", desc="new question")  # process reopens a gap
        self.assertEqual(orch.recommend_phase(s), "deepen")


class GoalMet(unittest.TestCase):
    def test_true_when_synthesize_drained_with_pending_draft(self):
        s = st.load_default()
        ids = _corpus(s, "t", 3)
        s["graph"]["dirty"] = False
        st.add_draft(s, topic="t", title="f", path="p", cites=ids, status="draft")
        self.assertFalse(orch._processable(s, 3))    # all sources now cited
        self.assertTrue(orch.goal_met(s))

    def test_false_when_still_processable(self):
        s = st.load_default()
        _corpus(s, "t", 3)                           # uncited -> processable
        s["graph"]["dirty"] = False
        self.assertFalse(orch.goal_met(s))

    def test_false_when_no_pending_draft(self):
        s = st.load_default()
        ids = _corpus(s, "t", 3)
        s["graph"]["dirty"] = False
        st.add_draft(s, topic="t", title="f", path="p", cites=ids, status="promoted")
        self.assertFalse(orch.goal_met(s))           # draft promoted, none pending


class NextActions(unittest.TestCase):
    def test_search_eligible_in_gather(self):
        s = st.load_default()                        # phase gather, search weight 0.7
        st.add_gap(s, topic="t", desc="q")
        a = orch.next_actions(s)
        self.assertTrue(a["search"])
        self.assertFalse(a["process"])               # process weight 0 in gather

    def test_process_eligible_in_synthesize(self):
        s = st.load_default()
        st.set_phase(s, "synthesize")
        _corpus(s, "t", 3)
        a = orch.next_actions(s)
        self.assertTrue(a["process"])
        self.assertFalse(a["search"])                # no queued gaps


class Decide(unittest.TestCase):
    def test_apply_flips_phase(self):
        s = st.load_default()                        # phase gather
        _corpus(s, "t", 3)
        s["graph"]["dirty"] = False
        res = orch.decide(s, apply=True)
        self.assertEqual(res["phase"], "synthesize")
        self.assertTrue(res["phase_changed"])
        self.assertEqual(s["budget"]["phase"], "synthesize")

    def test_dry_run_restores_phase(self):
        s = st.load_default()
        _corpus(s, "t", 3)
        s["graph"]["dirty"] = False
        res = orch.decide(s, apply=False)
        self.assertEqual(res["phase"], "synthesize")
        self.assertEqual(s["budget"]["phase"], "gather")   # not persisted


class BudgetAndDimensions(unittest.TestCase):
    def _drained_with_draft(self):
        s = st.load_default()
        ids = _corpus(s, "t", 3)
        s["graph"]["dirty"] = False
        st.add_draft(s, topic="t", title="f", path="p", cites=ids, status="draft")
        return s

    def test_budget_exhausted_sets_stop(self):
        s = self._drained_with_draft()
        st.init_run_budget(s, token_ceiling=100, now="T")
        st.set_run_tokens_spent(s, 100)
        res = orch.decide(s, apply=False)
        self.assertTrue(res["budget_exhausted"])
        self.assertTrue(res["stop"])

    def test_accept_eligible_blocks_goal_met(self):
        s = self._drained_with_draft()
        st.init_dimension_alpha(s, wealth=5)
        st.set_plan(s, entities=["a", "b"], dimensions=[], topics=[])
        for cy in (1, 2, 3):                              # 3 independent sources => corrob 3 >= K 3
            st.add_dimension_candidate(s, name="pref", cite=f"c{cy}", cycle=cy)
        self.assertTrue(orch.accept_eligible(s))
        self.assertFalse(orch.goal_met(s))               # eligible candidate blocks plateau

    def test_goal_met_when_no_eligible_candidates(self):
        s = self._drained_with_draft()
        st.init_dimension_alpha(s, wealth=5)
        st.set_plan(s, entities=["a", "b"], dimensions=[], topics=[])
        st.add_dimension_candidate(s, name="pref", cite="c1", cycle=1)  # corrob 1 < K 3
        self.assertFalse(orch.accept_eligible(s))
        self.assertTrue(orch.goal_met(s))

    def test_accept_eligible_empty_on_default_state(self):
        self.assertEqual(orch.accept_eligible(st.load_default()), [])  # legacy state: no plan/alpha

    def test_stop_true_when_both_goal_met_and_budget_exhausted(self):
        s = self._drained_with_draft()
        st.init_run_budget(s, token_ceiling=100, now="T")
        st.set_run_tokens_spent(s, 100)
        res = orch.decide(s, apply=False)
        self.assertTrue(res["goal_met"])
        self.assertTrue(res["budget_exhausted"])
        self.assertTrue(res["stop"])


if __name__ == "__main__":
    unittest.main()
