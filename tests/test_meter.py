import os, sys, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import meter


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


if __name__ == "__main__":
    unittest.main()
