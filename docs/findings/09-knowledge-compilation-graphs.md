# Findings — Knowledge Compilation & Graphs

**Question:** What does this category teach for building an AI research system?

## Key claims (cited)
- Flat vector RAG has two structural failures GraphRAG is built to fix: it cannot answer global questions ("what are the core themes across all reports?") because it only returns a few surface-similar chunks, and it breaks on multi-hop reasoning that requires chaining scattered fragments (e.g. "which seismic zone is the factory of Company A's supplier B located in?") — [GraphRAG: Knowledge Graph + RAG Next-Generation](https://www.meta-intelligence.tech/en/insight-graphrag)
- GraphRAG's indexing pipeline has four steps — text chunking (larger ~1200-token chunks to preserve cross-sentence relationships), LLM-based entity & relationship extraction, graph construction, and community detection + summary generation; chunks too small sever the relationships entity extraction depends on — [GraphRAG: Knowledge Graph + RAG Next-Generation](https://www.meta-intelligence.tech/en/insight-graphrag)
- Community detection uses the hierarchical Leiden algorithm (`hierarchical_leiden()` from graspologic) to produce a node-to-community mapping across hierarchy levels, where higher levels are broader communities — pre-computing this hierarchy is what makes global/thematic queries possible — [Community Detection | JayLZhou/GraphRAG | DeepWiki](https://deepwiki.com/JayLZhou/GraphRAG/7.2-community-detection)
- Two complementary query modes serve different question types: Local Query extracts entities and traverses 1–2 hop neighborhoods for precise facts; Global Query answers open-ended/thematic questions by map-reducing over pre-computed community summaries — [GraphRAG: Knowledge Graph + RAG Next-Generation](https://www.meta-intelligence.tech/en/insight-graphrag)
- The benefit comes at a cost: GraphRAG index construction is high (LLM extraction + community detection + summary generation) vs. low for vector embeddings, and Global query token consumption is high and proportional to the number of communities — but GraphRAG improves answer comprehensiveness by roughly +50–70% on global/thematic questions — [GraphRAG: Knowledge Graph + RAG Next-Generation](https://www.meta-intelligence.tech/en/insight-graphrag)
- The indexing pipeline is the most computationally expensive component; production builds should use incremental indexing (diff + graph merge, not full rebuild), tiered models (GPT-4o-mini for straightforward extraction, GPT-4o/Claude Opus reserved for complex summary synthesis), token-budget caps, parallel extraction via a queue (Celery/SQS), and human-in-the-loop review of critical nodes — [GraphRAG: Knowledge Graph + RAG Next-Generation](https://www.meta-intelligence.tech/en/insight-graphrag)
- LLMs can match or surpass traditional supervised extraction models for knowledge-graph construction, especially in open-domain scenarios — making LLM-driven extraction a viable foundation rather than a fallback — [GraphRAG: Knowledge Graph + RAG Next-Generation](https://www.meta-intelligence.tech/en/insight-graphrag)

## Convergent vs contested
- **Convergent:** Graph structure + hierarchical community summaries is the accepted way to support global/thematic and multi-hop questions that flat RAG cannot; Leiden hierarchical clustering is the standard community-detection algorithm; LLM-based extraction is good enough to build the graph.
- **Contested / open:** GraphRAG is not strictly better — for precise single-fact queries vector RAG is essentially on par, and GraphRAG adds latency and large indexing/token cost. Whether the +50–70% comprehensiveness gain justifies the cost is corpus- and question-mix-dependent.

## Implications for the system (Phase 2)
- Use a hybrid retrieval layer: vector/local retrieval for precise factual lookups, graph + community-summary (global) retrieval for synthesis/thematic questions — route by question type rather than committing to one.
- Treat the indexing pipeline as the cost center: build incremental indexing, tier models by task (cheap extraction, expensive summary), cap token budgets, and parallelize extraction through a queue.
- Add human-in-the-loop review of high-importance entities/relationships, since automated extraction carries noise that propagates downstream.
- Larger chunks (~1200 tokens) for the extraction stage to preserve cross-sentence relationships.

## Gaps found → re-scan
- Sources are GraphRAG-centric (mostly Microsoft GraphRAG and reimplementations); no coverage of alternative knowledge-compilation approaches (e.g. property-graph stores, ontology-driven KGs, temporal graphs). Re-scan: "knowledge graph vs property graph temporal graph ontology research knowledge base".
- Entity-resolution / deduplication and noise-propagation handling are named as problems but not solved in detail. Re-scan: "entity resolution deduplication knowledge graph noise propagation merge".
