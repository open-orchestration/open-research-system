---
status: draft
topic: 07-agentic-orchestration
id: d5c35de17
---

# The halt decision: how self-correcting agent loops decide when to stop, and why bounding it is the hard part

The self-correcting loop family (ReAct, Reflexion, CRAG, Self-RAG, and multi-agent
debate) is usually taxonomized by *what each adds* to a plain generate step. A more
useful axis for an engine that has to actually run these loops is *where the halt
decision lives and what bounds it* — because an unbounded "iterate until dry" loop
is the dominant failure mode, not a feature.

## Sub-questions framed

1. **Mechanism:** Where does each pattern place the "should I loop again?" decision?
2. **Bounding:** What stops the loop, and is the bound external (a hard cap) or internal (a model self-judgment)?
3. **Contrast:** Is single-agent reflection the same control problem as multi-agent debate?
4. **Evidence/tradeoff:** What does the most rigorous source actually claim about whether iterating/collaborating helps?

## Key claims (cited)

### Where the halt decision lives

- ReAct is the base case of the family: an iterative loop where the agent reasons
  about the current state, takes an action (e.g. querying a database), and observes
  the outcome before planning the next step — there is no separate self-critique
  stage, the loop simply continues until the agent decides to answer [cf4ac4282].
- CRAG places the loop's decision in a dedicated *retrieval evaluator* (a small, fast
  model) that scores retrieved documents and classifies them as **Correct**,
  **Incorrect**, or **Ambiguous**, branching to: use-as-is (with a "decompose-then-
  recompose" refinement that strips non-essential content), discard-and-web-search,
  or both [cf4ac4282]. A secondary explainer describes the same three-way branch and
  characterizes the evaluator as cheap because it is a small fast model [c33ed5b08],
  and a third frames CRAG generically as a *feedback loop* that "continuously
  evaluates the quality of retrieved documents" [cca3f9321].
- CRAG as described is fundamentally a **single-pass correction**, not a true
  repeating loop: where CRAG does one correction, Reflexion runs a true feedback loop
  that repeats [c3944e6ab].
- Self-RAG moves the halt decision *inside the model itself* by fine-tuning it to emit
  "reflection tokens": a `Retrieve` token decides whether external information is even
  needed, `ISREL` scores passage relevance, `ISSUP` checks whether a generated segment
  is actually supported by retrieved facts (an anti-hallucination check), and `ISUSE`
  scores overall utility [cf4ac4282]. The whole RAG loop therefore runs inside one
  model, which buys tight integration and adaptive retrieval at the cost of requiring
  fine-tuning — it is "less plug-and-play" than CRAG [c33ed5b08].
- Reflexion (attributed to Shinn et al., 2023, in the source) makes an agent
  self-improve through iteration: it drafts an answer, names its own information gaps,
  retrieves to fill them, then revises — repeating until the answer is complete or a
  maximum number of iterations is reached [c3944e6ab].

### What actually bounds the loop

- In a concrete Reflexion implementation, the loop is bounded by *both* an internal
  self-judgment and an external hard cap: the router continues to retrieve only while
  the answer is incomplete, there are queries left, AND the iteration budget is not
  exhausted (`is_complete or not search_queries or iteration_count >= MAX_ITERATIONS`
  routes to END) [c3944e6ab].
- The internal self-judgment is not trusted on its own: the revise step includes a
  "force-complete" safeguard that terminates the loop if the model claims the answer
  is incomplete but provides no new queries to act on [c3944e6ab]. This is direct
  evidence that "iterate until the model says it's done" is unsafe without a guard.
- A blueprint source generalizes this as the "Loop Pattern": the agent repeatedly
  refines through reflection until a quality threshold or explicit "termination
  condition" is met [cf4ac4282] — i.e. a termination condition is treated as a
  required design element, not an afterthought.

### Single-agent reflection vs. multi-agent collaboration is the same control problem

- The multi-agent case inherits and amplifies the same unbounded-loop hazard.
  Anthropic reports early agents "spawning 50 subagents for simple queries, scouring
  the web endlessly for nonexistent sources, and distracting each other with excessive
  updates" — failures of *when to stop and how much to spawn*, which they fixed
  primarily through prompt engineering rather than code [c1dcd6346].
- The cost of an unbounded multi-agent loop is steeper because state compounds:
  "agents are stateful and errors compound," minor changes cascade into large
  behavioral changes, and the system needs deterministic safeguards like retry logic
  and regular checkpoints layered onto the agent's adaptability [c1dcd6346].

### What the most rigorous source claims about whether collaboration helps

- The one peer-reviewed source here (Oriol et al., 2025, an arXiv/RE-conference paper)
  is deliberately cautious: it conducts a *systematic study* of existing Multi-Agent
  Debate strategies, builds a taxonomy of their core attributes, and reports only a
  *preliminary* evaluation demonstrating the **feasibility** of applying MAD to
  requirements-engineering classification — it concludes MAD is "a promising approach"
  and explicitly frames itself as a foundational understanding, not a benchmark win
  [cea4d6678]. The motivating premise is that single-pass outputs "without iterative
  refinement or collaboration" limit robustness and adaptability [cea4d6678].

## Convergent vs. contested

- **Convergent:** Every pattern is a loop with a halt decision, and the practitioner
  evidence (Reflexion's `MAX_ITERATIONS` + force-complete guard [c3944e6ab];
  Anthropic's 50-subagent runaway [c1dcd6346]) agrees that the model's own
  "I'm done" judgment must be backed by an external bound.
- **Contested / underdetermined:** Whether iterative refinement or debate actually
  *improves accuracy* is asserted by blogs but only weakly established by the rigorous
  source — Oriol et al. claim feasibility and promise, not a measured accuracy gain
  [cea4d6678]. The CRAG/Self-RAG mechanism descriptions are consistent across three
  independent secondary explainers [cf4ac4282][c33ed5b08][cca3f9321], but none of the
  corpus sources here supply a reproducible head-to-head benchmark.

## Provenance note

The load-bearing thesis (the halt-decision axis and the need to bound loops
externally) rests on the one runnable, inspectable implementation [c3944e6ab] and the
official engineering account of production failures [c1dcd6346], with the rigor anchor
on whether collaboration helps coming from the peer-reviewed paper [cea4d6678]. The
CRAG/Self-RAG branch descriptions are conceptual mechanism claims corroborated across
three secondary explainers and are not used to carry any benchmark number.
