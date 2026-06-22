[![EngineersofAI Logo](https://engineersofai.com/img/eai-logo.jpg)](https://engineersofai.com/)[Courses](https://engineersofai.com/courses)[Blog](https://engineersofai.com/blog)[Research Lab](https://research.engineersofai.com)[AI Letters](https://engineersofai.com/newsletter)[The Lab](https://engineersofai.com/lab)[Code Bank](https://engineersofai.com/code-bank)[Interactive 3D](https://engineersofai.com/playground)[Kodr](https://kodr.engineersofai.com)[Earnest](https://earnest.engineersofai.com)[Jobs](https://jobs.engineersofai.com)
[Sign in](https://engineersofai.com/login)
[Skip to main content](https://engineersofai.com/docs/llms/rag-systems/reranking#__docusaurus_skipToContent_fallback)
[ ![EngineersOfAI](https://engineersofai.com/img/EngineersOfAI-Logo.svg)![EngineersOfAI](https://engineersofai.com/img/EngineersOfAI-Logo.svg) **EngineersOfAI**](https://engineersofai.com/)[Python](https://engineersofai.com/python)[Math for AI](https://engineersofai.com/math-for-ai)[ML](https://engineersofai.com/ml)[Data Eng](https://engineersofai.com/data-engineering)[LLMs](https://engineersofai.com/llms)[AI Systems](https://engineersofai.com/ai-systems)[MLOps](https://engineersofai.com/mlops)[Agentic AI](https://engineersofai.com/agentic-ai)[AI Engineering](https://engineersofai.com/ai-engineering)[Break Into AI](https://engineersofai.com/break-into-ai)[Open Source Models](https://engineersofai.com/open-source-models)[Hardware & Silicon](https://engineersofai.com/hardware-and-silicon)[Applied AI](https://engineersofai.com/applied-ai)[Foundational CS](https://engineersofai.com/foundational-cs)
[Discord](https://discord.gg/g295dC6hr7)
  * [Master LLMs](https://engineersofai.com/docs/llms/home)
  * [Module 1 - Transformer Architecture](https://engineersofai.com/docs/category/module-1---transformer-architecture)
  * [Module 2 - Pretraining and Fine-Tuning](https://engineersofai.com/docs/category/module-2---pretraining-and-fine-tuning)
  * [Module 3 - Prompt Engineering](https://engineersofai.com/docs/category/module-3---prompt-engineering)
  * [Module 4 - RAG Systems](https://engineersofai.com/docs/category/module-4---rag-systems)
    * [Module 04: RAG Systems](https://engineersofai.com/docs/llms/rag-systems/overview)
    * [Why RAG and When Not To](https://engineersofai.com/docs/llms/rag-systems/why-rag-and-when-not-to)
    * [Document Chunking Strategies](https://engineersofai.com/docs/llms/rag-systems/document-chunking-strategies)
    * [Embedding Models Deep Dive](https://engineersofai.com/docs/llms/rag-systems/embedding-models-deep-dive)
    * [Vector Databases](https://engineersofai.com/docs/llms/rag-systems/vector-databases)
    * [Retrieval Algorithms and ANN](https://engineersofai.com/docs/llms/rag-systems/retrieval-algorithms-ann)
    * [Reranking](https://engineersofai.com/docs/llms/rag-systems/reranking)
    * [Hybrid Search: Dense and Sparse](https://engineersofai.com/docs/llms/rag-systems/hybrid-search-dense-sparse)
    * [RAG Evaluation](https://engineersofai.com/docs/llms/rag-systems/rag-evaluation)
    * [Advanced RAG Patterns](https://engineersofai.com/docs/llms/rag-systems/advanced-rag-patterns)
    * [Graph RAG](https://engineersofai.com/docs/llms/rag-systems/graph-rag)
    * [Agentic RAG](https://engineersofai.com/docs/llms/rag-systems/agentic-rag)
  * [Module 5 - LLM Agents](https://engineersofai.com/docs/category/module-5---llm-agents)
  * [Module 6 - LLM Evaluation](https://engineersofai.com/docs/category/module-6---llm-evaluation)
  * [Module 7 - Inference and Optimization](https://engineersofai.com/docs/category/module-7---inference-and-optimization)
  * [Module 8 - Multimodal Models](https://engineersofai.com/docs/category/module-8---multimodal-models)
  * [Module 9 - LLM System Design](https://engineersofai.com/docs/category/module-9---llm-system-design)
  * [Module 10 - Reasoning Models](https://engineersofai.com/docs/category/module-10---reasoning-models)
  * [Module 11 - Mixture of Experts](https://engineersofai.com/docs/category/module-11---mixture-of-experts)
  * [Module 12 - State Space Models](https://engineersofai.com/docs/category/module-12---state-space-models)
  * [Module 13 - Structured Generation](https://engineersofai.com/docs/category/module-13---structured-generation)
  * [Module 14 - Model Merging](https://engineersofai.com/docs/category/module-14---model-merging)
  * [Module 15 - Long Context Strategies](https://engineersofai.com/docs/category/module-15---long-context-strategies)
  * [Module 16 - Alignment and Safety](https://engineersofai.com/docs/category/module-16---alignment-and-safety)
  * [Module 17 - Embeddings Engineering](https://engineersofai.com/docs/category/module-17---embeddings-engineering)


  * [](https://engineersofai.com/)
  * [Module 4 - RAG Systems](https://engineersofai.com/docs/category/module-4---rag-systems)
  * Reranking


On this page
# Reranking
## The Precision Problem at the Top of the List[​](https://engineersofai.com/docs/llms/rag-systems/reranking#the-precision-problem-at-the-top-of-the-list "Direct link to The Precision Problem at the Top of the List")
The customer success team filed the same complaint three weeks in a row. Their RAG-powered support assistant retrieved relevant documents - the evaluation logs confirmed it. The right article was almost always in the top 20 results. But GPT-4o was seeing five chunks at a time, and the relevant chunk was consistently in positions 4-8 of the retrieved set, not position 1-3.
The LLM saw exactly what you'd expect: the most confident-sounding chunks first, generating an answer from them, while the most _relevant_ chunk sat unused in position 6. The system wasn't failing at retrieval - it was failing at ranking. The bi-encoder that drove retrieval was excellent at finding semantically related content but mediocre at distinguishing "answers this question precisely" from "is topically related to this question."
Adding a cross-encoder reranker between retrieval and generation required two days of engineering work and a $30/month Cohere API bill. It moved the most relevant chunk to position 1 for 78% of queries (from 41% before reranking). Answer quality scores from human evaluators jumped 22 points. The improvement per dollar was the highest of any optimization they'd made.
This lesson explains why bi-encoders underperform at fine-grained relevance, how cross-encoders solve the problem, and how to build a two-stage pipeline that fits within your latency budget.
## Why This Exists: The Limitation of Independent Encoding[​](https://engineersofai.com/docs/llms/rag-systems/reranking#why-this-exists-the-limitation-of-independent-encoding "Direct link to Why This Exists: The Limitation of Independent Encoding")
Bi-encoder retrieval encodes query and document independently: score(q,d)=cosine(E(q),E(d))\text{score}(q, d) = \text{cosine}(E(q), E(d))score(q,d)=cosine(E(q),E(d))
The fundamental limitation: the model has no cross-attention between query and document tokens during encoding. Each is encoded in isolation. The relevance score is computed from independent representations - which means the model can't reason about how specific query terms relate to specific document phrases.
Consider the query "What is the interest rate for a home equity loan?" and two passages:
  * **Passage A:** "Home equity loans typically offer fixed interest rates between 7-9% APR. Variable rates are available for some lenders."
  * **Passage B:** "Interest rates affect borrowing costs across many loan types including mortgages, auto loans, and home equity products."


Passage A directly answers the question. Passage B is topically related but answers a different question. A bi-encoder often gives both high similarity scores because both contain "interest rates" and "home equity" as high-salience semantic concepts. The bi-encoder can't see that the query asks about a specific rate range and Passage A provides it while Passage B doesn't.
A cross-encoder processes `[query; passage]` together with full attention between all tokens - it can literally attend to how "interest rate" in the query relates to "7-9% APR" in the passage, making the relevance decision much more accurate.
## Cross-Encoders: Full Attention at a Cost[​](https://engineersofai.com/docs/llms/rag-systems/reranking#cross-encoders-full-attention-at-a-cost "Direct link to Cross-Encoders: Full Attention at a Cost")
A cross-encoder is typically a BERT-style model (or similar) fine-tuned on relevance prediction. Given `[CLS] query [SEP] document [SEP]`, it outputs a single relevance score.
**Accuracy:** Cross-encoders are consistently 10-20% more accurate than bi-encoders on standard relevance benchmarks (MS-MARCO passage ranking). They can distinguish "passage that answers the question" from "passage that discusses the topic" with much higher precision.
**Cost:** Cannot precompute - the document representation depends on the specific query. Every (query, document) pair requires a full model forward pass. At 100 candidate documents, this is 100 forward passes per query. You'd never run this over your full corpus.
**The two-stage design:** Use bi-encoder for first-stage retrieval (fast, over all documents, returns top 50-100 candidates), use cross-encoder for second-stage reranking (accurate, over the small candidate set only).
## Production Reranker Models[​](https://engineersofai.com/docs/llms/rag-systems/reranking#production-reranker-models "Direct link to Production Reranker Models")
### Cohere Rerank[​](https://engineersofai.com/docs/llms/rag-systems/reranking#cohere-rerank "Direct link to Cohere Rerank")
The easiest production reranker - managed API, no model hosting required.

```


import cohere  





from typing import List  





  





co = cohere.Client("your-api-key")  





  





def rerank_with_cohere(  





    query: str,  





    documents: List[str],  





    top_n: int = 5,  





) -> List[dict]:  





    results = co.rerank(  





        query=query,  





        documents=documents,  





        top_n=top_n,  





        model="rerank-english-v3.0",  





        return_documents=True,  





    )  





    return [  





        {  





            "text": r.document.text,  





            "relevance_score": r.relevance_score,  





            "original_rank": r.index,  





        }  





        for r in results.results  





    ]  





  





# Example usage  





query = "What is the interest rate for a home equity loan?"  





candidates = [  





    "Home equity loans typically offer fixed interest rates between 7-9% APR.",  





    "Interest rates affect many loan types including mortgages and auto loans.",  





    "The Federal Reserve raised rates by 75 basis points in June 2022.",  





    "Home equity lines of credit (HELOCs) have variable rates tied to prime.",  





    "Loan applications require credit score verification and income documentation.",  





]  





  





reranked = rerank_with_cohere(query, candidates, top_n=3)  





for i, r in enumerate(reranked):  





    print(f"[{i+1}] Score: {r['relevance_score']:.4f}")  





    print(f"     Was: #{r['original_rank']+1} | {r['text'][:80]}")  



```

**Cohere Rerank v3 pricing:** ~2/1000APIcalls.At10,000queries/daywith50candidateseach:10,000×50=500,000document−querypairs/day.PricedperAPIcall(eachcallcanhaveupto1000documents):2/1000 API calls. At 10,000 queries/day with 50 candidates each: 10,000 × 50 = 500,000 document-query pairs/day. Priced per API call (each call can have up to 1000 documents): ~2/1000APIcalls.At10,000queries/daywith50candidateseach:10,000×50=500,000document−querypairs/day.PricedperAPIcall(eachcallcanhaveupto1000documents):20/day. For high-volume applications, self-hosting a cross-encoder model is more cost-effective.
### Self-Hosted Cross-Encoders (sentence-transformers)[​](https://engineersofai.com/docs/llms/rag-systems/reranking#self-hosted-cross-encoders-sentence-transformers "Direct link to Self-Hosted Cross-Encoders \(sentence-transformers\)")

```


from sentence_transformers import CrossEncoder  





from typing import List, Tuple  





import numpy as np  





  





# MS-MARCO trained cross-encoders - the standard for English passage ranking  





# Other options: 'cross-encoder/ms-marco-MiniLM-L-6-v2' (smaller, faster)  





model = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-12-v2')  





  





def rerank_with_cross_encoder(  





    query: str,  





    candidates: List[str],  





    top_k: int = 5,  





) -> List[Tuple[str, float]]:  





    """  





    Rerank candidates using a cross-encoder model.  





    Returns top_k (document, score) tuples sorted by relevance.  





    """  





    # Prepare (query, document) pairs  





    pairs = [(query, doc) for doc in candidates]  





  





    # Score all pairs in one batch (much faster than individual calls)  





    scores = model.predict(pairs, batch_size=32)  





  





    # Sort by score descending  





    ranked = sorted(  





        zip(candidates, scores),  





        key=lambda x: x[1],  





        reverse=True  





    )  





  





    return ranked[:top_k]  





  





# Full two-stage pipeline  





from openai import OpenAI  





import numpy as np  





  





client = OpenAI()  





  





def two_stage_retrieve(  





    query: str,  





    vector_store,          # your vector store with a .search() method  





    first_stage_k: int = 50,  





    final_k: int = 5,  





) -> List[str]:  





    """  





    Stage 1: Bi-encoder retrieves top-50 candidates.  





    Stage 2: Cross-encoder reranks to top-5.  





    """  





    # Stage 1: fast approximate retrieval  





    candidates = vector_store.search(query, top_k=first_stage_k)  





    candidate_texts = [c["text"] for c in candidates]  





  





    if not candidate_texts:  





        return []  





  





    # Stage 2: accurate reranking  





    reranked = rerank_with_cross_encoder(query, candidate_texts, top_k=final_k)  





    return [text for text, score in reranked]  



```

### BGE Reranker Models[​](https://engineersofai.com/docs/llms/rag-systems/reranking#bge-reranker-models "Direct link to BGE Reranker Models")
BAAI's BGE rerankers are strong open-source alternatives, available in multiple sizes:

```


from sentence_transformers import CrossEncoder  





  





# Small: 22M params, fast, good quality  





bge_reranker_small = CrossEncoder('BAAI/bge-reranker-base')  





# Large: 560M params, best quality, slower  





bge_reranker_large = CrossEncoder('BAAI/bge-reranker-large')  





  





# BGE reranker v2-m3: supports multilingual, 570M params  





# Best open-source multilingual reranker  





bge_m3 = CrossEncoder('BAAI/bge-reranker-v2-m3')  





  





scores = bge_reranker_large.predict([  





    ("What is home equity loan rate?", "Fixed rates between 7-9% APR."),  





    ("What is home equity loan rate?", "Interest rates affect many loan types."),  





])  





print(scores)  # [8.3, 2.1] - correctly identifies the relevant passage  



```

## ColBERT: Late Interaction - A Middle Ground[​](https://engineersofai.com/docs/llms/rag-systems/reranking#colbert-late-interaction---a-middle-ground "Direct link to ColBERT: Late Interaction - A Middle Ground")
**ColBERT** (Contextualized Late Interaction over BERT, 2020) is an elegant architecture between bi-encoder and cross-encoder. Instead of producing a single vector per query and document, ColBERT produces one vector per token. Similarity is computed as the sum of maximum similarities between query tokens and document tokens:
score(q,d)=∑i=1∣q∣max⁡j=1∣d∣Eq(qi)⋅Ed(dj)T\text{score}(q, d) = \sum_{i=1}^{|q|} \max_{j=1}^{|d|} E_q(q_i) \cdot E_d(d_j)^Tscore(q,d)=∑i=1∣q∣​maxj=1∣d∣​Eq​(qi​)⋅Ed​(dj​)T
**Why this is powerful:** Document token vectors can be precomputed and indexed. Query token vectors are computed at query time. Interaction is via the max-similarity operation - capturing which document tokens best match each query token - without requiring a full cross-encoder forward pass.
**ColBERT's practical advantages:**
  * More accurate than bi-encoders (token-level interaction)
  * Faster than cross-encoders (precomputed document representations)
  * Can be used for first-stage retrieval (unlike cross-encoders)


**ColBERT's practical disadvantages:**
  * Storage: 128-dimensional vector per token (not per document). A 200-token chunk requires 200 × 128 × 4 bytes = 102 KB vs 1536 × 4 = 6 KB for a bi-encoder. ~17x more storage.
  * Specialized infrastructure: requires `RAGatouille` or `Vespa` for production deployment



```


# ColBERT via RAGatouille library  





from ragatouille import RAGPretrainedModel  





  





# Load ColBERT-v2  





RAG = RAGPretrainedModel.from_pretrained("colbert-ir/colbertv2.0")  





  





# Index documents  





my_documents = [  





    "Home equity loans offer fixed rates between 7-9% APR.",  





    "Interest rates affect mortgage and auto loan costs.",  





    "HELOC rates are variable, tied to the prime rate.",  





]  





RAG.index(  





    collection=my_documents,  





    index_name="finance_docs",  





    max_document_length=512,  





    split_documents=True,  





)  





  





# Search - ColBERT does end-to-end retrieval + ranking  





results = RAG.search(query="home equity loan rate", k=3)  





for r in results:  





    print(f"Score: {r['score']:.2f} | {r['content'][:80]}")  



```

## LLM-as-Reranker[​](https://engineersofai.com/docs/llms/rag-systems/reranking#llm-as-reranker "Direct link to LLM-as-Reranker")
For maximum accuracy, use the LLM itself to judge relevance. Several approaches:
### Pointwise Scoring[​](https://engineersofai.com/docs/llms/rag-systems/reranking#pointwise-scoring "Direct link to Pointwise Scoring")
Ask the LLM to rate each passage's relevance to the query on a scale of 0-10.

```


from openai import OpenAI  





import json  





  





client = OpenAI()  





  





def llm_pointwise_rerank(  





    query: str,  





    candidates: List[str],  





    top_k: int = 5,  





) -> List[Tuple[str, float]]:  





    """Use GPT to score each passage's relevance."""  





    scored = []  





    for doc in candidates:  





        response = client.chat.completions.create(  





            model="gpt-4o-mini",  # use cheap model for scoring  





            messages=[  





                {  





                    "role": "system",  





                    "content": (  





                        "Rate the relevance of the passage to the query on a scale of 0-10. "  





                        "10 = directly answers the question. 0 = completely unrelated. "  





                        "Respond with only a JSON object: {\"score\": <number>}"  





                    )  





                },  





                {  





                    "role": "user",  





                    "content": f"Query: {query}\n\nPassage: {doc}"  





                }  





            ],  





            temperature=0,  





        )  





        try:  





            result = json.loads(response.choices[0].message.content)  





            score = float(result.get("score", 0))  





        except Exception:  





            score = 0.0  





        scored.append((doc, score))  





  





    scored.sort(key=lambda x: x[1], reverse=True)  





    return scored[:top_k]  



```

**Cost warning:** At 0.15/1Minputtokens(GPT−4o−mini),scoring50candidateswith500−tokenpassages=25Ktokens×0.15/1M input tokens (GPT-4o-mini), scoring 50 candidates with 500-token passages = 25K tokens × 0.15/1Minputtokens(GPT−4o−mini),scoring50candidateswith500−tokenpassages=25Ktokens×0.15/1M = 0.004perquery.At10Kqueries/day:0.004 per query. At 10K queries/day: 0.004perquery.At10Kqueries/day:40/day. Significant cost for reranking alone.
### RankGPT: Listwise Sliding Window[​](https://engineersofai.com/docs/llms/rag-systems/reranking#rankgpt-listwise-sliding-window "Direct link to RankGPT: Listwise Sliding Window")
A more elegant approach: ask the LLM to rank a list of passages directly, rather than scoring each independently. Developed by Sun et al. (2023).

```


def rankgpt_rerank(  





    query: str,  





    candidates: List[str],  





    window_size: int = 10,  





    step: int = 5,  





    top_k: int = 5,  





) -> List[str]:  





    """  





    Sliding window listwise reranking.  





    Processes candidates in windows, re-ordering each window.  





    """  





    ranked = list(range(len(candidates)))  





  





    # Slide window from end to beginning (sort most important positions last)  





    for start in range(len(ranked) - window_size, -1, -step):  





        end = min(start + window_size, len(ranked))  





        window_indices = ranked[start:end]  





        window_docs = [candidates[i] for i in window_indices]  





  





        # Ask LLM to rank this window  





        passages_text = "\n\n".join([  





            f"[{j+1}] {doc[:300]}"  





            for j, doc in enumerate(window_docs)  





        ])  





  





        response = client.chat.completions.create(  





            model="gpt-4o-mini",  





            messages=[  





                {  





                    "role": "system",  





                    "content": (  





                        "Rank the passages by relevance to the query. "  





                        "Output only a comma-separated list of passage numbers from most to least relevant. "  





                        "Example: 3,1,2,4"  





                    )  





                },  





                {  





                    "role": "user",  





                    "content": f"Query: {query}\n\n{passages_text}"  





                }  





            ],  





            temperature=0,  





        )  





  





        try:  





            order_str = response.choices[0].message.content.strip()  





            order = [int(x.strip()) - 1 for x in order_str.split(",")]  





            # Reorder the window  





            reordered = [window_indices[i] for i in order if i < len(window_indices)]  





            ranked[start:end] = reordered  





        except Exception:  





            pass  # Keep original order on parse failure  





  





    return [candidates[i] for i in ranked[:top_k]]  



```

## Reciprocal Rank Fusion (RRF)[​](https://engineersofai.com/docs/llms/rag-systems/reranking#reciprocal-rank-fusion-rrf "Direct link to Reciprocal Rank Fusion \(RRF\)")
RRF is a model-free method for combining multiple ranked lists. If you have results from a BM25 retriever, a dense retriever, and a cross-encoder, RRF gives you a principled way to merge them:
RRF(d)=∑r∈R1k+rankr(d)\text{RRF}(d) = \sum_{r \in R} \frac{1}{k + \text{rank}_r(d)}RRF(d)=∑r∈R​k+rankr​(d)1​
where RRR is the set of ranked lists, rankr(d)\text{rank}_r(d)rankr​(d) is document ddd's rank in list rrr, and kkk is a constant (typically 60) that dampens the impact of very high ranks.
**Why it works:** Reciprocal rank downweights high-rank differences - the gap between rank 1 and 2 matters less than the gap between rank 1 and rank 100. This makes RRF robust to score scale differences between retrievers.

```


from collections import defaultdict  





from typing import List, Dict, Tuple  





  





def reciprocal_rank_fusion(  





    ranked_lists: List[List[str]],  





    k: int = 60,  





) -> List[Tuple[str, float]]:  





    """  





    Fuse multiple ranked lists using RRF.  





    ranked_lists: list of lists, each sorted by relevance (best first)  





    Returns: list of (doc_id, rrf_score) sorted by score descending  





    """  





    scores: Dict[str, float] = defaultdict(float)  





  





    for ranked_list in ranked_lists:  





        for rank, doc_id in enumerate(ranked_list):  





            scores[doc_id] += 1.0 / (k + rank + 1)  # +1 for 1-indexed rank  





  





    return sorted(scores.items(), key=lambda x: x[1], reverse=True)  





  





  





# Example: fuse BM25 and dense retrieval results  





bm25_results = ["doc_A", "doc_C", "doc_B", "doc_E", "doc_D"]  





dense_results = ["doc_B", "doc_A", "doc_D", "doc_C", "doc_F"]  





  





fused = reciprocal_rank_fusion([bm25_results, dense_results])  





print("Fused ranking:")  





for doc_id, score in fused[:5]:  





    print(f"  {doc_id}: {score:.4f}")  





# doc_A and doc_B both appear high in both lists → high RRF scores  



```

## Latency Budget Analysis[​](https://engineersofai.com/docs/llms/rag-systems/reranking#latency-budget-analysis "Direct link to Latency Budget Analysis")
A two-stage pipeline adds latency. Before adding reranking, understand where your latency goes:  
| Stage  | Typical Latency  | Parallelizable?  |  
| --- | --- | --- |  
| Query embedding  | 20-50ms (API) / 5ms (local)  | No  |  
| ANN retrieval (top 50)  | 5-30ms  | No  |  
| Cross-encoder reranking (50 docs)  | 50-200ms (local) / 50-100ms (API)  | Parallel batches  |  
| LLM generation  | 500-3000ms  | No  |  
| **Total**  | **600-3400ms**  |   |  
The LLM generation dominates at 500ms+. Cross-encoder reranking adds 50-200ms - a 5-25% increase in total latency. For most applications, this is acceptable given the quality improvement.
**Optimizations:**
  * Use a smaller cross-encoder model: `MiniLM-L-6` is 3x faster than `MiniLM-L-12` with minimal quality loss
  * Reduce first-stage k: retrieve top 20 instead of top 50 if recall@20 is sufficient
  * Run reranking in parallel with LLM generation if you stream - start generating while reranking continues
  * Cache reranker scores for repeated queries



```


import time  





from concurrent.futures import ThreadPoolExecutor, as_completed  





  





def timed_stage(fn, *args, **kwargs):  





    t0 = time.time()  





    result = fn(*args, **kwargs)  





    return result, time.time() - t0  





  





# Profile your pipeline  





query = "What is the home equity loan interest rate?"  





  





# Stage 1: retrieval  





candidates, t_retrieval = timed_stage(vector_store.search, query, top_k=50)  





print(f"Retrieval: {t_retrieval*1000:.0f}ms, {len(candidates)} candidates")  





  





# Stage 2: reranking  





reranked, t_rerank = timed_stage(  





    rerank_with_cross_encoder, query, [c["text"] for c in candidates], top_k=5  





)  





print(f"Reranking: {t_rerank*1000:.0f}ms")  





  





# Check if reranking meaningfully changed the order  





print(f"\nTop 5 original ranks: {[candidates.index(next(c for c in candidates if c['text'] == t)) for t, _ in reranked]}")  



```

## When to Skip Reranking[​](https://engineersofai.com/docs/llms/rag-systems/reranking#when-to-skip-reranking "Direct link to When to Skip Reranking")
Reranking is not always worth the added latency and cost.
**Skip reranking when:**
  * Your retrieval precision is already high (consistently rank-1 recall above 80% without reranking)
  * Latency budget is under 200ms total (reranking eats 50-200ms)
  * Your corpus is small (under 10K documents) - bi-encoder recall is already near-perfect
  * Query volume is very high and cost is a constraint
  * The first-stage retrieval already uses a strong bi-encoder fine-tuned on your domain


**Definitely use reranking when:**
  * You're serving sensitive queries where rank-1 accuracy matters (medical, legal, financial)
  * Your corpus has many topically-similar documents where fine-grained relevance matters
  * Your bi-encoder evaluation shows rank-1 recall below 60%
  * You're combining multiple retrieval sources (hybrid BM25 + dense + metadata)


## Production Engineering Notes[​](https://engineersofai.com/docs/llms/rag-systems/reranking#production-engineering-notes "Direct link to Production Engineering Notes")
**Batch reranking:** Process all candidate pairs in a single batch call to the cross-encoder - don't call it one pair at a time. Sentence-transformers handles batching automatically with `model.predict(pairs, batch_size=32)`.
**Model selection by speed:** On a single CPU core:
  * `cross-encoder/ms-marco-MiniLM-L-4-v2` (22M params): ~10ms per 50 pairs
  * `cross-encoder/ms-marco-MiniLM-L-12-v2` (33M params): ~30ms per 50 pairs
  * `BAAI/bge-reranker-large` (560M params): ~200ms per 50 pairs


On GPU (A10):
  * MiniLM-L-12: ~5ms per 50 pairs
  * BGE-large: ~20ms per 50 pairs


For latency-sensitive applications, deploy on GPU or use the Cohere API.
**Cascaded reranking:** For very large first-stage retrievals (top 500), run a fast MiniLM reranker to get top 50, then run a higher-quality BGE-large reranker on those 50. Two stages of reranking with increasing quality at each stage.
## Common Mistakes[​](https://engineersofai.com/docs/llms/rag-systems/reranking#common-mistakes "Direct link to Common Mistakes")
:::danger Running Cross-Encoder Over All Documents A cross-encoder over 1M documents = 1M forward passes per query. At 10ms per 1000 pairs on GPU: 10,000 seconds per query. Never use a cross-encoder as a first-stage retriever. Always combine with a bi-encoder first stage. The cross-encoder is always a reranker over a small candidate set (typically 20-100). :::
:::warning Over-fetching in First Stage to Compensate for Bad Retrieval If your bi-encoder recall is poor (rank-1 recall under 50%), the temptation is to retrieve top 500 and rerank. This is masking the root problem (bad embedding model or chunking) with expensive reranking. The cross-encoder reranker can only work with what the bi-encoder retrieves - if the truly relevant document isn't in the top 500, no reranker can fix that. Fix retrieval first, then add reranking as a precision boost. :::
:::warning Not Evaluating Reranker Quality After adding reranking, measure whether it actually improves rank-1 accuracy. Run 100+ queries with known relevant documents. Compare rank position of the relevant document before and after reranking. If the improvement is under 5 percentage points, the reranker isn't helping your specific use case and the latency cost isn't justified. Many teams add reranking as "best practice" without measuring the actual improvement on their data. :::
## Interview Questions and Answers[​](https://engineersofai.com/docs/llms/rag-systems/reranking#interview-questions-and-answers "Direct link to Interview Questions and Answers")
**Q: Why is a cross-encoder more accurate than a bi-encoder for relevance scoring?**
A: A bi-encoder encodes query and document independently - there's no attention between query tokens and document tokens during encoding. The relevance judgment is made from separate representations, which limits the model's ability to reason about how specific query phrases relate to specific document phrases. A cross-encoder concatenates query and document and processes them together with full self-attention - it can literally attend to how "interest rate" in the query relates to "7-9% APR" in the document. This fine-grained token-level interaction allows much more precise relevance judgments. The price: cross-encoders can't precompute document representations, so they require a full forward pass for every (query, document) pair - O(n)O(n)O(n) complexity at query time. This is why cross-encoders are always used as rerankers over a small candidate set, never as first-stage retrievers over millions of documents.
**Q: Explain Reciprocal Rank Fusion and when you'd use it.**
A: RRF assigns each document a score ∑r1/(k+rankr(d))\sum_r 1/(k + \text{rank}_r(d))∑r​1/(k+rankr​(d)) across multiple ranked lists. The constant k=60k=60k=60 dampens the impact of rank-1 vs rank-2 differences. Documents appearing in multiple lists accumulate higher scores. RRF is model-free - it requires no training and doesn't assume scores are on the same scale, making it robust to combining retrievers with very different scoring distributions (e.g., BM25 scores vs cosine similarity vs cross-encoder scores). Use RRF when: combining multiple retrieval sources (dense + sparse + knowledge graph), when you don't want to tune fusion weights, or when you're combining scores from different model families. It's consistently one of the strongest baselines for multi-source fusion.
**Q: What is ColBERT's "late interaction" architecture and why is it a middle ground between bi-encoders and cross-encoders?**
A: ColBERT encodes query and document independently but produces per-token representations instead of single vectors. At query time, relevance is computed as ∑imax⁡jEq(qi)⋅Ed(dj)T\sum_i \max_j E_q(q_i) \cdot E_d(d_j)^T∑i​maxj​Eq​(qi​)⋅Ed​(dj​)T - for each query token, find the most similar document token; sum these max similarities. This gives token-level interaction without requiring a joint forward pass. Document token representations can be precomputed and indexed. Query tokens are computed at query time, and the max-similarity computation is fast matrix multiplication. ColBERT is more accurate than bi-encoders (token-level interaction captures fine-grained relevance) and faster than cross-encoders (precomputed document reps). The trade-off: storage. Each document needs per-token embeddings: a 200-token document at 128 dims per token needs 102KB vs 6KB for a single bi-encoder vector. ColBERT indexes are 10-20x larger than bi-encoder indexes.
**Q: How would you design a reranking system for a latency-sensitive production RAG serving 500 queries/second with a 300ms SLA?**
A: At 300ms total SLA budget: LLM generation takes ~200ms (using fast streaming models), leaving ~100ms for retrieval + reranking. First stage: use a self-hosted bi-encoder on GPU (5ms for embedding + 10ms for ANN retrieval = 15ms) retrieving top 30 candidates. Second stage: deploy `cross-encoder/ms-marco-MiniLM-L-6-v2` on the same GPU - on an A10, 30 candidate pairs take ~3ms in a batched call. Total retrieval + reranking: ~20ms, well within budget. For 500 QPS, you need ~500 × 20ms / 1000ms = 10 GPU-seconds of reranker capacity per second. A single A10 GPU handles roughly 300-500 reranking batches of 30 per second, so 1-2 GPUs for reranking. Horizontally scale the first-stage bi-encoder and ANN index across multiple GPU replicas. Use a request queue with timeouts to shed load gracefully under spikes.
**Q: When would you recommend skipping reranking entirely?**
A: Skip reranking when: (1) measured rank-1 recall without reranking is already above 75% - the improvement from reranking rarely exceeds 10-15 points and may not justify 50-200ms overhead; (2) latency budget is tight (under 200ms total) and LLM generation already consumes most of it; (3) your bi-encoder is fine-tuned on your specific domain - domain-specific bi-encoders often have higher recall than general cross-encoders; (4) query volume is extremely high and latency is more important than maximum accuracy (media recommendation, real-time feeds); (5) you're using a very small, well-curated corpus where recall is already near-perfect. The decision should be data-driven: measure rank-1 recall with and without reranking on your actual query distribution. If the improvement is under 5 percentage points, the latency and cost of reranking aren't justified.
## Reranker Evaluation and Selection[​](https://engineersofai.com/docs/llms/rag-systems/reranking#reranker-evaluation-and-selection "Direct link to Reranker Evaluation and Selection")
Before deploying a reranker, measure its impact on your specific data. Here is a complete evaluation pipeline:

```


from sentence_transformers import CrossEncoder  





from typing import List, Tuple, Dict  





import numpy as np  





import time  





  





def evaluate_reranker(  





    reranker: CrossEncoder,  





    test_cases: List[Dict],  





    first_stage_k: int = 20,  





    final_k: int = 5,  





) -> Dict:  





    """  





    Measure reranker impact on retrieval quality.  





  





    test_cases: list of {  





        "query": str,  





        "relevant_doc_id": str,  





        "candidates": [{"id": str, "text": str}, ...]  # ordered by bi-encoder score  





    }  





    """  





    without_reranking = []  





    with_reranking = []  





    latencies = []  





  





    for tc in test_cases:  





        query = tc["query"]  





        candidates = tc["candidates"][:first_stage_k]  





        relevant_id = tc["relevant_doc_id"]  





  





        # Rank WITHOUT reranker (bi-encoder order)  





        ids_no_rerank = [c["id"] for c in candidates]  





        rank_no_rerank = next(  





            (i + 1 for i, cid in enumerate(ids_no_rerank) if cid == relevant_id),  





            first_stage_k + 1  # not found  





        )  





        without_reranking.append(rank_no_rerank)  





  





        # Rank WITH reranker  





        pairs = [(query, c["text"]) for c in candidates]  





        t0 = time.time()  





        scores = reranker.predict(pairs, batch_size=32)  





        latencies.append((time.time() - t0) * 1000)  





  





        sorted_candidates = [candidates[i] for i in np.argsort(scores)[::-1]]  





        ids_with_rerank = [c["id"] for c in sorted_candidates]  





        rank_with_rerank = next(  





            (i + 1 for i, cid in enumerate(ids_with_rerank) if cid == relevant_id),  





            first_stage_k + 1  





        )  





        with_reranking.append(rank_with_rerank)  





  





    # Compute metrics  





    mrr_before = np.mean([1/r for r in without_reranking])  





    mrr_after = np.mean([1/r for r in with_reranking])  





    recall_at_5_before = np.mean([1 if r <= 5 else 0 for r in without_reranking])  





    recall_at_5_after = np.mean([1 if r <= 5 else 0 for r in with_reranking])  





  





    return {  





        "mrr_before": mrr_before,  





        "mrr_after": mrr_after,  





        "mrr_improvement": mrr_after - mrr_before,  





        "recall_at_5_before": recall_at_5_before,  





        "recall_at_5_after": recall_at_5_after,  





        "recall_at_5_improvement": recall_at_5_after - recall_at_5_before,  





        "mean_reranking_latency_ms": np.mean(latencies),  





        "p95_reranking_latency_ms": np.percentile(latencies, 95),  





    }  





  





  





# Compare reranker models  





models_to_compare = [  





    ("ms-marco-MiniLM-L-6-v2", CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")),  





    ("ms-marco-MiniLM-L-12-v2", CrossEncoder("cross-encoder/ms-marco-MiniLM-L-12-v2")),  





    ("bge-reranker-base", CrossEncoder("BAAI/bge-reranker-base")),  





]  





  





# test_cases = [...]  # Your golden dataset with bi-encoder candidates  





  





for name, model in models_to_compare:  





    # results = evaluate_reranker(model, test_cases)  





    print(f"{name}:")  





    # print(f"  MRR improvement: +{results['mrr_improvement']:.3f}")  





    # print(f"  Recall@5 improvement: +{results['recall_at_5_improvement']:.3f}")  





    # print(f"  Latency: {results['mean_reranking_latency_ms']:.0f}ms")  



```

## Reranking in the Context of the Full Pipeline[​](https://engineersofai.com/docs/llms/rag-systems/reranking#reranking-in-the-context-of-the-full-pipeline "Direct link to Reranking in the Context of the Full Pipeline")
Reranking sits at the junction between retrieval and generation. It's easy to add but easy to misconfigure. Here's the complete picture of where reranking fits in a production RAG system:
Key observations from this pipeline:
  1. **Caching eliminates reranking cost for repeated queries.** Common questions in production are often identical or near-identical. Cache the final answer with a 1-hour TTL. Semantic caching (using embedding similarity to detect near-duplicate queries) can hit 30-50% cache rates for production systems.
  2. **Metadata filtering happens before reranking.** If you're filtering to `doc_type="faq"`, the reranker only sees FAQ chunks - reducing both latency and the possibility of irrelevant non-FAQ chunks slipping into the top-5.
  3. **The first-stage k matters.** Reranking 100 candidates takes 2-4x longer than reranking 25 candidates. If your bi-encoder achieves 90% Recall@25 (the relevant document appears in the top 25 for 90% of queries), use k=25. Don't over-retrieve "just in case."
  4. **LLM generation dominates.** At 500-2000ms, LLM generation is 3-10x slower than retrieval + reranking combined. Optimize retrieval and reranking for correctness, not primarily for speed - the LLM is your bottleneck.


## Summary: The Reranking Decision[​](https://engineersofai.com/docs/llms/rag-systems/reranking#summary-the-reranking-decision "Direct link to Summary: The Reranking Decision")
Reranking is not an automatic addition to every RAG pipeline - it is a targeted intervention for a specific failure mode: first-stage retrieval returns relevant documents but ranks them below irrelevant ones.
The decision process:
  1. Measure rank-1 recall without reranking on your golden dataset
  2. If rank-1 recall is above 75%, first-stage retrieval is adequate
  3. If rank-1 recall is below 75%, add reranking and re-measure
  4. Verify the improvement is meaningful (more than 5 percentage points)
  5. Measure the latency impact and confirm it fits your SLA
  6. Choose the smallest reranker model that achieves your target recall


When reranking does help, it consistently produces the best improvements of any single RAG optimization - often 15-25 percentage points on rank-1 recall with a modest latency cost.
## Deploying a Self-Hosted Reranker as a Service[​](https://engineersofai.com/docs/llms/rag-systems/reranking#deploying-a-self-hosted-reranker-as-a-service "Direct link to Deploying a Self-Hosted Reranker as a Service")
For production systems handling significant traffic, deploy your cross-encoder as an independent microservice:

```


from fastapi import FastAPI  





from pydantic import BaseModel  





from sentence_transformers import CrossEncoder  





from typing import List, Tuple  





import numpy as np  





import time  





  





app = FastAPI(title="Reranking Service")  





  





# Load model at startup - keep in memory for all requests  





model = CrossEncoder(  





    "cross-encoder/ms-marco-MiniLM-L-12-v2",  





    device="cuda",  # Use GPU for production  





    max_length=512,  





)  





  





class RerankRequest(BaseModel):  





    query: str  





    documents: List[str]  





    top_k: int = 5  





  





class RankedDocument(BaseModel):  





    document: str  





    score: float  





    original_rank: int  





  





class RerankResponse(BaseModel):  





    results: List[RankedDocument]  





    latency_ms: float  





  





@app.post("/rerank", response_model=RerankResponse)  





async def rerank(request: RerankRequest) -> RerankResponse:  





    t0 = time.perf_counter()  





  





    # Create (query, document) pairs  





    pairs = [(request.query, doc) for doc in request.documents]  





  





    # Score all pairs in one batch  





    scores = model.predict(pairs, batch_size=64).tolist()  





  





    # Sort by score  





    ranked = sorted(  





        [(doc, score, i) for i, (doc, score) in enumerate(zip(request.documents, scores))],  





        key=lambda x: x[1],  





        reverse=True,  





    )[:request.top_k]  





  





    latency_ms = (time.perf_counter() - t0) * 1000  





  





    return RerankResponse(  





        results=[  





            RankedDocument(document=doc, score=score, original_rank=orig_rank)  





            for doc, score, orig_rank in ranked  





        ],  





        latency_ms=latency_ms,  





    )  





  





@app.get("/health")  





async def health():  





    return {"status": "ok", "model": "ms-marco-MiniLM-L-12-v2"}  





  





# Run with: uvicorn reranker_service:app --host 0.0.0.0 --port 8080 --workers 1  





# Note: CrossEncoder is not thread-safe for concurrent GPU inference.  





# Use 1 worker per GPU, scale by adding GPU replicas behind a load balancer.  



```

**Client-side integration:**

```


import httpx  





import asyncio  





  





async def rerank_async(  





    query: str,  





    candidates: List[str],  





    top_k: int = 5,  





    reranker_url: str = "http://reranker-service:8080",  





) -> List[dict]:  





    """Async call to the reranker service."""  





    async with httpx.AsyncClient(timeout=10.0) as client:  





        response = await client.post(  





            f"{reranker_url}/rerank",  





            json={"query": query, "documents": candidates, "top_k": top_k},  





        )  





        response.raise_for_status()  





        data = response.json()  





        return data["results"]  





  





  





# Use in your RAG pipeline  





async def rag_with_async_reranking(query: str, vector_store) -> str:  





    # Stage 1: retrieval (fast)  





    candidates = vector_store.search(query, top_k=30)  





    candidate_texts = [c["text"] for c in candidates]  





  





    # Stage 2: reranking (concurrent with other work if needed)  





    reranked = await rerank_async(query, candidate_texts, top_k=5)  





  





    # Stage 3: generation  





    context = "\n\n".join([r["document"] for r in reranked])  





    # ... call LLM  





    return context  



```

## Reranking Across Languages[​](https://engineersofai.com/docs/llms/rag-systems/reranking#reranking-across-languages "Direct link to Reranking Across Languages")
For multilingual RAG systems, standard MS-MARCO cross-encoders underperform on non-English text. Use multilingual rerankers:

```


from sentence_transformers import CrossEncoder  





  





# BGE-reranker-v2-m3: supports 100+ languages  





# Strong cross-lingual reranking (English query → French documents)  





multilingual_reranker = CrossEncoder("BAAI/bge-reranker-v2-m3")  





  





# Cohere Rerank with multilingual support  





import cohere  





co = cohere.Client("your-api-key")  





  





multilingual_results = co.rerank(  





    query="Comment retourner un article?",    # French query  





    documents=[  





        "Les articles peuvent être retournés dans les 30 jours.",   # French  





        "Items can be returned within 30 days.",                      # English  





        "Die Rücksendung ist innerhalb von 30 Tagen möglich.",       # German  





    ],  





    model="rerank-multilingual-v3.0",  





    top_n=2,  





)  



```

The Cohere multilingual reranker (`rerank-multilingual-v3.0`) supports 100+ languages and handles cross-lingual queries (query in English, documents in French) correctly. For self-hosted multilingual reranking, `BAAI/bge-reranker-v2-m3` is the strongest open-source option.
:::tip 🎮 Interactive Playground
**Visualize this concept:** Try the **[RAG Pipeline](https://engineersofai.com/playground/rag-pipeline)** demo on the EngineersOfAI Playground - no code required.
:::
**Tags:**
  * [llm](https://engineersofai.com/docs/tags/llm)
  * [rag](https://engineersofai.com/docs/tags/rag)
  * [deep-dive](https://engineersofai.com/docs/tags/deep-dive)


© 2026 EngineersOfAI. All rights reserved.
[Previous Retrieval Algorithms and ANN](https://engineersofai.com/docs/llms/rag-systems/retrieval-algorithms-ann)[Next Hybrid Search: Dense and Sparse](https://engineersofai.com/docs/llms/rag-systems/hybrid-search-dense-sparse)
  * [The Precision Problem at the Top of the List](https://engineersofai.com/docs/llms/rag-systems/reranking#the-precision-problem-at-the-top-of-the-list)
  * [Why This Exists: The Limitation of Independent Encoding](https://engineersofai.com/docs/llms/rag-systems/reranking#why-this-exists-the-limitation-of-independent-encoding)
  * [Cross-Encoders: Full Attention at a Cost](https://engineersofai.com/docs/llms/rag-systems/reranking#cross-encoders-full-attention-at-a-cost)
  * [Production Reranker Models](https://engineersofai.com/docs/llms/rag-systems/reranking#production-reranker-models)
    * [Cohere Rerank](https://engineersofai.com/docs/llms/rag-systems/reranking#cohere-rerank)
    * [Self-Hosted Cross-Encoders (sentence-transformers)](https://engineersofai.com/docs/llms/rag-systems/reranking#self-hosted-cross-encoders-sentence-transformers)
    * [BGE Reranker Models](https://engineersofai.com/docs/llms/rag-systems/reranking#bge-reranker-models)
  * [ColBERT: Late Interaction - A Middle Ground](https://engineersofai.com/docs/llms/rag-systems/reranking#colbert-late-interaction---a-middle-ground)
  * [LLM-as-Reranker](https://engineersofai.com/docs/llms/rag-systems/reranking#llm-as-reranker)
    * [Pointwise Scoring](https://engineersofai.com/docs/llms/rag-systems/reranking#pointwise-scoring)
    * [RankGPT: Listwise Sliding Window](https://engineersofai.com/docs/llms/rag-systems/reranking#rankgpt-listwise-sliding-window)
  * [Reciprocal Rank Fusion (RRF)](https://engineersofai.com/docs/llms/rag-systems/reranking#reciprocal-rank-fusion-rrf)
  * [Latency Budget Analysis](https://engineersofai.com/docs/llms/rag-systems/reranking#latency-budget-analysis)
  * [When to Skip Reranking](https://engineersofai.com/docs/llms/rag-systems/reranking#when-to-skip-reranking)
  * [Production Engineering Notes](https://engineersofai.com/docs/llms/rag-systems/reranking#production-engineering-notes)
  * [Common Mistakes](https://engineersofai.com/docs/llms/rag-systems/reranking#common-mistakes)
  * [Interview Questions and Answers](https://engineersofai.com/docs/llms/rag-systems/reranking#interview-questions-and-answers)
  * [Reranker Evaluation and Selection](https://engineersofai.com/docs/llms/rag-systems/reranking#reranker-evaluation-and-selection)
  * [Reranking in the Context of the Full Pipeline](https://engineersofai.com/docs/llms/rag-systems/reranking#reranking-in-the-context-of-the-full-pipeline)
  * [Summary: The Reranking Decision](https://engineersofai.com/docs/llms/rag-systems/reranking#summary-the-reranking-decision)
  * [Deploying a Self-Hosted Reranker as a Service](https://engineersofai.com/docs/llms/rag-systems/reranking#deploying-a-self-hosted-reranker-as-a-service)
  * [Reranking Across Languages](https://engineersofai.com/docs/llms/rag-systems/reranking#reranking-across-languages)


Learning Tracks
  * [Python Engineering](https://engineersofai.com/python)
  * [Math for AI](https://engineersofai.com/math-for-ai)
  * [Machine Learning](https://engineersofai.com/ml)
  * [Data Engineering for AI](https://engineersofai.com/data-engineering)
  * [LLMs](https://engineersofai.com/llms)
  * [AI Systems Design](https://engineersofai.com/ai-systems)
  * [MLOps](https://engineersofai.com/mlops)
  * [Agentic AI](https://engineersofai.com/agentic-ai)
  * [AI Engineering](https://engineersofai.com/ai-engineering)
  * [Break Into AI](https://engineersofai.com/break-into-ai)


Platform
  * [Kodr - Practice Platform](https://kodr.engineersofai.com)
  * [Jobs - AI/ML Board](https://jobs.engineersofai.com)
  * [Earnest - Salaries](https://earnest.engineersofai.com)
  * [SynapseKit](https://www.synapse-kit.com)
  * [Code Bank](https://engineersofai.com/code-bank)
  * [Blog](https://engineersofai.com/blog)
  * [Research Lab](https://research.engineersofai.com)
  * [AI Letters](https://engineersofai.com/newsletter)
  * [The Lab](https://engineersofai.com/lab)


Community
  * [Discord](https://discord.gg/g295dC6hr7)
  * [LinkedIn](https://www.linkedin.com/company/engineersofai)
  * [Twitter / X](https://x.com/engineersofai)
  * [GitHub](https://github.com/engineersofai)
  * [YouTube](https://youtube.com/@engineersofai)
  * [Substack](https://engineersofai.substack.com)


Company
  * [About EngineersOfAI](https://engineersofai.com/about)
  * [Mission](https://engineersofai.com/mission)
  * [Contact Us](https://engineersofai.com/contact)
  * [Press Kit](https://engineersofai.com/press)


[Terms of Use](https://engineersofai.com/terms) [Security](https://engineersofai.com/security) [Privacy](https://engineersofai.com/privacy) [Cookie Policy](https://engineersofai.com/cookies) Cookie Settings [Impressum](https://engineersofai.com/impressum)
Made with ❤ to make education accessible to all.
Copyright © 2026 EngineersOfAI. All rights reserved.

