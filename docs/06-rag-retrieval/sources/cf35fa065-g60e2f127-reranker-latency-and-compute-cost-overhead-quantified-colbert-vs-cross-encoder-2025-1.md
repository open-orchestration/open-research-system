[Sitemap](https://medium.com/sitemap/sitemap.xml)
[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)
Sign up
[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2F%40aimichael%2Fcross-encoders-colbert-and-llm-based-re-rankers-a-practical-guide-a23570d88548&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)
[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)
Get app
[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)
[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)
Sign up
[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2F%40aimichael%2Fcross-encoders-colbert-and-llm-based-re-rankers-a-practical-guide-a23570d88548&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)
![Unknown user](https://miro.medium.com/v2/resize:fill:32:32/1*dmbNkD5D-u45r44go_cf0g.png)
# Cross-Encoders, ColBERT, and LLM-Based Re-Rankers: A Practical Guide
[![Michael Ryaboy](https://miro.medium.com/v2/resize:fill:32:32/1*iTWSk2J3q-7jAnKaxSgKnQ.jpeg)](https://medium.com/@aimichael?source=post_page---byline--a23570d88548---------------------------------------)
[Michael Ryaboy](https://medium.com/@aimichael?source=post_page---byline--a23570d88548---------------------------------------)
Follow
7 min read
·
Jan 10, 2025
[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fp%2Fa23570d88548&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40aimichael%2Fcross-encoders-colbert-and-llm-based-re-rankers-a-practical-guide-a23570d88548&user=Michael+Ryaboy&userId=14223ef349bb&source=---header_actions--a23570d88548---------------------clap_footer------------------)
116
[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Frepost%2Fp%2Fa23570d88548&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40aimichael%2Fcross-encoders-colbert-and-llm-based-re-rankers-a-practical-guide-a23570d88548&user=Michael+Ryaboy&userId=14223ef349bb&source=---header_actions--a23570d88548---------------------repost_header------------------)
[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fa23570d88548&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40aimichael%2Fcross-encoders-colbert-and-llm-based-re-rankers-a-practical-guide-a23570d88548&source=---header_actions--a23570d88548---------------------bookmark_footer------------------)
[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3Da23570d88548&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40aimichael%2Fcross-encoders-colbert-and-llm-based-re-rankers-a-practical-guide-a23570d88548&source=---header_actions--a23570d88548---------------------post_audio_button------------------)
Share
Press enter or click to view image in full size
![](https://miro.medium.com/v2/resize:fit:700/1*2KJhLlc3QHDYqx5o019o9A.png)
Image comparing cross-encoders, ColBERT, and LLMs
Building a modern search pipeline isn’t just about pulling documents out of a giant haystack. It’s about refining those results until the user finds precisely what they want—quickly, reliably, and at a reasonable cost. Yet choosing the right re-ranking method often feels like navigating a maze of trade-offs. Let’s dig into three popular approaches: Cross-Encoders, ColBERT, and LLM-based Re-Rankers-and get into the nitty-gritty of what each means for your latency budgets, hardware requirements, integration complexity, and user satisfaction.
Press enter or click to view image in full size
![](https://miro.medium.com/v2/resize:fit:700/0*IfqwJwAdKLIBTAvv.png)
## Cross-Encoders: Precision Through Deep Pairwise Analysis
Cross-Encoders process each query-document pair together in a transformer model, with some models achieving state-of-the-art scores on benchmarks like MS MARCO (e.g., MRR@10 > 40). In practice, this means if you have a top-50 list from a quick initial retrieval, a cross-encoder can reorder it so the best answers rise to the top. For a high-stakes scenario-say, a legal search platform or a niche B2B product database-this level of accuracy can mean users trust your system more and convert or engage more deeply.
**The Catch:** Each document rerank requires a full forward pass. If your system handles thousands of queries per second and you try to cross-encode 100 documents per query, prepare for significant GPU usage and latency. Expect at least a few hundred milliseconds added per query if unoptimized. To mitigate costs, teams often truncate texts to reduce token counts, batch queries, or cache frequent queries. Some also lean on managed services (e.g., Cohere’s API) for convenience-though that shifts cost control outside your data center.
If you’re at massive scale (millions of queries/day), a pure cross-encoder solution may be too expensive. But if you serve a specialized domain with fewer, high-value queries, cross-encoders offer near “expert-level” sorting at the final step. Think of them as the last filter that ensures what the user sees is top-notch.
Press enter or click to view image in full size
![](https://miro.medium.com/v2/resize:fit:700/0*rflU7X35AoXJziif.png)
## ColBERT: A Middle Ground with Precomputed Token-Level Embeddings
ColBERT (Contextualized Late Interaction over BERT) encodes documents offline into token-level embeddings. At query time, it encodes the query and then efficiently compares query and document tokens. This avoids re-running a full transformer pass for every candidate, letting you handle larger candidate sets-say, a few hundred or even a thousand-more gracefully than a cross-encoder would.
**Cost Details:** Precomputing and storing token-level embeddings for millions of documents can consume tens of gigabytes. Applying 8-bit quantization or other compression can cut this down, though you’ll lose a bit of accuracy. You’ll likely need a vector database that has on-disk storage, such as [KDB.AI](http://KDB.AI)’s qHNSW index, as storing ColBERT embeddings in memory is far too inefficient and expensive.
Still, for large catalogs or knowledge bases where you want a step up in quality over simple embeddings but can’t afford cross-encoders at scale, ColBERT is a strong choice. It’s a sweet spot: more nuanced than vanilla vector similarity, more affordable than running a cross-encoder on every candidate.
ColBERT also has an image-based equivalent, ColPali. ColPali is currently SOTA in PDF retrieval, and allows you to effectively search PDFs without extracting text first.
## LLM-Based Re-Rankers: Flexible Criteria at Higher Cost
Large Language Models let you push relevance definitions beyond semantic similarity. Want to prioritize newer articles, verified sources, or with human-like judgement on arbitrary criteria without retraining a model? Prompt your LLM: “Re-rank these 20 documents by how [insert criteria here], preferring the most recently published.” It’ll adjust on the fly.
## Get Michael Ryaboy’s stories in your inbox
Join Medium for free to get updates from this writer.
Subscribe
Subscribe
Remember me for faster sign in
**Trade-Offs:** LLM calls are slow and expensive. A single LLM request might cost a few cents and add over a second of latency (especially when long lists of documents are passed)-unacceptable for many consumer-facing applications. This approach makes sense when queries are rare and high-value, like a research analyst’s queries in a finance firm or a legal team’s deep dive into precedent. You can combine LLM re-ranking with cheaper methods, using it only for complex queries or final refinements. One good example of when LLM reranking works is candidate search: which candidate is best suited based on this job description? An LLM would massively outperform a cross-encoder here.
Stability can be an issue. Prompt changes might cause ranking fluctuations, so you’ll need careful prompt design, testing, and possibly even fine-tuning. If you can handle the cost and latency, LLM-based re-ranking grants you extraordinary flexibility-just be prepared to spend time tuning prompts and observing how users react. There are also small LLM-based ranking models that work as well or better than their larger counterparts for some tasks, although just using the cheapest Gemini model can be a good starting point.
Press enter or click to view image in full size
![](https://miro.medium.com/v2/resize:fit:700/0*8ZKapw6lVrFDW3P3.png)
Image generated by Midjourney and edited by Michael Ryaboy
## Putting It All Together: A Layered Pipeline
A common production strategy is to layer these methods:
  1. **Initial Retrieval (Fast & Broad):** Use BM25 or a dense vector search to pull the top 1,000 documents. This step is cheap and ensures high recall.
  2. **Refinement (ColBERT):** Apply ColBERT to these 1,000 to produce a well-ordered shortlist of 100 with better semantic nuance. Your indexing overhead and ANN search keep latencies in check.
  3. **Final Touch (Cross-Encoder or LLM):** For those top 50–100 documents, run a cross-encoder if you need crisp relevance improvements at a tolerable GPU cost. Or, if your scenario calls for domain-specific logic (e.g., “Imagine you are an expert lawyer, sort these documents by how well they match your query”), use an LLM to apply those complex rules on the last handful of candidates.


This layered approach helps you control infrastructure spending while still providing outstanding relevance. E.g., in an e-commerce store, the initial retrieval gets all relevant SKUs, ColBERT filters them down, and the cross-encoder ensures that the final results match the user’s query as closely as possible. For a specialized B2B analytics portal, maybe you swap in an LLM at the end to sort results by compliance guidelines or proprietary scoring rules.
Press enter or click to view image in full size
![](https://miro.medium.com/v2/resize:fit:700/0*TBJzqNCf1HyK4t1Q.png)
## Evaluating Success and Balancing Costs
To know if these investments pay off, measure metrics like MRR or NDCG on a sample of queries. If cross-encoders bump your NDCG@10 by 5% but triple your GPU bills, is it worth it? In the case that you are passing the top 5 documents to an LLM, focus on your precision@5 to minimize hallucinations. If ColBERT reduces your latency from seconds to under a second with minimal accuracy loss compared to a cross-encoder, that’s valuable. Consider user satisfaction surveys, conversion rates, or reduced abandonment as practical KPIs. If customers quickly find what they need, that might translate into real revenue gains or fewer support tickets.
Memory and storage matter, too. Storing ColBERT embeddings might add 20GB+ to your infrastructure footprint for a million documents, which could mean higher cloud storage bills. I’d incorporate ColBERT if you know what you are doing, as it takes a little more expertise — for example, the large memory footprint can largely be mitigated with quantizations techniques like pooling/binarization, but that’s something you need to be aware of. With LLMs, prompt length and token counts directly translate to cost. You might be able to take advantage of prompt caching to save money, or only use LLMs for challenging queries/observability. Experiment with quantization, pruning, or using smaller models distilled from larger ones to balance cost and accuracy. You likely don’t need the largest model to give you a sorted list of document numbers.
## Staying Current
The field of information retrieval keeps evolving at a rapid pace. Research teams are exploring ways to distill large models into smaller, more efficient rankers-like RankZypher and specialized open-source cross-encoders-that retain strong performance without the staggering computational overhead. Vendors continually refine their APIs, making inference faster and cheaper, while open-source communities release new ColBERT variants, LLM-based rerankers, and layerwise methods optimized for large-scale tasks. Techniques like quantization and approximate nearest neighbor indices reduce storage footprints and latency, making re-ranking pipelines more practical to deploy.
Your choice ultimately hinges on your constraints and goals. Cross-encoders excel when precision and subtlety matter most, but only if you can handle their runtime cost on a small, curated set. ColBERT provides a flexible middle ground, improving relevance beyond a basic vector approach without demanding the resources of a cross-encoder at full scale. If your use case calls for dynamic, nuanced criteria-like blending domain rules, freshness, or authority signals-an LLM-based re-ranker can adapt on the fly, provided you can justify the added latency and expense. By combining these methods into a careful multi-stage pipeline and staying alert to fresh innovations, you can tailor your solution rather than settling for a one-size-fits-all approach-ultimately delivering a search experience that genuinely meets user needs and your organization’s priorities.
I’m releasing a comprehensive ebook on rerankers next month! Join the waitlist at [llmbook.co](https://llmbook.co) or follow me on [LinkedIn](https://www.linkedin.com/in/michael-ryaboy-software-engineer/) for more tips on retrieval and ranking.
[Data Science](https://medium.com/tag/data-science?source=post_page-----a23570d88548---------------------------------------)
[AI](https://medium.com/tag/ai?source=post_page-----a23570d88548---------------------------------------)
[Large Language Models](https://medium.com/tag/large-language-models?source=post_page-----a23570d88548---------------------------------------)
[Information Retrieval](https://medium.com/tag/information-retrieval?source=post_page-----a23570d88548---------------------------------------)
[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fp%2Fa23570d88548&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40aimichael%2Fcross-encoders-colbert-and-llm-based-re-rankers-a-practical-guide-a23570d88548&user=Michael+Ryaboy&userId=14223ef349bb&source=---footer_actions--a23570d88548---------------------clap_footer------------------)
116
[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fvote%2Fp%2Fa23570d88548&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40aimichael%2Fcross-encoders-colbert-and-llm-based-re-rankers-a-practical-guide-a23570d88548&user=Michael+Ryaboy&userId=14223ef349bb&source=---footer_actions--a23570d88548---------------------clap_footer------------------)
116
[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Frepost%2Fp%2Fa23570d88548&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40aimichael%2Fcross-encoders-colbert-and-llm-based-re-rankers-a-practical-guide-a23570d88548&user=Michael+Ryaboy&userId=14223ef349bb&source=---footer_actions--a23570d88548---------------------repost_footer------------------)
[](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2F_%2Fbookmark%2Fp%2Fa23570d88548&operation=register&redirect=https%3A%2F%2Fmedium.com%2F%40aimichael%2Fcross-encoders-colbert-and-llm-based-re-rankers-a-practical-guide-a23570d88548&source=---footer_actions--a23570d88548---------------------bookmark_footer------------------)
[![Michael Ryaboy](https://miro.medium.com/v2/resize:fill:48:48/1*iTWSk2J3q-7jAnKaxSgKnQ.jpeg)](https://medium.com/@aimichael?source=post_page---post_author_info--a23570d88548---------------------------------------)
[![Michael Ryaboy](https://miro.medium.com/v2/resize:fill:64:64/1*iTWSk2J3q-7jAnKaxSgKnQ.jpeg)](https://medium.com/@aimichael?source=post_page---post_author_info--a23570d88548---------------------------------------)
Follow
## [Written by Michael Ryaboy](https://medium.com/@aimichael?source=post_page---post_author_info--a23570d88548---------------------------------------)
[1.7K followers](https://medium.com/@aimichael/followers?source=post_page---post_author_info--a23570d88548---------------------------------------)
·[11 following](https://medium.com/@aimichael/following?source=post_page---post_author_info--a23570d88548---------------------------------------)
Developer Advocate at [KDB.AI](http://KDB.AI). I write about LLMs, RAG, and fullstack AI engineering
Follow
[Help](https://help.medium.com/hc/en-us?source=post_page-----a23570d88548---------------------------------------)
[Status](https://status.medium.com/?source=post_page-----a23570d88548---------------------------------------)
[About](https://medium.com/about?autoplay=1&source=post_page-----a23570d88548---------------------------------------)
[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----a23570d88548---------------------------------------)
Press
[Blog](https://blog.medium.com/?source=post_page-----a23570d88548---------------------------------------)
[Store](https://medium.com/store)
[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----a23570d88548---------------------------------------)
[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----a23570d88548---------------------------------------)
[Terms](https://policy.medium.com/medium-terms-of-service-9db0094a1e0f?source=post_page-----a23570d88548---------------------------------------)
[Text to speech](https://speechify.com/medium?source=post_page-----a23570d88548---------------------------------------)

