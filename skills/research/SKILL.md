---
name: research
description: One-prompt autonomous research run against the current project. Use when the user runs /ors:research "<question>" or asks ORS to research a topic and produce cited findings. Invoke to bootstrap a plan, then drive the autonomous goal loop to convergence.
disable-model-invocation: true
---

# /ors:research — one-prompt autonomous research bootstrap

Turn ONE natural-language prompt into a fully autonomous research run. Invoked as
`/ors:research "<prompt>" [--budget <tokens>] [--root <dir>]` (default budget 2000000,
default root `.` = the current project root). Do exactly this, then hand off to the goal loop:

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
   ors plan apply --root <root> --question "<prompt>" \
     --budget <tokens> --plan-file <root>/.research/plan-input.json
   ```
   If it exits non-zero, surface the `invalid plan: …` message and STOP — fix the plan
   JSON and retry; do not launch the loop on an invalid plan.
4. **Start the run log and meter baseline:**
   ```
   ors runlog start
   ors meter update --root <root>
   ```
   `ors` auto-discovers the session transcript (`CLAUDE_TRANSCRIPT_PATH`) and exports
   it for metering. If no transcript is found, the run proceeds with the per-cycle
   subagent estimate and the cycle cap as backstop.
5. **Hand off to the autonomous loop:** run the goal loop exactly as defined in
   `skills/_flows/goal.md` (it meters tokens, runs the dimension gate each cycle, and
   stops on plateau OR run-budget OR cycle cap). Do not re-implement it here.

The run is fully autonomous after step 3; the only human-visible pre-completion
stop is an invalid-plan halt.
