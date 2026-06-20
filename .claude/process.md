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
   `--from`/`--to` are `id`s from `.graphify/graph.json` (the `nodes[].id`
   field, not the label); `--cites` are the `corpus` ids that justify the edge.
   Assertions are auto-applied on the next ingest cycle's replay and are always
   recorded — only assert links you can defend from cited sources. Skip this
   step if no missing link is evident; do not invent edges to fill a quota.

8. Run `python3 scripts/check_integrity.py` — if it reports problems, stop and surface
   them; do not claim the cycle succeeded.

The draft now waits in the review queue (`python3 scripts/promote.py queue`). A human
promotes it (`promote.py promote <id>`) into `docs/findings/` + `SYNTHESIS.md`, or
rejects it (`promote.py reject <id>`).
