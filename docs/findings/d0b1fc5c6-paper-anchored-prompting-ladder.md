---
id: d0b1fc5c6
topic: 10-context-prompt-engineering
title: "Paper-anchored prompting ladder: chain-of-thought, self-consistency, and tree-of-thoughts from the originating papers"
status: draft
---

# Paper-anchored prompting ladder: chain-of-thought, self-consistency, and tree-of-thoughts from the originating papers

## Why this finding exists

A prior finding (d0cce1cec) anchored the *context-management* half of this topic on a
genuine primary paper (lost-in-the-middle), but it explicitly flagged that the
prompting-ladder **numbers** — chain-of-thought → self-consistency → tree-of-thoughts —
were *blog-relayed* and therefore non-load-bearing, because the three originating papers
were not in corpus. They now are. This finding retires those blog-relayed figures and
restates each rung's mechanism and headline result directly from its own paper. It is
deliberately complementary to d0cce1cec: it does **not** restate the lost-in-the-middle or
context-stuffing material — see d0cce1cec for the context-management half.

The sub-questions: (1) what is chain-of-thought and when does the paper claim it helps;
(2) how does self-consistency change CoT and what does it report; (3) how does
tree-of-thoughts generalize CoT and what does it report; (4) what do the papers themselves
say about cost and when each technique does *not* help; (5) how does this paper-anchored
ladder refine the engine's escalate-only-when-it-pays rule.

## 1. Chain-of-thought: a reasoning scaffold that emerges only at scale (Wei et al., arXiv:2201.11903)

Chain-of-thought (CoT) prompting supplies a few exemplars in which the answer is preceded
by a series of intermediate natural-language reasoning steps; the paper's central claim is
that such reasoning abilities **emerge naturally only in sufficiently large language
models** via this simple few-shot method [cf83dbc59]. The headline result: prompting
**PaLM 540B with just eight CoT exemplars** achieves state-of-the-art accuracy on the
**GSM8K** benchmark of math word problems, surpassing even a fine-tuned GPT-3 with a
verifier [cf83dbc59]. Concretely, on PaLM 540B the paper reports GSM8K accuracy rising
from **17.9% (standard prompting) to 56.9% (CoT), a +39.0-point gain**; the same table
reports SVAMP **69.4 → 79.0 (+9.6)**, AQuA **25.2 → 35.8 (+10.6)**, and MAWPS
**79.2 → 93.3 (+14.2)**, all PaLM 540B [cf83dbc59].

The crucial qualifier the paper states itself: CoT is an **emergent ability of model
scale** — it does *not* positively (and can negatively) affect performance for smaller
models, yielding gains only at roughly the ~100B-parameter scale [cf83dbc59]. The paper
also notes the largest gains accrue on harder multi-step problems like GSM8K, while
benchmarks needing only a few reasoning steps see smaller gains [cf83dbc59].

## 2. Self-consistency: sample diverse paths, marginalize by majority vote (Wang et al., arXiv:2203.11171)

Self-consistency is a **decoding strategy** that replaces the greedy decoding used in CoT.
Its "sample-and-marginalize" procedure: (1) keep CoT prompting, (2) sample a *diverse set
of reasoning paths* from the decoder instead of taking only the greedy one, and (3)
**marginalize out the reasoning paths by taking a majority vote over the final answers**
[cf02b8fc1]. The intuition is that a complex problem admits multiple valid ways of
thinking that converge on the same correct answer [cf02b8fc1].

The paper's abstract headline gains (absolute accuracy improvements over CoT):
**GSM8K +17.9%, SVAMP +11.0%, AQuA +12.2%, StrategyQA +6.4%, ARC-challenge +3.9%**
[cf02b8fc1]. The +17.9-point GSM8K figure is reported for PaLM-540B (74.4% with
self-consistency) and is matched by Code-davinci-002 (78.0%, also +17.9) [cf02b8fc1].
Experimentally these are averaged over 10 runs sampling **40 outputs** per question
[cf02b8fc1]. The paper reports gains are larger on larger models (e.g. +3-6% absolute over
UL2-20B but +9-23% for LaMDA-137B) and that sampling more paths (1, 5, 10, 20, 40)
consistently raises accuracy, with self-consistency outperforming sample-and-rank, beam
search, and ensemble approaches [cf02b8fc1].

## 3. Tree-of-thoughts: deliberate search over thought states with LM self-evaluation (Yao et al., arXiv:2305.10601)

Tree-of-thoughts (ToT) **generalizes CoT**: instead of one left-to-right chain, it frames
problem-solving as search over a tree whose nodes are coherent "thoughts" (intermediate
steps), letting the LM **consider multiple reasoning paths and self-evaluate choices** to
decide the next move, with the ability to look ahead and backtrack [c24586afe]. Search
heuristics come from **LM self-evaluation** of each state's progress (the paper's stated
novelty — prior search heuristics were programmed or learned), combined with classic
**breadth-first (BFS) or depth-first (DFS) search** algorithms [c24586afe].

The headline task is **Game of 24**: with GPT-4, **CoT prompting solved only 4% of tasks,
while ToT achieved a 74% success rate** [c24586afe]. The detail table reports standard IO
prompting 7.3%, CoT 4.0%, and CoT-with-self-consistency 9.0% — versus ToT at **45% with
breadth b=1 and 74% with b=5** [c24586afe]. ToT was also evaluated on Creative Writing and
5×5 mini-crosswords, where it improved over IO/CoT (crosswords: IO/CoT under 16% word-level
success vs. ToT substantially higher) [c24586afe].

## 4. What the papers themselves say about cost and limits

Each rung's gain comes at a stated cost, and each paper bounds its own applicability:

- **CoT** is emergent: the gain is **conditional on large model scale** and is costly to
  serve at that scale; it does not help (and can hurt) smaller models [cf83dbc59].
- **Self-consistency** multiplies inference cost — it requires sampling and aggregating
  many reasoning paths (40 in the paper's main experiments), so its cost scales with the
  number of sampled paths, with accuracy gains continuing as paths increase from 1 to 40
  [cf02b8fc1].
- **ToT** adds search overhead and the paper says so plainly: deliberate search **"might
  not be necessary for many existing tasks that GPT-4 already excels at"**, and ToT
  **requires more resources** (e.g. GPT-4 API cost) than a single CoT call — the paper
  reports a per-case cost on the order of $0.74 for Game of 24 [c24586afe]. Its
  recommendation: use ToT on tasks requiring deliberate reasoning where CoT struggles, and
  on easier tasks the extra search is wasted [c24586afe].

## 5. How this refines the engine's escalate-only-when-it-pays rule

This paper-anchored ladder sharpens d0cce1cec's qualitative cost/capability ordering into
defensible primary-sourced rungs, and the papers' own limit statements *are* the escalation
rule:

- Do not reach for CoT-style reasoning scaffolds when the serving model is small — the
  originating paper shows the gain is emergent at scale and absent or negative below it
  [cf83dbc59].
- Escalate from a single CoT chain to self-consistency only when the task admits a
  verifiable single answer (so majority vote is meaningful) and the accuracy gain justifies
  multiplying inference by the number of sampled paths [cf02b8fc1].
- Escalate to ToT only for problems needing exploration, lookahead, or backtracking where
  CoT measurably struggles (Game-of-24-like search), because the paper itself says the
  search overhead is wasted on tasks the base model already handles [c24586afe].

The blog-relayed numbers d0cce1cec flagged are now retired in favor of these
paper-attributed figures, each bound to its exact paper + benchmark + model. For the
context-management half of this topic (lost-in-the-middle, context stuffing), see
d0cce1cec.
