[Skip to content](https://developers.llamaindex.ai/python/llamaagents/workflows/#_top)
[ ![](https://developers.llamaindex.ai/_astro/llamaindex-light.m3GU97oV.svg) ![](https://developers.llamaindex.ai/_astro/llamaindex-dark.B8ExLyh7.svg) Developer Documentation  ](https://developers.llamaindex.ai/)
  * [ LlamaParse ](https://developers.llamaindex.ai/llamaparse/)
  * [ LiteParse ](https://developers.llamaindex.ai/liteparse/)
  * [ LlamaAgents ](https://developers.llamaindex.ai/python/llamaagents/)
  * [ LlamaIndex Framework ](https://developers.llamaindex.ai/python/framework/)


LlamaAgents
[LlamaParseLlamaParse ](https://developers.llamaindex.ai/llamaparse/)[LiteParseLiteParse ](https://developers.llamaindex.ai/liteparse/)[LlamaAgentsLlamaAgents ](https://developers.llamaindex.ai/python/llamaagents/)[LlamaIndex FrameworkLlamaIndex Framework ](https://developers.llamaindex.ai/python/framework/)
Search ` `⌘``K` `
Auto
Light
Dark
[API Dashboard](https://cloud.llamaindex.ai/)
  * [LlamaParse](https://developers.llamaindex.ai/llamaparse/)
  * [LiteParse](https://developers.llamaindex.ai/liteparse/)
  * [LlamaAgents](https://developers.llamaindex.ai/python/llamaagents/)
  * [LlamaIndex Framework](https://developers.llamaindex.ai/python/framework/)
  * [Overview](https://developers.llamaindex.ai/python/llamaagents/overview/)
  * Agent Workflows
    * [Introduction](https://developers.llamaindex.ai/python/llamaagents/workflows/)
    * [Branches and loops](https://developers.llamaindex.ai/python/llamaagents/workflows/branches_and_loops/)
    * [Concurrent execution of workflows](https://developers.llamaindex.ai/python/llamaagents/workflows/concurrent_execution/)
    * [Writing async workflows](https://developers.llamaindex.ai/python/llamaagents/workflows/async_workflows/)
    * [Streaming events](https://developers.llamaindex.ai/python/llamaagents/workflows/streaming/)
    * [Managing State](https://developers.llamaindex.ai/python/llamaagents/workflows/managing_state/)
    * [Custom start and stop events](https://developers.llamaindex.ai/python/llamaagents/workflows/customizing_entry_exit_points/)
    * [Resource Objects](https://developers.llamaindex.ai/python/llamaagents/workflows/resources/)
    * [Workflows from unbound functions](https://developers.llamaindex.ai/python/llamaagents/workflows/unbound_functions/)
    * [Error handling](https://developers.llamaindex.ai/python/llamaagents/workflows/retry_steps/)
    * [Human in the Loop](https://developers.llamaindex.ai/python/llamaagents/workflows/human_in_the_loop/)
    * [Writing durable workflows](https://developers.llamaindex.ai/python/llamaagents/workflows/durable_workflows/)
    * [DBOS Durable Execution](https://developers.llamaindex.ai/python/llamaagents/workflows/dbos/)
    * [Drawing a Workflow](https://developers.llamaindex.ai/python/llamaagents/workflows/drawing/)
    * [Testing Workflows](https://developers.llamaindex.ai/python/llamaagents/workflows/testing/)
    * [Observability](https://developers.llamaindex.ai/python/llamaagents/workflows/observability/)
    * [Run Your Workflow as a Server](https://developers.llamaindex.ai/python/llamaagents/workflows/deployment/)
    * [Python Client](https://developers.llamaindex.ai/python/llamaagents/workflows/client/)
  * Cloud
    * [Agent Builder](https://developers.llamaindex.ai/python/llamaagents/cloud/builder/)
    * [Click-to-Deploy from LlamaCloud](https://developers.llamaindex.ai/python/llamaagents/cloud/click-to-deploy/)
    * [Agent Data](https://developers.llamaindex.ai/python/llamaagents/cloud/agent-data-overview/)
  * llamactl
    * [Getting Started](https://developers.llamaindex.ai/python/llamaagents/llamactl/getting-started/)
    * [Agent Templates](https://developers.llamaindex.ai/python/llamaagents/llamactl/agent-templates/)
    * [Serving your Workflows](https://developers.llamaindex.ai/python/llamaagents/llamactl/workflow-api/)
    * [Configuring a UI](https://developers.llamaindex.ai/python/llamaagents/llamactl/ui-build/)
    * [Workflow React Hooks](https://developers.llamaindex.ai/python/llamaagents/llamactl/ui-hooks/)
    * [Deployment Config Reference](https://developers.llamaindex.ai/python/llamaagents/llamactl/configuration-reference/)
    * [Continuous Deployment with GitHub Actions](https://developers.llamaindex.ai/python/llamaagents/llamactl/cd-with-github-actions/)
  * llamactl Reference
    * [init](https://developers.llamaindex.ai/python/llamaagents/llamactl-reference/commands-init/)
    * [serve](https://developers.llamaindex.ai/python/llamaagents/llamactl-reference/commands-serve/)
    * [deployments](https://developers.llamaindex.ai/python/llamaagents/llamactl-reference/commands-deployments/)
    * [auth](https://developers.llamaindex.ai/python/llamaagents/llamactl-reference/commands-auth/)
    * [environments](https://developers.llamaindex.ai/python/llamaagents/llamactl-reference/commands-environments/)
    * [pkg](https://developers.llamaindex.ai/python/llamaagents/llamactl-reference/commands-pkg/)
    * [projects](https://developers.llamaindex.ai/python/llamaagents/llamactl-reference/commands-projects/)
    * [organizations](https://developers.llamaindex.ai/python/llamaagents/llamactl-reference/commands-organizations/)
    * [config](https://developers.llamaindex.ai/python/llamaagents/llamactl-reference/commands-config/)
  * [Agent Workflows Reference 🔗](https://developers.llamaindex.ai/python/workflows-api-reference/)


Install MCP Server
[ MCP Docs ](https://developers.llamaindex.ai/python/shared/mcp/) Copy MCP URL  [ Install in Cursor ](cursor://anysphere.cursor-deeplink/mcp/install?name=llama-index-docs&config=eyJ1cmwiOiJodHRwczovL2RldmVsb3BlcnMubGxhbWFpbmRleC5haS9tY3AifQ==) Copy Claude Code command  Copy Codex config 
[ ](https://github.com/run-llama) [ ](https://discord.com/invite/eN6D2HQ4aX) [ ](https://x.com/llama_index)
LlamaAgents
Agent Workflows
[Introduction](https://developers.llamaindex.ai/python/llamaagents/workflows/)
Copy Markdown
Open in **Claude**
Open in **ChatGPT**
Open in **Cursor**
* * *
**Copy Markdown**
**View as Markdown**
# Introduction
## What is a workflow?
[Section titled “What is a workflow?”](https://developers.llamaindex.ai/python/llamaagents/workflows/#what-is-a-workflow)
A workflow is an event-driven, step-based way to control the execution flow of an application.
Your application is divided into sections called steps. A step receives an event, does some work, and returns another event. That returned event triggers the next step whose type annotation accepts it.
That is the whole model. A step can call an LLM, run retrieval, ask for human input, update shared state, or dispatch a batch of work. The event types describe the edges of the workflow, and regular Python describes the logic inside each edge.
## Why workflows?
[Section titled “Why workflows?”](https://developers.llamaindex.ai/python/llamaagents/workflows/#why-workflows)
As generative AI applications become more complex, it becomes harder to manage the flow of data and control the execution of the application. Workflows provide a way to manage this complexity by breaking the application into smaller, more manageable pieces.
Other frameworks and LlamaIndex itself have attempted to solve this problem previously with directed acyclic graphs (DAGs) but these have a number of limitations that workflows do not:
  * Logic like loops and branches needed to be encoded into the edges of graphs, which made them hard to read and understand.
  * Passing data between nodes in a DAG created complexity around optional and default values and which parameters should be passed.
  * DAGs did not feel natural to developers trying to develop complex, looping, branching AI applications.


The event-based pattern and plain Python approach of Workflows resolves these problems.
Branches are ordinary `if` statements that return different event types. Loops are steps that return an event handled by an earlier step. Concurrent work is a step that returns `list[Event]`, paired with another step that accepts `list[Event]`. When the flow needs to become dynamic, you can send events directly from the `Context`.
Note
The Workflows library can be installed standalone, via `pip install llama-index-workflows`. However, `llama-index-core` comes with an installation of Workflows included.
In order to maintain the `llama_index` API stable and avoid breaking changes, when installing `llama-index-core` or the `llama-index` umbrella package, Workflows can be accessed with the import path `llama_index.core.workflow`.
## Getting Started
[Section titled “Getting Started”](https://developers.llamaindex.ai/python/llamaagents/workflows/#getting-started)
Tip
Workflows make async a first-class citizen, and this page assumes you are running in an async environment. What this means for you is setting up your code for async properly. If you are already running in a server like FastAPI, or in a notebook, you can freely use await already!
If you are running your own Python scripts, it’s best practice to have a single async entry point.

```


async def main():




    w = MyWorkflow(...)




    result = await w.run(...)




    print(result)












if __name__ == "__main__":




    import asyncio








    asyncio.run(main())


```

Here is the smallest useful shape: generate something, pass it to another step, then stop with a result.

```


from workflows import Workflow, step




from workflows.events import (




    Event,




    StartEvent,




    StopEvent,



)






# `pip install llama-index-llms-openai` if you don't already have it



from llama_index.llms.openai import OpenAI












class JokeEvent(Event):




    joke: str












class JokeFlow(Workflow):




    llm = OpenAI(model="gpt-4.1")








    @step




    async def generate_joke(self, ev: StartEvent) -> JokeEvent:




        topic = ev.topic








        prompt = f"Write your best joke about {topic}."




        response = await self.llm.acomplete(prompt)




        return JokeEvent(joke=str(response))








    @step




    async def critique_joke(self, ev: JokeEvent) -> StopEvent:




        joke = ev.joke








        prompt = f"Give a thorough analysis and critique of the following joke: {joke}"




        response = await self.llm.acomplete(prompt)




        return StopEvent(result=str(response))












w = JokeFlow(timeout=60, verbose=False)




result = await w.run(topic="pirates")




print(str(result))


```

![joke](https://developers.llamaindex.ai/_astro/joke.UFkPwogx_16xIbl.png)
There are a few moving pieces here, so let’s go through them one at a time.
### Defining Workflow Events
[Section titled “Defining Workflow Events”](https://developers.llamaindex.ai/python/llamaagents/workflows/#defining-workflow-events)

```


class JokeEvent(Event):




    joke: str


```

Events are user-defined Pydantic objects. You control the attributes and any other auxiliary methods. In this case, our workflow relies on a single user-defined event, the `JokeEvent`.
### Setting up the Workflow Class
[Section titled “Setting up the Workflow Class”](https://developers.llamaindex.ai/python/llamaagents/workflows/#setting-up-the-workflow-class)

```


class JokeFlow(Workflow):




    llm = OpenAI(model="gpt-4.1")




    ...


```

Our workflow is implemented by subclassing the `Workflow` class. For simplicity, we attached a static `OpenAI` LLM instance.
### Workflow Entry Points
[Section titled “Workflow Entry Points”](https://developers.llamaindex.ai/python/llamaagents/workflows/#workflow-entry-points)

```


class JokeFlow(Workflow):




    ...








    @step




    async def generate_joke(self, ev: StartEvent) -> JokeEvent:




        topic = ev.topic








        prompt = f"Write your best joke about {topic}."




        response = await self.llm.acomplete(prompt)




        return JokeEvent(joke=str(response))








    ...


```

Here, we come to the entry-point of our workflow. While most events are user-defined, there are two special-case events, the `StartEvent` and the `StopEvent` that the framework provides out of the box. Here, the `StartEvent` signifies where to send the initial workflow input.
The `StartEvent` is a bit of a special object since it can hold arbitrary attributes. Here, we accessed the topic with `ev.topic`, which would raise an error if it wasn’t there. You could also do `ev.get("topic")` to handle the case where the attribute might not be there without raising an error.
For further type safety, you can also subclass the `StartEvent`.
At this point, you may have noticed that we haven’t explicitly told the workflow what events are handled by which steps. Instead, the `@step` decorator is used to infer the input and output types of each step. Furthermore, these inferred input and output types are also used to verify for you that the workflow is valid before running!
### Workflow Exit Points
[Section titled “Workflow Exit Points”](https://developers.llamaindex.ai/python/llamaagents/workflows/#workflow-exit-points)

```


class JokeFlow(Workflow):




    ...








    @step




    async def critique_joke(self, ev: JokeEvent) -> StopEvent:




        joke = ev.joke








        prompt = f"Give a thorough analysis and critique of the following joke: {joke}"




        response = await self.llm.acomplete(prompt)




        return StopEvent(result=str(response))








    ...


```

Here, we have our second, and last step, in the workflow. We know it’s the last step because the special `StopEvent` is returned. When the workflow encounters a returned `StopEvent`, it immediately stops the workflow and returns whatever we passed in the `result` parameter.
In this case, the result is a string, but it could be a dictionary, list, or any other object.
You can also subclass the `StopEvent` class for further type safety.
### Running the Workflow
[Section titled “Running the Workflow”](https://developers.llamaindex.ai/python/llamaagents/workflows/#running-the-workflow)

```


w = JokeFlow(timeout=60, verbose=False)




result = await w.run(topic="pirates")




print(str(result))


```

Lastly, we create and run the workflow. There are some settings like timeouts (in seconds) and verbosity to help with debugging.
The `.run()` method starts the workflow and returns a `WorkflowHandler`. The handler is awaitable, so `await w.run(...)` waits for the final result. If you need streamed events while the workflow is running, keep the handler:

```


handler = w.run(topic="pirates")




async for ev in handler.stream_events():




    ...




result = await handler


```

The keyword arguments passed to `run()` become fields of the special `StartEvent` that is automatically emitted to start the workflow. As we have seen, in this case `topic` is accessed from the step with `ev.topic`.
## How to choose the right workflow API
[Section titled “How to choose the right workflow API”](https://developers.llamaindex.ai/python/llamaagents/workflows/#how-to-choose-the-right-workflow-api)
Most workflow code should use typed step inputs and typed returns. That gives validation, diagrams, and readable code:

```

@step



async def retrieve(self, ev: StartEvent) -> Retrieved:




    ...







@step



async def synthesize(self, ev: Retrieved) -> StopEvent:




    ...


```

Use the other APIs when the shape of the work asks for them:  
| Use this  | When  |  
| --- | --- |  
| Return `A  | B`  |  
| Return `list[A]`  | A step has a finite batch and can produce all work items before downstream workers start.  |  
| Accept `list[A]`  | A step needs the full batch of results before continuing.  |  
| `ctx.send_event(...)`  | A step needs to emit events incrementally, emit an unknown number of events, or send an event from outside the workflow while it is running.  |  
| `ctx.collect_events(...)`  | You used `ctx.send_event` and need to manually wait for a known set of events.  |  
| `ctx.store`  | Steps need shared per-run state.  |  
| `Resource(...)`  | Steps need clients, indexes, models, config, or other dependencies that should not live in serialized state.  |  
The type-first APIs are easier to validate and visualize. The context APIs are more flexible, but they make you own more of the bookkeeping.
## Validation
[Section titled “Validation”](https://developers.llamaindex.ai/python/llamaagents/workflows/#validation)
Before a workflow runs, Workflows validates the event graph described by your step signatures. It checks that start and stop events are present, produced events have consumers, consumed events have producers, and the graph does not contain accidental dead ends.
Most validation failures are useful design feedback. They usually mean one of these is true:  
| Symptom  | Usual cause  |  
| --- | --- |  
| A step consumes an event that is never produced  | A return annotation is missing, or the event is only sent dynamically with `ctx.send_event`.  |  
| A step produces an event that nobody consumes  | The next step has the wrong event type, or the branch is unfinished.  |  
| The workflow has no terminal event  | No reachable step returns `StopEvent` or a custom `StopEvent` subclass.  |  
For intentionally dynamic workflows, keep as much as possible in the type annotations and use `ctx.send_event` for the timing. If a step is intentionally unreachable from static analysis, skip that specific check on the step:

```


@step(skip_graph_checks=["reachability"])




async def receive_webhook(self, ev: WebhookEvent) -> StopEvent:




    ...


```

You can also call `workflow.validate()` directly in tests or startup code. Resource config files are validated by default; resource factories are only resolved if you call `validate(validate_resources=True)`.
## Examples
[Section titled “Examples”](https://developers.llamaindex.ai/python/llamaagents/workflows/#examples)
To help you become more familiar with the workflow concept and its features, LlamaIndex documentation offers example notebooks that you can run for hands-on learning:
  * [Common Workflow Patterns](https://developers.llamaindex.ai/python/examples/workflow/workflows_cookbook/) walks you through common usage patterns like looping and state management using simple workflows. It’s usually a great place to start.
  * [RAG + Reranking](https://developers.llamaindex.ai/python/examples/workflow/rag/) shows how to implement a real-world use case with a fairly simple workflow that performs both ingestion and querying.
  * [Citation Query Engine](https://developers.llamaindex.ai/python/examples/workflow/citation_query_engine/) similar to RAG + Reranking, the notebook focuses on how to implement intermediate steps in between retrieval and generation. A good example of how to use the [`Context`](https://developers.llamaindex.ai/python/llamaagents/workflows/managing_state) object in a workflow.
  * [Corrective RAG](https://developers.llamaindex.ai/python/examples/workflow/corrective_rag_pack/) adds some more complexity on top of a RAG workflow, showcasing how to query a web search engine after an evaluation step.
  * [Utilizing Concurrency](https://developers.llamaindex.ai/python/examples/workflow/parallel_execution/) explains how to manage the parallel execution of steps in a workflow, something that’s important to know as your workflows grow in complexity.


RAG applications are easy to understand and offer a great opportunity to learn the basics of workflows. However, more complex agentic scenarios involving tool calling, memory, and routing are where workflows excel.
The examples below highlight some of these use-cases.
  * [ReAct Agent](https://developers.llamaindex.ai/python/examples/workflow/react_agent/) is obviously the perfect example to show how to implement tools in a workflow.
  * [Function Calling Agent](https://developers.llamaindex.ai/python/examples/workflow/function_calling_agent/) is a great example of how to use the LlamaIndex framework primitives in a workflow, keeping it small and tidy even in complex scenarios like function calling.
  * [CodeAct Agent](https://developers.llamaindex.ai/python/examples/agent/from_scratch_code_act_agent/) is a great example of how to create a CodeAct Agent from scratch.
  * [Human In The Loop: Story Crafting](https://developers.llamaindex.ai/python/examples/workflow/human_in_the_loop_story_crafting/) is a powerful example showing how workflow runs can be interactive and stateful. In this case, to collect input from a human.
  * [Reliable Structured Generation](https://developers.llamaindex.ai/python/examples/workflow/reflection/) shows how to implement loops in a workflow, in this case to improve structured output through reflection.
  * [Query Planning with Workflows](https://developers.llamaindex.ai/python/examples/workflow/planning_workflow/) is an example of a workflow that plans a query by breaking it down into smaller items, and executing those smaller items. It highlights how to stream events from a workflow, execute steps in parallel, and looping until a condition is met.
  * [Writing Durable Workflows](https://developers.llamaindex.ai/python/llamaagents/workflows/durable_workflows) shows how to checkpoint workflow context and resume a run after a restart.


Last but not least, a few more advanced use cases that demonstrate how workflows can be extremely handy if you need to quickly implement prototypes, for example from literature:
  * [Advanced Text-to-SQL](https://developers.llamaindex.ai/python/examples/workflow/advanced_text_to_sql/)
  * [JSON Query Engine](https://developers.llamaindex.ai/python/examples/workflow/jsonalyze_query_engine/)
  * [Long RAG](https://developers.llamaindex.ai/python/examples/workflow/long_rag_pack/)
  * [Multi-Step Query Engine](https://developers.llamaindex.ai/python/examples/workflow/multi_step_query_engine/)
  * [Multi-Strategy Workflow](https://developers.llamaindex.ai/python/examples/workflow/multi_strategy_workflow/)
  * [Router Query Engine](https://developers.llamaindex.ai/python/examples/workflow/router_query_engine/)
  * [Self Discover Workflow](https://developers.llamaindex.ai/python/examples/workflow/self_discover_workflow/)
  * [Sub-Question Query Engine](https://developers.llamaindex.ai/python/examples/workflow/sub_question_query_engine/)


Note for AI agents: this documentation is built for programmatic access. - Overview of all docs: https://developers.llamaindex.ai/llms.txt - Any page is available as raw Markdown by appending index.md to its URL — e.g. https://developers.llamaindex.ai/llamaparse/parse/getting_started/index.md - Agent-friendly REST search APIs live under https://developers.llamaindex.ai/api/ — search (BM25 full-text), grep (regex), read (fetch a page), and list (browse the doc tree). See https://developers.llamaindex.ai/llms.txt for parameters. - A hosted documentation MCP server is available at https://developers.llamaindex.ai/mcp. If you support MCP, you can ask the user to install it for browsing these docs directly (an alternative to the REST API). Setup: https://developers.llamaindex.ai/python/shared/mcp/
[ Previous
* * *
Overview ](https://developers.llamaindex.ai/python/llamaagents/overview/)[ Next
* * *
Branches and loops ](https://developers.llamaindex.ai/python/llamaagents/workflows/branches_and_loops/)
[ Powered by ](https://www.stainless.com/products/docs)
## On this page
  * [ Overview ](https://developers.llamaindex.ai/python/llamaagents/workflows/#_top)
  * [ What is a workflow? ](https://developers.llamaindex.ai/python/llamaagents/workflows/#what-is-a-workflow)
  * [ Why workflows? ](https://developers.llamaindex.ai/python/llamaagents/workflows/#why-workflows)
  * [ Getting Started ](https://developers.llamaindex.ai/python/llamaagents/workflows/#getting-started)
    * [ Defining Workflow Events ](https://developers.llamaindex.ai/python/llamaagents/workflows/#defining-workflow-events)
    * [ Setting up the Workflow Class ](https://developers.llamaindex.ai/python/llamaagents/workflows/#setting-up-the-workflow-class)
    * [ Workflow Entry Points ](https://developers.llamaindex.ai/python/llamaagents/workflows/#workflow-entry-points)
    * [ Workflow Exit Points ](https://developers.llamaindex.ai/python/llamaagents/workflows/#workflow-exit-points)
    * [ Running the Workflow ](https://developers.llamaindex.ai/python/llamaagents/workflows/#running-the-workflow)
  * [ How to choose the right workflow API ](https://developers.llamaindex.ai/python/llamaagents/workflows/#how-to-choose-the-right-workflow-api)
  * [ Validation ](https://developers.llamaindex.ai/python/llamaagents/workflows/#validation)
  * [ Examples ](https://developers.llamaindex.ai/python/llamaagents/workflows/#examples)


  * [ LlamaParse ](https://developers.llamaindex.ai/llamaparse/)
  * [ LiteParse ](https://developers.llamaindex.ai/liteparse/)
  * [ LlamaAgents ](https://developers.llamaindex.ai/python/llamaagents/)
  * [ LlamaIndex Framework ](https://developers.llamaindex.ai/python/framework/)



