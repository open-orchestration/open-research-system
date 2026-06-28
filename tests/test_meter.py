import os, sys, unittest, tempfile
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import meter
import state as st


class SumTokens(unittest.TestCase):
    def test_sums_output_tokens(self):
        lines = [
            '{"timestamp":"2026-06-28T01:00:00Z","message":{"usage":{"output_tokens":100}}}',
            '{"timestamp":"2026-06-28T02:00:00Z","message":{"usage":{"output_tokens":250}}}',
            'not json',                                   # ignored
            '{"message":{"role":"user"}}',                # no usage, ignored
        ]
        self.assertEqual(meter.sum_output_tokens(lines), 350)

    def test_since_filter(self):
        lines = [
            '{"timestamp":"2026-06-28T01:00:00Z","message":{"usage":{"output_tokens":100}}}',
            '{"timestamp":"2026-06-28T03:00:00Z","message":{"usage":{"output_tokens":250}}}',
        ]
        self.assertEqual(meter.sum_output_tokens(lines, since_iso="2026-06-28T02:00:00Z"), 250)

    def test_estimate_fallback(self):
        self.assertEqual(meter.estimate_tokens(3, avg_output=8000), 24000)


class UpdateRunSpend(unittest.TestCase):
    def _root(self, d):
        s = st.load(d)
        st.init_run_budget(s, token_ceiling=10**9, now="T")
        st.save(s, d)

    def test_transcript_spend_is_absolute(self):
        with tempfile.TemporaryDirectory() as d:
            self._root(d)
            tp = os.path.join(d, "t.jsonl")
            with open(tp, "w") as f:
                f.write('{"timestamp":"2026-06-28T01:00:00Z","message":{"usage":{"output_tokens":500}}}\n')
            self.assertEqual(meter.update_run_spend(d, transcript_path=tp), 500)
            self.assertEqual(meter.update_run_spend(d, transcript_path=tp), 500)  # absolute, not 1000

    def test_estimate_spend_is_additive(self):
        with tempfile.TemporaryDirectory() as d:
            self._root(d)
            self.assertEqual(meter.update_run_spend(d, transcript_path="/no/such", subagents_fallback=2), 16000)
            self.assertEqual(meter.update_run_spend(d, transcript_path="/no/such", subagents_fallback=1), 24000)  # additive


if __name__ == "__main__":
    unittest.main()
