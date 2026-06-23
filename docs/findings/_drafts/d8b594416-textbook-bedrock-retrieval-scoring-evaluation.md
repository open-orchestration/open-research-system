---
id: d8b594416
topic: 15-textbooks-longform
title: "Textbook bedrock for retrieval scoring and evaluation: tf-idf, vector space, and ranked-retrieval metrics"
status: draft
---

# Textbook bedrock for retrieval scoring and evaluation: tf-idf, vector space, and ranked-retrieval metrics

## Why this finding

The engine's retrieval and evaluation layers already rest on a blog-and-paper
layer (RAG techniques, reranking, RAGAS-style faithfulness). Underneath that
layer sit a small set of definitions that are not novel and not in dispute:
how documents are scored against a query, and how a ranked result list is
measured. This finding anchors those definitions to their authoritative
textbook homes — the freely published *Introduction to Information Retrieval*
(Manning, Raghavan & Schütze; nlp.stanford.edu/IR-book) [c1fbccfab] and
*Speech and Language Processing* (Jurafsky & Martin; web.stanford.edu/~jurafsky/slp3)
[cee7c940c] — so that load-bearing concepts trace to the canonical reference
rather than to a third-party summary.

A provenance note governs everything below. The two Stanford-hosted IR-book
sources [c1fbccfab][ced7b1b52] and the IR-book abstract [cc3ea859c] are the
authoritative textbook's own pages, but they are companion-site / table-of-contents /
abstract pages: they establish which concepts the textbook canonically defines
and where, but they do not reproduce the prose formulas. The explicit metric
formulas in this finding therefore come from third-party summaries
[cc5061927][cd084662f][c6ed06790]; the textbook is cited for each concept's
canonical standing, and the summary for the formula's stated form. Where a
summary and the textbook's own framing diverge, the textbook framing wins.

## Method: ranked retrieval, tf-idf, and the vector space model

The IR-book devotes a dedicated chapter to *Scoring, term weighting and the
vector space model*, whose canonical sub-sections are *Term frequency and
weighting*, *Inverse document frequency*, *Tf-idf weighting*, and *The vector
space model for scoring* (with dot products, queries as vectors, and computing
vector scores) [c1fbccfab]. This places tf-idf weighting and the vector space
model as textbook-canonical primitives of ranked retrieval, not folklore.

The textbook treats document scoring as ranked rather than Boolean: a separate
chapter, *Computing scores in a complete search system*, covers efficient
top-K scoring and ranking — inexact top-K retrieval, index elimination,
champion lists, static quality scores, and impact ordering [c1fbccfab]. This is
the bedrock the engine's retrieval layer inherits: score documents against the
query, then return a ranked top-K, with practical shortcuts to avoid scoring
the whole collection.

For *semantic* (embedding-based) retrieval, the canonical reference is
*Speech and Language Processing* (Jurafsky & Martin), whose 3rd-edition draft is
freely published and whose vector-semantics/embeddings material is the textbook
home for representing word and document meaning as dense vectors [cee7c940c].
The official citation form for that book is "Daniel Jurafsky and James H.
Martin. 2026. *Speech and Language Processing*, 3rd edition. Online manuscript
released January 6, 2026" [cee7c940c]. Practitioner summaries frame the same
distinction the engine relies on: vector (semantic) search "transforms text
into numerical embeddings that capture semantic meaning and relationships" and
retrieves conceptually related results without keyword overlap, whereas
full-text (keyword) search matches exact phrases and is fast but lacks
contextual understanding [c6ed06790]. The summary's recommended default —
hybrid search combining vector and keyword retrieval — matches the engine's
existing hybrid-retrieval posture [c6ed06790].

## Evidence: the precise metric definitions and what each rewards

The IR-book's *Evaluation in information retrieval* chapter is the canonical
home for these metrics, with sub-sections for *Evaluation of unranked retrieval
sets*, *Evaluation of ranked retrieval results*, *Standard test collections*,
and *Assessing relevance* [c1fbccfab]. The textbook thus separates two evaluation
regimes — set-based (unranked) and rank-aware (ranked) — which is exactly the
split the metrics below fall into.

**Precision and recall (set-based).** Precision is the fraction of retrieved
documents that are relevant — |relevant ∩ retrieved| / |retrieved| — and recall
is the fraction of relevant documents that were retrieved — |relevant ∩
retrieved| / |relevant| [cc5061927]. Equivalently, precision = TP / (TP + FP)
[cd084662f]. Precision rewards avoiding irrelevant results; recall rewards
completeness of coverage. The two trade off against each other: improving one
often degrades the other [cc5061927]. The F1 score collapses both into one
number as their harmonic mean, 2·(P·R)/(P+R), useful when the relevant/irrelevant
split is uneven [cc5061927].

**Fall-out.** Fall-out is the proportion of non-relevant documents that were
retrieved out of all non-relevant documents — the probability a non-relevant
document is returned, FP / (FP + TN); lower is better [cc5061927]. It is the
complement of precision's concern, measuring noise against the irrelevant pool
rather than the retrieved pool.

**MAP (rank-aware, single-figure).** Mean Average Precision is a single-figure
measure of ranked-list quality across recall levels: compute the average
precision for each query, then take the mean over all queries, MAP = (1/Q)·
Σ AveragePrecision(q) [cc5061927]. MAP rewards a system that places relevant
documents early *and* maintains relevance as the user reads deeper, which is
why it is favored where users scroll past the first page [cd084662f].

**nDCG (rank-aware, graded relevance).** Normalized Discounted Cumulative Gain
evaluates the *positions* of relevant documents and gives extra weight to highly
relevant documents appearing early [cc5061927]. It is DCG / IDCG, where
DCG_k = Σ_{i=1..k} (2^{rel_i} − 1) / log₂(i + 1) and IDCG is the DCG of the
ideal ranking [cc5061927]. The two assumptions are explicit in that formula:
a *gain* function (2^{rel_i} − 1) that rewards graded relevance, and a *discount*
(1/log₂(i+1)) that penalizes relevant documents found lower in the list. nDCG
rewards ranking the most relevant results highest [c6ed06790].

## Tension: where these metrics mislead

The summaries are candid that these textbook metrics have failure modes the
engine's promotion gates must respect:

- **Binary-relevance assumption.** Precision and recall assume binary relevance
  and may not capture the nuance of user satisfaction; nDCG partly addresses
  this by using graded relevance and rank order [cc5061927]. A gate built only
  on precision/recall is blind to *how relevant* a result is.
- **Relevance-judgment subjectivity.** All these offline metrics depend on
  relevance judgments, which are subjective and vary between judges [cc5061927].
  The measured score is only as trustworthy as the judgment set behind it.
- **Precision/recall trade-off.** Because improving precision tends to lower
  recall and vice versa [cc5061927], a single-metric target can be gamed by
  trading the unmeasured axis away — the reason MAP and F1 exist as
  balance-aware summaries.
- **Evaluation skew from biased judgment data.** Bias in the underlying data can
  produce evaluation skew, where a system scores well overall but fails on
  underrepresented cases [cd084662f]. Aggregate metrics hide per-segment failure.

## Application: which engine layers this bedrock anchors

Two engine layers should rest on these definitions:

1. **Retrieval scoring.** The engine's hybrid retrieval — keyword plus
   embedding search — is the practical realization of the IR-book's vector
   space scoring [c1fbccfab] combined with SLP3-style embedding semantics
   [cee7c940c]. The top-K-then-rank structure, and the efficiency shortcuts for
   not scoring the whole collection, are the textbook's "complete search system"
   model [c1fbccfab].
2. **Evaluation / promotion metrics.** The engine's eval layer should treat
   set-based precision/recall and rank-aware MAP/nDCG as the textbook-canonical
   floor [c1fbccfab], while carrying the pitfalls forward: prefer graded over
   binary relevance where possible, treat judgment quality as a first-class
   variable, and watch the precision/recall trade-off and per-segment skew
   rather than a single aggregate [cc5061927][cd084662f]. These rank-aware
   metrics are the same family (Recall@k, MRR, nDCG, MAP) the engine's
   RAG-evaluation layer already reports, now grounded in their textbook source
   rather than only in benchmark papers.

## Provenance

- **[c1fbccfab]** — nlp.stanford.edu/IR-book companion site for *Introduction to
  Information Retrieval* (Manning, Raghavan & Schütze, Cambridge UP, 2008).
  Authoritative textbook (companion site / chapter index).
- **[ced7b1b52]** — nlp.stanford.edu/IR-book brief contents and chapter listing.
  Authoritative textbook (table of contents).
- **[cc3ea859c]** — IR-book abstract / authors page (informationretrieval.org /
  Cambridge). Authoritative textbook metadata.
- **[c6bd43b17]** — cambridge.org publisher catalog page for the IR-book.
  Authoritative (publisher metadata page; not chapter content).
- **[cee7c940c]** — web.stanford.edu/~jurafsky/slp3, *Speech and Language
  Processing* (3rd ed. draft, Jan 6 2026 release), Jurafsky & Martin.
  Authoritative textbook (release/contents page).
- **[cc5061927]** — geeksforgeeks.org, "Offline Evaluation Metrics in
  Information Retrieval." Blog/summary.
- **[cd084662f]** — dasroot.net, "Retrieval Evaluation Metrics You Should
  Actually Use." Blog/summary.
- **[c6ed06790]** — edge-ai-vision.com, "A Practical Guide to Recall, Precision,
  and NDCG." Blog/summary.
