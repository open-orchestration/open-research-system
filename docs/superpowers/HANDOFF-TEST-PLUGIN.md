# Handoff — test the ORS plugin from a fresh project

Paste the block below into a **new Claude Code session running inside a different
project** (not the open-research-system repo). It does one cheap real `/ors:research`
run and verifies the plugin works end-to-end against that project.

## Prerequisites (already true on this machine)

- Launch Claude Code in the target project **with the plugin loaded**:
  ```
  cd <some-throwaway-or-small-project>
  claude --plugin-dir /Users/joshua/Documents/GitHub/open-research-system
  ```
  (Or enable it via `/plugin` and `/reload-plugins`. Confirm `/ors:research` shows up.)
- Deps the run uses, all present: the **graphify** skill (`~/.claude/skills/graphify`),
  the **crawl4ai** venv (`~/.venvs/crawl4ai`), `jq`, `markitdown`. `python3` (not `python`).
- The skills are `disable-model-invocation: true` — invoke `/ors:research` explicitly.

---

## Paste this prompt

```
Test the ORS plugin (/ors:research) end-to-end in THIS project and report what works
and what breaks. This is a cheap real run, not a simulation.

Context: ORS is installed as a local Claude Code plugin named `ors` (loaded via
--plugin-dir from /Users/joshua/Documents/GitHub/open-research-system). It turns one
prompt into an autonomous, cited research run whose artifacts land in THIS project's
directory: <cwd>/.research/ (state, runlog, docs/NN-topic/sources, findings) and
<cwd>/.graphify/ (knowledge graph). The engine runs through a `bin/ors` dispatcher on
PATH; you never call python3 scripts directly. python3 only, never python.

Before starting: add `.research/` and `.graphify/` to this project's .gitignore (ORS
output is generated, not committed). Confirm `ors plan --help` runs (proves the plugin
PATH is active); if `ors` is not found, the plugin isn't loaded — stop and say so.

Do this:
1. Invoke the /ors:research skill with a SMALL throwaway question and a SMALL budget:
   /ors:research "<a small, concrete comparison or how-to question>" --budget 300000
   Follow the skill's steps exactly (it bootstraps a plan via `ors plan apply`, starts
   the runlog + meter, then runs the goal loop in skills/_flows/goal.md).
2. Watch the whole chain and narrate each stage as it happens:
   - plan written to <cwd>/.research/state.json (goal + plan + seeded gaps + budget)
   - `ors decide` returns phase/search/process; `ors search` fetches real sources via
     crawl4ai; `ors ingest` routes them to <cwd>/.research/docs/NN-<topic>/sources/
   - the ingest cycle's graphify `--update` step builds/updates <cwd>/.graphify/graph.json
   - `ors dim` gates dimension candidates; `ors meter update` accrues run tokens
   - the loop stops on plateau OR budget OR cycle cap (decide.stop)
3. When it converges (or stops on budget), run /ors:report and confirm it produces a
   cited narrative from the goal + plan + findings.
4. Optionally run /ors:dashboard and confirm the server starts and serves the graph for
   THIS project (Ctrl-C to stop).

Verify and report:
- All artifacts are under THIS project (<cwd>/.research, <cwd>/.graphify) — NOT under the
  open-research-system repo. Check the ORS repo stayed clean.
- Metering was real (ors auto-discovers CLAUDE_TRANSCRIPT_PATH for this session) — note the
  run token spend in <cwd>/.research/state.json budget.run.tokens_spent; if it's 0 or an
  estimate, say so.
- List every rough edge / bug / broken command with the exact error. The flows were
  validated against a scripted spine and a throwaway target, but a full agentic run
  (real drafting in process.md, real graphify --update, real review gate) has more
  surface — treat any failure as a real bug to fix back in the ORS repo, not to paper over.

Keep the budget small; this is a smoke test. Report findings concisely at the end.
```

---

## What a clean result looks like

- `<cwd>/.research/state.json` has `goal`, `plan`, gaps progressing queued→done, a non-empty
  `corpus`, and `budget.run.tokens_spent > 0`.
- `<cwd>/.research/docs/01-<topic>/sources/` holds fetched markdown sources.
- `<cwd>/.graphify/graph.json` exists with nodes/edges.
- `<cwd>/.research/docs/findings/` holds drafted findings (+ `SYNTHESIS.md`) after the
  process/review gate.
- The ORS repo at `/Users/joshua/Documents/GitHub/open-research-system` has **no** new
  `.research/docs/` or run artifacts.

## Known-untested surface (most likely to surface bugs)

The packaged spine (plan → search → ingest → decide → meter) is validated. Less exercised:
the **agentic** steps inside `skills/_flows/process.md` (drafting with inline citations,
`ors cite_check`, the two success gates) and `review.md` (the human-review promote gate),
and the **graphify `--update`** LLM step in `loop.md`. If something breaks, it is most
likely there.
