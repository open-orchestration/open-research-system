---
status: draft
topic: 14-papers
id: de3e9818e
title: "The foundational agent/RAG papers: ReAct, Self-RAG, Toolformer and the tool-learning survey, and what the engine inherits"
---

# The foundational agent/RAG papers: ReAct, Self-RAG, Toolformer and the tool-learning survey, and what the engine inherits

Three primary papers and one survey form the theoretical bedrock under this
system's loop, retrieval, and tool use. ReAct establishes interleaved
reasoning-and-acting against external sources [c945ec53b]; Self-RAG makes
retrieval on-demand and self-critiqued via reflection tokens [c87627e75];
Toolformer shows a model can teach itself when and how to call external tools
[c787b37e4]; and a tool-learning survey situates these mechanisms within a
broader taxonomy of how LLM agents retrieve, plan, and invoke tools
[c0eda480d]. This finding states what each paper's mechanism *is*, the reported
evidence, how they connect and where they stop, and maps them onto the engine's
own design. (Provenance note: the load-bearing numbers come from the genuine
papers/venue pages; the ReAct results table is reported on Google Research's
blog summarizing the paper [cb67d0c08], so where blog and paper overlap the
paper/venue is treated as primary [c945ec53b][c109a5136].)

## What each paper's mechanism is

**ReAct — interleaved reasoning and acting.** ReAct (Yao et al., ICLR 2023)
prompts an LLM to generate *both* free-form reasoning traces and task-specific
actions in an interleaved manner, so reasoning traces help the model induce,
track, and update action plans and handle exceptions, while actions let it
interface with external sources such as knowledge bases or environments to
gather information [c945ec53b][c109a5136]. Operationally this is a
Thought–Action–Observation loop: the task-solving trajectory consists of
multiple reasoning–action–observation steps, where for reasoning-heavy tasks the
model alternates reasoning and actions, and for action-heavy decision tasks
reasoning traces appear only sparsely at the most relevant positions
[cb67d0c08]. ReAct was demonstrated on a frozen PaLM-540B prompted with only
few-shot in-context examples to emit domain-specific actions (e.g. "search" for
QA, "go to" for navigation) [cb67d0c08].

**Self-RAG — on-demand retrieval plus reflection tokens.** Self-RAG (Asai et
al., NeurIPS 2023 Instruction Workshop / arXiv 2310.11511) trains a single
arbitrary LM to *adaptively retrieve passages on demand* and to generate and
reflect on retrieved passages and its own output using special **reflection
tokens** [c87627e75][c1ff42e4d]. There are four reflection-token types: a
**Retrieve** token (input x or x,y → {yes, no, continue}) that decides when to
call the retriever; **IsRel** (x,d → {relevant, irrelevant}); **IsSup** (x,d,y →
{fully supported, partially supported, no support}); and **IsUse** (x,y →
{5,4,3,2,1}) — the last three are *critique* tokens [c54d2906e]. Reflection
tokens are unified as next-token prediction from an expanded vocabulary, and the
generator is trained on a corpus interleaving retrieved passages and reflection
tokens produced by a separate critic model [c54d2906e]. At inference the model
self-evaluates: it decides retrieval via a tunable threshold on the
Retrieve=Yes probability, processes K passages in parallel, and runs a
segment-level beam search whose score is a weighted sum of the normalized
critique-token probabilities — and those weights are inference-time
hyperparameters, making behavior controllable per task [c54d2906e]. This
contrasts with conventional RAG, which retrieves a fixed number of documents
regardless of necessity and never revisits generation quality [c54d2906e].

**Toolformer — self-supervised tool use.** Toolformer (Schick et al.,
arXiv 2302.04761) is a model trained to decide *which* APIs to call, *when*,
*what arguments* to pass, and *how* to incorporate the results into future
token prediction — done in a self-supervised way requiring only a handful of
demonstrations per API [c787b37e4]. The incorporated tools are a calculator, a
Q&A system, two search engines, a translation system, and a calendar
[c787b37e4]. The motivation is the paradox that LLMs solve new tasks from few
examples yet struggle with basic functions like arithmetic or factual lookup
where smaller models excel [c787b37e4].

**The survey — a taxonomy of tool-learning agents.** The fourth source is
*LLM-Based Agents for Tool Learning: A Survey* (Springer, *Data Science and
Engineering*), which reviews tool-learning agents: it defines the tool-learning
task, describes the typical agent architecture, splits tool-retrieval methods
into training-based and non-training-based, and organizes tool *planning* by
whether the agent relies on its own inherent reasoning (internal planner) or
calls external reasoning/planning tools (external planner) [c0eda480d]. It
treats Toolformer as a representative fine-tuned tool-use agent and notes the
open challenge that such agents struggle to invoke tools across multi-step
reasoning tasks where inter-connected tools need holistic planning [c0eda480d].
(This source is the survey *about* these papers, not any of the papers itself.)

## The reported evidence

**ReAct.** On question answering (HotpotQA) and fact verification (FEVER), ReAct
overcomes hallucination and error propagation seen in chain-of-thought (CoT) by
interacting with a simple Wikipedia API [c945ec53b]. The PaLM-540B prompting
results show ReAct alone is competitive with CoT but the best configuration
combines ReAct + CoT, reaching 35.1 exact match on HotpotQA (6-shot) and 64.6
accuracy on FEVER (3-shot), versus 28.7/57.1 for the standard baseline —
still below fully supervised SoTA (67.5 on HotpotQA using ~140k samples)
[cb67d0c08]. On two interactive decision-making benchmarks, ALFWorld and
WebShop, ReAct outperforms imitation and reinforcement-learning methods by an
absolute success rate of **34% and 10%** respectively, while prompted with only
one or two in-context examples [c945ec53b][c109a5136]; the blog's tables put
ReAct at 71 on ALFWorld (2-shot) and 40 on WebShop (1-shot) versus 45/30.1 for
act-only [cb67d0c08]. ReAct also produces more interpretable, human-like
task-solving trajectories than baselines without reasoning traces [c945ec53b].

**Self-RAG.** Self-RAG at 7B and 13B parameters significantly outperforms
state-of-the-art LLMs and retrieval-augmented models across a diverse task set;
specifically it outperforms ChatGPT and retrieval-augmented Llama2-chat on
open-domain QA, reasoning, and fact-verification tasks, and shows significant
gains in factuality and citation accuracy for long-form generation relative to
those models [c87627e75][c1ff42e4d]. The setup uses Llama2 7B/13B as the
generator base, Llama2 7B as the critic, off-the-shelf Contriever-MS MARCO as
the retriever, and ~150k instruction-output training pairs [c54d2906e].

**Toolformer.** Toolformer achieves substantially improved zero-shot
performance across a variety of downstream tasks, often competitive with much
larger models, *without sacrificing its core language-modeling abilities*
[c787b37e4].

## How they connect — and where each stops

The three papers share one move: let the model reach outside its parameters
during generation. ReAct reaches into environments/knowledge sources via actions
[c945ec53b]; Self-RAG reaches into a passage corpus via on-demand retrieval
[c87627e75]; Toolformer reaches into APIs via learned call insertion
[c787b37e4]. They differ on *how the decision to reach out is learned and
controlled*. ReAct's decision lives in a prompted reasoning trace at inference,
needing no training [cb67d0c08]; Self-RAG's lives in trained reflection tokens
that gate retrieval and critique output, controllable via inference-time weights
and thresholds [c54d2906e]; Toolformer's lives in self-supervised training that
bakes the when/which/what of API calls into the model itself [c787b37e4].

What each does *not* solve: ReAct's best QA numbers still trail fully supervised
SoTA by a wide margin (35.1 vs 67.5 on HotpotQA), so prompted reasoning+acting
narrows but does not close the gap to task-specific training [cb67d0c08].
Self-RAG targets the failure of conventional RAG that retrieves a fixed number
of passages regardless of necessity or relevance and never re-checks quality —
but it requires training a critic and the generator on reflection-augmented data
rather than working zero-shot [c54d2906e]. Toolformer learns *individual* API
calls from a few demonstrations, but the survey flags that fine-tuned tool-use
agents like it still struggle to plan *inter-connected* tools across multi-step
reasoning [c0eda480d] — the gap that internal/external tool-planning methods in
the survey's taxonomy try to fill [c0eda480d].

## What the engine inherits

These papers are the theory behind the engine's three core mechanisms.

- **The loop.** The engine's gather/synthesize loop is a ReAct-style
  reason–act–observe cycle: it reasons about what to look for, acts by
  searching/fetching external sources, and observes results before continuing —
  the interleaving of reasoning traces with external-source actions that ReAct
  introduced [c945ec53b][cb67d0c08]. ReAct's finding that the strongest
  configuration combines acting with internal reasoning (ReAct + CoT)
  [cb67d0c08] is the justification for keeping a reasoning step around tool
  calls rather than acting blindly.

- **Retrieval gating.** The engine's practice of retrieving on demand and then
  judging whether retrieved material is relevant and whether a claim is
  supported mirrors Self-RAG's Retrieve / IsRel / IsSup / IsUse reflection
  tokens [c54d2906e]; Self-RAG's threshold-gated, controllable retrieval is the
  precedent for retrieving only when warranted instead of always pulling a fixed
  set [c54d2906e], and its per-segment support-and-citation self-assessment is
  the precedent for this engine's citation-first, faithfulness-gated drafting
  [c87627e75].

- **Tool use.** Toolformer establishes that deciding which tool to call, when,
  and with what arguments is itself a learnable, model-driven competence
  [c787b37e4], while the survey supplies the architectural vocabulary — tool
  retrieval (training- vs non-training-based) and tool planning (internal vs
  external planner) — for reasoning about how an agent should select and
  sequence tools [c0eda480d]. The survey's open challenge of planning
  inter-connected tools over multi-step tasks [c0eda480d] is exactly the
  orchestration problem an autonomous research engine faces when chaining
  search, fetch, retrieval, and synthesis.
