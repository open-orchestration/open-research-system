import json, os, sys, tempfile, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import plan
import state as st


VALID_CMP = {
    "shape": "comparison", "entities": ["777", "A380"],
    "dimensions": [{"name": "fuel", "why": "x"}, {"name": "range", "why": "y"}],
    "topics": [], "seed_gaps": [{"topic": "fuel", "desc": "777 fuel burn"}],
    "rationale": "r",
}


class Validate(unittest.TestCase):
    def test_valid_comparison(self):
        self.assertEqual(plan.validate_plan(VALID_CMP), [])

    def test_bad_shape(self):
        p = dict(VALID_CMP, shape="nonsense")
        self.assertTrue(any("shape" in x for x in plan.validate_plan(p)))

    def test_comparison_needs_entities_and_dimensions(self):
        p = dict(VALID_CMP, entities=[], dimensions=[])
        probs = plan.validate_plan(p)
        self.assertTrue(any("entities" in x for x in probs))
        self.assertTrue(any("dimensions" in x for x in probs))

    def test_survey_needs_topics(self):
        p = {"shape": "survey", "entities": [], "dimensions": [], "topics": [],
             "seed_gaps": [{"topic": "t", "desc": "d"}], "rationale": "r"}
        self.assertTrue(any("topics" in x for x in plan.validate_plan(p)))

    def test_duplicate_dimension_names_rejected(self):
        p = dict(VALID_CMP, dimensions=[{"name": "fuel", "why": "a"},
                                         {"name": "fuel", "why": "b"}])
        self.assertTrue(any("duplicate" in x for x in plan.validate_plan(p)))

    def test_duplicate_topic_names_rejected(self):
        p = {"shape": "survey", "entities": [], "dimensions": [],
             "topics": [{"name": "history", "why": "a"}, {"name": "history", "why": "b"}],
             "seed_gaps": [{"topic": "history", "desc": "d"}], "rationale": "r"}
        self.assertTrue(any("duplicate" in x for x in plan.validate_plan(p)))

    def test_seed_gap_missing_desc_rejected(self):
        p = dict(VALID_CMP, seed_gaps=[{"topic": "fuel"}])   # no desc
        self.assertTrue(any("topic/desc" in x or "desc" in x for x in plan.validate_plan(p)))

    def test_cap_for_budget(self):
        self.assertEqual(plan.cap_for_budget(120000), 4)   # floor is 4
        self.assertEqual(plan.cap_for_budget(2000000), 33)


class Apply(unittest.TestCase):
    def test_apply_writes_goal_plan_gaps_budget(self):
        s = st.load_default()
        res = plan.apply_plan(s, question="777 vs A380", plan=VALID_CMP,
                              budget_tokens=2000000, now="T")
        self.assertEqual(s["goal"]["shape"], "comparison")
        self.assertEqual([d["name"] for d in s["plan"]["dimensions"]], ["fuel", "range"])
        self.assertEqual(res["gaps_seeded"], 1)
        self.assertEqual(len(st.list_gaps(s, status="queued")), 1)
        self.assertEqual(s["budget"]["run"]["token_ceiling"], 2000000)
        self.assertEqual(s["budget"]["dimension_alpha"]["wealth"], 5)

    def test_apply_raises_on_invalid(self):
        s = st.load_default()
        with self.assertRaises(ValueError):
            plan.apply_plan(s, question="q", plan=dict(VALID_CMP, shape="bad"),
                            budget_tokens=1000, now="T")

    def test_seed_cap_limits_gaps(self):
        s = st.load_default()
        big = dict(VALID_CMP, seed_gaps=[{"topic": f"t{i}", "desc": f"d{i}"} for i in range(50)])
        res = plan.apply_plan(s, question="q", plan=big, budget_tokens=120000, now="T")
        self.assertEqual(res["gaps_seeded"], 4)            # cap_for_budget(120000)==4


if __name__ == "__main__":
    unittest.main()
