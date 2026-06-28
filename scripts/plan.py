"""Validate a research plan JSON and apply it to state. Stdlib only."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import state as state_mod

SHAPES = ("comparison", "survey", "causal", "how-to", "chronology")
_MATRIX = ("comparison", "causal")


def validate_plan(plan):
    problems = []
    shape = plan.get("shape")
    if shape not in SHAPES:
        problems.append(f"bad shape: {shape!r} (allowed: {', '.join(SHAPES)})")
        return problems
    if shape in _MATRIX:
        if not plan.get("entities"):
            problems.append("comparison/causal plan needs non-empty entities")
        if not plan.get("dimensions"):
            problems.append("comparison/causal plan needs non-empty dimensions")
        names = [d.get("name") for d in plan.get("dimensions", [])]
    else:
        if not plan.get("topics"):
            problems.append(f"{shape} plan needs non-empty topics")
        names = [t.get("name") for t in plan.get("topics", [])]
    if len(names) != len(set(names)):
        problems.append("duplicate dimension/topic names")
    gaps = plan.get("seed_gaps")
    if not gaps:
        problems.append("plan needs non-empty seed_gaps")
    else:
        for g in gaps:
            if "topic" not in g or "desc" not in g:
                problems.append(f"seed_gap missing topic/desc: {g!r}")
    return problems


def cap_for_budget(budget_tokens):
    return max(4, budget_tokens // 60000)


def seed_gaps_from_plan(state, plan, cap):
    n = 0
    for g in plan["seed_gaps"][:cap]:
        state_mod.add_gap(state, topic=g["topic"], desc=g["desc"], origin="plan")
        n += 1
    return n


def apply_plan(state, *, question, plan, budget_tokens, alpha_wealth=5, now=None):
    problems = validate_plan(plan)
    if problems:
        raise ValueError("; ".join(problems))
    state_mod.set_goal(state, question=question, shape=plan["shape"], now=now)
    state_mod.set_plan(state, entities=plan.get("entities", []),
                       dimensions=plan.get("dimensions", []),
                       topics=plan.get("topics", []))
    seeded = seed_gaps_from_plan(state, plan, cap_for_budget(budget_tokens))
    state_mod.init_run_budget(state, token_ceiling=budget_tokens, now=now)
    state_mod.init_dimension_alpha(state, wealth=alpha_wealth)
    return {"gaps_seeded": seeded,
            "dimensions": len(plan.get("dimensions", [])),
            "topics": len(plan.get("topics", []))}


def _main(argv):
    import argparse
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("apply")
    a.add_argument("--root", default=".")
    a.add_argument("--question", required=True)
    a.add_argument("--budget", type=int, required=True)
    a.add_argument("--plan-file", required=True)
    a.add_argument("--alpha-wealth", type=int, default=5)
    args = ap.parse_args(argv)
    if args.cmd == "apply":
        plan_obj = json.loads(Path(args.plan_file).read_text(encoding="utf-8"))
        try:
            with state_mod.locked_state(args.root) as st_:
                res = apply_plan(st_, question=args.question, plan=plan_obj,
                                 budget_tokens=args.budget, alpha_wealth=args.alpha_wealth)
        except ValueError as e:
            print(f"invalid plan: {e}", file=sys.stderr)
            return 1
        print(json.dumps(res))
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(_main(sys.argv[1:]))
