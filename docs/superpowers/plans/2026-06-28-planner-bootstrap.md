# The Planner: one-prompt research bootstrap — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Turn a single natural-language prompt into a fully autonomous research run on top of the existing `/goal` loop — decompose the question, research it to plateau or token budget, leaving cited findings.

**Architecture:** A `/research` flow does the LLM decomposition and emits a plan JSON; a pure-code `scripts/plan.py` validates it, writes `goal`+`plan` into `state.json`, seeds the gap queue and run budget, then hands off to the unchanged `/goal` loop. The loop gains a per-cycle dimension-discovery gate (streaming multiple-testing) and total-run token metering. Everything new is read via `.get()` defaults so existing state and tests are untouched.

**Tech Stack:** Python 3 stdlib only (`python3`, not `python`). Tests are `unittest` under `tests/`. Flows are agent procedures in `.claude/*.md`. State is `.research/state.json`, always reached through a `--root` param.

## Global Constraints

- `python3` only; **stdlib only** in all scripts (no new dependencies).
- All new paths go through the existing `--root` parameter — no cwd-hardcoded paths (sub-project B requires this).
- New `state.json` blocks (`goal`, `plan`, `budget.run`, `budget.dimension_alpha`) are **additive**; never add them to `check_integrity.REQUIRED_KEYS`; always read them with `.get()` defaults so existing states/tests don't break.
- Never modify `DEFAULT_STATE` to add the new blocks (would risk existing equality tests); the blocks are created on demand by `plan.py`.
- Tests: `unittest`, run with `python3 -m unittest tests.<module> -v`. No frameworks, no fixtures beyond `tempfile`.
- Commit per task; stage explicitly (never `git add .`/`-A`); Conventional Commits; no co-author trailer.
- NEVER touch/stage `public/dashboard.html`, `.research/*.log`, or `graphify-out/`.
- Shape enum (verbatim): `comparison`, `survey`, `causal`, `how-to`, `chronology`. Unknown → fall back to `survey`.
- Dimension-gate defaults: corroboration base `K=3`; pending TTL `3` cycles; dimension α-wealth initial `5`; cycle cap `25` (existing).

---

## File structure

| File | Responsibility | New? |
| --- | --- | --- |
| `scripts/state.py` | add goal/plan/run-budget/dimension helpers + CLI | modify |
| `scripts/plan.py` | validate plan JSON, seed gaps, apply plan to state | create |
| `scripts/meter.py` | sum run tokens from session transcript; fallback estimate | create |
| `scripts/dimension_gate.py` | deterministic corroboration/wealth/budget eligibility pre-filter | create |
| `scripts/orchestrator.py` | extend `goal_met`; add budget/stop to `decide` | modify |
| `scripts/check_integrity.py` | validate plan/candidate cites resolve to corpus | modify |
| `.claude/research.md` | the planner flow (LLM decompose → plan.py apply → launch /goal) | create |
| `.claude/goal.md` | add per-cycle meter step + dimension gate + stop-on-budget | modify |
| `.claude/process.md` | emit dimension candidates while drafting | modify |
| `.claude/report.md` | on-demand report assembler (separable final task) | create |
| `tests/test_planner_state.py` | state helper tests | create |
| `tests/test_plan.py` | plan.py tests | create |
| `tests/test_meter.py` | meter.py tests | create |
| `tests/test_dimension_gate.py` | gate eligibility tests | create |
| `tests/test_orchestrator.py` | extend for budget stop + dimension-stable goal_met | modify |
| `tests/test_check_integrity.py` | extend for plan-cite validation | modify |

---

## Task 1: State — goal + plan blocks and helpers

**Files:**
- Modify: `scripts/state.py` (add helpers after `set_phase`, ~line 273)
- Test: `tests/test_planner_state.py` (create)

**Interfaces:**
- Consumes: existing `state.add_gap`, `state.gen_id`, `state._now`.
- Produces:
  - `set_goal(state, *, question, shape, now=None) -> dict` — sets `state["goal"]={question,shape,created_at}`, returns it.
  - `set_plan(state, *, entities, dimensions, topics) -> dict` — sets `state["plan"]={entities,dimensions,topics,candidate_dimensions:[],rejected_dimensions:[]}`; `dimensions`/`topics` are lists of `{name, why}`.
  - `add_dimension_candidate(state, *, name, cite, cycle) -> dict` — upsert by `name`; appends `cite` to `evidence_cites` (deduped); sets `corroboration=len(evidence_cites)`, `last_seen_cycle=cycle`, `status="pending"`; on first sight sets `first_seen_cycle=cycle`.
  - `list_candidate_dimensions(state, status="pending") -> list`
  - `accept_dimension(state, name, *, now=None) -> dict|None` — moves candidate to `plan["dimensions"]` as `{name, why:"discovered", findings:[]}`, removes from candidates, sets `plan["last_accept_cycle"]`, returns the dimension; None if absent.
  - `reject_dimension(state, name, *, reason, cycle) -> dict|None` — moves candidate to `plan["rejected_dimensions"]` as `{name, reason, cycle}`; None if absent.

- [ ] **Step 1: Write the failing test**

```python
# tests/test_planner_state.py
import os, sys, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import state as st


class GoalPlan(unittest.TestCase):
    def test_set_goal_and_plan(self):
        s = st.load_default()
        st.set_goal(s, question="777 vs A380", shape="comparison")
        self.assertEqual(s["goal"]["shape"], "comparison")
        self.assertIn("created_at", s["goal"])
        st.set_plan(s, entities=["777", "A380"],
                    dimensions=[{"name": "fuel", "why": "efficiency"}], topics=[])
        self.assertEqual(s["plan"]["entities"], ["777", "A380"])
        self.assertEqual(s["plan"]["candidate_dimensions"], [])
        self.assertEqual(s["plan"]["rejected_dimensions"], [])


class Candidates(unittest.TestCase):
    def test_candidate_accumulates_independent_evidence(self):
        s = st.load_default()
        st.set_plan(s, entities=["a", "b"], dimensions=[], topics=[])
        st.add_dimension_candidate(s, name="passenger preference", cite="c1", cycle=1)
        st.add_dimension_candidate(s, name="passenger preference", cite="c1", cycle=2)  # dup cite
        st.add_dimension_candidate(s, name="passenger preference", cite="c2", cycle=2)
        c = st.list_candidate_dimensions(s)[0]
        self.assertEqual(c["corroboration"], 2)          # c1 deduped
        self.assertEqual(c["first_seen_cycle"], 1)
        self.assertEqual(c["last_seen_cycle"], 2)

    def test_accept_moves_candidate_to_dimensions(self):
        s = st.load_default()
        st.set_plan(s, entities=["a", "b"], dimensions=[], topics=[])
        st.add_dimension_candidate(s, name="noise", cite="c1", cycle=1)
        d = st.accept_dimension(s, "noise", now="T")
        self.assertEqual(d["name"], "noise")
        self.assertEqual([x["name"] for x in s["plan"]["dimensions"]], ["noise"])
        self.assertEqual(st.list_candidate_dimensions(s), [])
        self.assertEqual(s["plan"]["last_accept_cycle"], 1)

    def test_reject_moves_candidate_to_rejected(self):
        s = st.load_default()
        st.set_plan(s, entities=["a", "b"], dimensions=[], topics=[])
        st.add_dimension_candidate(s, name="weather", cite="c1", cycle=1)
        st.reject_dimension(s, "weather", reason="off-goal", cycle=2)
        self.assertEqual(s["plan"]["rejected_dimensions"][0]["reason"], "off-goal")
        self.assertEqual(st.list_candidate_dimensions(s), [])


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m unittest tests.test_planner_state -v`
Expected: FAIL — `AttributeError: module 'state' has no attribute 'set_goal'`.

- [ ] **Step 3: Write minimal implementation** — add to `scripts/state.py` after `set_phase` (after line 273):

```python
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
            dim = {"name": name, "why": "discovered", "findings": []}
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
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python3 -m unittest tests.test_planner_state -v`
Expected: PASS (4 tests).

- [ ] **Step 5: Commit**

```bash
git add scripts/state.py tests/test_planner_state.py
git commit -m "feat(state): goal/plan blocks + dimension-candidate helpers"
```

---

## Task 2: State — run budget + dimension α-wealth helpers and CLI

**Files:**
- Modify: `scripts/state.py` (helpers after Task 1's block; CLI subparsers in `_main`)
- Test: `tests/test_planner_state.py` (add a class)

**Interfaces:**
- Produces:
  - `init_run_budget(state, *, token_ceiling, now=None) -> dict` — `state["budget"]["run"]={token_ceiling,tokens_spent:0,started_at}`.
  - `set_run_tokens_spent(state, n) -> int` — sets `budget.run.tokens_spent=n`, returns it.
  - `run_budget_exceeded(state) -> bool` — True iff `run` exists and `tokens_spent >= token_ceiling`.
  - `init_dimension_alpha(state, *, wealth) -> dict` — `state["budget"]["dimension_alpha"]={wealth,spent:0}`.
  - `dimension_threshold(state, base_k) -> int` — `base_k + spent` (rises per acceptance).
  - `dimension_wealth_left(state) -> int` — `wealth - spent` (0 if absent).
  - `spend_dimension_alpha(state, n=1) -> int` — increments `spent`, returns wealth left.
  - CLI: `state.py init-run-budget --root --ceiling N`, `state.py set-run-spent --root --tokens N`, `state.py add-dim-candidate --root --name --cite --cycle N`.

- [ ] **Step 1: Write the failing test** — append to `tests/test_planner_state.py`:

```python
class RunBudget(unittest.TestCase):
    def test_run_budget_ceiling(self):
        s = st.load_default()
        st.init_run_budget(s, token_ceiling=1000, now="T")
        self.assertFalse(st.run_budget_exceeded(s))
        st.set_run_tokens_spent(s, 999)
        self.assertFalse(st.run_budget_exceeded(s))
        st.set_run_tokens_spent(s, 1000)
        self.assertTrue(st.run_budget_exceeded(s))

    def test_run_budget_absent_is_not_exceeded(self):
        self.assertFalse(st.run_budget_exceeded(st.load_default()))

    def test_dimension_alpha_threshold_rises_with_spend(self):
        s = st.load_default()
        st.init_dimension_alpha(s, wealth=5)
        self.assertEqual(st.dimension_threshold(s, 3), 3)   # base K, nothing spent
        self.assertEqual(st.dimension_wealth_left(s), 5)
        st.spend_dimension_alpha(s)
        self.assertEqual(st.dimension_threshold(s, 3), 4)   # bar rose
        self.assertEqual(st.dimension_wealth_left(s), 4)
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m unittest tests.test_planner_state.RunBudget -v`
Expected: FAIL — `module 'state' has no attribute 'init_run_budget'`.

- [ ] **Step 3: Write minimal implementation** — add to `scripts/state.py` after Task 1's helpers:

```python
def init_run_budget(state, *, token_ceiling, now=None):
    state["budget"]["run"] = {
        "token_ceiling": token_ceiling, "tokens_spent": 0, "started_at": now or _now(),
    }
    return state["budget"]["run"]


def set_run_tokens_spent(state, n):
    state["budget"].setdefault("run", {"token_ceiling": 0, "tokens_spent": 0})
    state["budget"]["run"]["tokens_spent"] = n
    return n


def run_budget_exceeded(state):
    r = state["budget"].get("run")
    return bool(r) and r["tokens_spent"] >= r["token_ceiling"]


def init_dimension_alpha(state, *, wealth):
    state["budget"]["dimension_alpha"] = {"wealth": wealth, "spent": 0}
    return state["budget"]["dimension_alpha"]


def _alpha(state):
    return state["budget"].setdefault("dimension_alpha", {"wealth": 0, "spent": 0})


def dimension_threshold(state, base_k):
    return base_k + _alpha(state)["spent"]


def dimension_wealth_left(state):
    a = _alpha(state)
    return max(0, a["wealth"] - a["spent"])


def spend_dimension_alpha(state, n=1):
    _alpha(state)["spent"] += n
    return dimension_wealth_left(state)
```

Then add CLI subparsers inside `_main` (next to the other `sub.add_parser` calls, ~line 320) and handlers (next to the others, ~line 408):

```python
    # --- in the parser block ---
    irb = sub.add_parser("init-run-budget"); irb.add_argument("--root", default=".")
    irb.add_argument("--ceiling", type=int, required=True)
    srs = sub.add_parser("set-run-spent"); srs.add_argument("--root", default=".")
    srs.add_argument("--tokens", type=int, required=True)
    adc = sub.add_parser("add-dim-candidate"); adc.add_argument("--root", default=".")
    adc.add_argument("--name", required=True); adc.add_argument("--cite", required=True)
    adc.add_argument("--cycle", type=int, required=True)
```

```python
    # --- in the dispatch block ---
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
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python3 -m unittest tests.test_planner_state -v`
Expected: PASS (all classes). Also smoke the CLI:
Run: `python3 scripts/state.py add-dim-candidate --root /tmp/orsX --name foo --cite c1 --cycle 1`
Expected: prints `1` (creates `/tmp/orsX/.research/state.json`).

- [ ] **Step 5: Commit**

```bash
git add scripts/state.py tests/test_planner_state.py
git commit -m "feat(state): run-token budget + dimension alpha-wealth helpers + CLI"
```

---

## Task 3: `plan.py` — validate plan JSON and cap from budget

**Files:**
- Create: `scripts/plan.py`
- Test: `tests/test_plan.py` (create)

**Interfaces:**
- Consumes: shape enum (Global Constraints).
- Produces:
  - `SHAPES = ("comparison","survey","causal","how-to","chronology")`
  - `validate_plan(plan: dict) -> list[str]` — returns problem strings; empty list = valid. Rules: `shape` in SHAPES; comparison/causal require non-empty `entities` and `dimensions`; survey/how-to/chronology require non-empty `topics`; `seed_gaps` non-empty with `{topic,desc}` items; no duplicate dimension/topic names.
  - `cap_for_budget(budget_tokens: int) -> int` — max seed gaps = `max(4, budget_tokens // 60000)`.

- [ ] **Step 1: Write the failing test**

```python
# tests/test_plan.py
import os, sys, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import plan


VALID_CMP = {
    "shape": "comparison", "entities": ["777", "A380"],
    "dimensions": [{"name": "fuel", "why": "x"}, {"name": "range", "why": "y"}],
    "topics": [], "seed_gaps": [{"topic": "fuel", "desc": "777 fuel burn"}],
    "rationale": "r",
}


class Validate(unittest.TestCase):
    def test_valid_comparison(self):
        self.assertEqual(plan.validate_plan(VALID_CMP), [])

    def test_bad_shape(self):
        p = dict(VALID_CMP, shape="nonsense")
        self.assertTrue(any("shape" in x for x in plan.validate_plan(p)))

    def test_comparison_needs_entities_and_dimensions(self):
        p = dict(VALID_CMP, entities=[], dimensions=[])
        probs = plan.validate_plan(p)
        self.assertTrue(any("entities" in x for x in probs))
        self.assertTrue(any("dimensions" in x for x in probs))

    def test_survey_needs_topics(self):
        p = {"shape": "survey", "entities": [], "dimensions": [], "topics": [],
             "seed_gaps": [{"topic": "t", "desc": "d"}], "rationale": "r"}
        self.assertTrue(any("topics" in x for x in plan.validate_plan(p)))

    def test_duplicate_dimension_names_rejected(self):
        p = dict(VALID_CMP, dimensions=[{"name": "fuel", "why": "a"},
                                         {"name": "fuel", "why": "b"}])
        self.assertTrue(any("duplicate" in x for x in plan.validate_plan(p)))

    def test_cap_for_budget(self):
        self.assertEqual(plan.cap_for_budget(120000), 4)   # floor is 4
        self.assertEqual(plan.cap_for_budget(2000000), 33)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m unittest tests.test_plan -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'plan'`.

- [ ] **Step 3: Write minimal implementation**

```python
# scripts/plan.py
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
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python3 -m unittest tests.test_plan -v`
Expected: PASS (6 tests).

- [ ] **Step 5: Commit**

```bash
git add scripts/plan.py tests/test_plan.py
git commit -m "feat(plan): plan-JSON validation + budget-derived seed-gap cap"
```

---

## Task 4: `plan.py` — seed gaps, apply plan, CLI

**Files:**
- Modify: `scripts/plan.py` (add `seed_gaps_from_plan`, `apply_plan`, `_main`)
- Test: `tests/test_plan.py` (add a class)

**Interfaces:**
- Consumes: `state_mod.set_goal/set_plan/add_gap/init_run_budget/init_dimension_alpha/locked_state` (Tasks 1-2), `validate_plan/cap_for_budget` (Task 3).
- Produces:
  - `seed_gaps_from_plan(state, plan, cap) -> int` — adds up to `cap` gaps from `plan["seed_gaps"]` via `state_mod.add_gap(origin="plan")`; returns count added.
  - `apply_plan(state, *, question, plan, budget_tokens, alpha_wealth=5, now=None) -> dict` — calls `validate_plan` (raises `ValueError` joined on `"; "` if non-empty), then `set_goal`, `set_plan`, `seed_gaps_from_plan`, `init_run_budget(token_ceiling=budget_tokens)`, `init_dimension_alpha(wealth=alpha_wealth)`; returns `{"gaps_seeded": int, "dimensions": int, "topics": int}`.
  - CLI: `plan.py apply --root R --question Q --budget N --plan-file PATH` → exit 1 + stderr on invalid; else prints the summary JSON.

- [ ] **Step 1: Write the failing test** — append to `tests/test_plan.py`:

```python
import json, tempfile
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import state as st


class Apply(unittest.TestCase):
    def test_apply_writes_goal_plan_gaps_budget(self):
        s = st.load_default()
        res = plan.apply_plan(s, question="777 vs A380", plan=VALID_CMP,
                              budget_tokens=2000000, now="T")
        self.assertEqual(s["goal"]["shape"], "comparison")
        self.assertEqual([d["name"] for d in s["plan"]["dimensions"]], ["fuel", "range"])
        self.assertEqual(res["gaps_seeded"], 1)
        self.assertEqual(len(st.list_gaps(s, status="queued")), 1)
        self.assertEqual(s["budget"]["run"]["token_ceiling"], 2000000)
        self.assertEqual(s["budget"]["dimension_alpha"]["wealth"], 5)

    def test_apply_raises_on_invalid(self):
        s = st.load_default()
        with self.assertRaises(ValueError):
            plan.apply_plan(s, question="q", plan=dict(VALID_CMP, shape="bad"),
                            budget_tokens=1000, now="T")

    def test_seed_cap_limits_gaps(self):
        s = st.load_default()
        big = dict(VALID_CMP, seed_gaps=[{"topic": f"t{i}", "desc": f"d{i}"} for i in range(50)])
        res = plan.apply_plan(s, question="q", plan=big, budget_tokens=120000, now="T")
        self.assertEqual(res["gaps_seeded"], 4)            # cap_for_budget(120000)==4
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m unittest tests.test_plan.Apply -v`
Expected: FAIL — `module 'plan' has no attribute 'apply_plan'`.

- [ ] **Step 3: Write minimal implementation** — add to `scripts/plan.py`:

```python
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
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python3 -m unittest tests.test_plan -v`
Expected: PASS (9 tests). CLI smoke:
```bash
echo '{"shape":"comparison","entities":["a","b"],"dimensions":[{"name":"x","why":"w"}],"topics":[],"seed_gaps":[{"topic":"x","desc":"d"}],"rationale":"r"}' > /tmp/p.json
python3 scripts/plan.py apply --root /tmp/orsP --question "a vs b" --budget 1000000 --plan-file /tmp/p.json
```
Expected: prints `{"gaps_seeded": 1, "dimensions": 1, "topics": 0}`.

- [ ] **Step 5: Commit**

```bash
git add scripts/plan.py tests/test_plan.py
git commit -m "feat(plan): apply plan to state (goal+plan+gaps+budget) + CLI"
```

---

## Task 5: Orchestrator — budget stop + dimension-stable plateau

**Files:**
- Modify: `scripts/orchestrator.py` (`goal_met`, `decide`)
- Test: `tests/test_orchestrator.py` (add cases)

**Interfaces:**
- Consumes: `state.run_budget_exceeded`, `state.list_candidate_dimensions`, `state.dimension_threshold`, `state.dimension_wealth_left` (Tasks 1-2).
- Produces:
  - `accept_eligible(state, base_k=3) -> list` — candidates with `corroboration >= dimension_threshold(state, base_k)` AND `dimension_wealth_left(state) > 0`.
  - `goal_met(state, min_sources=3)` — unchanged conditions AND `not accept_eligible(state)`.
  - `decide(...)` output gains `budget_exhausted: bool` and `stop: bool` (`goal_met or budget_exhausted`).

- [ ] **Step 1: Write the failing test** — add to `tests/test_orchestrator.py`:

```python
class BudgetAndDimensions(unittest.TestCase):
    def _drained_with_draft(self):
        s = st.load_default()
        ids = _corpus(s, "t", 3)
        s["graph"]["dirty"] = False
        st.add_draft(s, topic="t", title="f", path="p", cites=ids, status="draft")
        return s

    def test_budget_exhausted_sets_stop(self):
        s = self._drained_with_draft()
        st.init_run_budget(s, token_ceiling=100, now="T")
        st.set_run_tokens_spent(s, 100)
        res = orch.decide(s, apply=False)
        self.assertTrue(res["budget_exhausted"])
        self.assertTrue(res["stop"])

    def test_accept_eligible_blocks_goal_met(self):
        s = self._drained_with_draft()
        st.init_dimension_alpha(s, wealth=5)
        st.set_plan(s, entities=["a", "b"], dimensions=[], topics=[])
        for cy in (1, 2, 3):                              # 3 independent sources => corrob 3 >= K 3
            st.add_dimension_candidate(s, name="pref", cite=f"c{cy}", cycle=cy)
        self.assertTrue(orch.accept_eligible(s))
        self.assertFalse(orch.goal_met(s))               # eligible candidate blocks plateau

    def test_goal_met_when_no_eligible_candidates(self):
        s = self._drained_with_draft()
        st.init_dimension_alpha(s, wealth=5)
        st.set_plan(s, entities=["a", "b"], dimensions=[], topics=[])
        st.add_dimension_candidate(s, name="pref", cite="c1", cycle=1)  # corrob 1 < K 3
        self.assertFalse(orch.accept_eligible(s))
        self.assertTrue(orch.goal_met(s))
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m unittest tests.test_orchestrator.BudgetAndDimensions -v`
Expected: FAIL — `module 'orchestrator' has no attribute 'accept_eligible'`.

- [ ] **Step 3: Write minimal implementation** — edit `scripts/orchestrator.py`:

Add after `recommend_phase` (line ~36):

```python
def accept_eligible(state, base_k=3):
    if state_mod.dimension_wealth_left(state) <= 0:
        return []
    thr = state_mod.dimension_threshold(state, base_k)
    return [c for c in state_mod.list_candidate_dimensions(state)
            if c.get("corroboration", 0) >= thr]
```

Replace `goal_met` (lines 39-44) with:

```python
def goal_met(state, min_sources=3):
    return (
        recommend_phase(state, min_sources) == "synthesize"
        and not _processable(state, min_sources)
        and len(state_mod.list_drafts(state, status="draft")) >= 1
        and not accept_eligible(state)
    )
```

In `decide` (lines 58-70), add the two fields to `result`:

```python
def decide(state, min_sources=3, apply=False):
    before = state["budget"]["phase"]
    rec = recommend_phase(state, min_sources)
    state_mod.set_phase(state, rec)
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
        state_mod.set_phase(state, before)
    return result
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python3 -m unittest tests.test_orchestrator -v`
Expected: PASS (all existing + 3 new; the existing `Decide`/`GoalMet` classes still pass because plans/budgets default absent → `accept_eligible` empty, `run_budget_exceeded` False).

- [ ] **Step 5: Commit**

```bash
git add scripts/orchestrator.py tests/test_orchestrator.py
git commit -m "feat(orchestrator): run-budget stop + dimension-stable goal_met"
```

---

## Task 6: `meter.py` — run-token metering from session transcript

**Files:**
- Create: `scripts/meter.py`
- Test: `tests/test_meter.py` (create)

**Interfaces:**
- Consumes: `state_mod.locked_state/set_run_tokens_spent`.
- Produces:
  - `sum_output_tokens(lines: list[str], since_iso: str|None=None) -> int` — parse JSONL transcript lines; for each record with `message.usage.output_tokens`, add it when `timestamp >= since_iso` (or `since_iso` is None). Ignore unparseable lines.
  - `estimate_tokens(subagents_dispatched: int, avg_output: int=8000) -> int` — `subagents_dispatched * avg_output`.
  - `update_run_spend(root, *, transcript_path=None, started_at=None, subagents_fallback=0) -> int` — if transcript readable, `set_run_tokens_spent(sum_output_tokens(...))`; else estimate; returns spent. (Transcript auto-discovery is environment-coupled; the function takes an explicit path and only the CLI tries discovery.)
  - CLI: `meter.py update --root R [--transcript PATH] [--fallback-subagents N]` → prints spent.

- [ ] **Step 1: Write the failing test**

```python
# tests/test_meter.py
import os, sys, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import meter


class SumTokens(unittest.TestCase):
    def test_sums_output_tokens(self):
        lines = [
            '{"timestamp":"2026-06-28T01:00:00Z","message":{"usage":{"output_tokens":100}}}',
            '{"timestamp":"2026-06-28T02:00:00Z","message":{"usage":{"output_tokens":250}}}',
            'not json',                                   # ignored
            '{"message":{"role":"user"}}',                # no usage, ignored
        ]
        self.assertEqual(meter.sum_output_tokens(lines), 350)

    def test_since_filter(self):
        lines = [
            '{"timestamp":"2026-06-28T01:00:00Z","message":{"usage":{"output_tokens":100}}}',
            '{"timestamp":"2026-06-28T03:00:00Z","message":{"usage":{"output_tokens":250}}}',
        ]
        self.assertEqual(meter.sum_output_tokens(lines, since_iso="2026-06-28T02:00:00Z"), 250)

    def test_estimate_fallback(self):
        self.assertEqual(meter.estimate_tokens(3, avg_output=8000), 24000)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m unittest tests.test_meter -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'meter'`.

- [ ] **Step 3: Write minimal implementation**

```python
# scripts/meter.py
"""Meter cumulative run tokens from the Claude Code session transcript. Stdlib only.

Primary: sum output_tokens from the transcript JSONL. Fallback: estimate from the
number of subagents dispatched. Never lets the run go unmetered.
"""
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import state as state_mod


def sum_output_tokens(lines, since_iso=None):
    total = 0
    for line in lines:
        line = line.strip()
        if not line:
            continue
        try:
            rec = json.loads(line)
        except json.JSONDecodeError:
            continue
        usage = (rec.get("message") or {}).get("usage") or {}
        out = usage.get("output_tokens")
        if out is None:
            continue
        ts = rec.get("timestamp")
        if since_iso and ts and ts < since_iso:
            continue
        total += out
    return total


def estimate_tokens(subagents_dispatched, avg_output=8000):
    return subagents_dispatched * avg_output


def _discover_transcript():
    """Best-effort: the active session transcript path, or None.

    Honors CLAUDE_TRANSCRIPT_PATH if set; otherwise returns None and the caller
    falls back to estimation. (Auto-walking the projects dir is left to the caller's
    environment to avoid guessing a fragile path here.)
    """
    p = os.environ.get("CLAUDE_TRANSCRIPT_PATH")
    return p if p and Path(p).exists() else None


def update_run_spend(root, *, transcript_path=None, started_at=None, subagents_fallback=0):
    path = transcript_path or _discover_transcript()
    if path and Path(path).exists():
        lines = Path(path).read_text(encoding="utf-8").splitlines()
        spent = sum_output_tokens(lines, since_iso=started_at)
    else:
        spent = estimate_tokens(subagents_fallback)
    with state_mod.locked_state(root) as st_:
        cur = st_["budget"].get("run", {}).get("tokens_spent", 0)
        # estimation is additive (per cycle); transcript sum is absolute
        st_["budget"].setdefault("run", {"token_ceiling": 0, "tokens_spent": 0})
        if path and Path(path).exists():
            st_["budget"]["run"]["tokens_spent"] = spent
        else:
            st_["budget"]["run"]["tokens_spent"] = cur + spent
        spent = st_["budget"]["run"]["tokens_spent"]
    return spent


def _main(argv):
    import argparse
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    u = sub.add_parser("update")
    u.add_argument("--root", default=".")
    u.add_argument("--transcript", default=None)
    u.add_argument("--fallback-subagents", type=int, default=0)
    args = ap.parse_args(argv)
    if args.cmd == "update":
        st_ = state_mod.load(args.root)
        started = st_["budget"].get("run", {}).get("started_at")
        spent = update_run_spend(args.root, transcript_path=args.transcript,
                                 started_at=started, subagents_fallback=args.fallback_subagents)
        print(spent)
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(_main(sys.argv[1:]))
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python3 -m unittest tests.test_meter -v`
Expected: PASS (3 tests).

- [ ] **Step 5: Commit**

```bash
git add scripts/meter.py tests/test_meter.py
git commit -m "feat(meter): run-token metering from session transcript + estimate fallback"
```

---

## Task 7: `dimension_gate.py` — deterministic eligibility + decision recording

**Files:**
- Create: `scripts/dimension_gate.py`
- Test: `tests/test_dimension_gate.py` (create)

**Interfaces:**
- Consumes: `orchestrator.accept_eligible`, `state_mod` accept/reject/spend helpers, `state_mod.run_budget_exceeded`.
- Produces:
  - `eligible(state, base_k=3) -> list` — thin wrapper over `orchestrator.accept_eligible(state, base_k)` (single source of truth) filtered further by run-budget headroom: returns `[]` if `run_budget_exceeded(state)`.
  - `expired(state, current_cycle, ttl=3) -> list` — pending candidates with `current_cycle - last_seen_cycle >= ttl` AND `corroboration < dimension_threshold(state, base_k=3)`.
  - `accept(state, name, *, now=None) -> dict` — `accept_dimension` + `spend_dimension_alpha`; returns the dimension.
  - `reject(state, name, *, reason, cycle) -> dict` — `reject_dimension`.
  - CLI: `dimension_gate.py eligible --root R [--cycle N]` prints candidate names (one per line) the agent should LLM-judge; `dimension_gate.py accept --root R --name N`; `dimension_gate.py reject --root R --name N --reason S --cycle K`; `dimension_gate.py expire --root R --cycle N` (auto-rejects expired, prints count).

- [ ] **Step 1: Write the failing test**

```python
# tests/test_dimension_gate.py
import os, sys, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import state as st
import dimension_gate as gate


def _ready(corrob=3, wealth=5):
    s = st.load_default()
    st.set_plan(s, entities=["a", "b"], dimensions=[], topics=[])
    st.init_dimension_alpha(s, wealth=wealth)
    st.init_run_budget(s, token_ceiling=10**9, now="T")
    for i in range(corrob):
        st.add_dimension_candidate(s, name="pref", cite=f"c{i}", cycle=1)
    return s


class Eligible(unittest.TestCase):
    def test_eligible_when_corroborated_and_budget_ok(self):
        self.assertEqual([c["name"] for c in gate.eligible(_ready())], ["pref"])

    def test_not_eligible_when_budget_exhausted(self):
        s = _ready()
        st.set_run_tokens_spent(s, 10**9)
        self.assertEqual(gate.eligible(s), [])

    def test_accept_spends_wealth_and_moves_dimension(self):
        s = _ready()
        gate.accept(s, "pref", now="T")
        self.assertEqual([d["name"] for d in s["plan"]["dimensions"]], ["pref"])
        self.assertEqual(st.dimension_wealth_left(s), 4)

    def test_expire_rejects_stale_uncorroborated(self):
        s = st.load_default()
        st.set_plan(s, entities=["a", "b"], dimensions=[], topics=[])
        st.init_dimension_alpha(s, wealth=5)
        st.add_dimension_candidate(s, name="weak", cite="c1", cycle=1)  # corrob 1
        n = gate.expire(s, current_cycle=4, ttl=3)                      # 4-1>=3
        self.assertEqual(n, 1)
        self.assertEqual(s["plan"]["rejected_dimensions"][0]["name"], "weak")


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m unittest tests.test_dimension_gate -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'dimension_gate'`.

- [ ] **Step 3: Write minimal implementation**

```python
# scripts/dimension_gate.py
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
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python3 -m unittest tests.test_dimension_gate -v`
Expected: PASS (4 tests).

- [ ] **Step 5: Commit**

```bash
git add scripts/dimension_gate.py tests/test_dimension_gate.py
git commit -m "feat(dimension-gate): deterministic eligibility/expiry + decision recording"
```

---

## Task 8: `check_integrity.py` — validate plan/candidate cites resolve

**Files:**
- Modify: `scripts/check_integrity.py` (`check`, after the drafts loop ~line 42)
- Test: `tests/test_check_integrity.py` (add a case)

**Interfaces:**
- Consumes: existing `corpus_ids` set in `check`.
- Produces: integrity problems for any `plan.candidate_dimensions[].evidence_cites` id not in `corpus_ids`. (Accepted `dimensions[].findings` reference draft ids and are validated only for membership in `drafts`; keep it to candidate cites for now to stay minimal.)

- [ ] **Step 1: Write the failing test** — add to `tests/test_check_integrity.py` (follow its existing temp-dir pattern; minimal standalone case shown):

```python
def test_candidate_dimension_dangling_cite(self):
    import json
    from pathlib import Path
    import check_integrity as ci
    root = self.make_root()                  # existing helper that seeds a .research dir
    sp = Path(root) / ".research" / "state.json"
    state = json.loads(sp.read_text())
    state["plan"] = {"entities": [], "dimensions": [], "topics": [],
                     "candidate_dimensions": [{"name": "x", "evidence_cites": ["cNOPE"],
                                               "corroboration": 1}],
                     "rejected_dimensions": []}
    sp.write_text(json.dumps(state))
    probs = ci.check(root)
    self.assertTrue(any("cNOPE" in p for p in probs))
```

(If `tests/test_check_integrity.py` has no `make_root` helper, construct the root inline with `tempfile.TemporaryDirectory` + `state.save`, matching the file's existing style — read the file first and mirror its setup.)

- [ ] **Step 2: Run test to verify it fails**

Run: `python3 -m unittest tests.test_check_integrity -v`
Expected: FAIL — the dangling candidate cite is not reported.

- [ ] **Step 3: Write minimal implementation** — in `scripts/check_integrity.py`, after the drafts loop (after line 42, before the assertions block):

```python
    plan = st.get("plan") or {}
    for c in plan.get("candidate_dimensions", []):
        for cid in c.get("evidence_cites", []):
            if cid not in corpus_ids:
                problems.append(
                    f"plan candidate {c.get('name')!r} dangling cite: {cid}")
```

- [ ] **Step 4: Run test to verify it passes**

Run: `python3 -m unittest tests.test_check_integrity -v`
Expected: PASS. Also confirm the live tree stays clean:
Run: `python3 scripts/check_integrity.py`
Expected: `integrity OK`.

- [ ] **Step 5: Commit**

```bash
git add scripts/check_integrity.py tests/test_check_integrity.py
git commit -m "feat(integrity): validate plan candidate-dimension cites resolve to corpus"
```

---

## Task 9: `.claude/research.md` — the planner flow

**Files:**
- Create: `.claude/research.md`
- Test: `tests/test_research_flow.sh` (create, smoke)

**Interfaces:**
- Consumes: `plan.py apply`, `state.py`, the existing `/goal` loop (`.claude/goal.md`).
- Produces: the documented `/research` procedure. No code symbols; it is an agent procedure mirroring `.claude/goal.md` / `.claude/process.md`.

- [ ] **Step 1: Write the failing smoke test**

```bash
# tests/test_research_flow.sh
#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
test -f .claude/research.md || { echo "FAIL: .claude/research.md missing"; exit 1; }
# the flow must reference the three load-bearing steps
grep -q "plan.py apply" .claude/research.md || { echo "FAIL: no plan.py apply step"; exit 1; }
grep -q "validate" .claude/research.md || { echo "FAIL: no validation/halt step"; exit 1; }
grep -qi "goal.md\|/goal" .claude/research.md || { echo "FAIL: no handoff to /goal loop"; exit 1; }
echo "PASS research flow doc"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `bash tests/test_research_flow.sh`
Expected: `FAIL: .claude/research.md missing`.

- [ ] **Step 3: Write the flow** — `.claude/research.md`:

```markdown
<!-- .claude/research.md -->
# Research flow — one-prompt autonomous bootstrap

Turn ONE natural-language prompt into a fully autonomous research run. Invoked as
`/research "<prompt>" [--budget <tokens>] [--root <dir>]` (default budget 2000000,
default root `.`). Do exactly this, then hand off to the `/goal` loop:

1. **Classify the research shape** of the prompt: one of `comparison`, `survey`,
   `causal`, `how-to`, `chronology`. If unsure, use `survey`.
2. **Decompose** the prompt into a plan and write it to `.research/plan-input.json`
   (under `--root`). Emit exactly this schema:
   ```json
   {
     "shape": "comparison",
     "entities": ["Boeing 777", "Airbus A380"],
     "dimensions": [{"name": "fuel economy", "why": "..."}],
     "topics": [],
     "seed_gaps": [{"topic": "fuel economy", "desc": "Boeing 777 fuel burn per seat"}],
     "rationale": "..."
   }
   ```
   - `comparison`/`causal`: populate `entities` + `dimensions`; for each
     `entity × dimension` cell emit one `seed_gap`.
   - `survey`/`how-to`/`chronology`: populate `topics`; emit `seed_gaps` per topic.
   - Keep the plan grounded and concise — it does not need to be exhaustive; the
     dimension-discovery gate (step 4 of the goal loop) extends it as the run learns.
3. **Apply the plan** (pure code validates it; an invalid plan halts BEFORE any tokens
   are spent — this is the only pre-launch stop):
   ```
   python3 scripts/plan.py apply --root <root> --question "<prompt>" \
     --budget <tokens> --plan-file <root>/.research/plan-input.json
   ```
   If it exits non-zero, surface the `invalid plan: …` message and STOP — fix the plan
   JSON and retry; do not launch the loop on an invalid plan.
4. **Start the run log and meter baseline:**
   ```
   python3 scripts/runlog.py start
   python3 scripts/meter.py update --root <root>   # records run-start token baseline
   ```
5. **Hand off to the autonomous loop:** run the `/goal` loop exactly as defined in
   `.claude/goal.md` (it now meters tokens and runs the dimension gate each cycle, and
   stops on plateau OR run-budget OR cycle cap). Do not re-implement the loop here.

The run is fully autonomous after step 3; the only human-visible stop before completion
is an invalid-plan halt.
```

- [ ] **Step 4: Run test to verify it passes**

Run: `bash tests/test_research_flow.sh`
Expected: `PASS research flow doc`.

- [ ] **Step 5: Commit**

```bash
git add .claude/research.md tests/test_research_flow.sh
git commit -m "feat(flow): /research one-prompt bootstrap flow"
```

---

## Task 10: Wire metering + dimension gate into `.claude/goal.md` and candidate emission into `.claude/process.md`

**Files:**
- Modify: `.claude/goal.md` (add meter step + dimension-gate step + budget stop)
- Modify: `.claude/process.md` (emit dimension candidates while drafting)
- Test: `tests/test_goal_loop_wiring.sh` (create, smoke)

**Interfaces:**
- Consumes: `meter.py update`, `dimension_gate.py eligible/accept/reject/expire`, `state.py add-dim-candidate`, `orchestrator.py decide` (now returns `stop`).
- Produces: documented loop steps; no new code symbols.

- [ ] **Step 1: Write the failing smoke test**

```bash
# tests/test_goal_loop_wiring.sh
#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
grep -q "meter.py update" .claude/goal.md || { echo "FAIL: goal.md missing meter step"; exit 1; }
grep -q "dimension_gate.py" .claude/goal.md || { echo "FAIL: goal.md missing dimension gate"; exit 1; }
grep -q '"stop"' .claude/goal.md || grep -q "D.stop" .claude/goal.md || { echo "FAIL: goal.md not stopping on D.stop"; exit 1; }
grep -q "add-dim-candidate" .claude/process.md || { echo "FAIL: process.md not emitting candidates"; exit 1; }
echo "PASS loop wiring"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `bash tests/test_goal_loop_wiring.sh`
Expected: `FAIL: goal.md missing meter step`.

- [ ] **Step 3: Edit the flows.**

In `.claude/goal.md` step 2 (Decide), change the stop condition from `D.goal_met` to `D.stop`, and add a clause distinguishing budget stop from plateau. Replace the bullet:

> - If `D.goal_met` is `true`: **stop**. …

with:

```markdown
   - If `D.stop` is `true`: **stop**. If `D.goal_met` is true, report convergence
     (plateau). If instead `D.budget_exhausted` is true, report the run was cut short on
     budget: print the finding/dimension counts and the pending-candidate count so the
     user knows it did not fully converge. Then surface the review queue + stuck gaps
     (`python3 scripts/promote.py queue`; `python3 scripts/state.py list-gaps --status failed`),
     close the run log (`python3 scripts/runlog.py end --status ok`), and run no more cycles.
```

After step 4 (Process), add a new step 4b (Dimension gate):

```markdown
4b. **Dimension gate** (plan growth — runs every cycle, see `.claude/research.md` and
    the spec's §1.5). Do exactly this:
    - List deterministically-eligible candidates:
      `python3 scripts/dimension_gate.py eligible --root <root>` (these already pass the
      corroboration threshold, have α-wealth left, and fit the remaining budget).
    - For EACH eligible candidate, judge the three LLM axes against `goal.question` in
      `.research/state.json`: (1) goal-relevance, (2) distinctness from existing
      `plan.dimensions`, (3) comparability — both entities are scoreable on it
      (comparison shape only). Accept only if all three pass.
      - Accept: `python3 scripts/dimension_gate.py accept --root <root> --name "<name>"`,
        then seed one gap per `entity × new dimension`
        (`python3 scripts/state.py add-gap --topic "<name>" --desc "<entity> <name>" --origin dimension`).
      - Reject: `python3 scripts/dimension_gate.py reject --root <root> --name "<name>" --reason "<axis that failed>" --cycle K`.
    - Expire stale candidates: `python3 scripts/dimension_gate.py expire --root <root> --cycle K`.
    - Log: `python3 scripts/runlog.py log --flow dimension --step gate --status ok --data "{\"accepted\":A,\"rejected\":R}"`.
```

Before step 5 (Safety), add the meter step:

```markdown
4c. **Meter.** Update cumulative run-token spend so the next `decide` sees it:
    `python3 scripts/meter.py update --root <root> --fallback-subagents <subagents dispatched this cycle>`.
```

In `.claude/process.md`, in step 6 (Emit gaps), add a sibling instruction:

```markdown
   Also emit DIMENSION CANDIDATES: if a source raised a substantive comparable aspect
   that is NOT already a `plan.dimension` and is on-goal, record it (corroboration
   accumulates across cycles — record it every time a source raises it, with that
   source's corpus id):
   `python3 scripts/state.py add-dim-candidate --root <root> --name "<aspect>" --cite "<c-id>" --cycle K`
   Do not accept it here — the goal loop's dimension gate (step 4b) decides acceptance.
```

- [ ] **Step 4: Run test to verify it passes**

Run: `bash tests/test_goal_loop_wiring.sh`
Expected: `PASS loop wiring`.

- [ ] **Step 5: Commit**

```bash
git add .claude/goal.md .claude/process.md tests/test_goal_loop_wiring.sh
git commit -m "feat(loop): wire metering, dimension gate, budget-stop, candidate emission"
```

---

## Task 11: Full-suite regression + end-to-end plan→state smoke

**Files:**
- Create: `tests/test_planner_e2e.sh` (smoke)

**Interfaces:** exercises Tasks 1-8 together against a temp root.

- [ ] **Step 1: Write the smoke test**

```bash
# tests/test_planner_e2e.sh
#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
ROOT="$(mktemp -d)"
cat > "$ROOT/plan.json" <<'JSON'
{"shape":"comparison","entities":["777","A380"],
 "dimensions":[{"name":"fuel","why":"x"},{"name":"range","why":"y"}],
 "topics":[],
 "seed_gaps":[{"topic":"fuel","desc":"777 fuel"},{"topic":"range","desc":"A380 range"}],
 "rationale":"r"}
JSON
python3 scripts/plan.py apply --root "$ROOT" --question "777 vs A380" --budget 1000000 --plan-file "$ROOT/plan.json"
# goal record + queued gaps + run budget present
python3 - "$ROOT" <<'PY'
import json, sys
s = json.load(open(sys.argv[1] + "/.research/state.json"))
assert s["goal"]["shape"] == "comparison", s["goal"]
assert len([g for g in s["gaps"] if g["status"] == "queued"]) == 2
assert s["budget"]["run"]["token_ceiling"] == 1000000
assert s["budget"]["dimension_alpha"]["wealth"] == 5
print("e2e state OK")
PY
# budget stop fires when spent >= ceiling
python3 scripts/state.py set-run-spent --root "$ROOT" --tokens 1000000 >/dev/null
python3 scripts/orchestrator.py decide --root "$ROOT" | python3 -c 'import json,sys; d=json.load(sys.stdin); assert d["stop"] and d["budget_exhausted"], d; print("e2e stop OK")'
rm -rf "$ROOT"
echo "PASS planner e2e"
```

- [ ] **Step 2: Run it (expect pass once Tasks 1-8 are merged)**

Run: `bash tests/test_planner_e2e.sh`
Expected: `e2e state OK` / `e2e stop OK` / `PASS planner e2e`.

- [ ] **Step 3: Run the whole unit suite**

Run: `python3 -m unittest discover -s tests -p 'test_*.py' -v`
Expected: all green (existing + new). If any existing test broke, the cause is almost certainly a non-`.get()` read of a new block — fix the reader, not the test.

- [ ] **Step 4: Integrity check on the live repo (must stay clean)**

Run: `python3 scripts/check_integrity.py`
Expected: `integrity OK`.

- [ ] **Step 5: Commit**

```bash
git add tests/test_planner_e2e.sh
git commit -m "test: end-to-end planner bootstrap smoke (plan apply -> state -> budget stop)"
```

---

## Task 12 (separable): `.claude/report.md` — on-demand report assembler

> Per spec §4 this is separable. Build it last, or split into its own plan if Tasks 1-11 are merged first. Findings are the deliverable; the report is a deterministic view over them.

**Files:**
- Create: `.claude/report.md`
- Test: `tests/test_report_flow.sh` (smoke)

**Interfaces:**
- Consumes: `state.json` (`goal`, `plan`), `docs/findings/*.md`. Produces a documented `/report` procedure; output `docs/comparison-report.md` (or `docs/report.md` for non-comparison shapes).

- [ ] **Step 1: Write the failing smoke test**

```bash
# tests/test_report_flow.sh
#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
test -f .claude/report.md || { echo "FAIL: .claude/report.md missing"; exit 1; }
grep -qi "plan" .claude/report.md && grep -qi "findings" .claude/report.md \
  || { echo "FAIL: report flow must read plan + findings"; exit 1; }
grep -qi "citation\|\[c" .claude/report.md || { echo "FAIL: report must carry citations"; exit 1; }
echo "PASS report flow doc"
```

- [ ] **Step 2: Run test to verify it fails**

Run: `bash tests/test_report_flow.sh`
Expected: `FAIL: .claude/report.md missing`.

- [ ] **Step 3: Write the flow** — `.claude/report.md`:

```markdown
<!-- .claude/report.md -->
# Report flow — assemble a narrative from findings (on demand)

Invoked as `/report [--root <dir>]` after a `/research` run reaches plateau. Deterministic
view over the promoted findings; never part of the autonomous loop. Do exactly this:

1. Read `.research/state.json`: `goal` (question, shape) and `plan` (entities, dimensions
   or topics, with each accepted dimension/topic's `findings`).
2. Read the promoted findings under `docs/findings/` (status `promoted` in
   `state.json.drafts`).
3. Assemble `docs/comparison-report.md` (comparison/causal shape) or `docs/report.md`
   (otherwise):
   - Title from `goal.question`.
   - For a comparison: a matrix table of `entities × dimensions`, each cell summarizing the
     relevant findings; then one section per dimension.
   - For a survey/how-to/chronology: one section per topic.
   - Every load-bearing statement carries its finding's primary `[c…]` citation, resolved
     from the finding's `cites`. Do not introduce uncited claims.
4. Print the output path. Do not modify any finding or state — report generation is
   read-only over the corpus.
```

- [ ] **Step 4: Run test to verify it passes**

Run: `bash tests/test_report_flow.sh`
Expected: `PASS report flow doc`.

- [ ] **Step 5: Commit**

```bash
git add .claude/report.md tests/test_report_flow.sh
git commit -m "feat(flow): /report on-demand report assembler"
```

---

## Self-review (completed by plan author)

**Spec coverage:**
- §1 components/state blocks → Tasks 1-2 (state), 9 (research flow), 12 (report). ✓
- §1.5 dimension control loop → Tasks 1 (candidates), 2 (α-wealth), 5 (accept-eligible blocks plateau), 7 (gate), 10 (flow wiring). ✓
- §2 planner contract → Tasks 3-4 (validate/cap/apply), 9 (flow emits the schema). ✓
- §3 metering + stop → Task 6 (meter), 5 (decide stop), 10 (loop meter step). ✓
- §4 report → Task 12. ✓
- §5 error handling → Task 4 (invalid plan raises/halts), 9 (flow halts), existing flow reuse. ✓
- §6 testing → every task is TDD; Task 11 full-suite + e2e. ✓
- §7 portability → every CLI carries `--root`; no cwd hardcoding (Global Constraints). ✓

**Placeholder scan:** no TBD/TODO; all code steps show complete code. ✓ (Task 8's test notes a fallback if `make_root` is absent — that is an explicit instruction to mirror the file's existing setup, not a placeholder.)

**Type consistency:** helper names/signatures in Interfaces match their definitions and call sites across tasks (`accept_eligible`, `dimension_threshold`, `run_budget_exceeded`, `eligible`, `apply_plan`, `update_run_spend`). `decide` output keys (`stop`, `budget_exhausted`, `goal_met`) consistent between Task 5 and Task 10. ✓
```
