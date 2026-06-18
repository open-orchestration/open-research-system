# A complete architectural teardown of how Perplexity's deep research ...

Source: https://gist.github.com/Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136

[Skip to content](https://gist.github.com/Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136#start-of-content)
[ ](https://gist.github.com/)
Search Gists 
Search Gists
[All gists](https://gist.github.com/discover) [Back to GitHub](https://github.com) [ Sign in ](https://gist.github.com/auth/github?return_to=https%3A%2F%2Fgist.github.com%2FCo-Messi%2Fbfcfb39eede5c6bc2fadd2c04139a136) [ Sign up ](https://gist.github.com/join?return_to=https%3A%2F%2Fgist.github.com%2FCo-Messi%2Fbfcfb39eede5c6bc2fadd2c04139a136&source=header-gist)
[ ](https://gist.github.com/)
[ Sign in ](https://gist.github.com/auth/github?return_to=https%3A%2F%2Fgist.github.com%2FCo-Messi%2Fbfcfb39eede5c6bc2fadd2c04139a136) [ Sign up ](https://gist.github.com/join?return_to=https%3A%2F%2Fgist.github.com%2FCo-Messi%2Fbfcfb39eede5c6bc2fadd2c04139a136&source=header-gist)
You signed in with another tab or window. [Reload](https://gist.github.com/Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136) to refresh your session. You signed out in another tab or window. [Reload](https://gist.github.com/Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136) to refresh your session. You switched accounts on another tab or window. [Reload](https://gist.github.com/Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136) to refresh your session. Dismiss alert
{{ message }}
Instantly share code, notes, and snippets. 
[![@Co-Messi](https://avatars.githubusercontent.com/u/87403883?s=64&v=4)](https://gist.github.com/Co-Messi)
#  [Co-Messi](https://gist.github.com/Co-Messi)/**[perplexity-deep-research-architecture.md](https://gist.github.com/Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136)**
Created April 10, 2026 11:27
Show Gist options
  * [ Download ZIP  ](https://gist.github.com/Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136/archive/1c393a08947a70dea189a7d919ff9e7ba140dbee.zip)


  * [ Star 1 (1) ](https://gist.github.com/login?return_to=https%3A%2F%2Fgist.github.com%2FCo-Messi%2Fbfcfb39eede5c6bc2fadd2c04139a136)You must be signed in to star a gist
  * [ Fork 0 (0) ](https://gist.github.com/login?return_to=https%3A%2F%2Fgist.github.com%2FCo-Messi%2Fbfcfb39eede5c6bc2fadd2c04139a136)You must be signed in to fork a gist


  * Embed 
#  Select an option 
    * Embed  Embed this gist in your website.
    * Share  Copy sharable link for this gist.
    * Clone via HTTPS  Clone using the web URL.
## No results found
[Learn more about clone URLs](https://docs.github.com/articles/which-remote-url-should-i-use)
Clone this repository at &lt;script src=&quot;https://gist.github.com/Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136.js&quot;&gt;&lt;/script&gt; 
  * Save Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136 to your computer and use it in GitHub Desktop.


[ Code ](https://gist.github.com/Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136) [ Revisions 1 ](https://gist.github.com/Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136/revisions) [ Stars 1 ](https://gist.github.com/Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136/stargazers)
Embed 
#  Select an option 
  * Embed  Embed this gist in your website.
  * Share  Copy sharable link for this gist.
  * Clone via HTTPS  Clone using the web URL.


## No results found
[Learn more about clone URLs](https://docs.github.com/articles/which-remote-url-should-i-use)
Clone this repository at &lt;script src=&quot;https://gist.github.com/Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136.js&quot;&gt;&lt;/script&gt; 
Save Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136 to your computer and use it in GitHub Desktop.
[Download ZIP](https://gist.github.com/Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136/archive/1c393a08947a70dea189a7d919ff9e7ba140dbee.zip)
A complete architectural teardown of how Perplexity's deep research pipeline works — covering RAG orchestration, hybrid retrieval, multi-stage reranking, citation binding, Deep Research vs Standard mode, context window strategy, session memory, and a practical MVP-to-moat rebuild plan with open-source component recommendations. 
[ Raw ](https://gist.github.com/Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136/raw/1c393a08947a70dea189a7d919ff9e7ba140dbee/perplexity-deep-research-architecture.md)
[ **perplexity-deep-research-architecture.md** ](https://gist.github.com/Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136#file-perplexity-deep-research-architecture-md)
# Perplexity AI — Teardown and Rebuild Plan
[](https://gist.github.com/Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136#perplexity-ai--teardown-and-rebuild-plan)
**A complete architecture reference for building a Perplexity-class AI search agent**
* * *
## Executive Summary
[](https://gist.github.com/Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136#executive-summary)
Perplexity is not a smarter model. It is a disciplined **Retrieval-Augmented Generation (RAG) pipeline** that treats retrieval, source ranking, and inline citation as first-class engineering concerns — not afterthoughts bolted onto a chatbot. The underlying LLMs it uses (GPT-4, Claude, Gemini, its own Sonar) are the same families everyone else has access to. What differentiates it is the orchestration layer around those models.
A competing system does not require secret prompts or proprietary models. It requires robust query analysis, hybrid retrieval (BM25 + dense), multi-layer reranking, structured prompt assembly with embedded citations, constrained LLM generation, and tight observability around citation quality and latency. This is non-trivial engineering, but it is all reproducible with off-the-shelf components.
* * *
## Table of Contents
[](https://gist.github.com/Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136#table-of-contents)
  1. [What Makes Perplexity Different](https://gist.github.com/Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136#1-what-makes-perplexity-different)
  2. [Observable Product Behaviors](https://gist.github.com/Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136#2-observable-product-behaviors)
  3. [End-to-End Pipeline Architecture](https://gist.github.com/Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136#3-end-to-end-pipeline-architecture)
  4. [Retrieval Strategy](https://gist.github.com/Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136#4-retrieval-strategy)
  5. [Deep Research vs Standard Mode](https://gist.github.com/Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136#5-deep-research-vs-standard-mode)
  6. [Citation System](https://gist.github.com/Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136#6-citation-system)
  7. [Context Window Strategy](https://gist.github.com/Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136#7-context-window-strategy)
  8. [Session and Cross-Turn Memory](https://gist.github.com/Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136#8-session-and-cross-turn-memory)
  9. [Perplexity vs Claude vs ChatGPT vs Gemini vs Google](https://gist.github.com/Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136#9-perplexity-vs-claude-vs-chatgpt-vs-gemini-vs-google)
  10. [Rebuild Plan: MVP to Moat](https://gist.github.com/Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136#10-rebuild-plan-mvp-to-moat)
  11. [The Secret Sauce (Without Secrets)](https://gist.github.com/Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136#11-the-secret-sauce-without-secrets)
  12. [Failure Modes](https://gist.github.com/Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136#12-failure-modes)
  13. [Actionable Build Roadmap](https://gist.github.com/Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136#13-actionable-build-roadmap)
  14. [Appendix: Recommended Open-Source Components](https://gist.github.com/Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136#appendix-recommended-open-source-components)


* * *
## 1. What Makes Perplexity Different
[](https://gist.github.com/Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136#1-what-makes-perplexity-different)
Most AI assistants treat the web as an optional tool. Perplexity treats it as the primary substrate.  
| Dimension  | Claude / ChatGPT  | Perplexity  |  
| --- | --- | --- |  
| Default knowledge source  | Training data (cutoff)  | Live web retrieval  |  
| Citations  | Optional / inconsistent  | Default, numbered, per-claim  |  
| Research modes  | Single-pass generation  | Multi-pass agentic loop  |  
| Model  | Single LLM backend  | Routes across GPT, Claude, Gemini, Sonar  |  
| UX emphasis  | Conversation  | Evidence + answer side-by-side  |  
| Abstain logic  | Rare  | Explicit: refuses if evidence is weak  |  
**Analogy:** Claude and ChatGPT answer from memory like a student who studied last year. Perplexity runs to the library every time, reads 10–30 sources, and brings you highlighted excerpts with footnotes.
**Like explaining to a 10-year-old:** Imagine you asked a friend a question. ChatGPT answers from what it remembers learning. Perplexity opens a browser, reads a bunch of articles right now, and then tells you the answer — but also shows you which articles it read so you can check.
* * *
## 2. Observable Product Behaviors
[](https://gist.github.com/Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136#2-observable-product-behaviors)
### 2.1 Behaviors beyond standard LLM chat
[](https://gist.github.com/Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136#21-behaviors-beyond-standard-llm-chat)
  * Inline numbered citations appear on most factual sentences, linked directly to source URLs, by default — not as an optional toggle.
  * "Pro Search" and "Deep Research" modes execute visible multi-step plans, issuing multiple behind-the-scenes searches before synthesising a single answer.
  * Mode-adaptive behavior (Standard / Pro / Deep / API) implies configurable retrieval depth and model selection at the system level.
  * Current-events queries return fresh answers, confirming live web retrieval rather than reliance on training data.
  * Suggested follow-up questions are query-class-aware (research vs factual vs comparative).


### 2.2 Signals of multi-stage retrieval (inferred)
[](https://gist.github.com/Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136#22-signals-of-multi-stage-retrieval-inferred)
  * Complex prompts produce clearly multi-part structured answers, strongly implying internal query decomposition.
  * Pro and Deep modes take visibly longer and cite more sources, implying multiple retrieval passes and staged reranking.
  * Citations cluster around factual sentences — not scattered randomly — suggesting citation markers are embedded during prompt assembly, not added post-generation.
  * If sources are weak or unavailable (paywalls, no reputable hits), the system tends to produce no answer rather than hallucinate.


### 2.3 Likely division of responsibilities
[](https://gist.github.com/Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136#23-likely-division-of-responsibilities)
  * **Retrieval system:** query parsing, sub-query generation, search API calls, hybrid retrieval, deduplication, quality filtering, snippet extraction, citation ID assignment, prompt assembly.
  * **Model layer:** constrained answer synthesis using supplied passages, limited multi-step planning (Pro/Deep modes), follow-up suggestion generation.
  * **Frontend / UX:** mode selection, source carousel display, citation hover previews, streaming answer rendering, session-scoped context management.


* * *
## 3. End-to-End Pipeline Architecture
[](https://gist.github.com/Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136#3-end-to-end-pipeline-architecture)
This is the full pipeline from user query to final grounded answer. Each stage is independently optimisable.

```
User Query
    │
    ▼
┌─────────────────────────────┐
│  1. Request Intake & Routing │  Auth, rate limits, geo/risk, mode selection
└─────────────────────────────┘
    │
    ▼
┌─────────────────────────────┐
│  2. Intent Classification   │  Query type: factual / research / code / financial / news
│     & Query Analysis        │  Recency sensitivity detection (dates, "latest", "today")
└─────────────────────────────┘
    │
    ▼
┌─────────────────────────────┐
│  3. Query Decomposition     │  Sub-questions from complex prompts
│     & Rewriting             │  Entity expansion, anaphora removal, BM25 variants,
│                             │  natural language variants for dense retrieval
└─────────────────────────────┘
    │
    ▼
┌─────────────────────────────┐
│  4. Live Search             │  Proprietary index + external search APIs
│     (Hybrid Retrieval)      │  BM25/lexical + dense vector search
│                             │  Filters: language, region, recency, domain class
│                             │  Routing: trending index vs evergreen index
└─────────────────────────────┘
    │
    ▼
┌─────────────────────────────┐
│  5. Source Fetching         │  Fetch top N URLs
│     & Parsing               │  Boilerplate/nav/ad stripping (readability-style)
│                             │  Chunking: headings, paragraphs, code blocks
│                             │  Metadata: URL, title, timestamp, domain class, token count
└─────────────────────────────┘
    │
    ▼
┌─────────────────────────────┐
│  6. Deduplication           │  Near-duplicate URL and chunk detection (hash + similarity)
│     & Normalisation         │  Canonical URL resolution across mirrored domains
└─────────────────────────────┘
    │
    ▼
┌─────────────────────────────┐
│  7. Credibility & Quality   │  Domain type: .gov/.edu/vendor/blog/forum
│     Scoring                 │  Content structure, topical depth, freshness
│                             │  Historical engagement and citation success signals
│                             │  Learned quality model tuned for "answer-worthy passages"
└─────────────────────────────┘
    │
    ▼
┌─────────────────────────────┐
│  8. Multi-Layer Ranking     │  L1: fast relevance filter (BM25 + dense merge)
│     (L1 → L3)               │  L2: cross-encoder reranker on top ~50–100 candidates
│                             │  L3: heavy reranker with hard quality threshold (~0.7)
│                             │      only top ~30% survive; if too few pass, re-retrieve
│                             │  Diversity constraints: ensure query aspect coverage
└─────────────────────────────┘
    │
    ▼
┌─────────────────────────────┐
│  9. Context Assembly        │  Select top K chunks from M sources
│     & Citation Binding      │  Assign internal citation IDs to each chunk
│                             │  Build structured prompt: query + evidence chunks
│                             │  Each chunk tagged: [ID] URL, title, date, snippet
└─────────────────────────────┘
    │
    ▼
┌─────────────────────────────┐
│  10. Constrained LLM        │  Generate answer grounded ONLY in supplied evidence
│      Synthesis              │  Inline citation markers tied to chunk IDs
│                             │  Temperature and length tuned per mode
│                             │  Deep/Pro: loop (search → partial synthesis → refine → re-search)
└─────────────────────────────┘
    │
    ▼
┌─────────────────────────────┐
│  11. Post-Processing        │  Parse citation markers from model output
│      & Frontend Binding     │  Map IDs → URL metadata for UI display
│                             │  Stream tokens to frontend; render inline citations
│                             │  Build source sidebar / carousel with hover previews
└─────────────────────────────┘
    │
    ▼
┌─────────────────────────────┐
│  12. Follow-Up Generation   │  Suggest follow-ups based on answer + query class
│      & Session Context      │  Maintain per-session context: prior queries, citations
│                             │  Resolve pronouns and chained questions across turns
└─────────────────────────────┘
    │
    ▼
Final Grounded Answer + Inline Citations + Source Carousel

```

### Latency Optimisation (Cross-Cutting)
[](https://gist.github.com/Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136#latency-optimisation-cross-cutting)
  * Parallelise search calls across backends and sub-queries simultaneously.
  * Apply aggressive per-domain timeouts; do not block the pipeline on slow sites.
  * Cache: popular query results, hot documents, partial prompts, and LLM completions for deterministic prompts.
  * Begin LLM generation as soon as the top tier of evidence is ready; append delayed evidence in Deep modes without restarting.


* * *
## 4. Retrieval Strategy
[](https://gist.github.com/Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136#4-retrieval-strategy)
### 4.1 Index Architecture
[](https://gist.github.com/Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136#41-index-architecture)
Perplexity operates a **hybrid index setup** — not a thin wrapper on Bing:
  * A large proprietary index (200B+ URLs) with heavy recency bias, likely maintained with its own crawling infrastructure.
  * External search API connectors (notably Bing) for breadth and freshness.
  * Multiple specialised indices routed by query intent: a `trending_news_index` for recency-sensitive queries, an `evergreen` or `suggested` index for stable reference content.


For your own build: start with Tavily or Serper.dev (Phase 1), layer in your own vector DB index for high-value verticals (Phase 2), and progressively replace API calls with your own crawling (Phase 3).
### 4.2 Hybrid Retrieval
[](https://gist.github.com/Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136#42-hybrid-retrieval)
Never rely on one retrieval technique alone. Always combine:
  * **BM25 / lexical search** — strong for exact terms, specific entities, code symbols.
  * **Dense vector search** — strong for semantic similarity, paraphrased queries, fuzzy intent.
  * **Filters** — language, region, recency window, domain class (academic / news / official / forum).


The merge of BM25 and dense results dramatically improves recall on long-tail queries and fuzzy wording where one method alone would miss the answer.
### 4.3 Authority and Credibility
[](https://gist.github.com/Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136#43-authority-and-credibility)
Credibility scoring is passage-level, not just domain-level:
  * Domain type priors: official docs and government > major media > academic > vendor docs > blogs > forums.
  * Content quality signals: clarity of structure, topical depth, heading presence, appropriate length.
  * Recency signals: explicit timestamps weighted heavily for news/finance queries.
  * Corroboration: agreement across independent reputable sources is an explicit positive ranking signal.


**Key insight:** content quality at the passage level often matters more than classical backlink authority. A well-structured, on-topic paragraph from a mid-tier domain can outrank a thin paragraph from a major domain.
### 4.4 Vertical Routing (Inferred)
[](https://gist.github.com/Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136#44-vertical-routing-inferred)  
| Query Type  | Preferred Sources  |  
| --- | --- |  
| News / current events  | Newswire, major media, timestamped content  |  
| Financial / market data  | Regulators, exchanges, financial APIs  |  
| Technical / dev  | Official docs, GitHub, package registries, Stack Overflow  |  
| Academic / research  | Scholarly indices, preprint servers, academic domains  |  
| How-to / troubleshooting  | Forums, Reddit, community wikis  |  
| Legal / compliance  | Government and regulatory sources  |  
### 4.5 Handling Conflicting Sources
[](https://gist.github.com/Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136#45-handling-conflicting-sources)
Two layers of conflict resolution:
**Retrieval side:** corroboration boosting means sources that agree with others rank higher. Outlier claims are implicitly down-weighted before the LLM ever sees them. In Deep Research, a dedicated cross-source validation stage flags conflicts explicitly.
**Generation side:** when high-quality evidence conflicts, the LLM is supplied multiple opposing passages and instructed to synthesise conditionally ("some sources report X, others Y") with multiple citations. It does not pick a winner and hide the disagreement.
**Abstention:** if all retrieved evidence falls below quality thresholds — due to paywalls, spam, or no reputable hits — the system prefers to return an explicit uncertainty response rather than hallucinate an answer.
* * *
## 5. Deep Research vs Standard Mode
[](https://gist.github.com/Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136#5-deep-research-vs-standard-mode)
Deep Research is not "standard mode but slower." It is a fundamentally different orchestration loop layered on top of the same retrieval and ranking primitives.  
| Dimension  | Standard Mode  | Deep Research  |  
| --- | --- | --- |  
| Query decomposition  | Light rewriting + intent mapping  | Explicit sub-topic decomposition  |  
| Retrieval passes  | Single pass (one primary query + variants)  | 3–5 sequential refinement cycles  |  
| Search calls  | ~1–5  | Dozens (scanning hundreds of sources)  |  
| Duration  | Seconds  | 2–5 minutes  |  
| Conflict handling  | LLM decides in context  | Dedicated cross-source validation stage  |  
| Intermediate state  | None  | Structured scratchpad / notes across sub-queries  |  
| Output format  | Paragraph answer  | Structured report: sections, tables, timelines, uncertainty annotations  |  
| Evidence reuse  | Single context window  | Evidence explicitly preserved and re-queried across sub-topics  |  
**Analogy:** Standard mode is a smart Google search that summarises the top results. Deep Research is a junior analyst who receives your brief, writes a research plan, spends 3 minutes hammering the web in waves, cross-checks conflicting data, and hands you a structured report.
In pipeline terms, Deep Research is an **agentic loop:**

```
Decompose query into sub-topics
  For each sub-topic:
    → Retrieve → Partial synthesis → Update scratchpad
    → Identify gaps → Refine sub-queries → Re-retrieve
  Cross-source validation pass (flag conflicts)
  Final synthesis conditioned on full scratchpad + evidence set

```

* * *
## 6. Citation System
[](https://gist.github.com/Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136#6-citation-system)
Citations in Perplexity are **not** added by the LLM as an afterthought. They are wired into the pipeline before generation begins.
### How it works
[](https://gist.github.com/Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136#how-it-works)
  1. The ranking layer assigns each selected chunk a **provenance record** : `{citation_id, url, title, date, snippet_text}`.
  2. The context assembly stage inserts these chunks into the prompt with their IDs explicitly embedded: 
```
[1] https://example.com — "The widget supports three modes..."
[2] https://docs.example.com — "Configuration requires a YAML file..."

```

  3. The generation prompt instructs the model: _"Only claim facts supported by the evidence above. Tag each claim with the ID of the source passage."_
  4. The model outputs inline citation markers (e.g., `[1]`, `[2]`) tied to specific claims.
  5. Post-processing maps these markers back to the provenance records for frontend rendering.
  6. In the UI, each citation number is a clickable superscript; hovering shows the exact snippet; clicking opens the source URL.


### Why this matters for your build
[](https://gist.github.com/Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136#why-this-matters-for-your-build)
This design means **citation quality is a retrieval and prompt-engineering problem, not a model capability problem.** The model is filling in text around pre-structured citation hooks. A weaker model with a well-structured citation prompt will outperform a stronger model with a vague "cite your sources" instruction.
### Citation constraints for clean UX
[](https://gist.github.com/Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136#citation-constraints-for-clean-ux)
  * Cap total citations per answer (e.g., 15–20 max).
  * Cap citations per source (e.g., 3 max from a single domain).
  * Require at least 2 independent sources for any claim flagged as potentially contested.


* * *
## 7. Context Window Strategy
[](https://gist.github.com/Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136#7-context-window-strategy)
Perplexity feeds **paragraph-sized chunks** , not full pages, to the LLM.
  * Pages are split into logical units (~300–600 tokens with overlap) at the chunking stage.
  * Only the highest-scoring chunks across all candidate pages are assembled into the final prompt.
  * A dedicated "Context Window Packaging" stage selects the best-value chunks that fit within the model's context limit.
  * In Deep Research, intermediate notes and cross-sub-topic summaries are written before final synthesis — further compressing information rather than dumping more raw tokens into one window.


**Analogy:** You do not give the model every book in the library. You give it highlighted excerpts from selected chapters, then a compressed summary of those excerpts, and then it writes the essay.
### Practical implications for your build
[](https://gist.github.com/Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136#practical-implications-for-your-build)
  * Chunk at logical boundaries (headings, paragraphs), not arbitrary token counts.
  * Store chunks with metadata: source URL, position in document, heading path, token count.
  * Use a passage-level reranker, not a document-level one — you want the best paragraph, not the best page.
  * For Deep Research mode: implement an intermediate "scratchpad" where the agent writes notes between retrieval passes before final synthesis.


* * *
## 8. Session and Cross-Turn Memory
[](https://gist.github.com/Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136#8-session-and-cross-turn-memory)
Three distinct memory layers operate independently:  
| Layer  | Scope  | Mechanism  |  
| --- | --- | --- |  
| **Within a Deep Research run**  | Single request  | Evidence explicitly preserved across sub-queries; scratchpad maintained between retrieval passes  |  
| **Across turns in a conversation**  | Session  | Prior answers and citations included in conversational context; model can implicitly reference prior sources  |  
| **User-controlled evidence**  | Persistent  | "Spaces" feature lets users pin sources for reuse across sessions — a user-controlled RAG store  |  
There is no public evidence that ad-hoc retrieval results are merged into a global search index in real time. The memory is contextual and session-scoped, not persistent by default.
* * *
## 9. Perplexity vs Claude vs ChatGPT vs Gemini vs Google
[](https://gist.github.com/Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136#9-perplexity-vs-claude-vs-chatgpt-vs-gemini-vs-google)  
| System  | Stronger than Perplexity at  | Perplexity stronger at  | Core architectural difference  |  
| --- | --- | --- | --- |  
| **ChatGPT**  | Creative writing, coding, tool integrations, iterative ideation  | Default cited web answers, recency, research UX  | ChatGPT treats web as a tool; Perplexity treats it as the substrate  |  
| **Claude**  | Long-document analysis, careful reasoning, alignment, context length  | Dense citations, live research, source-forward UX  | Claude's web access is auxiliary; Perplexity's retrieval is central to every query  |  
| **Gemini**  | Deep Google ecosystem integration, native multimodal search  | Citation-dense answer engine vs SERP overlay  | Gemini inherits Google's link-first UX; Perplexity collapses SERP into a synthesised answer  |  
| **Google Search**  | Navigational search, "find a site," massive index, long-tail coverage  | Turning 10+ sources into one grounded cited answer  | Google is link-first; Perplexity is answer-with-evidence-first  |  
**Key takeaway:** Perplexity's perceived advantage is mostly architectural and product-design choices. The models underneath are often the same. What differs is the orchestration, ranking pipeline, and the UX decision to make evidence a first-class citizen rather than a footnote.
* * *
## 10. Rebuild Plan: MVP to Moat
[](https://gist.github.com/Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136#10-rebuild-plan-mvp-to-moat)
### Core Services (Modular, Independently Scalable)
[](https://gist.github.com/Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136#core-services-modular-independently-scalable)

```
┌─────────────┐   ┌──────────────────┐   ┌──────────────────┐
│   Gateway   │──▶│  Query Analyser  │──▶│ Retrieval Service│
│ Auth, Rate  │   │  Intent, Decomp  │   │  Search APIs +   │
│ Limits, Log │   │  Recency detect  │   │  Vector DB query │
└─────────────┘   └──────────────────┘   └──────────────────┘
                                                  │
                          ┌───────────────────────┘
                          ▼
              ┌───────────────────────┐
              │  Fetcher / Parser     │
              │  HTML → clean text    │
              │  Chunk + metadata     │
              └───────────────────────┘
                          │
                          ▼
              ┌───────────────────────┐
              │  Ranking Service      │
              │  BM25 + dense hybrid  │
              │  L1 → L2 → L3 stack  │
              └───────────────────────┘
                          │
                          ▼
              ┌───────────────────────┐
              │  Orchestrator         │
              │  Prompt assembly      │
              │  Citation ID binding  │
              │  LLM call + parsing   │
              └───────────────────────┘
                          │
                   ┌──────┴──────┐
                   ▼             ▼
        ┌──────────────┐  ┌────────────────┐
        │  LLM Gateway │  │ Citation & Tel │
        │  Provider    │  │ ID→URL mapping │
        │  abstraction │  │ Traces, metrics│
        └──────────────┘  └────────────────┘
                   │
                   ▼
        ┌──────────────────────────┐
        │  Frontend (React/Next)   │
        │  Streaming, citations,   │
        │  source sidebar, hovers  │
        └──────────────────────────┘

```

### Model Layer
[](https://gist.github.com/Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136#model-layer)  
| Role  | Recommended Starting Point  |  
| --- | --- |  
| Answer synthesis  | GPT-4.1 class or Claude Sonnet via API  |  
| Light tasks (query analysis, classification)  | Cheaper open-weight model (Llama / Mistral class)  |  
| Intent classifier  | Distilled transformer, fine-tuned on query type labels  |  
| Passage reranker  | Cross-encoder (bge-reranker or similar)  |  
| Embedding model  | High-quality text embedding optimised for web retrieval (e.g., text-embedding-3-large, or bge-large)  |  
### Search Provider Phasing
[](https://gist.github.com/Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136#search-provider-phasing)  
| Phase  | Approach  | Trade-off  |  
| --- | --- | --- |  
| Phase 1 (MVP)  | Single web search API (Tavily, Serper, Brave)  | Fast to ship; limited ranking control  |  
| Phase 2 (v1)  | Own index for 1–2 high-value verticals + vector DB (Qdrant, Weaviate, pgvector)  | Better ranking control; moderate infra cost  |  
| Phase 3 (moat)  | Gradually replace API calls with own crawling for high-traffic domains  | Lower latency, lower cost, full control  |  
### Ranking Layer (Staged)
[](https://gist.github.com/Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136#ranking-layer-staged)

```
Stage 0: Accept upstream search rank as a prior (free signal)
Stage 1: BM25 on your text index + vector search on embeddings → merge results
Stage 2: Cross-encoder reranker on top 50–100 candidates (passage-level)
Stage 3: Heavy reranker with quality thresholds + diversity constraints
         → Drop anything below threshold; prefer re-query over bad citations

```

Quality features to score:
  * Recency (time decay tuned per query type)
  * Domain authority heuristics (hand-curated class scores)
  * Content structure score (heading presence, paragraph coherence, length)
  * Historical citation success rates (once you have usage data)


### Prompt Assembly Template
[](https://gist.github.com/Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136#prompt-assembly-template)

```
System: You are a research assistant. Answer the user's question using ONLY 
the evidence passages below. For every factual claim, include an inline 
citation in the format [N] where N is the passage number. If the evidence 
does not support a claim, do not make it.

Evidence:
[1] Source: https://example.com | Title: "..." | Date: 2026-04-01
    Snippet: "The system operates using a hybrid retrieval approach..."

[2] Source: https://docs.example.com | Title: "..." | Date: 2026-03-15
    Snippet: "Configuration requires a minimum of three nodes..."

[3] ...

User question: {query}

```

### Caching Strategy
[](https://gist.github.com/Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136#caching-strategy)  
| Layer  | What to Cache  | TTL  |  
| --- | --- | --- |  
| Query cache  | Normalised query → full answer + citations  | Hours (news) to days (evergreen)  |  
| Retrieval cache  | Query embedding → top URLs + passage IDs  | 1–6 hours  |  
| Content cache  | Per-URL parsed text + chunks (invalidate on hash change)  | 24–72 hours  |  
| LLM cache  | Prompt hash → completion (for deterministic prompts)  | Indefinite  |  
### Observability and Evaluation
[](https://gist.github.com/Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136#observability-and-evaluation)
**Tracing per request:**
  * Log: sub-queries generated → URLs retrieved → passages ranked → passages selected → prompt sent → model output → citations rendered.
  * Flag: any query that triggers re-retrieval, abstention, or latency outliers.


**Metrics:**
  * Latency per stage (retrieval, ranking, LLM, total end-to-end)
  * Cost per query (API calls + LLM tokens)
  * Citation density (citations per 100 words)
  * Citation click-through rate (proxy for citation quality)
  * Abstain rate (proxy for evidence coverage)
  * Re-retrieval rate (proxy for ranking quality)


**Evaluation harness:**
  * Curated benchmark of ~200–500 queries across domains and difficulty levels.
  * Labels: factual accuracy, citation correctness, coverage of query intent, abstain appropriateness.
  * Run evals on every deploy; track regressions.


### Safety and Fallback Logic
[](https://gist.github.com/Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136#safety-and-fallback-logic)
**Pre-LLM filters:**
  * Domain blocklist (known spam, malware, extremist content).
  * Basic content classifiers: NSFW, self-harm, hate speech.


**Post-LLM filters:**
  * Output classifier + selective redaction or safe-template responses where required.


**Fallback hierarchy:**
  1. If ranking yields weak evidence → re-query with varied formulations.
  2. If still weak after re-query → return explicit uncertainty message + optional SERP-style link list.
  3. If LLM call fails → return top-ranked links with auto-extracted snippets from the reranker.
  4. Rate-limit expensive Deep Research mode per user to control cost.


* * *
## 11. The Secret Sauce (Without Secrets)
[](https://gist.github.com/Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136#11-the-secret-sauce-without-secrets)
These are the highest-leverage architectural decisions that drive Perplexity's research-native feel. None requires proprietary technology.  
| Decision  | Why It Matters  |  
| --- | --- |  
| **Citations as a first-class constraint**  | Shape the entire ranking and prompt pipeline around citation correctness, not just fluency  |  
| **Chunk-level ranking, not page-level**  | "Best paragraph for this question" is a different objective than "best webpage" — and it's more useful  |  
| **Hybrid retrieval by default**  | Lexical + dense + filters; never rely on one technique; dramatically improves recall on long-tail queries  |  
| **Multi-layer reranking with strict thresholds**  | Better to drop weak sources and re-query than to feed junk into the model  |  
| **Research modes as a product feature**  | Exposing multi-step planning to users builds trust and differentiates from single-shot chatbots  |  
| **Context shaped for LLM consumption**  | Tune passage length, ordering, and instructions specifically for groundedness; this reduces hallucination more than model choice  |  
| **Source-forward UX**  | Answer + evidence side-by-side, with easy source inspection — builds trust that compounds over time  |  
| **Abstain logic**  | Refusing to answer when evidence is weak is a feature, not a limitation; it distinguishes a research tool from a hallucination machine  |  
| **Metrics aligned to research quality**  | Track citation quality and grounding rates, not just token throughput or user retention  |  
All of these are systems and product choices. They do not depend on secret prompts.
* * *
## 12. Failure Modes
[](https://gist.github.com/Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136#12-failure-modes)
Know these before you ship:  
| Failure Mode  | Description  | Mitigation  |  
| --- | --- | --- |  
| **Hallucinated citations**  | Model attaches `[3]` to a claim not supported by passage 3, especially when context is dense or IDs are misaligned  | Strict citation-in-prompt templating; post-generation citation verification pass  |  
| **Stale data**  | Over-reliance on cached pages or slow refresh cycles produces outdated answers on fast-moving topics  | Aggressive TTL on content cache for news/finance; recency signals in ranking  |  
| **SEO spam ingestion**  | Without robust spam detection, highly optimised junk ranks into your top passages and poisons synthesis  | Spam classifiers, domain quality priors, corroboration-based ranking  |  
| **Over-aggressive query rewriting**  | Rewrites can shift intent ("best for me" → generic "best"), producing answers that seem smart but miss user constraints  | Conservative rewriting; preserve user-specific qualifiers  |  
| **Speed-quality trade-offs**  | Disabling higher-layer rerankers for latency immediately degrades grounding and trust  | Never cut L3 ranking; cut retrieval breadth before ranking depth  |  
| **Overconfident synthesis**  | LLMs smooth contradictions by default; users get an authoritative-sounding answer that hides underlying disagreement  | Explicit system prompt instructions to surface conflict; uncertainty annotations  |  
| **Shallow cross-verification**  | Using only 2–3 sources means minority-but-correct views are dropped  | Minimum source diversity requirements; boost passages that add new perspectives  |  
| **Index bias**  | If your index is skewed by language, region, or domain, ranking inherits that bias invisibly  | Diversify crawling targets; track per-vertical citation quality separately  |  
| **Citation count inflation**  | Too many citations per answer becomes noise, not signal  | Hard caps: max 15–20 total citations, max 3 per domain  |  
| **Deep Research cost explosion**  | Uncapped agentic loops are expensive fast  | Per-user rate limits, hard search-call caps, cost budgets per session  |  
* * *
## 13. Actionable Build Roadmap
[](https://gist.github.com/Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136#13-actionable-build-roadmap)
### What to copy immediately (MVP scope)
[](https://gist.github.com/Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136#what-to-copy-immediately-mvp-scope)
  * Inline citations as the default, not an optional mode.
  * Hybrid retrieval (BM25 + dense) feeding a passage-level reranker.
  * Structured prompt assembly: source snippets + citation IDs embedded before generation.
  * A "Standard vs Research" mode toggle that genuinely changes retrieval depth and planning steps.
  * End-to-end request tracing from query → sources → citations → answer.


### What NOT to copy
[](https://gist.github.com/Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136#what-not-to-copy)
  * Blind trust in upstream SERP rankings — always apply your own quality reranking.
  * An overly complex mode matrix at launch (keep it to 1–2 modes).
  * Heavy scraping of paywalled or legally ambiguous content without a clear policy.
  * Hiding uncertainty — design explicitly for "here is what we don't know."


### 7-Day MVP
[](https://gist.github.com/Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136#7-day-mvp)
  * Single-region backend: gateway, query analyser (simple classifier), retrieval orchestrator, fetcher/parser, passage splitter, LLM orchestrator.
  * Integrate one web search API (Tavily recommended) + one vector DB (Qdrant or pgvector).
  * BM25 + dense retrieval, basic cross-encoder reranker.
  * Prompt assembly: 8–15 passages with numeric citation IDs.
  * Web UI: streams answer text, renders inline citations, shows source list.


### 30-Day v1
[](https://gist.github.com/Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136#30-day-v1)
  * Multi-stage reranking (L1–L3), diversity constraints, recency-aware scoring.
  * Research mode: multi-step search plans, deeper retrieval, intermediate scratchpad.
  * Narrow proprietary index for one vertical (dev docs, finance, etc.) with own crawling.
  * Observability + evaluation harness: accuracy, citation quality, latency, cost dashboards.
  * Safety filters and explicit abstain logic for low-evidence topics.
  * Basic personalisation hooks: region, language, domain preference.


### What requires a real moat (6–18 months)
[](https://gist.github.com/Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136#what-requires-a-real-moat-618-months)
  * A large, high-quality, passage-centric web index with rich metadata and content-level understanding.
  * Well-trained ranking and quality models based on real user feedback and citation correctness data — this compounds significantly with scale.
  * Sophisticated evaluation pipelines and feedback loops that continuously improve retrieval and grounding.
  * Deep ecosystem integrations (APIs, plugins, enterprise data connectors) that make the system infrastructure, not just a website.
  * Brand trust around accuracy and reliability — each correct, well-cited answer compounds this over time.


* * *
## Appendix: Recommended Open-Source Components
[](https://gist.github.com/Co-Messi/bfcfb39eede5c6bc2fadd2c04139a136#appendix-recommended-open-source-components)  
| Component  | Options  |  
| --- | --- |  
| Web search API  | Tavily (AI-native, best for agents), Serper.dev (cheaper), Brave Search API  |  
| Vector database  | Qdrant, Weaviate, pgvector (Postgres extension)  |  
| BM25 / lexical search  | Elasticsearch, OpenSearch, BM25S (pure Python)  |  
| Cross-encoder reranker  | bge-reranker-v2-m3, Cohere Rerank API  |  
| Embedding model  | text-embedding-3-large (OpenAI), bge-large-en-v1.5, pplx-embed style  |  
| HTML content extraction  | trafilatura, readability-lxml, newspaper3k  |  
| LLM synthesis  | Claude Sonnet / GPT-4.1 class via API  |  
| Observability / tracing  | Langfuse, Arize, or custom OpenTelemetry pipeline  |  
| Frontend  | Next.js + Vercel AI SDK (streaming + citation rendering)  |  
* * *
_Built from public research, observed product behavior, and independent architectural reverse-engineering. No proprietary information used. All architectural claims are inferred from public descriptions and observable system behavior._
[Sign up for free](https://gist.github.com/join?source=comment-gist) **to join this conversation on GitHub**. Already have an account? [Sign in to comment](https://gist.github.com/login?return_to=https%3A%2F%2Fgist.github.com%2FCo-Messi%2Fbfcfb39eede5c6bc2fadd2c04139a136)
## Footer
[ ](https://github.com) © 2026 GitHub, Inc. 
### Footer navigation
  * [Terms](https://docs.github.com/site-policy/github-terms/github-terms-of-service)
  * [Privacy](https://docs.github.com/site-policy/privacy-policies/github-privacy-statement)
  * [Security](https://github.com/security)
  * [Status](https://www.githubstatus.com/)
  * [Community](https://github.community/)
  * [Docs](https://docs.github.com/)
  * [Contact](https://support.github.com?tags=dotcom-footer)
  * Manage cookies 
  * Do not share my personal information 


You can’t perform that action at this time. 

