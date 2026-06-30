# Handoff — resume ORS self-provisioning (sub-project C), Tasks 5–8

Paste the block below into a fresh Claude Code session (cwd =
`/Users/joshua/Documents/GitHub/open-research-system`) to continue the
subagent-driven build mid-flight. Tasks 1–4 are done and committed; Tasks 5–8 +
the final whole-branch review + merge remain.

---

## Paste this prompt

```
Resume the subagent-driven execution of sub-project C (ORS self-provisioning) in
/Users/joshua/Documents/GitHub/open-research-system. We are mid-flight on branch
feat/ors-self-provisioning. Invoke superpowers:subagent-driven-development and
continue from Task 5 — do NOT re-dispatch Tasks 1–4 (they are complete; trust the
ledger and git log).

Read first:
- Plan: docs/superpowers/plans/2026-06-30-ors-self-provisioning.md (8 tasks; the
  source of truth for each task's exact code + tests).
- Spec: docs/superpowers/specs/2026-06-30-self-provisioning-design.md.
- Ledger: .superpowers/sdd/progress.md (gitignored — what landed; check it first).

State:
- Branch feat/ors-self-provisioning, HEAD cdaaf9f, branched from main at 12fbe54.
- DONE (per ledger): Task 1 (ors_venv resolver + bundled crawl4ai helpers),
  Task 2 (consumers routed through ors_venv; markitdown command-v fallback),
  Task 3 (jq removed → python3), Task 4 (scripts/setup.sh + /open-research-system:setup
  skill, idempotent). Full unit suite OK; 15→ now ~21 shell smokes; integrity OK.
- REMAINING: Task 5 (SessionStart hook + scripts/provision_check.sh + hooks/hooks.json),
  Task 6 (graphify graceful degrade in skills/_flows/loop.md), Task 7 (README setup
  section + CHANGELOG 0.2.0 + bump plugin.json version to 0.2.0; claude plugin
  validate . --strict), Task 8 (full suite + smokes + integrity green, live
  `./bin/ors setup` idempotent smoke, no-hardcode grep, ledger finalize).

How to run each task (the established loop):
- Generate the brief with the skill's scripts/task-brief on the plan file + task N,
  dispatch a fresh implementer (model: sonnet — the plan carries complete code),
  then scripts/review-package <base> <head> and dispatch a sonnet task reviewer with
  the brief + report + diff paths. Fix Critical/Important via a fix subagent, ledger
  Minors. Record BASE = the commit before each implementer (from the ledger), never
  HEAD~1.
- Hard rules: python3 (3.12) only, stdlib-only engine; tests stub ORS_VENV/PY (no
  real venv or network); Conventional Commits; NO co-author trailer; explicit
  staging (never git add .); protected file public/dashboard.html (do not touch);
  no git worktrees (branch only); check_integrity.py green before each task is done.
- Build-path coverage is intentionally idempotent-only (user decision) — do not add
  a real venv build to the tests.

After Task 8: dispatch ONE final whole-branch review (model: opus) over
12fbe54..HEAD via scripts/review-package, pointing it at the Minor findings list in
the ledger for triage; apply Critical/Important via one fix subagent; then use
superpowers:finishing-a-development-branch. Merge to main is the user's call
(present the 4 options; do not push without consent — the repo publishes to the
public github.com/open-orchestration/open-research-system, currently at v0.1.0).
Task 7 bumps to 0.2.0; after merge, the release tag + push (claude plugin tag +
git push) is a separate user-gated publish step.

Carried Minor findings (for the final review to triage — already in the ledger):
- T1: no LIB_DIR assertion test; no bad-ORS_VENV-path fallthrough test.
- T2: gather.sh PY has no env-override seam (matches plan + original).
- T3: python3 url-parse skips url-less elements vs jq's "null" (an improvement).
- T4: (resolved in-task).

Begin by reading the ledger, then Task 5.
```

---

## Quick orientation (for the human)

```
git -C /Users/joshua/Documents/GitHub/open-research-system log --oneline 12fbe54..HEAD
cat .superpowers/sdd/progress.md
python3 -m unittest discover -s tests -p 'test_*.py'      # OK
./bin/ors setup                                            # idempotent: reuses ~/.venvs/crawl4ai
```
