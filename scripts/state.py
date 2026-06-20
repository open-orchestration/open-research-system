"""On-disk state ledger for the loop research engine. Stdlib only."""
import copy
import hashlib
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

DEFAULT_STATE = {
    "budget": {
        "tokens_per_cycle": 200000,
        "sources_per_cycle": 8,
        "max_subagents": 8,
        "phase": "gather",
        "weights": {
            "gather":     {"search": 0.7, "ingest": 0.3, "process": 0.0},
            "deepen":     {"search": 0.4, "ingest": 0.3, "process": 0.3},
            "synthesize": {"search": 0.1, "ingest": 0.1, "process": 0.8},
        },
        "spent": {"tokens": 0, "sources": 0, "cycle_started_at": None},
    },
    "gaps": [],
    "inbox": [],
    "corpus": [],
    "graph": {"dirty": False, "last_update": None, "node_count": 0, "edge_count": 0},
    "assertions": {"count": 0, "file": ".research/graph-assertions.jsonl"},
    "drafts": [],
}


def state_path(root="."):
    return Path(root) / ".research" / "state.json"


def load(root="."):
    p = state_path(root)
    if not p.exists():
        seed = copy.deepcopy(DEFAULT_STATE)
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(seed, indent=2, ensure_ascii=False), encoding="utf-8")
        return seed
    return json.loads(p.read_text(encoding="utf-8"))


def save(state, root="."):
    p = state_path(root)
    p.parent.mkdir(parents=True, exist_ok=True)
    tmp = p.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(state, indent=2, ensure_ascii=False), encoding="utf-8")
    os.replace(tmp, p)


def gen_id(prefix, seed):
    return prefix + hashlib.sha256(seed.encode("utf-8")).hexdigest()[:8]


def load_default():
    return copy.deepcopy(DEFAULT_STATE)


def _now():
    return datetime.now(timezone.utc).isoformat()


def add_corpus_entry(state, *, title, source, topic, native_path, extracted_path,
                     lossy=False, lifecycle="active", now=None, id=None):
    cid = id or gen_id("c", source)
    for e in state["corpus"]:
        if e["id"] == cid:
            return e
    entry = {
        "id": cid, "title": title, "source": source, "topic": topic,
        "lifecycle": lifecycle, "native_path": native_path,
        "extracted_path": extracted_path, "lossy": lossy,
        "ingested_at": now or _now(),
    }
    state["corpus"].append(entry)
    state["graph"]["dirty"] = True
    return entry


def set_graph(state, *, dirty=None, node_count=None, edge_count=None, last_update=None):
    g = state["graph"]
    if dirty is not None:
        g["dirty"] = dirty
    if node_count is not None:
        g["node_count"] = node_count
    if edge_count is not None:
        g["edge_count"] = edge_count
    if last_update is not None:
        g["last_update"] = last_update


def budget_reset(state, now=None):
    state["budget"]["spent"] = {"tokens": 0, "sources": 0, "cycle_started_at": now or _now()}


def budget_remaining_sources(state):
    b = state["budget"]
    return max(0, b.get("sources_per_cycle", 8) - b["spent"]["sources"])


def budget_spend_source(state, n=1):
    state["budget"]["spent"]["sources"] += n


def subagent_count(state, flow):
    b = state["budget"]
    return round(b["max_subagents"] * b["weights"][b["phase"]][flow])


def add_gap(state, *, topic, desc, origin="human", id=None):
    gid = id or gen_id("g", topic + "|" + desc)
    for g in state["gaps"]:
        if g["id"] == gid:
            return g
    gap = {"id": gid, "topic": topic, "desc": desc, "origin": origin,
           "status": "queued", "attempts": 0}
    state["gaps"].append(gap)
    return gap


def next_queued_gap(state, topic=None):
    for g in state["gaps"]:
        if g["status"] == "queued" and (topic is None or g["topic"] == topic):
            return g
    return None


def set_gap_status(state, gap_id, status, *, requeue=False):
    for g in state["gaps"]:
        if g["id"] == gap_id:
            if requeue:
                g["status"] = "queued"
                g["attempts"] += 1
            else:
                g["status"] = status
            return


def _main(argv):
    import argparse
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    g = sub.add_parser("gen-id")
    g.add_argument("prefix"); g.add_argument("seed")
    a = sub.add_parser("add-corpus")
    a.add_argument("--root", default=".")
    for f in ("title", "source", "topic", "native", "extracted"):
        a.add_argument(f"--{f}", required=True)
    a.add_argument("--lossy", action="store_true")
    a.add_argument("--id", default=None)
    sg = sub.add_parser("set-graph")
    sg.add_argument("--root", default=".")
    sg.add_argument("--dirty", choices=("true", "false"), default=None)
    sg.add_argument("--node-count", type=int, default=None)
    sg.add_argument("--edge-count", type=int, default=None)
    sg.add_argument("--last-update", default=None)
    br = sub.add_parser("budget-remaining"); br.add_argument("--root", default=".")
    brs = sub.add_parser("budget-reset"); brs.add_argument("--root", default=".")
    bsp = sub.add_parser("budget-spend"); bsp.add_argument("--root", default="."); bsp.add_argument("--sources", type=int, required=True)
    bst = sub.add_parser("budget-status"); bst.add_argument("--root", default=".")
    ag = sub.add_parser("add-gap"); ag.add_argument("--root", default=".")
    ag.add_argument("--topic", required=True); ag.add_argument("--desc", required=True)
    ag.add_argument("--origin", default="human")
    ng = sub.add_parser("next-gap"); ng.add_argument("--root", default="."); ng.add_argument("--topic", default=None)
    stg = sub.add_parser("set-gap"); stg.add_argument("--root", default=".")
    stg.add_argument("--id", required=True); stg.add_argument("--status", required=True)
    stg.add_argument("--requeue", action="store_true")
    args = ap.parse_args(argv)
    if args.cmd == "gen-id":
        print(gen_id(args.prefix, args.seed)); return 0
    if args.cmd == "add-corpus":
        st = load(args.root)
        e = add_corpus_entry(st, title=args.title, source=args.source, topic=args.topic,
                             native_path=args.native, extracted_path=args.extracted,
                             lossy=args.lossy, id=args.id)
        save(st, args.root)
        print(e["id"]); return 0
    if args.cmd == "set-graph":
        st = load(args.root)
        set_graph(st,
                  dirty={"true": True, "false": False}.get(args.dirty),
                  node_count=args.node_count, edge_count=args.edge_count,
                  last_update=args.last_update)
        save(st, args.root)
        print("graph updated"); return 0
    if args.cmd == "budget-remaining":
        print(budget_remaining_sources(load(args.root))); return 0
    if args.cmd == "budget-reset":
        st = load(args.root); budget_reset(st); save(st, args.root); print("budget reset"); return 0
    if args.cmd == "budget-spend":
        st = load(args.root); budget_spend_source(st, args.sources); save(st, args.root)
        print(budget_remaining_sources(st)); return 0
    if args.cmd == "budget-status":
        st = load(args.root)
        out = {"phase": st["budget"]["phase"],
               "remaining_sources": budget_remaining_sources(st),
               "subagents": {f: subagent_count(st, f) for f in ("search", "ingest", "process")}}
        print(json.dumps(out)); return 0
    if args.cmd == "add-gap":
        st = load(args.root); g = add_gap(st, topic=args.topic, desc=args.desc, origin=args.origin)
        save(st, args.root); print(g["id"]); return 0
    if args.cmd == "next-gap":
        g = next_queued_gap(load(args.root), topic=args.topic)
        if g:
            print(f"{g['id']}\t{g['topic']}\t{g['desc']}")
        return 0
    if args.cmd == "set-gap":
        st = load(args.root); set_gap_status(st, args.id, args.status, requeue=args.requeue)
        save(st, args.root); print("gap updated"); return 0
    return 1


if __name__ == "__main__":
    sys.exit(_main(sys.argv[1:]))
