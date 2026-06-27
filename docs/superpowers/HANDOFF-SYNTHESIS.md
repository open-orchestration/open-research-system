# Handoff — open-research-system: SYNTHESIS + SELF-IMPROVEMENT phase

Paste into a fresh session to start the next phase. Self-contained. The corpus is
**grounded and plateaued** (55 findings / 17 of 17 domains); this phase is no longer about
*gathering more primaries*. Two new workstreams:

1. **Definitive findings** — distill the 55 single-source findings into durable, individually-
   reviewed **cross-domain synthesis findings** ("the definitive X").
2. **Self-improvement** — feed the corpus's own conclusions back into the engine so the
   research *process* is grounded in the research *findings*.

READ FIRST, in order: `docs/superpowers/HANDOFF.md` (the operating runbook — gather/ingest/
graphify/process/review/promote mechanics; still authoritative for *how* a finding is drafted,
verified, reviewed, promoted, committed). Then root `SYNTHESIS.md` (the current cross-domain
distillation — the raw material for definitive findings). Don't re-derive what those say.

---

## State (verify live — drifts as you work)
- **58 promoted / 5 rejected** (was 55/5 — this phase added **3 definitive/synthesis findings**,
  all promoted on first independent review, all GRADE **moderate**, zero rejects). Corpus **223**
  active. Graph **2487 nodes / 2804 links** (`dirty:false`). 66 assertions. ALL 17/17 domains
  grounded. Phase `deepen`. 50 queued gaps (all dead-source / no-clean-primary / redundant —
  **do NOT chase them**, both the gather and process/candidates frontiers are exhausted).
- HEAD `ddbbc4a` (this phase: `c0350c4`→`ddbbc4a`).

## DONE this phase (cross off; pick up the unchecked items)
**Workstream 1 — definitive findings promoted (3 of 5 candidates):**
- ✅ **causal-inference decision tree** (`daccd735c`, 02, moderate) — commit `2743add`.
- ✅ **evaluation stack** (`d9136c25c`, 16, moderate) — commit `8662e64`.
- ✅ **anytime-valid testing kit** (`dd90b2c09`, 02, moderate) — commit `ddbbc4a`.
- ⬜ **grounding/faithfulness pipeline** (d1ad78766 + dfa42bc8a + d636208ea) — NOT yet done.
- ⬜ **deep-research architecture** (d603c3334 + da592d4f8 + dbc0e9395 + d369c3d06 + 06/07/12) — NOT yet done.

**Workstream 2 — process upgrades shipped (each cites its grounding finding in the commit body):**
- ✅ **#1 review gate → GRADE certainty + LLM-judge debiasing** (`.claude/review.md`; grounds
  d628b3d0f + dc577f3e2 + d4c45dd7e) — commit `c0350c4`. The gate now records a `CERTAINTY:`
  level per promote into the `runlog.py` ledger (free-form `--data`, no script change).
- ✅ **#2 promotion = streaming multiple-testing** (`.claude/review.md` new section; grounds
  d42ec736c + dc588b7cc) — commit `d159e01`. Framing + known-gap note; no α-budget tracking built.
- ✅ **#4 faithfulness self-check → FActScore atomic decomposition** (`.claude/process.md` step 4b;
  grounds d1ad78766 + dfa42bc8a) — commit `7350568`.
- ⬜ **#3 drafting → grounded prompting** (prompting ladder d0b1fc5c6 + Chain-of-Draft d6432467b) — NOT done.
- ⬜ **#5 citation discipline → CSL-JSON/biblatex** (d59d1279b, de47719c4) — NOT done.
- ⬜ **#6 candidate-selection → BM25/PMI** (d0fefa5d5, d7289dbd9) — NOT done.
- ⬜ **#7 ADR log for the process changes** (decf6989c / d657c1d86) — NOT done.

**Pattern that worked (reuse it):** for each definitive finding — resolve the contributing
findings' inline `[c…]` (regex `c[0-9a-f]{8}`, NOT 9 — ids are c+8hex) → corpus source map;
`gen-id`; dispatch one `general-purpose` DRAFTER with the theme + finding paths + c→source map +
the re-cite-primary rule; **self-verify independently** (re-run `cite_check.py` + Python
whitespace-insensitive re-grep of every cited number — both MISS cases this phase were *my* wrong
grep terms, not draft errors, so always confirm the term before trusting a MISS); `add-draft`;
`check_integrity.py`; dispatch a **FRESH** reviewer with the upgraded `.claude/review.md` rubric
verbatim (it now emits `CERTAINTY:` + `VERDICT:` as the last two lines); promote + log certainty +
integrity + re-ground `SYNTHESIS.md` + commit. All 3 drafts handled glyph-mangled PDF formulas the
same honest way (canonical form + lossiness note, component tokens byte-verified).
- Verify: `python3 scripts/check_integrity.py`, `python3 scripts/state.py candidates`,
  `git rev-parse --short HEAD` (should be `070af6f` or later, tree clean modulo the user's
  IDE file `public/dashboard.html` — **NEVER touch/stage/commit it, or `.research/*.log` /
  `graphify-out/`**).
- `python3` not `python` (no `python` on PATH).

## The finding corpus you are synthesizing (55, by domain)
The grounded base. Definitive findings cross-cut these. (Get live titles with
`python3 scripts/state.py list-drafts` + the `docs/findings/d*.md` frontmatter.)
- **01 methodology/epistemics:** GRADE certainty system (d628b3d0f); grade-reconcile-calibrate pipeline (dc577f3e2)
- **02 statistical/causal (9):** do-calculus vs potential-outcomes (d2c5150e6); online-FDR streams (d42ec736c); confidence sequences (d541a8e56); experiment design/power (d740bae09); ATE under ignorability — IPW/DR (d77c7f685); RDD estimation/validity (d8d9c5187); always-valid mSPRT (dc588b7cc); RD falsification toolkit (dd02167c3); IV/DiD/RDD identification (df8ca1aeb)
- **03 decision frameworks:** AHP (d030916c4); ACH + weighted criteria (d1b3c3b4c); Nygard ADR (d657c1d86); ADR/MADR format (decf6989c)
- **04 applied playbooks:** evidence-tier-split playbooks (d603c3334)
- **05 deep-research systems:** benchmark-accuracy comparability (d369c3d06); DeepResearch-Bench (dc6ee6f7f)
- **06 RAG/retrieval:** ColBERT late-interaction economics (d6ccd6b1c); GraphRAG/ColBERT shared-benchmark (d73a9474e); hybrid/contextual RAG (dc97efcf9)
- **07 agentic orchestration:** (d5c35de17, df8e7fa14)
- **08 grounding/truth:** FActScore + RARR (d1ad78766); faithfulness measurement machinery (dfa42bc8a)
- **09 KG/compilation:** extraction/community cost-fidelity (d37b490ee); KG2RAG (d6c359091)
- **10 context/prompting:** prompting ladder (d0b1fc5c6, d0cce1cec); FSM constrained decoding (d270b0177); Chain-of-Draft (d6432467b)
- **11 pipeline engineering:** CDC/index-freshness (d470b6824); LlamaIndex IngestionPipeline (da2a65c0c)
- **12 tooling:** LangGraph/AutoGen primitives (d1fb5a112); execution-model taxonomy (d28841446, de92d6feb)
- **13 reference systems:** GPT-Researcher internals (da592d4f8); STORM pipeline (dbc0e9395)
- **14 papers:** Self-RAG/Toolformer tables (d154759ce); foundational agent/RAG papers (de3e9818e)
- **15 textbooks:** BM25 (d0fefa5d5); textbook IR scoring/eval (d2fbbb962); PMI/PPMI term-weighting (d7289dbd9); vector semantics (ddc396092)
- **16 evaluation:** LLM-as-judge reliability (d4c45dd7e); RAGAS/ARES formulas (d636208ea); GAIA/BrowseComp (d69d7458e); agent-vs-RAG eval regimes (d6fad1a98); multi-hop QA (dcd1309fb); JSONSchemaBench (dd09194c4)
- **17 specs/standards:** MCP spec internals (d3c246500); MCP Tools/Prompts security (d4562e116); citation interchange formats (d59d1279b); CSL/concordance (d75f0cdee); biblatex modern types (de47719c4)

---

## WORKSTREAM 1 — Definitive (synthesis) findings

**What "definitive" means here.** A definitive finding answers a *system-level* question by
distilling **across multiple existing findings and their primaries** into one durable,
defensible conclusion — the thing you'd cite as "the answer" rather than "a source." It is the
operation the `synthesize` phase was built for but never had a recipe for (see Cross-check).

**The mechanism (reuses the existing gate — no new tooling needed).**
Definitive findings live in the same `docs/findings/` space and pass the same two gates +
independent review. The one rule that makes them work with the existing `cite_check.py`:

> **Every load-bearing claim still carries an inline primary `[c<id>]` citation** to the
> corpus source that actually backs it. Cross-reference sibling findings (`d…`) **in prose**
> for navigation, but the *citation of record* is always the primary `c…` id. (`cite_check.py`
> validates `c…` ids against `corpus`; it does not know finding ids. Re-citing the underlying
> primary keeps the gate green AND keeps provenance bulletproof — the synthesis inherits its
> evidence, it doesn't launder it.)

**Per-definitive-finding recipe** (same spine as `.claude/process.md`, new framing):
1. Pick a THEME that genuinely spans ≥3 findings across ≥2 domains (candidates below).
2. `ID=$(python3 scripts/state.py gen-id d "<topic>|<definitive title>")` — file the finding
   under the home topic most central to the theme (or 04-applied-playbooks for cross-cutting
   system architecture). Title it "The definitive …" / "… end to end" so its class is legible.
3. Dispatch a `general-purpose` DRAFTER. Give it: the theme, the **list of contributing
   findings (`d…` + paths)** AND **their cited corpus sources (`c…` id → source path/url)**,
   and the rule above. It reads the findings to map the territory, then reads the *primaries*
   to re-anchor each load-bearing claim on a `c…` id. Frame 3–5 system-level sub-questions
   (what's settled, what's contested between findings, what the composed recommendation is, what
   the honest limits are). Write to `docs/findings/_drafts/$ID-<slug>.md`, `status: draft`,
   every load-bearing claim an inline `[c…]`, sibling findings cross-linked in prose. Pass
   `cite_check.py`, faithfulness self-check, RETURN id/title/cites/contributing-findings/gaps.
4. **Self-verify yourself** (don't trust the drafter): re-run `cite_check.py`; re-grep every
   cited number/formula against the source bytes whitespace-insensitively (Python
   `re.sub(r'\s+','',open(p).read())` for >700KB sources — a shell `$(…)` var overflows and
   `grep` silently returns 0). Fix any over-claim. Watch the synthesis-specific failure mode:
   **a claim true of finding A's source asserted as general** — each `[c…]` must back the
   *specific* clause it sits on, not the surrounding generalization.
5. `state.py add-draft`; `check_integrity.py`.
6. Dispatch a **FRESH** `general-purpose` REVIEWER (rubric VERBATIM from `.claude/review.md`,
   never the drafter's context). Give it the `(corpus_id, source_path, source_url)` triples.
   The canon-worthiness bar for a definitive finding is **higher**: it must be a genuine
   cross-domain synthesis, not a longer restatement of one finding, and must not contradict a
   sibling finding without reconciling it. Parse last `VERDICT:` → `promote.py promote`/`reject`.
7. `runlog.py log`; `check_integrity.py`; re-ground root `SYNTHESIS.md`; commit
   `chore(research): <definitive title>` (stage explicitly, no co-author trailer).

**Candidate definitive findings (high-value, genuinely cross-cutting — pick, don't do all):**
- **The definitive evaluation stack** — compose d4c45dd7e (LLM-judge reliability) + d636208ea
  (RAGAS/ARES) + d1ad78766 (FActScore/RARR) + dfa42bc8a (faithfulness machinery) + d69d7458e
  (GAIA/BrowseComp) + d6fad1a98 (two eval regimes): what to measure, with which metric, under
  which regime, and the known judge biases to correct for.
- **The definitive grounding/faithfulness pipeline** — d1ad78766 + dfa42bc8a + d636208ea +
  08/16 findings: claim extraction → atomic-fact scoring → attribution editing → NLI entailment.
- **The definitive causal-inference decision tree** — d2c5150e6 + df8ca1aeb + d8d9c5187 +
  dd02167c3 + d77c7f685 + d740bae09: can you randomize? → which design → which estimator →
  which falsification test. (02 is the densest domain; this is the strongest single candidate.)
- **The definitive deep-research architecture** — d603c3334 + da592d4f8 + dbc0e9395 + d369c3d06
  + the 06/07/12 retrieval/orchestration findings: planner-executor-publisher, retrieval choice,
  orchestration primitive, and how it's actually benchmarked.
- **The definitive anytime/sequential-testing kit** — d541a8e56 + dc588b7cc + d42ec736c: confidence
  sequences + mSPRT + online-FDR as one coherent "test continuously without lying" story.

## WORKSTREAM 2 — Upgrade the research process FROM the findings

The engine currently runs on hand-authored heuristics. The corpus now contains the *peer-
reviewed methods* those heuristics approximate. Close the loop: each process change must be
**justified by a finding** (name the `d…` id in the commit body). These are normal code/doc
edits — apply the repo's engineering discipline (smallest defensible diff; if you touch a
script's logic, leave one runnable check behind; never suppress a linter; `python3`).

**Highest-value upgrades (ranked; each cites the finding that grounds it):**
1. **Review gate → evidence-grading.** `.claude/review.md` is binary promote/reject with an
   ad-hoc rubric. Ground it in **GRADE** (d628b3d0f) + the **grade-reconcile-calibrate** pipeline
   (dc577f3e2): add explicit certainty levels (high/moderate/low/very-low) and the
   downgrade/upgrade criteria, so a promote also records *how certain*. Ground the reviewer's
   own reliability in **LLM-as-judge** (d4c45dd7e): bake in the documented debiasing (position/
   verbosity/self-preference bias) — e.g. require the reviewer to judge faithfulness *before*
   seeing the draft's own confidence claims.
2. **Promotion = a multiple-comparison problem.** 55+ findings each independently "tested" for
   promotion is a streaming multiple-testing setup. Apply **online-FDR** (d42ec736c) /
   **always-valid inference** (dc588b7cc) thinking to the promote/reject ledger: are we
   controlling the false-promotion rate across the whole corpus, not just per-finding? At
   minimum document the framing in `review.md`; ideally track an α-budget.
3. **Drafting → grounded prompting.** `.claude/process.md` step 3 says "every claim carries a
   citation" but nothing about *how* to reason. Ground the drafter's instructions in the
   **prompting ladder** (d0b1fc5c6) and **Chain-of-Draft** (d6432467b) — concise,
   citation-dense reasoning over verbose CoT.
4. **Faithfulness self-check → FActScore.** The self-check in process.md is informal. Ground it
   in **FActScore atomic-fact precision** (d1ad78766) + the **faithfulness machinery**
   (dfa42bc8a): decompose the draft into atomic claims, score each against its cited source.
   (This also directly powers Workstream 1's self-verify step.)
5. **Citation discipline → real interchange formats.** Ground `cite_check.py` / finding headers
   in **CSL-JSON / biblatex** (d59d1279b, de47719c4): emit findings' provenance in a real
   citation schema so the corpus is exportable, not just internally consistent.
6. **Retrieval/candidate-selection → BM25.** If `state.py candidates` or any source-ranking is
   naive, ground it in **BM25 + probabilistic idf** (d0fefa5d5) and **PMI/PPMI** (d7289dbd9).
7. **Decision logging → ADR.** Record each *process* change as an **ADR** (decf6989c / d657c1d86)
   under `docs/superpowers/specs/` or a new `docs/adr/`, so the self-improvement is itself a
   decision log — dogfooding the corpus.

**Sequencing.** Do Workstream 1 and 2 interleaved, small commits each. Start with **#1
(review gate ← GRADE + LLM-judge)** — it's the highest-leverage and it raises the quality bar
for every subsequent definitive finding. Then the **definitive causal-inference tree** (densest,
cleanest) as the first definitive finding under the upgraded gate.

---

## HARD RULES (unchanged — these are the engine's spine; don't relax)
- **Provenance is THE reject axis.** Even synthesis findings: load-bearing claims rest on genuine
  primaries (re-cited `c…` ids); blog material attributed + non-load-bearing. 5 rejects to date,
  most on this exact failure.
- **Honest demotion beats hidden over-claim.** A number not in the source bytes doesn't get
  reported; a garbled formula gets its canonical form + a lossiness note, never a transcribed garble.
- **Reviewer must be FRESH + INDEPENDENT** (new subagent, never the drafter's context). No clear
  `VERDICT:` line → reject (conservative default).
- **`check_integrity.py` after EVERY mutating step.** For graph folds: `save_manifest` after each
  reconcile; assertions default-SKIP (source nodes drift across re-extraction — prefer stable
  concept/finding nodes if you must assert).
- **Commits:** stage EXPLICITLY (never `git add .`/`-A`), Conventional Commit, no co-author
  trailer. NEVER stage `public/dashboard.html`, `.research/*.log`, `graphify-out/`.
- **Process-change commits cite the finding** that grounds them (`d…` id in the body).

## When this phase is done
Definitive findings cover the major cross-domain questions; the process files (`.claude/*.md`,
`cite_check.py`, `review.md`) each cite the finding grounding their method; root `SYNTHESIS.md`
re-grounded; an ADR log records the process upgrades. Refresh `docs/superpowers/HANDOFF.md` to
the new state and report a terse per-workstream summary (definitive findings promoted; process
files upgraded + the finding each now cites; commit hashes).

---

## Cross-check (this handoff vs the repo, HEAD `070af6f`)
Verified live, not from memory:
- **Finding inventory** (55, by domain) read from `.research/state.json` drafts (status=promoted)
  + `docs/findings/d*.md` frontmatter — every `d…` id above resolves to a promoted finding on disk.
- **`synthesize` phase is real but un-recipe'd:** `scripts/orchestrator.py:33` returns
  `"synthesize"` when `queued==0 and not dirty and (processable or pending)`, and `goal_met()`
  (line 39) keys off it — but `.claude/` holds only `goal.md loop.md process.md review.md`; there
  is **no `synthesize.md`**. Workstream 1 is that missing operation. (Note: phase is currently
  `deepen`, and the 50 dead-source queued gaps keep `queued!=0`, so the orchestrator won't
  auto-flip to `synthesize` — these definitive findings are driven by hand via the process spine,
  not by waiting for the phase flip. If you want the phase to reflect reality, the queued
  dead-source gaps would need to be closed/parked first — a judgment call to raise with the human.)
- **Gate tooling reused as-is:** `cite_check.py` validates `[c…]` ids against `corpus` (confirmed
  it has no notion of finding ids — hence the "re-cite the primary" rule). `review.md` is the
  verbatim independent-reviewer rubric. Both unchanged by Workstream 1.
- **Two SYNTHESIS files, two owners** (don't merge): `docs/findings/SYNTHESIS.md` = auto-index
  (`promote.py` appends — leave to the script); root `SYNTHESIS.md` = human distillation (sections:
  "What the evidence supports" / "Tensions & open questions" / "Not yet grounded" / "Graph reading").
- **No discrepancies** between the two workstreams: Workstream 2 #4 (FActScore self-check) and
  Workstream 1 step 4 (self-verify) intentionally share the same atomic-fact machinery — build it
  once, use it both places.
