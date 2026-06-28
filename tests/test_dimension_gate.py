import os, sys, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import state as st
import dimension_gate as gate


def _ready(corrob=3, wealth=5):
    s = st.load_default()
    st.set_plan(s, entities=["a", "b"], dimensions=[], topics=[])
    st.init_dimension_alpha(s, wealth=wealth)
    st.init_run_budget(s, token_ceiling=10**9, now="T")
    for i in range(corrob):
        st.add_dimension_candidate(s, name="pref", cite=f"c{i}", cycle=1)
    return s


class Eligible(unittest.TestCase):
    def test_eligible_when_corroborated_and_budget_ok(self):
        self.assertEqual([c["name"] for c in gate.eligible(_ready())], ["pref"])

    def test_not_eligible_when_budget_exhausted(self):
        s = _ready()
        st.set_run_tokens_spent(s, 10**9)
        self.assertEqual(gate.eligible(s), [])

    def test_accept_spends_wealth_and_moves_dimension(self):
        s = _ready()
        gate.accept(s, "pref", now="T")
        self.assertEqual([d["name"] for d in s["plan"]["dimensions"]], ["pref"])
        self.assertEqual(st.dimension_wealth_left(s), 4)

    def test_expire_rejects_stale_uncorroborated(self):
        s = st.load_default()
        st.set_plan(s, entities=["a", "b"], dimensions=[], topics=[])
        st.init_dimension_alpha(s, wealth=5)
        st.add_dimension_candidate(s, name="weak", cite="c1", cycle=1)  # corrob 1
        n = gate.expire(s, current_cycle=4, ttl=3)                      # 4-1>=3
        self.assertEqual(n, 1)
        self.assertEqual(s["plan"]["rejected_dimensions"][0]["name"], "weak")

    def test_accept_unknown_name_is_noop(self):
        s = _ready()
        self.assertIsNone(gate.accept(s, "ghost"))           # not a candidate
        self.assertEqual(st.dimension_wealth_left(s), 5)     # wealth NOT spent on no-op

    def test_stale_but_corroborated_survives_expire(self):
        s = _ready()                                         # "pref" corrob 3, last_seen 1; threshold = 3
        self.assertEqual(gate.expire(s, current_cycle=100), 0)   # stale (100-1>=3) but corrob 3 >= thr 3
        self.assertEqual(len(st.list_candidate_dimensions(s)), 1)  # still pending


if __name__ == "__main__":
    unittest.main()
