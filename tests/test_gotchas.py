import os
import sys
import unittest
from tempfile import TemporaryDirectory

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import gotchas


def _finding(check, data, token="", severity="warn"):
    return {"check": check, "data": data, "token": token,
            "severity": severity, "title": check, "symptom": ""}


class Gotchas(unittest.TestCase):
    def test_sig_id_stable_and_distinct(self):
        a = gotchas.sig_id("search_zero_sources", "")
        self.assertEqual(a, gotchas.sig_id("search_zero_sources", ""))
        self.assertTrue(a.startswith("gh") and len(a) == 10)
        self.assertNotEqual(a, gotchas.sig_id("search_zero_sources", "Uh oh"))

    def test_match_honors_check_and_token_substring(self):
        reg = {}
        e, _ = gotchas.record(reg, _finding("c", {"msg": "boom Uh oh"}, token="Uh oh"))
        self.assertIsNotNone(gotchas.match(reg, _finding("c", {"msg": "x Uh oh y"})))
        self.assertIsNone(gotchas.match(reg, _finding("c", {"msg": "clean"})))
        self.assertIsNone(gotchas.match(reg, _finding("other", {"msg": "Uh oh"})))

    def test_empty_token_matches_any_data(self):
        reg = {}
        gotchas.record(reg, _finding("c", {"x": 1}, token=""))
        self.assertIsNotNone(gotchas.match(reg, _finding("c", {"y": 2})))

    def test_record_creates_todo_stub_then_bumps(self):
        reg = {}
        e, is_new = gotchas.record(reg, _finding("c", {"x": 1}), now="t0")
        self.assertTrue(is_new)
        self.assertEqual((e["root_cause"], e["fix"]), ("TODO", "TODO"))
        self.assertEqual(e["occurrences"], 1)
        e2, is_new2 = gotchas.record(reg, _finding("c", {"x": 9}), now="t1")
        self.assertFalse(is_new2)
        self.assertEqual(e2["id"], e["id"])           # dedup by signature
        self.assertEqual(e2["occurrences"], 2)
        self.assertEqual(e2["last_seen"], "t1")
        self.assertEqual(len(reg), 1)

    def test_save_load_round_trip(self):
        with TemporaryDirectory() as d:
            reg = {}
            gotchas.record(reg, _finding("c", {"x": 1}))
            gotchas.save_registry(reg, d)
            again = gotchas.load_registry(d)
            self.assertEqual(set(again), set(reg))


if __name__ == "__main__":
    unittest.main()
