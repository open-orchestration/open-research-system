import json, os, re, unittest
ROOT = os.path.join(os.path.dirname(__file__), "..")


class Manifest(unittest.TestCase):
    def test_manifest_valid(self):
        m = json.load(open(os.path.join(ROOT, ".claude-plugin/plugin.json")))
        self.assertEqual(m["name"], "ors")
        self.assertTrue(m.get("description"))

    def test_flows_have_no_raw_script_calls(self):
        d = os.path.join(ROOT, "skills/_flows")
        for fn in ("goal.md", "loop.md", "process.md", "review.md"):
            txt = open(os.path.join(d, fn)).read()
            self.assertNotRegex(txt, r"python3 scripts/", fn)
            self.assertNotRegex(txt, r"bash scripts/", fn)


if __name__ == "__main__":
    unittest.main()
