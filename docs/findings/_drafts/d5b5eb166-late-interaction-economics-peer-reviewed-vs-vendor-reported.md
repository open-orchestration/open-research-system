# Late-interaction economics: what peer-reviewed ColBERT evidence settles and what stays vendor-reported

status: draft
topic: 06-rag-retrieval

The two prior 06 findings establish *that* hybrid fusion plus a reranker earns its
place, and that on shared benchmarks GraphRAG's edge over dense is task-dependent
while ColBERT trades index size for sub-linear rerank cost. The repo's open question
is narrower and provenance-sensitive: a *controlled* ColBERT-vs-cross-encoder
comparison was still ungathered, because the concrete latency/$/NDCG numbers in the
corpus had come from marketing blogs — and a finding was rejected over exactly that.
This finding asks what the **peer-reviewed** late-interaction literature can settle
on its own, and draws a hard line around what remains only vendor- or
practitioner-reported. The discipline here is the point: the architectural and
storage tradeoff is anchored to arXiv papers; the per-query dollar-and-millisecond
economics are presented as attributed, non-load-bearing practitioner figures.

## Sub-questions

1. **Method** — what does a like-for-like ColBERT-vs-cross-encoder comparison actually
   hold constant, and what does each architecture cost asymptotically?
2. **Evidence (defensible)** — what recall/effectiveness/storage numbers come from the
   primary ColBERT papers, and under what conditions?
3. **Tension** — which numbers are still only practitioner/vendor-reported, and is the
   GraphRAG-vs-hybrid comparison yet apples-to-apples?
4. **Application** — what should an open engine default to, given only the verifiable
   evidence?

## Method — what the comparison holds constant

A cross-encoder concatenates the query and each candidate document into one transformer
forward pass and emits a relevance score, attending across both texts jointly; this is
why it is more accurate per pair and slower per pair [cf35fa065]. ColBERT
(Contextualized Late Interaction over BERT) instead encodes query and document
*independently* into bags of per-token embeddings, then scores with a MaxSim-and-sum
operator — for each query token, the max cosine similarity over document tokens, summed
[c9d345293]. The load-bearing structural difference is *where* the work happens: because
documents are encoded offline and only MaxSim runs at query time, ColBERT's online
scoring is O(n_q·n_d·m) dot-products per candidate, whereas a cross-encoder pays full
cross-attention O((|q|+|d|)²·H) and a full encode *per query-document pair*
[c9d345293]. That asymptotic gap — precomputed document representations versus
re-encoding every pair — is the invariant any fair head-to-head must respect, and it is
established from the primary papers, not a vendor benchmark [c9d345293].

## Evidence — the defensible, peer-reviewed numbers

From the ColBERT topic synthesis, which anchors each claim to its arXiv source:

- **Effectiveness/recall.** ColBERT achieves effectiveness competitive with BERT-based
  cross-encoders while keeping low query-time cost; the original work reports ~96%
  recall@1k with 50–100 ms reranking and <500 ms end-to-end retrieval, and a substantial
  FLOPs reduction versus cross-encoder methods (Khattab et al., 2020) [c9d345293]. This
  is the closest thing in the gathered corpus to a controlled "late interaction reaches
  cross-encoder quality at lower query-time compute" claim with a primary anchor.
- **Storage is the real cost.** Per-token embeddings make the index large: ColBERTv2
  introduces residual vector quantization that compresses token embeddings from 256
  bytes to 20–36 bytes — a 6–10x storage reduction — while preserving late-interaction
  quality (MRR@10 = 39.7% in-domain) via cross-encoder-distilled supervision (Santhanam
  et al., 2021) [c9d345293]. ColBERTer's Bag-of-Whole-Words reduction stores ~2.5x fewer
  vectors, approaching plaintext-size parity (Hofstätter et al., 2022) [c9d345293]. For
  an 8–10M-document collection at m=128 and 2 bytes/dim, the index is in the tens of GiB
  [c9d345293].
- **The tradeoff is tunable, not fixed.** Later variants trade effectiveness against
  storage/speed at inference by varying embedding dimensionality (e.g. d=64 vs d=128),
  and a simple 2-layer projection head adds +0.0201 nDCG@10 over the linear baseline
  across benchmarks without changing the index structure (Clavié et al., 2025; Jha et
  al., 2024) [c9d345293].

Taken together these settle the architectural half of the open question: late
interaction buys cross-encoder-class quality at sub-cross-encoder query compute, and the
price is a multi-vector index whose size is compressible by ~6–10x but never down to a
single-vector footprint [c9d345293].

## Tension — what is still only vendor/practitioner-reported

The *per-query dollar-and-millisecond* economics — the exact figures a prior finding was
rejected for resting on — remain practitioner- or vendor-reported, and this finding does
not lean on them as fact:

- A practitioner guide reports cross-encoders reaching "state-of-the-art" MS MARCO
  MRR@10 > 40 but adding "at least a few hundred milliseconds per query if unoptimized,"
  and storing ColBERT embeddings for a million documents adding "20GB+" to the footprint
  unless quantized — useful directionally, but these are blog estimates, not a controlled
  bench [cf35fa065]. A second practitioner table puts naive RAG at $0.001–0.01/query and
  GraphRAG at $0.02–0.15/query, and credits hybrid retrieval + reranking with a "25–40%
  precision improvement," again as practitioner figures rather than a registered
  benchmark [c3b9d1ab1]. Presented as attributed: *the controlled evidence shows late
  interaction matches cross-encoder quality at lower query-time FLOPs [c9d345293]; the
  per-query latency and cost deltas are only practitioner-reported and should not be
  treated as measured* [cf35fa065][c3b9d1ab1].

- **GraphRAG is still not on a tuned-hybrid shared benchmark.** The vendor and
  applied-blog sources are explicit that they are *not* reporting controlled GraphRAG-
  vs-hybrid numbers: one frames its decision matrix qualitatively and concedes that for
  unstructured corpora "BM25 + dense + reranker often beats graph-augmented retrieval on
  cost-per-quality," with the graph leg paying off only on entity-dense, multi-hop, or
  global-summarisation workloads [cc958dce4]. Its only hard figures are *cost*, not
  quality — indexing a 10M-token corpus at ~$1,000–$5,000 in LLM tokens, droppable 4–8x
  with a cheaper extractor — and these are 2026 blog prices, not a benchmark
  [cc958dce4]. The NetApp applied post likewise offers no GraphRAG-vs-hybrid eval of its
  own; its single quantitative anchor is a *cited* NVIDIA result of 96% factual
  faithfulness on financial-filings answers using a Graph+Vector architecture, which is
  an attribution to an external paper, not a controlled comparison the post ran
  [c4b99f896]. So the synthesis's "GraphRAG baselined only vs dense, not tuned hybrid"
  gap stays open on the gathered evidence [cc958dce4][c4b99f896].

- One practitioner source does claim a three-way hybrid (Dense + BM25 + SPLADE) with a
  ColBERT reranker "achieves the highest accuracy in Blended RAG benchmarks," and quotes
  hybrid recall rising from 0.72 (BM25 alone) to 0.91 — but it cites these as benchmark
  summaries without the controlled conditions, so they corroborate direction rather than
  settle the head-to-head [c3b9d1ab1].

## Application — what an open engine should default to

Given only the verifiable evidence: keep hybrid BM25+dense + a cross-encoder reranker as
the low-regret default, because it needs no second index and the reranker is a small
fraction of a generation-dominated latency budget [cf35fa065]. Reach for ColBERT late
interaction specifically when the workload needs wide candidate sets (k in the hundreds
to a thousand) where a cross-encoder's per-pair cost scales badly — long-tail recall over
legal, regulatory, or scientific corpora — and budget for a multi-vector index sized in
the tens of GiB per ~10M docs, compressible ~6–10x with ColBERTv2 quantization but not to
single-vector size [c9d345293]. Treat the layered pipeline (BM25/dense → ColBERT shortlist
→ cross-encoder or LLM final pass) as the way to bound cost while keeping quality, since
each stage narrows the candidate set the next, more expensive stage must score
[cf35fa065]. Do not provision against the per-query $/latency figures as if measured; the
defensible number is the architectural one — late interaction reaches cross-encoder-class
recall at lower query-time compute, paid for in index storage [c9d345293].
