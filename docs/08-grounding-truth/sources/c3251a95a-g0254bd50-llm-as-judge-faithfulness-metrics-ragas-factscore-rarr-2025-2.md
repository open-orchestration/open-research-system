[Skip to content](https://letsdatascience.com/blog/llm-evaluation-ragas-llm-as-judge-and-production-evals#main-content)
[![LDS Logo](https://letsdatascience.com/lds_logo.svg) LDS Let's Data ScienceLEARN • BUILD • STAY AHEAD ](https://letsdatascience.com/)
  * [News](https://letsdatascience.com/news)
  * [Blog](https://letsdatascience.com/blog)
  * Learn
  * [Code Problems](https://letsdatascience.com/problems)
  * [Pricing](https://letsdatascience.com/pricing)
  * [Contact](https://letsdatascience.com/contact)


[Sign in](https://letsdatascience.com/login?redirect=%2Fblog%2Fllm-evaluation-ragas-llm-as-judge-and-production-evals)
On this page0%
[Why Traditional ML Metrics Break for LLMs](https://letsdatascience.com/blog/llm-evaluation-ragas-llm-as-judge-and-production-evals#why-traditional-ml-metrics-break-for-llms)
[Reference-Based vs Reference-Free Evaluation](https://letsdatascience.com/blog/llm-evaluation-ragas-llm-as-judge-and-production-evals#reference-based-vs-reference-free-evaluation)
[RAGAS: Evaluating RAG Pipelines Systematically](https://letsdatascience.com/blog/llm-evaluation-ragas-llm-as-judge-and-production-evals#ragas-evaluating-rag-pipelines-systematically)
[LLM-as-Judge: Scalable Human-Quality Evaluation](https://letsdatascience.com/blog/llm-evaluation-ragas-llm-as-judge-and-production-evals#llm-as-judge-scalable-human-quality-evaluation)
[Eval Cost at Scale: Choosing Your Judge](https://letsdatascience.com/blog/llm-evaluation-ragas-llm-as-judge-and-production-evals#eval-cost-at-scale-choosing-your-judge)
[The Production Eval Toolkit in 2026](https://letsdatascience.com/blog/llm-evaluation-ragas-llm-as-judge-and-production-evals#the-production-eval-toolkit-in-2026)
[Building an Eval Pipeline from Scratch](https://letsdatascience.com/blog/llm-evaluation-ragas-llm-as-judge-and-production-evals#building-an-eval-pipeline-from-scratch)
[Evaluating Agents: Beyond Question-Answer Pairs](https://letsdatascience.com/blog/llm-evaluation-ragas-llm-as-judge-and-production-evals#evaluating-agents-beyond-question-answer-pairs)
[Common Mistakes in LLM Evaluation](https://letsdatascience.com/blog/llm-evaluation-ragas-llm-as-judge-and-production-evals#common-mistakes-in-llm-evaluation)
[When to Use Each Approach](https://letsdatascience.com/blog/llm-evaluation-ragas-llm-as-judge-and-production-evals#when-to-use-each-approach)
[Conclusion](https://letsdatascience.com/blog/llm-evaluation-ragas-llm-as-judge-and-production-evals#conclusion)
[Interview Questions](https://letsdatascience.com/blog/llm-evaluation-ragas-llm-as-judge-and-production-evals#interview-questions)
Like
Save
Back to top
[](https://letsdatascience.com/)[Blog](https://letsdatascience.com/blog)[GenAI & LLMs](https://letsdatascience.com/blog/genai-llms)
# LLM Evaluation: RAGAS, LLM-as-Judge, and Production Evals
DS
[LDS Team](https://letsdatascience.com/author/lds-team)
Let's Data Science
Mar 17, 2026March 17, 202622 min readAudio · 8 listens
Read summary
Listen Along
0:00/ 0:00
AI voice
151x15
[](https://open.spotify.com/show/0x4laIZ3OSlnAlr0R7gXsr)[](https://music.amazon.com/podcasts/f245918a-83ab-4b40-9730-d6e5446ad66e/let's-data-science-%E2%80%94-ai-news-daily)[](https://www.youtube.com/@letsdatascience)
You can't improve what you can't measure. That's true for any system, but LLMs make it uniquely hard. The output is open-ended text, correctness is often subjective, and a model can sound completely confident while making things up. Traditional ML evaluation — accuracy, F1, confusion matrices — was designed for systems with clear right and wrong answers. LLMs mostly don't have those.
This article covers the practical toolkit for evaluating LLM systems in production: what RAGAS measures and how it works, why LLM-as-Judge has become the default for open-ended evaluation, how to wire together a production eval pipeline, and how to evaluate AI agents that reason across multiple steps. We'll use a single running example throughout: a customer support RAG chatbot for a SaaS product that answers questions by retrieving from a knowledge base of help docs. Your job is to measure faithfulness, answer quality, and hallucination rate across 500 test queries and keep those numbers healthy as the system evolves.
### Why Traditional ML Metrics Break for LLMs
Traditional ML evaluation assumes you have a ground truth label and a predicted label. A spam classifier either got it right or wrong. A regression model's error is a number you can compute exactly.
LLM outputs break both assumptions. When a customer asks "how do I reset my password?", there are dozens of correct answers — different wordings, different levels of detail, different tones. BLEU and ROUGE, the metrics inherited from machine translation, count n-gram overlap between the model's output and a reference answer. If the reference says "click the reset button" and the model says "press the reset button", ROUGE penalizes that as a miss. More critically, neither metric detects hallucination: a model that generates a fluent, plausible answer with completely wrong information scores fine on ROUGE as long as it uses similar words.
The two problems are distinct:
  1. **Semantic correctness** — did the answer mean the right thing?
  2. **Faithfulness** — did the answer stay within the bounds of what the retrieved context says?


ROUGE and BLEU capture neither. This is why RAG systems in particular need purpose-built evaluation.
### Reference-Based vs Reference-Free Evaluation
![LLM evaluation paradigms: reference-based vs reference-free comparison](https://letsdatascience.com/images/blog/llm-evaluation-ragas-llm-as-judge/evaluation-paradigms.svg)Click to expandLLM evaluation paradigms: reference-based vs reference-free comparison
Every LLM evaluation approach falls into one of two categories.
**Reference-based evaluation** compares model output against a gold-standard answer. You need a labeled dataset: questions paired with correct answers. This works well for factual QA ("what's the capital of France?") but poorly for open-ended generation. Building a high-quality labeled set is expensive, and even when you have one, semantic equivalence is hard to capture with string matching. The benefit is determinism — you don't need another LLM to judge, and scores are reproducible.
**Reference-free evaluation** judges output without a predefined correct answer. Instead of asking "does this match the reference?", it asks "is this internally consistent with the context provided?" or "does this answer the question?" This is where frameworks like RAGAS and the LLM-as-Judge method live. The tradeoff: you depend on a judge model, which introduces its own variability and bias.
For production RAG systems, reference-free evaluation is almost always the right starting point. Getting labeled data at scale is hard; checking whether an answer contradicts the retrieved document it claims to be based on is much more tractable.
**Key Insight:** Reference-free eval doesn't mean unsupervised. You're still grounding the evaluation in structure — using the system's own inputs (question, context, answer) rather than an external label.
### RAGAS: Evaluating RAG Pipelines Systematically
RAGAS (RAG Assessment) is an open-source evaluation framework built specifically for RAG pipelines. Originally released by Exploding Gradients in 2023 and covered in the [RAGAS paper](https://arxiv.org/abs/2309.15217) (Es et al., 2023), RAGAS has evolved significantly. The current version (v0.2+, with v0.4 released in late 2025) expanded beyond RAG to cover any LLM application, including agentic workflows. The API changed substantially between v0.1 and v0.2 — if you're following older tutorials, the code won't work.
![RAGAS four metrics pipeline showing faithfulness, answer relevancy, context precision, context recall](https://letsdatascience.com/images/blog/llm-evaluation-ragas-llm-as-judge/ragas-metrics.svg)Click to expandRAGAS four metrics pipeline showing faithfulness, answer relevancy, context precision, context recall
RAGAS defines four core metrics that together cover the two components of a RAG system: the retriever and the generator. Each metric takes the triple (Question, Context, Answer) as input and outputs a score between 0 and 1.
#### Faithfulness: Does the Answer Stay Within the Context?
Faithfulness measures whether the generated answer is factually grounded in the retrieved context. A score of 1.0 means every claim in the answer can be traced back to something in the context. A score of 0.5 means half the claims are unsupported.
Faithfulness=statements supported by contexttotal statements in answer\text{Faithfulness} = \frac{\text{statements supported by context}}{\text{total statements in answer}}Faithfulness=total statements in answerstatements supported by context​
Where:
  * The numerator counts statements in the generated answer that are directly entailed by or consistent with the retrieved context
  * The denominator is the total number of atomic factual statements extracted from the generated answer
  * RAGAS uses an LLM internally to both decompose the answer into atomic statements and to verify each one against the context


**In Plain English:** Your customer support chatbot answers "Password resets expire after 24 hours and require a verified email." RAGAS splits this into two claims: (1) resets expire after 24 hours, (2) a verified email is required. It checks each claim against the retrieved help docs. If only claim 2 appears in the docs, faithfulness = 0.5. That missing "24 hours" is a hallucination, and faithfulness caught it.
#### Answer Relevancy: Does the Answer Address the Question?
Answer relevancy measures whether the generated answer addresses what was asked. RAGAS computes this by having an LLM generate several synthetic questions from the answer, then measuring the cosine similarity between those generated questions and the original question using embeddings.
High answer relevancy means the answer's content is tightly focused on what was asked. Low relevancy suggests the answer went off-topic, was evasive, or answered a different question.
**Common Pitfall:** Answer relevancy says nothing about whether the answer is correct — a confidently wrong answer can score high on relevancy. That's why you need faithfulness alongside it.
#### Context Precision: Is the Retrieved Context Relevant?
Context precision evaluates the retriever, not the generator. It measures what fraction of the retrieved context chunks are relevant to answering the question. If your RAG retrieves 5 chunks but only 2 are useful, context precision is 0.4.
Low context precision is a retriever problem. The LLM receives a lot of noise in its context window, which both wastes tokens and increases the risk that irrelevant content contaminates the answer.
#### Context Recall: Did You Retrieve What You Needed?
Context recall measures whether the retrieved context contains all the information needed to answer the question correctly. This metric requires a ground-truth answer — RAGAS checks how many pieces of the reference answer can be attributed to the retrieved context.
If your knowledge base has the answer but your retriever didn't surface the right chunks, context recall drops. It directly diagnoses retrieval gaps.  
| Metric  | What It Measures  | Requires Reference?  | Diagnoses  |  
| --- | --- | --- | --- |  
| Faithfulness  | Answer grounded in context  | No  | Generator hallucination  |  
| Answer Relevancy  | Answer addresses question  | No  | Generator focus  |  
| Context Precision  | Retrieved context is relevant  | No  | Retriever noise  |  
| Context Recall  | Retrieved context is complete  | Yes  | Retrieval gaps  |  
#### Additional RAGAS Metrics Worth Knowing
RAGAS v0.2+ added metrics beyond the original four. Two are particularly useful in production:
**Noise Sensitivity** measures how often the system makes incorrect claims based on irrelevant retrieved documents. It's scored 0 to 1, with lower being better. If your retriever occasionally fetches a completely unrelated chunk and the generator still hallucinates from it, noise sensitivity catches that failure mode that faithfulness might miss.
**Context Entity Recall** checks whether critical named entities (people, dates, product names, version numbers) in the reference answer appear in the retrieved context. For customer support specifically, this matters: if a user asks about "Plan Pro v3" and the retriever surfaces docs for "Plan Pro v2", entity recall drops while other metrics might look fine.
#### Running RAGAS in Practice (v0.2+ API)
The v0.2 API changed significantly from v0.1. The old `Dataset.from_dict()` pattern is gone — RAGAS now uses `EvaluationDataset` and `SingleTurnSample`, and metrics are initialized with the evaluator LLM explicitly rather than relying on global state.
Here's how to set up a RAGAS evaluation pipeline for the customer support chatbot using the current API:
python
Copy

```
from ragas import EvaluationDataset, SingleTurnSample, evaluate
from ragas.metrics import Faithfulness, AnswerRelevancy, ContextPrecision, ContextRecall
from ragas.llms import LangchainLLMWrapper
from langchain_openai import ChatOpenAI

# Initialize the evaluator LLM explicitly (v0.2+ requirement)
evaluator_llm = LangchainLLMWrapper(ChatOpenAI(model="gpt-4o"))

# Build the evaluation dataset
samples = [
    SingleTurnSample(
        user_input="How do I reset my password?",
        response="To reset your password, go to Settings > Security and click 'Reset Password'. You'll receive an email within 5 minutes.",
        retrieved_contexts=[
            "Password resets are initiated from Settings > Security. Reset emails arrive within 5 minutes."
        ],
        reference="Navigate to Settings > Security, click Reset Password, and check your email.",
    ),
    SingleTurnSample(
        user_input="Can I export my data in CSV format?",
        response="Yes, you can export data as CSV from the Reports tab under Export Options.",
        retrieved_contexts=[
            "Data export is available in CSV and JSON formats from Reports > Export Options."
        ],
        reference="Go to Reports tab, click Export Options, and select CSV.",
    ),
    # ... more samples
]

dataset = EvaluationDataset(samples=samples)

# Initialize metrics with explicit LLM (not global state)
result = evaluate(
    dataset=dataset,
    metrics=[
        Faithfulness(llm=evaluator_llm),
        AnswerRelevancy(llm=evaluator_llm),
        ContextPrecision(llm=evaluator_llm),
        ContextRecall(llm=evaluator_llm),
    ],
)

print(result)
# {'faithfulness': 0.87, 'answer_relevancy': 0.91,
#  'context_precision': 0.79, 'context_recall': 0.83}

```

RAGAS runs LLM calls under the hood to decompose statements and perform entailment checks. For 500 queries, expect 2,000 to 5,000 LLM calls depending on answer length — budget accordingly.
**Pro Tip:** Run RAGAS on a stratified sample rather than your entire query log. 100 to 200 representative queries evaluated daily is more actionable than 10,000 queries evaluated monthly.
### LLM-as-Judge: Scalable Human-Quality Evaluation
The LLM-as-Judge method uses a stronger language model to evaluate the output of a weaker one (or the same model in a different context). Introduced formally in the [MT-Bench paper](https://arxiv.org/abs/2306.05685) by Zheng et al. (2023), the method has become standard practice at most AI companies by 2025.
The core finding: GPT-4 judging agrees with human expert judgments at approximately **80%** agreement on most evaluation tasks, while being 500x cheaper per evaluation than human annotation. That makes it the only practical approach for continuous evaluation of LLM systems at production scale.
#### Two Scoring Modes
**Direct scoring** asks the judge to rate output on a rubric (typically 1 to 10). You provide the question, the model's response, and a scoring guide. The judge returns a score and an explanation.
**Pairwise comparison** presents two responses side-by-side and asks which is better. This is more reliable for detecting subtle quality differences, and it's harder for the judge to anchor on arbitrary numeric scales. The downside: you need pairs, which doubles the evaluation cost.
For production monitoring, direct scoring scales better. For A/B testing prompt changes, pairwise comparison gives cleaner signal.
#### A Practical Eval Prompt
Here's a concrete LLM-as-Judge prompt for evaluating customer support responses:
code
Copy

```
You are evaluating a customer support AI assistant. Score the following response on three dimensions.

QUESTION: {question}
CONTEXT FROM KNOWLEDGE BASE: {retrieved_context}
ASSISTANT RESPONSE: {response}

Score each dimension from 1 to 5:
- FAITHFULNESS (1-5): Does every claim in the response appear in the provided context?
  5 = fully grounded, 1 = multiple unsupported claims
- HELPFULNESS (1-5): Does the response directly solve the user's problem with actionable steps?
  5 = complete solution, 1 = vague or off-topic
- TONE (1-5): Is the response professional, clear, and appropriately concise?
  5 = excellent, 1 = confusing, rude, or excessively long

Return JSON: {"faithfulness": X, "helpfulness": X, "tone": X, "reasoning": "..."}

```

The JSON output format matters: it makes the judge's output parseable and dramatically reduces cases where the judge writes prose you can't aggregate.
#### Bias Risks You Need to Know
Research from 2024 to 2025 has mapped the bias landscape in LLM judges much more rigorously than the original MT-Bench paper. A 2025 paper at IJCNLP analyzed position bias across 15 judge models and over 150,000 evaluation instances, finding that position bias is not random — it varies systematically by task type and by the quality gap between the solutions being compared. A separate framework called CALM identified 12 distinct bias types in LLM-as-Judge systems.
The four that matter most in practice:
**Verbosity bias** : LLM judges systematically prefer longer responses. A 200-word answer that says nothing useful often scores higher than a 50-word answer that perfectly solves the problem. Research quantifies this as approximately **15%** score inflation for verbose answers. Counter this by adding explicit instructions like "brevity is preferred if the answer is complete."
**Self-enhancement bias** : Models rate their own outputs higher than outputs from competing models. Models consistently rate their own outputs higher than outputs from competing models. Don't use a model to judge its own outputs against competitors without a human validation step.
**Position bias** : In pairwise comparisons, judges often prefer whichever response comes first, with GPT-4 showing approximately **40%** inconsistency when the same pair is presented in reversed order. The fix is to run each comparison twice with positions swapped and average the results.
**Sycophancy toward assertive claims** : Judges tend to rate confident-sounding incorrect answers higher than hedged correct ones. A response that says "you absolutely must do X" may outscore a more accurate "it depends on Y."
**Warning:** Eval scores from an LLM judge are only as reliable as your judge prompt. Always validate your judge against a small set of human-labeled examples before trusting its scores at scale.
### Eval Cost at Scale: Choosing Your Judge
Not all judge models cost the same. Running evaluations across 1,000 test cases with RAGAS (which generates multiple LLM calls per sample) adds up quickly. The practical comparison:  
| Judge Model  | Cost per 1K eval calls (est.)  | Human Agreement  | Best For  |  
| --- | --- | --- | --- |  
| GPT-4o  | ~$2–$5  | ~80%  | General-purpose, balanced cost/quality  |  
| GPT-4o mini  | ~$0.15–$0.40  | ~72%  | High-volume monitoring, low-stakes evals  |  
| Claude 3.5 Sonnet  | ~$3–$6  | ~79%  | Long rubrics, complex criteria (caching helps)  |  
| Claude 3 Haiku  | ~$0.25–$0.60  | ~68%  | Cost-constrained production sampling  |  
| Fine-tuned judge  | ~$0.10–$0.50  | ~82–85%  | High-volume, domain-specific evals  |  
Claude's prompt caching makes a meaningful difference when your rubric is long and reused across many calls — the cached portion costs **90%** less. For an LLM-as-Judge setup where the evaluation criteria stays constant, this can halve the total cost of running Claude as judge. For simple short rubrics, GPT-4o mini at $0.20 per 1,000 calls is hard to beat on pure economics.
**Key Insight:** A fine-tuned small model (7B to 13B) that you've calibrated on 500 human-labeled examples can outperform GPT-4o as a judge for your specific domain at a fraction of the cost. The investment in calibration data pays off at scale.
### The Production Eval Toolkit in 2026
Beyond RAGAS and custom LLM-as-Judge prompts, several frameworks handle the full eval lifecycle.
![Production LLM evaluation pipeline from traffic sampling to prompt fixes](https://letsdatascience.com/images/blog/llm-evaluation-ragas-llm-as-judge/eval-pipeline.svg)Click to expandProduction LLM evaluation pipeline from traffic sampling to prompt fixes
#### DeepEval: pytest for LLMs
[DeepEval](https://github.com/confident-ai/deepeval) treats LLM evaluation like unit testing. You write test cases using a familiar pytest-style syntax and define assertions on LLM output. The library shipped its 50th metric in 2025 and added significant agent evaluation capabilities, including a DAG (Directed Acyclic Graph) metric that structures evaluation as a decision tree for deterministic, customizable scoring.
python
Copy

```
from deepeval import evaluate
from deepeval.metrics import FaithfulnessMetric, AnswerRelevancyMetric
from deepeval.test_case import LLMTestCase

test_case = LLMTestCase(
    input="How do I cancel my subscription?",
    actual_output="To cancel, go to Settings > Billing > Cancel Plan.",
    retrieval_context=[
        "Subscriptions can be cancelled at any time from Settings > Billing."
    ],
)

faithfulness_metric = FaithfulnessMetric(threshold=0.8)
relevancy_metric = AnswerRelevancyMetric(threshold=0.7)

evaluate([test_case], [faithfulness_metric, relevancy_metric])

```

DeepEval integrates with pytest's CI/CD hooks, which means you can gate deployments: if the average faithfulness score drops below 0.80, the pipeline fails. This is exactly the kind of regression guard that prevents quality degradation from going unnoticed in a busy release cycle.
#### Braintrust: Eval + Tracing in One Place
[Braintrust](https://www.braintrustdata.com/) bundles tracing, evaluation, and human review into a single platform. Every LLM call is logged automatically. You can run eval functions over logged traces, compare score distributions between prompt versions, and queue low-scoring responses for human review — all from the same UI.
Braintrust is trusted by teams at Notion, Stripe, and Vercel for this reason: it blocks deployments when quality degrades, provides statistical significance testing for prompt changes, and handles the full lifecycle without requiring a team to wire together separate tools. The tradeoff is vendor lock-in — Braintrust's proxy-based logging approach ties you to their platform.
#### Arize Phoenix: Open-Source Observability
[Arize Phoenix](https://phoenix.arize.com/) is the open-source option for LLM tracing and eval. It supports OpenTelemetry-based tracing, integrates with any LLM framework (LangChain, LlamaIndex, direct API calls) without code changes beyond adding a tracer, and deploys with one Docker command. Evaluations run as async jobs over stored traces.
Phoenix added strong agent evaluation support in 2025, capturing complete multi-step agent traces. It's the right choice when you want full data control — traces stay in your infrastructure — or when compliance requirements prevent sending data to a cloud SaaS.
#### Langfuse: Prompt Management + Evals
[Langfuse](https://langfuse.com/) occupies the tracing-plus-prompt-management space. It logs every prompt and completion, lets you version prompts, and runs evals over historical traces. The tight coupling between prompt versions and eval scores makes it easy to answer "did the prompt change on March 5th cause the faithfulness drop we saw on March 6th?" Langfuse also supports a native OTel instrumentation path, making it easy to instrument any framework without SDK changes.  
| Framework  | Primary Strength  | Hosting  | Best For  |  
| --- | --- | --- | --- |  
| DeepEval  | pytest integration, CI/CD gating, 50+ metrics  | Self-hosted or cloud  | Regression testing, pre-deploy checks  |  
| Braintrust  | Full eval lifecycle, deployment blocking  | Cloud  | Teams wanting one-stop-shop  |  
| Arize Phoenix  | Open-source, OTel tracing, agent traces  | Self-hosted  | Data-sensitive environments  |  
| Langfuse  | Prompt versioning + evals, OTel support  | Cloud or self-hosted  | Teams iterating on prompts frequently  |  
### Building an Eval Pipeline from Scratch
An eval pipeline is only useful if it's automatic and acted on. Here's the minimal viable setup for a production RAG system:
**What to evaluate:**
  * Faithfulness (per-response, sampled at 5 to **10%** of traffic)
  * Answer relevancy (same sample)
  * Latency (every request — this is cheap)
  * Refusal rate (the model saying "I don't know" — unusually high suggests retrieval problems)


**How often:**
  * Automated evals: daily, over the previous day's sample
  * Regression suite: every deployment, against 200 fixed test cases
  * Human spot-check: weekly, 20 to 30 randomly sampled responses


**How to act on results:** Set alert thresholds for each metric. If faithfulness drops below 0.75 (from a normal range of 0.85 to 0.90), that's a signal to inspect: did the knowledge base change? Did a new topic area start getting queries the retriever wasn't trained on? Did a recent prompt change unintentionally loosen grounding?
Never respond to a score drop by tuning the eval threshold — that's gaming the measurement, not fixing the problem.
### Evaluating Agents: Beyond Question-Answer Pairs
![Agent evaluation framework showing tool call accuracy, planning quality, and task completion layers](https://letsdatascience.com/images/blog/llm-evaluation-ragas-llm-as-judge/agent-eval-layers.svg)Click to expandAgent evaluation framework showing tool call accuracy, planning quality, and task completion layers
Standard RAG evaluation assumes a simple question-in, answer-out structure. AI agents — systems that use tools, plan across steps, and complete multi-turn tasks — need additional eval dimensions. If you're building agents, [Function Calling and Tool Use in AI Agents](https://letsdatascience.com/blog/function-calling-tool-use-ai-agents) covers the mechanics that drive agent behavior.
For agent evaluation, three layers matter:
**Tool call accuracy** asks: did the agent invoke the right tool with the right parameters? This is reference-based — you need a labeled dataset of tasks with known correct tool sequences. Score each step: correct tool chosen (binary), correct parameters passed (can be partial credit), correct order in multi-step sequences.
**Planning quality** asks: for multi-step tasks, did the agent decompose the goal correctly? LLM-as-Judge works well here. Give the judge the task, the agent's plan, and a rubric for "complete and logical decomposition." RAGAS includes a Topic Adherence metric and Agent Goal Accuracy metric for this layer. DeepEval's 2025 DAG metric is well-suited for planning evaluation because it structures the evaluation as a decision tree, making it more deterministic than a simple 1-to-5 rubric.
**Task completion rate** asks: did the agent successfully finish the end-to-end task? This is the ultimate metric — binary pass/fail per task, evaluated in a sandboxed environment where you verify the actual outcome, not just the final response.
**Key Insight:** Agent evals cost significantly more to automate than single-turn evals. Each task run is expensive, failure modes are more complex (wrong plan, wrong tool, correct tool with wrong params), and ground truth is harder to define for open-ended tasks. Start by manually labeling 50 to 100 representative task scenarios before building automation around them.
For agentic RAG systems specifically — where an agent retrieves, reasons, and potentially re-retrieves before answering — [Agentic RAG: Self-Correcting Retrieval](https://letsdatascience.com/blog/agentic-rag-self-correcting-retrieval) covers the architecture patterns that inform what you're evaluating.
### Common Mistakes in LLM Evaluation
**Evaluating on training data.** If you fine-tuned your model on a dataset and then evaluate on the same dataset, you'll see inflated scores that evaporate in production. Always hold out a test set from the start.
**No baseline.** Evaluating your current system in isolation tells you nothing. You need a baseline — whether that's the previous prompt version, a simpler rule-based fallback, or a smaller model — to know if your scores are good or bad. A faithfulness score of 0.82 sounds high until you learn that the naive baseline scored 0.85.
**Ignoring latency and cost.** Eval metrics are meaningless if your system is too slow or too expensive for users. Include p50/p95 latency and cost-per-query in every eval report. A prompt that improves faithfulness by **5%** but doubles latency may not be worth deploying.
**Single-metric optimization.** Optimizing faithfulness alone tends to produce answers so cautious they become unhelpful ("Based on the provided context, I cannot fully answer your question..."). Your metrics need to work together. Track the Pareto frontier across faithfulness, helpfulness, and latency.
**Not versioning your eval suite.** As your application evolves, your test queries become stale. Refresh 10 to **20%** of your regression suite quarterly to reflect new use cases, edge cases caught in production, and topic areas that have grown in user queries.
### When to Use Each Approach
RAGAS is the right starting point for any RAG system. It's purpose-built, covers retriever and generator separately, and requires no labeled data for three of its four metrics. Use the v0.2+ API with explicit LLM initialization to avoid the subtle configuration bugs that tripped up teams using the old global-state approach.
Add LLM-as-Judge for dimensions RAGAS doesn't cover — tone, helpfulness, safety, brand voice. Design your judge prompt around what "good" means for your specific application, validate it against human labels, and run it on a sample of production traffic. For cost-sensitive production monitoring, start with GPT-4o mini or a fine-tuned small judge, then escalate to GPT-4o or Claude for low-scoring samples that need deeper analysis.
Use a framework (DeepEval, Braintrust, Langfuse) when you need to scale: multiple team members, multiple prompt versions, automated regression gates, or compliance requirements around logging. The frameworks don't add new measurement capability — they add workflow infrastructure around the metrics you'd run anyway.
Skip evaluation entirely only for internal demos and prototypes with no users. Once real users are involved, continuous eval is non-negotiable.
### Conclusion
LLM evaluation has matured significantly since the "vibe check" era of 2022. RAGAS gives RAG systems a principled metric framework that covers both retrieval quality and generation quality — and with v0.2+, it extends beyond RAG to cover any LLM application including agentic workflows. LLM-as-Judge scales human-quality evaluation to production traffic volumes, though the 2025 research on judge bias (verbosity inflation, self-preference, position effects) demands that you validate your judge before trusting it. Frameworks like DeepEval and Braintrust turn these measurements into automated gates and dashboards that surface problems before users do.
The customer support chatbot running example shows the full loop: sample production traffic, compute faithfulness and relevancy daily, gate deployments on a regression suite, and route low-scoring responses to human review. That loop, running continuously, is what separates a system that drifts toward hallucination from one that stays reliable.
For the retrieval layer specifically, pair these evals with a solid understanding of the underlying technology — [Retrieval-Augmented Generation: Making LLMs Smarter With Your Data](https://letsdatascience.com/blog/retrieval-augmented-generation-rag-making-llms-smarter-with-your-data) covers how the retrieval pipeline works end to end. For systems where agents are doing the retrieval and reasoning, [Agentic RAG: Self-Correcting Retrieval](https://letsdatascience.com/blog/agentic-rag-self-correcting-retrieval) extends the picture to more complex architectures. And if you're tracking model performance across prompt versions and experiments, [MLflow for Experiment Tracking](https://letsdatascience.com/blog/mlflow-experiment-tracking) is the standard tool for keeping those runs organized.
Start measuring. A faithfulness score of 0.6 isn't a failure — it's a diagnosis that tells you exactly where to look next.
### Interview Questions
**What are the four core RAGAS metrics and what does each measure?**
Faithfulness measures whether every claim in the generated answer is supported by the retrieved context, detecting hallucinations. Answer relevancy measures whether the answer addresses the question asked. Context precision measures what fraction of the retrieved chunks are relevant to the question, evaluating retriever quality. Context recall measures whether the retrieved context contained everything needed to answer correctly, requiring a reference answer to compute.
**How does the RAGAS v0.2 API differ from v0.1, and why does it matter?**
In v0.1, metrics were pre-initialized global objects and datasets were HuggingFace `Dataset` objects loaded with `Dataset.from_dict()`. In v0.2+, you initialize each metric explicitly with the evaluator LLM using `Faithfulness(llm=evaluator_llm)`, and datasets use RAGAS's own `EvaluationDataset` with `SingleTurnSample` objects. The explicit LLM initialization removes a common source of bugs where teams didn't realize which model was being used for evaluation — especially important when using a different judge model than the application model.
**How does the LLM-as-Judge method work and what are its main limitations?**
A stronger LLM evaluates the output of a target system using a structured rubric, scoring responses on dimensions like faithfulness, helpfulness, or tone. Agreement with human expert judgments is approximately **80%** on most tasks. Main limitations: verbosity bias (judges favor longer responses, inflating scores by roughly **15%**), self-enhancement bias (models rate their own outputs higher than competitors'), position bias in pairwise comparisons (GPT-4 is ~**40%** inconsistent when pairs are reversed), and sycophancy toward assertive claims. All four can be partially mitigated through prompt design, counterbalancing, and periodic human validation of judge accuracy.
**Your RAG chatbot's faithfulness score drops from 0.88 to 0.71 after a knowledge base update. How do you diagnose the cause?**
First, segment the score drop by query category to find which topic areas degraded — this often points to specific knowledge base sections that were added or modified. Then inspect low-scoring responses manually to see whether the hallucinations share a pattern (for example, all involve a specific new product feature). Check whether context precision also dropped, which would indicate the retriever is fetching irrelevant chunks from the new content. Finally, compare the old and new knowledge base chunks for the affected topic to find formatting or terminology changes that might confuse the retriever.
**When would you prefer pairwise comparison over direct scoring in LLM-as-Judge evaluation?**
Pairwise comparison is preferable when you're comparing two specific versions of a system (A/B testing a prompt change), when the quality difference is subtle and hard to express on a numeric scale, or when you're evaluating a new baseline against an existing one. Direct scoring scales better for continuous monitoring of a single system because you don't need pairs. The main risk with pairwise comparison is position bias — always randomize response order and run each pair twice with positions swapped.
**How do you evaluate an AI agent that uses multiple tools across a multi-step task?**
Agent evaluation needs three layers: tool call accuracy (did the agent invoke the right tool with correct parameters at each step), planning quality (did it decompose the task correctly before acting), and end-to-end task completion rate (did the task succeed). Tool call accuracy is reference-based and needs a labeled dataset of tasks with known correct action sequences. Planning quality uses LLM-as-Judge or a tool like DeepEval's DAG metric. Task completion rate is a binary pass/fail evaluated in a sandboxed environment. RAGAS also includes Agent Goal Accuracy as a native metric for agentic workflows.
**What's the risk of optimizing for a single eval metric in an LLM system?**
Single-metric optimization almost always creates unintended tradeoffs. Optimizing faithfulness alone produces overly conservative responses ("Based on the context, I cannot fully answer...") that score high on faithfulness but low on helpfulness. Optimizing helpfulness tends to produce confident, comprehensive answers that are more likely to hallucinate. In practice, you need to track a dashboard of metrics — faithfulness, relevancy, latency, and cost — and make deployment decisions on the Pareto frontier. A prompt change is worth deploying only if it improves one metric without meaningfully degrading the others.
**Why might a fine-tuned small judge model outperform GPT-4 for your specific eval task?**
A general-purpose judge like GPT-4 is calibrated to broad human preferences across many domains. Your application has a specific definition of "good" — your customer support bot values accuracy over comprehensiveness, uses a specific tone, and has domain terminology. A 7B to 13B model fine-tuned on 500 human-labeled examples from your specific application can learn that definition precisely, hitting 82 to **85%** human agreement on your eval task versus GPT-4's **80%** on general tasks — while running at a fraction of the cost. The investment in calibration data typically pays for itself within a few months of production monitoring.
Practice interview problems based on real data
1,500+ SQL & Python problems across 15 industry datasets — the exact type of data you work with.
[Try 250 free problems](https://letsdatascience.com/problems)
Free Career Roadmaps8 PATHS
Step-by-step roadmaps from zero to job-ready — curated courses, salary data, and the exact learning order that gets you hired.
[Data Analyst$95K](https://letsdatascience.com/learn/paths/data-analyst)[Data Scientist$130K](https://letsdatascience.com/learn/paths/data-scientist)[ML Engineer$155K](https://letsdatascience.com/learn/paths/ml-engineer)[AI Engineer$160K](https://letsdatascience.com/learn/paths/ai-engineer)[Data Engineer$140K](https://letsdatascience.com/learn/paths/data-engineer)[Analytics Eng.$140K](https://letsdatascience.com/learn/paths/analytics-engineer)[MLOps Engineer$160K](https://letsdatascience.com/learn/paths/mlops-engineer)[Quant Analyst$175K](https://letsdatascience.com/learn/paths/quant-analyst)
[Explore all career paths ](https://letsdatascience.com/learn/paths)
Like
Save
Share
Written by [LDS Team](https://letsdatascience.com/author/lds-team)
[More articles](https://letsdatascience.com/blog)
## Recommended Reading
Curated articles related to this topic
[ Multimodal AIIntermediate 26 min Multimodal AI: How Vision-Language Models Work Multimodal AI systems integrate text and visual data processing into a single architecture, enabling applications like receipt scanning and code generation from diagrams. Vision-language models (VLMs) fundamentally changed machine learning by moving beyond unimodal constraints, allowing bidirectional reasoning where images ground text generation and text queries direct visual attention. The CLIP architecture pioneered this shift using contrastive learning to align image and text embeddings in a shared vector space without manual labeling. Modern implementations like GPT-4o and Gemini Pro build upon these foundations to perform complex tasks such as interpreting medical scans or extracting JSON data from restaurant bills. Understanding the underlying mechanisms—specifically how dual encoders compute cosine similarity between visual and textual representations—provides the necessary framework for deploying these models in production environments. Mastering VLM architecture empowers developers to build sophisticated applications that seamlessly bridge the gap between visual perception and language reasoning. Audio Mar 18, 2026 ](https://letsdatascience.com/blog/multimodal-ai-how-vision-language-models-work)[ Prompt EngineeringIntermediate 25 min Advanced Prompt Engineering: Chain-of-Thought, ReAct, and Structured Outputs Advanced prompt engineering transforms Large Language Model interactions from basic question-answering to reliable production workflows by implementing structured reasoning frameworks. This guide details essential techniques including Chain-of-Thought (CoT) for multi-step logic, ReAct for integrating external tools, and Self-Consistency for improving answer reliability through multiple reasoning paths. The analysis demonstrates how Zero-Shot CoT instructions like "Let's think step by step" can improve reasoning accuracy on complex tasks, while structured outputs ensure data adheres to strict schemas like JSON for downstream applications. Developers learn to solve specific production problems such as hallucination, format inconsistency, and token cost inefficiencies using prompt caching and system prompt engineering. The text explains the specific trade-offs of each method, noting that Self-Consistency increases token usage by 3-5x while Prompt Caching can reduce costs by up to 90%. By mastering these strategies, engineers can build robust agentic systems capable of handling complex medical record analysis or autonomous reporting tasks with production-grade reliability. Audio Mar 17, 2026 ](https://letsdatascience.com/blog/advanced-prompt-engineering-chain-of-thought-react-and-structured-outputs)[ Fine-TuningIntermediate 19 min LLM Quantization: Run Any Model on Consumer Hardware Large Language Model quantization enables running massive 70-billion-parameter models like Llama 3.1 70B on consumer hardware such as a single NVIDIA RTX 4090 by reducing numerical precision. Reducing weights from standard 16-bit floating point (FP16) to 4-bit integers (INT4) compresses memory requirements by nearly 75 percent, dropping a 140GB model to roughly 35GB with minimal quality loss. This process relies on specific formats like GGUF, which supports flexible execution across CPUs and GPUs using tools like llama.cpp, Ollama, and LM Studio. Advanced techniques like K-Quants optimize performance by assigning higher precision to sensitive layers like attention projections while compressing feed-forward layers more aggressively. Practitioners use quantization to balance VRAM usage against perplexity, allowing local execution of state-of-the-art AI without enterprise A100 clusters. Mastering these numerical tradeoffs empowers developers to deploy sophisticated generative AI applications on standard laptops and gaming desktops. Audio Mar 17, 2026 ](https://letsdatascience.com/blog/llm-quantization-run-any-model-on-consumer-hardware)[ LLM FundamentalsIntermediate 21 min Open Source LLMs in 2026: The Definitive Comparison The gap between open source and proprietary Large Language Models (LLMs) has effectively closed by early 2026, making self-hosting a superior strategy for production use cases like AI coding assistants. While proprietary APIs like GPT-5 cost approximately 52,000, representing an 88% cost reduction. Beyond economics, open source models allow for data privacy compliance under HIPAA and SOC 2, preventing proprietary source code from leaking to third-party servers. Llama 3.3 70B specifically achieves 92.1 on IFEval and 86.0% on MMLU, outperforming earlier models like GPT-4o on instruction following benchmarks. Newer models like Llama 4 Maverick utilize Mixture-of-Experts architectures with extreme context windows of up to 1 million tokens, enabling whole-codebase understanding that closed APIs struggle to match. Data science teams can now deploy highly customized, fine-tuned models using LoRA adapters on consumer hardware like dual RTX 4090s or enterprise H100 clusters. Audio Mar 17, 2026 ](https://letsdatascience.com/blog/open-source-llms-in-2026-the-definitive-comparison)[ RAG & Vector DBsIntermediate 19 min RAG vs Fine-Tuning: Which to Use for Your LLM App Retrieval-Augmented Generation (RAG) and model fine-tuning solve fundamentally different problems in Large Language Model (LLM) application development. RAG systems optimize for factual accuracy and real-time knowledge retrieval by injecting vector embeddings from knowledge bases directly into an inference context window, ensuring answers remain grounded in current documents. Conversely, fine-tuning using parameter-efficient methods like LoRA (Low-Rank Adaptation) permanently modifies model weights to instill specific behavioral patterns, stylistic consistency, or domain-specific language structures, such as legal phrasing or medical coding formats. Choosing between these approaches requires evaluating whether an application demands dynamic external data access or ingrained stylistic adherence. Many production environments benefit from hybrid architectures or the emerging capabilities of long-context models that process massive inputs without retrieval complexity. By distinguishing between knowledge injection and behavioral adaptation, developers prevent wasted GPU resources on unnecessary training and avoid building complex vector databases when simple context window prompting suffices. Understanding the architectural trade-offs enables engineering teams to deploy cost-effective, high-performance legal assistants, customer support agents, and technical analysis tools using the correct tool for the specific machine learning objective. Audio Mar 17, 2026 ](https://letsdatascience.com/blog/rag-vs-fine-tuning-which-to-use-for-your-llm-app)[ Fine-TuningIntermediate 23 min Fine-Tuning LLMs with LoRA and QLoRA: Complete Guide Low-Rank Adaptation (LoRA) and Quantized Low-Rank Adaptation (QLoRA) enable machine learning engineers to fine-tune massive 7-billion-parameter models like Llama 3 on single consumer GPUs for approximately $10 in compute costs. These parameter-efficient fine-tuning (PEFT) techniques solve the hardware constraints of full fine-tuning by freezing the original model weights and injecting small, trainable rank decomposition matrices into each layer. Rather than updating all parameters, LoRA modifies a parallel branch using low-rank matrices, drastically reducing memory usage from 56GB to manageable levels for 16-bit float models. QLoRA further optimizes this process by quantizing the base model to 4-bit precision without sacrificing performance. This guide details the mathematical foundations of low-rank updates, the specific hyperparameters for configuring scaling factors (alpha) and rank (r), and practical Python implementation strategies. Data scientists gain the ability to customize Large Language Models for specific domains, such as medical question-answering or consistent clinical documentation, while avoiding catastrophic forgetting and the prohibitive costs of A100 clusters. Audio Mar 17, 2026 ](https://letsdatascience.com/blog/fine-tuning-llms-with-lora-and-qlora-complete-guide)[ Fine-TuningIntermediate 19 min Synthetic Data Generation: The Complete Guide Synthetic data generation solves data privacy and scarcity challenges by creating artificial datasets that mirror the statistical properties of real-world information without exposing sensitive details. Unlike traditional data augmentation techniques like SMOTE which merely interpolate between existing points, generative models learn the full joint distribution of the source data to produce entirely new, statistically valid records. The process relies on sophisticated statistical methods, particularly Copula-based generation which separates marginal distributions from dependency structures using Gaussian transformations. For tabular data applications like electronic health records, Gaussian Copulas offer interpretability by allowing data scientists to inspect learned correlation matrices directly. By leveraging these techniques rather than simple anonymization, machine learning teams can bypass GDPR constraints, address class imbalance, and train robust predictive models on datasets that preserve critical relationships like BMI-to-glucose correlations while containing zero real individuals. Audio Mar 10, 2026 ](https://letsdatascience.com/blog/synthetic-data-generation-the-complete-guide)[ LLM FundamentalsIntermediate 17 min GPT Architecture: The Technology Behind ChatGPT Inside the GPT architecture: decoder-only transformers, autoregressive generation, causal self-attention, and the evolution from GPT-1 to GPT-5. Audio Mar 10, 2026 ](https://letsdatascience.com/blog/gpt-architecture-technology-behind-chatgpt)[ LLM FundamentalsIntermediate 16 min The Transformer Architecture Explained The complete guide to the Transformer architecture: self-attention, multi-head attention, positional encoding, and why this single paper changed AI forever. Audio Mar 10, 2026 ](https://letsdatascience.com/blog/attention-is-all-you-need-transformer-revolution)[ LLM FundamentalsIntermediate 17 min Vibe Coding: How AI Coding Assistants Work Vibe coding represents a fundamental shift in software development where developers define outcomes in natural language while AI assistants handle implementation details and syntax generation. Originally coined by Andrej Karpathy in early 2025, vibe coding moves beyond simple autocomplete toward autonomous agents that can scaffold entire projects like Next.js applications or internal dashboards from single prompts. The methodology relies on a spectrum of autonomy ranging from GitHub Copilot's inline suggestions to fully agentic workflows in tools like Devin that resolve Jira tickets independently. Successful implementation requires a hybrid approach where developers use high-autonomy modes for scaffolding and prototyping while applying rigorous human review to critical security logic, authentication flows, and payment endpoints. Developers mastering vibe coding learn to shift cognitive load from memorizing syntax to managing context, crafting precise prompts, and verifying AI-generated outputs against architectural requirements. By adopting tools such as Cursor, Claude Code, and GitHub Copilot within this framework, engineering teams significantly accelerate prototype-to-production cycles while maintaining code quality through strategic oversight. Audio Mar 7, 2026 ](https://letsdatascience.com/blog/vibe-coding-ai-coding-assistants)
© 2026 Let's Data Science
[](https://www.youtube.com/@letsdatascience)[](https://x.com/letsdatascience)[](https://www.linkedin.com/company/lets-data-science/)[](https://www.instagram.com/lets_datascience/)[](https://open.spotify.com/show/0x4laIZ3OSlnAlr0R7gXsr)[](https://www.reddit.com/user/letsdatascience/)[](https://music.amazon.com/podcasts/f245918a-83ab-4b40-9730-d6e5446ad66e/let's-data-science-%E2%80%94-ai-news-daily)
[Advertise](https://letsdatascience.com/advertise)|[Terms](https://letsdatascience.com/terms)|[Privacy](https://letsdatascience.com/privacy)|Cookie preferences|[Image Rights](https://letsdatascience.com/copyright)
Feedback
### We value your privacy
We use cookies to keep this site fast, useful, and our content free. Choose how you want us to use them. [Privacy Policy](https://letsdatascience.com/privacy)
Essential onlyAccept all

