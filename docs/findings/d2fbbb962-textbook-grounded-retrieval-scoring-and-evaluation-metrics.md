# Textbook-grounded retrieval scoring and ranked-retrieval evaluation metrics

status: draft
topic: 15-textbooks-longform

A prior 15 finding was rejected because its load-bearing metric and term-weighting
formulas (tf-idf, precision/recall/F, MAP, nDCG) rested on blog summaries while the
genuine Stanford IR-book and SLP3 entries were only table-of-contents and abstract
pages. This finding rebuilds the engine's retrieval-scoring and evaluation vocabulary
directly on the ingested chapter prose of the field's two canonical textbooks:
*Introduction to Information Retrieval* (Manning, Raghavan & Schütze; Cambridge
University Press, 2008), chapters 6 and 8, and *Speech and Language Processing* 3rd
ed. (Jurafsky & Martin), chapter 6. Every weighting, set-based, and ranked-retrieval
definition below is taken from the textbook chapter that defines it — no secondary
source is cited. That provenance is the whole point: these are the primary
definitions a downstream component can trust as bedrock.

## Sub-questions

1. **Method** — how do the textbooks define term weighting (tf, idf, tf-idf) and the
   vector-space view of a document?
2. **Method / evidence** — how do they define set-based evaluation (precision, recall,
   F-measure), and why is accuracy the wrong metric?
3. **Evidence** — how is evaluation extended to *ranked* retrieval (precision–recall
   curve, interpolated precision, MAP, precision@k, R-precision, nDCG)?
4. **Bridge / contradiction** — what does SLP3 ch.6 actually contribute, and what does
   the ingested file *not* contain despite its filename?
5. **Application** — what durable cautions do the textbooks state about these metrics?

## Method — term weighting and the vector-space view

The starting intuition is that a document mentioning a query term more often has more
to do with that query and should score higher; a free-text query is treated as a set
of words and the document score is the sum, over query terms, of per-term match
scores [c6031ef87]. The simplest term weight is *term frequency* tf_{t,d}, the number
of occurrences of term t in document d [c6031ef87]. Under this *bag of words model*
the exact ordering of terms is discarded and only the count of each term is retained,
so "Mary is quicker than John" and "John is quicker than Mary" have identical
representations [c6031ef87].

Raw tf has a critical flaw: it treats all terms as equally important, yet terms
appearing in almost every document (the textbook's example is "auto" across an
auto-industry collection) have little discriminating power [c3d6ca44f]. The fix is the
*document frequency* df_t — the number of documents containing t — preferred over
collection frequency because a document-level statistic better discriminates between
documents for scoring [c3d6ca44f]. The *inverse document frequency* of a term is then
defined (eq. 21) as **idf_t = log(N / df_t)**, where N is the total number of documents
in the collection; the idf of a rare term is high and that of a frequent term is low,
and the precise base of the logarithm does not affect ranking [c3d6ca44f].

Combining the two yields the composite *tf-idf* weight (eq. 22):
**tf-idf_{t,d} = tf_{t,d} × idf_t** [cdafe8773]. This weight is highest when t occurs
many times within a small number of documents, lower when t occurs fewer times or in
many documents, and lowest when t occurs in virtually all documents [cdafe8773]. At
this point each document is viewed as a *vector* with one component per dictionary
term, each component weighted by its tf-idf, and the overlap score of a document for a
query q is **Score(q,d) = Σ_{t∈q} tf-idf_{t,d}** [cdafe8773]. This is the vector-space
view of scoring, defined here from the IR-book itself rather than any summary.

## Method / evidence — set-based evaluation and why accuracy fails

For a system that returns an unranked *set* of documents, the two basic effectiveness
measures are precision and recall [c5c86be0c]. **Precision (P) is the fraction of
retrieved documents that are relevant** — #(relevant retrieved) / #(retrieved) =
P(relevant | retrieved) [c5c86be0c]. **Recall (R) is the fraction of relevant
documents that are retrieved** — #(relevant retrieved) / #(relevant) =
P(retrieved | relevant) [c5c86be0c]. Both follow from the relevant/retrieved
contingency table of true/false positives and negatives [c5c86be0c].

The textbook explicitly argues against the obvious alternative, *accuracy* =
(tp + tn) / (tp + fp + fn + tn): because the data is extremely skewed — normally over
99.9% of documents are nonrelevant — a system can maximize accuracy by deeming every
document nonrelevant, which is useless to a user who wants to see *some* documents and
tolerates some false positives [c5c86be0c]. This is precisely why precision and recall,
not accuracy, are the IR effectiveness measures.

Precision and recall trade off, so they are combined in the *F-measure*, the weighted
harmonic mean **F = 1 / (α·(1/P) + (1−α)·(1/R)) = ((β²+1)·P·R) / (β²·P + R)** where
β² = (1−α)/α [c5c86be0c]. The balanced default sets α = 1/2 (β = 1), giving the
familiar **F_{β=1} = 2PR / (P + R)** [c5c86be0c]. Values β < 1 weight precision more,
β > 1 weight recall more [c5c86be0c].

## Evidence — ranked-retrieval evaluation

For ranked results, precision and recall become functions of rank, traced out as the
*precision–recall curve*, which characteristically saw-tooths [c7101583a]. To smooth
it, the textbook defines *interpolated precision* at recall level r as
**p_interp(r) = max over r' ≥ r of p(r')** — the highest precision found at any recall
at or beyond r [c7101583a]. The traditional single-curve summary (used in the first 8
TREC Ad Hoc evaluations) is *11-point interpolated average precision*: interpolated
precision is measured at the 11 recall levels 0.0, 0.1, …, 1.0 and averaged across
information needs [c7101583a].

The dominant single-number measure is *Mean Average Precision*:
**MAP(Q) = (1/|Q|) · Σ_{j=1..|Q|} (1/m_j) · Σ_{k=1..m_j} Precision(R_{jk})** — the
arithmetic mean, over queries, of each query's average precision, where average
precision approximates the area under that query's uninterpolated precision–recall
curve [c7101583a]. MAP uses no fixed recall levels and no interpolation; when a
relevant document is never retrieved its precision contribution is taken as 0
[c7101583a].

Where users only care about the first results page — as in web search — the textbook
defines *Precision at k* ("Precision at 10", "Precision at 30"): precision over a fixed
low number of retrieved results, which needs no estimate of the size of the relevant
set but is the least stable common measure [c7101583a]. *R-precision* instead uses the
known set of |Rel| relevant documents and reports precision among the top |Rel|
returned, adjusting for how many documents are actually relevant [c7101583a]. The
textbook notes an exact identity: if there are |Rel| relevant documents and r of the
top |Rel| are relevant, then precision and recall at that cutoff are both r/|Rel|, so
R-precision equals the *break-even point* of the precision–recall curve (the point
where precision = recall) [c7101583a]. Like Precision at k, R-precision describes only
one point on the curve rather than summarizing the whole of it [c7101583a].

For graded rather than binary relevance, the textbook defines *Normalized Discounted
Cumulative Gain* (eq. 44):
**NDCG(Q, k) = (1/|Q|) · Σ_{j=1..|Q|} Z_{kj} · Σ_{m=1..k} (2^{R(j,m)} − 1) / log₂(1 + m)**,
where R(j,m) is the relevance score an assessor gave to the document at rank m for
query j and Z_{kj} is a per-query normalization making a perfect ranking's NDCG equal
to 1 [c7101583a]. NDCG is explicitly designed for non-binary notions of relevance and,
like Precision at k, is evaluated over the top results [c7101583a].

## Bridge / contradiction — what SLP3 ch.6 actually contains

The ingested file labelled "slp3-ch6-vector-semantics-and-embeddings" is, on its own
text, SLP3 (Jurafsky & Martin, draft of January 6, 2026) **chapter 6 "Neural
Networks"**, not a vector-semantics/embeddings chapter [cb0370497]. It defines the
neural unit's weighted sum as a *dot product* **z = w·x + b** (eq. 6.2) — the same
linear-combination primitive that, taken over term-weight vectors, underlies
vector-space document scoring — and discusses activation functions, the vanishing-
gradient problem, the XOR problem, and *representation learning* for embeddings (which
it cross-references to chapter 5 rather than defining in place) [cb0370497]. It does
**not** contain a cosine-similarity formula, a tf-idf definition, or a stand-alone
vector-semantics treatment; the vector-space view in this finding is therefore anchored
to the IR-book (Score and document-as-vector) [cdafe8773], and SLP3 ch.6 is cited only
for the dot-product scoring primitive and for representation learning as the modern,
neural continuation of the same vectorize-then-score idea [cb0370497]. Flagging this
filename↔content mismatch is itself a provenance result for the corpus.

## Application — durable cautions the textbooks state

- **MAP varies widely across queries.** MAP scores normally range roughly 0.1–0.7
  across information needs within a single system, and there is more agreement on MAP
  for one information need across systems than across information needs for one system;
  the test set must therefore be large and diverse to be representative [c7101583a].
- **R-precision ≡ break-even point.** Treat R-precision and the precision–recall
  break-even point as the same single-point measure; both describe one point on the
  curve, not effectiveness across it, so prefer MAP or a max-F-measure point when a
  whole-curve summary is wanted [c7101583a].
- **Precision at k is unstable.** It is the least stable common measure and may not be
  germane beyond first-page applications, but it avoids needing the relevant-set size
  [c7101583a].
- **Use nDCG for graded relevance.** When relevance is non-binary, nDCG (normalized by
  the ideal ranking) is the metric the textbook designates [c7101583a].
- **Accuracy is unsuitable for IR.** Because of class skew, never grade a retrieval set
  by classification accuracy; use precision/recall/F [c5c86be0c].

## Provenance note

All definitions above trace to canonical textbooks — Manning, Raghavan & Schütze
(IR-book chs. 6 & 8) for tf/idf/tf-idf, precision/recall/F, accuracy critique, the
precision–recall curve, interpolated precision, MAP, Precision at k, R-precision and
nDCG; Jurafsky & Martin (SLP3 ch. 6) for the dot-product scoring primitive and
representation learning — and to no secondary blog. The equation numbers (21, 22, 36,
37, F-measure, p_interp, MAP, eq. 44/NDCG, 6.2) are the textbooks' own.

## Gaps found → re-scan

- The cosine-similarity normalization of the vector-space score (Score divided by the
  product of vector norms) is *not* present in any of the six ingested files — the
  IR-book tf-idf page stops at the unnormalized overlap Score, and SLP3 ch.6 is the
  neural-networks chapter — so cosine remains ungrounded in this corpus.
- A genuine SLP3 *vector-semantics & embeddings* chapter (defining tf-idf in NLP,
  PPMI, and cosine) was expected from the filename but not delivered; the correct
  chapter still needs ingesting.
- The IR-book's formal justification of the idf form (the "optimal weight g" /
  page-reference the chapter defers to) is referenced but not included in these files.
