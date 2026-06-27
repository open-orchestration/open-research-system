<!-- .claude/review.md -->

# Review gate — independent reviewer

Automated promotion gate. An **independent** reviewer (a fresh subagent, never the
agent that wrote the draft) judges a finished draft and the engine promotes or rejects it
without a human. The gate is **conservative**: promote only a draft that is clearly
canon-worthy; otherwise reject (rejecting frees its cited sources for a stronger redraft).
A promote also records **how certain** the evidence is (a GRADE level), so the corpus
carries graded confidence, not a bare promoted/rejected bit.

**This gate is grounded in the corpus's own peer-reviewed methods** (each method names the
finding that grounds it; a process change citing a finding is how the engine dogfoods its
own conclusions):
- **GRADE certainty** — the four-level certainty scale and its downgrade/upgrade domains
  come from the GRADE handbook finding **d628b3d0f**; the "auditable per-domain rationale,
  ≥2 reviewers, certainty ≠ recommendation" framing from **dc577f3e2** (which flagged that
  this engine had *no explicit certainty rating* — this gate is that rating).
- **Judge debiasing** — the reviewer's own reliability is bounded by the LLM-as-judge
  finding **d4c45dd7e**: judge faithfulness against the source bytes *before* the draft's
  own confidence framing can anchor the verdict (self-enhancement / anchoring control),
  decompose into per-axis judgments rather than one holistic score (RAG-Triad spirit), and
  never reward length over substance (verbosity bias). The reviewer is still one judge, so
  its verdict is treated as evidence under these controls, not as ground truth.

Run this on one draft id `D`, or loop it over every queued draft
(`python3 scripts/promote.py queue` lists them). For each `D`, do exactly this:

1. **Resolve the draft and its cited sources** (the reviewer must read the sources, not the
   draft's word for it):
   ```
   python3 - "$D" <<'PY'
   import json, sys
   s = json.load(open(".research/state.json"))
   d = next((x for x in s["drafts"] if x["id"] == sys.argv[1]), None)
   assert d, "unknown draft"
   cmap = {e["id"]: e for e in s["corpus"]}
   print("PATH", d["path"])
   for cid in d["cites"]:
       e = cmap.get(cid)
       print("CITE", cid, e["extracted_path"] if e else "MISSING", "|", (e or {}).get("source",""))
   PY
   ```

2. **Dispatch a fresh `general-purpose` reviewer subagent.** It MUST be a new subagent —
   not your own context — so the review is independent of the drafting. Give it: the draft
   file path, the list of `(corpus_id, source_path, source_url)` triples from step 1, and
   this rubric verbatim. Do not tell it which way to lean.

   > You are an independent reviewer deciding whether a machine-written research draft is
   > trustworthy enough to enter a permanent source-of-truth, and how certain its evidence
   > is. You did not write it. Work in this order — the order is a debiasing control, do not
   > reorder it:
   >
   > **A. Faithfulness FIRST, from the sources — before reading the draft's own confidence
   > framing.** Open each cited source file. For each `[c<id>]` claim, decide whether that
   > source actually bears out the *specific clause the citation sits on* (not merely that
   > the source exists or is topical). Judge this against the source bytes alone; do NOT let
   > the draft's own "definitive" / "clearly" / high-confidence language raise your trust —
   > that wording is the thing being tested, not evidence for it. Flag every claim the
   > source does not support, by `[c<id>]` and the clause.
   > **B. Source provenance.** Are the cited sources trustworthy (primary papers, official
   > docs, reputable engineering writing) or promotional/secondary (vendor marketing,
   > listicles, SEO blogs)? A **load-bearing** claim resting on a promotional source is a
   > reject reason; a blog claim that is explicitly attributed and non-load-bearing is fine.
   > **C. Canon-worthiness.** Is the finding coherent, non-trivial, and useful as a durable
   > reference, or thin/redundant? Judge substance, NOT length — a longer draft is not a
   > better one; padding, restatement, and verbose hedging count against it, not for it. For
   > a *definitive/synthesis* finding the bar is higher: it must genuinely compose across
   > findings and must not contradict a sibling finding without reconciling it.
   >
   > Treat A, B, C as three independent axes — a draft must clearly pass all three. Default
   > to **reject**; promote only if all three are clearly satisfied.
   >
   > **Then assign a GRADE certainty level** to what you are about to promote (skip if you
   > reject). Start the load-bearing core at **High** if it rests on primary papers / official
   > specs, **Low** if it rests on a single source or attributed secondary material. Then move
   > the level DOWN one per domain that applies, and record which:
   >   - *risk of bias / provenance* — any load-bearing claim leans on a weaker-tier source;
   >   - *inconsistency* — sources or sibling findings disagree and the draft doesn't resolve it;
   >   - *indirectness* — a source answers an adjacent question, not the exact claim;
   >   - *imprecision* — a load-bearing number/formula is single-sourced, hedged, or only
   >     approximately matched in the bytes;
   >   - *selective sourcing* — obvious primary evidence is missing or one-sided.
   > (Certainty is your confidence in the *evidence*, separate from whether it's worth
   > promoting — a thin-but-true finding can be High-certainty and still fail canon-worthiness.)
   >
   > Return, as the LAST TWO lines exactly:
   > `CERTAINTY: <high|moderate|low|very-low>` then `VERDICT: <promote|reject>`,
   > preceded by 2–5 lines of specific reasons per axis (name the failing claim or source,
   > and which downgrade domains you applied).

3. **Act on the verdict** (parse the subagent's last `VERDICT:` line; read `CERTAINTY:` from
   the line above it):
   - `promote` → `python3 scripts/promote.py promote "$D"`
   - `reject`  → `python3 scripts/promote.py reject "$D" --reason "ai-independent: <the reviewer's reasons, one line>"`
   - If no clear `VERDICT:` line is returned, treat it as **reject** (conservative default).
   - If a promote returns no clear `CERTAINTY:` line, record `very-low` (conservative default)
     and prefer to re-review rather than promote on an uncertain grade.
   Then log it (the certainty rides in the free-form `--data`, so no script change is needed
   to record graded confidence):
   ```
   python3 scripts/runlog.py log --flow process --step review --status ok \
     --data "{\"draft_id\":\"$D\",\"decision\":\"<promote|reject>\",\"certainty\":\"<high|moderate|low|very-low>\",\"reviewer\":\"ai-independent\"}"
   ```

4. **Integrity:** after acting, run `python3 scripts/check_integrity.py`; if it reports
   problems, surface them and stop.

The reviewer's authority is real — a `promote` moves the draft into `docs/findings/` and
appends it to `SYNTHESIS.md`; a `reject` frees its sources. A human can still override after
the fact (`promote.py promote/reject` by hand).

## Promotion is a streaming multiple-comparison problem

Each draft is independently "tested" for promotion, and the corpus has run this test 60+
times (56 promoted / 5 rejected to date). That is a **streaming multiple-testing** setup, and
the corpus's own findings name the discipline it implies — so the gate must reason about its
**false-promotion rate across the whole corpus**, not just per-draft.

- A single-draft promote decision is the analogue of an **always-valid** sequential test —
  the engine peeks at each draft as it arrives and decides at a data-dependent stopping time,
  which is exactly the regime where a naive fixed-threshold test loses its error guarantee
  (always-valid inference / mSPRT, **dc588b7cc**).
- Across the *stream* of drafts, single-test validity is not enough; the right target is
  **mFDR control over the family** via an online-FDR scheme — LORD's *alpha-investing*: start
  with an α-wealth budget below α and spend a fraction per test, earning wealth back on each
  rejection (online FDR for streams, **d42ec736c**). In this engine a **promote** is the
  "rejection of the null that the draft is not canon-worthy," so each promote is a discovery
  whose error contributes to the corpus-wide false-promotion rate.

**What this gate does about it (today):** the conservative defaults already approximate an
α-budget — *default-reject*, the *higher bar for definitive/synthesis findings*, and the
*GRADE certainty downgrades* all spend promotion-credit grudgingly, so a marginal draft is
rejected rather than promoted on a coin-flip. The `runlog.py` ledger (`decision` + `certainty`
per review) is the **append-only record needed to actually measure** the false-promotion rate:
the running promoted-vs-rejected counts and the certainty mix are the observable α-wealth.

**What stays a known gap:** no *quantitative* α-budget is tracked or enforced — a promote does
not debit a wealth counter, and there is no automated mFDR bound. The conservative bar is a
qualitative stand-in. Tightening it into a real online-FDR budget over the runlog ledger is the
grounded upgrade (d42ec736c) if the false-promotion rate ever needs a hard guarantee rather
than a defensible default.
