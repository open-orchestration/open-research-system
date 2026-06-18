# RAG Evaluation 2026 - Faithfulness, Relevancy, and Context Metrics

Source: https://benchmarkingagents.com/rag-eval/

Independent reference. No vendor affiliation. Scores cited with source and capture date. [Affiliate disclosure.](https://benchmarkingagents.com/faq/)
Vol. III · Apr 2026
[THE Benchmarking Agents Review An independent reference on AI evaluation](https://benchmarkingagents.com/)
ISSN 2026-0428
[Benchmarks](https://benchmarkingagents.com/benchmarks-list/)·[Agent Evals](https://benchmarkingagents.com/agent-benchmarks/)·[Custom Evals](https://benchmarkingagents.com/custom-evals/)·[Tools](https://benchmarkingagents.com/tools-compared/)·[What is Missing](https://benchmarkingagents.com/what-these-benchmarks-miss/)·[Glossary](https://benchmarkingagents.com/glossary/)·[FAQ](https://benchmarkingagents.com/faq/)
Sections
[Home](https://benchmarkingagents.com/)/RAG EvaluationLast verified April 2026
# RAG Evaluation 2026 - Faithfulness, Relevancy, and Context Metrics
RAG (Retrieval-Augmented Generation) systems have two places where things go wrong: retrieval (did you fetch the right context?) and generation (did the answer use the context correctly?). Evaluating a RAG system requires measuring both. This is a tool-agnostic guide to the four canonical metrics, how to build a golden dataset, and which tools compute these metrics in 2026.
## What RAG Eval Is
### Retrieval Evaluation
Did the retriever fetch the right context? Metrics: context precision (of what was retrieved, how much was relevant?) and context recall (of what was needed, how much was retrieved?). Poor retrieval upstream causes generation failures downstream.
### Generation Evaluation
Did the LLM use the context correctly? Metrics: faithfulness (did the answer only make claims supported by context?) and answer relevancy (did the answer actually address the question?). Good retrieval cannot save a bad generation step.
## The Four Canonical Metrics (Ragas Framework)
### Faithfulness
Range: 0 - 1
Question being answered
“Does the answer only make claims that are supported by the retrieved context?”
How it is computed
The judge LLM breaks the answer into individual claims, then checks each claim against the retrieved context chunks. Faithfulness = (number of supported claims) / (total number of claims). A claim is 'supported' if it can be directly inferred from the context.
What low scores indicate
The model asserts facts that are not in the retrieved context - a hallucination. Particularly dangerous in legal, medical, and financial applications.
Target threshold
> 0.85 for most production applications. > 0.95 for high-stakes domains.
### Answer Relevancy
Range: 0 - 1
Question being answered
“Does the answer actually address the question that was asked?”
How it is computed
The judge LLM generates several plausible questions that the answer would address, then computes the semantic similarity between those generated questions and the original question. High similarity means the answer was on-topic.
What low scores indicate
The model produces a technically accurate answer to a different or broader question than asked. Common when the retriever returns context about a related topic.
Target threshold
> 0.80. Lower scores often indicate retrieval issues (wrong context retrieved) rather than generation issues.
### Context Precision
Range: 0 - 1
Question being answered
“Of the chunks retrieved, how many were actually relevant to answering the question?”
How it is computed
Each retrieved chunk is evaluated for relevance to the question. Context Precision = (relevant chunks retrieved) / (total chunks retrieved). Computed with LLM-as-judge or embedding similarity against the ground-truth answer.
What low scores indicate
The retriever returns too many chunks that are topically adjacent but not directly useful. Increases context length, cost, and confusion for the generation step.
Target threshold
> 0.75. Low precision suggests retriever tuning - chunk size, embedding model, similarity threshold.
### Context Recall
Range: 0 - 1
Question being answered
“Of the information needed to answer the question, how much was actually retrieved?”
How it is computed
The ground-truth answer is broken into claims. Each claim is checked against retrieved chunks - is this information present? Context Recall = (ground-truth claims supported by retrieved context) / (total ground-truth claims). Requires a ground-truth answer.
What low scores indicate
The retriever misses key context needed to answer the question. The generation step may hallucinate to fill the gap, or refuse to answer.
Target threshold
> 0.80. Low recall often means chunk size is too small, top-k is too low, or the embedding model does not match your domain.
Note: all four Ragas metrics use LLM-as-judge under the hood. See [/llm-as-judge](https://benchmarkingagents.com/llm-as-judge/) for the methodology and bias considerations.
## Building a Golden Dataset
A golden dataset is a set of (question, expected answer, expected source chunks) triples where the expected answer and sources are human-verified ground truth. This is the most important step most teams skip, and the most important investment in eval quality.
Building a golden dataset requires human effort. There is no automated shortcut that produces reliable ground truth. The process: (1) Select representative questions from your application's real traffic or anticipated query distribution. (2) For each question, identify the source chunks in your knowledge base that contain the information needed to answer it. (3) Write the ground-truth answer based only on those source chunks. (4) Label edge cases - questions where the knowledge base does not contain the answer, and the correct behavior is to say so.
Minimum viable golden dataset: 30 examples covering common queries, edge cases, and at least 5 cases where the correct answer is “I don't know.” 100 examples give you statistically reliable metric scores. Budget 15-30 minutes of human time per example for the initial creation; much faster for ongoing additions.
Version control your golden dataset alongside your code. Track which version of the dataset each eval run used. A change in the dataset between runs makes the metric comparison meaningless.
## Tools That Compute These Metrics  
| Tool  | OSS  | RAG Metrics Included  | Notes  |  
| --- | --- | --- | --- |  
| Ragas  | Yes  | All 4 canonical + BLEU, ROUGE, AnswerSimilarity  | The original. Pip-installable, works with any LLM or embedding model.  |  
| DeepEval  | Yes  | GEval, Faithfulness, Contextual Precision/Recall  | pytest-style API, CI-friendly. Confident AI cloud adds dashboard.  |  
| Arize Phoenix  | Yes  | Faithfulness, Relevancy, Hallucination detection  | OSS + Arize AI cloud. Strong production tracing alongside evals.  |  
| Langfuse  | Yes  | Custom metrics + LLM-as-judge templates  | Self-host or cloud. Flexible eval definition, strong tracing.  |  
| LangSmith  | No  | LLM-as-judge templates, custom evaluators  | LangChain-native. Best for teams already on LangChain.  |  
| Braintrust  | No  | LLM-as-judge, custom scorers, BLEU, ROUGE  | Strong CI integration. Does not natively compute all 4 Ragas metrics.  |  
| Some links to eval tools are affiliate links; rankings are not influenced. Full comparison at /tools-compared. |  
## Beyond the Four Metrics
The four Ragas metrics cover retrieval and generation quality on individual responses. For production RAG systems, additional dimensions matter:
  * **Answer similarity:** How similar is the generated answer to a reference answer? Useful when there is a known ground truth. Measured via embedding cosine similarity or BLEU/ROUGE.
  * **Context relevance ranking:** Beyond binary relevant/not-relevant, how does the relevance of retrieved chunks rank? A retriever that ranks the most relevant chunk first is better than one that buries it at position 5.
  * **End-to-end task success:** For agentic RAG (the agent takes actions based on retrieved information), did the downstream task succeed? Faithfulness is necessary but not sufficient for a research agent that must also take correct actions.
  * **Latency:** RAG adds retrieval latency on top of generation latency. P95 latency under load is the most relevant metric for user experience.
  * **Cost per query:** Longer contexts increase inference cost. Context precision directly impacts cost - irrelevant chunks make every query more expensive.


## Frequently Asked Questions
What is a good faithfulness score?+
Faithfulness measures whether your RAG system's answers are grounded in the retrieved context. A score above 0.85 on a 0-1 scale is generally good. Scores below 0.70 indicate significant hallucination and require investigation. The interpretation depends on your use case: a legal assistant requires faithfulness close to 1.0; a brainstorming tool might accept lower scores.
Do I need all four Ragas metrics?+
Not necessarily. Start with faithfulness (is the answer grounded in context?) because hallucination is the most dangerous failure mode. Add answer relevancy as a second priority. Context precision and context recall are important if you are optimising your retrieval component specifically. Faithfulness + answer relevancy covers the most critical failure modes with minimum eval investment.
How many test cases do I need for RAG evaluation?+
Minimum 30 examples to get directionally useful metrics. 100 examples give you statistically reliable scores. 500+ examples allow slicing by query type and document source. Start with 30-50 golden examples covering your most common query patterns and edge cases. Creating ground-truth answers and expected source chunks requires human effort - take it seriously.
What is the difference between context precision and context recall?+
Context precision measures: of the chunks retrieved, what fraction were actually relevant? High precision means the retriever is not returning junk. Context recall measures: of the information needed to answer the question, what fraction did the retriever actually retrieve? High recall means the retriever is not missing important content. The two often trade off.
Is LLM-as-judge reliable for RAG eval?+
LLM-as-judge is reliable enough for faithfulness and answer relevancy when the judge model is stronger than the model being evaluated. It is fast, cheap, and directionally correct. The main risks: the judge may share the same knowledge gaps (problematic for factual correctness), and it can exhibit verbosity bias. Use LLM-as-judge for iteration speed and human eval at release milestones.
[LLM-as-Judge methodology ->](https://benchmarkingagents.com/llm-as-judge/)[Custom eval pipelines ->](https://benchmarkingagents.com/custom-evals/)[Eval tools compared ->](https://benchmarkingagents.com/tools-compared/)
### Sources
  1. [1] Ragas framework - [ragas.io](https://ragas.io)
  2. [2] Es et al., RAGAS: Automated Evaluation of RAG - [arxiv.org/abs/2309.15217](https://arxiv.org/abs/2309.15217) - 2023
  3. [3] DeepEval documentation - [docs.confident-ai.com](https://docs.confident-ai.com)
  4. [4] Arize Phoenix RAG tracing docs - [docs.arize.com/phoenix](https://docs.arize.com/phoenix)


From the editor
Benchmarking Agents Review is published by Digital Signet, an independent firm that builds and ships AI agents in production for mid-market companies. If you are evaluating, designing, or productionising LLM agents and want a working second opinion, get in touch.
[Book a 30-min scoping call](https://calendly.com/oliver-digitalsignet/scoping-call-30-min)[Digital Signet →](https://digitalsignet.com)
30 minutes, free, independent.·1-page action plan within 48h.·Honest if not the right fit.
Colophon
## Read every score as a claim, not a fact.
#### I. Public Benchmarks
  * [Benchmark Reference](https://benchmarkingagents.com/benchmarks-list/)
  * [MMLU and MMLU-Pro](https://benchmarkingagents.com/mmlu/)
  * [HumanEval, LiveCodeBench](https://benchmarkingagents.com/humaneval/)
  * [GPQA, ARC-AGI](https://benchmarkingagents.com/gpqa-arc-agi/)
  * [What Benchmarks Miss](https://benchmarkingagents.com/what-these-benchmarks-miss/)


#### II. Agent Evaluation
  * [Agent Benchmarks](https://benchmarkingagents.com/agent-benchmarks/)
  * [SWE-bench Verified](https://benchmarkingagents.com/swe-bench/)
  * [RAG Evaluation](https://benchmarkingagents.com/rag-eval/)
  * [LLM-as-Judge](https://benchmarkingagents.com/llm-as-judge/)
  * [Human vs Automated](https://benchmarkingagents.com/human-vs-automated/)


#### III. Practitioner
  * [Custom Eval Guide](https://benchmarkingagents.com/custom-evals/)
  * [Eval Tools Compared](https://benchmarkingagents.com/tools-compared/)
  * [Production Monitoring](https://benchmarkingagents.com/for-production-monitoring/)
  * [FAQ](https://benchmarkingagents.com/faq/)
  * [Glossary](https://benchmarkingagents.com/glossary/)


#### IV. Editorial Notes
  * [About this site](https://benchmarkingagents.com/about/)
  * [Methodology](https://benchmarkingagents.com/methodology/)
  * [What benchmarks miss](https://benchmarkingagents.com/what-these-benchmarks-miss/)


Last verified June 2026. Scores captured from primary sources with capture dates shown inline. Some links to evaluation tools are affiliate links. The neutral editorial framing is not influenced by affiliate placement.
No vendor affiliation. No newsletter capture. No display advertising.
© 2026 The Benchmarking Agents ReviewSet in Newsreader and IBM Plex Monobenchmarkingagents.com
[Privacy](https://digitalsignet.com/legal/privacy)[Cookies](https://digitalsignet.com/legal/cookies)[Terms](https://digitalsignet.com/legal/terms)[Accessibility](https://digitalsignet.com/legal/accessibility)

