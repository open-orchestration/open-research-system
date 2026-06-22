[Sitemap](https://aryaroop04.medium.com/sitemap/sitemap.xml)
[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)
Sign up
[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Faryaroop04.medium.com%2Fyour-rag-is-lying-to-you-the-complete-engineering-blueprint-for-agentic-self-corrective-rag-bc5f0c46aa6f&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)
[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)
Get app
[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)
[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)
Sign up
[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Faryaroop04.medium.com%2Fyour-rag-is-lying-to-you-the-complete-engineering-blueprint-for-agentic-self-corrective-rag-bc5f0c46aa6f&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)
![Unknown user](https://miro.medium.com/v2/resize:fill:32:32/1*dmbNkD5D-u45r44go_cf0g.png)
# Your RAG Is Lying to You — The Complete Engineering Blueprint for Agentic, Self-Corrective RAG Systems (2026)
[![Aryaroop Majumder](https://miro.medium.com/v2/resize:fill:32:32/1*B_pnTovCjFYQKSI6UmDZaQ.jpeg)](https://aryaroop04.medium.com/?source=post_page---byline--bc5f0c46aa6f---------------------------------------)
[Aryaroop Majumder](https://aryaroop04.medium.com/?source=post_page---byline--bc5f0c46aa6f---------------------------------------)
Follow
12 min read
·
Mar 20, 2026
[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fp%2Fbc5f0c46aa6f&operation=register&redirect=https%3A%2F%2Faryaroop04.medium.com%2Fyour-rag-is-lying-to-you-the-complete-engineering-blueprint-for-agentic-self-corrective-rag-bc5f0c46aa6f&user=Aryaroop+Majumder&userId=e55b3dba53ac&source=---header_actions--bc5f0c46aa6f---------------------clap_footer------------------)
5
[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Frepost%2Fp%2Fbc5f0c46aa6f&operation=register&redirect=https%3A%2F%2Faryaroop04.medium.com%2Fyour-rag-is-lying-to-you-the-complete-engineering-blueprint-for-agentic-self-corrective-rag-bc5f0c46aa6f&user=Aryaroop+Majumder&userId=e55b3dba53ac&source=---header_actions--bc5f0c46aa6f---------------------repost_header------------------)
[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fbc5f0c46aa6f&operation=register&redirect=https%3A%2F%2Faryaroop04.medium.com%2Fyour-rag-is-lying-to-you-the-complete-engineering-blueprint-for-agentic-self-corrective-rag-bc5f0c46aa6f&source=---header_actions--bc5f0c46aa6f---------------------bookmark_footer------------------)
[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3Dbc5f0c46aa6f&operation=register&redirect=https%3A%2F%2Faryaroop04.medium.com%2Fyour-rag-is-lying-to-you-the-complete-engineering-blueprint-for-agentic-self-corrective-rag-bc5f0c46aa6f&source=---header_actions--bc5f0c46aa6f---------------------post_audio_button------------------)
Share
From “Retrieve-and-Read” to “Reason-Retrieve-Verify-Generate” — a deep technical playbook for production engineers who’ve outgrown naive pipelines.
Press enter or click to view image in full size
![](https://miro.medium.com/v2/resize:fit:700/1*TJnU-OVCl076X8ibFaHBeA.png)
**RAG Evolution Timeline**
> The “Retrieve-Read” pipeline is no longer sufficient. Production systems must replace it with a **Reason → Retrieve → Verify → Generate** loop — one that can self-correct, reason hierarchically, and collaborate across agents.
## Abstract
The evolution of large language models has fundamentally altered the landscape of natural language processing, shifting the paradigm from purely parametric knowledge toward hybrid systems that leverage external, non-parametric data stores. While early iterations relied heavily on the internal weights of pre-trained transformers, the inherent limitations of these models — factual obsolescence, hallucinations in specialized domains, and the high cost of frequent fine-tuning — necessitated the development of **Retrieval-Augmented Generation (RAG)**.
This white-paper delineates the sophisticated landscape of RAG-based chatbots, moving beyond the foundational “Retrieve-and-Generate” workflow toward **modular, agentic, and self-corrective architectures**. By synthesizing recent advancements in data ingestion, query optimisation, and hierarchical reasoning, this report provides a comprehensive blueprint for professional peers seeking to implement high-fidelity, production-grade RAG systems.
## 1. The Paradigm Shift: From Naive to Modular RAG
The foundational concepts of **Naive RAG** follow a linear “Retrieve-Read” framework. In this traditional setup, documents are segmented, embedded into a vector space, and retrieved based on cosine similarity to a user query. While this works at the prototype stage, it fails critically in complex enterprise environments.
Naive RAG suffers from three compounding failure modes:
  * **Low retrieval precision** — the most semantically similar chunks are not always the most factually relevant.
  * **Low recall** — the system fails to find all necessary information for multi-hop queries.
  * **Contextual dilution** — irrelevant retrieved data degrades the final output through noise.


To overcome these hurdles, the industry has transitioned through **Advanced RAG** toward the current state-of-the-art: **Modular RAG**. This evolution represents a departure from fixed pipelines to composable, specialized modules that can be dynamically reconfigured. Modular RAG introduces specialized components such as search modules for structured databases, fusion modules for multi-query expansion, and alignment modules for refining retrieved text before it reaches the generator.
Press enter or click to view image in full size
![](https://miro.medium.com/v2/resize:fit:700/1*FbMeDuhUer0ZJQn0btP3OQ.png)
## 2. Advanced Ingestion and the Science of Semantic Chunking
The quality of a RAG system is inextricably linked to the **granularity and coherence of its data chunks**. Most baseline implementations use fixed-size character splitting — a method that is computationally efficient but often results in “contextual orphans”: fragments of text where the semantic meaning is severed by an arbitrary character limit.
## 2.1 Recursive Character and Structural Splitting
**Recursive character splitting** uses a hierarchical set of separators — paragraphs (`\n\n`), sentences (`\n`), and words () — to keep semantically related text together until the target chunk size is reached.
For structured documents like legal contracts or technical manuals, **document-based chunking** is superior. This approach leverages Markdown headers, HTML tags, or code structure (classes and functions) to define chunk boundaries, ensuring that sections and their relevant headings remain intact.
## 2.2 Semantic and Recursive Semantic Chunking (RSC)
**Semantic chunking** groups sentences based on the distance between their embeddings. A shift in meaning is identified when the cosine similarity between subsequent sentence embeddings falls below a certain threshold, triggering a new chunk boundary.
A more refined version, **Recursive Semantic Chunking (RSC)** , addresses the “chunk size dilemma” where purely semantic segments might become too large for efficient retrieval. The RSC framework applies an initial semantic split and then recursively re-splits any segment that exceeds a defined token threshold — often involving a “breakpoint adjustment” where the similarity threshold is gradually reduced in each iteration.
## 2.3 Agentic Chunking and Proposition-Level Granularity
At the leading edge of ingestion technology is **agentic chunking**. This methodology uses an LLM to perform “proposition conversion,” breaking down complex sentences into atomic, standalone statements that convey a single fact. While this is the most contextually accurate method, it introduces significant ingestion-time latency and cost, making it ideal for high-stakes, relatively static knowledge bases where accuracy outweighs speed.
### Chunking Methods Comparison
Press enter or click to view image in full size
![](https://miro.medium.com/v2/resize:fit:700/1*MWSrzORW4AbxZ2B1A7ylag.png)
## 3. Pre-Retrieval Optimization: Mastering the Semantic Gap
Sending raw queries directly to the vector database frequently leads to retrieval failure because users often use vague language or terminology that does not match the indexed corpus. Pre-retrieval optimization focuses on transforming the user’s intent into a format that maximizes the likelihood of a successful match within the latent space.
## 3.1 Hypothetical Document Embeddings (HyDE) and Inverse HyDE
**HyDE** solves the “query-document mismatch” by using an LLM to generate a hypothetical answer to the user’s question _before_ retrieval begins. By embedding this hypothetical response — which likely contains the technical jargon and dense vocabulary of the target documents — the system can perform a “document-to-document” search in the vector space, which is significantly more accurate than a “query-to-document” search.
To mitigate the query-time latency of HyDE, some production systems employ **Inverse HyDE** (hypothetical question generation). During the ingestion phase, the model generates 3–5 hypothetical questions for every document chunk. At query time, the system performs a “question-to-question” match — shifting the computational burden to the offline indexing phase.
## 3.2 Query Expansion and Step-Back Prompting
**Query expansion** involves generating multiple variations of a user’s question — using synonyms, domain-specific terms, and related concepts — to ensure a broader capture of relevant documents.
**Step-Back Prompting** encourages the model to “step back” from a specific, complex question to a broader, more abstract principle, helping the retriever locate high-level summaries that provide foundational context.
## 4. Retrieval Layer Enhancements: Beyond Vector Similarity
Press enter or click to view image in full size
![](https://miro.medium.com/v2/resize:fit:700/1*9bf_Vr1e4TIVvoMTKOVH4Q.png)
**Hybrid Retrieval + RRF Fusion Pipeline**
Modern research indicates that vector-only retrieval is often insufficient for production systems, particularly when dealing with exact identifiers, acronyms, or multi-hop reasoning.
## 4.1 Hybrid Retrieval and Reciprocal Rank Fusion (RRF)
The current gold standard for retrieval is a **hybrid approach** that combines semantic (dense) search with lexical (sparse) search. Semantic search excels at capturing intent and meaning, while lexical search (using BM25 or TF-IDF) is essential for retrieving specific terms, product IDs, or legal clauses.
To integrate these two distinct search results into a single ranked list, systems employ **Reciprocal Rank Fusion (RRF)** — an unsupervised method that calculates a combined score based on the rank of a document in each individual result set, not its absolute similarity score. This makes the merging process robust and eliminates the need for complex score normalization.
Press enter or click to view image in full size
![](https://miro.medium.com/v2/resize:fit:700/1*-IsLI_af-CPLpWPnjTalNA.png)
## 4.2 Multi-Vector Retrieval and the Parent Document Retriever
A common failure mode in baseline RAG systems is the “fragmentation” of information, where retrieved chunks are too small to provide the LLM with enough context. **Multi-vector retrieval** addresses this by decoupling the data used for retrieval from the data used for generation.
The **Parent Document Retriever** indexes small “child” chunks for precise similarity matching but returns the larger “parent” document to the generator — ensuring high retrieval precision while preserving semantic continuity.
## 5. Post-Retrieval Refinement: Reranking and Context Compression
The retrieval phase often produces a large set of candidate documents that vary significantly in their actual utility. Without a secondary filter, systems fall prey to **“prompt bloat”** and the **“lost in the middle” phenomenon** — where models ignore information placed in the center of long contexts.
## 5.1 Multi-Stage Reranking and Cross-Encoders
Reranking introduces a two-stage retrieval architecture:
  1. **Stage 1** — A “fast and cheap” retriever (like hybrid search) fetches a broad set of candidates (e.g., top 100).
  2. **Stage 2** — A “slow and expensive” reranker — often a cross-encoder or a specialized LLM-based ranker — performs a deep, token-level comparison between the query and each candidate to reorder them by true relevance.


**Cross-encoders** are particularly effective because they process the query and document simultaneously, capturing intricate interactions that standard cosine similarity misses. Reranking the top 50 candidates to find the final top 5 is considered the “sweet spot” for most production use cases.
## 5.2 Context Compression and Knowledge Distillation
**Context compression** uses an LLM or a smaller specialized model to summarize or prune retrieved chunks before passing them to the generator. This reduces token usage and minimizes “soft noise” — irrelevant details that distract the model from core facts. By extracting only the “knowledge strips” or essential propositions, the system consolidates more diverse information into the model’s finite context window.
## 6. GraphRAG: Hierarchical Reasoning over Private Datasets
Traditional RAG systems are inherently limited to “local” reasoning — they can only find information explicitly stated within a single chunk or a small set of semantically similar chunks. This makes them ineffective for holistic questions like _“What are the main themes across all these documents?”_
## Get Aryaroop Majumder’s stories in your inbox
Join Medium for free to get updates from this writer.
Subscribe
Subscribe
Remember me for faster sign in
**Microsoft’s GraphRAG framework** addresses this by constructing a knowledge graph from source documents, using LLMs to extract entities (nodes) and their relationships (edges), organized into hierarchical “communities” using algorithms like the **Leiden Algorithm**.
## 6.1 Local vs. Global Search in GraphRAG
GraphRAG enables two distinct modes of operation:
  1. **Local Search** — Optimized for targeted queries about specific entities. Retrieves the entity’s direct neighbors and associated concepts from the graph to provide a nuanced, multi-hop answer that baseline RAG would miss.
  2. **Global Search** — Designed for holistic dataset reasoning. Utilizes “community reports” — pre-computed summaries of graph clusters — to synthesize an answer reflecting the overarching themes of the entire corpus.


A critical advancement is **“dynamic community selection,”** which rates the relevance of high-level community reports before performing a map-reduce operation, reducing costs by up to **77%** compared to static global search.
### GraphRAG Search Modes
Press enter or click to view image in full size
![](https://miro.medium.com/v2/resize:fit:700/1*S6l7YPIUGt5-TH50QW_KrA.png)
## 7. Self-Corrective Frameworks: CRAG and Self-RAG
Press enter or click to view image in full size
![](https://miro.medium.com/v2/resize:fit:700/1*jutf67TN4GibFK1XoX_yCg.png)
**CRAG State Machine**
One of the most significant gaps in naive RAG architectures is the **lack of a feedback loop**. If the retriever fetches irrelevant information, the generator has no choice but to hallucinate. Self-corrective architectures introduce “quality gates” that allow the system to assess and refine its own retrieval and generation steps.
## 7.1 Corrective RAG (CRAG) State Machine
CRAG introduces a lightweight **retrieval evaluator** that assigns a confidence score to retrieved documents, classifying them as **Correct** , **Incorrect** , or **Ambiguous**. This triggers specific corrective actions:
  * **Correct** — Performs a “decompose-then-recompose” refinement, stripping away non-essential elements and keeping only core facts for the generator.
  * **Incorrect** — Discards retrieved chunks and initiates a large-scale web search to find the necessary information.
  * **Ambiguous** — Combines both internal retrieval and web search to provide a balanced context.


## 7.2 Self-Reflective RAG (Self-RAG)
Self-RAG takes this further by training the model to generate specialized **“reflection tokens”** that govern the RAG process on-demand. These tokens allow the model to critique its own work at multiple granularities:
  * `**Retrieve**`**Token** — Determines whether external information is even necessary for the current query.
  * `**ISREL**`**(Relevance)** — Evaluates if each retrieved passage is useful for answering the question.
  * `**ISSUP**`**(Support)** — Checks whether the generated response segment is actually supported by the retrieved facts, effectively acting as an anti-hallucination check.
  * `**ISUSE**`**(Utility)** — Scores the overall quality and direct relevance of the final response.


## 8. Agentic RAG: Autonomy and Multi-Agent Collaboration
**Agentic RAG** represents the pinnacle of current chatbot architecture, where AI agents are embedded directly into the RAG pipeline to manage complex, multi-step reasoning tasks. Unlike static workflows, agentic systems can autonomously decide when to retrieve data, which tools to use, and how to refine their goals based on intermediate results.
## 8.1 Core Agentic Design Patterns
  * **Planning and Task Decomposition** — Query planning agents break down complex, ambiguous user prompts into a structured sequence of sub-queries distributed to specialized sub-agents.
  * **ReAct (Reason and Act)** — Creates an iterative loop where the agent reasons about the current state, takes an action (like querying a database), and observes the outcome before planning the next step.
  * **Multi-Agent Collaboration** — A “research department” of specialized agents: a routing agent selects the best data source, a retrieval agent fetches the data, and a critic agent verifies the final output.


## 8.2 Orchestration and Logic Loops
In enterprise-grade systems, these agents are orchestrated through frameworks like **LangGraph** , enabling complex state machines:
  * **Sequential Pattern** — One agent’s output is the direct input for the next in a linear, deterministic chain.
  * **Parallel Pattern** — Multiple specialized sub-agents perform independent searches simultaneously, with outputs synthesized at the end.
  * **Loop Pattern** — The agent repeatedly refines its output through reflection until a specific quality threshold or “termination condition” is met.


### Agentic Design Patterns Comparison
Press enter or click to view image in full size
![](https://miro.medium.com/v2/resize:fit:700/1*2Ar5VSBpLh1z_s2Z7vTWHA.png)
## 9. RAG Performance Benchmarking and Latency Trade-offs
Every optimization added to a RAG pipeline — reranking, HyDE, or agentic reflection — **improves accuracy at the cost of latency and computational expense**. Deliberate engineering trade-offs are unavoidable.
## 9.1 Accuracy Benchmarks: Dense vs. Hybrid
Data suggests that hybrid systems significantly outperform dense-only approaches. Moving from dense-only to hybrid retrieval elevated the **Mean Reciprocal Rank (MRR)** from **0.410 to 0.486** — an **18.5% improvement** in the likelihood of the correct answer appearing in the top position. This accuracy lift came with a **24.5% increase in query latency** (an additional 201ms), largely due to the overhead of generating both dense and sparse vectors.
## 9.2 Reranking Efficiency
Reranking top-50 candidates is considered the “sweet spot” for most production use cases. While bi-encoders provide low-latency retrieval, cross-encoder rerankers can be **5,000× more expensive** in terms of compute-per-query. For systems where the response budget is strictly under 1,000ms, expensive rerankers may be unacceptable, forcing developers to rely on faster, quantized models or optimized late-interaction models like **ColBERT**.
## 9.3 Ingestion-Time vs. Query-Time Optimization
A critical strategy for production systems is to **shift as much computation as possible to the ingestion phase**. Generating hypothetical questions (Inverse HyDE) increases the vector store size by 5× and raises ingestion costs but allows for near-instant retrieval at query time — a vital trade-off for interactive chatbots.
## 10. RAG Evaluation Frameworks: RAGAS and Beyond
Modern RAG evaluation uses **“LLM-as-a-judge”** to separately score the retriever and the generator. The **RAGAS framework** utilizes four primary metrics:
  1. **Faithfulness** — Measures if the generated answer is factually consistent with the retrieved context (detects hallucinations).
  2. **Answer Relevancy** — Assesses how well the answer addresses the user’s original query.
  3. **Context Precision** — Evaluates the signal-to-noise ratio in the retrieved chunks and checks if ground-truth-relevant items are ranked correctly.
  4. **Context Recall** — Checks whether the retrieval system successfully found all the information required to support a ground-truth answer.


Tools like **DeepEval** and **Datadog** integrate these metrics into CI/CD pipelines, allowing developers to set thresholds for “drift detection” and automated PR gates. This shift from qualitative “vibes-based” testing to quantitative benchmarking is what distinguishes a mature technical implementation from a prototype.
## 11. Security, Robustness, and Adversarial Frontiers
## 11.1 Data Poisoning and BadRAG
Research into **BadRAG** demonstrates that poisoning just **0.04% of a corpus** with adversarial content can lead to a **98.2% attack success rate** , causing the system to return incorrect or malicious information. Defenses like cryptographic document signing and adversarial filtering are currently being developed, but proactive design — secure ingestion pipelines and integrity validation — is essential.
## 11.2 Privacy and Memorization Leakage
While RAG is often touted as a way to prevent model memorization, structured prompting can still exploit retrieval databases to leak private information. Conversely, some research suggests that RAG can act as a “grounding mechanism” that actually _reduces_ memorization leakage by forcing the model to rely on provided context rather than its own internal weights.
## 12. Strategic Conclusion: Building the Next-Generation RAG Pipeline
> The “Retrieve-Read” pipeline is no longer sufficient. It must be replaced by a **Reason → Retrieve → Verify → Generate** loop.
The transition from Naive RAG to the modular and agentic architectures detailed here is a necessary step for any production-level chatbot. To achieve this, developers should prioritize:
  * **Semantic Integrity** — Moving from character-based splitting to Recursive Semantic Chunking (RSC) to ensure the retriever has high-quality segments.
  * **Retrieval Redundancy** — Implementing Hybrid Search with RRF to combine the strengths of keyword and semantic matching.
  * **Refinement Loops** — Using CRAG and Self-RAG reflection tokens to proactively catch retrieval and generation errors.
  * **Hierarchical Understanding** — Deploying GraphRAG for complex datasets where entity relationships and holistic summaries are required.


By adopting these advanced techniques, RAG systems can move beyond simple information retrieval to become truly intelligent assistants capable of nuanced reasoning, factual grounding, and secure enterprise deployment. **The future of RAG lies in its modularity and agentic autonomy** — where the model no longer just “fetches” information but actively manages its own knowledge discovery and verification process.
_If you found this useful, consider following for more deep-dive engineering content on LLMs, RAG, and production AI systems._
[Rag](https://medium.com/tag/rags?source=post_page-----bc5f0c46aa6f---------------------------------------)
[LLM](https://medium.com/tag/llm?source=post_page-----bc5f0c46aa6f---------------------------------------)
[Ai Engineering](https://medium.com/tag/ai-engineering?source=post_page-----bc5f0c46aa6f---------------------------------------)
[Machine Learning](https://medium.com/tag/machine-learning?source=post_page-----bc5f0c46aa6f---------------------------------------)
[NLP](https://medium.com/tag/nlp?source=post_page-----bc5f0c46aa6f---------------------------------------)
[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fp%2Fbc5f0c46aa6f&operation=register&redirect=https%3A%2F%2Faryaroop04.medium.com%2Fyour-rag-is-lying-to-you-the-complete-engineering-blueprint-for-agentic-self-corrective-rag-bc5f0c46aa6f&user=Aryaroop+Majumder&userId=e55b3dba53ac&source=---footer_actions--bc5f0c46aa6f---------------------clap_footer------------------)
5
[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fp%2Fbc5f0c46aa6f&operation=register&redirect=https%3A%2F%2Faryaroop04.medium.com%2Fyour-rag-is-lying-to-you-the-complete-engineering-blueprint-for-agentic-self-corrective-rag-bc5f0c46aa6f&user=Aryaroop+Majumder&userId=e55b3dba53ac&source=---footer_actions--bc5f0c46aa6f---------------------clap_footer------------------)
5
[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Frepost%2Fp%2Fbc5f0c46aa6f&operation=register&redirect=https%3A%2F%2Faryaroop04.medium.com%2Fyour-rag-is-lying-to-you-the-complete-engineering-blueprint-for-agentic-self-corrective-rag-bc5f0c46aa6f&user=Aryaroop+Majumder&userId=e55b3dba53ac&source=---footer_actions--bc5f0c46aa6f---------------------repost_footer------------------)
[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fbc5f0c46aa6f&operation=register&redirect=https%3A%2F%2Faryaroop04.medium.com%2Fyour-rag-is-lying-to-you-the-complete-engineering-blueprint-for-agentic-self-corrective-rag-bc5f0c46aa6f&source=---footer_actions--bc5f0c46aa6f---------------------bookmark_footer------------------)
[![Aryaroop Majumder](https://miro.medium.com/v2/resize:fill:48:48/1*B_pnTovCjFYQKSI6UmDZaQ.jpeg)](https://aryaroop04.medium.com/?source=post_page---post_author_info--bc5f0c46aa6f---------------------------------------)
[![Aryaroop Majumder](https://miro.medium.com/v2/resize:fill:64:64/1*B_pnTovCjFYQKSI6UmDZaQ.jpeg)](https://aryaroop04.medium.com/?source=post_page---post_author_info--bc5f0c46aa6f---------------------------------------)
Follow
## [Written by Aryaroop Majumder](https://aryaroop04.medium.com/?source=post_page---post_author_info--bc5f0c46aa6f---------------------------------------)
[12 followers](https://aryaroop04.medium.com/followers?source=post_page---post_author_info--bc5f0c46aa6f---------------------------------------)
·[1 following](https://aryaroop04.medium.com/following?source=post_page---post_author_info--bc5f0c46aa6f---------------------------------------)
I’m innovating at the intersection of AI and LLMs. Machine Learning Engineer at Prescience Decision Solutions.
Follow
[Help](https://help.medium.com/hc/en-us?source=post_page-----bc5f0c46aa6f---------------------------------------)
[Status](https://status.medium.com/?source=post_page-----bc5f0c46aa6f---------------------------------------)
[About](https://medium.com/about?autoplay=1&source=post_page-----bc5f0c46aa6f---------------------------------------)
[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----bc5f0c46aa6f---------------------------------------)
Press
[Blog](https://blog.medium.com/?source=post_page-----bc5f0c46aa6f---------------------------------------)
[Store](https://medium.com/store)
[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----bc5f0c46aa6f---------------------------------------)
[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----bc5f0c46aa6f---------------------------------------)
[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----bc5f0c46aa6f---------------------------------------)
[Text to speech](https://speechify.com/medium?source=post_page-----bc5f0c46aa6f---------------------------------------)

