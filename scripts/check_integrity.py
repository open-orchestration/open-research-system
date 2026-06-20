"""Integrity lint for the state spine. Stdlib only."""
import json
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import state as state_mod
import assertions as assertions_mod

REQUIRED_KEYS = ("budget", "gaps", "inbox", "corpus", "graph", "assertions", "drafts")


def check(root="."):
    problems = []
    p = state_mod.state_path(root)
    if not p.exists():
        return []
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
    corpus_ids = {e.get("id") for e in st.get("corpus", [])}
    for dft in st.get("drafts", []):
        did = dft.get("id")
        if dft.get("status") != "promoted":
            dp = dft.get("path", "")
            if not (Path(root) / dp).exists():
                problems.append(f"draft {did} missing file: {dp}")
        for cid in dft.get("cites", []):
            if cid not in corpus_ids:
                problems.append(f"draft {did} dangling cite: {cid}")
    active = assertions_mod.load_overlay(root)
    if active:
        gp = Path(root) / assertions_mod.GRAPH_REL
        node_ids = None
        if gp.exists():
            try:
                graph = json.loads(gp.read_text(encoding="utf-8"))
                node_ids = {n.get("id") for n in graph.get("nodes", [])}
            except json.JSONDecodeError as e:
                problems.append(f"graph.json unreadable: {e}")
                node_ids = None
        for a in active:
            aid = a.get("id")
            if node_ids is not None:
                for endpoint in (a.get("from"), a.get("to")):
                    if endpoint not in node_ids:
                        problems.append(
                            f"assertion {aid} references missing node: {endpoint}")
            for cid in a.get("cites", []):
                if cid not in corpus_ids:
                    problems.append(f"assertion {aid} dangling cite: {cid}")
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
