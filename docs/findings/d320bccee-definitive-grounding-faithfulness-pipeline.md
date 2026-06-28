---
id: d320bccee
topic: 08-grounding-truth
title: "The definitive grounding and faithfulness pipeline: claim extraction → atomic-fact scoring → attribution editing → NLI entailment, end to end"
status: draft
---

# The definitive grounding and faithfulness pipeline: claim extraction → atomic-fact scoring → attribution editing → NLI entailment, end to end

Measuring whether generated text is faithful to its sources is not one metric but a
*pipeline*, and four primary papers each formalize a different stage of it. This
synthesis composes them into one durable, defensible answer to: what is the canonical
grounding/faithfulness machinery, stage by stage; what is settled across the methods;
where they genuinely contest each other; and which stage to reach for when. It draws on
three sibling findings for navigation only — `d1ad78766` (FActScore atomic precision +
RARR attribution editing), `dfa42bc8a` (the generic faithfulness measurement machinery),
and `d636208ea` (RAGAS / ARES primary metric formulas). Those `d…` ids map territory;
they are never the citation of record. Every load-bearing claim below rests on a primary
paper cited inline as `[c<id>]`: FActScore (arXiv:2305.14251) [ce1c38128], RARR
(arXiv:2210.08726) [c6fc7d334], RAGAS (arXiv:2309.15217) [c1ee9053c], and ARES
(arXiv:2311.09476) [ccb6561db].

## The canonical pipeline, stage by stage — and which primary defines each

The four methods are not competing point solutions; read together they describe a single
end-to-end pipeline with four stages, each owned by a different primary.

1. **Claim / atomic-fact extraction.** Decompose a long-form generation into the smallest
   independently-checkable units. FActScore calls these **atomic facts** — short
   statements each conveying one piece of information that can independently be true or
   false [ce1c38128]. RAGAS performs the same decomposition under a different name,
   splitting the answer into **statements** before any scoring happens [c1ee9053c]. This
   shared decompose-first move is the backbone of the whole pipeline.

2. **Atomic-fact / statement scoring against a reference.** Score each unit as supported
   or not, then aggregate. FActScore defines the per-response score as the fraction of
   atomic facts supported by a specified knowledge source C: for a response `y` with
   atomic-fact list `A_y`, `f(y) = (1/|A_y|) · Σ_{a∈A_y} I[a supported by C]` — every
   atomic fact weighted equally [ce1c38128]. RAGAS computes faithfulness as the same
   shape against the *retrieved context*: the count of supported statements over total
   statements, reported as `F = |V| / |S|` [c1ee9053c]. (Both single-line equations are
   lossy in their papers' PDF→markdown conversion; the component tokens — `|A_y|`, the
   indicator over support, `|V|`, `|S|` — verify against the source bytes, and the clean
   renderings live in siblings `d1ad78766` and `d636208ea`. Stated here as the primaries
   express them: a decomposed-then-supported-fraction.)

3. **Attribution editing (repair, not verdict).** Where stages 1–2 *measure*, RARR
   *repairs*: it edits an arbitrary LM output so the revised text becomes attributable to
   freshly retrieved evidence, via a research-and-revision workflow of query generation →
   retrieval → agreement-check → edit [c6fc7d334]. RARR is explicitly model-agnostic — it
   improves the attribution of *any existing LM* rather than constraining generation
   [c6fc7d334].

4. **NLI / entailment verification underneath.** The "is this unit supported?" decision in
   stages 2–3 is, at bottom, a textual-entailment check. RARR makes this explicit: its
   automated attribution proxy is an NLI model, `Attr_auto(y, A) = avg_{s∈y} max_{e∈A}
   NLI(e, s)` — per sentence, the best entailment score over evidence [c6fc7d334].
   FActScore's automated estimator implements the same primitive differently: retrieve
   passages from C (GTR dense retriever, restricted to the topic entity's page) and let a
   strong LM (ChatGPT, or LLaMA with nonparametric-probability scoring) decide per atomic
   fact whether it is supported [ce1c38128].

## What is SETTLED across the methods

Three things are genuinely agreed across all four primaries — this is the defensible core.

- **Decompose before you score.** Every method first breaks the generation into atomic
  units (FActScore's atomic facts [ce1c38128]; RAGAS's statements [c1ee9053c]) or scores
  per sentence (RARR's sentence-level AIS [c6fc7d334]). No method scores a whole paragraph
  as one verdict; the unit of judgment is sub-sentential or sentential.

- **Score = fraction of units supported by a reference.** The aggregate is a
  supported-fraction in every case: FActScore's `f(y)` averages an indicator over atomic
  facts [ce1c38128]; RAGAS's faithfulness is supported statements over total `|V|/|S|`
  [c1ee9053c]; RARR's attribution is the average AIS across sentences,
  `Attr_AIS(y,A) = avg_{s∈y} AIS(s,A)` [c6fc7d334]. The differences are entirely in *what
  reference* the support is checked against.

- **The support check is entailment.** Whether expressed as an NLI model [c6fc7d334] or as
  retrieval-plus-LM judgment [ce1c38128], the per-unit decision is "does the evidence
  entail this unit?" RAGAS frames its verification identically — for each statement, decide
  if it is inferable from the retrieved context [c1ee9053c]. This is the shared
  atomic-decomposition + entailment-scoring backbone the sibling `dfa42bc8a` grounds
  generically.

## Where the methods genuinely DIVERGE

The contests are real and load-bearing; they are about *reference*, *output type*, and
*reliability*, not about the backbone.

**The reference differs — this is the grounding spectrum.** Faithfulness against
*retrieved context* is not factual precision against *the world*, and neither is the same
as *repairing* text into attributability. RAGAS scores an answer against its retrieved
context [c1ee9053c]; FActScore scores against a *specified external knowledge source* C —
its score is precision relative to *this* C, not absolute truth [ce1c38128]; RARR does not
emit a verdict at all, it edits output to *become* attributable to retrieved evidence
[c6fc7d334]. The spectrum runs: evaluate-vs-context (RAGAS) → evaluate-vs-knowledge-source
(FActScore) → repair-into-attributable (RARR).

**Verdict vs. repair.** FActScore and RAGAS are measurement metrics that emit a scalar;
RARR is a *revision* method whose output is edited text plus a report, not a faithfulness
number [c6fc7d334]. A system that only scores will tell you something is unfaithful; only
RARR fixes it.

**Prompt-only point score vs. trained-and-calibrated estimate.** This is the sharpest
contest, between the two RAG harnesses that score the *same* three dimensions. RAGAS is
reference-free and prompt-only — no training, no human labels — and emits a bare point
score with no error bar, so its reliability is exactly the (unbounded) reliability of the
prompting judge [c1ee9053c]. ARES instead fine-tunes lightweight per-dimension DeBERTa-v3
judges on synthetically generated query–passage–answer triples, then applies
prediction-powered inference (PPI) against a small human-annotated validation set to emit
*confidence intervals* on system scores rather than a bare judge average [ccb6561db]. The
payoff is measurable: validated by ranking accuracy (Kendall's τ) against human rankings,
ARES on real-world RAG systems averages τ = 0.91 for context relevance and τ = 0.97 for
answer relevance — 0.16 and 0.15 higher than RAGAS respectively [ccb6561db].

**Single-axis vs. dual-axis with a tension.** FActScore and RAGAS optimize one number;
RARR scores on two axes that are in explicit tension — Attribution (AIS) and Preservation,
where preservation is a function of character-level Levenshtein edit distance,
`Pres_Lev(x,y) = max(1 − Lev(x,y)/length(x), 0)`, rewarding changing the original as
little as possible [c6fc7d334]. The paper states optimizing attribution alone cannot
ensure a good revision (an adversarial editor could overwrite everything), so the pair has
no free optimum [c6fc7d334].

## The composed recommendation — which stage/metric to use when

- **You have generation + the context it was retrieved from, and want a fast, label-free
  grounding score:** use RAGAS faithfulness — supported statements over total, `|V|/|S|`,
  no training required [c1ee9053c]. Accept that the output is a point estimate with no
  error bar [c1ee9053c].
- **You need that score to be *trustworthy* / comparable across systems with a confidence
  interval:** use ARES — trained DeBERTa-v3 judges debiased with PPI against ~human-labeled
  validation, materially closer to human rankings (τ up to 0.97) [ccb6561db].
- **You are checking factual precision against an authoritative knowledge base (not just
  the retrieved snippets):** use FActScore — atomic-fact precision against a chosen C, with
  the automated estimator scoring abstaining/unsupported responses as 0.0 [ce1c38128].
- **You want to *fix* an ungrounded output, not just flag it:** use RARR to retrofit
  attribution, accepting the Attribution↔Preservation trade-off [c6fc7d334].

## Honest limits

- **The reference defines the verdict.** FActScore is precision relative to a *specified*
  C — "supported" means "entailed by this C," not "true" [ce1c38128]; RAGAS faithfulness is
  relative to whatever was retrieved [c1ee9053c]. A perfectly grounded answer can still be
  wrong about the world if C or the retrieval is wrong.
- **Recall blind spots.** The supported-fraction backbone scores *precision* — the fraction
  of emitted units that are supported [ce1c38128] — and says nothing about facts the
  generation omitted. Faithfulness is not completeness.
- **The prompting judge is the unbounded weak link.** RAGAS routes its score through an
  LLM judge with no error bar, so reliability equals the judge's [c1ee9053c]; ARES's PPI
  confidence intervals exist precisely to bound that, but only against a small human
  validation set [ccb6561db].
- **Citation accuracy trades against edit volume.** RARR's Attribution/Preservation pair
  has no free optimum [c6fc7d334]; a grounding-by-editing system cannot simultaneously
  maximize attribution coverage and minimize how much it rewrites.
- **Cost and validation.** FActScore's automated estimator exists because human evaluation
  is costly, and it is validated to approximate the human FActScore with an error rate
  below 2% [ce1c38128]; that error rate — not the separately-reported r = 0.99 *inter-
  estimator* agreement between its two automated variants [ce1c38128] — is the human-
  approximation fidelity, and it was established on people-biography generation against
  Wikipedia, not arbitrary domains [ce1c38128].
- **Formula fidelity.** The exact single-line renderings of RAGAS `F=|V|/|S|` and
  FActScore `f(y)` are lossy in the primaries' PDF→markdown conversion; the component terms
  verify against source bytes, and the clean equations are carried by siblings `d636208ea`
  and `d1ad78766`.
