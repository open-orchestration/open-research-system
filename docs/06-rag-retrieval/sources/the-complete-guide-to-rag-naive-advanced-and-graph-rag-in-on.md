# The Complete Guide to RAG: Naive, Advanced, and Graph RAG in One ...

Source: https://www.mrlatte.net/en/research/2026/04/27/rag-complete-guide/

[Skip to main](https://www.mrlatte.net/en/research/2026/04/27/rag-complete-guide/#main)
[**Mr. Latte**](https://www.mrlatte.net/en/)
  * [Hello ▾](https://www.mrlatte.net/en/research/2026/04/27/rag-complete-guide/)
    * [About](https://www.mrlatte.net/en/about)
    * [Work With Me](https://www.mrlatte.net/en/work-with-me)
    * [Contact](https://www.mrlatte.net/en/contact)
  * [Build ▾](https://www.mrlatte.net/en/research/2026/04/27/rag-complete-guide/)
    * [Products](https://www.mrlatte.net/en/services)
    * [Projects](https://www.mrlatte.net/en/projects)
  * [Writing ▾](https://www.mrlatte.net/en/research/2026/04/27/rag-complete-guide/)
    * [Blog](https://www.mrlatte.net/en/blog)
    * [Research](https://www.mrlatte.net/en/research)
  * [Learn ▾](https://www.mrlatte.net/en/research/2026/04/27/rag-complete-guide/)
    * [Courses](https://www.mrlatte.net/en/courses)
    * [Store](https://www.mrlatte.net/en/store)
  * [Hobby ▾](https://www.mrlatte.net/en/research/2026/04/27/rag-complete-guide/)
    * [Paintings](https://www.mrlatte.net/en/paintings)
  * [KO](https://www.mrlatte.net/research/2026/04/27/rag-complete-guide/)


  * [About](https://www.mrlatte.net/en/about)
  * [Work With Me](https://www.mrlatte.net/en/work-with-me)
  * [Contact](https://www.mrlatte.net/en/contact)
  * [Products](https://www.mrlatte.net/en/services)
  * [Projects](https://www.mrlatte.net/en/projects)
  * [Blog](https://www.mrlatte.net/en/blog)
  * [Research](https://www.mrlatte.net/en/research)
  * [Courses](https://www.mrlatte.net/en/courses)
  * [Store](https://www.mrlatte.net/en/store)
  * [Paintings](https://www.mrlatte.net/en/paintings)
  * [한국어](https://www.mrlatte.net/research/2026/04/27/rag-complete-guide/)


* * *
# The Complete Guide to RAG: Naive, Advanced, and Graph RAG in One Document
  * [Home](https://www.mrlatte.net/en/)
  * [Research](https://www.mrlatte.net/en/research)
  * The Complete Guide to RAG: Naive, Advanced, and Graph RAG in One Document


> **One document that covers RAG end to end.** Theory (why you need it, how it evolved) + runnable code (copy-paste and run) + the latest patterns (Agentic, GraphRAG, Contextual Retrieval) + limits and alternatives + a decision guide — all in here.
I’ve been building and operating RAG systems since 2023, and it’s by far the pattern I run into most. The material is scattered across blogs, papers, and release notes, so I pulled my own notes and the examples I trust into one place — so the next time I need to look something up, I can do it on a single page. Beginners can read it as a learning path; folks already shipping it can use the comparison tables to pick options.
* * *
## Table of Contents
**Part I — Foundations**
  1. [What is RAG?](https://www.mrlatte.net/en/research/2026/04/27/rag-complete-guide/#1-what-is-rag)
  2. [Why RAG?](https://www.mrlatte.net/en/research/2026/04/27/rag-complete-guide/#2-why-rag)
  3. [Three generations of RAG: Naive → Advanced → Modular → Graph](https://www.mrlatte.net/en/research/2026/04/27/rag-complete-guide/#3-three-generations-of-rag-naive--advanced--modular--graph)


  * [Before we start: Glossary](https://www.mrlatte.net/en/research/2026/04/27/rag-complete-guide/#before-we-start-glossary)


**Part II — Implementation**
  1. [Naive RAG: the basic five steps](https://www.mrlatte.net/en/research/2026/04/27/rag-complete-guide/#4-naive-rag-the-basic-five-steps)
  2. [Example 1: Naive RAG (LangChain + Chroma)](https://www.mrlatte.net/en/research/2026/04/27/rag-complete-guide/#example-1-naive-rag-langchain--chroma)
  3. [Advanced RAG, in depth](https://www.mrlatte.net/en/research/2026/04/27/rag-complete-guide/#6-advanced-rag-in-depth)
  4. [Example 2: Advanced RAG (Hybrid + Rerank + query transformation + citation + Self-Eval)](https://www.mrlatte.net/en/research/2026/04/27/rag-complete-guide/#example-2-advanced-rag)
  5. [Graph RAG, in depth](https://www.mrlatte.net/en/research/2026/04/27/rag-complete-guide/#8-graph-rag-in-depth)
  6. [Example 3: Graph RAG (entity/relation extraction + graph traversal)](https://www.mrlatte.net/en/research/2026/04/27/rag-complete-guide/#example-3-graph-rag)


**Part III — Operations and decisions**
  1. [Evaluation methods and metrics](https://www.mrlatte.net/en/research/2026/04/27/rag-complete-guide/#10-evaluation-methods-and-metrics)
  2. [Recent trends (2024–2026)](https://www.mrlatte.net/en/research/2026/04/27/rag-complete-guide/#11-recent-trends-20242026)
  3. [Limits and alternatives](https://www.mrlatte.net/en/research/2026/04/27/rag-complete-guide/#12-limits-and-alternatives)
  4. [Three-way comparison and decision guide](https://www.mrlatte.net/en/research/2026/04/27/rag-complete-guide/#13-three-way-comparison-and-decision-guide)
  5. [Production checklist](https://www.mrlatte.net/en/research/2026/04/27/rag-complete-guide/#14-production-checklist)
  6. [Setting up your environment](https://www.mrlatte.net/en/research/2026/04/27/rag-complete-guide/#15-setting-up-your-environment)


**Part IV — Beyond RAG**
  1. [LLM Wiki: a knowledge system that _accumulates_ instead of retrieving](https://www.mrlatte.net/en/research/2026/04/27/rag-complete-guide/#16-llm-wiki-a-knowledge-system-that-accumulates-instead-of-retrieving)
  2. [Example 4: LLM Wiki (a self-maintaining wiki agent)](https://www.mrlatte.net/en/research/2026/04/27/rag-complete-guide/#example-4-llm-wiki)


* * *
## Part I — Foundations
### 1. What is RAG?
**RAG (Retrieval-Augmented Generation)** combines _Retrieval + Augmentation + Generation_. The concept was formalized in 2020 by Lewis et al. (Facebook AI Research).
The core idea is one line:
> **Don’t pack all knowledge into the LLM’s parameters — let it pull what it needs from outside, when it needs it.**
The LLM is the _reasoner_. The external knowledge base is the _reference_. If you compare it to an exam, RAG turns a closed-book test into an open-book one.

```
[user question] → [retrieval] → top-K relevant docs → [question + docs] → LLM → [grounded answer]
```

### 2. Why RAG?
RAG addresses **three fundamental problems** that show up when you use an LLM by itself.
#### 2.1 Freshness
LLMs don’t know what happened after their training cutoff. If your company policy changed yesterday, the model has no way to know. **With RAG, you just refresh the index and the change is reflected immediately.**
#### 2.2 Private knowledge
Internal wikis, customer tickets, medical charts, legal contracts — none of that is in the model’s training data. Training it in costs a fortune and creates security headaches. **RAG keeps the data outside the model and never touches the weights.**
#### 2.3 Hallucination
LLMs invent plausible-sounding answers when they don’t actually know. **RAG mitigates this with the constraint “answer only from the retrieved documents” plus citations — fewer hallucinations and verifiable answers.**
#### 2.4 Side benefits
  * **Cost** : a smaller model with good RAG is often cheaper than a large model alone.
  * **Permissions** : you can apply per-user permissions at the retrieval step.
  * **Auditability** : you log which documents informed each answer — a must in regulated industries.


### 3. Three generations of RAG: Naive → Advanced → Modular → Graph
RAG has evolved fast since 2020. The classification most academics and practitioners agree on:
#### 3.1 Naive RAG (1st gen, ~early 2023)
> “Vector-search the question as-is, dump the result into the LLM.”
The simplest form. Chunk → embed → similarity search → generate. Most beginner tutorials are this.
**Limits** : weak on ambiguous questions, missing synonyms, multi-hop reasoning, and cases where keyword matching matters.
#### 3.2 Advanced RAG (2nd gen, 2023–2024)
> “Make every stage of retrieval — pre, during, post — smarter.”
_Pre-retrieval_ : semantic chunking, metadata enrichment, query rewriting/expansion/decomposition, HyDE. _Retrieval_ : Hybrid (Dense + Sparse), Multi-vector, ColBERT. _Post-retrieval_ : Reranking, contextual compression, MMR, forced citations.
**Core message** : _“smarter retrieval.”_ Data representation is still chunks + embeddings.
#### 3.3 Modular RAG (2.5 gen)
> “Make each stage modular and swappable; let the system route, loop, and call tools freely.”
A router dispatches different sub-RAGs by question type, the system loops if results are insufficient, and external tools (SQL/API/web) are in play. **Self-RAG, CRAG, Adaptive RAG, Agentic RAG** all live here.
#### 3.4 Graph RAG (relation-centric evolution)
> “Represent documents as an entity-relation graph instead of chunks.”
The LLM extracts _(entity, relation, entity)_ triples from the documents and stores them in a graph DB. At query time you traverse the graph to gather multi-hop information. Microsoft GraphRAG (2024), LightRAG (2024), and the Neo4j-LangChain integration are the canonical examples.
**Strengths** : multi-hop reasoning, domains where relationships are the point. **Weaknesses** : graph construction cost, schema design overhead.
#### At a glance  
| Generation  | Core idea  | Data representation  | Strengths  | Weaknesses  |  
| --- | --- | --- | --- | --- |  
| Naive  | Simple search → generate  | Chunks + embeddings  | Easy to build  | Low accuracy  |  
| Advanced  | Smarter retrieval pipeline  | Chunks + embeddings + metadata  | Better retrieval accuracy  | Pipeline complexity  |  
| Modular  | Routing, looping, tools  | Mix of indexes  | Flexibility, autonomy  | Operational difficulty  |  
| Graph  | Relationship graph  | Nodes + edges (+ embeddings)  | Multi-hop, relational reasoning  | Graph build cost  |  
* * *
* * *
## Before we start: Glossary
Before we dive into implementation, here’s everything you’ll see throughout this document — terms and tool names — collected in one place. **Skip what you already know** , and come back when something later in the document trips you up.
### A. Basic concepts
  * **LLM (Large Language Model)** — GPT, Claude, Gemini, etc. Here it plays the _reasoner_ role that generates the answer.
  * **token** — the smallest unit an LLM processes. One English word ≈ 1–1.5 tokens; one Korean character ≈ 1–3 tokens. A model’s context limit is expressed in tokens (e.g., “Claude 200K tokens”).
  * **context window** — the max number of tokens the model can take in a single input.
  * **embedding** — text converted into a numeric vector (e.g., a 1024-dim float array). Retrieval rests on the property _“if the meanings are similar, the vectors are close.”_
  * **vector** — here, just _an array of numbers_. Embedding a sentence yields an N-dim vector.
  * **vector DB** — a database designed to store embedding vectors and _quickly find similar ones_. e.g., Chroma, Pinecone.
  * **similarity** — how close two vectors are. _Cosine similarity_ is the most common; closer to 1 means more similar.
  * **top-k** — the top k results. “top-5 documents” = the 5 most relevant.
  * **chunk** — a slice of a long document that becomes a unit of retrieval.
  * **chunk_size / chunk_overlap** — the size of one chunk / how much adjacent chunks overlap.


### B. HuggingFace model paths — what is `BAAI/bge-m3`?
**HuggingFace** is a platform for sharing AI models (think _GitHub for ML_). Models are identified as `org_name/model_name`. So `BAAI/bge-m3` means _the model named bge-m3, by an org called BAAI_.  
| Identifier  | What it is  |  
| --- | --- |  
| `BAAI/bge-m3`  | The **BGE-M3** model from **BAAI** (Beijing Academy of AI). A strong multilingual embedding.  |  
| `BAAI/bge-reranker-v2-m3`  | A **reranker** (cross-encoder) from the same BAAI  |  
| `intfloat/multilingual-e5-large`  | The **E5** multilingual embedding from researcher _intfloat_  |  
| `nlpai-lab/KURE-v1`  | A Korean-tuned embedding from a Korean NLP AI lab  |  
| `sentence-transformers/all-MiniLM-L6-v2`  | A lightweight English embedding (popular for testing)  |  
**Common model families**
  * **BGE** (BAAI General Embedding) — BAAI’s embedding line. `bge-m3` (multilingual), `bge-large-en` (English), `bge-reranker` (reranker), etc.
  * **E5** — Microsoft Research embeddings. `multilingual-e5-large`, `e5-mistral-7b-instruct`, etc.
  * **GTE** — Alibaba’s embedding line.
  * **ColBERT** — late-interaction retrieval model.


When you write `HuggingFaceEmbeddings(model_name="BAAI/bge-m3")` in code, the model is downloaded _once_ from HuggingFace and cached at `~/.cache/huggingface`; subsequent runs load it from cache.
### C. Retrieval algorithms / techniques
  * **BM25** — the standard keyword-matching scoring function in IR (formalized in the 1990s). It computes _“how often and how distinctively does this term appear in this document.”_ Strong on exact identifiers (error codes, proper nouns).
  * **Dense / Sparse Retrieval** — _Dense_ is vector (dense) search; _Sparse_ is word-based search like BM25. The latter is called “sparse” because its representation is mostly zeros.
  * **ANN (Approximate Nearest Neighbor)** — algorithms that find the nearest vector among millions _approximately_ but quickly. **HNSW** , **IVF-PQ** are the popular variants. Essentially every vector DB uses one internally.
  * **Bi-encoder vs Cross-encoder** — _Bi-encoder_ : question and document are embedded separately and then compared (fast, used for first-pass retrieval). _Cross-encoder_ : both are fed in together to compute a score (accurate, slow, used for reranking).
  * **RRF (Reciprocal Rank Fusion)** — the standard way to combine results from multiple retrievers. Sum the inverses of each retriever’s rank. See §6.4.
  * **MMR (Maximal Marginal Relevance)** — adds _diversity_ to the top-k. Prevents near-identical chunks from dominating the slots.
  * **HyDE (Hypothetical Document Embeddings)** — the LLM drafts a fake answer first, and _that answer_ is embedded for retrieval. Exploits the fact that answer-to-answer is usually closer than question-to-answer.


### D. Libraries / frameworks
  * **LangChain** — the LLM application framework (Python/JS). The skeleton of every example here.
  * **LCEL (LangChain Expression Language)** — LangChain’s `|` pipe syntax. You _vertically pipe_ components like `prompt | llm | parser`. Same idea as `cat file | grep ... | wc -l` in a Unix shell.
  * **Runnable** — the common interface for components you can chain with `|` in LCEL. `RunnablePassthrough()` passes the input straight through to the next stage.
  * **LlamaIndex** — LangChain’s main rival. More specialized in indexing and knowledge graphs.
  * **sentence-transformers** — the most common Python library; supports both embeddings and cross-encoders.
  * **NetworkX** — Python’s in-memory graph library. Used in Example 3 as a stand-in for a real graph DB.
  * **rank_bm25** — a small Python package that implements BM25.


### E. Vector DBs / Graph DBs  
| Category  | Name  | One-liner  |  
| --- | --- | --- |  
| Vector (managed)  | **Pinecone**  | Easiest cloud option, costs money  |  
| Vector  | **Weaviate**  | Built-in hybrid search, GraphQL support  |  
| Vector  | **Qdrant**  | Rust-based, friendly to self-hosting  |  
| Vector  | **Chroma**  | Lightest, top pick for prototyping (used in this doc)  |  
| Vector  | **Milvus**  | Billion-vector scale  |  
| Vector (extension)  | **pgvector**  | Drop-in PostgreSQL extension  |  
| Vector + keyword  | **Elasticsearch / OpenSearch**  | Both, plenty of operational know-how  |  
| Graph  | **Neo4j**  | The de-facto standard graph DB. Query language **Cypher**  |  
| Graph  | **Memgraph**  | Neo4j-compatible, faster  |  
| Graph  | **NebulaGraph**  | Large-scale distributed graph  |  
  * **Cypher** — Neo4j’s query language. e.g., `MATCH (p:Person)-[:WORKS_AT]->(c:Company) RETURN p, c`. Think _SQL for graphs_.


### F. Evaluation / benchmarks
  * **MTEB (Massive Text Embedding Benchmark)** — HuggingFace’s combined leaderboard for embedding models. The first place to look when picking an embedding.
  * **RAGAS** — an automated RAG evaluation framework. Measures _Faithfulness_ , _Answer Relevance_ , _Context Precision_ , etc., LLM-as-judge style.
  * **TruLens / DeepEval / ARES** — alternatives or complements to RAGAS.
  * **LLM-as-judge** — asking another LLM _“is this answer good?”_ as your evaluation method.
  * **Faithfulness / Hallucination** — _Faithfulness_ : does the answer stick to the retrieved context? _Hallucination_ : a plausible answer made up without evidence.


### G. Tools / services (especially in Part IV)
  * **Obsidian** — a markdown-based personal knowledge management app. Wikilinks `[[page name]]`, graph view supported. Free.
  * **Web Clipper** — a browser extension that turns web pages into markdown saved into Obsidian.
  * **Dataview** — an Obsidian plugin that queries page YAML frontmatter SQL-style to generate dynamic tables/lists.
  * **Marp** — a tool for making slides from markdown. Has an Obsidian plugin.
  * **qmd** — a local search engine for a folder of markdown (BM25 + vector + LLM rerank). Provides CLI + MCP server.
  * **Claude Code / Codex** — _agentic coding tools_ that operate the file system and shell directly. A natural fit for LLM Wiki.
  * **CLAUDE.md / AGENTS.md** — _project usage instructions_ meant to be read by the agentic tools above. A meta document in natural language describing _“this repo is laid out like X, please work on it like Y.”_ See §16.2.
  * **Microsoft GraphRAG** — Microsoft Research’s official GraphRAG implementation.
  * **LightRAG** — a lighter GraphRAG variant from HKU (Hong Kong University).


### H. Common acronyms  
| Acronym  | Expansion  |  
| --- | --- |  
| API  | Application Programming Interface  |  
| LLM  | Large Language Model  |  
| RAG  | Retrieval-Augmented Generation  |  
| KG  | Knowledge Graph  |  
| NER  | Named Entity Recognition  |  
| DB  | Database  |  
| MQ  | Message Queue  |  
| IaC  | Infrastructure as Code  |  
| PR  | Pull Request  |  
| PoC  | Proof of Concept  |  
| PM  | Project Manager  |  
| MCP  | Model Context Protocol (Anthropic’s tool integration standard)  |  
| PII  | Personally Identifiable Information  |  
| RRF  | Reciprocal Rank Fusion  |  
| MMR  | Maximal Marginal Relevance  |  
| BFS  | Breadth-First Search  |  
| AST  | Abstract Syntax Tree  |  
* * *
## Part II — Implementation
### 4. Naive RAG: the basic five steps
The simplest RAG flow:
  1. **Load** : collect raw sources from PDFs, the web, a DB, Notion, etc.
  2. **Chunk** : split long documents into retrieval-sized pieces.
  3. **Embed** : convert each chunk into a vector.
  4. **Retrieve** : pull the K chunks closest to the question’s embedding.
  5. **Generate** : drop the retrieved text into the prompt and let the LLM answer.


#### Recommended chunking parameters  
| Item  | Recommended  | Notes  |  
| --- | --- | --- |  
| chunk_size  | 256–1024 tokens  | Too small loses context, too large adds noise  |  
| chunk_overlap  | 10–20% of chunk_size  | Prevents loss at boundaries  |  
| Legal documents  | By clause  | Prefer the domain’s structure  |  
| Technical docs  | By section (header)  | Markdown header splitter  |  
| FAQ  | Q&A pairs  | The question is the retrieval unit  |  
| Code  | By function/class  | AST-based splitter  |  
#### Choosing an embedding model (as of 2026)
> Note: if `BAAI/bge-m3` looks unfamiliar, see [Glossary §B](https://www.mrlatte.net/en/research/2026/04/27/rag-complete-guide/#b-huggingface-model-paths--what-is-baaibge-m3) first — that’s a HuggingFace model path of the form _org_name/model_name_.
  * **Multilingual / Korean** : `BAAI/bge-m3`, `intfloat/multilingual-e5-large`, `nlpai-lab/KURE-v1`
  * **English / closed-source** : OpenAI `text-embedding-3-large`, Cohere `embed-v3`, Voyage `voyage-3`
  * Decide based on **MTEB leaderboard** scores + domain fit + cost/latency.


* * *
### Example 1: Naive RAG (LangChain + Chroma)
> Internal HR wiki scenario. The five steps in their simplest form. Environment setup is in [§15](https://www.mrlatte.net/en/research/2026/04/27/rag-complete-guide/#15-setting-up-your-environment). You need `ANTHROPIC_API_KEY`.

```
"""example_1_naive_rag.py — minimum 5-step Naive RAG"""
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# ── 1) Documents (in production, load from PDFs/Notion/DB) ─
raw = [
    Document(page_content=(
        "ACME annual leave policy: full-time employees receive 15 days of annual leave "
        "after one year of employment. 16 days after 3 years, 18 days after 5 years, "
        "20 days after 10 years. Unused leave can be carried over to June 30 of the "
        "following year, after which it expires."),
        metadata={"source": "HR/leave_policy_v3.md"}),
    Document(page_content=(
        "Special leave: 5 days for own marriage, 1 day for child's marriage, "
        "10 days for spouse's childbirth, 5 days for death of own/spouse's parent, "
        "3 days for death of grandparent. Family events such as a parent's 60th or 70th "
        "birthday do not qualify for special leave and must be taken as annual leave."),
        metadata={"source": "HR/special_leave.md"}),
    Document(page_content=(
        "Remote work: full-time employees can work from home twice a week. Manager "
        "approval required in advance. Tue/Thu remote is discouraged (company-wide "
        "meetings). New hires must come in every day for the first 3 months."),
        metadata={"source": "HR/remote_work_policy.md"}),
]

# ── 2) Chunking ──────────────────────────────────────────
splitter = RecursiveCharacterTextSplitter(
    chunk_size=300, chunk_overlap=50,
    separators=["\n\n", "\n", ". ", " ", ""])
chunks = splitter.split_documents(raw)

# ── 3) Embed + vector store ─────────────────────────────
emb = HuggingFaceEmbeddings(
    model_name="BAAI/bge-m3",
    encode_kwargs={"normalize_embeddings": True})
vectordb = Chroma.from_documents(chunks, emb, collection_name="acme_hr")

# ── 4) Retriever ────────────────────────────────────────
retriever = vectordb.as_retriever(search_kwargs={"k": 3})

# ── 5) Prompt + LLM + chain ─────────────────────────────
prompt = ChatPromptTemplate.from_messages([
    ("system",
     "ACME HR assistant. Answer based only on the [reference documents] below. "
     "If you can't find an answer, reply 'I cannot find the answer in the provided documents.' "
     "End each claim with [filename] as the citation."),
    ("human", "[reference documents]\n{context}\n\n[question]\n{question}")])

llm = ChatAnthropic(model="claude-opus-4-7", temperature=0)

def fmt(docs):
    return "\n\n".join(f"[{d.metadata['source']}]\n{d.page_content}" for d in docs)

# LCEL: LangChain Expression Language. Components are chained with `|`.
# Same idea as `cat file | grep ... | wc -l` in a Unix shell.
chain = ({"context": retriever | fmt, "question": RunnablePassthrough()}
         | prompt | llm | StrOutputParser())

# ── Run ────────────────────────────────────────────────
for q in [
    "If my parent's 60th birthday falls in my first year, how many days of leave do I get?",
    "How many days of annual leave does someone with 7 years of tenure get?",
    "Can a new hire work from home?",
    "Does the company cover lunch?",  # not in the docs → should refuse
]:
    print(f"\n━━━ Q: {q}\n> {chain.invoke(q)}")

```

#### What this shows
  * The five-step flow fits on one screen.
  * You can verify that “questions not in the docs” are properly refused.
  * A multilingual embedding (`bge-m3`) handles mixed Korean/English content.


#### Limits (you can feel them in this example)
  * Weak on synonyms / paraphrases — “salary” vs “compensation”.
  * Misses when the keyword is a precise identifier — “ERR_404”.
  * Multi-hop — “Who is the manager of the employee who took the most vacation recently?” → can’t be answered from a single chunk.
  * If retrieval is wrong, the answer is automatically wrong.


→ The next step, **Advanced RAG** , addresses these limits one by one.
* * *
### 6. Advanced RAG, in depth
Advanced RAG **takes the Naive RAG retrieval pipeline and strengthens it across the pre/during/post stages**. The data representation is still chunks + embeddings, but each stage gets sharper techniques that meaningfully boost retrieval accuracy and answer quality.

```
                          ┌─ Pre-retrieval  ────┐
raw docs ─→ semantic ────→│ metadata enrichment  │
            chunking      │ Contextual Embedding │
                          └──────────┬───────────┘
                                     ▼
user question ─→ query xform ─→ Hybrid retrieval ──→ Reranking ──→ context compression ─→ prompt ─→ LLM ─→ answer
                (Pre-retrieval)     (Retrieval)        (Post-retrieval)
```

#### 6.1 Semantic Chunking
Fixed-size chunking ignores meaning boundaries. Semantic chunking uses embedding-similarity discontinuities as boundaries, producing more natural units.

```
from langchain_experimental.text_splitter import SemanticChunker
from langchain_community.embeddings import HuggingFaceEmbeddings

splitter = SemanticChunker(
    HuggingFaceEmbeddings(model_name="BAAI/bge-m3"),
    breakpoint_threshold_type="percentile",  # or "standard_deviation", "interquartile"
    breakpoint_threshold_amount=95)
chunks = splitter.create_documents([long_text])

```

It costs more, but pays off on long reports or transcripts where semantic units are irregular.
#### 6.2 Contextual Retrieval (Anthropic, 2024)
Before embedding each chunk, prepend it with **a short summary of the document the chunk comes from** , generated by an LLM.

```
Original chunk: "Revenue grew 12% year-over-year."

Contextual chunk:
"This chunk is from ACME's Q3 2024 earnings report, in the financial
performance section. — Revenue grew 12% year-over-year."
```

According to Anthropic’s report, retrieval failure rate drops by **35–67%**. Indexing costs more LLM tokens, but it’s a one-time cost — and combined with prompt caching it becomes very cheap.
#### 6.3 Query Transformation
Reshape the original question when it isn’t a great query.  
| Technique  | Description  | Example  |  
| --- | --- | --- |  
| **Query Rewriting**  | LLM rewrites the question more clearly  | “what’s their policy?” → “What is ACME’s refund policy?”  |  
| **Query Expansion**  | Add synonyms / related terms  | “quitting” + “resignation, leaving, separation”  |  
| **HyDE**  | LLM drafts a hypothetical answer → embed the _answer_ and search  | Answer-to-answer is closer than question-to-answer  |  
| **Multi-Query**  | Search with N variants of one question, then merge  | Combine with RRF  |  
| **Step-Back**  | Abstract to a more general question first  | “Side effects of drug X” → “Mechanism of action of drug X?”  |  
| **Decomposition**  | Break a compound question into sub-questions  | “Compare A vs B” → [“What is A?”, “What is B?”]  |  
##### HyDE example

```
from langchain_core.prompts import ChatPromptTemplate
from langchain_anthropic import ChatAnthropic

llm = ChatAnthropic(model="claude-opus-4-7", temperature=0)
hyde_prompt = ChatPromptTemplate.from_messages([
    ("system", "Write a single plausible paragraph answering the question, regardless of factual accuracy."),
    ("human", "{question}")
])

def hyde_search(question: str, retriever):
    hypothetical = (hyde_prompt | llm).invoke({"question": question}).content
    # Embed the hypothetical answer for retrieval (usually more accurate than searching with the question itself)
    return retriever.invoke(hypothetical)

```

#### 6.4 Hybrid Retrieval
**BM25 (keyword) + Dense (vector)** combined. Almost always beats either alone.

```
from langchain_community.retrievers import BM25Retriever
from langchain.retrievers import EnsembleRetriever

bm25 = BM25Retriever.from_documents(chunks); bm25.k = 10
dense = vectordb.as_retriever(search_kwargs={"k": 10})
hybrid = EnsembleRetriever(
    retrievers=[bm25, dense],
    weights=[0.4, 0.6])  # tune by domain (heavier BM25 if lots of code/identifiers)

```

##### RRF (Reciprocal Rank Fusion)
The standard way to combine multiple retrievers’ results. RRF(d)=∑i1k+ranki(d)\text{RRF}(d) = \sum_{i} \frac{1}{k + \text{rank}_i(d)}RRF(d)=i∑​k+ranki​(d)1​ Typically _k=60_. Similar to what `EnsembleRetriever` does internally.
#### 6.5 Reranking
The first-pass retrieval pulls 50–100 candidates broadly; the reranker tightens the list to a precise 5–10.  
| Type  | Accuracy  | Speed  | Cost  |  
| --- | --- | --- | --- |  
| Cross-encoder (`bge-reranker-v2-m3`)  | High  | Moderate  | Free (self-hosted)  |  
| Cohere Rerank-v3 / Voyage Rerank  | Very high  | Fast  | Paid API  |  
| ColBERT (late interaction)  | High  | Fast  | Free  |  
| LLM-as-reranker (Claude/GPT)  | Very high  | Slow  | Very expensive  |  
**Empirical effect** : simply adding reranking commonly improves answer accuracy by 10–20 points.
#### 6.6 Contextual Compression
Trim the parts of retrieved documents that aren’t relevant to the question. Saves tokens, mitigates Lost-in-the-Middle.

```
from langchain.retrievers.document_compressors import LLMChainExtractor
from langchain.retrievers import ContextualCompressionRetriever

compressor = LLMChainExtractor.from_llm(llm)  # extract only what's needed to answer
compressed = ContextualCompressionRetriever(
    base_compressor=compressor,
    base_retriever=hybrid)

```

#### 6.7 Self-RAG / CRAG (the start of Modular RAG)
The model itself evaluates retrieval quality and branches accordingly.
  * **Self-RAG (Asai et al., 2023)** : the model decides whether to retrieve via a `[Retrieve]` token, and self-evaluates retrieval/answer quality with `[IsRel]`, `[IsSup]`, `[IsUse]` tokens.
  * **CRAG (Yan et al., 2024)** : judges retrieval results — **Correct → use** , **Ambiguous → augment** , **Incorrect → discard and web-search**.


#### 6.8 Handling Lost in the Middle
LLMs use information at the start and end of the context well, but tend to miss the middle. Mitigations:
  * Place the most important documents at the **very beginning or very end**.
  * Don’t blindly raise top-k; keep it at 5–10.
  * Use a reranker to get the top-of-list ordering exactly right.
  * Use contextual compression to shrink the volume itself.


* * *
### Example 2: Advanced RAG
> Hybrid retrieval + Reranking + Multi-Query query transformation + contextual compression + forced citations + Self-Eval, all in one pipeline.

```
"""example_2_advanced_rag.py — production-shaped Advanced RAG"""
from __future__ import annotations
from typing import List
from dataclasses import dataclass

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.retrievers import BM25Retriever
from langchain.retrievers import EnsembleRetriever
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from sentence_transformers import CrossEncoder

# ════════════════════════════════════════════════════════════════
# 0. Data — six engineering policy documents
# ════════════════════════════════════════════════════════════════
KB = [
    {"source": "ENG/Coding_Standards.md",
     "content": "Python follows PEP 8 and the black formatter. Line length 100. Type hints on every "
                "public function. Function names snake_case, classes PascalCase, constants UPPER_SNAKE_CASE."},
    {"source": "ENG/Code_Review_Policy.md",
     "content": "PR merges require at least 2 approvals. One must be a senior. Security changes need "
                "additional approval from the security team. Recommended PR size 400 lines, ask for a "
                "split if it exceeds 1000. Reviews within 2 business days."},
    {"source": "ENG/Deploy_Process.md",
     "content": "Production deploys are Tue/Wed/Thu, 10:00–16:00. Forbidden on Fridays and the day "
                "before holidays. Validate on staging for 24 hours before deploying. Hotfixes can "
                "bypass the time restriction with CTO approval. Wait 30 minutes monitoring after deploy."},
    {"source": "ENG/On_Call_Policy.md",
     "content": "On-call rotates weekly. Target response: P1 within 15 minutes, P2 within 1 hour. "
                "Night (22:00–08:00) and weekend on-call earns extra hourly compensation. Vacations "
                "require a swap arranged in advance."},
    {"source": "ENG/Tech_Stack.md",
     "content": "Backend standard is Python 3.12 + FastAPI. DB: PostgreSQL 16, cache: Redis 7, "
                "MQ: RabbitMQ. Frontend TypeScript + React 18. AWS (ECS/RDS/S3) + Terraform."},
    {"source": "HR/Remote_Work.md",
     "content": "Full-timers can work from home twice a week. Manager approval required. Tue/Thu "
                "remote is discouraged. New hires come in every day for the first 3 months. Working "
                "abroad needs separate approval and tax review."},
]

# ════════════════════════════════════════════════════════════════
# 1. Indexing — for hybrid retrieval, build both Dense and BM25
# ════════════════════════════════════════════════════════════════
def build_retrievers():
    docs = [Document(page_content=d["content"], metadata={"source": d["source"]}) for d in KB]
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=350, chunk_overlap=70,
        separators=["\n\n", "\n", ". ", " ", ""])
    chunks = splitter.split_documents(docs)

    emb = HuggingFaceEmbeddings(
        model_name="BAAI/bge-m3", encode_kwargs={"normalize_embeddings": True})
    vectordb = Chroma.from_documents(chunks, emb, collection_name="adv_rag")

    dense = vectordb.as_retriever(search_kwargs={"k": 8})
    bm25 = BM25Retriever.from_documents(chunks); bm25.k = 8

    hybrid = EnsembleRetriever(retrievers=[bm25, dense], weights=[0.4, 0.6])
    return hybrid

# ════════════════════════════════════════════════════════════════
# 2. Query transformation — diversify with Multi-Query generation
# ════════════════════════════════════════════════════════════════
multi_query_prompt = ChatPromptTemplate.from_messages([
    ("system", "Rewrite the user's question into 3 retrieval queries that preserve the meaning "
               "but vary the wording and angle. One per line, no numbering."),
    ("human", "{question}")
])

llm = ChatAnthropic(model="claude-opus-4-7", temperature=0)

def multi_queries(question: str) -> List[str]:
    raw = (multi_query_prompt | llm).invoke({"question": question}).content
    qs = [q.strip("-•123456789. ").strip() for q in raw.split("\n") if q.strip()]
    return [question] + qs[:3]  # original + 3 variants

# ════════════════════════════════════════════════════════════════
# 3. Reranking — sort candidates with a cross-encoder
# ════════════════════════════════════════════════════════════════
class Reranker:
    def __init__(self, name="BAAI/bge-reranker-v2-m3"):
        self.m = CrossEncoder(name, max_length=512)

    def __call__(self, query: str, docs: List[Document], top_n=4) -> List[Document]:
        if not docs: return []
        scores = self.m.predict([(query, d.page_content) for d in docs])
        ranked = sorted(zip(scores, docs), key=lambda x: x[0], reverse=True)
        # Deduplicate by page_content
        seen, out = set(), []
        for s, d in ranked:
            if d.page_content in seen: continue
            seen.add(d.page_content)
            d.metadata["rerank_score"] = float(s)
            out.append(d)
            if len(out) == top_n: break
        return out

# ════════════════════════════════════════════════════════════════
# 4. Answer generation — forced citations
# ════════════════════════════════════════════════════════════════
answer_prompt = ChatPromptTemplate.from_messages([
    ("system",
     "ACME engineering assistant. Answer based only on the [reference documents] below.\n"
     "Rules:\n"
     "1) End every fact with a [number] citation.\n"
     "2) If multiple documents support a claim, cite all of them like [1][3].\n"
     "3) If the docs don't say, answer 'Not specified in the documents.'\n"
     "4) Keep it concise and to the point."),
    ("human", "[reference documents]\n{context}\n\n[question]\n{question}")
])

@dataclass
class Result:
    answer: str
    sources: List[Document]
    queries_used: List[str]

def make_ctx(docs: List[Document]) -> str:
    return "\n\n".join(
        f"[{i}] (source: {d.metadata['source']})\n{d.page_content}"
        for i, d in enumerate(docs, 1))

def advanced_rag(question: str, hybrid, reranker) -> Result:
    # ① Multi-Query transformation
    queries = multi_queries(question)

    # ② Hybrid search (per query variant)
    candidates: List[Document] = []
    seen = set()
    for q in queries:
        for d in hybrid.invoke(q):
            key = d.page_content
            if key not in seen:
                seen.add(key); candidates.append(d)

    # ③ Reranking (precise sort against the original question)
    top = reranker(question, candidates, top_n=4)

    # ④ Generate answer (forced citations)
    msg = answer_prompt.invoke({"context": make_ctx(top), "question": question})
    ans = llm.invoke(msg).content
    return Result(answer=ans, sources=top, queries_used=queries)

# ════════════════════════════════════════════════════════════════
# 5. Self-Evaluation — automatic faithfulness check
# ════════════════════════════════════════════════════════════════
judge_prompt = ChatPromptTemplate.from_messages([
    ("system", "Judge the faithfulness of a RAG answer. If every fact in the [answer] is supported "
               "by the [reference documents], return PASS; if any fact lacks support, FAIL. "
               "First line PASS/FAIL, the rest the reasoning."),
    ("human", "[reference documents]\n{context}\n\n[answer]\n{answer}\n\nVerdict:")
])

def judge(res: Result) -> str:
    msg = judge_prompt.invoke({"context": make_ctx(res.sources), "answer": res.answer})
    return llm.invoke(msg).content

# ════════════════════════════════════════════════════════════════
# 6. Run
# ════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    hybrid = build_retrievers()
    rerank = Reranker()

    for q in [
        "Who needs to approve a security-related PR merge?",
        "Can I push a hotfix on Friday afternoon?",
        "Can a new hire apply for remote work?",
        "What do we use for DB and cache?",
        "What's on the company lunch menu?",  # not in docs
    ]:
        print(f"\n{'='*72}\nQ: {q}")
        r = advanced_rag(q, hybrid, rerank)
        print(f"\nQuery variants: {r.queries_used}")
        print(f"\nRetrieved + reranked top-{len(r.sources)}:")
        for i, d in enumerate(r.sources, 1):
            print(f"  [{i}] {d.metadata['source']:28s}  "
                  f"score={d.metadata.get('rerank_score',0):+.2f}")
        print(f"\n> Answer:\n{r.answer}")
        print(f"\nSelf-Eval:\n{judge(r)}")

```

#### What’s better — versus Naive  
| Aspect  | Naive  | Advanced  |  
| --- | --- | --- |  
| Synonyms / paraphrases  | Weak  | Multi-Query + Hybrid handle it  |  
| Exact identifiers  | Weak  | Strong, thanks to BM25  |  
| Precise top-of-list ordering  | Plain cosine score  | Cross-encoder reranking  |  
| Answer verification  | None  | Citations + Self-Eval  |  
| Lost in the Middle  | Defenseless  | Reranking puts the right thing on top  |  
#### Limits (still hard at this stage)
  * **Multi-hop reasoning** : “What is the code review policy of the team that deployed most recently?” → no single chunk has the answer.
  * **Relational questions** : “Among people who worked on Project X, who collaborates with the security team?” → needs relationship traversal.


→ The next step, **Graph RAG** , exists to address this.
* * *
### 8. Graph RAG, in depth
Graph RAG **represents documents as an entity-relation graph instead of chunks, and retrieves over the graph**. The decisive moment for the field was Microsoft Research’s 2024 paper _“From Local to Global: A Graph RAG Approach”_.
#### 8.1 Why a graph — limits of vector RAG
Vector RAG can only find “this chunk is semantically close to this question.” It struggles with the following:
  * **Multi-hop** : “Where did Project Alpha’s PM work before?” → needs (project → PM → past employer) chained traversal.
  * **Relational queries** : “Which projects have John and Jane both worked on?” → needs the intersection of two people.
  * **Global understanding** : “Who are this company’s 5 most influential people?” → needs the structure of the whole graph.
  * **Time / causal chains** : “How did Event A end up affecting Event C?” → needs traversal through a causal graph.


For these, _the relationship itself is the information_. The answer might not be written verbatim in any one document — you have to _combine_ information from multiple sources.
#### 8.2 Core idea: the indexing stage
Extract **(subject, relation, object)** triples from documents and store them in a graph DB (Neo4j, Memgraph, NetworkX, etc.).

```
Document: "John is the CTO of ACME and leads Project Alpha.
           Jane is the security lead for Project Alpha."

Extracted triples:
  (John, IS_CTO_OF, ACME)
  (John, LEADS, Project Alpha)
  (Jane, IS_SECURITY_LEAD_OF, Project Alpha)

→ In the graph, "John" and "Jane" are 2-hop connected through "Project Alpha".
```

##### Extraction approaches
  * **LLM-based extraction** : prompt GPT/Claude with _“extract entities and relations from this document.”_ The most common.
  * **NER + Relation Extraction model** : dedicated models like spaCy + REBEL. Can be domain-tuned.
  * **Manual schema + parser** : in highly structured domains like healthcare or law.


##### Entity Resolution
Expressions like “John Smith”, “J. Smith”, “the CTO” can refer to the same person. Merging them into a single node is what makes or breaks graph quality. Usually handled with embedding-based clustering.
#### 8.3 Microsoft GraphRAG’s key innovation: community summaries
A bare graph alone is weak on “global” questions (understanding the whole). Microsoft GraphRAG:
  1. After building the graph, detects communities (densely connected node groups) with the **Leiden algorithm**.
  2. Generates **an LLM summary** for each community ahead of time.
  3. Global questions → map-reduce over the community summaries.
  4. Local questions → answer from the subgraph around the relevant entity.


This is the decisive difference between plain graph-traversal RAG and GraphRAG.
#### 8.4 Query stage: Local vs Global  
| Type  | Example  | How it’s handled  |  
| --- | --- | --- |  
| **Local**  | “What is John’s title?”, “Who’s on Project Alpha?”  | Identify the entity → BFS to an N-hop subgraph → summarize  |  
| **Global**  | “What are the 5 main issues for this org?”  | LLM merges all community summaries → map-reduce  |  
| **Drift**  | A blend of both  | Use both and combine  |  
#### 8.5 GraphRAG vs vector RAG hybrid
In practice, **Hybrid Graph RAG** is the standard.

```
[query]
    ├─→ entity extraction → graph traversal (relationship-based evidence)
    └─→ vector retrieval (semantic evidence)
         ↓
    [combine evidence + LLM answer]
```

  * The graph handles _relationships_ , vectors handle _content_.
  * LangChain’s `Neo4jVector` + `GraphCypherQAChain` combo is the canonical setup.
  * LlamaIndex’s `KnowledgeGraphIndex` + `VectorStoreIndex` combo is also popular.


#### 8.6 Comparison of major implementations  
| Implementation  | Notes  | Good for  |  
| --- | --- | --- |  
| **Microsoft GraphRAG**  | Most polished. Community summaries, Leiden clustering  | The “by-the-book” approach, large corpora  |  
|  **LightRAG** (HKU, 2024)  | Lighter and faster. Dual-level retrieval (low-level entities + high-level keywords)  | Quick builds  |  
| **LangChain + Neo4j**  | LLMGraphTransformer + GraphCypherQAChain  | Production, Cypher-based precise queries  |  
| **LlamaIndex KG Index**  | TripletExtractor + KnowledgeGraphIndex  | Fast prototyping  |  
| **NetworkX (in-memory)**  | No DB, learning/experimentation  | Example 3 in this guide  |  
#### 8.7 The real cost of Graph RAG
  * **Indexing cost balloons** : every document goes through an LLM for triple extraction → big token bill.
  * **Schema design** : deciding “what entity types? what relation types?” is hard.
  * **Graph operations** : you need ops experience for a separate DB like Neo4j.
  * **A failed entity resolution makes the graph fall apart** : handling synonyms is the make-or-break.


→ Hence the common practical ordering: _“Start with Advanced RAG, and add Graph RAG when relational questions actually start dominating.”_
* * *
### Example 3: Graph RAG
> No external DB like Neo4j — uses **NetworkX in-memory graph** to demonstrate the Graph RAG core flow (entity extraction → graph build → graph traversal → answer). In production, swap in Neo4j with LangChain’s `LLMGraphTransformer`.

```
"""example_3_graph_rag.py — mini GraphRAG over NetworkX"""
from __future__ import annotations
import json
from typing import List, Tuple, Dict, Set
from dataclasses import dataclass, field

import networkx as nx
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate

# ════════════════════════════════════════════════════════════════
# 0. Data — fictional company wiki rich in person/project/org relations
# ════════════════════════════════════════════════════════════════
DOCS = [
    "John Kim is the CTO of ACME and joined in 2019. Before that he was a senior engineer at "
    "BlueTech. He currently leads Project Alpha and concurrently serves as director of the "
    "Machine Learning Infrastructure team.",

    "Jane Park is the security lead at ACME and serves as the security owner for Project Alpha. "
    "She previously spent 10 years at SecureCorp, and was a colleague of John Kim back at BlueTech.",

    "Minsoo Lee is a senior engineer on ACME's Data Platform team. He owns the data pipeline for "
    "Project Alpha and reports directly to John Kim. He's also collaborating with Jane Park on a "
    "security audit.",

    "Jihoon Choi is the PM for Project Beta. Beta aims to build a new payments system, and "
    "Minsoo Lee is partially involved in Beta as well, supporting the data migration.",

    "Project Alpha is ACME's next-generation recommendation system, started in January 2024. "
    "Project Beta is the payments system project, started in June 2024. "
    "Both projects are supported by the Machine Learning Infrastructure team.",
]

# ════════════════════════════════════════════════════════════════
# 1. Extract entity/relation triples with the LLM
# ════════════════════════════════════════════════════════════════
llm = ChatAnthropic(model="claude-opus-4-7", temperature=0)

extract_prompt = ChatPromptTemplate.from_messages([
    ("system",
     "Extract entities and relations from the following document and output them as a JSON list of triples.\n"
     "Each triple is in the form {\"s\": subject, \"r\": relation, \"o\": object}.\n"
     "Entities should be clear concrete things only — people, organizations, projects, roles.\n"
     "Relations should be short verb phrases (e.g., WORKS_AT, LEADS, IS_CTO_OF, REPORTS_TO, COLLABORATES_WITH).\n"
     "Normalize different mentions of the same person to one name.\n"
     "Output pure JSON array only, no other text."),
    ("human", "{document}")
])

def _safe_json_parse(text: str, default):
    """Extract just the JSON portion from the LLM response (strip markdown fences, etc.)"""
    import re
    m = re.search(r"(\[.*\]|\{.*\})", text, re.DOTALL)
    if not m:
        return default
    try:
        return json.loads(m.group(1))
    except json.JSONDecodeError:
        return default

def extract_triples(doc: str) -> List[Dict]:
    raw = (extract_prompt | llm).invoke({"document": doc}).content
    return _safe_json_parse(raw, default=[])

# ════════════════════════════════════════════════════════════════
# 2. Build a NetworkX graph (+ index of source documents)
# ════════════════════════════════════════════════════════════════
@dataclass
class KnowledgeGraph:
    G: nx.MultiDiGraph = field(default_factory=nx.MultiDiGraph)
    # entity → set of source document indices it appears in
    ent2docs: Dict[str, Set[int]] = field(default_factory=dict)
    docs: List[str] = field(default_factory=list)

def build_kg(docs: List[str]) -> KnowledgeGraph:
    kg = KnowledgeGraph(docs=docs)
    for i, d in enumerate(docs):
        triples = extract_triples(d)
        for t in triples:
            s, r, o = t.get("s"), t.get("r"), t.get("o")
            if not (s and r and o): continue
            kg.G.add_edge(s, o, relation=r, doc_idx=i)
            kg.ent2docs.setdefault(s, set()).add(i)
            kg.ent2docs.setdefault(o, set()).add(i)
    return kg

# ════════════════════════════════════════════════════════════════
# 3. Extract entities from the query
# ════════════════════════════════════════════════════════════════
query_ent_prompt = ChatPromptTemplate.from_messages([
    ("system", "Extract only the entities (people, organizations, projects, roles) mentioned in the question, "
               "as a JSON array. e.g., [\"John Kim\", \"Project Alpha\"]. No other text."),
    ("human", "{question}")
])

def extract_query_entities(q: str) -> List[str]:
    raw = (query_ent_prompt | llm).invoke({"question": q}).content
    return _safe_json_parse(raw, default=[])

# ════════════════════════════════════════════════════════════════
# 4. Graph traversal — N-hop subgraph around the query entities
# ════════════════════════════════════════════════════════════════
def find_node(kg: KnowledgeGraph, name: str) -> str | None:
    """Try exact match first, then fall back to substring matching"""
    if name in kg.G: return name
    for n in kg.G.nodes:
        if name in n or n in name:
            return n
    return None

def subgraph_around(kg: KnowledgeGraph, entities: List[str], hops: int = 2) -> Tuple[nx.MultiDiGraph, Set[int]]:
    """Subgraph collected from the N-hop neighborhood of the seed query entities + related document indices"""
    seed_nodes = {n for e in entities if (n := find_node(kg, e))}
    if not seed_nodes:
        return nx.MultiDiGraph(), set()

    # Convert to undirected for bidirectional BFS
    undirected = kg.G.to_undirected()
    visited = set(seed_nodes)
    frontier = set(seed_nodes)
    for _ in range(hops):
        next_frontier = set()
        for n in frontier:
            if n not in undirected: continue
            next_frontier.update(undirected.neighbors(n))
        frontier = next_frontier - visited
        visited |= frontier

    sub = kg.G.subgraph(visited).copy()
    # Collect related document indices
    doc_ids = set()
    for n in visited:
        doc_ids.update(kg.ent2docs.get(n, set()))
    return sub, doc_ids

def serialize_subgraph(sub: nx.MultiDiGraph) -> str:
    """Convert the subgraph into text to pass to the LLM"""
    if sub.number_of_edges() == 0:
        return "(no related graph)"
    lines = []
    for u, v, data in sub.edges(data=True):
        lines.append(f"({u}) -[{data['relation']}]-> ({v})")
    return "\n".join(sorted(set(lines)))

# ════════════════════════════════════════════════════════════════
# 5. Answer generation — feed both the graph and source docs as context
# ════════════════════════════════════════════════════════════════
graph_answer_prompt = ChatPromptTemplate.from_messages([
    ("system",
     "You are an internal knowledge assistant. Answer based only on the [knowledge graph] and [source documents] below.\n"
     "- Walk the graph relationships to perform multi-hop reasoning.\n"
     "- Cite the relations you used in the form (A) -[relation]-> (B).\n"
     "- If evidence is insufficient, answer 'Cannot be answered with the provided information.'"),
    ("human",
     "[knowledge graph]\n{graph}\n\n[source documents]\n{docs}\n\n[question]\n{question}")
])

def graph_rag(question: str, kg: KnowledgeGraph) -> str:
    ents = extract_query_entities(question)
    sub, doc_ids = subgraph_around(kg, ents, hops=2)

    graph_text = serialize_subgraph(sub)
    doc_text = "\n\n".join(f"[doc{i}] {kg.docs[i]}" for i in sorted(doc_ids)) or "(no related documents)"

    print(f"  · Query entities: {ents}")
    print(f"  · Subgraph nodes {sub.number_of_nodes()}, edges {sub.number_of_edges()}")
    print(f"  · Related source docs: {sorted(doc_ids)}")

    msg = graph_answer_prompt.invoke({
        "graph": graph_text, "docs": doc_text, "question": question})
    return llm.invoke(msg).content

# ════════════════════════════════════════════════════════════════
# 6. Run
# ════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("[1/3] Building the graph...")
    kg = build_kg(DOCS)
    print(f"     done. nodes {kg.G.number_of_nodes()}, edges {kg.G.number_of_edges()}\n")

    # Preview the graph
    print("[2/3] Extracted triples (full):")
    for u, v, data in kg.G.edges(data=True):
        print(f"     ({u}) -[{data['relation']}]-> ({v})  (doc{data['doc_idx']})")

    # Questions that genuinely need multi-hop
    print("\n[3/3] Graph RAG Q&A:")
    for q in [
        # 1-hop: simple fact
        "Which company is John Kim CTO of?",
        # 2-hop: multi-hop — who from Kim's previous workplace are colleagues with him?
        "How do Jane Park and John Kim know each other?",
        # Relational intersection: a project both work on
        "Where do Minsoo Lee and Jane Park work together?",
        # Multi-hop + aggregation: one person across multiple projects
        "Which projects is Minsoo Lee involved in, and who are the other key members of those projects?",
        # Information not in the graph
        "What is John Kim's salary?",
    ]:
        print(f"\n━━━ Q: {q}")
        print(f"> {graph_rag(q, kg)}")

```

#### What this shows
This small example covers all four core stages of Graph RAG.
  1. **Entity/relation extraction** — generate triples with the LLM (in production you’d index once and cache).
  2. **Graph construction** — NetworkX in-memory (abstract enough to swap in Neo4j).
  3. **Graph traversal** — query entities → 2-hop subgraph + related documents.
  4. **Answer generation** — both the graph _and_ the source docs are in the context.


In particular, _“How do Jane Park and John Kim know each other?”_ is a question with no answer in any single chunk — it’s only answerable because the graph connects them through _BlueTech_ as a common node. Vector RAG would have a very hard time with that kind of question.
#### Going to production  
| Component  | This example  | Production  |  
| --- | --- | --- |  
| Graph storage  | NetworkX (in-memory)  | Neo4j, Memgraph, NebulaGraph  |  
| Triple extraction  | LLM call on the spot  | LangChain `LLMGraphTransformer`, cached  |  
| Entity resolution  | Substring matching  | Embedding clustering + human review  |  
| Querying  | BFS subgraph  | Auto-generated Cypher (`GraphCypherQAChain`)  |  
| Global queries  | Not supported  | Community detection + summarization (Microsoft GraphRAG)  |  
| Evaluation  | Manual  | RAGAS graph evaluation + a golden set  |  
Migrating to LangChain takes essentially two lines.

```
from langchain_neo4j import Neo4jGraph
from langchain_experimental.graph_transformers import LLMGraphTransformer

graph = Neo4jGraph(url=..., username=..., password=...)
transformer = LLMGraphTransformer(llm=llm)
graph_documents = transformer.convert_to_graph_documents(docs)
graph.add_graph_documents(graph_documents)

```

After that, `GraphCypherQAChain` translates natural-language questions into Cypher and queries Neo4j directly.
* * *
## Part III — Operations and decisions
### 10. Evaluation methods and metrics
You should evaluate **retrieval quality** and **generation quality** separately for RAG.
#### 10.1 Retrieval metrics  
| Metric  | What it measures  |  
| --- | --- |  
| **Recall@K**  | Did the correct document make it into the top K?  |  
| **Precision@K**  | Of the top K, what fraction are correct?  |  
|  **MRR** (Mean Reciprocal Rank)  | Average of the inverse rank at which the first correct result appears  |  
| **nDCG@K**  | Rank-weighted normalized score  |  
| **Hit Rate@K**  | 1 if _any_ correct result is in the top K  |  
#### 10.2 Generation metrics  
| Metric  | What it measures  |  
| --- | --- |  
| **Faithfulness**  | Does the answer stay faithful to the retrieved context (i.e., not hallucinate)?  |  
| **Answer Relevance**  | Does the answer fit the question?  |  
| **Context Precision**  | What fraction of the context was actually used in the answer?  |  
| **Context Recall**  | Is all the information needed for the correct answer present in the context?  |  
| **Answer Correctness**  | Factual accuracy compared to ground truth  |  
#### 10.3 Tools
  * **RAGAS** : the most common RAG evaluation framework, LLM-as-judge based.
  * **TruLens** : tracing + evaluation in one.
  * **DeepEval** : unit-test style, integrates well with pytest.
  * **ARES** : automated RAG evaluation, leverages synthetic datasets.


#### 10.4 RAGAS usage example (quick)

```
from ragas import evaluate
from ragas.metrics import faithfulness, answer_relevancy, context_precision, context_recall
from datasets import Dataset

eval_data = Dataset.from_dict({
    "question": ["How many days off for a parent's 60th birthday in my first year?"],
    "answer": ["It's a general family event, so it doesn't qualify for special leave and must be taken as annual leave [HR/special_leave.md]."],
    "contexts": [["Family events such as a parent's 60th or 70th birthday do not qualify for special leave and must be taken as annual leave."]],
    "ground_truth": ["It must be taken as annual leave."],
})

result = evaluate(eval_data, metrics=[
    faithfulness, answer_relevancy, context_precision, context_recall])
print(result)

```

#### 10.5 What to monitor in production
  * Retrieval recall / hit rate (daily batch over a golden set)
  * Context utilization rate (cited / retrieved)
  * Hallucination rate (LLM-as-judge estimate)
  * Response latency (P50, P95, P99)
  * Tokens / cost per query
  * User feedback (thumbs up/down + free-text)
  * Index freshness (last update timestamp)


* * *
### 11. Recent trends (2024–2026)
#### 11.1 The rise of Agentic RAG (2024 ~ )
The biggest current. The shift is from **“retrieve once and answer”** to **“an agent orchestrates retrieval.”**
  * The model decides whether to retrieve at all (Self-RAG).
  * If results are weak, augment or discard them (CRAG).
  * Pick the right tool for the situation (vector / SQL / web / API).
  * Interleave reasoning steps with retrieval (ReAct).


#### 11.2 GraphRAG and structured retrieval (2024)
Microsoft GraphRAG drove home the idea that _“vectors alone are weak on global understanding and multi-hop.”_ Follow-up research like LightRAG and HippoRAG is active.
#### 11.3 Contextual Retrieval (Anthropic, 2024)
The LLM stamps each chunk with its document-level context. Retrieval failure rate drops 35–67%. Combined with **prompt caching** , the cost overhead is small.
#### 11.4 Long Context vs RAG (debate, settled)
When Gemini, Claude, and GPT started supporting 1M+ tokens, the “RAG is dead” claim went around. In practice:
  * Cost (running 1M tokens every time isn’t realistic).
  * Lost in the Middle still happens.
  * Freshness — RAG wins on real-time updates.
  * Permissions — per-user separation lives most naturally at the retrieval step.


→ Conclusion: **RAG is alive, and Long Context is being used to extend RAG’s context window.**
#### 11.5 CAG / TAG / KAG  
| Acronym  | Expansion  | Core idea  |  
| --- | --- | --- |  
| **CAG**  | Cache-Augmented Generation  | Pre-load frequently used knowledge into the KV cache  |  
| **TAG**  | Table-Augmented Generation  | Combine tabular data with SQL/SPJ-style operators  |  
| **KAG**  | Knowledge-Augmented Generation  | Reasoning powered by knowledge graphs  |  
The trend is clear: **“Don’t try to solve everything with one RAG — combine the augmentation style that fits the data.”**
#### 11.6 Multimodal RAG
Expanding retrieval to images, tables, charts, audio, and video. Multimodal embeddings like CLIP, BLIP-2, and **ColPali** (which vectorizes the document image itself) are evolving fast. Big payoff in domains heavy with PDF tables and charts (finance, healthcare).
#### 11.7 Small LLMs + RAG
7B–13B open models with a well-designed RAG pipeline now match or come close to GPT-4 alone in many cases. Strong on cost, privacy, and on-prem deployments.
* * *
### 12. Limits and alternatives
#### 12.1 Inherent limits of RAG  
| Limit  | Description  |  
| --- | --- |  
| Retrieval is the ceiling  | If retrieval is wrong, the answer is wrong. Garbage in, garbage out.  |  
| Chunking is arbitrary  | When chunk boundaries don’t match meaning, information gets split  |  
| Weak on multi-hop  | Plain retrieval isn’t enough for chained reasoning → need Graph RAG  |  
| Context cost  | Increasing top-k raises cost and latency  |  
| Inconsistency  | Even small retrieval differences can shift the answer for the same question  |  
| Can’t learn reasoning  | RAG can’t change the model’s reasoning _style_ (that’s what fine-tuning is for)  |  
| Security: prompt injection  | If a malicious prompt sneaks into a retrieved doc, the LLM can be hijacked  |  
| Security: permission leaks  | A wrong per-user permission split leaks data  |  
#### 12.2 Alternatives
##### Fine-tuning  
| Aspect  | RAG  | Fine-tuning  |  
| --- | --- | --- |  
| Knowledge updates  | Immediate  | Re-training required  |  
| Hallucination control  | Strong (citations)  | Weak  |  
| Sourcing  | Yes  | No  |  
| Style / tone learning  | Weak  | Strong  |  
| Reasoning patterns  | No  | Yes  |  
→ **They aren’t substitutes; they complement each other.** Fine-tune for style/format/reasoning; RAG for factual knowledge.
##### Long Context (skip retrieval, just stuff it all in)
If documents are few and you reuse the same material, plain long context can beat RAG. Analyzing one book, reviewing a single contract, etc.
##### Knowledge Graph / Text-to-SQL
If the data is enterprise-style with _structured relationships_ , auto-generating SQL/Cypher is more accurate than RAG. “Top 5 customers by revenue last quarter” → SQL is the right answer.
##### Tool Use / Function Calling
Replace retrieval with another tool. “Current exchange rate?” → call a forex API.
##### Cache / rules
Pre-cache answers to common questions, or use rule-matching. 90% of an FAQ is often covered by 100 canned answers.
#### 12.3 Recommended in practice: hybrid routing

```
user question
    ↓
[1] cache / FAQ match → respond immediately on hit
    ↓ (cache miss)
[2] intent classifier
    ├─ structured / numeric / aggregate → SQL / API
    ├─ relational reasoning → Graph RAG
    ├─ unstructured docs → Advanced RAG (Hybrid + Rerank)
    └─ general chat → bare LLM
    ↓
[3] answer + citations + guardrails
    ↓
[4] evaluation + logging + feedback loop
```

* * *
### 13. Three-way comparison and decision guide
#### 13.1 Naive vs Advanced vs Graph at a glance  
| Aspect  | Naive RAG  | Advanced RAG  | Graph RAG  |  
| --- | --- | --- | --- |  
| **Data representation**  | Chunks + embeddings  | Chunks + embeddings + metadata  | Nodes + edges (+ embeddings)  |  
| **Retrieval**  | Vector similarity  | Hybrid + Rerank  | Graph traversal (+ vectors)  |  
| **Query transformation**  | None  | Multi-Query, HyDE, etc.  | Entity extraction + Cypher  |  
| **Multi-hop**  | No  | Sort of  | Yes  |  
| **Global understanding**  | No  | Sort of  | Yes (community summaries)  |  
| **Implementation effort**  | Low  | Medium  | Very high  |  
| **Indexing cost**  | Low  | Medium  | High (LLM triple extraction)  |  
| **Operational cost**  | Low  | Medium  | High (graph DB to operate)  |  
| **Best-fit data**  | General docs, FAQ  | Tech docs, internal wiki  | People, orgs, events, relations  |  
#### 13.2 One-line decision guide
> **“Where does the answer live?”**
>   * In unstructured documents → **Advanced RAG**
>   * In the _relationships between_ documents → **Graph RAG**
>   * In a structured DB → **Text-to-SQL**
>   * In the model weights → **Fine-tuning**
>   * In an external API/tool → **Tool Use**
>   * The same short reference every time → **Long Context**
>   * Personal/research knowledge that _accumulates over time_ → **LLM Wiki** (§16)
> 

#### 13.3 Recommended adoption order
The order I recommend for most organizations:
  1. **PoC with Naive RAG** — 1–2 weeks. Understand what’s possible and where it breaks.
  2. **Ship Advanced RAG** — Hybrid + Rerank + forced citations.
  3. **Build an evaluation set + monitoring** — golden set of 100–200, RAGAS automated evaluation.
  4. **Add Graph RAG once relational questions get common** — usually as a 30–50% complement to Advanced.
  5. **Expand to Modular/Agentic** — routing, tool calls, Self-RAG/CRAG.


* * *
### 14. Production checklist
#### 14.1 Design
  * Use case is defined (Q&A? summarization? analysis?)
  * You’ve mapped where the answer lives (docs? DB? API? relationships?)
  * Data permission and security model defined
  * Update cadence defined
  * Golden set of 100–200 examples for evaluation


#### 14.2 Indexing
  * Loaders cover all the formats you need
  * Strategy for tables and images (Unstructured, LlamaParse, etc.)
  * Metadata schema standardized
  * Chunking parameters tuned per domain
  * Embedding model fit for your language/domain confirmed
  * Vector DB backup / rollback
  * (Graph) Entity resolution procedure


#### 14.3 Retrieval
  * Plan to expand from Dense-only to Hybrid in stages
  * BM25 index operated separately
  * Reranker introduced (with the accuracy/cost trade-off considered)
  * Metadata filtering
  * MMR for diversity
  * (Graph) Auto-generated Cypher validated


#### 14.4 Generation
  * “If there’s no evidence, say you don’t know” prompt
  * Forced citations
  * Refusal policy
  * Guardrails (PII, inappropriate content)
  * Prompt-injection defense (don’t interpret retrieved doc content as system instructions)


#### 14.5 Operations
  * Retrieval metrics (Recall@K, MRR)
  * Generation metrics (Faithfulness, Relevance)
  * Response latency P95
  * Token cost tracking
  * User feedback + retraining loop
  * Index freshness
  * Automated regression tests


* * *
### 15. Setting up your environment
To run all three examples in this document (`example_1_naive_rag`, `example_2_advanced_rag`, `example_3_graph_rag`):
#### 15.1 venv + packages

```
python3 -m venv .venv && source .venv/bin/activate

pip install \
  langchain>=0.3.0 \
  langchain-community>=0.3.0 \
  langchain-anthropic>=0.3.0 \
  langchain-text-splitters>=0.3.0 \
  langchain-experimental>=0.3.0 \
  chromadb>=0.5.0 \
  sentence-transformers>=3.0.0 \
  rank_bm25>=0.2.2 \
  networkx>=3.2 \
  tiktoken>=0.7.0

```

#### 15.2 API key

```
export ANTHROPIC_API_KEY="sk-ant-..."

```

#### 15.3 Auto-downloaded on first run
  * `BAAI/bge-m3` (embedding, ~2.3GB)
  * `BAAI/bge-reranker-v2-m3` (reranker, ~600MB)


These run on CPU without a GPU, though the reranker can be a bit slow on CPU.
#### 15.4 If you’d rather split the code into files
Save the code blocks in this document as `example_1_naive_rag.py`, `example_2_advanced_rag.py`, `example_3_graph_rag.py`, `example_4_llm_wiki.py`, then:

```
python example_1_naive_rag.py
python example_2_advanced_rag.py
python example_3_graph_rag.py
python example_4_llm_wiki.py

```

* * *
## Part IV — Beyond RAG
### 16. LLM Wiki: a knowledge system that _accumulates_ instead of retrieving
Every flavor of RAG we’ve covered so far (Naive, Advanced, Graph) shares one thing.
> **Every question rederives knowledge from scratch.**
Whether there are 5 chunks or 100,000, whether the graph has 10 nodes or 10,000, the LLM repeats _retrieve → read → synthesize_ on every query. In other words, **knowledge is _re-derived_ at retrieval time**. Asking the same question twice does the same work twice. Insights, syntheses, contradictions discovered in earlier queries don’t accumulate anywhere.
**LLM Wiki** is a different idea.
> **Knowledge is _compiled_ once into a set of markdown files, and incrementally _maintained_ as new material comes in. The LLM is no longer the retriever — it’s the wiki editor.**
This isn’t a variant of RAG; it’s a different paradigm. It’s spreading quickly thanks to the rise of **agentic tools that write directly to the file system** — Claude Code, OpenAI Codex, and friends.
A key quote:
> _“The wiki is a persistent compounding artifact. The cross-references are already there. The contradictions are already flagged. The synthesis already reflects all the material.”_
#### 16.1 RAG vs LLM Wiki — the essential difference  
| Aspect  | RAG  | LLM Wiki  |  
| --- | --- | --- |  
| Form of knowledge  | Chunks + embeddings (for retrieval)  | Structured markdown pages  |  
| **Accumulation**  | None — re-derive every query  | Yes — incremental  |  
| Cross references  | Attempted at query time  | Pre-existing as explicit wikilinks  |  
| Contradiction detection  | Hard  | Caught automatically by lint  |  
| Synthesis / consolidation cost  | Every query  | Once at indexing  |  
| When the LLM is called  | Every query  | Indexing + query  |  
| Human readability  | Almost no one reads chunks  | The wiki itself is _a readable artifact_  |  
| Scale  | Thousands to millions of docs  | Tens to hundreds of sources  |  
| Pattern maturity  | Very mature (since 2020)  | Emerging (since 2024)  |  
| Determinism  | Relatively high  | Low (page structure varies between runs)  |  
**Key insight** : every cross-reference, contradiction flag, and synthesis in the wiki _is reused by the next query as-is_. The wiki gets richer as you add material, and queries get faster and more accurate.
#### 16.2 Three-layer architecture

```
┌─────────────┐
│  Raw source │  Immutable. Curated by the user. (PDFs, markdown, images, data)
└──────┬──────┘
       │  LLM only reads
       ▼
┌─────────────┐
│   Wiki      │  *Wholly owned* by the LLM. Pages written, updated, cross-linked.
│  (markdown) │  You read; the LLM writes.
└──────┬──────┘
       │  Defines rules
       ▼
┌─────────────┐
│  Schema     │  CLAUDE.md / AGENTS.md.
│ (meta doc)  │  Rules for "how to maintain this wiki." Co-evolved by user and LLM.
└─────────────┘
```

  * **Raw** : source of truth. The LLM only reads from it, never modifies it.
  * **Wiki** : indexes, entity pages, concept pages, syntheses, comparison tables. A git repo of markdown files.
  * **Schema** : the meta document that teaches the LLM _“this is how the wiki is laid out, this is what to do when a new source arrives.”_ Co-evolved by user and LLM over time. **This is the key configuration file** — it’s what makes the difference between a generic chatbot and a wiki maintainer.


#### 16.3 Core operations — Ingest / Query / Lint
##### Ingest (intake)
When a new source is added to raw:
  1. The LLM reads the material and discusses key points with the user.
  2. Writes a _summary page_ in the wiki.
  3. Updates the _index_.
  4. Updates every affected _entity / concept page_ (sometimes touching 10–15 files at once).
  5. Adds one line to the _log_.


> Touching 15 pages while ingesting one source is the essence of LLM Wiki. A human would never do this (it’s too tedious to bother with). The LLM doesn’t get tired, so it does.
##### Query (asking)
  * Index → pick relevant pages → read pages → cite-rich answer.
  * **Important insight** : _a good answer can be saved back into the wiki as a new page._ Comparisons, analyses, connections you discover shouldn’t disappear into chat history — they should become wiki assets. This way _exploration itself accumulates._


##### Lint (wiki health check)
Periodically have the LLM audit the wiki:
  * Contradictions between pages
  * Stale claims that new material should have updated
  * _Orphan pages_ with no inbound links
  * _Important concepts_ that recur but lack their own page
  * Missing cross references
  * _Data gaps_ that could be filled by web search


LLMs are good at suggesting questions to investigate further and what material to look for. Lint keeps the wiki healthy.
#### 16.4 Index and log
As the wiki grows, two special files become the LLM’s compass.  
| File  | Nature  | Role  |  
| --- | --- | --- |  
| **index.md**  | Content-oriented  | Catalog of every page (link + one-line summary + metadata). Organized by category. _Updated on every ingest._ At query time, the LLM reads the index first and drills down.  |  
| **log.md**  | Time-oriented  | Append-only. Records ingest/query/lint. With a consistent prefix like `## [2026-04-02] ingest | article title`, you can pull the last 5 entries with `grep "^## \[" log.md | tail -5`.  |  
Up to a few hundred pages, **the index file alone is enough** — no need for embedding-RAG infrastructure. That’s one of the reasons LLM Wiki beats RAG at small scale.
#### 16.5 RAG vs LLM Wiki — when to use which?  
| Situation  | Recommended  | Why  |  
| --- | --- | --- |  
| Tens of thousands to millions of docs, lots of one-off queries  | **RAG**  | Compilation cost wouldn’t pay off  |  
| Tens to hundreds of sources, deeply accumulating topic  | **LLM Wiki**  | Synthesis and cross-references are valuable  |  
| Reading a single book with a companion wiki  | **LLM Wiki**  | Incremental accumulation is the point  |  
| One person’s long-term research (months to years)  | **LLM Wiki**  | Avoids re-deriving every time  |  
| Internal wiki (frequently updated, many users)  | **Both**  | Use the compiled wiki as the RAG source  |  
| Real-time changing data (stock prices, logs)  | **RAG / tool calls**  | Compilation can’t keep up  |  
| Evaluation / reproducibility matters  | **RAG**  | More deterministic  |  
| Permission separation is core  | **RAG**  | Permissions live naturally at the indexing stage  |  
##### Good fits in practice
  * **Personal** : tracking your own goals, health, psychology, growth. Build a structured picture of _yourself_ over time, from journals, articles, and podcast notes.
  * **Research** : a single topic over weeks or months. Papers, articles, and reports → an evolving synthesis wiki.
  * **Reading a book deeply** : index by chapter, auto-create person/theme/plot pages. End of the book = a _Tolkien Gateway_ -style companion wiki.
  * **Company/team** : Slack threads, meeting notes, project docs, customer calls → an internal wiki maintained by the LLM, reviewed by humans. The wiki is _always current_ — the LLM does the maintenance no one wants to do.
  * **Competitive analysis, due diligence, trip planning, lecture notes, deep-dives into a hobby** — _anything that gains value as it accumulates and gets organized over time._


#### 16.6 Tool ecosystem  
| Tool  | Role  |  
| --- | --- |  
| **Obsidian**  | The wiki IDE. Graph view, wikilink autocompletion, Dataview plugin  |  
| **Obsidian Web Clipper**  | Web page → markdown (browser extension)  |  
| **Marp**  | Markdown-based slides (Obsidian plugin available) — turn a wiki page directly into a deck  |  
| **qmd**  | Local search engine for a markdown folder. BM25 + vector + LLM rerank. CLI + MCP server  |  
| **git**  | A wiki is just a markdown git repo. Free version control, branching, collaboration  |  
| **Claude Code / Codex**  | Agents that write directly to the file system. The best fit for LLM Wiki  |  
> The typical workflow: **LLM agent on one side, Obsidian on the other.** The LLM edits files based on the conversation, and the human watches the result in real time — following links, scanning the graph view, reading freshly-updated pages. **Obsidian is the IDE, the LLM is the programmer, the wiki is the codebase.**
#### 16.7 Why it works — the connection to Memex
The real difficulty of maintaining a knowledge base isn’t _reading_ or _thinking_ — it’s _bookkeeping_. Updating cross-references, refreshing summaries, noting contradictions, keeping dozens of pages consistent. Humans give up on wikis — _the maintenance cost grows faster than the value._
LLMs don’t get bored, don’t forget cross-references, and can touch 15 files at once. **The maintenance cost is near-zero, so the wiki survives.**
This connects directly to **Vannevar Bush’s 1945 Memex** vision — a personally curated knowledge store with _associative trails_ between documents. Bush couldn’t solve _“who does the maintenance.”_ **The LLM is the answer.**
#### 16.8 Limits of LLM Wiki
  * **Low determinism** : running the same ingest twice produces subtly different page structure — hard to evaluate or reproduce.
  * **Schema drift** : weak explicit rules and page formats lose consistency → regular lint is essential.
  * **Token cost beyond a few hundred sources** : every ingest needs to show many pages to the LLM in context → cost adds up.
  * **Depends on the user** : a good wiki comes from good curation and good questions. There’s a limit to what automation can do.
  * **Multi-user / permissions** : permission separation at the index stage isn’t as natural as in RAG.
  * **Search precision** : at scale, vector search beats an index file.


#### 16.9 Wiki + RAG combined (the realistic endpoint)
The most interesting evolution: **“use the LLM-maintained wiki itself as the RAG source.”**

```
[Raw source]
    │
    │  LLM compiles (Ingest)
    ▼
[Wiki markdown] ◀── humans read directly (Obsidian)
    │
    │  RAG indexing
    ▼
[Vector DB / BM25]
    │
    │  search
    ▼
[Fast Q&A]
```

  * You get _depth_ (the wiki’s synthesis) and _speed_ (RAG’s retrieval).
  * The most realistic endpoint for an internal wiki system.
  * The wiki is _directly readable and reviewable by humans_ — lower hallucination risk than RAG alone.


* * *
### Example 4: LLM Wiki
> No external tools — just **Python + the Anthropic API + the file system** to demonstrate the LLM Wiki pattern (ingest → auto-write/update pages → maintain index/log → query). By indexing three time-ordered documents from a fictional company, you can watch the wiki grow richer firsthand.

```
"""example_4_llm_wiki.py — minimal LLM Wiki implementation
==================================================
A single file demonstrates:
  1) Sequentially ingesting 3 time-ordered sources
  2) On each ingest, the LLM creates/updates entities/projects/concepts pages
  3) Auto-maintaining index.md / log.md
  4) Time-evolution queries against the wiki itself as context
"""
from __future__ import annotations
import json, re, datetime, shutil
from pathlib import Path
from typing import Dict
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate

# ════════════════════════════════════════════════════════════════
# 0. Sample raw sources — 3 time-ordered docs from a fictional company
# ════════════════════════════════════════════════════════════════
SAMPLE_SOURCES = {
    "2024Q3_strategy.md": """# Q3 2024 Strategy Meeting Summary

Q3 priorities announced by CTO John Kim:
1. Project Alpha (recommendation system overhaul) targeted for November launch
2. Data infrastructure team headcount up 50%
3. Stronger collaboration with the security team

Jane Park joins Project Alpha as security owner.
Minsoo Lee owns the data pipeline.""",

    "2024Q4_alpha_launch.md": """# Project Alpha Launch Retrospective (2024-11-30)

Launched Nov 15. Traffic up 30%, click-through up 12%.

Key contributors:
- John Kim (overall lead)
- Jane Park (security review)
- Minsoo Lee (data pipeline)
- Hyunwoo Jung (UI/UX, new joiner)

Failure mode: an early cache miss spike → resolved by scaling out the Redis cluster
Next: kick off Project Beta (payments system).""",

    "2025Q1_orgchange.md": """# Org Changes, January 2025

- John Kim: stays as CTO. Concurrently director of the Machine Learning Infrastructure team
- Jane Park: promoted to security team lead
- Minsoo Lee: promoted to Data Platform team lead
- Hyunwoo Jung: moves from the Alpha team to the Beta team
- Jihoon Choi: joins as PM of the Beta team (external hire)

Project Alpha shifts to maintenance mode. Project Beta becomes the new top priority."""
}

# ════════════════════════════════════════════════════════════════
# 1. Prompts — Ingest (action plan) / Query
# ════════════════════════════════════════════════════════════════
INGEST_PROMPT = ChatPromptTemplate.from_messages([
    ("system",
     "You are a wiki editor. Looking at a new source document, you decide how to update wiki pages.\n"
     "You'll receive every existing wiki page along with its content.\n\n"
     "Output must be a pure JSON array (no other explanation):\n"
     '  [{"op":"create","path":"entities/john_kim.md","content":"full markdown"},\n'
     '   {"op":"append","path":"projects/alpha.md","content":"markdown to append"}]\n\n'
     "Rules:\n"
     "- People: entities/<name>.md   Projects: projects/<name>.md   Concepts: concepts/<name>.md\n"
     "- Only act when there's new info. If purely duplicate, return an empty array.\n"
     "- In page bodies, use [[Other_Page_Name]] wikilinks generously.\n"
     "- End each page with '> source: [source_filename]' (also when appending).\n"
     "- If you find contradictions, add a 'TODO: review contradiction — ...' note."),
    ("human",
     "[new source: {source_name}]\n{source_text}\n\n"
     "[current wiki]\n{existing_pages}\n\n"
     "Action JSON array to reflect this source:")
])

QUERY_PROMPT = ChatPromptTemplate.from_messages([
    ("system",
     "You are a wiki assistant. Answer questions based only on the [wiki pages] below.\n"
     "Cite the source page after each fact in [[Page Name]] form.\n"
     "If evidence is insufficient, answer 'The wiki doesn't have enough information.'"),
    ("human", "[wiki pages]\n{pages}\n\n[question]\n{question}")
])


# ════════════════════════════════════════════════════════════════
# 2. WikiAgent — core logic
# ════════════════════════════════════════════════════════════════
class WikiAgent:
    def __init__(self, root: str):
        self.root = Path(root)
        self.raw_dir = self.root / "raw"
        self.wiki_dir = self.root / "wiki"
        self.llm = ChatAnthropic(model="claude-opus-4-7", temperature=0)

    # ── Setup: directories + sample sources + empty index/log ──
    def setup(self):
        if self.root.exists():
            shutil.rmtree(self.root)
        self.raw_dir.mkdir(parents=True)
        self.wiki_dir.mkdir(parents=True)
        for name, content in SAMPLE_SOURCES.items():
            (self.raw_dir / name).write_text(content, encoding="utf-8")
        (self.wiki_dir / "index.md").write_text("# Wiki Index\n\n", encoding="utf-8")
        (self.wiki_dir / "log.md").write_text("# Operation Log\n\n", encoding="utf-8")

    # ── All current wiki pages (path → content). Excludes index/log ──
    def _list_pages(self) -> Dict[str, str]:
        out = {}
        for p in self.wiki_dir.rglob("*.md"):
            rel = p.relative_to(self.wiki_dir).as_posix()
            if rel in ("index.md", "log.md"):
                continue
            out[rel] = p.read_text(encoding="utf-8")
        return out

    @staticmethod
    def _parse_json_array(text: str):
        m = re.search(r"\[.*\]", text, re.DOTALL)
        if not m: return []
        try: return json.loads(m.group(0))
        except json.JSONDecodeError: return []

    # ── Ingest: absorb one source into the wiki ──
    def ingest(self, source_name: str):
        print(f"\nIngest: {source_name}")
        source_text = (self.raw_dir / source_name).read_text(encoding="utf-8")

        pages = self._list_pages()
        existing = "(no pages yet)" if not pages else "\n\n".join(
            f"### {path}\n{content}" for path, content in pages.items())

        msg = INGEST_PROMPT.invoke({
            "source_name": source_name,
            "source_text": source_text,
            "existing_pages": existing,
        })
        actions = self._parse_json_array(self.llm.invoke(msg).content)

        # Execute actions
        for a in actions:
            target = self.wiki_dir / a["path"]
            target.parent.mkdir(parents=True, exist_ok=True)
            if a["op"] == "create":
                target.write_text(a["content"].rstrip() + "\n", encoding="utf-8")
                print(f"    CREATE  {a['path']}")
            elif a["op"] == "append":
                cur = target.read_text(encoding="utf-8") if target.exists() else ""
                target.write_text(cur.rstrip() + "\n\n" + a["content"].rstrip() + "\n",
                                  encoding="utf-8")
                print(f"    APPEND  {a['path']}")

        self._update_index()
        self._append_log(f"ingest | {source_name} | actions={len(actions)}")

    # ── Rebuild index: grouped by category + one-line summary ──
    def _update_index(self):
        pages = self._list_pages()
        groups: Dict[str, list] = {}
        for path in sorted(pages):
            cat = path.split("/")[0] if "/" in path else "root"
            groups.setdefault(cat, []).append(path)
        lines = ["# Wiki Index",
                 f"\n_updated: {datetime.date.today()}_  / {len(pages)} pages\n"]
        for cat, paths in groups.items():
            lines.append(f"\n## {cat}")
            for p in paths:
                first = pages[p].splitlines()[0].lstrip("# ").strip()
                lines.append(f"- [[{p[:-3]}]] — {first}")
        (self.wiki_dir / "index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    # ── Append to log ──
    def _append_log(self, msg: str):
        line = f"## [{datetime.date.today()}] {msg}\n"
        with (self.wiki_dir / "log.md").open("a", encoding="utf-8") as f:
            f.write(line)

    # ── Query: answer using the whole wiki as context (small-scale demo) ──
    def query(self, question: str) -> str:
        # In production: read the index first, then have the LLM open relevant pages as a tool
        # The demo is small, so just put every page into the context at once
        pages = self._list_pages()
        joined = "\n\n".join(f"### [[{p[:-3]}]]\n{c}" for p, c in pages.items())
        msg = QUERY_PROMPT.invoke({"pages": joined, "question": question})
        return self.llm.invoke(msg).content


# ════════════════════════════════════════════════════════════════
# 3. Main — time-ordered ingest, then evolution queries
# ════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    agent = WikiAgent("./demo_wiki")
    agent.setup()

    # Ingest 3 sources in time order. Watch the wiki grow richer.
    for name in ["2024Q3_strategy.md", "2024Q4_alpha_launch.md", "2025Q1_orgchange.md"]:
        agent.ingest(name)

    # Final wiki tree
    print("\nFinal wiki structure:")
    for p in sorted(Path("./demo_wiki/wiki").rglob("*.md")):
        rel = p.relative_to("./demo_wiki/wiki")
        print(f"   {rel}  ({p.stat().st_size}B)")

    # Time-evolution queries — very hard for RAG
    # (need to integrate role changes for the same person across multiple sources)
    print("\nWiki queries:")
    for q in [
        "How have the core members of Project Alpha changed over time?",
        "How did Jane Park's role evolve?",
        "Is Minsoo Lee involved in both Alpha and Beta? How?",
    ]:
        print(f"\n━━━ Q: {q}")
        print(f"> {agent.query(q)}")

```

#### What this shows
This small example demonstrates all four core features of the LLM Wiki pattern.
  1. **Incremental accumulation** — as the three sources are ingested in order, the same person’s page keeps growing via _append_. After the first ingest, John Kim is just “CTO”; after the third, his page also says _“concurrently director of the Machine Learning Infrastructure team.”_
  2. **Auto cross-references** — wikilinks like `[[Alpha]]`, `[[John Kim]]` are generated by the LLM. Open it in Obsidian and the graph view visualizes it instantly.
  3. **Auto-maintained index** — `index.md`, organized by category, is updated on every ingest. Sufficient up to a few hundred pages — no RAG required.
  4. **Time-evolution queries** — questions like _“How did Jane Park’s role evolve?”_ are very hard for RAG (no single chunk has the answer, you need time-ordered integration). LLM Wiki answers them naturally from the already-accumulated pages.


#### Example directory output (after a run)

```
demo_wiki/
├── raw/
│   ├── 2024Q3_strategy.md
│   ├── 2024Q4_alpha_launch.md
│   └── 2025Q1_orgchange.md
└── wiki/
    ├── index.md
    ├── log.md
    ├── entities/
    │   ├── john_kim.md       ← updated 3 times (CTO → +concurrent director)
    │   ├── jane_park.md      ← updated 3 times (security owner → security team lead)
    │   ├── minsoo_lee.md     ← updated 3 times
    │   ├── hyunwoo_jung.md   ← appears starting in Q4
    │   └── jihoon_choi.md    ← new in 2025
    └── projects/
        ├── alpha.md          ← updated 3 times (planned → launched → maintenance)
        └── beta.md           ← introduced in Q4, formalized in 25Q1
```

#### Going to production  
| Component  | This example  | Production  |  
| --- | --- | --- |  
| Agent execution  | A single script  | Claude Code / Codex (direct file edits)  |  
| Wiki IDE  | Just the file system  | Obsidian + graph view + Dataview  |  
| Search  | All pages in the context (small-scale)  | qmd MCP server (BM25 + vector + LLM rerank)  |  
| Action types  | create / append only  | + update (mid-file patch), + delete, + rename  |  
| Schema  | Inlined in the prompt  | Separate `CLAUDE.md` / `AGENTS.md`  |  
| Lint  | Not implemented  | Periodic cron or user-triggered  |  
| Version control  | None  | git repo (commit every change)  |  
| Multimodal  | Text only  | Download images + LLM views them separately  |  
| Save the answer back  | None  | “Save this answer to the wiki?” UX  |  
#### One step further — the schema file
In production, place a `CLAUDE.md` (or `AGENTS.md`) at the root of the wiki and pre-load the LLM with it. Example:

```
# Schema for the LLM Wiki

## Directory layout
- `raw/` — immutable source documents
- `wiki/entities/` — person and organization pages
- `wiki/projects/` — project pages
- `wiki/concepts/` — conceptual / topic pages
- `wiki/index.md` — auto-maintained catalog
- `wiki/log.md` — append-only operation log

## Conventions
- Every fact ends with `> source: [filename]`
- Wiki links: `[[Page Name]]` (no .md extension)
- Person pages: H1 = full name, H2 sections: Title / History / Projects / Relationships
- Contradictions: insert `TODO: review contradiction — ...`

## Ingest workflow
1. Discuss key takeaways with the user first
2. Plan actions (create/append/update)
3. Execute actions
4. Update `index.md`
5. Append a line to `log.md` like `## [YYYY-MM-DD] ingest | <source>`

## Query workflow
1. Read `index.md` first
2. Open only relevant pages (don't load everything)
3. Cite each fact with `[[Page Name]]`
4. Offer to save the answer back as a new wiki page

```

This single file turns the LLM from a _generic chatbot_ into a _trained wiki editor_. It’s a living document the user and LLM evolve together over time.
* * *
### Closing
RAG is **“a mechanism for safely fetching what the model doesn’t know from outside.”** The concept is simple, but building a good RAG system means handling chunking, embeddings, retrieval, reranking, prompting, and evaluation with care, end to end.
The **Naive → Advanced → Graph** progression isn’t just feature creep — it’s a qualitative expansion of _what you can answer_. Naive answers _“what does this document say,”_ Advanced answers _“which part of these documents matters most,”_ Graph answers _“what falls out when you connect across documents.”_
And alongside RAG, **LLM Wiki** is growing as a different paradigm. Where RAG _re-derives knowledge on every query_ , LLM Wiki _compiles knowledge once and accumulates it._ The arrival of agents that write directly to the file system — Claude Code, Codex — is what makes this pattern practical. **The two don’t compete — using the wiki as a RAG source is the practical endpoint.**
The 2024–2026 trend is clear:
  1. **RAG isn’t dead.** It coexists with Long Context.
  2. The shift is **from plain RAG to Agentic RAG**.
  3. **Vector + keyword + graph + tools** combined into hybrids is the standard.
  4. We’re in the era of **picking the right augmentation per data shape**.
  5. **Alongside the era of retrieval, the era of _accumulation_** — the LLM Wiki pattern offers a new practical option for _knowledge that accumulates over time_ : personal research, deep reading, internal wikis.


Running the four examples in this document (`example_1` through `example_4`) and comparing them is the fastest way to feel the difference between each step. In particular, _Example 4’s`How did Jane Park's role evolve?`_ -style time-evolution query is very hard with RAG-family approaches — and natural in LLM Wiki. Seeing the difference firsthand makes it clear that the two paradigms are _complements_ , not _substitutes_.
* * *
_The RAG and LLM Wiki space is moving fast — double-check library versions and model specs separately._
April 27, 2026 ∙ [RAG](https://www.mrlatte.net/en/tags/rag/) [LLM](https://www.mrlatte.net/en/tags/llm/) [GraphRAG](https://www.mrlatte.net/en/tags/graphrag/) [Agentic RAG](https://www.mrlatte.net/en/tags/agentic-rag/) [LangChain](https://www.mrlatte.net/en/tags/langchain/) [vector search](https://www.mrlatte.net/en/tags/vector-search/) [embeddings](https://www.mrlatte.net/en/tags/embeddings/)
  * [Previous: AWS S3 403 Signature Mismatch: Pinpoint APM Was the Real Cause](https://www.mrlatte.net/en/research/2025/10/18/pinpoint-causes-s3-signature-mismatch/)
  * [Next: The Inference Engine Architecture War — What Actually Differs Between vLLM, SGLang, TensorRT-LLM, and Custom Silicon](https://www.mrlatte.net/en/research/2026/05/07/inference-engine-architecture/)


**Looking for a product partner?** Founders, teams, businesses — from problem framing to launch.
[Work With Me](https://www.mrlatte.net/en/work-with-me/) [Get in touch →](https://www.mrlatte.net/en/contact/)
[LinkedIn](https://linkedin.com/in/jonghaahn) [YouTube](https://www.youtube.com/@mrlattestory) [X (Twitter)](https://x.com/mrlatte_story) [Threads](https://www.threads.com/@mrlattestory) [Instagram](https://www.instagram.com/mrlattestory/)
Copyright © 2026 - present Mr. Latte. All Rights Reserved.

