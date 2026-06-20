import unittest, subprocess, tempfile
from pathlib import Path
import sys
SCRIPTS = Path(__file__).resolve().parent.parent / "scripts"
sys.path.insert(0, str(SCRIPTS))
import state


def _seed_draft(root):
    st = state.load(root)
    drafts_dir = Path(root) / "docs/findings/_drafts"
    drafts_dir.mkdir(parents=True, exist_ok=True)
    did = state.gen_id("d", "05-ai|Deep research")
    fname = f"{did}-deep-research.md"
    (drafts_dir / fname).write_text("# Deep research\n\nclaim [c1a2b3c4d]\n", encoding="utf-8")
    state.add_draft(st, topic="05-ai", title="Deep research",
                    path=f"docs/findings/_drafts/{fname}", cites=["c1a2b3c4d"], id=did)
    state.save(st, root)
    return did, fname


class TestPromoteOps(unittest.TestCase):
    def test_promote_draft_sets_fields(self):
        st = state.load_default()
        d = state.add_draft(st, topic="t", title="x", path="p.md", cites=["c1"])
        out = state.promote_draft(st, d["id"], "docs/findings/p.md",
                                  now="2026-06-20T00:00:00+00:00")
        self.assertEqual(out["status"], "promoted")
        self.assertEqual(out["promoted_path"], "docs/findings/p.md")
        self.assertEqual(out["promoted_at"], "2026-06-20T00:00:00+00:00")
        self.assertIsNone(state.promote_draft(st, "dffffffff", "x"))

    def test_reject_draft_sets_fields(self):
        st = state.load_default()
        d = state.add_draft(st, topic="t", title="x", path="p.md", cites=[])
        out = state.reject_draft(st, d["id"], reason="thin")
        self.assertEqual(out["status"], "rejected")
        self.assertEqual(out["reject_reason"], "thin")


class TestPromoteCLI(unittest.TestCase):
    def _run(self, root, *args):
        return subprocess.run(["python3", str(SCRIPTS / "promote.py"), *args, "--root", root],
                              capture_output=True, text=True)

    def test_promote_moves_file_and_appends_synthesis(self):
        with tempfile.TemporaryDirectory() as d:
            did, fname = _seed_draft(d)
            r = self._run(d, "promote", did)
            self.assertEqual(r.returncode, 0, r.stderr)
            self.assertFalse((Path(d) / "docs/findings/_drafts" / fname).exists())
            self.assertTrue((Path(d) / "docs/findings" / fname).exists())
            syn = (Path(d) / "docs/findings/SYNTHESIS.md").read_text(encoding="utf-8")
            self.assertIn(fname, syn)
            self.assertIn("Deep research", syn)
            st = state.load(d)
            self.assertEqual(state.get_draft(st, did)["status"], "promoted")

    def test_promote_unknown_id_fails(self):
        with tempfile.TemporaryDirectory() as d:
            r = self._run(d, "promote", "dffffffff")
            self.assertEqual(r.returncode, 1)

    def test_reject_leaves_file_and_flips_status(self):
        with tempfile.TemporaryDirectory() as d:
            did, fname = _seed_draft(d)
            r = self._run(d, "reject", did, "--reason", "thin")
            self.assertEqual(r.returncode, 0)
            self.assertTrue((Path(d) / "docs/findings/_drafts" / fname).exists())
            st = state.load(d)
            self.assertEqual(state.get_draft(st, did)["status"], "rejected")

    def test_queue_lists_review_ready(self):
        with tempfile.TemporaryDirectory() as d:
            did, _ = _seed_draft(d)
            self.assertIn(did, self._run(d, "queue").stdout)


if __name__ == "__main__":
    unittest.main()
