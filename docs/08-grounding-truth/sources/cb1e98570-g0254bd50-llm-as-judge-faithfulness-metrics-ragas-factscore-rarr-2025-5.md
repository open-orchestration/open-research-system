💙 **Making a Difference:** All ad revenue from this site supports educational opportunities for underprivileged communities. 📚
[Akshay Uppal](https://au1206.github.io/ "Akshay Uppal \(Alt + H\)")
  * [Posts](https://au1206.github.io/posts/ "Posts")
  * [Categories](https://au1206.github.io/categories/ "Categories")
  * [Tags](https://au1206.github.io/tags/ "Tags")
  * [About](https://au1206.github.io/about/ "About")
  * [Search](https://au1206.github.io/search/ "Search \(Alt + /\)")


[Home](https://au1206.github.io/) » [Posts](https://au1206.github.io/posts/)
# RAG Evaluation Guide: Metrics, Frameworks & LLM Evaluation in Production
A practical guide to RAG evaluation: faithfulness, context precision, context recall, LLM-as-judge, and how to run LLM evaluation in production using RAGAS, DeepEval, and LangSmith.
February 15, 2026 · 14 min · Akshay Uppal
Table of Contents
  * [Why Traditional Benchmarks Fail RAG Evaluation](https://au1206.github.io/posts/rag-evaluation-guide/#why-traditional-benchmarks-fail-rag-evaluation)
  * [The RAG Evaluation Metric Landscape](https://au1206.github.io/posts/rag-evaluation-guide/#the-rag-evaluation-metric-landscape)
  * [RAG-Specific Evaluation Metrics: The Four Dimensions](https://au1206.github.io/posts/rag-evaluation-guide/#rag-specific-evaluation-metrics-the-four-dimensions)
    * [Faithfulness](https://au1206.github.io/posts/rag-evaluation-guide/#faithfulness)
    * [Context Precision and Recall](https://au1206.github.io/posts/rag-evaluation-guide/#context-precision-and-recall)
    * [Answer Relevancy](https://au1206.github.io/posts/rag-evaluation-guide/#answer-relevancy)
  * [LLM-as-Judge: When It Works and When It Doesn’t](https://au1206.github.io/posts/rag-evaluation-guide/#llm-as-judge-when-it-works-and-when-it-doesnt)
  * [Evaluation Data Construction](https://au1206.github.io/posts/rag-evaluation-guide/#evaluation-data-construction)
  * [Framework Comparison: DeepEval, RAGAS, and LangSmith](https://au1206.github.io/posts/rag-evaluation-guide/#framework-comparison-deepeval-ragas-and-langsmith)
  * [RAG Evaluation vs. Production Observability](https://au1206.github.io/posts/rag-evaluation-guide/#rag-evaluation-vs-production-observability)
  * [Common RAG Evaluation Pitfalls (and How to Avoid Them)](https://au1206.github.io/posts/rag-evaluation-guide/#common-rag-evaluation-pitfalls-and-how-to-avoid-them)
  * [Summary: Building a Robust RAG Evaluation Pipeline](https://au1206.github.io/posts/rag-evaluation-guide/#summary-building-a-robust-rag-evaluation-pipeline)
  * [Resources](https://au1206.github.io/posts/rag-evaluation-guide/#resources)


## Why Traditional Benchmarks Fail RAG Evaluation[#](https://au1206.github.io/posts/rag-evaluation-guide/#why-traditional-benchmarks-fail-rag-evaluation)
If you work with RAG systems in production, you’ve probably noticed that BLEU and ROUGE scores tell you almost nothing useful. A system can score 0.78 BLEU and still hallucinate financial figures. A system with 0.40 BLEU might be more useful to real users. Traditional metrics were designed for narrow, deterministic tasks — machine translation against reference translations, text summarization against human-written summaries — where the space of valid outputs is small and reference-matching is meaningful.
Modern RAG systems break these assumptions. There’s no single “correct” way to phrase an answer, responses depend on retrieved context that varies per query, and the most important failure mode — confabulation — is invisible to n-gram overlap metrics.
This RAG evaluation guide covers what to measure instead, how the metrics work under the hood, and what breaks in practice when you take these systems to production.
![Modern vs traditional metrics](https://au1206.github.io/diagrams/metrics-evolution.png)
* * *
## The RAG Evaluation Metric Landscape[#](https://au1206.github.io/posts/rag-evaluation-guide/#the-rag-evaluation-metric-landscape)
Before picking a LLM evaluation framework, it helps to understand the three families of evaluation approaches and their tradeoffs:
**Lexical / statistical metrics** (BLEU, ROUGE, exact match): Fast, cheap, deterministic. Useful only when you have reference outputs and the task is closed-form. Use for extractive QA, slot-filling, or anywhere a canonical answer exists.
**Model-based metrics** (BERTScore, MoverScore, NLI-based): Use a pretrained model to compare semantic similarity or check entailment. More expensive but correlation with human judgment is better. NLI-based approaches (checking whether claim B is entailed by premise A) underpin most modern faithfulness metrics.
**LLM-as-judge** : Use a capable LLM to score responses on dimensions like correctness, helpfulness, or faithfulness. Highest correlation with human judgment for open-ended tasks, but comes with its own bias catalog (more on this below). Most expensive.
For RAG specifically, you typically want a mix: cheap deterministic checks in CI, model-based NLI for faithfulness at scale, and LLM-judge for a sample of production traffic.
* * *
## RAG-Specific Evaluation Metrics: The Four Dimensions[#](https://au1206.github.io/posts/rag-evaluation-guide/#rag-specific-evaluation-metrics-the-four-dimensions)
![The four pillars of modern RAG evaluation: Faithfulness, Context Precision, Context Recall, and Answer Relevancy](https://au1206.github.io/diagrams/evaluation-taxonomy.png)
### Faithfulness[#](https://au1206.github.io/posts/rag-evaluation-guide/#faithfulness)
Faithfulness measures whether every claim in the response is supported by the retrieved context. The standard implementation:
  1. **Claim extraction** : decompose the response into atomic propositions. “The study ran for 8 weeks and found 67% improvement” becomes [“The study ran for 8 weeks”, “67% of participants improved”].
  2. **Entailment checking** : for each claim, ask an NLI model (or LLM) whether the context logically entails it.
  3. **Score** : `supported_claims / total_claims`



```
from ragas.metrics import faithfulness
from ragas import evaluate
from datasets import Dataset

# A case where the model adds information not in context
data = Dataset.from_dict({
    "question": ["What were the trial results?"],
    "answer": [
        # Model said '2 weeks' — the context says '8 weeks'
        "The treatment showed 67% improvement within just 2 weeks."
    ],
    "contexts": [[
        "The study found that 67% of participants improved after 8 weeks of treatment."
    ]],
    "ground_truth": ["67% of participants improved after 8 weeks."]
})

results = evaluate(data, metrics=[faithfulness])
print(results)
# faithfulness: 0.5  (one claim verified, one hallucinated)

```
copy
**What breaks** : Short responses score artificially high because there are fewer claims to verify. A response of “The results were positive” is technically faithful to almost any positive-outcome context. Also, faithfulness only checks whether claims appear in context — it doesn’t check whether the context is itself accurate.
### Context Precision and Recall[#](https://au1206.github.io/posts/rag-evaluation-guide/#context-precision-and-recall)
These two metrics evaluate the retriever, not the generator. They’re easy to conflate but measure opposite things.
**Context precision** : Of the chunks retrieved, what fraction were actually relevant to answering the question?

```
context_precision = relevant_retrieved / total_retrieved
copy
```

Low precision means your retriever is pulling noise. The generator is forced to work with irrelevant context, which increases hallucination risk — especially if the relevant signal is diluted.
**Context recall** : Of the facts needed to answer the question correctly, what fraction were present in the retrieved chunks?

```
context_recall = facts_in_retrieved / total_facts_needed
copy
```

Low recall means the retriever is missing relevant chunks. No matter how good your generator is, it can’t answer from context it never saw.
The practical implication: if you’re debugging a RAG failure, check these two first. A hallucination with high context recall is a **generator failure** — the answer was there and the model ignored it. A wrong answer with low context recall is a **retriever failure** — fix the retrieval, not the prompt.

```
from ragas.metrics import context_precision, context_recall

# Example with a multi-hop question
data = Dataset.from_dict({
    "question": ["What was the treatment duration and its effect on the control group?"],
    "answer": ["Treatment ran for 8 weeks. The control group showed 12% improvement."],
    "contexts": [[
        "The study ran for 8 weeks.",
        "Treatment group showed 67% improvement.",
        # Missing: control group data — this is a recall failure
    ]],
    "ground_truth": [
        "The treatment lasted 8 weeks. The control group showed 12% improvement."
    ]
})

results = evaluate(data, metrics=[context_precision, context_recall])
# context_precision: 0.67 (2 of 3 chunks relevant)
# context_recall: 0.5 (control group fact missing from context)

```
copy
### Answer Relevancy[#](https://au1206.github.io/posts/rag-evaluation-guide/#answer-relevancy)
Measures whether the response actually addresses the question. This catches a different failure mode from faithfulness: a response can be entirely grounded in context and still not answer what was asked.
The RAGAS implementation uses an interesting approach: generate N synthetic questions from the response, then measure embedding similarity between those questions and the original question. If the response addresses the question, the derived questions should cluster near the original.

```
from ragas.metrics import answer_relevancy

# Faithful but not relevant
data = Dataset.from_dict({
    "question": ["What is the refund timeline for digital products?"],
    "answer": [
        # Faithful to retrieved context, but about the wrong product category
        "Physical products can be returned within 30 days with original packaging."
    ],
    "contexts": [[
        "Physical products can be returned within 30 days with original packaging.",
        "Digital products are non-refundable after download."
    ]],
    "ground_truth": ["Digital products are non-refundable after download."]
})

results = evaluate(data, metrics=[answer_relevancy])
# answer_relevancy: 0.31 — low despite faithful response

```
copy
* * *
## LLM-as-Judge: When It Works and When It Doesn’t[#](https://au1206.github.io/posts/rag-evaluation-guide/#llm-as-judge-when-it-works-and-when-it-doesnt)
LLM-as-judge is increasingly used because it correlates well with human preference, especially for open-ended tasks where lexical or NLI-based metrics fail. But it’s not free of problems.
**Known biases:**
  * **Self-enhancement bias** : models rate their own outputs higher than equivalent outputs from other models. Don’t use GPT-4 to judge GPT-4 outputs.
  * **Verbosity bias** : longer, more elaborate responses are rated higher even when a shorter response is more accurate.
  * **Position bias** (pairwise setting): in A/B comparisons, the first option gets a slight bump. Mitigate by swapping order and averaging.
  * **Format bias** : responses with markdown formatting, headers, and bullet points tend to score higher regardless of content quality.


**Mitigation strategies:**

```
def robust_llm_judge(question: str, response: str, context: str) -> dict:
    """
    More reliable LLM judging with structured output and chain-of-thought.
    Uses a different model family from what generated the response.
    """
    prompt = f"""You are evaluating a RAG system response.

Question: {question}
Retrieved context: {context}
Response: {response}

Evaluate on these dimensions. Think step-by-step before scoring.

1. Faithfulness (0-1): Are all claims in the response supported by the context?
   Reasoning: <explain each claim>
   Score: <0.0-1.0>

2. Relevancy (0-1): Does the response address what was asked?
   Reasoning: <explain>
   Score: <0.0-1.0>

3. Completeness (0-1): Are all aspects of the question addressed?
   Reasoning: <explain>
   Score: <0.0-1.0>

Return valid JSON: {{"faithfulness": X, "relevancy": X, "completeness": X, "reasoning": "..."}}"""

    # Use a different model family from the one being evaluated
    response = anthropic_client.messages.create(
        model="claude-opus-4-7",
        max_tokens=512,
        messages=[{"role": "user", "content": prompt}]
    )
    return json.loads(response.content[0].text)

```
copy
Chain-of-thought helps, but it doesn’t eliminate bias. The safest approach: use LLM-judge for a sample (5-10% of traffic in production, 100% in offline eval) and periodically audit the judge against human labels on a held-out set. If your judge and your human raters disagree on more than 15-20% of cases, the judge is miscalibrated.
* * *
## Evaluation Data Construction[#](https://au1206.github.io/posts/rag-evaluation-guide/#evaluation-data-construction)
This is where most teams underinvest, and it’s the most common reason evaluation results don’t transfer to production.
**The synthetic question trap** : If you generate test questions by asking an LLM “generate questions from this document,” you’ll get questions that are easy to answer from the document. Real user queries are messier, more ambiguous, and often require reasoning across multiple chunks. Synthetic eval sets overestimate your system’s performance.
**What actually works:**
  1. **Mine production logs** — even before you have labels, real queries tell you what your users actually ask. Cluster by intent, then manually label a representative sample.
  2. **Adversarial examples** — include queries the system should refuse: questions outside the document scope, queries for which the answer has changed, ambiguous queries. A system that hallucinates on these is a liability.
  3. **Multi-hop questions** — questions requiring synthesis across multiple documents stress-test both retrieval recall and the generator’s ability to combine information.
  4. **Label faithfulness directly** — for a critical domain (legal, financial, medical), have domain experts annotate which claims in responses are supported vs. hallucinated. This is expensive but gives you ground truth to calibrate your automated metrics.



```
def build_evaluation_dataset(log_store, domain_expert=None):
    """
    Example data pipeline for real-world eval set construction.
    """
    # Step 1: Sample from production logs
    queries = log_store.sample(
        n=500,
        stratify_by="intent_cluster",   # ensure coverage
        date_range="last_60_days"       # avoid recency bias
    )

    # Step 2: Deduplicate near-duplicates
    queries = semantic_dedup(queries, threshold=0.92)

    # Step 3: Run your current system to get responses
    labeled = []
    for q in queries:
        result = rag_system.query(q.text)
        labeled.append({
            "question": q.text,
            "answer": result.answer,
            "contexts": result.retrieved_chunks,
            "intent": q.intent_cluster
        })

    # Step 4: If domain expert available, add faithfulness labels
    if domain_expert:
        labeled = domain_expert.annotate_claims(labeled)

    return Dataset.from_list(labeled)

```
copy
* * *
## Framework Comparison: DeepEval, RAGAS, and LangSmith[#](https://au1206.github.io/posts/rag-evaluation-guide/#framework-comparison-deepeval-ragas-and-langsmith)  
|   | DeepEval  | RAGAS  | LangSmith  |  
| --- | --- | --- | --- |  
| **Focus**  | General LLM testing  | RAG metrics  | Tracing + evaluation  |  
| **Integration style**  | pytest-like  | HuggingFace Datasets  | LangChain-first  |  
| **Metric computation**  | LLM-judge (customizable)  | LLM-judge + NLI  | Configurable  |  
| **Best for**  | CI/CD regression testing  | Offline RAG experimentation  | Production tracing + sampling  |  
| **Main limitation**  | LLM-judge calls add latency/cost  | LLM calls, Requires HF Datasets format  | LangChain coupling  |  
**RAGAS** is the easiest entry point for RAG-specific metrics. The faithfulness, context precision, and context recall implementations are solid and well-documented. The main friction is the `Dataset` format requirement and the fact that all metrics call an LLM internally — budget accordingly.

```
from ragas import evaluate
from ragas.metrics import (
    faithfulness,
    context_precision,
    context_recall,
    answer_relevancy,
)
from datasets import Dataset

# A realistic RAG eval case: financial document QA
data = Dataset.from_dict({
    "question": [
        "What was Q3 operating margin and how did it compare to guidance?",
        "What were the primary drivers of increased SG&A in 2025?"
    ],
    "answer": [
        "Q3 operating margin was 18.2%, which came in 140bps above the guidance range of 16.5-17.0%.",
        "SG&A increased primarily due to higher headcount in sales (up 23% YoY) and expanded marketing spend ahead of the product launch."
    ],
    "contexts": [
        [
            "Q3 2025 operating margin: 18.2%. Full year guidance provided in August was 16.5-17.0%.",
            "Revenue grew 14% YoY to $2.3B in Q3."
        ],
        [
            "SG&A increased $47M YoY, driven by 23% headcount growth in sales and $18M incremental marketing investment related to the Apex product launch."
        ]
    ],
    "ground_truth": [
        "18.2%, 140bps above the 16.5-17.0% guidance.",
        "Higher sales headcount (23% YoY) and increased marketing spend for the Apex launch."
    ]
})

result = evaluate(data, metrics=[faithfulness, context_precision, context_recall, answer_relevancy])
print(result.to_pandas())

```
copy
**DeepEval** is better suited for treating evaluation as a continuous testing concern — it integrates with pytest, supports custom metrics, and makes it natural to add LLM evaluation gates to CI/CD. The tradeoff: every metric invocation calls an LLM, so running the full suite on a large dataset is slow and costly. Structure your test pyramid: a small golden test set in CI (50-100 cases), a larger eval set run less frequently (nightly or pre-release).

```
import pytest
from deepeval import assert_test
from deepeval.test_case import LLMTestCase
from deepeval.metrics import FaithfulnessMetric, ContextualRecallMetric

# Golden test cases — curated, high-confidence ground truth
GOLDEN_CASES = [
    {
        "input": "What was the Q3 operating margin?",
        "expected_output": "18.2%",
        "context": ["Q3 2025 operating margin: 18.2%."],
    },
    # ... more carefully curated cases
]

@pytest.mark.parametrize("case", GOLDEN_CASES)
def test_rag_golden(case):
    result = rag_system.query(case["input"])
    test_case = LLMTestCase(
        input=case["input"],
        actual_output=result.answer,
        expected_output=case["expected_output"],
        retrieval_context=result.retrieved_chunks,
    )
    assert_test(test_case, [
        FaithfulnessMetric(threshold=0.85),
        ContextualRecallMetric(threshold=0.8),
    ])

```
copy
**LangSmith** is primarily an observability platform with evaluation capabilities bolted on. If you’re not using LangChain, the integration is more awkward. Its strength is production tracing — you can log every retrieval and generation step, then run evaluators asynchronously over the logged traces. This makes it easy to measure quality on real traffic without adding latency to the critical path.
* * *
## RAG Evaluation vs. Production Observability[#](https://au1206.github.io/posts/rag-evaluation-guide/#rag-evaluation-vs-production-observability)
![Evaluation \(pre-production, test sets, offline metrics\) versus Observability \(production, live traffic, real-time monitoring\)](https://au1206.github.io/diagrams/eval-vs-observability.png)
These two things solve different problems and require different infrastructure.
**Evaluation** is offline: you run your system against a fixed dataset, compute metrics, and use the results to decide whether to deploy. It’s where you catch regressions before they hit users.
**Observability** is online: you instrument your production system, sample traffic, run lightweight quality checks asynchronously, and alert when metrics degrade. LLMs fail silently — a hallucinated but plausible answer doesn’t throw an exception — so you need this layer even when evaluation looks good in staging.
The critical point: **your evaluation distribution will drift from your production distribution**. Users ask questions you didn’t anticipate. Documents in your corpus change. Models get updated. Build a pipeline to continuously harvest production queries back into your eval set.
![Production RAG observability stack: user query flows through retrieval and generation, with async evaluation, metrics collection, and threshold-based alerting](https://au1206.github.io/diagrams/production-stack.png)

```
import asyncio
import random
from dataclasses import dataclass

@dataclass
class RAGResponse:
    answer: str
    retrieved_chunks: list[str]
    latency_ms: float
    input_tokens: int
    output_tokens: int

class InstrumentedRAGSystem:
    """
    Production RAG with async quality sampling.
    Evaluation runs off the critical path — does not add latency to user requests.
    """

    EVAL_SAMPLE_RATE = 0.05  # evaluate 5% of traffic

    def __init__(self, retriever, generator, tracer, evaluator):
        self.retriever = retriever
        self.generator = generator
        self.tracer = tracer
        self.evaluator = evaluator

    async def query(self, question: str, user_id: str) -> RAGResponse:
        with self.tracer.span("rag_query", {"user_id": user_id}) as span:
            import time
            t0 = time.monotonic()

            chunks = await self.retriever.retrieve(question, top_k=5)
            span.set("retrieval.chunk_count", len(chunks))

            response = await self.generator.generate(question, chunks)
            latency_ms = (time.monotonic() - t0) * 1000

            span.set("generation.input_tokens", response.input_tokens)
            span.set("generation.output_tokens", response.output_tokens)
            span.set("latency_ms", latency_ms)

            # Fire-and-forget quality evaluation — does not block response
            if random.random() < self.EVAL_SAMPLE_RATE:
                asyncio.create_task(
                    self._evaluate_async(question, response.answer, chunks, span.trace_id)
                )

            return RAGResponse(
                answer=response.answer,
                retrieved_chunks=chunks,
                latency_ms=latency_ms,
                input_tokens=response.input_tokens,
                output_tokens=response.output_tokens,
            )

    async def _evaluate_async(self, question, answer, chunks, trace_id):
        scores = await self.evaluator.score(question, answer, chunks)
        self.tracer.attach_scores(trace_id, scores)

        if scores["faithfulness"] < 0.7:
            self.tracer.flag_for_review(trace_id, reason="low_faithfulness")

```
copy
**What to alert on** : not every metric deserves an immediate page. A useful mental model:  
| Metric  | Alert level  | Threshold example  |  
| --- | --- | --- |  
| Faithfulness p25 (rolling 1h)  | Page  | < 0.65  |  
| Context recall p50  | Slack  | < 0.75  |  
| Latency p95  | Page  | > 2000ms  |  
| Error rate  | Page  | > 1%  |  
| Cost per request (rolling 24h)  | Slack  | > 1.5x baseline  |  
Use a rolling window rather than point-in-time metrics. A single bad batch response or a 30-second spike shouldn’t page anyone.
* * *
## Common RAG Evaluation Pitfalls (and How to Avoid Them)[#](https://au1206.github.io/posts/rag-evaluation-guide/#common-rag-evaluation-pitfalls-and-how-to-avoid-them)
**Evaluating retrieval and generation together obscures where failures originate.** Compute context recall and context precision separately before computing faithfulness. If context recall is low, fix the retriever — prompt engineering won’t help.
**Automated metrics are only as good as your eval set.** If your eval set is easy or synthetic, you’ll have high automated scores and poor production quality. Set aside budget for human annotation on a representative production sample, especially for the cases where automated metrics score highest (to catch false positives in your evaluator).
**LLM-as-judge is biased and drifts.** The same judge model will score the same response differently across versions. Re-calibrate your judge against human labels every time you change either the judge model or the system under test. Don’t use a model to evaluate its own outputs.
**Sampling rate for production evaluation matters.** 5% is often cited but the right rate depends on query volume and variance. At low volume (< 1000 queries/day), evaluate more aggressively (20-30%) to get statistically stable estimates. At high volume, 1-2% may be enough. Use stratified sampling by intent cluster — rare but high-stakes query types need overrepresentation.
**Faithfulness doesn’t catch all hallucinations.** A model can be “faithful” to retrieved context that is itself outdated or wrong. Faithfulness measures consistency with retrieved chunks, not factual accuracy. For domains where the ground truth evolves (financial data, medical literature, legal regulations), you need a separate accuracy check against authoritative sources.
* * *
## Summary: Building a Robust RAG Evaluation Pipeline[#](https://au1206.github.io/posts/rag-evaluation-guide/#summary-building-a-robust-rag-evaluation-pipeline)
RAG evaluation is a measurement system, not a single score. The three layers most production teams converge on:
  1. **Offline eval (pre-deploy):** Run RAGAS metrics — faithfulness, context precision, context recall, answer relevancy — against a curated eval set. Catches regressions before they reach users.
  2. **CI/CD regression gates:** Use DeepEval with pytest. A small golden test set (50–100 well-annotated cases) with hard thresholds. Fails the build if faithfulness drops below your baseline.
  3. **Production monitoring:** Sample 5–20% of live traffic (depending on volume), run async LLM-as-judge scoring off the critical path, and alert on rolling metric windows — not point-in-time spikes.


If you’re starting from scratch: RAGAS first to understand your baseline → DeepEval once you have a stable eval set → production observability when you’re shipping to real users.
* * *
## Resources[#](https://au1206.github.io/posts/rag-evaluation-guide/#resources)
  * [RAGAS paper](https://arxiv.org/abs/2309.15217) — the metric definitions and methodology behind the Ragas library
  * [Judging the Judges](https://arxiv.org/abs/2401.10020) — systematic analysis of LLM-as-judge biases
  * [ARES: An Automated Evaluation Framework for RAG](https://arxiv.org/abs/2311.09476) — alternative approach using classifier-based evaluation
  * [Hallucination Leaderboard](https://github.com/vectara/hallucination-leaderboard) — cross-model hallucination comparison on a standardized task


  * [RAG Evaluation](https://au1206.github.io/tags/rag-evaluation/)
  * [LLM Evaluation](https://au1206.github.io/tags/llm-evaluation/)
  * [RAG in Production](https://au1206.github.io/tags/rag-in-production/)
  * [LLM as Judge](https://au1206.github.io/tags/llm-as-judge/)
  * [RAGAS](https://au1206.github.io/tags/ragas/)
  * [DeepEval](https://au1206.github.io/tags/deepeval/)
  * [LangSmith](https://au1206.github.io/tags/langsmith/)
  * [Hallucination Detection](https://au1206.github.io/tags/hallucination-detection/)
  * [LLM Testing](https://au1206.github.io/tags/llm-testing/)
  * [Retrieval Augmented Generation](https://au1206.github.io/tags/retrieval-augmented-generation/)

[Next »  
DiT Annotated Paper](https://au1206.github.io/posts/2022-04-21-dit/)
  * [](https://x.com/intent/tweet/?text=RAG%20Evaluation%20Guide%3a%20Metrics%2c%20Frameworks%20%26%20LLM%20Evaluation%20in%20Production&url=https%3a%2f%2fau1206.github.io%2fposts%2frag-evaluation-guide%2f&hashtags=RAGEvaluation%2cLLMEvaluation%2cRAGinProduction%2cLLMasJudge%2cRAGAS%2cDeepEval%2cLangSmith%2cHallucinationDetection%2cLLMTesting%2cRetrievalAugmentedGeneration)
  * [](https://www.linkedin.com/shareArticle?mini=true&url=https%3a%2f%2fau1206.github.io%2fposts%2frag-evaluation-guide%2f&title=RAG%20Evaluation%20Guide%3a%20Metrics%2c%20Frameworks%20%26%20LLM%20Evaluation%20in%20Production&summary=RAG%20Evaluation%20Guide%3a%20Metrics%2c%20Frameworks%20%26%20LLM%20Evaluation%20in%20Production&source=https%3a%2f%2fau1206.github.io%2fposts%2frag-evaluation-guide%2f)
  * [](https://reddit.com/submit?url=https%3a%2f%2fau1206.github.io%2fposts%2frag-evaluation-guide%2f&title=RAG%20Evaluation%20Guide%3a%20Metrics%2c%20Frameworks%20%26%20LLM%20Evaluation%20in%20Production)
  * [](https://facebook.com/sharer/sharer.php?u=https%3a%2f%2fau1206.github.io%2fposts%2frag-evaluation-guide%2f)
  * [](https://api.whatsapp.com/send?text=RAG%20Evaluation%20Guide%3a%20Metrics%2c%20Frameworks%20%26%20LLM%20Evaluation%20in%20Production%20-%20https%3a%2f%2fau1206.github.io%2fposts%2frag-evaluation-guide%2f)
  * [](https://telegram.me/share/url?text=RAG%20Evaluation%20Guide%3a%20Metrics%2c%20Frameworks%20%26%20LLM%20Evaluation%20in%20Production&url=https%3a%2f%2fau1206.github.io%2fposts%2frag-evaluation-guide%2f)
  * [](https://news.ycombinator.com/submitlink?t=RAG%20Evaluation%20Guide%3a%20Metrics%2c%20Frameworks%20%26%20LLM%20Evaluation%20in%20Production&u=https%3a%2f%2fau1206.github.io%2fposts%2frag-evaluation-guide%2f)

© 2026 [Akshay Uppal](https://au1206.github.io/) · Powered by [Hugo](https://gohugo.io/) & [PaperMod](https://github.com/adityatelange/hugo-PaperMod/)[ ](https://au1206.github.io/posts/rag-evaluation-guide/#top "Go to Top \(Alt + G\)")

