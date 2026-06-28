import os, sys, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import plan


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

    def test_cap_for_budget(self):
        self.assertEqual(plan.cap_for_budget(120000), 4)   # floor is 4
        self.assertEqual(plan.cap_for_budget(2000000), 33)


if __name__ == "__main__":
    unittest.main()
