"""Compute graph deltas and append them to the event stream. Stdlib only."""
import json
import sys
from datetime import datetime, timezone
from pathlib import Path


def node_edge_sets(graph):
    nodes = {n.get("id") for n in graph.get("nodes", []) if n.get("id") is not None}
    edges = {(e.get("source"), e.get("target")) for e in graph.get("edges", [])
             if e.get("source") is not None and e.get("target") is not None}
    return nodes, edges


def diff(old, new):
    on, oe = node_edge_sets(old)
    nn, ne = node_edge_sets(new)
    return {
        "new_nodes": sorted(nn - on),
        "new_edges": [list(p) for p in sorted(ne - oe)],
    }


def append_event(events_path, delta, now=None):
    p = Path(events_path)
    p.parent.mkdir(parents=True, exist_ok=True)
    rec = {"ts": now or datetime.now(timezone.utc).isoformat(),
           "new_nodes": delta.get("new_nodes", []),
           "new_edges": delta.get("new_edges", [])}
    with p.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(rec, ensure_ascii=False) + "\n")


def _load(path):
    if not path:
        return {}
    p = Path(path)
    return json.loads(p.read_text(encoding="utf-8")) if p.is_file() else {}


def _main(argv):
    import argparse
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("append")
    a.add_argument("--old", default="")
    a.add_argument("--new", required=True)
    a.add_argument("--events", required=True)
    args = ap.parse_args(argv)
    if args.cmd == "append":
        d = diff(_load(args.old), _load(args.new))
        append_event(args.events, d)
        print(f"appended delta: +{len(d['new_nodes'])} nodes, +{len(d['new_edges'])} edges")
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(_main(sys.argv[1:]))
