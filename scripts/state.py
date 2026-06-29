"""On-disk state ledger for the loop research engine. Stdlib only."""
import copy
import fcntl
import hashlib
import json
import os
import sys
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path


def docs_base():
    """Root-relative base dir for research output (topic dirs + findings)."""
    import os
    return os.environ.get("DOCS_BASE", ".research/docs")


DEFAULT_STATE = {
    "budget": {
        "tokens_per_cycle": 200000,
        "sources_per_cycle": 8,
        "max_subagents": 8,
        "max_workers": 4,
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


def lock_path(root="."):
    return Path(root) / ".research" / "state.lock"


@contextmanager
def locked_state(root="."):
    """Load -> yield -> save the state under an exclusive cross-process flock.

    The lock is a stable sidecar file (never the state file, whose os.replace
    swaps the inode). The state is saved only on clean exit; an exception
    propagates without a partial write. flock releases when the fd closes.
    """
    lp = lock_path(root)
    lp.parent.mkdir(parents=True, exist_ok=True)
    with open(lp, "w") as lf:
        fcntl.flock(lf, fcntl.LOCK_EX)
        st = load(root)
        yield st
        save(st, root)


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


def budget_reserve(state, n=1):
    granted = max(0, min(n, budget_remaining_sources(state)))
    state["budget"]["spent"]["sources"] += granted
    return granted


def budget_refund(state, n=1):
    s = state["budget"]["spent"]
    s["sources"] = max(0, s["sources"] - n)


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


def list_gaps(state, topic=None, status=None):
    return [
        g for g in state["gaps"]
        if (topic is None or g["topic"] == topic)
        and (status is None or g["status"] == status)
    ]


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


def add_draft(state, *, topic, title, path, cites, status="draft", now=None, id=None):
    did = id or gen_id("d", topic + "|" + title)
    for d in state["drafts"]:
        if d["id"] == did:
            return d
    draft = {
        "id": did, "topic": topic, "title": title, "path": path,
        "status": status, "cites": list(cites),
        "created_at": now or _now(), "promoted_path": None,
    }
    state["drafts"].append(draft)
    return draft


def list_drafts(state, status=None, topic=None):
    return [
        d for d in state["drafts"]
        if (status is None or d["status"] == status)
        and (topic is None or d["topic"] == topic)
    ]


def get_draft(state, draft_id):
    for d in state["drafts"]:
        if d["id"] == draft_id:
            return d
    return None


def set_draft_status(state, draft_id, status):
    d = get_draft(state, draft_id)
    if d is not None:
        d["status"] = status
    return d


def promote_draft(state, draft_id, dest_path, now=None):
    d = get_draft(state, draft_id)
    if d is None:
        return None
    d["status"] = "promoted"
    d["promoted_path"] = dest_path
    d["promoted_at"] = now or _now()
    return d


def reject_draft(state, draft_id, reason=None, now=None):
    d = get_draft(state, draft_id)
    if d is None:
        return None
    d["status"] = "rejected"
    if reason:
        d["reject_reason"] = reason
    return d


def _cited_ids(state, exclude_rejected=True):
    out = set()
    for d in state["drafts"]:
        if exclude_rejected and d["status"] == "rejected":
            continue
        out.update(d.get("cites", []))
    return out


def unprocessed_sources(state, topic):
    cited = _cited_ids(state)
    return [e for e in state["corpus"]
            if e["topic"] == topic and e["id"] not in cited]


def process_candidates(state, min_sources=3):
    if subagent_count(state, "process") <= 0:
        return []
    cited = _cited_ids(state)
    counts = {}
    for e in state["corpus"]:
        if e["id"] not in cited:
            counts[e["topic"]] = counts.get(e["topic"], 0) + 1
    cands = [(t, n) for t, n in counts.items() if n >= min_sources]
    cands.sort(key=lambda tn: (-tn[1], tn[0]))
    return cands


def set_phase(state, phase):
    if phase not in state["budget"]["weights"]:
        raise ValueError(f"unknown phase: {phase}")
    state["budget"]["phase"] = phase
    return phase


def set_goal(state, *, question, shape, now=None):
    state["goal"] = {"question": question, "shape": shape, "created_at": now or _now()}
    return state["goal"]


def set_plan(state, *, entities, dimensions, topics):
    state["plan"] = {
        "entities": list(entities), "dimensions": list(dimensions),
        "topics": list(topics), "candidate_dimensions": [], "rejected_dimensions": [],
    }
    return state["plan"]


def _plan(state):
    return state.setdefault("plan", {
        "entities": [], "dimensions": [], "topics": [],
        "candidate_dimensions": [], "rejected_dimensions": [],
    })


def add_dimension_candidate(state, *, name, cite, cycle):
    p = _plan(state)
    for c in p["candidate_dimensions"]:
        if c["name"] == name:
            if cite not in c["evidence_cites"]:
                c["evidence_cites"].append(cite)
            c["corroboration"] = len(c["evidence_cites"])
            c["last_seen_cycle"] = cycle
            return c
    c = {"name": name, "evidence_cites": [cite], "corroboration": 1,
         "first_seen_cycle": cycle, "last_seen_cycle": cycle, "status": "pending"}
    p["candidate_dimensions"].append(c)
    return c


def list_candidate_dimensions(state, status="pending"):
    return [c for c in _plan(state)["candidate_dimensions"]
            if status is None or c.get("status") == status]


def accept_dimension(state, name, *, now=None):
    p = _plan(state)
    for i, c in enumerate(p["candidate_dimensions"]):
        if c["name"] == name:
            p["candidate_dimensions"].pop(i)
            dim = {"name": name, "why": "discovered", "findings": [],
                   "accepted_at": now or _now()}
            p["dimensions"].append(dim)
            p["last_accept_cycle"] = c.get("last_seen_cycle")
            return dim
    return None


def reject_dimension(state, name, *, reason, cycle):
    p = _plan(state)
    for i, c in enumerate(p["candidate_dimensions"]):
        if c["name"] == name:
            p["candidate_dimensions"].pop(i)
            rec = {"name": name, "reason": reason, "cycle": cycle}
            p["rejected_dimensions"].append(rec)
            return rec
    return None


def init_run_budget(state, *, token_ceiling, now=None):
    state["budget"]["run"] = {
        "token_ceiling": token_ceiling, "tokens_spent": 0, "started_at": now or _now(),
    }
    return state["budget"]["run"]


def set_run_tokens_spent(state, n):
    state["budget"].setdefault("run", {"token_ceiling": 0, "tokens_spent": 0, "started_at": None})
    state["budget"]["run"]["tokens_spent"] = n
    return n


def run_budget_exceeded(state):
    r = state["budget"].get("run")
    return bool(r) and r["tokens_spent"] >= r["token_ceiling"]


def init_dimension_alpha(state, *, wealth):
    state["budget"]["dimension_alpha"] = {"wealth": wealth, "spent": 0}
    return state["budget"]["dimension_alpha"]


def _alpha(state):
    return state["budget"].get("dimension_alpha") or {"wealth": 0, "spent": 0}


def dimension_threshold(state, base_k):
    return base_k + _alpha(state)["spent"]


def dimension_wealth_left(state):
    a = _alpha(state)
    return max(0, a["wealth"] - a["spent"])


def spend_dimension_alpha(state, n=1):
    a = state["budget"].setdefault("dimension_alpha", {"wealth": 0, "spent": 0})
    a["spent"] += n
    return dimension_wealth_left(state)


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
    brv = sub.add_parser("budget-reserve"); brv.add_argument("--root", default="."); brv.add_argument("--sources", type=int, required=True)
    brf = sub.add_parser("budget-refund"); brf.add_argument("--root", default="."); brf.add_argument("--sources", type=int, required=True)
    bst = sub.add_parser("budget-status"); bst.add_argument("--root", default=".")
    ag = sub.add_parser("add-gap"); ag.add_argument("--root", default=".")
    ag.add_argument("--topic", required=True); ag.add_argument("--desc", required=True)
    ag.add_argument("--origin", default="human")
    lg = sub.add_parser("list-gaps"); lg.add_argument("--root", default=".")
    lg.add_argument("--topic", default=None); lg.add_argument("--status", default=None)
    ng = sub.add_parser("next-gap"); ng.add_argument("--root", default="."); ng.add_argument("--topic", default=None)
    stg = sub.add_parser("set-gap"); stg.add_argument("--root", default=".")
    stg.add_argument("--id", required=True); stg.add_argument("--status", required=True)
    stg.add_argument("--requeue", action="store_true")
    ad = sub.add_parser("add-draft"); ad.add_argument("--root", default=".")
    ad.add_argument("--topic", required=True); ad.add_argument("--title", required=True)
    ad.add_argument("--path", required=True); ad.add_argument("--cites", default="")
    ad.add_argument("--status", default="draft"); ad.add_argument("--id", default=None)
    ld = sub.add_parser("list-drafts"); ld.add_argument("--root", default=".")
    ld.add_argument("--status", default=None); ld.add_argument("--topic", default=None)
    sd = sub.add_parser("set-draft"); sd.add_argument("--root", default=".")
    sd.add_argument("--id", required=True); sd.add_argument("--status", required=True)
    cd = sub.add_parser("candidates"); cd.add_argument("--root", default=".")
    cd.add_argument("--min-sources", type=int, default=3)
    sph = sub.add_parser("set-phase"); sph.add_argument("--root", default=".")
    sph.add_argument("--phase", required=True)
    irb = sub.add_parser("init-run-budget"); irb.add_argument("--root", default=".")
    irb.add_argument("--ceiling", type=int, required=True)
    srs = sub.add_parser("set-run-spent"); srs.add_argument("--root", default=".")
    srs.add_argument("--tokens", type=int, required=True)
    adc = sub.add_parser("add-dim-candidate"); adc.add_argument("--root", default=".")
    adc.add_argument("--name", required=True); adc.add_argument("--cite", required=True)
    adc.add_argument("--cycle", type=int, required=True)
    args = ap.parse_args(argv)
    if args.cmd == "gen-id":
        print(gen_id(args.prefix, args.seed)); return 0
    if args.cmd == "add-corpus":
        with locked_state(args.root) as st:
            e = add_corpus_entry(st, title=args.title, source=args.source, topic=args.topic,
                                 native_path=args.native, extracted_path=args.extracted,
                                 lossy=args.lossy, id=args.id)
        print(e["id"]); return 0
    if args.cmd == "set-graph":
        with locked_state(args.root) as st:
            set_graph(st,
                      dirty={"true": True, "false": False}.get(args.dirty),
                      node_count=args.node_count, edge_count=args.edge_count,
                      last_update=args.last_update)
        print("graph updated"); return 0
    if args.cmd == "budget-remaining":
        print(budget_remaining_sources(load(args.root))); return 0
    if args.cmd == "budget-reset":
        with locked_state(args.root) as st:
            budget_reset(st)
        print("budget reset"); return 0
    if args.cmd == "budget-spend":
        with locked_state(args.root) as st:
            budget_spend_source(st, args.sources)
            remaining = budget_remaining_sources(st)
        print(remaining); return 0
    if args.cmd == "budget-reserve":
        with locked_state(args.root) as st:
            granted = budget_reserve(st, args.sources)
        print(granted); return 0
    if args.cmd == "budget-refund":
        with locked_state(args.root) as st:
            budget_refund(st, args.sources)
        print("refunded"); return 0
    if args.cmd == "budget-status":
        st = load(args.root)
        out = {"phase": st["budget"]["phase"],
               "remaining_sources": budget_remaining_sources(st),
               "max_workers": st["budget"].get("max_workers", 4),
               "subagents": {f: subagent_count(st, f) for f in ("search", "ingest", "process")}}
        print(json.dumps(out)); return 0
    if args.cmd == "add-gap":
        with locked_state(args.root) as st:
            g = add_gap(st, topic=args.topic, desc=args.desc, origin=args.origin)
        print(g["id"]); return 0
    if args.cmd == "list-gaps":
        for g in list_gaps(load(args.root), topic=args.topic, status=args.status):
            print(f"{g['id']}\t{g['topic']}\t{g['desc']}")
        return 0
    if args.cmd == "next-gap":
        g = next_queued_gap(load(args.root), topic=args.topic)
        if g:
            print(f"{g['id']}\t{g['topic']}\t{g['desc']}")
        return 0
    if args.cmd == "set-gap":
        with locked_state(args.root) as st:
            set_gap_status(st, args.id, args.status, requeue=args.requeue)
        print("gap updated"); return 0
    if args.cmd == "add-draft":
        with locked_state(args.root) as st:
            cites = [c for c in args.cites.split(",") if c]
            d = add_draft(st, topic=args.topic, title=args.title, path=args.path,
                          cites=cites, status=args.status, id=args.id)
        print(d["id"]); return 0
    if args.cmd == "list-drafts":
        for d in list_drafts(load(args.root), status=args.status, topic=args.topic):
            print(f"{d['id']}\t{d['status']}\t{d['topic']}\t{d['title']}")
        return 0
    if args.cmd == "set-draft":
        try:
            with locked_state(args.root) as st:
                if set_draft_status(st, args.id, args.status) is None:
                    raise LookupError(args.id)
        except LookupError as e:
            print(f"unknown draft: {e.args[0]}", file=sys.stderr); return 1
        print("draft updated"); return 0
    if args.cmd == "candidates":
        for topic, n in process_candidates(load(args.root), min_sources=args.min_sources):
            print(f"{topic}\t{n}")
        return 0
    if args.cmd == "set-phase":
        try:
            with locked_state(args.root) as st:
                set_phase(st, args.phase)
        except ValueError as e:
            print(str(e), file=sys.stderr); return 1
        print(args.phase); return 0
    if args.cmd == "init-run-budget":
        with locked_state(args.root) as st_:
            init_run_budget(st_, token_ceiling=args.ceiling)
        print("run budget set"); return 0
    if args.cmd == "set-run-spent":
        with locked_state(args.root) as st_:
            set_run_tokens_spent(st_, args.tokens)
        print(args.tokens); return 0
    if args.cmd == "add-dim-candidate":
        with locked_state(args.root) as st_:
            c = add_dimension_candidate(st_, name=args.name, cite=args.cite, cycle=args.cycle)
        print(c["corroboration"]); return 0
    return 1


if __name__ == "__main__":
    sys.exit(_main(sys.argv[1:]))
