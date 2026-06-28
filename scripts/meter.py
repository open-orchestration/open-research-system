"""Meter cumulative run tokens from the Claude Code session transcript. Stdlib only.

Primary: sum output_tokens from the transcript JSONL. Fallback: estimate from the
number of subagents dispatched. Never lets the run go unmetered.
"""
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import state as state_mod


def sum_output_tokens(lines, since_iso=None):
    total = 0
    for line in lines:
        line = line.strip()
        if not line:
            continue
        try:
            rec = json.loads(line)
        except json.JSONDecodeError:
            continue
        usage = (rec.get("message") or {}).get("usage") or {}
        out = usage.get("output_tokens")
        if out is None:
            continue
        ts = rec.get("timestamp")
        if since_iso and ts and ts < since_iso:
            continue
        total += out
    return total


def estimate_tokens(subagents_dispatched, avg_output=8000):
    return subagents_dispatched * avg_output


def _discover_transcript():
    """Returns the transcript path if CLAUDE_TRANSCRIPT_PATH is set and the file exists; otherwise None and the caller falls back to estimation."""
    p = os.environ.get("CLAUDE_TRANSCRIPT_PATH")
    return p if p and Path(p).exists() else None


def update_run_spend(root, *, transcript_path=None, started_at=None, subagents_fallback=0):
    path = transcript_path or _discover_transcript()
    if path and Path(path).exists():
        lines = Path(path).read_text(encoding="utf-8").splitlines()
        spent = sum_output_tokens(lines, since_iso=started_at)
    else:
        spent = estimate_tokens(subagents_fallback)
    with state_mod.locked_state(root) as st_:
        cur = st_["budget"].get("run", {}).get("tokens_spent", 0)
        if path and Path(path).exists():
            state_mod.set_run_tokens_spent(st_, spent)
        else:
            state_mod.set_run_tokens_spent(st_, cur + spent)
        spent = st_["budget"]["run"]["tokens_spent"]
    return spent


def _main(argv):
    import argparse
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    u = sub.add_parser("update")
    u.add_argument("--root", default=".")
    u.add_argument("--transcript", default=None)
    u.add_argument("--fallback-subagents", type=int, default=0)
    args = ap.parse_args(argv)
    if args.cmd == "update":
        st_ = state_mod.load(args.root)
        started = st_["budget"].get("run", {}).get("started_at")
        spent = update_run_spend(args.root, transcript_path=args.transcript,
                                 started_at=started, subagents_fallback=args.fallback_subagents)
        print(spent)
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(_main(sys.argv[1:]))
