# Faithfulness measurement machinery: structured LLM-judging, NLI entailment, and the faithfulness-vs-correctness evidence split

status: draft
topic: 08-grounding-truth

The promoted topic-08 finding establishes *that* faithfulness is an
atomic-statement metric scored by validated multi-judge ensembles. It does not
open the box on *how* the metric is actually computed, why an LLM judge can be
trusted to automate it at all, or what distinguishes faithfulness from adjacent
metrics that look similar but anchor on different evidence. This finding supplies
that mechanical layer — drawn primarily from RAGAS's own documentation — because
the engine's review gate is itself a faithfulness check, and an under-specified
gate inherits every confound the metric carries.

## Provenance note

Load-bearing definitional claims here rest on the **official RAGAS documentation**
(`docs.ragas.io`) [c7baa2195] [c2a47e89f] and a dated engineering write-up of
RAGAS implementation mechanics (saulius.io, Dec 15 2025) [c86a2d307]. The two
remaining sources are secondary explainers (a personal engineering blog
[cb1e98570] and an educational blog [c3251a95a]); their broad framing claims are
attributed in-line as "X describes…", and the one quantified blog figure is
flagged as non-reproducible rather than used as a thesis pillar.

## Key claims (cited)

- RAGAS's official definition: Faithfulness "measures how factually consistent a
  `response` is with the `retrieved context`," ranges from 0 to 1, and a response
  is faithful only if **all** its claims can be supported by the retrieved
  context [c7baa2195]. The score is computed in three steps — (1) identify all
  claims in the response, (2) check whether each claim can be inferred from the
  retrieved context, (3) compute `supported claims / total claims` [c7baa2195].
  This is the per-statement grounding ratio the existing finding asserts, now
  anchored to the primary doc rather than a secondary explainer.

- Faithfulness is **reference-free**: it asks "is this answer internally
  consistent with the context provided?" and therefore needs no gold answer,
  which is precisely why frameworks like RAGAS and LLM-as-judge can run on live
  traffic — at the cost of depending on a judge model that introduces its own
  variability and bias, as the letsdatascience explainer puts it [c3251a95a].

- The reliability trick that makes LLM-as-judge automatable is **structured
  judging, not free-form text**: the saulius write-up describes RAGAS as guiding
  the model into emitting a constrained JSON object (instruction + JSON schema +
  few-shot examples + machine-readable input payload), with structured-output
  parsing and retries, rather than an essay [c86a2d307]. The numeric score is an
  aggregation over those structured judgments, never parsed out of prose
  [c86a2d307].

- Faithfulness and factual correctness are **different metrics with different
  evidence anchors**, a distinction easy to conflate: faithfulness asks "is this
  answer supported by the retrieved context?" while factual correctness asks "is
  this answer correct vs a reference / ground truth?" — both use an LLM judge,
  but they grade against different evidence [c86a2d307]. A pipeline that retrieves
  wrong-but-internally-consistent context can therefore score high on
  faithfulness and low on correctness simultaneously.

- The substrate underneath modern faithfulness scoring is **natural-language
  inference (entailment)**: the au1206 explainer states that NLI-based approaches
  (checking whether claim B is entailed by premise A) underpin most modern
  faithfulness metrics, and decomposes the metric as claim extraction →
  per-claim entailment checking → `supported_claims / total_claims` [cb1e98570].
  Consistent with this, RAGAS ships a faithfulness variant computed with the
  HHEM-2.1-Open NLI model as an alternative to a general LLM judge [c7baa2195].

- Faithfulness is one metric in a **family**, not the whole grounding signal:
  RAGAS's metrics index lists Context Precision, Context Recall, Context Entities
  Recall, Noise Sensitivity, Response Relevancy, and Faithfulness alongside
  general-purpose graders (Aspect Critic, Rubrics-Based Scoring) and traditional
  non-LLM string metrics [c2a47e89f]. Retrieval-quality and generation-grounding
  failures thus surface on different metrics, so a gate that watches only
  faithfulness is blind to retrieval defects.

- LLM judges carry a documented **bias catalog** that the score does not reveal
  on its own: the au1206 explainer lists verbosity bias (longer answers rated
  higher even when a shorter one is more accurate), position bias in pairwise A/B
  comparisons (the first option gets a bump; mitigate by swapping order and
  averaging), and format bias (markdown/headers/bullets score higher regardless
  of content) [cb1e98570]. The letsdatascience explainer additionally reports a
  2025 IJCNLP study analyzing position bias across 15 judge models and over
  150,000 evaluation instances, finding the bias is systematic rather than
  random — varying by task type and by the quality gap between compared solutions
  [c3251a95a].

- The operational guardrail both explainers converge on is **judge calibration
  before trust**: "eval scores from an LLM judge are only as reliable as your
  judge prompt — always validate your judge against a small set of human-labeled
  examples before trusting its scores at scale" [c3251a95a]. (The same source
  quantifies verbosity inflation at ~15%, but this is a single blog figure with
  no reproducible eval behind it and is recorded here only as an order-of-magnitude
  caution, not a relied-upon number [c3251a95a].)

## Convergent vs contested

- **Convergent:** Faithfulness is a 0–1 grounding ratio of supported-to-total
  atomic claims against the retrieved context [c7baa2195]; LLM-judge automation is
  made tractable by constraining the judge to structured (JSON-schema) output
  [c86a2d307]; entailment/NLI is the underlying decision primitive [cb1e98570];
  and a judge must be validated against human labels before its scores are trusted
  [c3251a95a].

- **Contested / open:** Whether an NLI-model faithfulness variant (HHEM-2.1-Open
  [c7baa2195]) or a general LLM judge is preferable is not resolved by these
  sources — RAGAS offers both without ranking them. The magnitude of judge biases
  is reported inconsistently (a blog ~15% verbosity figure [c3251a95a] vs. a
  task-dependent characterization of position bias [c3251a95a] [cb1e98570]),
  signalling the numbers are setting-specific, not universal constants.

## Implications for the system (Phase 2)

- The engine's own review gate should emit **structured judgments** (a constrained
  schema: per-claim supported/unsupported + rationale) rather than a free-text
  verdict, because that is what makes the faithfulness score reproducible and
  parseable [c86a2d307] — and it mirrors the per-statement grounding contract the
  pipeline already enforces.

- Track **faithfulness and a retrieval-side metric separately** (e.g. context
  precision/recall or noise sensitivity from the RAGAS family [c2a47e89f]) so a
  bad retrieval that produces internally-consistent-but-wrong context is not
  masked by a high faithfulness score; reinforce with the faithfulness-vs-
  correctness evidence split [c86a2d307].

- Before trusting the gate's scores, **calibrate the judge against a held-out
  human-labeled set** [c3251a95a], and neutralize the known biases structurally —
  swap positions and average on any pairwise comparison, and do not reward longer
  or more heavily-formatted drafts [cb1e98570].

- Consider an **NLI/entailment check** (the HHEM-style variant [c7baa2195],
  [cb1e98570]) as a cheaper deterministic pre-filter ahead of the full LLM judge
  for high-volume per-claim grounding.

## Gaps found → re-scan

- **RARR and FActScore are named in the source-set slug but not substantively
  covered** by any of these five files (they are RAGAS-centric). The
  attribution-editing method RARR and the atomic-fact precision metric FActScore
  remain unsourced here. Re-scan primary sources: "RARR retrofit attribution
  research revision arXiv" and "FActScore atomic facts precision long-form
  factuality arXiv".
- These sources describe judge biases qualitatively/with blog figures and cite,
  but do not summarize, the primary papers (RAGAS arXiv:2309.15217, "Judging the
  Judges" arXiv:2401.10020, ARES arXiv:2311.09476 per [cb1e98570]). Re-scan those
  primaries for reproducible bias magnitudes and the original metric definitions.
- No source here covers **claim-to-source span anchoring** (how a specific
  sentence is bound to a precise retrieved span), only claim-to-context inference.
  Re-scan: "citation span attribution claim-to-source anchoring".
