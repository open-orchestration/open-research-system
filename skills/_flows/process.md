<!-- skills/_flows/process.md -->

# Process cycle

Run one process cycle for the research engine. Do exactly this, then stop:

1. Pick a topic: run `ors state candidates`. If it prints nothing,
   stop early — either the phase is `gather` (process is gated off) or no topic has
   enough un-processed sources. Otherwise take the top line's topic `T`.

2. Plan: read the un-processed sources for `T`
   (`ors state list-drafts` shows what is already drafted; the source
   files live under `$DOCS_BASE/<T>/sources/`). Read the existing finding for `T` under
   `$DOCS_BASE/findings/` and the knowledge graph (`.graphify/graph.json`) for context.
   Frame **3–5 sub-questions across different perspectives** (method, evidence,
   contradiction, application).

3. Draft: write a finding answering those sub-questions. **Every claim must carry an
   inline `[corpus_id]` citation** to the `corpus` entry it came from (the `c…` ids
   from `state.json`), e.g. `… pre-registration reduces bias [c1a2b3c4d].`
   **Reason concisely, citation-dense — grounded in the corpus's own prompting findings.**
   Draft in the **Chain-of-Draft** style (d6432467b): minimal, informative reasoning steps
   that carry the essential intermediate result, not verbose step-by-step narration — CoD
   matches chain-of-thought accuracy at a fraction of the tokens [c810db9f5]. The finding
   body is the *evidence and its citations*, not a transcript of deliberation; every
   sentence should either state a cited fact or connect two of them. **Escalate reasoning
   depth only when it pays** (prompting ladder d0b1fc5c6): plain citation-anchored prose is
   the default; reach for heavier multi-step reasoning only on a genuinely contested or
   multi-source claim, since the originating papers show added reasoning is an
   emergent-at-scale, cost-incurring move, not a free win [cf83dbc59]. Compute the
   draft id and filename:
   ```
   ID=$(ors state gen-id d "T|<your title>")
   ```
   Write the draft to `$DOCS_BASE/findings/_drafts/$ID-<slug>.md` with a `status: draft`
   line in its header.

4. Success check — **two gates**, do not skip either:
   - **(a) Citation resolution (deterministic):** run
     `ors cite_check $DOCS_BASE/findings/_drafts/$ID-<slug>.md`.
     - Exit 0 → continue. Exit 1 → the draft has missing or dangling citations. Fix the
       draft (cite real corpus ids, or remove the unsupported claim) and re-run until it
       passes.
     Log the citation gate: on exit 0 `ors runlog log --flow process --step cite_check --status ok`;
     on exit 1 (after you have exhausted fixes) `--status fail`.
   - **(b) Faithfulness self-check (agent judgment) — FActScore-style atomic decomposition.**
     This gate is grounded in the corpus's own grounding findings: **FActScore atomic factual
     precision** (d1ad78766 — decompose a generation into atomic facts, score each as supported
     / not-supported by its source, *abstain* rather than guess) and the **faithfulness
     measurement machinery** (dfa42bc8a — per-claim entailment against the exact cited bytes).
     Apply it as:
     1. **Decompose, don't skim.** Break the draft into its individual load-bearing claims
        (one verifiable assertion each — split compound sentences). A vague paragraph judged
        as a whole hides an unsupported clause; an atomic claim cannot.
     2. **Score each claim against the bytes it cites** — does the cited source *entail* this
        specific clause, not merely sit in the same topic? For any **number, formula, or quoted
        phrase**, re-grep it in the source **whitespace-insensitively** before trusting it
        (Python `re.sub(r'\s+','',open(p).read().lower())`; never a shell `$(…)` var — a
        >700KB source overflows it and `grep` silently returns 0).
     3. **Abstain beats guess.** A number not in the source bytes does **not** get reported;
        a garbled formula gets its canonical form + a one-line lossiness note, never a
        transcribed garble. Rewrite or drop any claim the source does not bear out.
     Faithfulness is not deterministically checkable, so `cite_check` does not attempt it —
     this atomic pass is the agent-side complement. (It is the same machinery Workstream-1
     definitive findings run as their self-verify step.)

   Do **not** record a draft until **both** gates pass.

5. Record the draft:
   ```
   ors state add-draft --id "$ID" --topic "T" --title "<your title>" \
     --path "$DOCS_BASE/findings/_drafts/$ID-<slug>.md" --cites "c…,c…"
   ```
   (`--cites` is the comma-separated list of every corpus id you cited.)
   Log the draft: `ors runlog log --flow process --step draft --status ok --data "{\"draft_id\":\"$ID\"}"`.

6. Emit gaps (closes the loop to search): for each open question the corpus could not
   answer, run
   `ors state add-gap --topic "T" --desc "<the missing question>" --origin process`.

   Also emit DIMENSION CANDIDATES: if a source raised a substantive comparable aspect
   that is NOT already a `plan.dimension` and is on-goal, record it (corroboration
   accumulates across cycles — record it every time a source raises it, with that
   source's corpus id):
   `ors state add-dim-candidate --root <root> --name "<aspect>" --cite "<c-id>" --cycle K`
   Do not accept it here — the goal loop's dimension gate (step 4b) decides acceptance.

7. Author graph assertions (optional, autonomous — no human gate). While
   reading the knowledge graph in step 2, if you perceive a **missing
   cross-community link** — two nodes in different communities that your
   sources show are genuinely related (a bridge), or one source that
   `supports`/`contradicts`/`refines` another — append one assertion per link:
   ```
   ors assertions add \
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

8. Run `ors check_integrity` — if it reports problems, stop and surface
   them; do not claim the cycle succeeded.
   Log it: `ors runlog log --flow process --step integrity --status ok` (or `--status fail` if it reported problems).

9. Review gate: run the independent reviewer on this draft exactly as defined in
   `skills/_flows/review.md` (dispatch a **fresh** reviewer subagent — never your own drafting
   context — over the draft `$ID` and its cited sources; it returns a binary verdict and the
   engine promotes or rejects accordingly). The gate is conservative: a clear `promote`
   moves the finding into `$DOCS_BASE/findings/` + appends `$DOCS_BASE/findings/SYNTHESIS.md`; anything else rejects and frees
   the sources for a stronger redraft.

A human can still override the gate after the fact (`ors promote promote/reject <id>` by hand).
