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
