---
id: d636208ea
topic: 16-evaluation-benchmarks
title: "Primary metric formulas of RAGAS and ARES: reference-free LLM-prompting (F=|V|/|S|, AR cosine) vs. fine-tuned judges debiased with prediction-powered inference"
status: draft
---

This finding grounds the **primary metric definitions and validation methodology** of the
two most-cited automated RAG-evaluation harnesses — RAGAS [c1ee9053c] and ARES
[ccb6561db] — directly on their own peer-reviewed papers (RAGAS at EACL 2024 demo,
arXiv:2309.15217; ARES at NAACL 2024, arXiv:2311.09476). It complements two existing
findings rather than restating them. `dfa42bc8a` (faithfulness measurement machinery)
established faithfulness as an atomic-statement / NLI-entailment metric computed by
structured LLM judging at the *mechanism* level; this finding pins the *named-harness
primary formulas* that sit on top of that mechanism — RAGAS's `F = |V|/|S|` and the
answer-relevance cosine, and ARES's fine-tuned judges plus prediction-powered inference.
`d6fad1a98` (two evaluation regimes) named RAGAS/ARES/TruLens as the decomposed-RAG-harness
regime; this finding supplies the actual RAGAS and ARES formulas that finding referenced
without re-deriving its two-regimes framing.

## RAGAS faithfulness — decompose-then-verdict, F = |V|/|S|

RAGAS is explicitly **reference-free**: the authors target metrics that are "fully
self-contained" because in practice "we usually do not have access to human-annotated
datasets or reference answers" [c1ee9053c]. Faithfulness is the first of three quality
aspects and "refers to the idea that the answer should be grounded in the given context"
[c1ee9053c].

Estimation is a two-step LLM-prompting procedure [c1ee9053c]:
1. **Decompose.** Prompt an LLM to break the answer `a_s(q)` into a set of shorter,
   focused statements `S` — "the [goal] of this step is to decompose longer sentences
   into shorter and more focused assertions" [c1ee9053c].
2. **Verdict.** For each statement `s_i` in `S`, the LLM applies a verification function
   `v(s_i, c(q))` that "determines if `s_i` can be inferred from `c(q)`", prompted to
   decide whether each statement is supported by the context and to give a final
   Yes/No verdict per statement [c1ee9053c].

The final **faithfulness score F** is the fraction of statements supported by the context.
The paper states it as **F = |V| / |S|**, "where |V| is the number of statements" supported
and |S| is the total number of statements [c1ee9053c]. (The paper's PDF→markdown
conversion squashes the denominator; the canonical form `F = |V|/|S|` — supported
statements over total statements — is confirmed by the surrounding text, which shows both
`|V|` and `|S|` flanking the `F =` expression [c1ee9053c].)

## RAGAS answer relevance (Eq. 1) and context relevance (Eq. 2)

**Answer Relevance (AR)** captures whether "the generated answer should address the actual
question" and "penalizes the presence of redundant information or incomplete answers"
[c1ee9053c]. Estimation: prompt the LLM to generate `n` questions from the answer, embed
each generated question `q_i` and the original question `q` with the
`text-embedding-ada-002` model, and compute the similarity `sim(q, q_i)` as the cosine
between the corresponding embeddings [c1ee9053c]. The score is the mean over the generated
questions, given in the paper as **Eq. (1): AR = (1/n) · Σ_{i=1..n} sim(q, q_i)**
[c1ee9053c]. Higher AR means the answer addresses the actual question; incomplete or
redundant answers drive the generated questions away from `q` and lower the score. (The
`1/n` factor and summation are rendered as `AR = sim(q,q_i) (1)` with stray `n` and `i=1`
fragments in the conversion; the canonical mean-cosine form is recoverable from the
adjacent text — `n` generated questions, the explicit `sim(q,q_i)` cosine, and the
summation glyph — and is reported here as such rather than guessed [c1ee9053c].)

**Context Relevance (CR)** measures whether the retrieved context is focused, "containing
as little irrelevant information as possible" [c1ee9053c]. Given a question `q` and its
context `c(q)`, the LLM "extracts a subset of sentences" from `c(q)` "that are crucial to
answer q" [c1ee9053c]. The paper defines **Eq. (2): CR = (number of extracted sentences) /
(total number of sentences in c(q))** [c1ee9053c]. CR penalizes retrieving redundant or
irrelevant context: the more of the retrieved context the judge has to discard as
non-essential, the lower the score.

## RAGAS validation — WikiEval, agreement with human annotators

RAGAS is validated on **WikiEval**, a dataset the authors built and annotated, where two
fluent-English annotators labelled questions along the three quality dimensions
[c1ee9053c]. Table 1 reports the **agreement with human annotators in pairwise comparisons
of faithfulness, answer relevance, and context relevance, using the WikiEval dataset
(accuracy)** [c1ee9053c]. The reported agreement (accuracy) for RAGAS is **0.95 for
faithfulness, 0.78 for answer relevance, and 0.70 for context relevance**, versus a
GPTScore baseline at **0.72 / 0.52 / 0.63** on the same three dimensions [c1ee9053c]. So
RAGAS's faithfulness metric agrees with human judgement far more often than its
context-relevance metric, and beats the GPTScore baseline on all three [c1ee9053c]. (The
paper spells the dataset both "WikiEval" and, in the Table 1 caption, "WikEval"; the
agreement figures are read directly from the converted Table 1 [c1ee9053c].)

## ARES — three dimensions via synthetic data → fine-tuned judges → PPI

ARES scores RAG systems on **three dimensions parallel to RAGAS — context relevance,
answer faithfulness, and answer relevance** — but with a fundamentally different mechanism
[ccb6561db]. It "proceeds in three stages" and requires only three inputs: an in-domain
passage set, a human preference validation set of "approximately 150 annotated data points
(or more)", and a few-shot set of in-domain query/answer examples [ccb6561db].

1. **Synthetic data generation.** ARES generates **synthetic query–passage–answer triples**
   from the target corpus to create both positive and contrastive/negative training data.
   The synthetic passages and contrastive negatives are "created using FLAN-T5-XXL"; for
   context-relevance negatives it samples in-domain passages unrelated to the synthetic
   query (using BM25 to retrieve the top-10 similar passages for strong negatives), and for
   answer-faithfulness/answer-relevance negatives it prompts FLAN-T5-XXL to generate
   contradictory or off-topic answers [ccb6561db].
2. **Fine-tune lightweight judges.** ARES fine-tunes its **synthetic dataset to fine-tune
   DeBERTa-v3** judges — "for each metric, a separate LLM with a binary classifier head is
   fine-tuned to classify positive and [negative]" triples, so there is one lightweight
   judge per dimension [ccb6561db]. These judges are "lightweight models fine-tuned" so they
   are deployable on commercial GPUs without calling external APIs, in contrast to few-shot
   GPT judges [ccb6561db].
3. **Debias and bound with PPI.** ARES applies the judges to a sample of any RAG system's
   in-domain triples, then uses **prediction-powered inference (PPI)** with the small
   human-annotated preference validation set to produce **confidence intervals** on the
   system scores. PPI "uses the LLM judges on the human preference validation set to learn a
   rectifier function"; the rectifier "allows us to estimate the errors of the LLM judge and
   generate confidence bounds for the success and failure rates of the RAG system" across
   the three criteria [ccb6561db]. ARES cites **Angelopoulos, Bates, Fannjiang, Jordan &
   Zrnic (2023)** for PPI [ccb6561db].

**Why the PPI human-label set matters.** Without it, ARES would only be reporting the
average of its judges' predictions, which inherit the judges' own errors. PPI's small
human-annotated set is what converts those raw judge predictions into statistically
debiased point estimates with confidence intervals, so ARES's scores are reliable rather
than just judge-prediction averages [ccb6561db]. The paper's Table 3 shows ARES efficacy
(Kendall's τ) rising with the PPI labelled count — from low/unstable τ at 25–50 labels to
substantially higher τ at 150–400 labels — empirically confirming that the human-label
budget governs reliability [ccb6561db].

## ARES validation, and the RAGAS-vs-ARES contrast

ARES validates by how accurately it *ranks* RAG systems against the correct human ranking,
measured with **Kendall's τ = ((# concordant pairs) − (# discordant pairs)) / (# total
pairs)** [ccb6561db]. On mock RAG systems across KILT and SuperGLUE, "ARES provides a more
accurate ranking of RAG systems than RAGAS", averaging a Kendall's τ **0.065 higher for
context relevance and 0.132 higher for answer relevance than RAGAS** [ccb6561db]. On
real-world RAG systems (Table 5), ARES averages a Kendall's τ of **0.91 for context
relevance and 0.97 for answer relevance**, **0.16 higher for context relevance and 0.15
higher for answer relevance than RAGAS** [ccb6561db].

The two harnesses sit at different points on a reliability/cost trade-off:

- **RAGAS** is **reference-free and prompt-only** — it needs no training and no human-label
  set, computing each metric by prompting a general LLM (statement decomposition + verdict
  for faithfulness; question generation + cosine for AR; sentence extraction for CR)
  [c1ee9053c]. Its validation is *agreement accuracy* with human pairwise comparisons on
  WikiEval; it reports a point score with no built-in error bar [c1ee9053c]. This makes it
  cheap and immediately deployable, but the score's reliability is exactly the (unbounded)
  reliability of the prompting judge.
- **ARES** trades that simplicity for **statistical guarantees**: it requires synthetic
  training data and a ~150+ human-annotated validation set, fine-tunes per-dimension
  DeBERTa-v3 judges, and uses PPI to emit **confidence intervals** on system scores
  [ccb6561db]. Its validation is *ranking accuracy* (Kendall's τ) against human rankings,
  and on that axis it outranks RAGAS [ccb6561db]. The cost is the human-label budget and a
  training step; the payoff is debiased estimates with bounds rather than a bare
  judge-average.

In short: RAGAS answers "what is each metric's value, by prompting" with reference-free
LLM-prompting formulas; ARES answers "how do these systems rank, with statistical
confidence" by debiasing fine-tuned-judge predictions through PPI. They are complementary
expressions of the same three-dimension decomposition (context relevance / faithfulness /
answer relevance) that `d6fad1a98` identified as the decomposed-RAG-harness regime.

## Gaps found

- **TruLens primary not grounded.** `d6fad1a98` names TruLens's "RAG Triad" (context
  relevance, groundedness, answer relevance) alongside RAGAS/ARES, but no TruLens primary
  source was read here; its groundedness/relevance definitions remain blog-attributed.
- **FActScore / RARR primaries not grounded.** The atomic-fact-precision (FActScore) and
  retrieve-and-revise (RARR) families referenced around `dfa42bc8a` are not grounded on
  their own papers in this finding.
- **RAGAS Eq. (1) and F formula are lossy in conversion.** The `1/n` factor and summation
  in AR Eq. (1), and the `|S|` denominator of `F = |V|/|S|`, are mangled by the PDF→markdown
  conversion; the canonical forms are reported from the surrounding text rather than read
  cleanly glyph-by-glyph. A clean re-extraction from the original PDF would remove residual
  doubt.
- **ARES per-dimension absolute accuracy numbers** (e.g. the Table 5 per-dataset RAGAS vs.
  ARES accuracy percentages, and the GPT-4-labels-vs-human-labels degradation in Table 4)
  are present but only partially recovered from the converted tables; the headline Kendall's
  τ deltas reported above are the cleanly-readable figures.
