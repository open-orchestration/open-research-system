"""Asserted-edge overlay for the knowledge graph. Stdlib only.

The overlay (.research/graph-assertions.jsonl) is append-only and committed.
Each active line is an asserted edge; a `{"id": ..., "pruned": true}` line is a
tombstone that retires an earlier id (last-write-wins). Replay (Task 2) projects
the active set into graph.json's `links` array.
"""
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import state as state_mod

OVERLAY_REL = ".research/graph-assertions.jsonl"
GRAPH_REL = ".graphify/graph.json"
RELATIONS = ("bridges", "supports", "contradicts", "refines")


def overlay_path(root="."):
    return Path(root) / OVERLAY_REL


def load_overlay(root="."):
    p = overlay_path(root)
    if not p.exists():
        return []
    by_id = {}
    for line in p.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            rec = json.loads(line)
        except json.JSONDecodeError:
            continue
        rid = rec.get("id")
        if rid is None:
            continue
        by_id[rid] = rec  # last-write-wins
    return [r for r in by_id.values() if not r.get("pruned")]


def _append_line(root, rec):
    p = overlay_path(root)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(rec, ensure_ascii=False) + "\n")


def sync_count(root="."):
    st = state_mod.load(root)
    n = len(load_overlay(root))
    st["assertions"]["count"] = n
    st["assertions"]["file"] = OVERLAY_REL
    state_mod.save(st, root)
    return n


def add_assertion(root=".", *, frm, to, relation, rationale, cites,
                  author="ai", confidence=0.8, id=None, now=None):
    if relation not in RELATIONS:
        raise ValueError(f"unknown relation: {relation} (allowed: {RELATIONS})")
    st = state_mod.load(root)
    corpus_ids = {e["id"] for e in st["corpus"]}
    for cid in cites:
        if cid not in corpus_ids:
            raise ValueError(f"dangling cite: {cid}")
    aid = id or state_mod.gen_id("a", frm + "|" + to + "|" + relation)
    rec = {
        "id": aid, "from": frm, "to": to, "relation": relation,
        "rationale": rationale, "cites": list(cites), "author": author,
        "confidence": confidence, "created_at": now or state_mod._now(),
    }
    _append_line(root, rec)
    sync_count(root)
    return rec


def prune_assertion(root=".", assertion_id=None, now=None):
    active = {r["id"] for r in load_overlay(root)}
    existed = assertion_id in active
    if existed:
        _append_line(root, {"id": assertion_id, "pruned": True,
                            "pruned_at": now or state_mod._now()})
        sync_count(root)
    return existed


def _asserted_link(rec):
    return {
        "source": rec.get("from"), "target": rec.get("to"),
        "relation": rec.get("relation"), "weight": 1.0, "_origin": "asserted",
        "assertion_id": rec["id"], "rationale": rec.get("rationale", ""),
        "cites": rec.get("cites", []), "author": rec.get("author", "ai"),
        "confidence": rec.get("confidence"),
    }


def replay(root=".", graph_path=None):
    gp = Path(graph_path) if graph_path else Path(root) / GRAPH_REL
    if not gp.exists():
        return {"asserted": 0, "stripped": 0, "skipped": f"no graph at {gp}"}
    graph = json.loads(gp.read_text(encoding="utf-8"))
    links = graph.get("links", [])
    kept = [l for l in links if l.get("_origin") != "asserted"]
    stripped = len(links) - len(kept)
    active = [r for r in load_overlay(root)
              if r.get("from") and r.get("to") and r.get("relation")]
    graph["links"] = kept + [_asserted_link(r) for r in active]
    tmp = gp.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(graph, ensure_ascii=False), encoding="utf-8")
    os.replace(tmp, gp)
    return {"asserted": len(active), "stripped": stripped, "skipped": None}


def _main(argv):
    import argparse
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)

    a = sub.add_parser("add")
    a.add_argument("--root", default=".")
    a.add_argument("--from", dest="frm", required=True)
    a.add_argument("--to", required=True)
    a.add_argument("--relation", required=True)
    a.add_argument("--rationale", required=True)
    a.add_argument("--cites", required=True, help="comma-separated corpus ids")
    a.add_argument("--author", default="ai")
    a.add_argument("--confidence", type=float, default=0.8)
    a.add_argument("--id", default=None)

    pr = sub.add_parser("prune")
    pr.add_argument("--root", default=".")
    pr.add_argument("id")

    li = sub.add_parser("list")
    li.add_argument("--root", default=".")

    rp = sub.add_parser("replay")
    rp.add_argument("--root", default=".")
    rp.add_argument("--graph", default=None)

    args = ap.parse_args(argv)
    if args.cmd == "add":
        cites = [c for c in args.cites.split(",") if c]
        rec = add_assertion(root=args.root, frm=args.frm, to=args.to,
                            relation=args.relation, rationale=args.rationale,
                            cites=cites, author=args.author,
                            confidence=args.confidence, id=args.id)
        print(rec["id"])
        return 0
    if args.cmd == "prune":
        ok = prune_assertion(root=args.root, assertion_id=args.id)
        print("pruned" if ok else "no such active assertion")
        return 0
    if args.cmd == "list":
        for r in load_overlay(args.root):
            print(f"{r['id']} {r['relation']} {r['from']} -> {r['to']}")
        return 0
    if args.cmd == "replay":
        res = replay(root=args.root, graph_path=args.graph)
        if res["skipped"]:
            print(res["skipped"])
        else:
            print(f"replayed: +{res['asserted']} asserted links "
                  f"(stripped {res['stripped']})")
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(_main(sys.argv[1:]))
