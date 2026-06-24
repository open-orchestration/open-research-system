---
id: d1fb5a112
topic: 12-tooling-landscape
title: "Two dispatch philosophies, grounded in their own docs: LangGraph Send/Command (explicit graph edges + per-branch state) vs AutoGen Topic/Subscription (decoupled publish/subscribe)"
status: draft
---

# Two dispatch philosophies, grounded in their own docs: LangGraph Send/Command vs AutoGen Topic/Subscription

Finding [d28841446] argues the durable axis for agent-orchestration frameworks is
the **execution-model taxonomy** (graph/state-machine vs. multi-agent
conversation vs. …), not a "best framework" ranking — but it flags as a gap that
**no primary LangGraph or AutoGen documentation is in that corpus**; its
execution-model shapes rest on convergent blogs plus one Microsoft doc
[d28841446]. This finding closes part of that gap by grounding the **concrete
control-flow primitives** of two of those models directly on each framework's
**own official documentation**: LangGraph's graph/state-machine model
(`Send`, `Command`) on the LangChain LangGraph Graph API docs [cc413ffed], and
AutoGen's event-driven pub/sub model (Topic, Subscription) on Microsoft's AutoGen
core docs [cce59d029]. Both sources are the frameworks' own API documentation, so
they are primary for "how X's own API works"; both are crawl4ai markdown captures
with navigation cruft, and the claims below were confirmed whitespace-insensitively
against the source bytes.

The load-bearing thesis: these two primitive sets embody **two different dispatch
philosophies**. LangGraph routes by *explicit graph edges with per-branch state* —
the sender (a node or routing function) names exactly which node(s) run next and
what state each receives. AutoGen routes by *decoupled publish/subscribe* — a
broadcasting sender does **not** name recipients at all; subscriptions decide who
receives. The choice shapes how you express fan-out and agent-to-agent
communication.

## Sub-question 1: what problem does `Send` solve that static edges cannot?

In LangGraph, nodes and edges are normally defined ahead of time and operate on
the same shared state; static `add_edge("node_a", "node_b")` always routes A→B
[cc413ffed]. But sometimes the exact edges are **not known ahead of time**, and/or
you want **different versions of `State` to exist at the same time** — and static
edges cannot express either [cc413ffed]. The canonical case the docs name is the
**map-reduce** design pattern: a first node generates a list of objects and you
apply a downstream node to all of them, where the number of objects (hence the
number of edges) is unknown ahead of time and each downstream invocation should
receive a *different* input state [cc413ffed]. `Send` is the primitive for this
**dynamic fan-out**: it is returned from conditional edges and takes two arguments
— the name of the target node and the state to pass to that node — so a routing
function can emit one `Send` per generated item [cc413ffed]. This is dispatch where
the *sender explicitly names each target node and hands it a tailored state*.

## Sub-question 2: what does `Command` fuse, and why use it over conditional edges?

`Command` is the LangGraph primitive that **combines state updates and routing in a
single function** — the docs say to use it "instead of conditional edges" when you
want to do both [cc413ffed]. It packages an **`update`** (apply state updates, as
when returning updates from a node) together with a **`goto`** (navigate to
specific node(s), as conditional edges do) [cc413ffed]. The docs also list a
**`graph`** parameter — set to **`graph=Command.PARENT`** to navigate from a node
inside a subgraph to a node in the parent graph, which the docs call particularly
useful for multi-agent handoffs — and a `resume` parameter for continuing after an
interrupt [cc413ffed]. The decision rule the docs give: use `Command` when you need
to **both** update state **and** route; if you only need to route without updating
state, use conditional edges instead [cc413ffed]. Either way the routing is still
*explicit and node-named* — `Command` only adds dynamic edges, and the docs warn
that for a given node you should use either `Command`/dynamic routing or static
edges, not both, since both paths would execute [cc413ffed].

## Sub-question 3: what is an AutoGen Topic, and how does TypeSubscription route?

AutoGen's model is the opposite end of the dispatch spectrum. A **Topic** has two
components — a **Topic Type** and a **Topic Source** — analogous to an agent ID
[cce59d029]. A **Subscription** maps topics to agents; the runtime uses
subscriptions to decide who receives a broadcast [cce59d029]. The Python API
**`TypeSubscription`** implements **type-based subscription**, which maps a
**Topic Type → Agent Type**: it declares an unbounded mapping from topics to agent
IDs without knowing the exact topic sources or agent keys, so any topic matching the
subscription's topic type is mapped to an agent ID whose type is the subscription's
agent type and whose key is the value of the topic source [cce59d029]. The docs
state type-based subscription is generally the **preferred** way to declare
subscriptions because it is **portable and data-independent** — developers do not
write application code that depends on specific agent IDs [cce59d029]. Crucially,
the *publisher names a topic, not a recipient*; the subscription layer resolves
which agents are addressed.

## Sub-question 4: broadcast vs. direct messaging — what is decoupled?

AutoGen's runtime delivers messages two ways [cce59d029]:

- **Direct messaging** — one-to-one; the sender **must provide the recipient's
  agent ID** [cce59d029].
- **Broadcast** — one-to-many via publish; the sender **does NOT provide
  recipients' agent IDs** [cce59d029].

The docs motivate broadcast precisely by decoupling: in event-driven workflows,
agents do not always know who will handle their messages, and a workflow can be
composed of agents with no inter-dependencies [cce59d029]. This is the structural
inverse of LangGraph's explicit edges: in LangGraph the sender always names the
next node(s) (via `Send`/`Command`/conditional edges); in AutoGen broadcast the
sender names only a topic and is deliberately ignorant of recipients [cce59d029].

Subscription patterns are organized along two axes: **single-tenant vs.
multi-tenant**, and **single-topic vs. multiple-topics-per-tenant**, where a
"tenant" is a set of agents handling a specific user session/request [cce59d029].
In single-tenant scenarios the topic source is hard-coded (e.g. `"default"`); a
good indication of a multi-tenant scenario is needing multiple instances of the
same agent type — at which point the topic source becomes data-dependent (e.g. a
unique issue identifier), and the runtime creates a per-source agent instance on
demand [cce59d029].

## Sub-question 5: how do these embody different execution models per [d28841446]?

Mapping onto [d28841446]'s taxonomy, these two primitive sets are the concrete
control-flow machinery of two of its execution models — and the contrast is sharp:

- **LangGraph = graph/state-machine model.** Routing is by **explicit edges**;
  the sender names the next node(s). `Send` expresses dynamic fan-out with
  **per-branch state** (a distinct `State` per target), and `Command` **fuses**
  the state write and the routing decision into one return value [cc413ffed]. The
  control flow is a graph you can render and reason about — the docs even require
  return-type annotations listing the nodes a `Command` may route to so the graph
  can be drawn [cc413ffed].
- **AutoGen = event-driven pub/sub model.** Routing is by **decoupled
  publish/subscribe**; on broadcast the sender names a **topic, not a recipient**,
  and `TypeSubscription` (Topic Type → Agent Type) resolves recipients
  data-independently [cce59d029]. Senders and receivers need no inter-dependencies
  [cce59d029].

So the durable, doc-anchored difference is **who decides the recipient and when**:
in LangGraph the *sending node* decides explicitly and per-branch; in AutoGen the
*subscription configuration* decides, and the sender stays decoupled. That choice
shapes how each framework naturally expresses fan-out (LangGraph: one `Send` per
item with tailored state; AutoGen: one publish to a topic that many subscribers
receive) and agent-to-agent communication (LangGraph: explicit handoff via
`Command(graph=Command.PARENT)`; AutoGen: implicit via topic membership)
[cc413ffed][cce59d029]. This grounds, on primary sources, the control-flow shapes
that [d28841446] could previously support only from blogs plus one Microsoft doc
[d28841446].

## Provenance

Both primaries are the frameworks' **own official documentation** — primary for
"how X's own API works," not third-party characterizations: the LangChain LangGraph
Graph API docs (`docs.langchain.com/oss/python/langgraph/graph-api`) [cc413ffed]
and Microsoft's AutoGen core "Topic and Subscription" docs
(`microsoft.github.io/autogen/stable/.../topic-and-subscription.html`) [cce59d029].
Both were captured as crawl4ai markdown with interleaved navigation/menu cruft;
every load-bearing token above (`Send`, `map-reduce`, `Command`, `goto`, `update`,
`graph=Command.PARENT`, "combine state updates and routing"; `TopicType`,
`TopicSource`, `TypeSubscription`, "Type-Based Subscription", `broadcast`,
`direct messaging`, `single-tenant`/`multi-tenant`, "portable and
data-independent", "preferred") was verified whitespace-insensitively against the
source bytes.

## Gaps found

- **Cross-language parity not established.** Both sources document the **Python**
  surface (`from langgraph.types import Send`; `TypeSubscription(...)`). Whether the
  JS/.NET equivalents have identical signatures is not transcribed here; re-scan the
  respective language docs to confirm parity before any cross-language claim.
- **AutoGen `DefaultSubscription` not covered.** The captured page grounds
  `TypeSubscription` (type-based) only; other subscription mechanisms (e.g.
  `DefaultSubscription`) are not in scope of these bytes and are not claimed.
- **Exact `Command`/`Send` constructor signatures beyond the parameter names are
  not transcribed.** The four `Command` parameters (`update`, `goto`, `graph`,
  `resume`) and the two `Send` arguments (target node name, state) are confirmed,
  but full type signatures and defaults were not re-grepped and are deliberately not
  asserted.
- **No comparative/performance claim is made.** Consistent with [d28841446], this
  finding grounds only the *shape and semantics* of the primitives, not which model
  is faster, cheaper, or "better."
