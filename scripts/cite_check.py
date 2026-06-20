"""Validate a draft's inline [corpus_id] citations resolve. Stdlib only."""
import re
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import state as state_mod

_CITE = re.compile(r"\[(c[0-9a-f]{8})\]")


def find_cites(text):
    return _CITE.findall(text)


def check_draft(text, corpus_ids):
    cites = find_cites(text)
    problems = []
    if not cites:
        problems.append("no [corpus_id] citations found")
    for cid in dict.fromkeys(cites):
        if cid not in corpus_ids:
            problems.append(f"dangling citation: {cid}")
    return problems


def _main(argv):
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("draft")
    ap.add_argument("--root", default=".")
    args = ap.parse_args(argv)
    st = state_mod.load(args.root)
    ids = {e["id"] for e in st["corpus"]}
    text = Path(args.draft).read_text(encoding="utf-8", errors="replace")
    probs = check_draft(text, ids)
    for p in probs:
        print("PROBLEM:", p)
    if probs:
        return 1
    print("citations OK")
    return 0


if __name__ == "__main__":
    sys.exit(_main(sys.argv[1:]))
