---
id: d1ad78766
topic: 08-grounding-truth
title: "FActScore atomic-fact precision and RARR attribution editing: two grounding-truth primitives, grounded on their own papers"
status: draft
---

This finding closes gap `g4668dd58` by grounding two complementary
factuality/attribution primitives directly on their primary papers: **FActScore**
[ce1c38128] (atomic-fact precision against a knowledge source) and **RARR**
[c6fc7d334] (post-hoc editing of an LM output to make it attributable). It
complements two existing findings rather than restating them. `dfa42bc8a`
(faithfulness measurement machinery) grounds faithfulness generically as an
atomic-statement / NLI-entailment metric; FActScore is the **named precision
sibling** of that mechanism — it formalizes "fraction of atomic facts supported"
into a single scalar `f(y)` and pins it explicitly to a chosen knowledge source
[ce1c38128]. `d636208ea` (RAGAS/ARES primary formulas) grounds the named RAG-eval
harnesses that score a system's output against its **retrieved context**;
FActScore instead scores against a **specified knowledge source**, and RARR does
something different again — it **edits** an arbitrary LM output into an
attributable one [c6fc7d334]. The three thus sit at three distinct points on the
grounding/attribution spectrum, made explicit in the last sub-section.

## FActScore: definition and the f(y) = (1/|A_y|) Σ I[a⊨C] formula

FActScore decomposes a long-form generation into **atomic facts** — short
statements each conveying one piece of information that can independently be true
or false — and scores the **percentage of those atomic facts supported by a given
knowledge source C** [ce1c38128]. Formally, for a language model M, a prompt set
X, a knowledge source C, a response y = M_x to prompt x, and its list of atomic
facts A_y, the per-response score is

  **f(y) = (1/|A_y|) · Σ_{a ∈ A_y} I[a is supported by C]**

— the fraction of atomic facts in y entailed by C, with every atomic fact given
equal weight [ce1c38128]. The model-level FActScore aggregates this over prompts
where the model actually responds: **FActScore(M) = E_{x∈X}[ f(M_x) | M_x
responds ]**, where "responds" means M did not abstain on x [ce1c38128]. The
definition rests on two stated assumptions: that whether an atomic fact is
supported by C is undebatable, and that every atomic fact in A_y carries equal
importance [ce1c38128].

The load-bearing property is that FActScore is **factual precision relative to a
specified C, not absolute truth** — the score is defined per knowledge source, so
"supported" means "entailed by *this* C" [ce1c38128]. In the paper's main
evaluation, C is the English Wikipedia and the task is people-biography
generation: the authors sample 183 people entities from Wikidata with Wikipedia
pages, choosing biographies because they are objective, specific, and
self-consistent, satisfying the definition's assumptions [ce1c38128]. Their human
evaluation gives headline FActScores of **42.5% (InstructGPT), 58.3% (ChatGPT),
and 71.5% (PerplexityAI)** — i.e. even commercial LMs are "riddled with errors" —
and these scores drop sharply as entity rarity rises (e.g. 80% → 16% for ChatGPT
across rarity bins) [ce1c38128].

## FActScore's automated estimator (retrieval + LM, abstain → 0) and its validation

Because human evaluation is costly (the paper estimates evaluating 12 LMs by hand
would have cost ≈$65K), FActScore introduces an **automated estimator** that
decomposes a generation into atomic facts and validates each one against the
given knowledge source using **retrieval plus a strong language model**
[ce1c38128]. Concretely, the estimator retrieves passages from C (Wikipedia,
restricted to the topic entity's page, with a GTR dense retriever) and uses a
competitive LM (ChatGPT, or LLaMA with nonparametric-probability scoring) to
decide per atomic fact whether it is supported [ce1c38128]. An **abstaining or
otherwise unsupported response is scored 0.0**, consistent with the definition's
"M responds" gate [ce1c38128].

Validation is reported as the estimator's **error rate versus the human
FActScore**: the retrieval-augmented estimator approximates the human FActScore
with an **error rate of < 2%**, and the two best estimator variants (ChatGPT and
LLaMA+NP, both with retrieval) rank the 13 subjects (humans + 12 LMs)
near-identically — the two metrics' scores correlate at **Pearson r = 0.99**
[ce1c38128]. The paper also reports a complementary per-decision quality metric
(F1_MICRO over individual atomic-fact judgments) alongside the aggregate error
rate, noting the two can rank evaluators differently — an estimator may have a
better F1_MICRO yet systematically over- or under-estimate the aggregate
[ce1c38128].

## RARR: the "Editing for Attribution" task (research → revise → attribution report)

RARR (Retrofit Attribution using Research and Revision) formalizes the task of
**Editing for Attribution**: given a text passage x produced by *any* generation
model, produce a revised passage y plus an **attribution report A = {e_1, ..., e_M}**
of evidence snippets that support the content in y [c6fc7d334]. RARR is
deliberately **model-agnostic** — rather than constraining the LM to generate
attributed text, it retrofits attribution onto an existing model's output, which
the paper frames as retrieval-augmentation that happens *after* generation rather
than before [c6fc7d334].

The pipeline has two stages [c6fc7d334]:

- **Research** — a query generator raises comprehension questions about different
  aspects of x, and a retriever searches for evidence to investigate each query.
- **Revision** — an agreement model detects disagreement between the text and the
  retrieved evidence, and an edit model revises the text only where needed; M
  evidence snippets (the paper finds M = 5 sufficient for full attribution) are
  then selected to form the attribution report A.

The defining constraint is that the revision must make y **attributable to the
retrieved evidence while preserving the original output's intent and content as
much as possible** [c6fc7d334].

## RARR's two metrics: Attribution (AIS) and Preservation (Levenshtein), and their trade-off

RARR evaluates the revised text along **two dimensions** [c6fc7d334]:

- **Attribution** is measured with **AIS (Attributable to Identified Sources)**.
  Binary sentence-level AIS asks, for each sentence s of y, whether a generic
  hearer would affirm "According to A, s" — full credit (1.0) only if all content
  is attributable, no credit (0.0) otherwise. RARR reports the **average AIS
  across sentences**, Attr_AIS(y, A) = avg_{s∈y} AIS(s, A) [c6fc7d334]. For
  model development it uses an automated proxy, **auto-AIS (Attr_auto)**, built on
  an NLI entailment model: Attr_auto(y, A) = avg_{s∈y} max_{e∈A} NLI(e, s)
  [c6fc7d334].

- **Preservation** is measured by a function of the **character-level Levenshtein
  edit distance** between x and y:

    **Pres_Lev(x, y) = max( 1 − Lev(x, y) / length(x), 0 )**

  which is 1.0 when x and y are identical and 0.0 when the revision completely
  overwrites x — it rewards changing the original as little as possible
  [c6fc7d334]. The full preservation metric combines an intent term with this
  edit-distance term, **Pres_comb(x, y) = Pres_intent(x, y) · Pres_Lev(x, y)**;
  since Pres_intent requires human annotation, Pres_Lev serves as the automated
  proxy during development [c6fc7d334].

The two metrics are in explicit tension. The paper notes that **optimizing for
attribution alone cannot ensure a good revision** — an adversarial editor could
trivially reach 100% attribution by replacing x with the text of any retrieved
document (attributable to itself), so preservation is the necessary counterweight
[c6fc7d334]. RARR therefore reports both and their **harmonic mean F1_AP**
(analogous to combining precision and recall) as the combined score, and the
experiments show RARR significantly improves attribution while keeping
preservation high relative to a rewrite-everything baseline (EFEC, which collapses
the passage into a single sentence) [c6fc7d334]. The automated metrics are
validated against human judgments: on the NQ benchmark, human AIS vs. auto-AIS
correlate at **Pearson 0.74 (N = 450)**, and human-vs-automated preservation at
**Pearson 0.62** [c6fc7d334].

## The three-point grounding spectrum: evaluate-vs-context / evaluate-vs-knowledge-source / repair-into-attributable

These three primitives are not interchangeable; they occupy three distinct points
on the grounding/attribution spectrum:

1. **Evaluate-vs-context (RAGAS / ARES, `d636208ea`).** RAGAS faithfulness and
   ARES's fine-tuned judges score a RAG system's answer against the **retrieved
   context that the system itself surfaced** — the reference is the system's own
   retrieval, and the question is whether the answer is supported by *what was
   retrieved* [d636208ea].

2. **Evaluate-vs-knowledge-source (FActScore).** FActScore scores factual
   precision against a **specified external knowledge source C** (e.g. Wikipedia),
   independent of any retrieval the generator may or may not have done — `f(y)` is
   the fraction of atomic facts entailed by C [ce1c38128]. The anchor is a chosen
   ground-truth corpus, not the system's retrieval set.

3. **Repair-into-attributable (RARR).** RARR neither scores against context nor
   against a fixed corpus to produce a verdict — it **edits** an arbitrary LM
   output so that the *revised* text becomes attributable to freshly retrieved
   evidence, emitting both the revised passage and an attribution report
   [c6fc7d334]. It is a repair/retrofit operation, not just a measurement.

So the spectrum runs evaluate-vs-context → evaluate-vs-knowledge-source →
repair-into-attributable: RAGAS/ARES judge against retrieval, FActScore judges
against a knowledge source, RARR rewrites to make output attributable. All three
share the same atomic/sentence-level decomposition-then-entailment substrate that
`dfa42bc8a` grounds generically [ce1c38128] [c6fc7d334].

## Gaps found

- **RARR's exact headline result-table deltas are lossy in conversion.** The
  precise per-benchmark attribution-improvement points and preservation-percentage
  retained (PaLM / LaMDA outputs across NQ, SQA, QReCC; the F1_AP level-curve
  table) are mangled by the PDF→markdown table conversion and cannot be recovered
  glyph-by-glyph; only the qualitative claim ("significantly improves attribution
  while keeping preservation high vs. the EFEC baseline") and the validation
  correlations (auto-AIS 0.74, preservation 0.62) are cleanly readable
  [c6fc7d334]. A clean re-extraction of the original PDF tables would pin the
  exact numbers.
- **FActScore atomic-fact decomposition prompt details not grounded.** The exact
  prompt / procedure by which a generation is split into atomic facts (and the
  decontextualization rules) is only partially recoverable from the converted
  text and is not reproduced here.
- **TruLens "RAG Triad" primary still ungrounded.** As flagged in `d636208ea`,
  TruLens's groundedness/context-relevance/answer-relevance definitions remain
  blog-attributed; this finding does not close that.
- **FActScore F1_MICRO vs. Error-Rate ranking divergence** (the worked Figure-4
  example where two evaluators rank differently under F1_MICRO vs. ER) is reported
  qualitatively here; the exact figure numbers in that comparison are partially
  recovered from a mangled table [ce1c38128].
