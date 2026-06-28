"""Deterministic half of the dimension-discovery gate. Stdlib only.

The agent applies the LLM axes (goal-relevance, distinctness, comparability) to the
candidates this returns as `eligible`; this module owns the deterministic axes
(corroboration threshold, alpha-wealth, run-budget headroom, TTL expiry) and records
the accept/reject decisions.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import state as state_mod
import orchestrator as orch


def eligible(state, base_k=3):
    if state_mod.run_budget_exceeded(state):
        return []
    return orch.accept_eligible(state, base_k)


def expired(state, current_cycle, ttl=3, base_k=3):
    thr = state_mod.dimension_threshold(state, base_k)
    return [c for c in state_mod.list_candidate_dimensions(state)
            if current_cycle - c.get("last_seen_cycle", current_cycle) >= ttl
            and c.get("corroboration", 0) < thr]


def accept(state, name, *, now=None):
    dim = state_mod.accept_dimension(state, name, now=now)
    if dim is not None:
        state_mod.spend_dimension_alpha(state)
    return dim


def reject(state, name, *, reason, cycle):
    return state_mod.reject_dimension(state, name, reason=reason, cycle=cycle)


def expire(state, current_cycle, ttl=3):
    n = 0
    for c in list(expired(state, current_cycle, ttl)):
        reject(state, c["name"], reason=f"ttl-expired@{current_cycle}", cycle=current_cycle)
        n += 1
    return n


def _main(argv):
    import argparse
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    e = sub.add_parser("eligible"); e.add_argument("--root", default=".")
    ac = sub.add_parser("accept"); ac.add_argument("--root", default="."); ac.add_argument("--name", required=True)
    rj = sub.add_parser("reject"); rj.add_argument("--root", default="."); rj.add_argument("--name", required=True)
    rj.add_argument("--reason", required=True); rj.add_argument("--cycle", type=int, required=True)
    ex = sub.add_parser("expire"); ex.add_argument("--root", default="."); ex.add_argument("--cycle", type=int, required=True)
    args = ap.parse_args(argv)
    if args.cmd == "eligible":
        for c in eligible(state_mod.load(args.root)):
            print(c["name"])
        return 0
    if args.cmd == "accept":
        with state_mod.locked_state(args.root) as st_:
            accept(st_, args.name)
        print("accepted"); return 0
    if args.cmd == "reject":
        with state_mod.locked_state(args.root) as st_:
            reject(st_, args.name, reason=args.reason, cycle=args.cycle)
        print("rejected"); return 0
    if args.cmd == "expire":
        with state_mod.locked_state(args.root) as st_:
            n = expire(st_, args.cycle)
        print(n); return 0
    return 1


if __name__ == "__main__":
    sys.exit(_main(sys.argv[1:]))
