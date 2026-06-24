---
id: d4c45dd7e
topic: 16-evaluation-benchmarks
title: "LLM-as-judge reliability: bias magnitudes, judge-human correlation, and the TruLens RAG-Triad decomposition"
status: draft
---

This finding grounds the **reliability** of LLM-as-judge — the named biases with the
magnitudes their originating studies report, and how well judge verdicts correlate with
human judgment under raw vs. chance-corrected metrics — and the **TruLens RAG-Triad**
as the per-axis decomposition that makes such a judge operationally tractable. It draws on
the foundational MT-Bench paper [ceadbfa68], the systematic alignment study of Thakur et
al. [cc884c0e5], and the official TruLens RAG-Triad documentation [c5f5c1369]. It
**complements, and does not restate, two existing findings**: `d636208ea` already grounds
the RAGAS/ARES primary metric *formulas* (`F = |V|/|S|`, the answer-relevance cosine,
ARES's fine-tuned judges + prediction-powered inference) — consult it for the formulas, not
here; and `dfa42bc8a` grounds the faithfulness *measurement machinery* (atomic-statement /
NLI-entailment structured judging and the judge-calibration guardrail). This finding sits
upstream of both: it concerns whether the judge can be trusted at all, and how to structure
it so it can be.

## The LLM-as-judge paradigm

LLM-as-judge is the use of a strong LLM (e.g. GPT-4) as a surrogate evaluator: instead of
collecting human preference labels, the LLM is prompted to grade or compare model outputs,
either by pairwise comparison or by single-answer grading on a rubric [ceadbfa68]. The
MT-Bench paper frames its two key benefits as **scalability** (reducing human involvement,
enabling fast iteration) and **explainability** (the judge emits not just a score but a
rationale) [ceadbfa68]. The same paper is explicit that the approach has limitations it
groups as **position bias, verbosity bias, self-enhancement bias, and limited reasoning
ability** [ceadbfa68].

## Measured biases (MT-Bench)

**Position bias** — the judge's propensity to favor an answer by its slot rather than its
quality. MT-Bench measures it as *consistency*: the percentage of cases where a judge gives
the same verdict when the two answers' order is swapped [ceadbfa68]. With the default
prompt, **GPT-4 was consistent on 65.0%** of swapped pairs (favoring the first answer in
30.0% of cases), **GPT-3.5 on 46.2%**, and **Claude-v1 on only 23.8%** (favoring the first
answer 75.0% of the time) [ceadbfa68]. The bias is not unique to LLMs and has been observed
in human decision-making [ceadbfa68].

**Verbosity bias** — "when an LLM judge favors longer, verbose responses, even if they are
not as clear, high-quality, or accurate as shorter alternatives" [ceadbfa68]. MT-Bench
probes it with a "repetitive list" attack on 23 model answers, padding each with a
rephrased duplicate that adds no information [ceadbfa68]. Under this attack the judge
**failure rate was 91.3% for Claude-v1 and 91.3% for GPT-3.5, versus 8.7% for GPT-4** — i.e.
only GPT-4 reliably detected the padding [ceadbfa68].

**Self-enhancement bias** — the suspected tendency of a judge to favor its own outputs.
MT-Bench observes that **GPT-4 favors itself with a 10% higher win rate, and Claude-v1
favors itself with a 25% higher win rate**, relative to human preference [ceadbfa68].
Critically, the paper does **not** claim this proves the bias: "Due to limited data and
small differences, our study cannot determine whether the models exhibit a self-enhancement
bias," and notes GPT-3.5 does not favor itself [ceadbfa68]. The magnitudes are therefore a
caution flag, not an established effect.

**Limited capability in grading math/reasoning** — even when a judge can *solve* a problem,
it can mis-grade it, "misled by the provided answers" [ceadbfa68]. On 10 elementary-math
grading questions (tested in both orderings, 20 trials), **GPT-4's failure rate — counting
cases where it called an incorrect answer correct — was 14/20 with the default prompt,
dropping to 6/20 with chain-of-thought prompting and 3/20 when given a reference solution**
[ceadbfa68]. GPT-3.5 and Claude-v1 showed the same weakness [ceadbfa68]. The fix the paper
proposes is reference-guided grading [ceadbfa68].

## Judge-human agreement

MT-Bench's headline reliability result is that a strong LLM judge reaches human-level
agreement. Excluding ties (setup S2), **agreement between GPT-4 and human experts reaches
85%, which is higher than the agreement among humans themselves (81%)** [ceadbfa68]. The
abstract states the same result as GPT-4 matching human evaluation "at an agreement rate
exceeding 80%, achieving the same level of human-human agreement" [ceadbfa68]. Agreement
rises with the performance gap between the two models being compared — from ~70% up to
nearly 100% as the win-rate difference widens [ceadbfa68].

Thakur et al. sharpen this by separating **raw percent agreement** from **chance-corrected
alignment**, using percent agreement alongside **Scott's π** (a chance-corrected
inter-annotator coefficient the paper recommends as the more robust measure) [cc884c0e5]. Their central finding is that
the two metrics tell different stories: **percent alignment is high for virtually all judge
models, but Scott's π is low for most** — the chance correction collapses the apparent
agreement [cc884c0e5]. Even the best-aligned judges (Llama-3 70B, Llama-3.1 70B, GPT-4
Turbo) reach Scott's π only "in the high 80s," and **the best-scoring judge, Llama-3 70B, is
8 points behind human judgment** [cc884c0e5]. For context, human evaluators agreed with the
human majority vote at a Scott's π of **96.2 ± 1.07** and percent agreement of **98.52% ±
0.42%** [cc884c0e5]. The paper's stated recommendation: **compute both percent agreement and
Scott's π, paired with qualitative analysis, and caution against blindly trusting judge
verdicts even when they appear aligned with humans** — because aligned judges' scores can
still differ by up to 5 points from human scores [cc884c0e5].

## The TruLens RAG-Triad: per-axis decomposition

The TruLens documentation defines the **RAG Triad** as three feedback functions that
evaluate a RAG application along each edge of its architecture [c5f5c1369]:

- **Context relevance** — verifying that each retrieved chunk of context is relevant to the
  input query, since irrelevant retrieved context can be woven into a hallucination
  [c5f5c1369].
- **Groundedness** — after the LLM forms an answer, separating the response into individual
  claims and independently searching the retrieved context for evidence supporting each
  [c5f5c1369].
- **Answer relevance** — verifying that the final response actually addresses the original
  user query [c5f5c1369].

TruLens's stated claim is structural, not a performance benchmark: "Satisfactory evaluations
on each provides us confidence that our LLM app is free from hallucination," and reaching
satisfactory evaluations across the triad lets one state the application "is verified to be
hallucination free up to the limit of its knowledge base" [c5f5c1369]. The operational point
for a citation-gated engine is that this decomposes a holistic "is this answer good?"
judgment — the kind shown above to be bias-prone and hard to calibrate — into three narrow,
single-axis judgments that a judge can render far more tractably.

## Synthesis: the practical rule for a citation-gated engine

LLM-as-judge is usable for grounding/faithfulness gating only under three disciplines that
the sources jointly motivate:

1. **Decompose into RAG-Triad-style per-axis judgments** rather than asking for one holistic
   verdict — judge context relevance, groundedness, and answer relevance separately
   [c5f5c1369], which is the same per-dimension split the named harnesses operationalize
   (see `d636208ea` for their formulas).
2. **Control for the named biases**: average over swapped positions to neutralize position
   bias (consistency as low as 23.8% for weak judges, 65.0% even for GPT-4) [ceadbfa68];
   guard against verbosity inflation (only GPT-4 resisted the repetitive-list attack, at
   8.7% failure vs. 91.3% for the others) [ceadbfa68]; and never let a model judge its own
   outputs unguarded given the observed self-favoring win-rate gaps [ceadbfa68].
3. **Calibrate against chance-corrected agreement, not raw percent agreement** — Scott's π /
   Cohen's κ, not bare percent, because percent agreement overstates alignment and even the
   best judges trail human judgment by ~8 points on the chance-corrected metric [cc884c0e5].
   This is the upstream version of the judge-calibration guardrail that `dfa42bc8a` records
   at the faithfulness-mechanism level.

In short: a judge is trustworthy for citation gating to the extent it is decomposed,
de-biased, and chance-corrected against human labels — never on the strength of a high raw
agreement number alone.
