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
