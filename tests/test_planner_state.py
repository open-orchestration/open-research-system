import os, sys, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import state as st


class GoalPlan(unittest.TestCase):
    def test_set_goal_and_plan(self):
        s = st.load_default()
        st.set_goal(s, question="777 vs A380", shape="comparison")
        self.assertEqual(s["goal"]["shape"], "comparison")
        self.assertIn("created_at", s["goal"])
        st.set_plan(s, entities=["777", "A380"],
                    dimensions=[{"name": "fuel", "why": "efficiency"}], topics=[])
        self.assertEqual(s["plan"]["entities"], ["777", "A380"])
        self.assertEqual(s["plan"]["candidate_dimensions"], [])
        self.assertEqual(s["plan"]["rejected_dimensions"], [])


class Candidates(unittest.TestCase):
    def test_candidate_accumulates_independent_evidence(self):
        s = st.load_default()
        st.set_plan(s, entities=["a", "b"], dimensions=[], topics=[])
        st.add_dimension_candidate(s, name="passenger preference", cite="c1", cycle=1)
        st.add_dimension_candidate(s, name="passenger preference", cite="c1", cycle=2)  # dup cite
        st.add_dimension_candidate(s, name="passenger preference", cite="c2", cycle=2)
        c = st.list_candidate_dimensions(s)[0]
        self.assertEqual(c["corroboration"], 2)          # c1 deduped
        self.assertEqual(c["first_seen_cycle"], 1)
        self.assertEqual(c["last_seen_cycle"], 2)

    def test_accept_moves_candidate_to_dimensions(self):
        s = st.load_default()
        st.set_plan(s, entities=["a", "b"], dimensions=[], topics=[])
        st.add_dimension_candidate(s, name="noise", cite="c1", cycle=1)
        d = st.accept_dimension(s, "noise", now="T")
        self.assertEqual(d["name"], "noise")
        self.assertEqual([x["name"] for x in s["plan"]["dimensions"]], ["noise"])
        self.assertEqual(st.list_candidate_dimensions(s), [])
        self.assertEqual(s["plan"]["last_accept_cycle"], 1)

    def test_reject_moves_candidate_to_rejected(self):
        s = st.load_default()
        st.set_plan(s, entities=["a", "b"], dimensions=[], topics=[])
        st.add_dimension_candidate(s, name="weather", cite="c1", cycle=1)
        st.reject_dimension(s, "weather", reason="off-goal", cycle=2)
        self.assertEqual(s["plan"]["rejected_dimensions"][0]["reason"], "off-goal")
        self.assertEqual(st.list_candidate_dimensions(s), [])


if __name__ == "__main__":
    unittest.main()
