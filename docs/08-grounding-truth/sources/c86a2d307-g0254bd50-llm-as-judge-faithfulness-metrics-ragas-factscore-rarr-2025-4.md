[Saulius blog](https://saulius.io/)
[Blog](https://saulius.io/blog)[Tags](https://saulius.io/tags)[About](https://saulius.io/about)
[Home](https://saulius.io/)
[Blog](https://saulius.io/blog)
[Tags](https://saulius.io/tags)
[About](https://saulius.io/about) Published on
    December 15, 2025
# Ragas Metrics Explained: What Context Precision/Recall, Faithfulness, and Factual Correctness Actually Compute
Ragas is a popular evaluation library for Retrieval-Augmented Generation (RAG). A lot of its most useful metrics are _not_ pure string-matching: they ask an LLM to act like a structured grader (“judge”), and then turn those structured judgments into numeric scores.
This post explains the _implementation mechanics_ behind that approach (prompt format, structured output parsing/retries, LLM/embedding plumbing), and then dives into five commonly used metrics:
  * Natural Language Comparison: **Factual Correctness** , **Semantic Similarity**
  * RAG-focused: **Context Precision** , **Context Recall** , **Faithfulness**


The descriptions below focus on the mechanics and what the metrics compute (prompt structure, structured outputs, and the score aggregations).
* * *
##  [](https://saulius.io/blog/ragas-rag-evaluation-metrics-llm-judge#1-the-core-pattern-structured-judging-not-free-form-text)1) The core pattern: structured judging, not free-form text
###  [](https://saulius.io/blog/ragas-rag-evaluation-metrics-llm-judge#prompt-construction-schema--examples--json-input)Prompt construction: schema + examples + JSON input
Ragas standardizes judge prompts around a consistent “V1-identical” prompt layout:
  1. A natural-language instruction
  2. A **JSON Schema** for the required output
  3. Few-shot examples (often)
  4. A final “Now perform the same…” instruction
  5. The input payload as JSON


You can see this format in two main prompt abstractions: a modern prompt base and a legacy Pydantic-style prompt class.
Both ultimately render strings that embed:
  * the output model schema (Pydantic -> JSON schema)
  * example input/output pairs
  * a machine-readable JSON input block


This matters because it’s how Ragas makes “LLM-as-a-judge” _reliable enough_ to automate: the model is guided into emitting a constrained JSON object, not an essay.
###  [](https://saulius.io/blog/ragas-rag-evaluation-metrics-llm-judge#what-models-can-you-use-for-ragas-judging)What models can you use for Ragas judging?
Ragas is intentionally model-agnostic: the “judge” is just an LLM that can follow the schema-constrained prompt.
Common options:
  * **Commercial/hosted LLMs** : OpenAI (and Azure OpenAI), Anthropic, Google, etc. Ragas supports multiple providers via adapters/factories and integrations.
  * **LangChain chat models** : you can pass a LangChain `ChatModel` through Ragas’ LangChain wrappers. That includes commercial providers (e.g. `ChatOpenAI`, `ChatAnthropic`) and local providers.
  * **Local models via Ollama** : local models can act as the judge as well. A common pattern is to use LangChain’s `ChatOllama` as the chat model and then wrap it for Ragas. See the LangChain docs: <https://python.langchain.com/docs/integrations/chat/ollama/>


Note on **LangGraph** : LangGraph is a workflow/orchestration layer around LangChain. You _can_ run your RAG pipeline in LangGraph and still evaluate with Ragas, but Ragas’ judging integrations themselves are typically expressed as direct LLM wrappers (e.g. LangChain wrappers), not “LangGraph-specific” wrappers.
###  [](https://saulius.io/blog/ragas-rag-evaluation-metrics-llm-judge#structured-outputs-pydantic-models-as-the-contract)Structured outputs: Pydantic models as the contract
Under the hood, judge calls typically look like:
  * build prompt string
  * call `llm.generate(...)` / `llm.agenerate(...)` with a `response_model=SomePydanticModel`
  * validate/parse the JSON into that model


That approach is wired through Ragas’ LLM wrappers and factories.
The key idea: _metrics define an output model_ , and the runtime enforces it.
###  [](https://saulius.io/blog/ragas-rag-evaluation-metrics-llm-judge#fix-output-format-retries-when-the-model-breaks-the-contract)“Fix output format”: retries when the model breaks the contract
Even with schemas, models sometimes emit malformed JSON or wrong fields. Ragas includes a “repair” loop:
  * parse and validate output
  * if parsing fails, re-prompt using a dedicated “fix the output format” instruction


That retry/repair machinery is typically implemented as: validate → if invalid, re-prompt with a “fix the output format” instruction.
So the system is not “one prompt, hope for the best”: it’s a constrained generation + validation + retry pipeline.
###  [](https://saulius.io/blog/ragas-rag-evaluation-metrics-llm-judge#embeddings-plumbing-for-non-judge-metrics)Embeddings plumbing for non-judge metrics
Some metrics don’t require an LLM judge at all (or only optionally): they use embeddings.
Ragas supports multiple embedding backends via an embedding interface and factory.
This is the backbone for **Semantic Similarity**.
* * *
##  [](https://saulius.io/blog/ragas-rag-evaluation-metrics-llm-judge#2-metric-deep-dives)2) Metric deep-dives
###  [](https://saulius.io/blog/ragas-rag-evaluation-metrics-llm-judge#a-semantic-similarity-embeddings--cosine)A) Semantic Similarity (embeddings + cosine)
**What it’s trying to measure** How close the generated answer is to a reference answer in semantic space, even if wording differs.
**How it’s implemented** This is usually an embedding-based metric:
  1. Embed the generated answer and the reference
  2. Compute cosine similarity


In practice this is computed by embedding both texts and taking cosine similarity.
**The computation** With embeddings uuu and vvv:
cosine(u,v)=u⋅v∥u∥∥v∥\text{cosine}(u,v) = \frac{u \cdot v}{\|u\|\,\|v\|}cosine(u,v)=∥u∥∥v∥u⋅v​
**Practical notes**
  * This is _not_ a faithfulness measure. A hallucinated answer can still be semantically similar to a reference if it contains overlapping themes.
  * Your embedding model choice can move scores substantially.


* * *
###  [](https://saulius.io/blog/ragas-rag-evaluation-metrics-llm-judge#b-context-precision-llm-judge-per-chunk--average-precision)B) Context Precision (LLM judge per chunk → average precision)
**What it’s trying to measure** Given the contexts your retriever returned, how many of them are _actually useful_ for answering the question (relative to some ground truth, usually a reference answer).
**How it works (pipeline)**
  1. For each retrieved context chunk, the LLM judge returns a binary verdict like “useful / not useful”.
  2. Those binary verdicts are combined using **Average Precision** , meaning:
     * early useful contexts count more than late ones
     * ordering quality matters


**Prompt used by Ragas (described)**
In Ragas v2 this is implemented as the structured prompt class `ContextPrecisionPrompt`.
The prompt’s instruction is short and binary (useful vs not useful). A few short verbatim snippets:
  * “verify if the context was useful”
  * “Give verdict as "1" if useful”
  * “"0" if not”


In plain English: the judge is asked, “Given this question and this answer, did this specific retrieved chunk actually help?” It must answer with a yes/no-style verdict and a short justification.
**The scoring formula (as implemented)** Let vi∈{0,1}v_i \in \\{0,1\\}vi​∈{0,1} be the verdict for context at rank iii (1-indexed). Define precision at iii:
P@i=∑j=1ivjiP@i = \frac{\sum_{j=1}^{i} v_j}{i}P@i=i∑j=1i​vj​​
Average precision:
AP=∑i=1n(P@i)vi∑i=1nvi+εAP = \frac{\sum_{i=1}^{n} (P@i)\,v_i}{\sum_{i=1}^{n} v_i + \varepsilon}AP=∑i=1n​vi​+ε∑i=1n​(P@i)vi​​
This is the standard average-precision aggregation (often with a tiny epsilon to avoid division by zero).
**Why this is a judge metric** The core operation is the per-chunk “usefulness” classification, which is done by prompting an LLM with a schema-constrained output model.
* * *
###  [](https://saulius.io/blog/ragas-rag-evaluation-metrics-llm-judge#c-context-recall-llm-attribution-per-reference-statement--mean)C) Context Recall (LLM attribution per reference statement → mean)
**What it’s trying to measure** Whether the retrieved context contains _enough information_ to support the reference answer (coverage).
**How it works (pipeline)**
  1. The metric operates over **reference statements** (or a similar decomposition).
  2. The judge marks each reference statement as _attributed_ (supported by the retrieved context) or not.
  3. The score is the mean of those attribution flags.


**Prompt used by Ragas (described)**
In Ragas v2 this is implemented as the structured prompt class `ContextRecallPrompt`.
This prompt asks the judge to go statement-by-statement through the reference answer and mark each as attributable to the retrieved context. Short verbatim snippets:
  * “analyze each statement in the answer”
  * “binary classification: 1 … 0 …”
  * “Provide detailed reasoning”


In plain English: the judge is asked to turn the reference answer into a checklist of statements and mark each one as “supported by the retrieved context” (1) or “not supported” (0), explaining each decision.
**The scoring** If there are mmm statements and ak∈{0,1}a_k \in \\{0,1\\}ak​∈{0,1} indicates attribution:
ContextRecall=1m∑k=1mak\text{ContextRecall} = \frac{1}{m}\sum_{k=1}^{m} a_kContextRecall=m1​∑k=1m​ak​
Edge case: if there are zero statements, the score can be undefined (often NaN).
**Interpretation**
  * High context recall: retriever returned information that covers what the reference says.
  * Low context recall: the retriever missed important pieces, even if some chunks are relevant.


* * *
###  [](https://saulius.io/blog/ragas-rag-evaluation-metrics-llm-judge#d-faithfulness-statement-extraction--nli-judge-vs-context--fraction-supported)D) Faithfulness (statement extraction → NLI judge vs context → fraction supported)
**What it’s trying to measure** Whether the model’s answer is _supported by the retrieved context_ , i.e., it did not hallucinate beyond what was provided.
**How it works (two-stage judge pipeline)**
  1. **Statement generation** : ask an LLM to rewrite the answer into a list of standalone, atomic statements.
  2. **NLI verification** : for each statement, ask an LLM judge if it is inferable from (entailed by) the retrieved context.
  3. Score = fraction of statements judged supported.


**Prompt example: how Ragas breaks answers into statements**
Ragas does statement extraction with a “V1-identical statement generator” prompt. Here’s a _short, partial excerpt_ (with omissions) highlighting the key instructions:

```
Given a question and an answer, analyze the complexity of each sentence in the answer.
Break down each sentence into one or more fully understandable statements.
Ensure that no pronouns are used in any statement.
Format the outputs in JSON.
Please return the output in a JSON format that complies with the following schema as specified in JSON Schema:
...
--------EXAMPLES-----------
Example 1
Input: {
   "question": "Who was Albert Einstein and what is he best known for?",
   "answer": "He was a German-born theoretical physicist, ..."
}
Output: {
   "statements": [
      "Albert Einstein was a German-born theoretical physicist.",
      ...
   ]
}

```

**The scoring** Let sss be number of extracted statements, and ei∈{0,1}e_i \in \\{0,1\\}ei​∈{0,1} be the NLI verdict (“entailed by context”).
Faithfulness=∑i=1seis\text{Faithfulness} = \frac{\sum_{i=1}^{s} e_i}{s}Faithfulness=s∑i=1s​ei​​
If statement extraction yields zero statements, the score is undefined (often NaN).
**Key nuance** Faithfulness is about _support in the provided context_ , not agreement with a reference answer.
* * *
###  [](https://saulius.io/blog/ragas-rag-evaluation-metrics-llm-judge#e-factual-correctness-claim-decomposition--nli-judge-vs-reference--precisionrecallf%CE%B2)E) Factual Correctness (claim decomposition → NLI judge vs reference → precision/recall/Fβ)
**What it’s trying to measure** Whether the answer’s factual claims are correct relative to a reference (or ground-truth source).
**How it works (pipeline)**
  1. **Claim decomposition** : break the response into atomic factual claims.
  2. **Verification** : judge each claim against the reference using an NLI-style decision (supported/unsupported) plus rationale.
  3. Compute precision/recall (and an FβF_\betaFβ​ aggregate) over those judgments.


**The scoring** If:
  * precision PPP = fraction of response claims supported by the reference
  * recall RRR = fraction of reference claims recovered/supported by the response


then:
Fβ=(1+β2)PRβ2P+RF_{\beta} = (1+\beta^2)\,\frac{P\,R}{\beta^2 P + R}Fβ​=(1+β2)β2P+RPR​
You can compute different “modes” (precision, recall, or FβF_\betaFβ​) depending on what you want to emphasize; some implementations also apply rounding.
**How it differs from Faithfulness**
  * Faithfulness: “Is this answer supported by retrieved context?”
  * Factual correctness: “Is this answer correct vs reference/ground truth?”


Both use LLM-as-a-judge, but they grade against different evidence.
* * *
##  [](https://saulius.io/blog/ragas-rag-evaluation-metrics-llm-judge#3-what-to-watch-out-for-implementation-driven-gotchas)3) What to watch out for (implementation-driven gotchas)
  * **Context Precision is order-sensitive** : shuffling contexts can change the score even if the set is identical.
  * **Statement/claim decomposition is a critical dependency** : if decomposition misses claims or over-splits, downstream NLI checks and final scores drift.
  * **Long contexts can degrade NLI accuracy** : concatenation is simple but can exceed model attention or increase confusion.
  * **Structured output improves robustness, not correctness** : JSON schemas prevent format errors, but don’t guarantee good judgments.


* * *
##  [](https://saulius.io/blog/ragas-rag-evaluation-metrics-llm-judge#4-what-do-the-scores-mean-in-a-customer-support-rag-system)4) What do the scores _mean_ in a customer support RAG system?
Ragas metric scores are typically normalized to [0,1][0,1][0,1], but **a score like 0.8 is not a universal “80% correct”**. It means “0.8 according to _this metric’s definition and judge/model choices_ on _this dataset_.” The most useful way to interpret scores is as _operational signals_ tied to concrete failure modes.
Below are practical interpretations for a customer support RAG system (e.g., “answer questions about policies, billing, troubleshooting”), assuming you’re evaluating across many tickets.
###  [](https://saulius.io/blog/ragas-rag-evaluation-metrics-llm-judge#semantic-similarity-how-close-is-the-answer-to-the-reference)Semantic Similarity: “How close is the answer to the reference?”
  * **What 0.8 suggests** : Answers are usually _near-paraphrases_ of the reference (similar meaning, possibly different wording). Users would often find them acceptable _if the reference is correct and complete_.
  * **What it does _not_ guarantee**: Groundedness. A hallucinated answer can still be “semantically similar” to a reference if it shares topic/phrasing.
  * **Practical read** : Use it to track “answer shape/coverage relative to your gold responses,” not truthfulness.


###  [](https://saulius.io/blog/ragas-rag-evaluation-metrics-llm-judge#context-precision-did-we-retrieve-useful-chunks-early)Context Precision: “Did we retrieve useful chunks early?”
Context Precision is computed like average precision over binary “useful” verdicts per retrieved chunk.
  * **What 0.8 suggests** : Most of the chunks the model sees (especially top-ranked ones) are judged useful. In practice, this often correlates with:
    * fewer irrelevant policy pages in the top-kkk
    * fewer distracting/contradictory snippets
    * faster time-to-answer in multi-step agents (less reading)
  * **How to translate 0.8 into operations** : With small kkk (e.g. 5 contexts), 0.8 commonly corresponds to “most contexts are useful and the useful ones tend to appear early,” but the exact mapping depends on ranking and judge decisions.


###  [](https://saulius.io/blog/ragas-rag-evaluation-metrics-llm-judge#context-recall-did-retrieval-include-the-needed-information-at-all)Context Recall: “Did retrieval include the needed information at all?”
Context Recall is essentially the fraction of reference statements that the judge can attribute to the retrieved context.
  * **What 0.8 suggests** : Roughly ~80% of the facts needed to reproduce the reference answer are present in the retrieved context. In customer support terms, the retriever usually brings the right doc(s), but may miss an important clause (e.g., an exception, limit, or prerequisite).
  * **Typical failure at ~0.8** : Answers are mostly right but omit key details (“You can refund” without “within 14 days” or “for annual plans only”).


###  [](https://saulius.io/blog/ragas-rag-evaluation-metrics-llm-judge#faithfulness-is-the-answer-supported-by-the-retrieved-context)Faithfulness: “Is the answer supported by the retrieved context?”
Faithfulness is computed as the fraction of generated statements that the judge says are entailed by the retrieved context.
  * **What 0.8 suggests** : About 20% of the answer’s statements are _not_ supported by the provided context. In customer support, this often shows up as:
    * invented policy details (dates/fees/eligibility)
    * confident troubleshooting steps not present in docs
    * ungrounded promises (“we will refund today”)
  * **Practical read** : A faithfulness score of 0.8 can still be risky if the unsupported 20% contains high-impact claims (refunds, account actions, compliance). It’s a “hallucination rate” proxy, not a severity measure.


###  [](https://saulius.io/blog/ragas-rag-evaluation-metrics-llm-judge#factual-correctness-is-the-answer-correct-vs-the-referenceground-truth)Factual Correctness: “Is the answer correct vs the reference/ground truth?”
Factual Correctness typically decomposes into claims and uses NLI-style verification against the reference, then aggregates as precision/recall or FβF_\betaFβ​.
  * **What 0.8 suggests** : Most factual claims align with the reference, but there are still meaningful errors or omissions depending on whether you’re emphasizing precision, recall, or FβF_\betaFβ​.
    * If you’re using a **precision-like** mode: ~20% of _claims made_ may be incorrect.
    * If you’re using a **recall-like** mode: ~20% of _needed claims_ may be missing.
  * **Practical read** : In customer support, missing constraints and wrong edge-case handling are the common culprits.


###  [](https://saulius.io/blog/ragas-rag-evaluation-metrics-llm-judge#how-to-make-08-actionable-recommended)How to make “0.8” actionable (recommended)
  * **Use distributions, not single numbers** : Track median, p10/p90, and “% below threshold.” Averages hide tails.
  * **Calibrate with a small human-labeled set** : Sample ~50–200 tickets and label common failure types (wrong policy, missing constraint, hallucinated detail, irrelevant context). Then see what metric values correspond to “acceptable” for your org.
  * **Pick thresholds by risk** :
    * For low-risk intents (how-to steps), you might accept lower faithfulness.
    * For high-risk intents (billing/refunds/security), you usually want higher faithfulness and factual correctness, and you may gate responses (e.g., “ask to escalate” when below threshold).
  * **Keep judge configuration stable** : If you change judge model/prompts, scores can shift. Treat the judge as part of the metric definition.


* * *
##  [](https://saulius.io/blog/ragas-rag-evaluation-metrics-llm-judge#5-takeaways)5) Takeaways
Ragas’ “LLM-as-a-judge” is best thought of as a small, repeatable _program_ :
  * prompts render as instruction + schema + examples + JSON input
  * outputs are forced into Pydantic models
  * parsing failures can trigger repair prompts
  * final metric scores are computed deterministically from structured verdicts


This architecture is why these metrics are reproducible enough to batch over datasets, and why inspecting prompts + scoring code is essential when you’re deciding which metric to trust.
* * *
##  [](https://saulius.io/blog/ragas-rag-evaluation-metrics-llm-judge#appendix-worked-example-wixqa-dataset-item)Appendix: Worked example (WixQA dataset item)
This is a single, concrete example showing what each metric would do.
Source: WixQA dataset (Hugging Face): <https://huggingface.co/datasets/Wix/WixQA/tree/main>
**Dataset item**
  * Question: Can I start accepting payments on my site while my Wix Payments account is still under verification?
  * Generated answer: You can start accepting payments on your site using Wix Payments almost immediately. However, we need to verify your identity before your account can be fully activated.


**KB article / context source** (WixQA KB corpus; article id `49d9e88f...`, title "Wix Payments Verification Process")
To illustrate context-based metrics, assume the retriever returned these 3 "chunks" (ranked):
  * `c1` (rank 1): "If you do not complete your account setup within 30 days, we will be required to suspend your Wix Payments account..."
  * `c2` (rank 2): "You can start accepting payments ... almost immediately. However, we need to verify your identity before your account can be fully activated."
  * `c3` (rank 3): "During this process, we request further information... These need to be uploaded... This may take up to 7 business days."


For metrics that require a reference answer, assume the reference is a short KB-grounded answer:
  * Reference answer: "Yes—you can start accepting payments almost immediately, but Wix needs to verify your identity before the account is fully activated."


###  [](https://saulius.io/blog/ragas-rag-evaluation-metrics-llm-judge#semantic-similarity)Semantic Similarity
Compare embeddings of generated answer vs reference answer and take cosine similarity. Here it should be very high because they’re near-paraphrases (the exact value depends on the embedding model).
###  [](https://saulius.io/blog/ragas-rag-evaluation-metrics-llm-judge#context-precision)Context Precision
The judge gives a binary "useful?" verdict per chunk (given question + answer):
  * `c1`: not useful (0) - suspension policy doesn’t answer "can I start accepting payments while under verification?"
  * `c2`: useful (1) - directly answers the question
  * `c3`: useful (1) - adds verification expectations (supporting detail)


Verdicts by rank: [0,1,1][0, 1, 1][0,1,1]
Compute precision at each rank:
  * P@1=0/1=0P@1 = 0/1 = 0P@1=0/1=0
  * P@2=1/2=0.5P@2 = 1/2 = 0.5P@2=1/2=0.5
  * P@3=2/3≈0.667P@3 = 2/3 \approx 0.667P@3=2/3≈0.667


Average precision (mean of precisions at the ranks where vi=1v_i=1vi​=1):
AP=P@2+P@32=0.5+2/32≈0.583AP = \frac{P@2 + P@3}{2} = \frac{0.5 + 2/3}{2} \approx 0.583AP=2P@2+P@3​=20.5+2/3​≈0.583
This shows the key behavior: even with two useful chunks, putting an irrelevant chunk first pulls the score down.
###  [](https://saulius.io/blog/ragas-rag-evaluation-metrics-llm-judge#context-recall)Context Recall
Break the reference answer into atomic statements and check whether each is attributable to the retrieved context set:
  * `s1`: "You can start accepting payments almost immediately." → attributable (supported by `c2`)
  * `s2`: "Identity verification is needed before the account is fully activated." → attributable (supported by `c2`)


Context recall = mean attribution = (1+1)/2=1.0(1+1)/2 = 1.0(1+1)/2=1.0.
###  [](https://saulius.io/blog/ragas-rag-evaluation-metrics-llm-judge#faithfulness)Faithfulness
Break the generated answer into atomic statements and check whether each is entailed by the retrieved context set:
  * `a1`: "You can start accepting payments almost immediately." → entailed by `c2`
  * `a2`: "Identity verification is required before full activation." → entailed by `c2`


Faithfulness = (1+1)/2=1.0(1+1)/2 = 1.0(1+1)/2=1.0.
###  [](https://saulius.io/blog/ragas-rag-evaluation-metrics-llm-judge#factual-correctness)Factual Correctness
Decompose the generated answer into claims and verify each against the reference answer.
Here both claims match the reference, so precision = 1.0 and recall = 1.0 (and therefore F1=1.0F_1 = 1.0F1​=1.0).
##  [](https://saulius.io/blog/ragas-rag-evaluation-metrics-llm-judge#appendix-local-judging-via-ollama-conceptual-wiring)Appendix: Local judging via Ollama (conceptual wiring)
Ragas doesn’t require OpenAI/Anthropic specifically: the same judge metrics can run on local models, as long as the model can reliably follow the structured prompt and emit valid JSON.
Conceptually:
  * **Local judge** : use an Ollama-served chat model (e.g. Gemma) via LangChain’s `ChatOllama`.
  * **Ragas integration** : pass that chat model into Ragas through the available integrations/wrappers, so metrics that require an LLM can call it.


LangChain `ChatOllama` docs: <https://python.langchain.com/docs/integrations/chat/ollama/>
Load Comments
[← Why You Don’t Need AI Agent Evaluations](https://saulius.io/blog/why-not-to-evaluate-ai-agents)
[Automatic Debugging and Failure Detection in AI Agent Systems →](https://saulius.io/blog/automatic-debugging-and-failure-detection-in-ai-agent-systems)
[github](https://github.com/saultaut)[linkedin](https://www.linkedin.com/in/sautaut/)[scholar](https://scholar.google.com/citations?user=Cpdc--cAAAAJ&hl=en)
Saulius
• 
© 2026
• 
[Saulius blog](https://saulius.io/)

