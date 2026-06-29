# ORS: The Package — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Turn the open-research-system repo into a self-contained, personal, local Claude Code plugin so `/ors:research` and `/ors:report` run from any target project, writing all artifacts into that target.

**Architecture:** The repo root *becomes* the plugin (`.claude-plugin/plugin.json` + `bin/ors` + `skills/`). A `bin/ors` dispatcher (on the Bash tool PATH while the plugin is enabled) is the single engine entrypoint that survives the harness's non-persistent shells and bakes in the env contract (`REPO_ROOT=$PWD`, `DOCS_BASE=.research/docs`). The agent-facing flow docs move from `.claude/*.md` into `skills/`, with every `python3 scripts/X.py` rewritten to `ors <verb>`. A single `DOCS_BASE` convention namespaces all research output under `<target>/.research/docs`.

**Tech Stack:** python3 (stdlib only), bash, Claude Code plugin format.

**Spec:** `docs/superpowers/specs/2026-06-29-ors-package-design.md`

## Global Constraints

- **python3 only** (never `python`); **stdlib only** in engine scripts — no new deps.
- **Backward-compat is load-bearing:** new `state.json` blocks stay additive, read via `.get()`; never add to `check_integrity.REQUIRED_KEYS`; `DEFAULT_STATE` unmodified.
- **Protected files — never stage/commit without explicit user say-so:** `public/dashboard.html` (the user's), `.research/*.log` (gitignored), `.graphify/`.
- **Branch off `main`** (`feat/ors-package`); **no git worktrees**; explicit staging (never `git add .`/`-A`); **Conventional Commits**; **no co-author trailer**.
- **TDD per task; independent reviewer per task; `python3 scripts/check_integrity.py` green before any task is "done".**
- **`DOCS_BASE` default = `.research/docs`** — the single namespacing switch, uniform for all runs.
- **Verb table (authoritative for all `ors` rewrites):**

  | flow-doc call | `ors` verb |
  |---|---|
  | `python3 scripts/plan.py …` | `ors plan …` |
  | `python3 scripts/orchestrator.py decide …` | `ors decide …` |
  | `python3 scripts/dimension_gate.py …` | `ors dim …` |
  | `python3 scripts/meter.py …` | `ors meter …` |
  | `python3 scripts/state.py …` | `ors state …` |
  | `python3 scripts/runlog.py …` | `ors runlog …` |
  | `python3 scripts/promote.py …` | `ors promote …` |
  | `python3 scripts/check_integrity.py …` | `ors check_integrity …` |
  | `python3 scripts/cite_check.py …` | `ors cite_check …` |
  | `python3 scripts/graph_events.py …` | `ors graph_events …` |
  | `python3 scripts/verify_run.py …` | `ors verify_run …` |
  | `python3 scripts/export_csl.py …` | `ors export_csl …` |
  | `bash scripts/search_flow.sh …` | `ors search …` |
  | `bash scripts/ingest_flow.sh …` | `ors ingest …` |
  | `bash scripts/gather.sh …` | `ors gather …` |

**Baseline before starting:** `python3 -m unittest discover -s tests -p 'test_*.py'` → 164 OK; the 4 shell smokes PASS; `python3 scripts/check_integrity.py` → `integrity OK`.

**SDD ledger:** append progress to `.superpowers/sdd/progress.md` (gitignored) per task.

---

## Pre-task setup (fold into Task 1's commit)

Create the branch and the ledger:

```bash
cd /Users/joshua/Documents/GitHub/open-research-system
git checkout main && git pull --ff-only 2>/dev/null; git checkout -b feat/ors-package
mkdir -p .superpowers/sdd
printf '# ORS package — SDD progress ledger\nPlan: docs/superpowers/plans/2026-06-29-ors-package.md\nBranch: feat/ors-package\nBASE: %s\n\n## Tasks\n' "$(git rev-parse --short HEAD)" > .superpowers/sdd/progress.md
```

---

## Task 1: `DOCS_BASE` helper + `resolve_topic_dir`

Introduce the single namespacing knob and apply it to topic-dir resolution.

**Files:**
- Modify: `scripts/state.py` (add `docs_base()` helper near the top, after imports)
- Modify: `scripts/lib.sh:7-25` (`resolve_topic_dir`)
- Test: `tests/test_resolve_topic_dir.sh` (update expectations to `.research/docs`)
- Test: `tests/test_docs_base.py` (new — the python helper)

**Interfaces:**
- Produces: `state.docs_base() -> str` returns `os.environ.get("DOCS_BASE", ".research/docs")`.
- Produces: bash `resolve_topic_dir <root> <topic>` creates/returns `<root>/$DOCS_BASE/NN-<slug>` where `DOCS_BASE` defaults to `.research/docs`.

- [ ] **Step 1: Write the failing python test**

Create `tests/test_docs_base.py`:

```python
import os, sys, unittest
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
import state


class DocsBase(unittest.TestCase):
    def test_default(self):
        os.environ.pop("DOCS_BASE", None)
        self.assertEqual(state.docs_base(), ".research/docs")

    def test_env_override(self):
        os.environ["DOCS_BASE"] = "custom/dir"
        try:
            self.assertEqual(state.docs_base(), "custom/dir")
        finally:
            os.environ.pop("DOCS_BASE", None)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run it to verify it fails**

Run: `python3 -m unittest tests.test_docs_base -v`
Expected: FAIL — `AttributeError: module 'state' has no attribute 'docs_base'`.

- [ ] **Step 3: Add the helper to `scripts/state.py`**

After the existing imports at the top of `scripts/state.py`, add:

```python
def docs_base():
    """Root-relative base dir for research output (topic dirs + findings)."""
    import os
    return os.environ.get("DOCS_BASE", ".research/docs")
```

- [ ] **Step 4: Run it to verify it passes**

Run: `python3 -m unittest tests.test_docs_base -v` → Expected: PASS (2 tests).

- [ ] **Step 5: Update the bash test to the new convention**

In `tests/test_resolve_topic_dir.sh`, replace the three `$TMP/docs/...` expectations with `$TMP/.research/docs/...`:
- `[ "$d" = "$TMP/docs/01-columnar-storage" ]` → `[ "$d" = "$TMP/.research/docs/01-columnar-storage" ]`
- `[ "$d3" = "$TMP/docs/02-vectorized-execution" ]` → `[ "$d3" = "$TMP/.research/docs/02-vectorized-execution" ]`

- [ ] **Step 6: Run the bash test to verify it now fails**

Run: `bash tests/test_resolve_topic_dir.sh` → Expected: FAIL (still creates `docs/`, not `.research/docs/`).

- [ ] **Step 7: Update `resolve_topic_dir` in `scripts/lib.sh`**

Replace the body of `resolve_topic_dir` (currently using `$root/docs`) so it reads `DOCS_BASE` (default `.research/docs`):

```bash
resolve_topic_dir() {
  local root="$1" slug match next base
  base="${DOCS_BASE:-.research/docs}"
  slug="$(slugify "$2")"
  match=$(find "$root/$base" -maxdepth 1 -type d -name "*${slug}*" 2>/dev/null \
            | grep -E '/[0-9]{2}-[^/]+$' | head -1)
  if [ -z "$match" ]; then
    next=$(find "$root/$base" -maxdepth 1 -type d 2>/dev/null \
             | grep -oE '/[0-9]{2}-' | tr -dc '0-9\n' | sort -n | tail -1)
    next=$(printf '%02d' $(( 10#${next:-0} + 1 )))
    match="$root/$base/${next}-${slug}"
    mkdir -p "$match" || { echo "could not create topic dir '$match'" >&2; return 1; }
  fi
  echo "$match"
}
```

(Keep the existing explanatory comment block above the function.)

- [ ] **Step 8: Run both tests**

Run: `bash tests/test_resolve_topic_dir.sh && python3 -m unittest tests.test_docs_base -v`
Expected: both PASS.

- [ ] **Step 9: Branch + commit**

Run the Pre-task setup block above first (creates `feat/ors-package` + ledger), then:

```bash
git add scripts/state.py scripts/lib.sh tests/test_resolve_topic_dir.sh tests/test_docs_base.py
git commit -m "feat(docs-base): DOCS_BASE knob + resolve_topic_dir namespaces under .research/docs"
```

---

## Task 2: `promote.py` + `ingest.sh` honor `DOCS_BASE`

Move findings output under `DOCS_BASE`.

**Files:**
- Modify: `scripts/promote.py:8-9` (`FINDINGS_DIR`, `SYNTHESIS`)
- Modify: `scripts/ingest.sh:14` (findings fallback)
- Test: `tests/test_promote.py` (update `docs/findings` → `.research/docs/findings`)

**Interfaces:**
- Consumes: `state.docs_base()` from Task 1.
- Produces: `promote.py` writes findings to `<docs_base>/findings/` + `<docs_base>/findings/SYNTHESIS.md`.

- [ ] **Step 1: Update `tests/test_promote.py` to the new paths (failing test)**

Replace every literal `docs/findings` in `tests/test_promote.py` with `.research/docs/findings`. The affected lines are 11, 17, 26, 29, 58, 59, 60, 76, 88, 91, 96, 103, 107. Example:
- `drafts_dir = Path(root) / "docs/findings/_drafts"` → `Path(root) / ".research/docs/findings/_drafts"`
- `out = state.promote_draft(st, d["id"], "docs/findings/p.md", …)` → `"…/.research/docs/findings/p.md"`
- `self.assertEqual(out["promoted_path"], "docs/findings/p.md")` → `".research/docs/findings/p.md"`

(Mechanical: `sed -i '' 's#docs/findings#.research/docs/findings#g' tests/test_promote.py` then eyeball the diff.)

- [ ] **Step 2: Run to verify it fails**

Run: `python3 -m unittest tests.test_promote -v`
Expected: FAIL — promote still writes/returns `docs/findings/...`.

- [ ] **Step 3: Update `scripts/promote.py`**

Replace lines 8-9:

```python
FINDINGS_DIR = "docs/findings"
SYNTHESIS = "docs/findings/SYNTHESIS.md"
```

with module-level derivation from the helper (add `import state` if not already imported at top — it is via the existing `sys.path` block; confirm):

```python
import state as _state
FINDINGS_DIR = _state.docs_base() + "/findings"
SYNTHESIS = FINDINGS_DIR + "/SYNTHESIS.md"
```

If `promote.py` already imports `state` under another name, reuse that name instead of `_state` (check the top of the file; do not double-import).

- [ ] **Step 4: Run to verify it passes**

Run: `python3 -m unittest tests.test_promote -v` → Expected: PASS.

- [ ] **Step 5: Update `scripts/ingest.sh:14`**

Replace the findings fallback so it uses `DOCS_BASE`:

```bash
if [ "${1:-}" ]; then dest="$(resolve_topic_dir "$ROOT" "$1")/sources"; else dest="$ROOT/${DOCS_BASE:-.research/docs}/findings"; fi
```

- [ ] **Step 6: Commit**

```bash
git add scripts/promote.py scripts/ingest.sh tests/test_promote.py
git commit -m "feat(docs-base): promote + ingest findings under DOCS_BASE"
```

---

## Task 3: Migrate remaining engine-behavior tests + gitignore; whole-suite green

Sweep the rest of the engine tests onto `.research/docs`, keep the legacy-corpus catalog test on `docs/`, and ignore generated output in git.

**Files:**
- Modify tests (engine behavior): `tests/test_check_integrity.py`, `tests/test_process_state.py`, `tests/test_ingest.sh`, `tests/test_ingest_flow.sh`, `tests/test_ingest_flow_inbox.sh`, `tests/test_search_flow.sh`, `tests/test_process_flow.sh`, `tests/test_gather.sh`
- **Leave unchanged:** `tests/test_catalog.sh` (validates the *frozen legacy corpus* `docs/01-10`, which is out of scope to migrate per the spec), and `tests/test_state.py:48` (the `extracted_path` is an opaque stored string, not a path the code resolves)
- Modify: `.gitignore` (add generated research output)

**Interfaces:** none new — this task only realigns fixtures to Task 1/2's convention.

- [ ] **Step 1: Update each engine test's `docs/` fixtures to `.research/docs/`**

For each file in the "engine behavior" list, replace topic/findings path literals:
- `docs/findings/...` → `.research/docs/findings/...`
- `docs/NN-...` / `docs/06-rag-retrieval` / `docs/11-x` / `docs/<T>` topic dirs → `.research/docs/<same>`
- `mkdir -p "$TMP/docs/..."` fixtures → `"$TMP/.research/docs/..."`

Do NOT touch `tests/test_catalog.sh` or `tests/test_state.py`.

- [ ] **Step 2: Run the full unit suite**

Run: `python3 -m unittest discover -s tests -p 'test_*.py' 2>&1 | tail -3`
Expected: OK (count = 164 + 2 new from Task 1 = 166).

- [ ] **Step 3: Run all shell smokes**

Run:
```bash
for t in research_flow goal_loop_wiring planner_e2e report_flow resolve_topic_dir \
         ingest_flow ingest_flow_inbox ingest gather search_flow process_flow catalog; do
  printf "%s: " "$t"; bash tests/test_$t.sh >/dev/null 2>&1 && echo PASS || echo FAIL; done
```
Expected: all PASS. (If `catalog` fails, the legacy `docs/01-10` corpus must still exist on the branch — it does; do not migrate it.)

- [ ] **Step 4: Verify integrity**

Run: `python3 scripts/check_integrity.py` → Expected: `integrity OK`.

- [ ] **Step 5: Ignore generated research output in git**

Append to `.gitignore` (the state *spine* stays committed; only generated corpus/findings output is ignored):

```
# research output (corpus topic dirs + findings) is generated, not committed
.research/docs/
```

- [ ] **Step 6: Commit**

```bash
git add tests/test_check_integrity.py tests/test_process_state.py tests/test_ingest.sh \
        tests/test_ingest_flow.sh tests/test_ingest_flow_inbox.sh tests/test_search_flow.sh \
        tests/test_process_flow.sh tests/test_gather.sh .gitignore
git commit -m "test(docs-base): migrate engine tests to .research/docs; ignore generated output"
```

---

## Task 4: `bin/ors` dispatcher

The single engine entrypoint.

**Files:**
- Create: `bin/ors`
- Test: `tests/test_ors_dispatch.sh`

**Interfaces:**
- Produces: `ors <verb> [args]` resolves a verb to a bundled script, exports `REPO_ROOT` (default `$PWD`) and `DOCS_BASE` (default `.research/docs`), and execs it. Verb table per Global Constraints.

- [ ] **Step 1: Write the failing test**

Create `tests/test_ors_dispatch.sh`:

```bash
#!/usr/bin/env bash
set -uo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
ORS="$ROOT/bin/ors"
fail=0

# 1. Generic python verb resolves to scripts/<verb>.py (plan.py prints usage on --help).
"$ORS" plan --help >/dev/null 2>&1 && echo "ok: plan verb runs" \
  || { echo "MISS: plan verb"; fail=1; }

# 2. Alias: decide -> orchestrator.py (has a 'decide' subcommand).
"$ORS" decide --help >/dev/null 2>&1 && echo "ok: decide alias" \
  || { echo "MISS: decide alias"; fail=1; }

# 3. Shell-flow verb: search -> search_flow.sh (usage exit 2 when no --topic).
"$ORS" search >/dev/null 2>&1; [ $? -eq 2 ] && echo "ok: search alias" \
  || { echo "MISS: search alias"; fail=1; }

# 4. Unknown verb exits 2.
"$ORS" nonsense >/dev/null 2>&1; [ $? -eq 2 ] && echo "ok: unknown verb exit 2" \
  || { echo "MISS: unknown verb"; fail=1; }

# 5. Defaults exported (run a verb that echoes them via a tiny probe).
out="$(REPO_ROOT= DOCS_BASE= "$ORS" __envprobe 2>/dev/null)"
echo "$out" | grep -q "REPO_ROOT=$PWD" && echo "ok: REPO_ROOT default" \
  || { echo "MISS: REPO_ROOT default ($out)"; fail=1; }
echo "$out" | grep -q "DOCS_BASE=.research/docs" && echo "ok: DOCS_BASE default" \
  || { echo "MISS: DOCS_BASE default ($out)"; fail=1; }

[ "$fail" = 0 ] && echo "ALL OK" || echo "FAILED"
exit "$fail"
```

- [ ] **Step 2: Run to verify it fails**

Run: `bash tests/test_ors_dispatch.sh` → Expected: FAIL (`bin/ors` missing).

- [ ] **Step 3: Create `bin/ors`**

```bash
#!/usr/bin/env bash
# Single engine entrypoint. On the Bash-tool PATH while the plugin is enabled,
# so flow docs call `ors <verb>` from any (non-persistent) shell. Resolves the
# verb to a bundled script and bakes in the env contract.
set -euo pipefail
HERE="$(cd "$(dirname "$0")/.." && pwd)"          # plugin/repo root
export REPO_ROOT="${REPO_ROOT:-$PWD}"             # target project
export DOCS_BASE="${DOCS_BASE:-.research/docs}"    # uniform output namespace
verb="${1:?usage: ors <verb> [args]}"; shift || true
case "$verb" in
  __envprobe) echo "REPO_ROOT=$REPO_ROOT"; echo "DOCS_BASE=$DOCS_BASE"; exit 0 ;;
  decide) exec python3 "$HERE/scripts/orchestrator.py" "$@" ;;
  dim)    exec python3 "$HERE/scripts/dimension_gate.py" "$@" ;;
  search) exec bash    "$HERE/scripts/search_flow.sh" "$@" ;;
  ingest) exec bash    "$HERE/scripts/ingest_flow.sh" "$@" ;;
  gather) exec bash    "$HERE/scripts/gather.sh" "$@" ;;
  *)
    if   [ -f "$HERE/scripts/$verb.py" ]; then exec python3 "$HERE/scripts/$verb.py" "$@"
    elif [ -f "$HERE/scripts/$verb.sh" ]; then exec bash    "$HERE/scripts/$verb.sh" "$@"
    else echo "ors: unknown verb '$verb'" >&2; exit 2; fi ;;
esac
```

Then: `chmod +x bin/ors`.

- [ ] **Step 4: Run to verify it passes**

Run: `bash tests/test_ors_dispatch.sh` → Expected: ALL OK.

- [ ] **Step 5: Commit**

```bash
git add bin/ors tests/test_ors_dispatch.sh
git commit -m "feat(ors): bin/ors dispatcher — single engine entrypoint on plugin PATH"
```

---

## Task 5: Plugin manifest + move internal flows into `skills/_flows/`

Scaffold the plugin manifest and relocate the four internal procedure docs, rewriting their engine calls to `ors`.

**Files:**
- Create: `.claude-plugin/plugin.json`
- Move: `.claude/goal.md` → `skills/_flows/goal.md`; `.claude/loop.md` → `skills/_flows/loop.md`; `.claude/process.md` → `skills/_flows/process.md`; `.claude/review.md` → `skills/_flows/review.md`
- Test: `tests/test_plugin_manifest.py`

**Interfaces:**
- Produces: `.claude-plugin/plugin.json` with `name: "ors"`; `skills/_flows/{goal,loop,process,review}.md` containing zero raw `python3 scripts/`/`bash scripts/` calls (all rewritten to `ors`).

- [ ] **Step 1: Write the failing test**

Create `tests/test_plugin_manifest.py`:

```python
import json, os, re, unittest
ROOT = os.path.join(os.path.dirname(__file__), "..")


class Manifest(unittest.TestCase):
    def test_manifest_valid(self):
        m = json.load(open(os.path.join(ROOT, ".claude-plugin/plugin.json")))
        self.assertEqual(m["name"], "ors")
        self.assertTrue(m.get("description"))

    def test_flows_have_no_raw_script_calls(self):
        d = os.path.join(ROOT, "skills/_flows")
        for fn in ("goal.md", "loop.md", "process.md", "review.md"):
            txt = open(os.path.join(d, fn)).read()
            self.assertNotRegex(txt, r"python3 scripts/", fn)
            self.assertNotRegex(txt, r"bash scripts/", fn)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run to verify it fails**

Run: `python3 -m unittest tests.test_plugin_manifest -v`
Expected: FAIL — `.claude-plugin/plugin.json` and `skills/_flows/` do not exist.

- [ ] **Step 3: Create the manifest**

Create `.claude-plugin/plugin.json`:

```json
{
  "name": "ors",
  "description": "Open Research System — one-prompt autonomous research against any project's directory.",
  "version": "0.1.0",
  "author": { "name": "Joshua Tyler" }
}
```

- [ ] **Step 4: Move the four flow docs and rewrite their engine calls**

```bash
mkdir -p skills/_flows
git mv .claude/goal.md skills/_flows/goal.md
git mv .claude/loop.md skills/_flows/loop.md
git mv .claude/process.md skills/_flows/process.md
git mv .claude/review.md skills/_flows/review.md
```

In each moved file, apply the **verb table** (Global Constraints): replace every `python3 scripts/<X>.py` with `ors <verb>` and every `bash scripts/<Y>.sh` with `ors <verb>`. Also rewrite the literal output-path references in `skills/_flows/process.md` (lines were 13, 14, 35, 40, 72, 119 in the original): `docs/<T>/sources/` → `$DOCS_BASE/<T>/sources/`, `docs/findings/` → `$DOCS_BASE/findings/` (the flow runs under `ors`, which exports `DOCS_BASE`). In `skills/_flows/loop.md`, the graphify/`.graphify` references stay as-is (graphify owns `.graphify`).

- [ ] **Step 5: Verify no raw calls remain**

Run: `! grep -rnE "python3 scripts/|bash scripts/" skills/_flows/ && echo CLEAN`
Expected: prints `CLEAN`.

- [ ] **Step 6: Run the test**

Run: `python3 -m unittest tests.test_plugin_manifest -v` → Expected: PASS.

- [ ] **Step 7: Commit**

```bash
git add .claude-plugin/plugin.json skills/_flows/ tests/test_plugin_manifest.py
git add -u .claude   # stage the removals from the git mv
git commit -m "feat(plugin): manifest + move internal flows to skills/_flows, calls via ors"
```

---

## Task 6: User-facing skills — `research`, `report`, `dashboard`

Author the three invocable skills; delete the old entry-point docs.

**Files:**
- Create: `skills/research/SKILL.md` (from `.claude/research.md` body)
- Create: `skills/report/SKILL.md` (from `.claude/report.md` body)
- Create: `skills/dashboard/SKILL.md` (new)
- Remove: `.claude/research.md`, `.claude/report.md`
- Test: extend `tests/test_plugin_manifest.py`

**Interfaces:**
- Consumes: `bin/ors` (Task 4); `skills/_flows/*` (Task 5).
- Produces: three `SKILL.md` files with frontmatter `name` + `description` + `disable-model-invocation: true`; bodies reference engine via `ors` and the loop via `skills/_flows/goal.md`.

- [ ] **Step 1: Extend the manifest test (failing)**

Append to `tests/test_plugin_manifest.py` inside the `Manifest` class:

```python
    def test_user_skills_frontmatter(self):
        import re
        for name in ("research", "report", "dashboard"):
            p = os.path.join(ROOT, "skills", name, "SKILL.md")
            txt = open(p).read()
            self.assertTrue(txt.startswith("---"), name)
            fm = txt.split("---", 2)[1]
            self.assertRegexpMatches(fm, r"name:\s*\S", name) if hasattr(self, "assertRegexpMatches") else self.assertRegex(fm, r"name:\s*\S")
            self.assertRegex(fm, r"description:\s*\S")
            self.assertRegex(fm, r"disable-model-invocation:\s*true")
            self.assertNotRegex(txt, r"python3 scripts/")
            self.assertNotRegex(txt, r"bash scripts/")
```

- [ ] **Step 2: Run to verify it fails**

Run: `python3 -m unittest tests.test_plugin_manifest -v`
Expected: FAIL — skill files missing.

- [ ] **Step 3: Create `skills/research/SKILL.md`**

Frontmatter + the bootstrap body adapted from `.claude/research.md`, calls via `ors`:

```markdown
---
name: research
description: One-prompt autonomous research run against the current project. Use when the user runs /ors:research "<question>" or asks ORS to research a topic and produce cited findings. Invoke to bootstrap a plan, then drive the autonomous goal loop to convergence.
disable-model-invocation: true
---

# /ors:research — one-prompt autonomous research bootstrap

Turn ONE natural-language prompt into a fully autonomous research run. Invoked as
`/ors:research "<prompt>" [--budget <tokens>] [--root <dir>]` (default budget 2000000,
default root `.` = the current project). All engine calls go through `ors` (the
bundled dispatcher). Do exactly this, then hand off to the goal loop:

1. **Classify the research shape**: one of `comparison`, `survey`, `causal`,
   `how-to`, `chronology`. If unsure, use `survey`.
2. **Decompose** the prompt into a plan and write it to `.research/plan-input.json`
   (under `--root`). Emit this schema:
   ```json
   {"shape":"comparison","entities":["A","B"],
    "dimensions":[{"name":"...","why":"..."}],"topics":[],
    "seed_gaps":[{"topic":"...","desc":"..."}],"rationale":"..."}
   ```
   - `comparison`/`causal`: populate `entities` + `dimensions`; one `seed_gap` per
     `entity × dimension` cell.
   - `survey`/`how-to`/`chronology`: populate `topics`; `seed_gaps` per topic.
3. **Apply the plan** (pure code validates; an invalid plan halts before any tokens):
   ```
   ors plan apply --root <root> --question "<prompt>" --budget <tokens> \
     --plan-file <root>/.research/plan-input.json
   ```
   If it exits non-zero, surface the `invalid plan: …` message and STOP.
4. **Wire metering, then baseline:** resolve this session's transcript so token
   metering is real (not the estimate fallback) —
   ```
   export CLAUDE_TRANSCRIPT_PATH="$(ls -t "$HOME/.claude/projects/$(pwd | sed 's#[/.]#-#g')"/*.jsonl 2>/dev/null | head -1)"
   ors runlog start
   ors meter update --root <root>
   ```
   If no transcript is found, proceed anyway (metering uses the per-cycle subagent
   estimate; the cycle cap is the backstop).
5. **Hand off to the autonomous loop:** run the goal loop exactly as defined in
   `skills/_flows/goal.md` (it meters tokens, runs the dimension gate each cycle,
   and stops on plateau OR run-budget OR cycle cap). Do not re-implement it here.

The run is fully autonomous after step 3; the only human-visible pre-completion
stop is an invalid-plan halt.
```

(Copy the full step detail from the original `.claude/research.md` where this
summary is terser; keep the CLI flags identical, only the program changes to `ors`.)

- [ ] **Step 4: Create `skills/report/SKILL.md`**

Frontmatter + the body from `.claude/report.md`, engine calls via `ors`:

```markdown
---
name: report
description: Generate the narrative research report from the current run's goal, plan, and findings. Use when the user runs /ors:report or asks ORS for a written summary of a completed/partial research run.
disable-model-invocation: true
---

# /ors:report — on-demand narrative report
```

Then paste the body of `.claude/report.md` below the frontmatter, rewriting any
`python3 scripts/X.py` to `ors <verb>` per the verb table (the original had 0 such
calls, but verify with grep).

- [ ] **Step 5: Create `skills/dashboard/SKILL.md`**

```markdown
---
name: dashboard
description: Launch the live knowledge-graph dashboard for the current research run. Use when the user runs /ors:dashboard or asks to see the realtime graph/state UI for an ORS run in this project.
disable-model-invocation: true
---

# /ors:dashboard — live graph UI

Serve the realtime graph + run dashboard against THIS project's artifacts. Run:

```
GV_GRAPH="$PWD/.graphify/graph.json" \
GV_STATE="$PWD/.research/state.json" \
GV_HTML="${CLAUDE_PLUGIN_ROOT}/public/index.html" \
GV_DASHBOARD="${CLAUDE_PLUGIN_ROOT}/public/dashboard.html" \
  python3 "${CLAUDE_PLUGIN_ROOT}/scripts/graph_view_server.py" --port 8765
```

Then open the printed URL. The server reads the target's `.graphify/graph.json`
and `.research/state.json`; the HTML is served from the plugin bundle. Stop it
with Ctrl-C when done. (graphify must have produced `.graphify/graph.json` for the
graph panel to populate.)
```

- [ ] **Step 6: Delete the old entry-point docs**

```bash
git rm .claude/research.md .claude/report.md
```

- [ ] **Step 7: Run the test**

Run: `python3 -m unittest tests.test_plugin_manifest -v` → Expected: PASS (all methods).

- [ ] **Step 8: Commit**

```bash
git add skills/research/SKILL.md skills/report/SKILL.md skills/dashboard/SKILL.md tests/test_plugin_manifest.py
git add -u .claude
git commit -m "feat(plugin): /ors:research, /ors:report, /ors:dashboard skills"
```

---

## Task 7: Confirm dashboard server honors GV_* env (no behavior change)

Lock in the portable-dashboard contract with a test, since Task 6's dashboard skill depends on it.

**Files:**
- Test: `tests/test_graph_view_env.py`
- Modify (only if the test surfaces a gap): `scripts/graph_view_server.py:199-207`

**Interfaces:**
- Consumes: `graph_view_server.py` env vars `GV_GRAPH`, `GV_STATE`, `GV_HTML`, `GV_DASHBOARD`.

- [ ] **Step 1: Write the test**

Create `tests/test_graph_view_env.py`:

```python
import importlib.util, os, unittest
SPEC = os.path.join(os.path.dirname(__file__), "..", "scripts", "graph_view_server.py")


class GVEnv(unittest.TestCase):
    def test_env_vars_referenced(self):
        src = open(SPEC).read()
        for var in ("GV_GRAPH", "GV_STATE", "GV_HTML", "GV_DASHBOARD"):
            self.assertIn(var, src, var)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Run it**

Run: `python3 -m unittest tests.test_graph_view_env -v`
Expected: PASS immediately (the server already reads these — see `graph_view_server.py:199-207`). If it FAILS, add `os.environ.get("GV_…", default)` for the missing var(s) at those lines, then re-run.

- [ ] **Step 3: Commit**

```bash
git add tests/test_graph_view_env.py
# include scripts/graph_view_server.py only if Step 2 required an edit
git commit -m "test(dashboard): lock GV_* env contract for portable dashboard"
```

---

## Task 8: Full-suite green + live target-run validation

Prove the packaged plugin runs end-to-end against a target distinct from the ORS repo.

**Files:** none (validation + ledger only).

- [ ] **Step 1: Whole suite + smokes + integrity on the branch**

Run:
```bash
python3 -m unittest discover -s tests -p 'test_*.py' 2>&1 | tail -2
for t in research_flow goal_loop_wiring planner_e2e report_flow resolve_topic_dir \
         ingest_flow ingest_flow_inbox ingest gather search_flow process_flow catalog \
         ors_dispatch; do
  printf "%s: " "$t"; bash tests/test_$t.sh >/dev/null 2>&1 && echo PASS || echo FAIL; done
python3 scripts/check_integrity.py
```
Expected: unit OK; all smokes PASS; `integrity OK`.

- [ ] **Step 2: Live target run via the dispatcher (throwaway target dir)**

Simulate a target project distinct from the ORS repo, driving the spine through `ors`:

```bash
T=/tmp/ors-target; rm -rf "$T"; mkdir -p "$T/.research"
ORS="$PWD/bin/ors"; cd "$T"
cat > .research/plan-input.json <<'JSON'
{"shape":"comparison","entities":["SQLite","DuckDB"],
 "dimensions":[{"name":"columnar storage","why":"core perf diff"}],"topics":[],
 "seed_gaps":[{"topic":"columnar storage","desc":"DuckDB columnar vectorized execution"}],
 "rationale":"live target validation"}
JSON
"$ORS" plan apply --root . --question "SQLite vs DuckDB columnar storage?" \
  --budget 400000 --plan-file .research/plan-input.json
"$ORS" runlog start; "$ORS" meter update --root .
"$ORS" decide --root . --apply
# one real search+ingest cycle:
IN=".research/ingest/.work/columnar storage"; mkdir -p "$IN"
PER_GAP=2 "$ORS" search --topic "columnar storage" --inbox "$IN"
"$ORS" ingest "columnar storage" --inbox "$IN"
ls -d "$T"/.research/docs/*/ ; python3 - <<PY
import json; s=json.load(open("$T/.research/state.json"))
print("corpus:", len(s["corpus"]), "graph.dirty:", s["graph"]["dirty"])
PY
cd - >/dev/null
```
Expected: artifacts land under `/tmp/ors-target/.research/docs/01-columnar-storage/`, `corpus > 0`, `graph.dirty: True`, and **nothing written into the ORS repo**. Clean up: `rm -rf /tmp/ors-target`.

- [ ] **Step 3: Plugin loads via `--plugin-dir` (manual, by the user)**

Note in the ledger: the user verifies `claude --plugin-dir "$PWD"` then `/ors:research "<tiny q>" --budget 200000` from a separate project. (This step is user-run; the agent records the request, does not self-launch a research run.)

- [ ] **Step 4: Update the ledger + final commit**

```bash
printf 'ALL TASKS COMPLETE. Suite green, live target run OK (artifacts under target/.research).\n' >> .superpowers/sdd/progress.md
git add .superpowers 2>/dev/null || true   # gitignored; no-op if so
git commit --allow-empty -m "chore(ors): package validation complete — live target run green"
```

---

## Final whole-branch review

After Task 8, request one whole-branch review (most-capable model) over `main..feat/ors-package`, per the repo discipline. Address Critical/Important inline, then use `superpowers:finishing-a-development-branch` to merge.

---

## Self-review (plan vs spec)

- **Spec §Decisions 1-6** → Tasks 4 (dispatcher), 5-6 (repo-as-plugin, skills, deletes), 1-3 (DOCS_BASE uniform), 6 (dashboard.html bundled in place — untouched), 6 (graphify prereq noted in skills). ✓
- **Spec §`bin/ors`** → Task 4 (incl. no `--root` injection, self-locating, env defaults). ✓
- **Spec §DOCS_BASE threading** (lib.sh, promote.py, ingest.sh, process/loop literals, gather cosmetic, check_integrity/cite_check path-agnostic) → Tasks 1, 2, 5; catalog/state.py left per spec out-of-scope. ✓
- **Spec §Plugin structure** (manifest, 3 skills, _flows, disable-model-invocation) → Tasks 5, 6. ✓
- **Spec §Metering wiring** → Task 6 research skill Step 3. ✓
- **Spec §Dashboard skill** → Tasks 6, 7. ✓
- **Spec §Testing** (dispatcher, DOCS_BASE namespacing, plugin structure, regression, live target run) → Tasks 4, 1-3, 5-6, 3/8, 8. ✓
- **Placeholder scan:** no TBD/TODO; the one rule-based transform (verb rewrite) ships a complete table + a `grep` verification gate. ✓
- **Type/name consistency:** `docs_base()`, `DOCS_BASE`, `ors <verb>` table used identically across tasks. ✓
- **Gap found + added:** `.gitignore` for generated `.research/docs/` (the `.research/` spine is committed) — folded into Task 3. The legacy `test_catalog.sh` exclusion is called out so the migration doesn't break the frozen-corpus test.
