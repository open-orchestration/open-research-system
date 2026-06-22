# Hybrid retrieval and contextual RAG: architecture tradeoffs and what the evidence shows

status: draft
topic: 06-rag-retrieval

Retrieval exists because language models hallucinate when asked for information they
were not trained on or cannot recall from parameters [c86fc957c]. The design question is
not *whether* to retrieve but *how* — and the 2025 sources converge on a layered answer:
lexical and dense retrieval are complementary, "contextual retrieval" is an architecture
rather than a product, and reranking earns its place only on top of disciplined chunking.

## Method — what the competing retrieval architectures actually are

The base choice is sparse versus dense. Sparse (lexical) retrieval such as BM25/BM25+
matches terms directly, while dense retrieval uses neural embeddings computed from
transformer models [c86fc957c]. Dense retrieval is prone to "semantic drift" without
chunking discipline [c86fc957c]. The canonical RAG pipeline breaks the corpus into chunks
of usually no more than a few hundred tokens, embeds each chunk, and stores the vectors in
a database searched by semantic similarity at query time [cf60e5897]. Retrieval quality
improves when embeddings and BM25 are combined rather than used alone [cf60e5897].

Critically, "contextual retrieval" is a chunking-and-indexing spec, not a single tool: it
decomposes into context generation, embedding, a lexical index, fusion, and reranking, and
those stages should be separated before any library is chosen [c9742d19a]. ColBERT is one
reranking option — a reranker model used inside a RAG system [c1be385f0].

## Evidence — what evaluation shows

Empirical comparison is now systematic rather than anecdotal. One benchmark evaluates ten
retrieval methods on a text-and-table financial QA corpus, reporting retrieval metrics
(Recall@k, MRR, nDCG, MAP) alongside generation metrics, with paired bootstrap significance
testing and ablations isolating fusion strategies and reranker candidate depth [c46fda511].
That benchmark frames its guidance as empirical cost-accuracy analysis for practitioners
building RAG over heterogeneous documents [c46fda511]. On the effect size of the full stack,
Anthropic's own ablation reports that context plus contextual BM25 plus reranking reduces
top-20 retrieval failure by 67% [c9742d19a].

## Tension — is the reranker a fix or a crutch?

Vendors present reranking as a precision filter at the end of the pipeline that passes only
the most relevant documents downstream, reducing token use, minimizing latency, and boosting
accuracy [c7316bbcb]. The pipeline-engineering view pushes back: teams "keep bolting a
reranker onto broken chunking and calling it contextual retrieval," and a reranker cannot
repair upstream chunking and indexing failures [c9742d19a]. These are reconcilable — rerank
genuinely sharpens a sound pipeline [c7316bbcb], but only after the context-generation and
indexing stages are correct [c9742d19a].

## Application — how to build and choose

Decompose the pipeline first, then pick a single approach per layer: the Anthropic recipe
(Claude Haiku 4.5 prefixing every chunk with generated context) and voyage-context-3 (a
jointly-trained contextual encoder) solve the same context problem at different layers, so
pick one; add ColBERT only when queries demand token-level matching [c9742d19a]. Where
latency and token budget matter, a reranker narrows the candidate set before generation
[c7316bbcb]. Validate the result by measured retrieval failure rate at top-20 on your own
corpus rather than by impression, reproducing the ablation's gain rather than assuming it
[c9742d19a].
