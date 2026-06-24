---
id: d6c359091
topic: 09-knowledge-compilation-graphs
title: "KG2RAG: knowledge-graph-guided chunk expansion algorithm and HotpotQA result magnitudes"
status: draft
---

This finding grounds the chunk-expansion algorithm and the HotpotQA result
magnitudes of KG2RAG (Knowledge Graph-Guided Retrieval Augmented Generation),
the NAACL 2025 primary paper, stage by stage and number by number from the full
PDF [c340e0b25]. It complements finding d37b490ee, which cites only the
abstract-level KG2RAG corpus entry (a separate id) and explicitly notes that the
HotpotQA result magnitudes and the chunk-expansion algorithm detail were absent
from that entry; this finding supplies exactly that detail and does not restate
d37b490ee's high-level "expand-and-organize" point.

## The algorithm, stage by stage

KG2RAG has three phases following document offline processing: KG-enhanced chunk
retrieval (a semantic-based retrieval plus graph-guided expansion) and KG-based
context organization [c340e0b25].

**(1) Offline KG construction over chunks.** Documents are first split into `n`
chunks `D = {c_1, ..., c_n}` based on sentence and paragraph structure under a
predefined chunk size [c340e0b25]. Each chunk is then associated with a KG by
extracting entities and relations from it; the paper adopts the
extract-from-chunk approach (rather than relying on a pre-existing KG) by
prompting an LLM, and in the HotpotQA experiments it uses Llama-3 to extract
entities and relations from the 66,581 Wikipedia documents [c340e0b25]. The
resulting association is the set of triplet-chunk tuples
`G = {(h, r, t, c) | c ∈ D}` (Eq. 1), where `h`, `r`, `t` are head entity,
relation, and tail entity, and `c` is the chunk that derives the triplet
[c340e0b25]. This association is query-independent: it is built once for all
documents, can be performed offline, and supports incremental updates as new
documents are added [c340e0b25].

**(2) Semantic-based retrieval → seed chunks.** The semantic-based retrieval
prepares several *seed chunks* using embedding and ranking techniques; these
seed chunks are the chunks `D_q` most relevant to the query and are the input to
expansion [c340e0b25]. Relying on semantic-based retrieval alone, the paper
argues, returns isolated chunks that miss crucial factual knowledge and the
intrinsic connections among chunks [c340e0b25].

**(3) KG-guided chunk expansion.** The seed chunks are used to extract a
relevant subgraph `G_q ⊆ G` from the association KG (Eq. 3) [c340e0b25].
KG2RAG then traverses the **m-hop neighborhood** of `G_q` to produce an
expanded subgraph `G^m`, which pulls in chunks containing overlapped or related
entities and triplets — chunks the semantic retriever missed — without
requiring those expanded chunks to have high semantic similarity to the query or
to be physically located near the retrieved chunks [c340e0b25]. `m` is the
expansion hyperparameter that trades retrieval precision against recall; the
paper sets **m = 1** in its main experiments [c340e0b25].

**(4) KG-based context organization.** This post-processing stage both filters
and arranges the expanded chunk set [c340e0b25]. Because redundant knowledge can
create multiple edges between the same pair of nodes, KG2RAG generates the
**maximum spanning tree (MST) of each connected component** for filtering —
`T_i = MST(B_i)` (Eq. 7) — retaining only the most relevant information in the
subgraph [c340e0b25]. It then computes relevance scores between the MSTs and the
user query from their triplet representations using a cross-encoder reranking
function — `R(q, T_i) = C(q, conc(T_i))` (Eq. 8) [c340e0b25]. The KG additionally
acts as a *skeleton* to arrange the retained chunks into internally coherent
paragraphs; these semantically coherent, well-organized chunks are fed to the
LLM with the user query for response generation [c340e0b25].

## HotpotQA result magnitudes

The paper evaluates on HotpotQA (and shuffled variants) in both a distractor and
a fullwiki setting, reporting response quality and retrieval quality separately
(F1 / Precision / Recall) [c340e0b25]. Numbers below are read directly from the
results tables; the markitdown conversion interleaved figure/table cells, so each
value was confirmed against the source bytes.

**Response quality (Table 1, F1 / Precision / Recall).** On HotpotQA-distractor,
KG2RAG scores F1 0.663, precision 0.690, recall 0.683 [c340e0b25]. The strongest
baselines there are HybridRAG (F1 0.653) and SemanticRAG+Rerank (F1 0.652), so
KG2RAG's distractor-setting F1 gain over the best baseline is about +0.010
[c340e0b25]. On HotpotQA-fullwiki, KG2RAG scores F1 0.631 / precision 0.665 /
recall 0.643 versus SemanticRAG+Rerank at F1 0.587 — a larger gain of about
+0.044 F1 [c340e0b25]. Baseline F1 values on Hotpot-distractor for reference:
LLM-only 0.237, SemanticRAG 0.617, SemanticRAG+Rerank 0.652, HybridRAG 0.653,
LightRAG 0.293, GraphRAG 0.400 [c340e0b25].

**Retrieval quality (Table 2, F1 / Precision / Recall of retrieved chunks).** On
HotpotQA-distractor, KG2RAG retrieval F1 is 0.436, precision 0.301, recall 0.908
[c340e0b25]. The strongest baseline retrieval F1 is SemanticRAG+Rerank at 0.357
(precision 0.224, recall 0.932), so KG2RAG's retrieval-F1 gain is about +0.079
and its precision gain about +0.077, while recall stays comparable to the
high-recall rerank baseline [c340e0b25]. In the more challenging fullwiki setup,
the paper states KG2RAG achieves at least an 8% improvement over baselines,
attributing it to KG-guided retrieval surpassing semantic- and keyword-based
methods [c340e0b25].

**Ablations confirm the two stages (Tables 3 and 4).** On HotpotQA-distractor,
full KG2RAG reaches response F1 0.663 with retrieval F1 0.436 / precision 0.301 /
recall 0.908 at an average of 8.11 retrieved chunks [c340e0b25]. Removing context
organization ("w/o organization") drops retrieval precision to 0.153 and retrieval
F1 to 0.259 while ballooning the average to 16.76 chunks — i.e. organization is
what trims redundant chunks and lifts precision [c340e0b25]. Removing expansion
("w/o expansion") drops response F1 to 0.626 and recall to 0.842 at only 4.41
chunks — i.e. expansion is what recovers missed evidence and raises recall
[c340e0b25]. Varying `m` (Table 5) shows m=1 already balances the
precision/recall trade-off, with m=3 giving response F1 0.658 and recall 0.924
[c340e0b25].

## Synthesis

KG-guided chunk expansion matters for a source-of-truth corpus engine because it
recovers evidence that lexical and semantic similarity alone miss: KG2RAG's
expansion step deliberately admits chunks that are *not* semantically close to
the query and *not* physically adjacent, pulling them in solely because they
share entities or triplets along the graph, across documents [c340e0b25]. The
ablation isolates the mechanism — removing expansion costs recall (0.908 → 0.842)
while removing organization costs precision (0.301 → 0.153) — so the graph
structure is doing the evidence-recovery work, not the retriever [c340e0b25].
This is the same mechanism the engine's own finding → source → concept graph
supports: following typed edges to reach evidence a similarity search would
leave isolated, then trimming the expanded set (KG2RAG's MST-plus-rerank filter)
so only query-relevant, non-redundant context survives [c340e0b25].

## Residual gaps

- The source does not give a closed-form retrieval *latency* or *cost* per query
  for the expansion/organization stages; only average retrieved-chunk counts are
  reported [c340e0b25].
- The "at least 8%" fullwiki figure is stated as a floor in prose rather than a
  single tabulated metric, so the exact per-metric fullwiki retrieval deltas
  beyond the Table 2 values are not itemized here [c340e0b25].
- The cross-encoder reranking model and embedding model specifics beyond the
  Llama-3 extractor and the cross-encoder reranking function are not fully
  enumerated in the grounded sections [c340e0b25].
