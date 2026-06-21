import json
import os
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import runlog


def _lines(root):
    p = Path(root) / ".research" / "run.jsonl"
    return [json.loads(x) for x in p.read_text().splitlines() if x.strip()]


class RunLog(unittest.TestCase):
    def test_start_mints_id_and_resets_context(self):
        with TemporaryDirectory() as d:
            rid = runlog.start(d)
            self.assertTrue(rid.startswith("r") and len(rid) == 9)
            recs = _lines(d)
            self.assertEqual(len(recs), 1)
            self.assertEqual(recs[0]["step"], "run_start")
            self.assertEqual(recs[0]["seq"], 0)
            self.assertIn("state", recs[0]["data"])          # baseline snapshot
            ctx = json.loads((Path(d) / ".research" / "run-context.json").read_text())
            self.assertEqual(ctx, {"run_id": rid, "cycle": 0, "seq": 0})

    def test_log_increments_seq_across_separate_calls(self):
        with TemporaryDirectory() as d:
            runlog.start(d)
            runlog.log_event("search", "gather", "ok", {"a": 1}, d)
            runlog.log_event("ingest", "normalize", "ok", {"b": 2}, d)  # fresh ctx read each call
            recs = _lines(d)
            self.assertEqual([r["seq"] for r in recs], [0, 1, 2])
            self.assertEqual(recs[1]["flow"], "search")
            self.assertEqual(recs[2]["data"], {"b": 2})

    def test_set_cycle_tags_subsequent_records(self):
        with TemporaryDirectory() as d:
            runlog.start(d)
            runlog.set_cycle(3, d)
            runlog.log_event("process", "draft", "ok", {}, d)
            self.assertEqual(_lines(d)[-1]["cycle"], 3)

    def test_end_writes_run_end(self):
        with TemporaryDirectory() as d:
            runlog.start(d)
            runlog.end("ok", d)
            last = _lines(d)[-1]
            self.assertEqual(last["step"], "run_end")
            self.assertEqual(last["data"]["status"], "ok")


if __name__ == "__main__":
    unittest.main()
