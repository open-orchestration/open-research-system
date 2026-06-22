# Reranker and GraphRAG economics: latency, compute cost, and benchmark deltas quantified

status: draft
topic: 06-rag-retrieval

The promoted hybrid/contextual-RAG finding establishes *that* reranking and
hybrid fusion earn their place; it does not price them. This finding supplies the
missing quantitative layer: how much latency and compute a reranker actually
adds, where ColBERT and cross-encoders trade off, and what the head-to-head
benchmark numbers are for hybrid BM25+dense versus the heavier neural-reranking
and adaptive strategies.

## Method — what the reranker tiers actually are

A cross-encoder concatenates `[CLS] query [SEP] document [SEP]` and emits one
relevance score, so it cannot precompute document representations — every
(query, document) pair costs a full forward pass, making it O(n) at query time
and usable only over a small candidate set, never as a first-stage retriever
[c3bd3a176]. ColBERT's "late interaction" keeps a vector per token and computes
relevance as the sum over query tokens of the max similarity to any document
token (MaxSim), so document vectors are precomputed and indexed — yielding
cross-encoder-grade ranking at bi-encoder-grade latency at the cost of storage
[c67cbb7b0]. LLM-as-reranker feeds 20–50 candidates into one prompt and asks for
a ranked permutation, in listwise (RankGPT-style), pointwise, or pairwise-
tournament flavors [c67cbb7b0].

## Evidence — reranker latency and cost, quantified

On a 50K-chunk internal docs corpus, pure vector search at k=5 gives Recall@5
0.62 / Precision@5 0.62 at 40ms; widening to k=50 lifts Recall to 0.91 but
collapses Precision@5 to 0.18 at 55ms; adding a reranker over the k=50 set
restores Precision@5 to 0.81 while preserving Recall 0.91, at 180ms; and hybrid
k=100 + rerank-to-top-5 reaches Recall 0.96 / Precision@5 0.87 at 240ms
[c67cbb7b0]. On an 80K-chunk customer-support corpus, hybrid-only retrieval
scores NDCG@10 0.612 at 55ms and $0.00; self-hosted BGE-reranker-v2-m3 lifts
that to 0.794 (+29.7%) at 140ms and $0.18/1K (GPU amortized); Cohere Rerank 3.5
reaches 0.811 (+32.5%) at 220ms P50 and $2.00/1K; Voyage rerank-2.5 reaches
0.806 (+31.7%) at 240ms and $2.00/1K [c67cbb7b0].

Concrete per-model compute: `cross-encoder/ms-marco-MiniLM-L-4-v2` (22M params)
reranks 50 pairs in ~10ms on a single CPU core, MiniLM-L-12 (33M) in ~30ms, and
BGE-reranker-large (560M) in ~200ms; on an A10 GPU those drop to ~5ms and ~20ms
respectively [c3bd3a176]. BGE-reranker-v2-m3 (568M params) runs roughly 80ms per
batch of 50 query-doc pairs on a single A10G [c67cbb7b0]. In a 300ms-SLA design
serving 500 QPS, `cross-encoder/ms-marco-MiniLM-L-6-v2` reranks 30 candidate
pairs in ~3ms batched on an A10, needing only 1–2 reranking GPUs [c3bd3a176].
Cohere Rerank costs ~$1 per 1,000 requests while self-hosted cross-encoders are
free apart from GPU compute [c83cc0570]. A reference latency budget puts query
embedding at 20–50ms (API) / 5ms (local), ANN retrieval at 5–30ms, cross-encoder
reranking of 50 docs at 50–200ms (local) / 50–100ms (API), and LLM generation at
500–3000ms — so reranking is a 5–25% increase on a generation-dominated total
[c3bd3a176]. A separate cost-benefit tier table puts TinyBERT at +30ms/+10%
quality, MiniLM at +50ms/+20%, Cohere at +100ms/$1/+25%, and LLM reranking at
+500ms/$5–20/+30% [c83cc0570].

ColBERT's cost profile is sub-linear in candidate count because the heavy work is
precomputed: one source reports ColBERT reranking 500 candidates in the same
wall-clock time a cross-encoder reranks 50, where a cross-encoder pays 4x latency
going from 50 to 200 candidates [c67cbb7b0]. The penalty is storage — a raw
ColBERT index is 50–100x larger than a dense single-vector index (200–400GB for
1M chunks at 512 tokens average), which ColBERTv2 residual compression brings
down to roughly 5–10x [c67cbb7b0].

## Evidence — GraphRAG and heavier strategies vs hybrid BM25+dense

On the T2-RAGBench financial QA benchmark (23,088 queries over 7,318 text-and-
table documents, evaluated with Recall@k, MRR, and nDCG plus paired bootstrap
significance testing), a two-stage pipeline of hybrid retrieval with neural
reranking achieves Recall@5 0.816 and MRR@3 0.605, outperforming all single-
stage methods by a large margin [ca7f1d531]. The same benchmark reports that
BM25 outperforms state-of-the-art dense retrieval on these financial documents,
challenging the assumption that semantic search universally dominates, and that
query-expansion methods (HyDE, multi-query) and adaptive retrieval give limited
benefit for precise numerical queries while contextual retrieval yields
consistent gains [ca7f1d531]. Ablations show fusion-method choice (CC vs. RRF)
and reranker candidate depth significantly impact performance, with all reported
differences statistically significant at p<0.001 [ca7f1d531].

On a separately constructed synthetic DataMorgana set over the FineWeb-10BT
corpus, the LiveRAG system found that hybrid retrieval merely *matched* sparse
retrieval on most metrics — the dense component being complementary rather than
additive — but that RankLLaMA neural re-ranking lifted MAP from 0.523 (hybrid) to
0.797, a 52% relative improvement [c578103a5]. That re-ranking gain came at a
steep compute cost of ~84 seconds per question [c578103a5]. In the LiveRAG
Challenge on 500 unseen questions the same system placed 11th of 25 on
correctness but 4th of 25 on faithfulness, with a 17% refusal rate attributed to
conservative prompting [c578103a5].

## Tension — sources disagree on whether the second stage is decisive

The reranking-cost sources treat a cross-encoder reranker as a near-universal
+30% NDCG upgrade for ~100–200ms [c67cbb7b0][c83cc0570], and the financial
benchmark agrees that hybrid+reranking beats every single-stage method
[ca7f1d531]. But LiveRAG reports hybrid retrieval adding little over BM25 alone,
locating nearly all the lift in the re-ranker — and at ~84s/question that
re-ranker is not production-viable [c578103a5]. The two benchmarks also disagree
on the dense component: T2-RAGBench finds BM25 beating dense outright on
financial text [ca7f1d531], while LiveRAG finds dense merely non-additive on web
text [c578103a5] — both undercut the "dense semantic search dominates" prior, but
from different corpora.

## Application — how to price the second stage

For a generation-dominated pipeline, a self-hosted MiniLM or BGE cross-encoder is
the low-regret default: it adds 50–200ms (a 5–25% latency increase) for roughly
+20–30% NDCG and is free apart from GPU [c67cbb7b0][c83cc0570][c3bd3a176]. Choose
ColBERT specifically when candidate depth is high (k=200+) or latency budgets are
tight and storage is not the bottleneck, accepting a 5–10x larger index after
ColBERTv2 compression [c67cbb7b0]. Reserve LLM-listwise reranking (+500ms, $5–20+
per 1K, 30x the cost of Cohere) for low-QPS, reasoning-heavy queries as a third
stage on top of a cross-encoder, not a replacement [c67cbb7b0][c83cc0570]. Treat
heavyweight re-rankers like RankLLaMA as offline/eval tools, not online serving,
given the ~84s/question cost [c578103a5]. Finally, benchmark on your own corpus
before assuming dense beats sparse: on financial text-and-table data BM25 alone
beat dense retrieval [ca7f1d531].
