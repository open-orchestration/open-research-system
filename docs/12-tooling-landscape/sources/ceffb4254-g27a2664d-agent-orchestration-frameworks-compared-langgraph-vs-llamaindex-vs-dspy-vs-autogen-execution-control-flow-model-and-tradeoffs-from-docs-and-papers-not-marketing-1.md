[Skip to content](https://www.youngju.dev/blog/culture/2026-05-16-ai-agent-frameworks-langchain-langgraph-llamaindex-crewai-autogen-pydanticai-mastra-dspy-mcp-2026-deep-dive.en#main-content)[ChaosAndOrder](https://www.youngju.dev/)
[Blog](https://www.youngju.dev/blog)[Tags](https://www.youngju.dev/tags)[Projects](https://www.youngju.dev/projects)[Tools](https://www.youngju.dev/tools)[Explore](https://www.youngju.dev/explore)[About](https://www.youngju.dev/about)
  1. [Home](https://www.youngju.dev/)
  2. /
  3. [Blog](https://www.youngju.dev/blog)
  4. /
  5. blog
  6. /
  7. AI Agent Frameworks 2026 Deep Dive — LangChain, LangGraph, LlamaIndex, CrewAI, AutoGen, PydanticAI, Mastra, DSPy, MCP Complete Guide

Published on
    2026년 5월 16일 토요일
# AI Agent Frameworks 2026 Deep Dive — LangChain, LangGraph, LlamaIndex, CrewAI, AutoGen, PydanticAI, Mastra, DSPy, MCP Complete Guide
[🇰🇷KO한국어](https://www.youngju.dev/blog/culture/2026-05-16-ai-agent-frameworks-langchain-langgraph-llamaindex-crewai-autogen-pydanticai-mastra-dspy-mcp-2026-deep-dive "한국어")🇺🇸ENEnglish[🇯🇵JA日本語](https://www.youngju.dev/blog/culture/2026-05-16-ai-agent-frameworks-langchain-langgraph-llamaindex-crewai-autogen-pydanticai-mastra-dspy-mcp-2026-deep-dive.ja "日本語")
[Split View](https://www.youngju.dev/split/culture/2026-05-16-ai-agent-frameworks-langchain-langgraph-llamaindex-crewai-autogen-pydanticai-mastra-dspy-mcp-2026-deep-dive)[필사 모드](https://www.youngju.dev/transcribe/culture/2026-05-16-ai-agent-frameworks-langchain-langgraph-llamaindex-crewai-autogen-pydanticai-mastra-dspy-mcp-2026-deep-dive.en) 

Authors
    
  * ![avatar](https://www.youngju.dev/static/images/avatar.jpg) 

Name
    Youngju Kim 

Twitter
    [@fjvbn20031](https://twitter.com/fjvbn20031)


##  [](https://www.youngju.dev/blog/culture/2026-05-16-ai-agent-frameworks-langchain-langgraph-llamaindex-crewai-autogen-pydanticai-mastra-dspy-mcp-2026-deep-dive.en#intro--may-2026-agent-frameworks-at-the-tail-end-of-consolidation)Intro — May 2026, agent frameworks at the tail end of consolidation
After the hype storm that lasted from late 2023 into early 2024, by May 2026 the AI agent framework market has settled into **three major currents**. First, LangChain remains the share leader despite endless criticism (over-abstraction, frequent breaking changes, debugging pain). Second, **MCP (Model Context Protocol), proposed by Anthropic** , has become a de-facto tool standard, weakening framework lock-in. Third, **newcomers that put "type safety" front and center, like PydanticAI and Mastra** , are eating into LangChain's enterprise base.
This article isn't a marketing comparison chart. It's an honest look at "what goes where in production today." We compare LangGraph's StateGraph, LlamaIndex's query engine, CrewAI's Crew/Task/Agent, PydanticAI's Agent decorator, Mastra's TypeScript agent, DSPy's compiler, Instructor's structured output, and the OpenAI Agents SDK and Vercel AI SDK 4, all with real API code.
##  [](https://www.youngju.dev/blog/culture/2026-05-16-ai-agent-frameworks-langchain-langgraph-llamaindex-crewai-autogen-pydanticai-mastra-dspy-mcp-2026-deep-dive.en#agent-frameworks-2026--decomposed-into-6-layers)Agent frameworks 2026 — decomposed into 6 layers
Start with the big picture. The 2026 agent stack splits into 6 layers:
  1. **Orchestration** : agent loop, tool calls, state management
  2. **Structured output** : Pydantic, Zod, JSON Schema, constrained decoding
  3. **RAG / knowledge** : embeddings, vector search, GraphRAG, context compression
  4. **Tool standards** : MCP, OpenAPI function calling, A2A
  5. **Memory** : short-term context, long-term episodic, per-user state
  6. **Observability and eval** : trace, run replay, eval suite


The era where one or two tools owned a layer is over. Now even **within a layer there's a split between the "LangChain camp", "Python-native camp", and "TypeScript camp."** We'll walk through each layer below.
##  [](https://www.youngju.dev/blog/culture/2026-05-16-ai-agent-frameworks-langchain-langgraph-llamaindex-crewai-autogen-pydanticai-mastra-dspy-mcp-2026-deep-dive.en#langchain--why-it-still-leads-despite-the-criticism)LangChain — why it still leads despite the criticism
Throughout 2025, X (Twitter) and Hacker News posted roughly one "why you should not use this" piece per week about LangChain. Even so, as of May 2026 the LangChain family (langchain, langchain-core, langchain-community) still passes 60 million monthly downloads on PyPI. The reason is simple: **there's too much code already written against it, and the number of integrated LLMs, vector DBs, and tools is overwhelming**.
The core is **LangChain Expression Language (LCEL)**. You compose chains with the pipe operator, and the `Runnable` interface handles sync/async/streaming uniformly. Breaking changes have dropped sharply since v0.3.

```
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatAnthropic(model="claude-opus-4-5-20250929")
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a senior staff engineer reviewing code."),
    ("human", "Review this diff and return concerns:\n\n{diff}"),
])

chain = prompt | llm | StrOutputParser()
result = chain.invoke({"diff": "<the code diff>"})

```

The `{diff}` above is a LangChain prompt-template placeholder. The same pattern propagates `{question}` `{context}` style variables through the chain. LangChain's real value lies in this placeholder convention plus the consistency of methods like `with_structured_output`, `bind_tools`, and `with_fallbacks`.
##  [](https://www.youngju.dev/blog/culture/2026-05-16-ai-agent-frameworks-langchain-langgraph-llamaindex-crewai-autogen-pydanticai-mastra-dspy-mcp-2026-deep-dive.en#langgraph--the-limits-of-chains-that-langchain-itself-admitted)LangGraph — the "limits of chains" that LangChain itself admitted
LCEL is great for linear chains, but it falls short on what agents really need: conditional branches, loops, and human-in-the-loop. LangGraph is the LangChain team's own **state-graph library** built to solve this. By late 2025 LangGraph became the fastest-growing package in the LangChain org.
The core is `StateGraph`. Nodes are functions, edges are conditions, and state accumulates via reducers. ReAct patterns, multi-agent handoffs, and human-review checkpoints all map cleanly onto the graph.

```
from typing import Annotated, TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages

class AgentState(TypedDict):
    messages: Annotated[list, add_messages]
    next: str

def planner(state: AgentState) -> dict:
    return {"next": "researcher", "messages": [{"role": "assistant", "content": "plan"}]}

def researcher(state: AgentState) -> dict:
    return {"next": END, "messages": [{"role": "assistant", "content": "found"}]}

graph = StateGraph(AgentState)
graph.add_node("planner", planner)
graph.add_node("researcher", researcher)
graph.add_edge(START, "planner")
graph.add_conditional_edges("planner", lambda s: s["next"])
app = graph.compile(checkpointer=...)

```

LangGraph's killer feature is its **checkpointer**. It saves runtime state to SQLite/Postgres/Redis, resumes after human approval, and supports time-travel debugging from any branch point. The single biggest production problem — "pause and wait for a human" — falls out naturally from this pattern.
##  [](https://www.youngju.dev/blog/culture/2026-05-16-ai-agent-frameworks-langchain-langgraph-llamaindex-crewai-autogen-pydanticai-mastra-dspy-mcp-2026-deep-dive.en#llamaindex--differentiating-on-rag-depth)LlamaIndex — differentiating on RAG depth
LlamaIndex (which started in 2022 as GPT Index) shipped around the same time as LangChain but took a different road by **focusing on retrieval-augmented generation (RAG)**. In 2026, LlamaIndex is "agents-capable but RAG-first." A single package gives you 70+ loaders, multi-tier indexes, GraphRAG, multi-query routing, and MetaGPT-style workflows.

```
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.llms.anthropic import Anthropic

documents = SimpleDirectoryReader("./docs").load_data()
index = VectorStoreIndex.from_documents(documents)

retriever = VectorIndexRetriever(index=index, similarity_top_k=10)
query_engine = RetrieverQueryEngine(
    retriever=retriever,
    llm=Anthropic(model="claude-opus-4-5-20250929"),
)

response = query_engine.query("What is the on-call rotation policy?")
print(response.response)
for node in response.source_nodes:
    print(node.metadata["file_path"], node.score)

```

Since late 2025 LlamaIndex has been pushing `Workflow`, an event-driven abstraction. It's similar to LangGraph's graphs but uses an event-dispatch model. Most reviewers agree LlamaIndex has the smoothest GraphRAG (entity graph + embeddings) implementation in the ecosystem.
##  [](https://www.youngju.dev/blog/culture/2026-05-16-ai-agent-frameworks-langchain-langgraph-llamaindex-crewai-autogen-pydanticai-mastra-dspy-mcp-2026-deep-dive.en#crewai--the-role-based-multi-agent-flagship)CrewAI — the role-based multi-agent flagship
CrewAI, started in 2024 by João Moura, puts the model that **"agents should collaborate like colleagues with assigned roles"** into code. You only need four first-class concepts: Agent, Task, Crew, and Process. The on-ramp is lower than LangChain's, so CrewAI shows up often in non-developer PoCs.

```
from crewai import Agent, Task, Crew, Process

researcher = Agent(
    role="Senior Researcher",
    goal="Find the latest on Claude Opus 4.5 benchmarks",
    backstory="A meticulous AI researcher who cross-checks every source.",
    verbose=True,
)

writer = Agent(
    role="Technical Writer",
    goal="Turn research into a 500-word brief",
    backstory="Writes for engineering leaders. No fluff.",
    verbose=True,
)

task1 = Task(description="Collect 5 sources", agent=researcher, expected_output="bullet list")
task2 = Task(description="Write the brief", agent=writer, expected_output="markdown")

crew = Crew(agents=[researcher, writer], tasks=[task1, task2], process=Process.sequential)
result = crew.kickoff()

```

CrewAI 1.0 (April 2025) added a graph-based API called `Flow`, enabling LangGraph-like branching. The downside is debugging — agents have high freedom and can wander off-task. For eval and observability you fall back on LangSmith or CrewAI's own Plus cloud.
##  [](https://www.youngju.dev/blog/culture/2026-05-16-ai-agent-frameworks-langchain-langgraph-llamaindex-crewai-autogen-pydanticai-mastra-dspy-mcp-2026-deep-dive.en#autogen--microsofts-conversational-multi-agent)AutoGen — Microsoft's conversational multi-agent
AutoGen is the multi-agent conversation framework that Microsoft Research released in 2023. It was completely redesigned for the 0.4 release in 2025. The core abstraction is **"conversations between agents,"** with GroupChat and GroupChatManager coordinating turn-taking.

```
from autogen_agentchat.agents import AssistantAgent
from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_ext.models.openai import OpenAIChatCompletionClient

model_client = OpenAIChatCompletionClient(model="gpt-4o")

coder = AssistantAgent("coder", model_client=model_client,
    system_message="You write Python. Output a single function.")
reviewer = AssistantAgent("reviewer", model_client=model_client,
    system_message="You review code. Approve or reject with reasons.")

team = RoundRobinGroupChat([coder, reviewer], max_turns=4)
result = await team.run(task="Write a function that parses ISO 8601 dates.")

```

AutoGen Studio is a GUI that lets you visually assemble agents and inspect runs. Its share is strongest in academia and research PoCs. That said, production operations (thread persistence, background execution, retry policies) still trail LangGraph by most accounts.
##  [](https://www.youngju.dev/blog/culture/2026-05-16-ai-agent-frameworks-langchain-langgraph-llamaindex-crewai-autogen-pydanticai-mastra-dspy-mcp-2026-deep-dive.en#pydanticai--the-rising-type-safe-agent-framework)PydanticAI — the rising type-safe agent framework
PydanticAI is an agent SDK released in late 2024 by the Pydantic team (Samuel Colvin and others). The tagline is **"FastAPI-feel for AI agents."** It applies Pydantic data validation directly to agent tool signatures and output schemas. It's being adopted the fastest as a LangChain alternative in the enterprise.

```
from pydantic import BaseModel
from pydantic_ai import Agent, RunContext

class WeatherResult(BaseModel):
    city: str
    temp_c: float
    condition: str

agent = Agent(
    "anthropic:claude-opus-4-5-20250929",
    result_type=WeatherResult,
    system_prompt="Return current weather as structured data.",
)

@agent.tool
async def get_weather(ctx: RunContext, city: str) -> dict:
    return {"temp_c": 18.4, "condition": "cloudy"}

result = await agent.run("What's the weather in Seoul?")
print(result.data.city, result.data.temp_c)

```

PydanticAI's strengths are **dependency injection** and **type inference**. You inject DB/HTTP clients through `RunContext`, and the `@agent.tool` decorator auto-derives JSON Schema from the function signature. Observability is first-class via Pydantic Logfire, and OpenTelemetry export is built in.
##  [](https://www.youngju.dev/blog/culture/2026-05-16-ai-agent-frameworks-langchain-langgraph-llamaindex-crewai-autogen-pydanticai-mastra-dspy-mcp-2026-deep-dive.en#mastra--the-typescript-camps-agent-framework)Mastra — the TypeScript camp's agent framework
Mastra is a **TypeScript-first** agent framework started in 2024 by Shane Thomas and team. It sits on top of the Vercel AI SDK and runs on Cloudflare Workers, Vercel Edge, and Node.js. It's quickly gaining share in the JavaScript full-stack world (especially Next.js shops).

```
import { Mastra } from "@mastra/core";
import { Agent } from "@mastra/core/agent";
import { anthropic } from "@ai-sdk/anthropic";
import { z } from "zod";

const supportAgent = new Agent({
  name: "support",
  instructions: "You handle customer support tickets concisely.",
  model: anthropic("claude-opus-4-5-20250929"),
  tools: {
    lookupOrder: {
      description: "Look up an order by id",
      parameters: z.object({ orderId: z.string() }),
      execute: async ({ orderId }) => ({ orderId, status: "shipped" }),
    },
  },
});

const mastra = new Mastra({ agents: { support: supportAgent } });
const result = await mastra.getAgent("support").generate("Where is order 1234?");

```

Mastra bundles workflows (LangGraph-like), RAG, eval, and memory into a single package. As Vercel's formal partnership deepens in 2026, the pattern of pairing Mastra with Next.js App Router server actions is becoming the de-facto.
##  [](https://www.youngju.dev/blog/culture/2026-05-16-ai-agent-frameworks-langchain-langgraph-llamaindex-crewai-autogen-pydanticai-mastra-dspy-mcp-2026-deep-dive.en#agno-smolagents-cog-letta--the-lightweight-and-specialized-camp)agno, smolagents, Cog, Letta — the lightweight and specialized camp
  * **agno** (formerly Phidata): bills itself as a "fast agent framework." Claims 5x lighter runtime overhead than LangChain. Multimodal, memory, and team agents are first-class concepts.
  * **smolagents** : HuggingFace's minimalist framework released in late 2024. Starts from a single definition: "an agent is an LLM with a code-execution tool." Its `CodeAgent` generates and runs Python directly.
  * **Cog** (Replicate): not an agent framework per se, but the closest thing to a standard for packaging agents as containers. A one-line `cog.yaml` turns a GPU model/agent into an OCI image.
  * **Letta** (formerly MemGPT): a memory-centric agent that started at UC Berkeley. The core paradigm is "page context in and out like an operating system." It has the highest share in long-running conversational bots.


##  [](https://www.youngju.dev/blog/culture/2026-05-16-ai-agent-frameworks-langchain-langgraph-llamaindex-crewai-autogen-pydanticai-mastra-dspy-mcp-2026-deep-dive.en#dspy--the-prompt-programming-paradigm-out-of-stanford)DSPy — the "prompt programming" paradigm out of Stanford
DSPy, led by Omar Khattab (Stanford), proposes a model where **you declare signatures and modules instead of writing prompts directly, then a compiler optimizes them automatically**. In 2026 it's actively adopted in academia and at some hedge funds and research labs.

```
import dspy

lm = dspy.LM("anthropic/claude-opus-4-5-20250929")
dspy.configure(lm=lm)

class RAG(dspy.Module):
    def __init__(self):
        super().__init__()
        self.retrieve = dspy.Retrieve(k=5)
        self.generate = dspy.ChainOfThought("context, question -> answer")

    def forward(self, question):
        ctx = self.retrieve(question).passages
        return self.generate(context=ctx, question=question)

rag = RAG()
optimized = dspy.MIPROv2(metric=dspy.evaluate.answer_exact_match).compile(rag, trainset=train)

```

The core insight is that "prompt engineering gets replaced by code generation." Few-shot selection, instruction writing, and chain-of-thought shape are all auto-tuned by the compiler (MIPROv2, BootstrapFinetune, and friends) against training data.
##  [](https://www.youngju.dev/blog/culture/2026-05-16-ai-agent-frameworks-langchain-langgraph-llamaindex-crewai-autogen-pydanticai-mastra-dspy-mcp-2026-deep-dive.en#instructor-and-outlines--the-two-pillars-of-structured-output)Instructor and Outlines — the two pillars of structured output
The fact that LLMs don't always emit clean JSON has been known since 2023. By 2026 two solutions are standard.
  * **Instructor** (jxnl/instructor): pass a Pydantic model as the function signature and the LLM answers in that shape. Retry and validation are first-class. Same API across OpenAI/Anthropic/Mistral/Gemini.
  * **Outlines** : token-level constrained decoding via regex, JSON Schema, or grammars. Guarantees 100% schema adherence on local models (vLLM, Transformers).



```
import instructor
from anthropic import Anthropic
from pydantic import BaseModel

class Ticket(BaseModel):
    title: str
    severity: str
    components: list[str]

client = instructor.from_anthropic(Anthropic())
ticket = client.messages.create(
    model="claude-opus-4-5-20250929",
    response_model=Ticket,
    max_tokens=1024,
    messages=[{"role": "user", "content": "Login broken on iOS Safari only, P0."}],
)
print(ticket.severity, ticket.components)

```

Instructor centers on cloud APIs and Outlines centers on local inference, so the territories are clearly split. Reviewers say both are lighter and easier to debug than `Marvin` or `Guardrails AI`.
##  [](https://www.youngju.dev/blog/culture/2026-05-16-ai-agent-frameworks-langchain-langgraph-llamaindex-crewai-autogen-pydanticai-mastra-dspy-mcp-2026-deep-dive.en#openai-agents-sdk-vercel-ai-sdk-4-anthropic-sdk--vendor-sdks-evolve)OpenAI Agents SDK, Vercel AI SDK 4, Anthropic SDK — vendor SDKs evolve
Vendor SDKs are no longer mere "LLM call wrappers."
  * **OpenAI Agents SDK** (officially released late 2024): `Agent`, `Runner`, `handoffs`, `guardrails` are first-class concepts. The official successor to the 2024 experimental Swarm.
  * **Vercel AI SDK 4** : `streamText`, `generateObject`, `tool` helpers wire React Server Component streaming and tool calls into a few lines.
  * **Anthropic Python/TS SDK** : tool calls via `tools` and `tool_choice` params on `messages.create`, plus a `computer_use` tool type.



```
import { streamText, tool } from "ai";
import { anthropic } from "@ai-sdk/anthropic";
import { z } from "zod";

const result = streamText({
  model: anthropic("claude-opus-4-5-20250929"),
  prompt: "Summarize today's PR list.",
  tools: {
    listPRs: tool({
      description: "List open PRs",
      parameters: z.object({ repo: z.string() }),
      execute: async ({ repo }) => ({ prs: [] }),
    }),
  },
  maxSteps: 5,
});

for await (const chunk of result.textStream) process.stdout.write(chunk);

```

Add Bedrock Agents (AWS), Google Gemini Function Calling, and Cloudflare AI Agents and you have **every major cloud vendor shipping a first-class agent SDK in 2026**.
##  [](https://www.youngju.dev/blog/culture/2026-05-16-ai-agent-frameworks-langchain-langgraph-llamaindex-crewai-autogen-pydanticai-mastra-dspy-mcp-2026-deep-dive.en#mcp--anthropics-tool-standard-de-facto-in-2026)MCP — Anthropic's tool standard, de-facto in 2026
The Model Context Protocol (MCP) is a **JSON-RPC tool/resource protocol** that Anthropic announced in late 2024. In a year and a half, LangChain, LlamaIndex, OpenAI Agents, Vercel AI SDK, and Mastra have all added first-class MCP client support. As of May 2026, the official registry lists more than 800 MCP servers.

```
from mcp.server import Server
from mcp.server.stdio import stdio_server

app = Server("calendar-server")

@app.list_tools()
async def list_tools():
    return [{
        "name": "create_event",
        "description": "Create a calendar event",
        "inputSchema": {"type": "object", "properties": {"title": {"type": "string"}}},
    }]

@app.call_tool()
async def call_tool(name, arguments):
    if name == "create_event":
        return [{"type": "text", "text": f"created: {arguments['title']}"}]

async with stdio_server() as (r, w):
    await app.run(r, w, app.create_initialization_options())

```

MCP's core insight is the separation: **"tools are servers, agents are clients."** Once Slack, GitHub, Notion, Postgres, and Stripe ship official MCP servers, every agent framework draws from the same tool pool. Lock-in breaks.
##  [](https://www.youngju.dev/blog/culture/2026-05-16-ai-agent-frameworks-langchain-langgraph-llamaindex-crewai-autogen-pydanticai-mastra-dspy-mcp-2026-deep-dive.en#a2a--googles-agent-to-agent-protocol)A2A — Google's Agent-to-Agent protocol
A2A (Agent2Agent) is the agent-to-agent collaboration standard Google announced in early 2025. If MCP is "between agent and tool," A2A standardizes the message format, capability advertisement, and task handoff "between agent and agent."
Adoption today is slower than MCP, but SaaS vendors like Salesforce, ServiceNow, and Atlassian are betting on A2A to build multi-agent meshes. As of May 2026, LangChain and Vertex AI Agents ship A2A adapters.

```
{
  "name": "research-agent",
  "version": "1.0.0",
  "capabilities": [
    { "name": "web.search", "description": "Search the web" },
    { "name": "doc.summarize", "description": "Summarize a document" }
  ],
  "endpoints": { "rpc": "https://agent.example.com/a2a" }
}

```

The above is an example A2A capability card. Other agents read it to decide which tasks to delegate.
##  [](https://www.youngju.dev/blog/culture/2026-05-16-ai-agent-frameworks-langchain-langgraph-llamaindex-crewai-autogen-pydanticai-mastra-dspy-mcp-2026-deep-dive.en#tool-call-standards--openai-function-calling-anthropic-tool-use-json-schema)Tool-call standards — OpenAI function calling, Anthropic tool use, JSON Schema
Vendor tool-call formats still differ in subtle ways. As of 2026 the key standards are:
  * **OpenAI Chat Completions function calling** : register JSON Schema in the `tools` array; receive results in `tool_calls`.
  * **Anthropic tool use** : `tools` array plus `tool_use` content blocks. `input_schema` is JSON Schema-compatible.
  * **Google Gemini Function Calling** : register via `FunctionDeclaration` objects. The schema is an OpenAPI 3.0 subset.
  * **MCP** : `inputSchema` is JSON Schema. Convertible into all the above.


Frameworks like LangChain, LlamaIndex, PydanticAI, and Mastra absorb the differences via adapters. You only need to track them when using SDKs directly.
##  [](https://www.youngju.dev/blog/culture/2026-05-16-ai-agent-frameworks-langchain-langgraph-llamaindex-crewai-autogen-pydanticai-mastra-dspy-mcp-2026-deep-dive.en#guidance-baml-griptape-agency-swarm--strong-players-in-specialized-niches)guidance, BAML, griptape, Agency Swarm — strong players in specialized niches
  * **guidance** (Microsoft): expresses token-level constrained decoding like code. More precise than JSON Schema but has a learning curve.
  * **BAML** (Boundary ML): declares prompts and functions in a separate **.baml file** and auto-generates TypeScript/Python code. The "prompt-as-code" version-controlled pattern.
  * **griptape** : enterprise RAG/agent. Abstractions like Drivers, Memory, and Rulesets are crisp; security and governance metadata are first-class.
  * **Agency Swarm** (VRSEN): puts multi-agent communication on top of the OpenAI Assistants API. Great for fast in-house automation PoCs.


##  [](https://www.youngju.dev/blog/culture/2026-05-16-ai-agent-frameworks-langchain-langgraph-llamaindex-crewai-autogen-pydanticai-mastra-dspy-mcp-2026-deep-dive.en#agent-evaluation--langsmith-phoenix-langfuse-galileo-patronus-deepeval)Agent evaluation — LangSmith, Phoenix, Langfuse, Galileo, Patronus, DeepEval
For agents, the "run trace" is the debugging unit. By 2026 the market splits into 5 groups.
  1. **LangSmith** (LangChain Inc.): the standard in the LangChain camp. Trace, dataset, evaluator, and online eval are all first-class.
  2. **Arize AI Phoenix** : open-source, OpenTelemetry-based. Easy to self-host, and the OpenInference spec covers every framework.
  3. **Langfuse** : open-source plus cloud. Simple self-hosting and friendlier pricing than LangSmith make it the startup favorite.
  4. **Galileo** , **Patronus AI** , **Confident AI DeepEval** : eval-centric (metrics, hallucination detection, regression). Great for CI/CD.
  5. **Weights & Biases Weave**: a trace view that feels familiar to existing W&B users.



```
import phoenix as px
from openinference.instrumentation.langchain import LangChainInstrumentor

px.launch_app()
LangChainInstrumentor().instrument()

result = chain.invoke({"diff": "..."})

```

Phoenix's strength is alignment with **OpenTelemetry GenAI semconv 1.0**. In late 2025 the OTel SIG stabilized the GenAI semantic conventions, dramatically improving trace compatibility.
##  [](https://www.youngju.dev/blog/culture/2026-05-16-ai-agent-frameworks-langchain-langgraph-llamaindex-crewai-autogen-pydanticai-mastra-dspy-mcp-2026-deep-dive.en#agent-memory--mem0-zep-pinecone-qdrant-redis)Agent memory — Mem0, Zep, Pinecone, Qdrant, Redis
Long-term memory is the fastest-maturing layer in 2026. Four patterns are standard.
  * **Mem0** : a "per-user memory layer" as a first-class API. Automates fact extraction and retrieval.
  * **Zep** : session memory plus a knowledge graph. Auto-indexes conversation history into an entity graph.
  * **Pinecone/Qdrant/Weaviate/Milvus** : vector stores for episodic memory.
  * **Redis + Postgres pgvector** : short-term cache plus persistent state.


LangGraph wraps all of the above behind its own `Memory` abstraction. PydanticAI also added first-class `Memory` support in late 2025.
##  [](https://www.youngju.dev/blog/culture/2026-05-16-ai-agent-frameworks-langchain-langgraph-llamaindex-crewai-autogen-pydanticai-mastra-dspy-mcp-2026-deep-dive.en#guardrails--guardrails-ai-nemo-guardrails-lakera-guard)Guardrails — Guardrails AI, NeMo Guardrails, Lakera Guard
Production agents must block jailbreaks, PII leakage, and policy violations. Three libraries are standard.
  * **Guardrails AI** : input/output validation via the `RAIL` spec. Both Python and JS supported.
  * **NVIDIA NeMo Guardrails** : declare conversation-flow rules in the Colang DSL. Can also restrict tool calls.
  * **Lakera Guard** : commercial API. Most reviewers rank it highest for prompt-injection detection accuracy.



```
rails:
  input:
    flows:
      - self check input
  output:
    flows:
      - self check output
      - check policy

```

The above is a snippet of NeMo Guardrails' `config.yml`. Separate input/output flows enforce policy.
##  [](https://www.youngju.dev/blog/culture/2026-05-16-ai-agent-frameworks-langchain-langgraph-llamaindex-crewai-autogen-pydanticai-mastra-dspy-mcp-2026-deep-dive.en#framework-comparison--at-a-glance)Framework comparison — at a glance  
| Framework  | Language  | Multi-agent  | Structured output  | Observability  | Notes  |  
| --- | --- | --- | --- | --- | --- |  
| LangChain + LangGraph  | Python/TS  | Graph  | with_structured_output  | LangSmith  | Largest ecosystem  |  
| LlamaIndex  | Python/TS  | Workflow  | Pydantic  | LangSmith, Phoenix  | RAG-first  |  
| CrewAI  | Python  | Role-based  | Pydantic  | LangSmith, own  | Non-dev friendly  |  
| AutoGen  | Python  | GroupChat  | Pydantic  | OTel  | Microsoft camp  |  
| PydanticAI  | Python  | Handoffs  | Pydantic, first-class  | Logfire, OTel  | Type-safe  |  
| Mastra  | TypeScript  | Workflow  | Zod  | OTel  | TS-camp standard  |  
| DSPy  | Python  | Modules  | Signatures  | MLflow  | Compiler paradigm  |  
| OpenAI Agents SDK  | Python/TS  | handoffs  | Pydantic/Zod  | OpenAI Traces  | Vendor SDK  |  
| Vercel AI SDK  | TypeScript  | maxSteps  | Zod  | Vercel Observability  | Next.js native  |  
##  [](https://www.youngju.dev/blog/culture/2026-05-16-ai-agent-frameworks-langchain-langgraph-llamaindex-crewai-autogen-pydanticai-mastra-dspy-mcp-2026-deep-dive.en#choice-guide--what-to-pick-in-may-2026)Choice guide — what to pick in May 2026
The big rules are simple.
  1. **Already lots of LangChain code** : migrate incrementally to LangGraph. Write new code in LangGraph; leave existing LCEL alone.
  2. **Type safety and enterprise governance matter** : PydanticAI. You inherit the entire Pydantic ecosystem.
  3. **TypeScript full-stack (Next.js, Cloudflare Workers)** : Mastra or Vercel AI SDK 4. RSC integration is natural.
  4. **RAG is the main act and you need GraphRAG** : LlamaIndex.
  5. **Fast PoC for multi-role collaboration** : CrewAI.
  6. **Research labs, paper reproduction, auto-tuned benchmarks** : DSPy.
  7. **Local models (vLLM) and 100% schema adherence** : Outlines.
  8. **Single-vendor lock-in is acceptable (OpenAI/Anthropic)** : OpenAI Agents SDK or the Anthropic SDK directly.


Whichever you pick, we recommend **exposing tools as MCP servers**. That keeps future framework swaps cheap.
##  [](https://www.youngju.dev/blog/culture/2026-05-16-ai-agent-frameworks-langchain-langgraph-llamaindex-crewai-autogen-pydanticai-mastra-dspy-mcp-2026-deep-dive.en#cost-management--token-accounting-and-caching)Cost management — token accounting and caching
In production, LLM tokens are cost. Three things are standard in 2026.
  * **Prompt caching** : Anthropic's `cache_control`, OpenAI prompt caching, and Gemini context caching all use a 5-minute TTL. Pulling system prompts and tool definitions into cache blocks cuts cost by 75% or more.
  * **Batch APIs** : time-insensitive workloads on OpenAI/Anthropic batch APIs get a 50% discount.
  * **Model cascades** : try Haiku/Mini first, escalate failures to Opus/4. Implement via LangChain `with_fallbacks` or PydanticAI's `models` list.


LangSmith, Helicone, and OpenLLMetry all aggregate token cost at the trace level. Pick one of these before you build a custom dashboard.
##  [](https://www.youngju.dev/blog/culture/2026-05-16-ai-agent-frameworks-langchain-langgraph-llamaindex-crewai-autogen-pydanticai-mastra-dspy-mcp-2026-deep-dive.en#anti-patterns--six-months-later-youll-regret-these)Anti-patterns — six months later you'll regret these
  1. **Using "all of" LangChain** : pulling every `langchain-community` integration leads to dependency explosion and a security audit nightmare. Import only what you need.
  2. **Allowing unbounded agent loops** : always set `max_iterations` and `max_steps`. The #1 cause of cost blow-ups.
  3. **Multi-turn agents without memory** : without Mem0/Zep, shoving the full history into the LLM each turn grows tokens not linearly but quadratically.
  4. **Shipping to production without eval** : build at least 50 golden cases in a LangSmith/Phoenix dataset and run them as regression tests.
  5. **Tool lock-in without MCP** : exposing tools only via LangChain's `@tool` decorator forces a rewrite on framework change. Pulling them into an MCP server keeps you free.
  6. **Bolting on guardrails right before launch** : include jailbreak scenarios and PII leakage as test cases from day one.


##  [](https://www.youngju.dev/blog/culture/2026-05-16-ai-agent-frameworks-langchain-langgraph-llamaindex-crewai-autogen-pydanticai-mastra-dspy-mcp-2026-deep-dive.en#closing--outlook-for-late-2026)Closing — outlook for late 2026
In the second half of 2026 expect three things.
  * **Full MCP standardization** : ISO/IETF-level formal-standard discussions begin. Cross-cloud tool compatibility is guaranteed.
  * **Enterprise standardization on type-safe agents** : PydanticAI and Mastra take share from LangChain rapidly, especially in finance, healthcare, and public sector.
  * **The agent OS emerges** : Letta (MemGPT) style "agent operating system" abstractions merge with LangGraph, making background, long-running, and human-review first-class.


If you're starting today, the default we recommend is LangGraph + PydanticAI + MCP + LangSmith (or Phoenix). If TypeScript is your main, go Mastra + Vercel AI SDK + OTel. Both combos hold up well a year later.
##  [](https://www.youngju.dev/blog/culture/2026-05-16-ai-agent-frameworks-langchain-langgraph-llamaindex-crewai-autogen-pydanticai-mastra-dspy-mcp-2026-deep-dive.en#references)References
  * LangChain docs: docs.langchain.com
  * LangGraph docs: langchain-ai.github.io/langgraph
  * LlamaIndex docs: docs.llamaindex.ai
  * CrewAI docs: docs.crewai.com
  * AutoGen site: microsoft.github.io/autogen
  * PydanticAI site: ai.pydantic.dev
  * Mastra site: mastra.ai
  * agno docs: docs.agno.com
  * smolagents docs: huggingface.co/docs/smolagents
  * DSPy site: dspy.ai
  * Instructor: github.com/jxnl/instructor
  * Outlines: github.com/outlines-dev/outlines
  * Model Context Protocol: modelcontextprotocol.io
  * OpenAI Agents SDK: openai.github.io/openai-agents-python
  * Anthropic docs: docs.anthropic.com
  * Vercel AI SDK: sdk.vercel.ai
  * LangSmith: smith.langchain.com
  * Arize Phoenix: phoenix.arize.com
  * Langfuse: langfuse.com
  * Galileo: galileo.ai
  * Patronus AI: patronus.ai
  * Confident AI DeepEval: confident-ai.com
  * Weights & Biases Weave: wandb.ai/site/weave
  * Mem0: mem0.ai
  * Zep: getzep.com
  * Guardrails AI: guardrailsai.com
  * NeMo Guardrails: github.com/NVIDIA/NeMo-Guardrails
  * Lakera Guard: lakera.ai
  * OpenTelemetry GenAI semconv: opentelemetry.io/docs/specs/semconv/gen-ai
  * A2A protocol: google.github.io/A2A


[Discuss on Twitter](https://mobile.twitter.com/search?q=https%3A%2F%2Fwww.youngju.dev%2Fblog%2Fculture%2F2026-05-16-ai-agent-frameworks-langchain-langgraph-llamaindex-crewai-autogen-pydanticai-mastra-dspy-mcp-2026-deep-dive.en) • [View on GitHub](https://github.com/fjvbn2003/yj-next-blog2/blob/main/data/blog/culture/2026-05-16-ai-agent-frameworks-langchain-langgraph-llamaindex-crewai-autogen-pydanticai-mastra-dspy-mcp-2026-deep-dive.en.mdx)
Load Comments
## Tags
[ai-agent](https://www.youngju.dev/tags/ai-agent)[langchain](https://www.youngju.dev/tags/langchain)[langgraph](https://www.youngju.dev/tags/langgraph)[llamaindex](https://www.youngju.dev/tags/llamaindex)[crewai](https://www.youngju.dev/tags/crewai)[autogen](https://www.youngju.dev/tags/autogen)[pydantic-ai](https://www.youngju.dev/tags/pydantic-ai)[mastra](https://www.youngju.dev/tags/mastra)[dspy](https://www.youngju.dev/tags/dspy)[mcp](https://www.youngju.dev/tags/mcp)[a2a](https://www.youngju.dev/tags/a2a)[agent-eval](https://www.youngju.dev/tags/agent-eval)[instructor](https://www.youngju.dev/tags/instructor)[guardrails](https://www.youngju.dev/tags/guardrails)
## Related Articles
  * ### [AI 에이전트 프레임워크 2026 심층 분석 - LangChain · LangGraph · LlamaIndex · CrewAI · AutoGen · PydanticAI · Mastra · DSPy · MCP 완벽 가이드 2026년 5월 16일](https://www.youngju.dev/blog/culture/2026-05-16-ai-agent-frameworks-langchain-langgraph-llamaindex-crewai-autogen-pydanticai-mastra-dspy-mcp-2026-deep-dive)
  * ### [AI 에이전트 프레임워크 2026 — LangGraph / AutoGen / CrewAI / OpenAI Agents SDK / Anthropic Agent SDK 비교 심층 가이드 2026년 5월 15일](https://www.youngju.dev/blog/culture/2026-05-15-ai-agent-frameworks-2026-langgraph-autogen-crewai-openai-agents-sdk-anthropic-claude-code-deep-dive)
  * ### [AI Agent Engineer 커리어 가이드: 2025년 가장 뜨거운 AI 직군의 모든 것 2026년 3월 23일](https://www.youngju.dev/blog/culture/2026-03-23-ai-agent-engineer-career-guide-2025)


## Previous Article
[AI 에이전트 & LLM 벤치마크 2026 — SWE-bench Verified / ARC-AGI 2 / GAIA / MMLU-Pro / GPQA / LiveCodeBench / Chatbot Arena 심층 가이드](https://www.youngju.dev/blog/culture/2026-05-16-ai-agent-llm-benchmarks-2026-swe-bench-verified-arc-agi-2-gaia-mmlu-pro-gpqa-livecodebench-chatbot-arena-deep-dive)
## Next Article
[AI 에이전트 프레임워크 2026 완벽 가이드 - LangGraph · AutoGen · CrewAI · Semantic Kernel · OpenAI Agents SDK · Claude Agent SDK · Pydantic AI 심층 분석](https://www.youngju.dev/blog/culture/2026-05-16-ai-agent-frameworks-2026-langgraph-autogen-crewai-semantic-kernel-openai-agents-claude-sdk-pydantic-ai-deep-dive)
[← Back to the blog](https://www.youngju.dev/blog)
mailMail[githubGitHub](https://github.com/fjvbn2003)[facebookFacebook](https://www.facebook.com/profile.php?id=100010923780547)[youtubeYoutube](https://youtube.com/channel/UC1VM2Zl33X70KJsDLixv_SQ)[linkedinLinkedin](https://www.linkedin.com/in/%EC%98%81%EC%A3%BC-%EA%B9%80-2303b8214/?originalSubdomain=kr)[twitterTwitter](https://twitter.com/fjvbn20031)
Youngju Kim
• 
© 2026
• 
[Chaos and Order](https://www.youngju.dev/)
[Tailwind Nextjs Theme](https://github.com/timlrx/tailwind-nextjs-starter-blog)
[Home](https://www.youngju.dev/)[Blog](https://www.youngju.dev/blog)[Tags](https://www.youngju.dev/tags)[Projects](https://www.youngju.dev/projects)[Tools](https://www.youngju.dev/tools)[Explore](https://www.youngju.dev/explore)[About](https://www.youngju.dev/about)

