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


if __name__ == "__main__":
    unittest.main()
