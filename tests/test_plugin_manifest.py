import json, os, re, unittest
ROOT = os.path.join(os.path.dirname(__file__), "..")


class Manifest(unittest.TestCase):
    def test_manifest_valid(self):
        with open(os.path.join(ROOT, ".claude-plugin/plugin.json")) as f:
            m = json.load(f)
        self.assertEqual(m["name"], "ors")
        self.assertTrue(m.get("description"))

    def test_flows_have_no_raw_script_calls(self):
        d = os.path.join(ROOT, "skills/_flows")
        for fn in ("goal.md", "loop.md", "process.md", "review.md"):
            with open(os.path.join(d, fn)) as f:
                txt = f.read()
            self.assertNotRegex(txt, r"python3 scripts/", fn)
            self.assertNotRegex(txt, r"bash scripts/", fn)

    def test_user_skills_frontmatter(self):
        for name in ("research", "report", "dashboard"):
            p = os.path.join(ROOT, "skills", name, "SKILL.md")
            with open(p) as f:
                txt = f.read()
            self.assertTrue(txt.startswith("---"), name)
            fm = txt.split("---", 2)[1]
            self.assertRegex(fm, r"name:\s*\S")
            self.assertRegex(fm, r"description:\s*\S")
            self.assertRegex(fm, r"disable-model-invocation:\s*true")
            self.assertNotRegex(txt, r"python3 scripts/")
            self.assertNotRegex(txt, r"bash scripts/")


if __name__ == "__main__":
    unittest.main()
