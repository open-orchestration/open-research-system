---
id: d154759ce
topic: 14-papers
title: "Self-RAG and Toolformer: full per-benchmark result tables and zero-shot deltas"
status: draft
---

This finding grounds the full per-benchmark result tables of Self-RAG [c118a1750] and Toolformer [c4313f7c9] on their primary papers — the exact accuracy figures, long-form citation metrics, and zero-shot deltas that the corpus previously carried only as abstract-level "outperforms" claims. It complements finding de3e9818e (which introduces ReAct, Self-RAG, Toolformer, and the tool-learning survey at the conceptual level): that finding states what the mechanisms are, this one supplies the numbers that validate them and is not restated here.

## Self-RAG: per-benchmark results (Asai et al., ICLR 2024)

Self-RAG is evaluated zero-shot on six tasks: short-form QA (PopQA, TriviaQA-unfiltered, both scored by whether the gold answer appears in the generation, reported as accuracy), closed-set tasks (PubHealth fact verification and ARC-Challenge, both accuracy), and long-form generation (biography generation scored by FactScore, and ALCE-ASQA scored by str-em correctness, Rouge, MAUVE fluency, and citation precision/recall) [c118a1750].

The two Self-RAG models post the following Table 2 figures — columns PopQA(acc) / TriviaQA(acc) / PubHealth(acc) / ARC(acc) / Bio-FactScore / ASQA-em / ASQA-rouge / ASQA-MAUVE / ASQA-citation-precision / ASQA-citation-recall [c118a1750]:

- Self-RAG 7B: 54.9 / 66.4 / 72.4 / 67.3 / 81.2 / 30.0 / 35.7 / 74.3 / 66.9 / 67.8 [c118a1750]
- Self-RAG 13B: 55.8 / 69.3 / 74.5 / 73.1 / 80.2 / 31.7 / 37.0 / 71.6 / 70.3 / 71.3 [c118a1750]

Against non-retrieval baselines, both Self-RAG models beat the supervised fine-tuned LLMs on all tasks; e.g. Alpaca-7B scores PopQA 23.6, PubHealth 49.8, ARC 45.0, and Llama2-chat-13B scores PopQA 20.0, TriviaQA 59.3, PubHealth 49.4, ARC 38.4 [c118a1750]. Self-RAG also exceeds the proprietary ChatGPT (PopQA 29.3, PubHealth 70.1, Bio-FactScore 71.8, ASQA-Rouge 36.2, ASQA-MAUVE 68.8) on PubHealth, PopQA, biography generation, and ASQA (Rouge and MAUVE) — though ChatGPT remains ahead on TriviaQA (74.3) and ARC (75.3) [c118a1750].

Against retrieval-augmented baselines, Self-RAG obtains the best performance among non-proprietary LM-based models on all tasks [c118a1750]. The standard-RAG baselines it beats include Llama2-7B+retrieval (PopQA 38.2, TriviaQA 42.5, PubHealth 30.0, ARC 48.0, ASQA citation precision 2.9 / recall 4.0) and Alpaca-7B+retrieval (PopQA 46.7, TriviaQA 64.1, ASQA citation precision 5.5 / recall 7.2) [c118a1750]. The ASQA citation gap is the sharpest: standard RAG baselines land in the single digits on citation precision/recall, whereas Self-RAG 7B reaches 66.9/67.8 and 13B reaches 70.3/71.3 — competitive even with Ret-ChatGPT (citation precision 65.1 / recall 76.6) [c118a1750].

Mechanism (only as needed to read the numbers): Self-RAG trains the generator to emit reflection tokens defined in Table 1 — `Retrieve` ∈ {yes, no, continue} decides when to call the retriever, `ISREL` ∈ {relevant, irrelevant} judges passage relevance, `ISSUP` ∈ {fully supported, partially supported, no support} checks whether each statement is grounded in the retrieved passage, and `ISUSE` ∈ {1–5} scores response utility; a separately trained critic LM produces the training labels for these tokens, and the generator learns to emit them itself at inference [c118a1750]. The strong ASQA citation scores are the direct payoff of the support/relevance critique being trained into generation rather than bolted on.

## Toolformer: zero-shot results (Schick et al., NeurIPS 2023)

Toolformer is built on a 6.7B-parameter GPT-J model that is self-supervised to decide when to call external tools (a QA system, a calculator, a Wikipedia search, a calendar, and a machine-translation system) [c4313f7c9]. It is compared against vanilla GPT-J, GPT-J+CC (further pretrained on CCNet), a "Toolformer (disabled)" ablation that has the same finetuning but is barred from making API calls at inference, and the much larger OPT (66B) and GPT-3 (175B) [c4313f7c9].

LAMA factual recall — Table 3, columns SQuAD / Google-RE / T-REx (the question-answering tool is used for most examples) [c4313f7c9]:

- GPT-J: 17.8 / 4.9 / 31.9 [c4313f7c9]
- GPT-J+CC: 19.2 / 5.6 / 33.2 [c4313f7c9]
- Toolformer (disabled): 22.1 / 6.3 / 34.9 [c4313f7c9]
- Toolformer: 33.8 / 11.5 / 53.5 [c4313f7c9]
- OPT (66B): 21.6 / 2.9 / 30.1 [c4313f7c9]
- GPT-3 (175B): 26.8 / 7.0 / 39.8 [c4313f7c9]

Toolformer improves on the best baseline by 11.7, 5.2, and 18.6 points on the three subsets respectively, and clearly outperforms both OPT (66B) and GPT-3 (175B) despite being far smaller [c4313f7c9].

Math reasoning — Table 4, columns ASDiv / SVAMP / MAWPS (the calculator tool is used for 97.9% of examples) [c4313f7c9]:

- GPT-J: 7.5 / 5.2 / 9.9 [c4313f7c9]
- GPT-J+CC: 9.6 / 5.0 / 9.3 [c4313f7c9]
- Toolformer (disabled): 14.8 / 6.3 / 15.0 [c4313f7c9]
- Toolformer: 40.4 / 29.4 / 44.0 [c4313f7c9]
- OPT (66B): 6.0 / 4.9 / 7.9 [c4313f7c9]
- GPT-3 (175B): 14.0 / 10.0 / 19.8 [c4313f7c9]

Enabling API calls more than doubles performance over the disabled ablation on every math task and clearly beats the much larger OPT and GPT-3 [c4313f7c9].

Question answering — Table 5, columns WebQS / NQ / TriviaQA (relying mostly on the Wikipedia search tool) [c4313f7c9]:

- GPT-J: 18.5 / 12.8 / 43.9 [c4313f7c9]
- GPT-J+CC: 18.4 / 12.2 / 45.6 [c4313f7c9]
- Toolformer (disabled): 18.9 / 12.6 / 46.7 [c4313f7c9]
- Toolformer: 26.3 / 17.7 / 48.8 [c4313f7c9]
- OPT (66B): 18.6 / 11.4 / 45.7 [c4313f7c9]
- GPT-3 (175B): 29.0 / 22.6 / 65.9 [c4313f7c9]

On QA, Toolformer clearly outperforms all same-size GPT-J-based baselines but still lags GPT-3 (175B), which the paper attributes to the simplicity of its search engine and its inability to reformulate queries or browse multiple results [c4313f7c9]. The headline pattern holds across LAMA and math but not QA: a 6.7B model that learned when to invoke a tool matches or exceeds 10x–25x larger models, while base GPT-J does poorly on the same tasks [c4313f7c9].

## Synthesis: what the two papers jointly establish for a grounded engine

Together these results validate the two control mechanisms a citation-gated research engine depends on, with concrete benchmark gains rather than architecture alone. Self-RAG demonstrates self-reflective retrieval control — retrieve on demand and critique each passage for relevance and support — and the payoff shows up most where grounding is hardest: ASQA citation precision/recall jump from single digits under standard RAG to the high 60s/70s [c118a1750]. Toolformer demonstrates self-taught tool invocation — a model deciding for itself when an external call (calculator, QA, search) helps — and the payoff is a 6.7B model matching or beating 66B–175B baselines on LAMA and math, with base GPT-J left far behind [c4313f7c9]. Retrieval-relevance/support critique [c118a1750] and on-demand external-call decisions [c4313f7c9] are thus the two empirically validated levers for an engine that must ground every claim.
