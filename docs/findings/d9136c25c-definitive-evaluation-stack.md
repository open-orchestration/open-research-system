---
id: d9136c25c
topic: 16-evaluation-benchmarks
title: "The definitive evaluation stack: what to measure, with which metric, under which regime, and the judge biases to correct"
status: draft
---

# The definitive evaluation stack: what to measure, with which metric, under which regime, and the judge biases to correct

Evaluating a deep-research / RAG system is not one measurement problem but a layered
one, and six prior findings each pin down a different layer. This synthesis composes
them into a single durable answer to: *what to measure, with which metric, under
which regime, and which judge biases to correct.* It draws on `d6fad1a98` (the two
evaluation regimes — frozen-web agent benchmarks vs. decomposed RAG harnesses),
`d69d7458e` (GAIA / BrowseComp task design and scores), `d636208ea` (RAGAS / ARES
primary metric formulas), `d1ad78766` (FActScore atomic precision + RARR attribution
editing), `dfa42bc8a` (the faithfulness measurement machinery underneath), and
`d4c45dd7e` (LLM-as-judge reliability — biases, agreement, the RAG-Triad). The
contribution here is the *stack*: how the regimes nest, when one metric supersedes
another, and why the judge sits underneath the whole thing so its biases propagate up
into every quality number the system reports.

## Provenance note

Every load-bearing claim below is anchored on a strong primary — a named paper or an
official framework doc, cited inline as `[c<id>]`: GAIA (arXiv:2311.12983)
[c57655b9e], BrowseComp (arXiv:2504.12516) [cedea9fbe], RAGAS (arXiv:2309.15217)
[c1ee9053c], ARES (arXiv:2311.09476) [ccb6561db], FActScore (arXiv:2305.14251)
[ce1c38128], RARR (arXiv:2210.08726) [c6fc7d334], MT-Bench (arXiv:2306.05685)
[ceadbfa68], Judging-the-Judges (arXiv:2406.12624) [cc884c0e5], and the TruLens
RAG-Triad official docs [c5f5c1369]. The sibling findings (`d…` ids) are referenced
in prose only to map territory; they are not the citation of record. Where a formula
(RAGAS `F=|V|/|S|`, FActScore `f(y)`) is reported, the component terms verify against
the primary source bytes but the single-line glyph rendering is mangled by the
paper's PDF→markdown conversion — the clean renderings live in `d636208ea` and
`d1ad78766`; the claims here are stated as the primaries express them (a
decomposed-then-supported-fraction), not as exact transcribed equations.

## Two regimes — they measure different things, with different reliability properties

The first decision is *which regime you are in*, because the two answer different
questions and fail in different ways.

**Regime A — the web-research AGENT.** Here the unit of evaluation is the whole agent:
did it find and reason to the correct answer across a multi-step trace? This regime
is anchored on frozen-corpus agent benchmarks. GAIA grades general-assistant
questions that require planning across web browsing, coding, multimodality, and file
reading, scored by quasi-exact-match on a factoid answer [c57655b9e]. BrowseComp
isolates a different competency — persistent browsing for a single hard-to-find fact
that is easy to verify once located [cedea9fbe]. The signature both share, by
construction, is a large human-vs-model gap: GAIA reports 92% human accuracy vs. 15%
for GPT-4 with plugins [c57655b9e]; BrowseComp reports a 29.2% human-trainer solve
rate against models ranging from near-zero (GPT-4o at 0.6%) up to OpenAI Deep Research
at 51.5% — the only system to exceed the human baseline [cedea9fbe]. The two are
complementary: GAIA probes multi-tool orchestration, BrowseComp probes depth and
persistence.

**Regime B — RAG grounding.** Here the unit is the answer relative to what was
retrieved, and quality is *decomposed* into a retrieval axis and a generation axis so
a regression can be attributed to the side that broke. RAGAS and ARES both operate on
the same three-dimension split — context relevance, faithfulness/groundedness, and
answer relevance [c1ee9053c] [ccb6561db]. This is the regime the named harnesses
occupy.

The two regimes are not interchangeable; a deep-research system needs both, because
Regime A tells you whether the agent *found the right answer* and Regime B tells you
whether the synthesis *stayed grounded in its sources*. A system can pass one and fail
the other.

## The metrics in each regime

**Agent regime → task success / quasi-exact-match.** GAIA's grade is quasi-exact-match
against a reference factoid [c57655b9e]; BrowseComp's answers are constructed to be
hard to find but easy to verify, so scoring is a near-exact correctness check
[cedea9fbe]. The reported human-vs-model gaps above are the design property that makes
these benchmarks discriminate genuine research capability from surface
pattern-matching.

**RAG regime → decomposed reference-free vs. calibrated metrics.** Within Regime B
there are two named approaches sitting at different points on a reliability/cost
trade-off:

- **RAGAS** is reference-free and prompt-only. Faithfulness is computed by
  decomposing the answer into statements and taking the fraction supported by the
  retrieved context — reported as `F=|V|/|S|`, the count of supported statements over
  total statements [c1ee9053c]. Answer relevance is the mean cosine similarity
  between the original question and questions generated from the answer [c1ee9053c],
  and context relevance scores how much of the retrieved context is on-topic
  [c1ee9053c]. RAGAS needs no training and no human labels, but emits a point score
  with no error bar, so its reliability is exactly the (unbounded) reliability of the
  prompting judge [c1ee9053c].

- **ARES** scores the same three dimensions but fine-tunes lightweight per-dimension
  DeBERTa-v3 judges on synthetically generated query–passage–answer triples, then
  applies prediction-powered inference (PPI) against a small (~150+) human-annotated
  validation set to emit confidence intervals on system scores rather than a bare
  judge average [ccb6561db]. ARES validates by ranking accuracy (Kendall's τ) against
  human rankings and on real-world RAG systems averages τ of 0.91 for context
  relevance and 0.97 for answer relevance — 0.16 and 0.15 higher than RAGAS
  respectively [ccb6561db].

**The grounding/attribution pair (a third measurement target).** Faithfulness against
*retrieved context* is not the same as factual precision against *the world*, and not
the same as *repairing* output to be attributable — so two further primitives extend
the RAG regime along a grounding spectrum. FActScore scores atomic factual precision
against a specified external knowledge source C (e.g. Wikipedia): a generation is split
into atomic facts and `f(y)` is the fraction of those facts supported by C, with an
automated estimator that abstains to 0 when no fact can be checked [ce1c38128]. RARR
is not a verdict metric at all — it *edits* an arbitrary LM output so the revised text
becomes attributable to freshly retrieved evidence, scoring the result on two axes:
Attribution (AIS — attributable to identified sources) and Preservation (how little
the original was changed, measured via Levenshtein) [c6fc7d334]. So the spectrum runs:
evaluate-vs-context (RAGAS/ARES) → evaluate-vs-knowledge-source (FActScore) →
repair-into-attributable (RARR).

## The judge underneath both regimes

Both regimes ultimately route quality through an LLM judge — RAGAS by prompting,
ARES's automated traces, and any faithfulness scorer — so the whole stack inherits
judge (un)reliability. This is the load-bearing layer, and three disciplines are
jointly motivated by the primaries.

**Decompose per-axis.** Do not ask for one holistic verdict; the TruLens RAG-Triad
splits evaluation into context relevance, groundedness, and answer relevance as
separate judgments [c5f5c1369] — the same per-dimension split the named harnesses
operationalize.

**Control the named biases.** MT-Bench groups the judge's documented weaknesses as
position bias, verbosity bias, self-enhancement bias, and limited reasoning ability
[ceadbfa68]. These are measurable, not hypothetical: position consistency is as low as
23.8% for weak judges and only 65.0% even for GPT-4, motivating averaging over swapped
positions [ceadbfa68]; on a repetitive-list verbosity attack only GPT-4 resisted, at
8.7% failure vs. 91.3% for the other judges [ceadbfa68]; and self-enhancement means a
model should never judge its own outputs unguarded [ceadbfa68].

**Calibrate on chance-corrected agreement.** MT-Bench's headline is that GPT-4 reaches
85% agreement with human judges, above the 81% agreement humans reach with each other
[ceadbfa68] — but that is raw percent agreement, which overstates alignment. The
Judging-the-Judges work shows the calibration must use chance-corrected metrics
(Scott's π / Cohen's κ), and on that metric even the best judges trail human judgment
by a meaningful margin [cc884c0e5]. The rule: trust a judge to the extent it is
decomposed, de-biased, and chance-corrected against human labels — never on the
strength of a high raw-agreement number alone.

## Tensions reconciled — when to use which

**Reference-free point scores (RAGAS) vs. calibrated intervals (ARES).** These are not
rivals to rank but tools for different phases. RAGAS is cheap and immediately
deployable — prompt-only, no labels, no training — so it fits fast iteration and
regression smoke-testing, accepting that its score is exactly as reliable as the
prompting judge with no error bar [c1ee9053c]. ARES costs a human-label budget and a
fine-tuning step but returns debiased estimates with confidence intervals and ranks
systems more accurately [ccb6561db]; use it when a *decision* rests on the number (e.g.
declaring system A better than system B) and the judge-variance risk must be bounded.
In short: RAGAS to monitor, ARES to decide.

**Context-faithfulness vs. world-factuality.** A high RAGAS faithfulness score means
the answer is supported by *what was retrieved* [c1ee9053c]; it says nothing about
whether the retrieval itself was correct. FActScore closes that gap by scoring against
an external knowledge source independent of the system's own retrieval [ce1c38128]. A
deep-research system that retrieves wrong sources can be perfectly faithful and
factually wrong — so the two metrics must both be read, not substituted.

**Attribution accuracy vs. volume (the RARR tension).** RARR's two axes pull against
each other: maximizing Attribution (rewriting freely until every claim is supported)
degrades Preservation (the output drifts from the original) [c6fc7d334]. There is no
single number that captures "well-attributed"; the pair must be reported together, and
the same accuracy-vs-volume tension applies to any citation-gated engine — more
citations is not strictly better if accuracy per citation falls.

## Honest limits

- **The judge is the shared weak link.** Both regimes route quality through an LLM
  judge whose biases (position, verbosity, self-enhancement) and variance are
  documented and only *partially* mitigable [ceadbfa68]; judge scores should be
  treated as data to be validated, not as ground truth.
- **Raw agreement overstates alignment.** The 85% / 81% MT-Bench agreement figures are
  raw percent [ceadbfa68]; chance-corrected agreement is lower and is the metric that
  should gate any "the judge is good enough" claim [cc884c0e5].
- **Citation accuracy trades against volume.** RARR's Attribution/Preservation pair has
  no free optimum [c6fc7d334]; a citation-gated system cannot simultaneously maximize
  coverage and minimize edit distance.
- **Formula fidelity.** The exact single-line renderings of RAGAS `F=|V|/|S|` and
  FActScore `f(y)` are lossy in the primaries' PDF→markdown conversion; the component
  terms verify but the clean equations are carried by `d636208ea` and `d1ad78766`.
