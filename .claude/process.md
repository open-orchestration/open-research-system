<!-- .claude/process.md -->

# Process cycle

Run one process cycle for the research engine. Do exactly this, then stop:

1. Pick a topic: run `python3 scripts/state.py candidates`. If it prints nothing,
   stop early — either the phase is `gather` (process is gated off) or no topic has
   enough un-processed sources. Otherwise take the top line's topic `T`.

2. Plan: read the un-processed sources for `T`
   (`python3 scripts/state.py list-drafts` shows what is already drafted; the source
   files live under `docs/<T>/sources/`). Read the existing finding for `T` under
   `docs/findings/` and the knowledge graph (`.graphify/graph.json`) for context.
   Frame **3–5 sub-questions across different perspectives** (method, evidence,
   contradiction, application).

3. Draft: write a finding answering those sub-questions. **Every claim must carry an
   inline `[corpus_id]` citation** to the `corpus` entry it came from (the `c…` ids
   from `state.json`), e.g. `… pre-registration reduces bias [c1a2b3c4d].` Compute the
   draft id and filename:
   ```
   ID=$(python3 scripts/state.py gen-id d "T|<your title>")
   ```
   Write the draft to `docs/findings/_drafts/$ID-<slug>.md` with a `status: draft`
   line in its header.

4. Success check — **two gates**, do not skip either:
   - **(a) Citation resolution (deterministic):** run
     `python3 scripts/cite_check.py docs/findings/_drafts/$ID-<slug>.md`.
     - Exit 0 → continue. Exit 1 → the draft has missing or dangling citations. Fix the
       draft (cite real corpus ids, or remove the unsupported claim) and re-run until it
       passes.
     Log the citation gate: on exit 0 `python3 scripts/runlog.py log --flow process --step cite_check --status ok`;
     on exit 1 (after you have exhausted fixes) `--status fail`.
   - **(b) Faithfulness self-check (agent judgment):** re-read each claim **against the
     source it cites** and confirm the source actually supports the claim — not merely
     that the cited id exists. Rewrite or drop any claim the source does not bear out.
     This gate is intentionally agent-side: faithfulness is not deterministically
     checkable, so `cite_check.py` does not attempt it.

   Do **not** record a draft until **both** gates pass.

5. Record the draft:
   ```
   python3 scripts/state.py add-draft --id "$ID" --topic "T" --title "<your title>" \
     --path "docs/findings/_drafts/$ID-<slug>.md" --cites "c…,c…"
   ```
   (`--cites` is the comma-separated list of every corpus id you cited.)
   Log the draft: `python3 scripts/runlog.py log --flow process --step draft --status ok --data "{\"draft_id\":\"$ID\"}"`.

6. Emit gaps (closes the loop to search): for each open question the corpus could not
   answer, run
   `python3 scripts/state.py add-gap --topic "T" --desc "<the missing question>" --origin process`.

7. Author graph assertions (optional, autonomous — no human gate). While
   reading the knowledge graph in step 2, if you perceive a **missing
   cross-community link** — two nodes in different communities that your
   sources show are genuinely related (a bridge), or one source that
   `supports`/`contradicts`/`refines` another — append one assertion per link:
   ```
   python3 scripts/assertions.py add \
     --from "<node_id>" --to "<node_id>" \
     --relation bridges|supports|contradicts|refines \
     --rationale "<why these two connect>" \
     --cites "c…,c…"
   ```
   `--from`/`--to` are graph node `id`s from `.graphify/graph.json` (the
   `nodes[].id` field, not the label) — **never the `c…` corpus ids**, which
   belong only in `--cites`. A corpus id used as `--from`/`--to` is a phantom
   node and fails the next integrity check. Resolve a real node id by grepping
   `.graphify/graph.json` (e.g. a source file maps to a `sources_…` node, a
   concept to a `…_concept`/snake-case node) and confirm it exists before
   asserting. `--cites` are the `corpus` ids that justify the edge.
   Assertions are auto-applied on the next ingest cycle's replay and are always
   recorded — only assert links you can defend from cited sources. Skip this
   step if no missing link is evident; do not invent edges to fill a quota.

8. Run `python3 scripts/check_integrity.py` — if it reports problems, stop and surface
   them; do not claim the cycle succeeded.
   Log it: `python3 scripts/runlog.py log --flow process --step integrity --status ok` (or `--status fail` if it reported problems).

9. Review gate: run the independent reviewer on this draft exactly as defined in
   `.claude/review.md` (dispatch a **fresh** reviewer subagent — never your own drafting
   context — over the draft `$ID` and its cited sources; it returns a binary verdict and the
   engine promotes or rejects accordingly). The gate is conservative: a clear `promote`
   moves the finding into `docs/findings/` + `SYNTHESIS.md`; anything else rejects and frees
   the sources for a stronger redraft.

A human can still override the gate after the fact (`promote.py promote/reject <id>` by hand).
