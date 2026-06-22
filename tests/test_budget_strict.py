import json, subprocess, sys, tempfile, unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STATE_PY = str(ROOT / "scripts" / "state.py")

def _seed(d):
    subprocess.run([sys.executable, STATE_PY, "budget-reset", "--root", d],
                   check=True, stdout=subprocess.DEVNULL)

class TestStrictBudget(unittest.TestCase):
    def test_concurrent_reserve_never_exceeds_cap(self):
        with tempfile.TemporaryDirectory() as d:
            _seed(d)  # sources_per_cycle defaults to 8, spent.sources = 0
            procs = [subprocess.Popen([sys.executable, STATE_PY, "budget-reserve",
                                       "--root", d, "--sources", "1"],
                                      stdout=subprocess.PIPE, text=True) for _ in range(12)]
            grants = [int(p.communicate()[0].strip() or 0) for p in procs]
            self.assertEqual(sum(grants), 8)            # exactly the cap granted
            st = json.loads((Path(d) / ".research" / "state.json").read_text())
            self.assertEqual(st["budget"]["spent"]["sources"], 8)  # never exceeded

    def test_refund_round_trips_and_clamps(self):
        with tempfile.TemporaryDirectory() as d:
            _seed(d)
            g = subprocess.run([sys.executable, STATE_PY, "budget-reserve", "--root", d,
                                "--sources", "3"], capture_output=True, text=True)
            self.assertEqual(g.stdout.strip(), "3")
            subprocess.run([sys.executable, STATE_PY, "budget-refund", "--root", d,
                            "--sources", "5"], check=True, stdout=subprocess.DEVNULL)  # over-refund
            st = json.loads((Path(d) / ".research" / "state.json").read_text())
            self.assertEqual(st["budget"]["spent"]["sources"], 0)  # clamped at 0

    def test_status_reports_max_workers_default(self):
        with tempfile.TemporaryDirectory() as d:
            _seed(d)
            out = subprocess.run([sys.executable, STATE_PY, "budget-status", "--root", d],
                                 capture_output=True, text=True).stdout
            self.assertEqual(json.loads(out)["max_workers"], 4)

if __name__ == "__main__":
    unittest.main()
