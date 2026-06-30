"""Convergence orchestrator: deterministic phase + flow decisions over state.json.

Stdlib only. Reads only .research/state.json (via state.py). The phase decision is
a stateless function of current signals, so it self-corrects in either direction.
"""
import json
import sys

import state as state_mod


def _processable(state, min_sources):
    """True when some topic has >= min_sources un-cited corpus entries.

    Phase-independent on purpose: state.process_candidates self-gates on the process
    subagent count (0 in `gather`), which would make the gather->deepen decision
    circular.
    """
    cited = state_mod._cited_ids(state)
    counts = {}
    for e in state["corpus"]:
        if e["id"] not in cited:
            counts[e["topic"]] = counts.get(e["topic"], 0) + 1
    return any(n >= min_sources for n in counts.values())


def recommend_phase(state, min_sources=3):
    """Budget phase from current signals. `synthesize` needs no queued gaps, a clean
    graph, and either processable corpus or a pending draft — so it is reachable with
    no draft yet; `goal_met` narrows that to the done case.
    """
    queued = len(state_mod.list_gaps(state, status="queued"))
    dirty = state["graph"]["dirty"]
    processable = _processable(state, min_sources)
    pending = len(state_mod.list_drafts(state, status="draft"))
    if queued == 0 and not dirty and (processable or pending):
        return "synthesize"
    if not processable and not pending:
        return "gather"
    return "deepen"


def accept_eligible(state, base_k=3):
    if state_mod.dimension_wealth_left(state) <= 0:
        return []
    thr = state_mod.dimension_threshold(state, base_k)
    return [c for c in state_mod.list_candidate_dimensions(state)
            if c.get("corroboration", 0) >= thr]


def goal_met(state, min_sources=3):
    """True only while a finished draft still waits (status='draft') and nothing else
    is processable — a 'ready for human adjudication' signal, NOT 'done'. Adjudicating
    the last draft (promote/reject) clears it by design; convergence is work-drained +
    drafts adjudicated, so do not poll this flag while reviewing inline (see ADR 0008).
    """
    return (
        recommend_phase(state, min_sources) == "synthesize"
        and not _processable(state, min_sources)
        and len(state_mod.list_drafts(state, status="draft")) >= 1
        and not accept_eligible(state)
    )


def next_actions(state, min_sources=3):
    queued = len(state_mod.list_gaps(state, status="queued"))
    search = (
        queued > 0
        and state_mod.budget_remaining_sources(state) > 0
        and state_mod.subagent_count(state, "search") > 0
    )
    process = len(state_mod.process_candidates(state, min_sources)) > 0
    return {"search": bool(search), "process": bool(process)}


def decide(state, min_sources=3, apply=False):
    before = state["budget"]["phase"]
    rec = recommend_phase(state, min_sources)
    state_mod.set_phase(state, rec)                 # in-memory flip (validated)
    budget_exhausted = state_mod.run_budget_exceeded(state)
    met = goal_met(state, min_sources)
    result = {
        "phase": rec,
        "phase_changed": rec != before,
        **next_actions(state, min_sources),
        "goal_met": met,
        "budget_exhausted": budget_exhausted,
        "stop": met or budget_exhausted,
    }
    if not apply:
        state_mod.set_phase(state, before)          # restore for dry-run
    return result


def _main(argv):
    import argparse
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    d = sub.add_parser("decide")
    d.add_argument("--root", default=".")
    d.add_argument("--min-sources", type=int, default=3)
    d.add_argument("--apply", action="store_true")
    args = ap.parse_args(argv)
    if args.cmd == "decide":
        st = state_mod.load(args.root)
        res = decide(st, min_sources=args.min_sources, apply=args.apply)
        if args.apply:
            state_mod.save(st, args.root)
        print(json.dumps(res))
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(_main(sys.argv[1:]))
