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
