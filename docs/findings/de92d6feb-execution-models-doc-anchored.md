---
id: de92d6feb
topic: 12-tooling-landscape
title: "Agent-framework execution models, stated in each framework's own documented primitives"
status: draft
---

# Agent-framework execution models, stated in each framework's own documented primitives

The execution-model taxonomy for agent orchestration frameworks — choose by
control-flow model, not by a "best framework" listicle ranking — is established and
re-argued elsewhere [d28841446]; this finding does not relitigate that. Its sole
contribution is to **doc-anchor** each framework's execution model to that
framework's own primary documentation or paper, replacing blog-convergent prose
with the named primitives the maintainers themselves use. All four sources here are
primaries — three official docs and one arXiv paper — so this finding is
primary-only.

The organizing question: *what is the unit of computation in each framework, and
how does data move between units?* The four answers are genuinely different shapes,
which is exactly why the taxonomy is durable.

## LangGraph — a typed shared-state graph stepped by message passing

LangGraph's documented model has three primitives: **State** (a shared data
structure, "the current snapshot of your application," typically a typed schema),
**Nodes** (functions that receive the current state, do work, and return a state
update), and **Edges** (functions that decide which node runs next) [cf59fd727].
The doc's own summary: "nodes do the work, edges tell what to do next" [cf59fd727].
The unit of computation is the **node**; the main graph class is `StateGraph`,
parameterized by a user-defined `State` object, and a graph is assembled by adding
nodes and edges and then calling `.compile()` [cf59fd727].

Data moves by **message passing over shared state channels**. The docs state the
underlying algorithm "uses message passing to define a general program": when a
node completes it "sends messages along one or more edges," recipient nodes activate
on incoming messages, and — inspired by Google's Pregel — "the program proceeds in
discrete 'super-steps,'" terminating when all nodes are inactive and no messages are
in transit [cf59fd727]. How concurrent updates to the same state key are merged is
governed by **reducers**; the docs call reducers "key to understanding how updates"
are applied [cf59fd727]. A node "can write to any state channel in the graph state,"
and the graph state is "the union of the state channels defined at initialization"
[cf59fd727]. This is the graph / state-machine model in its maintainers' own terms.

## LlamaIndex Workflows — event-driven steps that emit and consume events

LlamaIndex's documented model is explicitly **event-driven**: "A workflow is an
event-driven, step-based way to control the execution flow of an application"
[c75bec793]. The unit of computation is the **step** — "A step receives an event,
does some work, and returns another event. That returned event triggers the next
step whose type annotation accepts it" — and the docs add, "That is the whole model"
[c75bec793]. A step is a method decorated with `@step`; the `@step` decorator infers
each step's input and output types from its signature rather than from an explicit
wiring step [c75bec793].

Data moves as **typed events**: "The event types describe the edges of the
workflow, and regular Python describes the logic inside each edge" [c75bec793]. Two
framework-provided events bracket a run — `StartEvent` marks "where to send the
initial workflow input," and a step returning `StopEvent` (or a subclass) is the
terminal event [c75bec793]. Before running, Workflows **validates the event graph**
described by the step signatures, checking that start and stop events exist, that
"produced events have consumers, consumed events have producers, and the graph does
not contain accidental dead ends" [c75bec793]. For dynamic fan-out the docs document
`ctx.send_event(...)` to emit events incrementally and `ctx.collect_events(...)` to
wait for a known set, with `ctx.store` for shared per-run state [c75bec793]. The
distinguishing primitive is the **event**, not a node-and-edge graph object: edges
are implied by event types on step signatures.

## DSPy — declarative modules with signatures, compiled by teleprompters

DSPy is the model that breaks from the other three: its unit is not a runtime
node/step/agent but a **declarative module**, and the load-bearing operation happens
at **compile time**, not at orchestration time. The paper translates string-based
prompting techniques "into declarative modules that carry natural-language typed
signatures," and contributes three abstractions: **signatures** (which "abstract the
input/output behavior of a module"), **modules** (which "replace existing
hand-prompting techniques and can be composed in arbitrary pipelines"), and
**teleprompters** (which "optimize all modules in the pipeline to maximize a
metric") [c638230a6]. Built-in modules such as `ChainOfThought` are themselves
implemented "in a few lines of code by expanding the user-defined signature" and
calling `Predict` on the new signature [c638230a6].

The differentiator is **compilation**. "A key source of DSPy's expressive power is
its ability to compile — or automatically optimize — any program in this programming
model"; compiling "relies on a teleprompter, which is an optimizer." The compiler's
inputs are "the program, a few training inputs with optional labels, and a
validation metric"; it "simulates versions of the program on the inputs and
bootstraps example traces of each module," using them "to construct effective
few-shot prompts or finetuning small LMs" [c638230a6]. The explicit analogy is to
neural-network abstractions, "where ... the model weights can be trained using
optimizers instead of being hand-tuned" [c638230a6]. The paper reports that "within
minutes to tens of minutes of compiling, compositions of DSPy modules can raise the
quality of simple programs from 33% to 82% (Sec 6) and from 32% to 46%" [c638230a6].
So DSPy is not a competitor execution model to the other three; it is a **compile-time
prompt/weight optimizer** that composes with an orchestrator rather than replacing
it [d28841446].

## AutoGen Core — message-passing agents over a runtime

AutoGen Core's documented foundation is a **runtime environment** "which facilitates
communication between agents, manages their identities and lifecycles, and enforce
security and privacy boundaries" [ccd7e36d6]. The unit of computation is the
**agent**, and data moves as **messages routed through the runtime**: "agents
communicate via messages through the runtime, and the runtime manages the lifecycle
of agents" [ccd7e36d6]. This is the actor-style model — independent agents that own
their state and interact only by message — with the runtime as the message fabric.

The runtime comes in two documented forms with an identical agent-facing API: a
**standalone** runtime "suitable for single-process applications where all agents
are ... running in the same process" (e.g. `SingleThreadedAgentRuntime`), and a
**distributed** runtime for "multi-process applications where agents may be
implemented in different programming languages and running on different machines,"
consisting of "a host servicer and multiple workers" where the host servicer
"facilitates communication between agents across workers" [ccd7e36d6]. Crucially,
"agents work the same way as in the standalone runtime so that developers can switch
between the two runtime types with no change to their agent implementation"
[ccd7e36d6] — the message-passing-over-a-runtime model is invariant across
deployment topology.

## The taxonomy, now resting on primitives rather than prose

Each framework's execution model is now stated in its maintainers' own named
primitives: LangGraph = `StateGraph` of nodes/edges over reducer-merged shared state
stepped in super-steps [cf59fd727]; LlamaIndex = `@step` methods consuming and
emitting typed events with a validated event graph [c75bec793]; AutoGen Core =
message-passing agents over a standalone-or-distributed runtime [ccd7e36d6]; DSPy =
declarative modules with signatures, compiled by teleprompters against a metric
[c638230a6]. This is the doc-anchored substance behind the established
"choose-by-execution-model" taxonomy [d28841446], with DSPy correctly placed as a
compile-time optimizer orthogonal to the three runtime models.

## Gaps found → re-scan

- AutoGen's pub/sub primitives (topics, subscriptions, direct vs. broadcast
  messaging) are listed in the docs' nav but not on the "Agent Runtime
  Environments" page captured here; gather the official "Topic and Subscription"
  page to doc-anchor AutoGen's broadcast model.
- LangGraph's `Send` and `Command` primitives (dynamic fan-out and combined
  state-update-plus-goto control flow) are present in the source's page index but
  not yet doc-anchored in a finding.
- No primary covers cross-framework composition concretely (e.g. a DSPy-compiled
  module invoked from inside a LangGraph node or AutoGen agent); the orthogonality
  claim is currently inferential rather than doc-demonstrated.
