import json, os, subprocess, sys, tempfile, unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
STATE_PY = str(ROOT / "scripts" / "state.py")

def _add_gap(root, i):
    return subprocess.Popen([sys.executable, STATE_PY, "add-gap", "--root", root,
                             "--topic", f"t{i}", "--desc", f"gap number {i}"],
                            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

class TestLockedState(unittest.TestCase):
    def test_concurrent_add_gap_loses_no_updates(self):
        with tempfile.TemporaryDirectory() as d:
            subprocess.run([sys.executable, STATE_PY, "add-gap", "--root", d,
                            "--topic", "seed", "--desc", "seed gap"], check=True,
                           stdout=subprocess.DEVNULL)
            N = 12
            procs = [_add_gap(d, i) for i in range(N)]
            for p in procs:
                self.assertEqual(p.wait(), 0)
            state = json.loads((Path(d) / ".research" / "state.json").read_text())
            self.assertEqual(len(state["gaps"]), N + 1)  # seed + N, none lost

if __name__ == "__main__":
    unittest.main()
