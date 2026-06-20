"""Integrity lint for the state spine. Stdlib only."""
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import state as state_mod

REQUIRED_KEYS = ("budget", "gaps", "inbox", "corpus", "graph", "drafts")


def check(root="."):
    problems = []
    p = state_mod.state_path(root)
    if not p.exists():
        return ["no state.json found"]
    try:
        st = json.loads(p.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        return [f"state.json unreadable: {e}"]
    for k in REQUIRED_KEYS:
        if k not in st:
            problems.append(f"state.json missing key: {k}")
    seen = set()
    for e in st.get("corpus", []):
        cid = e.get("id")
        if cid in seen:
            problems.append(f"duplicate corpus id: {cid}")
        seen.add(cid)
        ep = e.get("extracted_path", "")
        if not (Path(root) / ep).exists():
            problems.append(f"corpus {cid} missing file: {ep}")
    return problems


def _main(argv):
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    args = ap.parse_args(argv)
    probs = check(args.root)
    for p in probs:
        print("PROBLEM:", p)
    if probs:
        return 1
    print("integrity OK")
    return 0


if __name__ == "__main__":
    sys.exit(_main(sys.argv[1:]))
