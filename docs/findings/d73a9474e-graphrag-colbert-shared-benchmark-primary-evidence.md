# GraphRAG and ColBERT vs hybrid retrieval: what shared-benchmark primary sources actually measure

status: draft
topic: 06-rag-retrieval

The promoted hybrid/contextual-RAG finding establishes that hybrid fusion and
reranking earn their place. This finding asks a narrower, evidence-bound
question its predecessor could not answer cleanly: when you put true GraphRAG
(entity/community graph retrieval) and ColBERT late interaction on a *shared*
benchmark against hybrid BM25+dense, what do the peer-reviewed numbers actually
say — and where does the win stop? Every load-bearing number below comes from an
arXiv paper, not a vendor blog.

## Sub-questions

1. On a shared corpus, does true GraphRAG beat single-vector dense retrieval, and by how much?
2. Is the GraphRAG win uniform across query types, or task-dependent?
3. What does ColBERT late interaction actually buy versus a cross-encoder, per the primary source?
4. When does BM25 beat dense, and how much does neural reranking add on top of hybrid?

## Evidence — true GraphRAG vs dense on a shared enterprise benchmark

The strongest controlled comparison comes from a 2025 arXiv paper from SAP,
*Towards Practical GraphRAG: Efficient Knowledge Graph Construction and Hybrid
Retrieval at Scale* (arXiv:2507.03226v3), which evaluates GraphRAG against a
dense-vector baseline on one shared corpus: 550 enterprise PDF documents (ABAP
code-migration cookbooks and notes) preprocessed into ~2000 text chunks
[cd52d257c]. On the RAGAS evaluation of the CCM chat task (Table 1), GraphRAG
(GPT-4o) reaches Avg. 75.83% versus the Dense Vector (ada-002) baseline's 71.48%,
driven mostly by answer relevancy (89.43% vs 82.92%); notably the dense baseline
actually scores *higher* on faithfulness (77.18% vs 74.24%) [cd52d257c].

The win is far larger on the harder task. On the CCM code-proposal task judged by
an LLM-as-a-Judge (Table 3), GraphRAG (GPT-4o) wins 77% of head-to-head
comparisons against the dense baseline's 23%, with average scores of 4.04 vs 3.48
on a 1–5 scale [cd52d257c]. A semantic-alignment evaluation (Table 2) shows the
same direction: GraphRAG (GPT-4o) weighted-average 65.83% vs dense 50.80%, with
GraphRAG reaching Full Coverage on 58.99% of answers versus 42.88% for dense
[cd52d257c]. The paper's other headline is a cost result: a dependency-based
(classical-NLP) graph-construction variant retains 94% of the GPT-4o variant's
context-precision performance while removing the LLM from the construction step
[cd52d257c].

The takeaway is not "GraphRAG wins" but "GraphRAG's margin is task-dependent": a
modest, mixed edge on factual chat (and a faithfulness *loss* there), but a large
edge on multi-hop, synthesis-heavy code-proposal generation [cd52d257c].

## Evidence — when BM25 beats dense, and the reranking delta on hybrid

On a different shared benchmark — T2-RAGBench, 23,088 queries over 7,318
text-and-table financial documents, scored with Recall@k, MRR and nDCG plus
paired-bootstrap significance — a two-stage pipeline of hybrid retrieval with
neural reranking achieves Recall@5 = 0.816 and MRR@3 = 0.605, outperforming all
single-stage methods by a wide margin [ca7f1d531]. The same paper reports that
BM25 outperforms dense retrieval (text-embedding-3-large) on every metric except
Recall@20 on this financial corpus, directly challenging the assumption that
semantic search universally dominates lexical search; contextual retrieval gives
consistent gains while query expansion (HyDE, multi-query) helps little for
precise numerical queries, and all reported differences are significant at
p<0.001 [ca7f1d531].

A second arXiv source, the LiveRAG study (DataMorgana synthetic set over the
FineWeb-10BT corpus), found that hybrid retrieval merely *matched* sparse
retrieval on most metrics — the dense component being complementary rather than
additive — but that RankLLaMA neural reranking lifted MAP from 0.523 (hybrid) to
0.797, a 52% relative improvement [c578103a5]. That gain was computationally
expensive at ~84 seconds per question, which is why heavyweight rerankers belong
in offline/eval settings rather than online serving [c578103a5]. On the LiveRAG
Challenge's 500 unseen questions the same system placed 4th of 25 on faithfulness
but only 11th of 25 on correctness, consistent with a conservative,
retrieval-grounded strategy [c578103a5].

## Evidence — ColBERT late interaction vs cross-encoders, per the primary source

The ColBERT win over single-pass cross-encoders is architectural, and the primary
source states it directly. In *ColBERT: Efficient and Effective Passage Search via
Contextualized Late Interaction over BERT* (arXiv:2004.12832, Khattab & Zaharia),
the authors observe that LM-based ranking models "increase computational cost by
orders of magnitude over prior approaches" because they must feed each
query–document pair through a massive network to compute a single score; ColBERT's
late-interaction design instead encodes query and document independently and
applies a cheap MaxSim interaction, which lets document representations be
precomputed offline [cf44b434b]. This is the mechanism behind ColBERT's
cross-encoder-grade quality at bi-encoder-grade query latency — the cost moves
from query time to index storage rather than disappearing [cf44b434b].

One practitioner write-up reports that ColBERTv2 residual compression cuts
per-token storage by roughly 10x, bringing the index to a level comparable to a
sparse+dense hybrid index; this figure is not load-bearing here and is offered
only as color [c2fb735f5].

## Synthesis

Three shared-benchmark primary sources converge on a consistent picture. (1) The
default "dense beats sparse" intuition is wrong on lexically precise corpora: BM25
beat dense across nearly all metrics on T2-RAGBench financial text-and-table data
[ca7f1d531]. (2) Moving beyond hybrid pays off, but the *kind* of gain differs by
move: neural reranking buys a large quality lift at a large compute cost
(+52% MAP, ~84s/q [c578103a5]), while true GraphRAG buys a task-dependent gain —
modest and mixed on factual chat, large (77% vs 23% win rate) on multi-hop
synthesis [cd52d257c]. (3) ColBERT's value over cross-encoders is a
latency/storage trade, not a quality trade, by the original paper's own framing
[cf44b434b]. The practical rule: benchmark on your own corpus before assuming the
heavier strategy wins, because every one of these edges flips or shrinks under a
different task or document type.
