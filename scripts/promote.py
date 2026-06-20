"""Human review gate: promote or reject process-flow drafts. Stdlib only."""
import shutil
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import state as state_mod

FINDINGS_DIR = "docs/findings"
SYNTHESIS = "docs/findings/SYNTHESIS.md"


def promote(root, draft_id):
    st = state_mod.load(root)
    d = state_mod.get_draft(st, draft_id)
    if d is None:
        return 1, f"unknown draft: {draft_id}"
    src = Path(root) / d["path"]
    if not src.exists():
        return 1, f"draft file missing: {d['path']}"
    dest_rel = f"{FINDINGS_DIR}/{src.name}"
    dest = Path(root) / dest_rel
    if dest.exists():
        return 1, f"dest already exists: {dest_rel}"
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.move(str(src), str(dest))
    state_mod.promote_draft(st, draft_id, dest_rel)
    syn = Path(root) / SYNTHESIS
    if not syn.exists():
        syn.write_text("# Synthesis — promoted findings\n\n", encoding="utf-8")
    with syn.open("a", encoding="utf-8") as f:
        f.write(f"- [{d['title']}]({src.name}) — {d['topic']}\n")
    state_mod.save(st, root)
    return 0, f"promoted {draft_id} -> {dest_rel}"


def reject(root, draft_id, reason=None):
    st = state_mod.load(root)
    if state_mod.reject_draft(st, draft_id, reason) is None:
        return 1, f"unknown draft: {draft_id}"
    state_mod.save(st, root)
    return 0, f"rejected {draft_id}"


def _main(argv):
    import argparse
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("promote"); p.add_argument("draft_id"); p.add_argument("--root", default=".")
    r = sub.add_parser("reject"); r.add_argument("draft_id"); r.add_argument("--root", default=".")
    r.add_argument("--reason", default=None)
    q = sub.add_parser("queue"); q.add_argument("--root", default=".")
    args = ap.parse_args(argv)
    if args.cmd == "promote":
        code, msg = promote(args.root, args.draft_id)
    elif args.cmd == "reject":
        code, msg = reject(args.root, args.draft_id, args.reason)
    else:  # queue
        for d in state_mod.list_drafts(state_mod.load(args.root), status="draft"):
            print(f"{d['id']}\t{d['topic']}\t{d['title']}")
        return 0
    if code == 0:
        print(msg)
    else:
        print(msg, file=sys.stderr)
    return code


if __name__ == "__main__":
    sys.exit(_main(sys.argv[1:]))
