Limited OfferMCP Mastery — up to 95% off17JUN26[Get Course](https://kgptalkie.com/mcp)
[![](https://kgptalkie.com/_next/image?url=%2Flogo%2Fkgp-symbol-light.png&w=96&q=75)![](https://kgptalkie.com/_next/image?url=%2Flogo%2Fkgp-symbol-dark.png&w=96&q=75)KGP Talkie](https://kgptalkie.com/)
[Learning Paths](https://kgptalkie.com/learning-paths)
[Tutorials](https://kgptalkie.com/tutorials)
[Udemy Courses](https://kgptalkie.com/udemy-courses)[Book Me](https://kgptalkie.com/book-me)[About Me](https://kgptalkie.com/about)
Search...`Ctrl K`[English](https://www.youtube.com/@kgptalkie "Subscribe to KGP Talkie \(English\) on YouTube")[हिंदी](https://www.youtube.com/@kgptalkie-hindi "Subscribe to KGP Talkie \(Hindi\) on YouTube")
[Tutorials](https://kgptalkie.com/tutorials)/[Generative AI](https://kgptalkie.com/tutorials/generative-ai)/Reflexion Agentic RAG: Self-Improving Answers
# Reflexion Agentic RAG: Self-Improving Answers
Build a Reflexion agent in LangGraph that drafts an answer, reflects on missing information, retrieves to fill gaps, and revises iteratively until complete.
[Laxmi Kant Tiwari](https://kgptalkie.com/about)Jun 17, 20268 min read[Follow](https://www.youtube.com/@kgptalkie "Follow KGP Talkie on YouTube")
![Reflexion Agentic RAG: Self-Improving Answers](https://kgptalkie.com/_next/image?url=%2Fimages%2Fthumbs%2Freflexion-agentic-rag.jpg&w=3840&q=75)
Topics You Will Master
Modeling an answer, its self-critique, and follow-up queries in one Pydantic schema
Drafting an initial answer that names its own information gaps
Retrieving documents for each gap-filling search query
Revising the answer and deciding when it is complete
**Reflexion** ([Shinn et al., 2023](https://arxiv.org/abs/2303.11366)) makes an agent **self-improve through iteration**. It drafts an answer, identifies what is missing, retrieves to fill those gaps, then revises — repeating until the answer is complete or a maximum number of iterations is reached. Where [CRAG](https://kgptalkie.com/tutorials/generative-ai/corrective-rag-crag) does a single correction, Reflexion runs a true feedback loop.
This lesson uses `gpt-oss` and builds on the [`retrieve_docs` tool](https://kgptalkie.com/tutorials/generative-ai/rag-retrieval-and-reranking) from earlier in the series.
**Prerequisites:** The `scripts/my_tools.py` tools from [RAG Data Retrieval and Re-Ranking](https://kgptalkie.com/tutorials/generative-ai/rag-retrieval-and-reranking). [Ollama](https://ollama.com/) running with `gpt-oss`, plus the packages below.
BASH Copy

```
pip install -U langgraph langchain-ollama langchain-core pydantic
ollama pull gpt-oss
```

Note
`gpt-oss` is OpenAI's open-weight model, distributed under the Apache 2.0 license. You can swap in `qwen3` by changing `LLM_MODEL` if you prefer.
95% OFF
#### Private Agentic RAG with LangGraph and Ollama
Step-by-step guide to building private, self-correcting RAG systems with LangGraph, ChromaDB, and local models like Qwen3 and gpt-oss.
[Enroll Now — 95% OFF →](https://kgptalkie.com/agentic-rag)
* * *
##  [](https://kgptalkie.com/tutorials/generative-ai/reflexion-agentic-rag#schemas-and-state)Schemas and State
![The unified Answer schema bundling the answer, reflection, follow-up queries, and a completion flag](https://kgptalkie.com/images/reflexion-agentic-rag-2.jpg)
The `Answer` schema bundles the answer, a critical reflection, follow-up search queries, and a completion flag — so a single structured call produces everything the loop needs.
PYTHON Copy

```
from typing import List
from langgraph.graph import StateGraph, START, END
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from pydantic import BaseModel, Field
from typing_extensions import TypedDict, Annotated
import operator, os
from scripts import my_tools

BASE_URL = "http://localhost:11434"
LLM_MODEL = "gpt-oss"
MAX_ITERATIONS = 3
llm = ChatOllama(model=LLM_MODEL, base_url=BASE_URL)

class Reflection(BaseModel):
    """Critique of current answer"""
    missing: str = Field(description="What critical information is missing or incomplete")
    superfluous: str = Field(description="What information is unnecessary or redundant")

class Answer(BaseModel):
    """Answer with inline citation, reflection and search queries"""
    answer: str = Field(description="Detailed answer with inline citation [1], [2] with reference list at the end")
    reflection: Reflection = Field(description="Critical reflection on the answer")
    search_queries: List[str] = Field(default_factory=list, description="1-3 search queries if more information needed, empty if complete")
    is_complete: bool = Field(default=False, description="True if answer is complete and no more searches needed")

class AgentState(TypedDict):
    messages: Annotated[List, operator.add]
    iteration_count: int
    retrieved_docs: str
    search_queries: List[str]
    is_complete: bool
```

##  [](https://kgptalkie.com/tutorials/generative-ai/reflexion-agentic-rag#draft-node)Draft Node
![The draft node writing an answer and naming its own information gaps](https://kgptalkie.com/images/reflexion-agentic-rag-3.jpg)
The draft node produces an initial answer plus a self-critique and the queries needed to fill the gaps.
PYTHON Copy

```
def draft_node(state: AgentState):
    llm_structured = llm.with_structured_output(Answer)

    system_prompt = """You are an expert financial document researcher.

              TASK:
              1. Provide detailed answer (~250 words) to user's question
              2. Use Markdown formatting (headings, bullets, tables, bold)
              3. Reflect critically: identify missing and superfluous information
              4. Generate 1-3 specific search queries to retrieve missing information"""

    messages = [SystemMessage(system_prompt)] + state['messages']
    response = llm_structured.invoke(messages)

    text_response = f"""
                      **Answer**: {response.answer}\n\n
                      **Reflection** - Missing: {response.reflection.missing}\n\n
                      **Reflection** - Superfluous: {response.reflection.superfluous}\n\n
                      **Search Queries**: {','.join(response.search_queries)}"""

    print(f"[DRAFT] Generated answer with {len(response.search_queries)}")
    return {
        'messages': [AIMessage(text_response)],
        'iteration_count': 1,
        'search_queries': response.search_queries
    }
```

##  [](https://kgptalkie.com/tutorials/generative-ai/reflexion-agentic-rag#retrieve-node)Retrieve Node
The retrieve node runs every pending search query through the retrieval tool and combines the results.
PYTHON Copy

```
def retrieve_node(state: AgentState):
    search_queries = state.get('search_queries', [])
    if not search_queries:
        return {'retrieved_docs': 'No document is retrieved as there is no search query.'}

    all_retrieved_text = []
    for idx, query in enumerate(search_queries, 1):
        print(f"[RETRIEVE] {idx} Query: {query}")
        result = my_tools.retrieve_docs.invoke({'query': query, 'k': 3})
        all_retrieved_text.append(f"\n---- Query {idx}: {query}\n\nResult:\n{result}")

    combined_result = "\n\n".join(all_retrieved_text)
    os.makedirs('debug_logs', exist_ok=True)
    with open('debug_logs/reflexion_agentic_rag.md', 'w', encoding='utf-8') as f:
        f.write(combined_result)

    return {'retrieved_docs': combined_result}
```

##  [](https://kgptalkie.com/tutorials/generative-ai/reflexion-agentic-rag#revise-node)Revise Node
![The revise node updating the answer and looping until complete or the iteration cap](https://kgptalkie.com/images/reflexion-agentic-rag-4.jpg)
The revise node rewrites the answer using the new documents, decides whether it is complete, and emits more queries if not. A safety check forces completion if the model claims incompleteness but provides no new queries.
PYTHON Copy

```
def revise_node(state: AgentState):
    print(f"[REVISE] Revise - Iteration {state.get('iteration_count', 1)}")
    llm_structured = llm.with_structured_output(Answer)

    system_prompt = """You are an expert financial document researcher.

                TASK:
                1. Write DETAILED answer (~250-300 words) with MARKDOWN formatting
                2. Include inline citations [1], [2] and a reference list at the end
                3. Critically reflect on what's missing or superfluous
                4. Generate 2-3 SPECIFIC search queries if information is incomplete

                DECISION LOGIC - ask yourself:
                - Do I have complete quarterly breakdown? Segment-wise data? YoY comparisons?
                - Do I have all metrics and all companies requested?

                MANDATORY: If is_complete=false, you MUST provide 2-3 specific search_queries."""

    query_prompt = f"""
                    Retrieved document:
                    {state.get('retrieved_docs', 'No doc found.')}

                    Revise your answer using these documents. Output JSON only data.
                    """

    messages = [SystemMessage(system_prompt)] + state['messages'] + [HumanMessage(query_prompt)]
    response = llm_structured.invoke(messages)

    if not response.is_complete and not response.search_queries:
        print("[REVISE] WARNING - No queries but incomplete. Forcing completion.")
        response.is_complete = True

    print(f"[REVISE] Complete: {response.is_complete}")

    text_response = f"""
                      **Answer**: {response.answer}\n\n
                      **Reflection** - Missing: {response.reflection.missing}\n\n
                      **Status** {'Complete' if response.is_complete else 'Needs more information'}"""

    return {
        'messages': [AIMessage(text_response)],
        'iteration_count': state.get('iteration_count', 1) + 1,
        'search_queries': response.search_queries,
        'is_complete': response.is_complete
    }
```

##  [](https://kgptalkie.com/tutorials/generative-ai/reflexion-agentic-rag#router-and-graph)Router and Graph
![The Reflexion loop: draft, retrieve, and revise until the answer is complete](https://kgptalkie.com/images/reflexion-agentic-rag-1.jpg)
The router loops back to retrieval only while the answer is incomplete, there are queries left, and the iteration budget is not exhausted.
PYTHON Copy

```
def should_continue(state: AgentState):
    iteration_count = state.get('iteration_count', 0)
    is_complete = state.get('is_complete', False)
    search_queries = state.get('search_queries', [])

    if is_complete or not search_queries or iteration_count >= MAX_ITERATIONS:
        return END

    print(f"[ROUTER] Iteration {iteration_count} - continue to retrieve")
    return 'retrieve'
```

The graph is a cycle: `draft → retrieve → revise → (retrieve)* → END`.
PYTHON Copy

```
def create_reflexion_agent():
    builder = StateGraph(AgentState)

    builder.add_node('draft', draft_node)
    builder.add_node('retrieve', retrieve_node)
    builder.add_node('revise', revise_node)

    builder.add_edge(START, 'draft')
    builder.add_edge('draft', 'retrieve')
    builder.add_edge('retrieve', 'revise')
    builder.add_conditional_edges('revise', should_continue, ['retrieve', END])

    return builder.compile()

agent = create_reflexion_agent()
```

##  [](https://kgptalkie.com/tutorials/generative-ai/reflexion-agentic-rag#testing-reflexion)Testing Reflexion
A balance-sheet question drafts an answer, generates three gap-filling queries, retrieves, and revises:
PYTHON Copy

```
query = "what is amazon's balance sheet in 2023?"
result = agent.invoke({'messages': [HumanMessage(query)]})
```

OUTPUT

```
[DRAFT] Generated answer with 3
[RETRIEVE] Fetching documents
[RETRIEVE] 1 Query: Amazon 2023 balance sheet figures 10-K
[RETRIEVE] 2 Query: Amazon total assets liabilities equity 2023
[RETRIEVE] 3 Query: Amazon 2023 annual report financial statements
[REVISE] Revise - Iteration 1
[REVISE] Complete: True
[ROUTER] iteration count: 2
```

A comparison question fires several retrieval queries in one pass before converging on a complete answer:
PYTHON Copy

```
query = "Compare the Amazon's and Apple's revenue of 2024 Q1?"
result = agent.invoke({'messages': [HumanMessage(query)]})
```

OUTPUT

```
[DRAFT] Generated answer with 4
[RETRIEVE] 1 Query: Amazon Q1 2024 revenue $162.5B
[RETRIEVE] 2 Query: Apple fiscal Q1 2024 revenue $123.9B
[RETRIEVE] 3 Query: Amazon Q1 2024 earnings release
[RETRIEVE] 4 Query: Apple Q1 2024 earnings release
[REVISE] Revise - Iteration 1
[REVISE] Complete: True
```

The next lesson, [Self-RAG](https://kgptalkie.com/tutorials/generative-ai/self-rag), checks the _final_ answer for hallucination and usefulness rather than reflecting before retrieval.
* * *
##  [](https://kgptalkie.com/tutorials/generative-ai/reflexion-agentic-rag#what-you-built)What You Built
In this lesson you built a Reflexion agent:
  * **Unified`Answer` schema** — answer, reflection, follow-up queries, and a completion flag in one structured output
  * **Draft node** — produces an initial answer and names its own gaps
  * **Retrieve node** — fetches documents for each gap-filling query
  * **Revise node** — rewrites the answer and decides whether it is complete, with a force-complete safeguard
  * **Bounded loop** — `MAX_ITERATIONS = 3` and the `should_continue` router prevent runaway iteration


Reflexion turns a single-shot answer into a research process that keeps improving until nothing important is missing.
### Found this useful? Keep building with me.
New tutorials every week on YouTube — or go deeper with a full structured course.
[Subscribe on YouTube](https://www.youtube.com/@kgptalkie?sub_confirmation=1)[Browse Udemy Courses](https://kgptalkie.com/udemy-courses)[Join the Newsletter](https://kgptalkie.com/tutorials/generative-ai/reflexion-agentic-rag#footer)
[← Previous in Agentic RAG with LangGraphCorrective RAG (CRAG) with LangGraph and Ollama](https://kgptalkie.com/tutorials/generative-ai/corrective-rag-crag)[Next in Agentic RAG with LangGraph →Self-RAG: Grounded Answers with Quality Gates](https://kgptalkie.com/tutorials/generative-ai/self-rag)
Related Tutorials
### Latest recommendations you might like
[ ![Adaptive RAG: Routing Documents, SQL, and Web](https://kgptalkie.com/_next/image?url=%2Fimages%2Fthumbs%2Fadaptive-rag.jpg&w=3840&q=75)Generative AI Adaptive RAG: Routing Documents, SQL, and Web Build Adaptive RAG in LangGraph that routes each query to a vector store, a SQL employee database, or live web search — with SQLite short-term memory. Jun 17, 2026Read Tutorial ](https://kgptalkie.com/tutorials/generative-ai/adaptive-rag)[ ![Agentic PageRAG: A ReAct Agent with LangGraph](https://kgptalkie.com/_next/image?url=%2Fimages%2Fthumbs%2Fagentic-pagerag.jpg&w=3840&q=75)Generative AI Agentic PageRAG: A ReAct Agent with LangGraph Build a ReAct agent in LangGraph that wraps retrieval as a tool, decides when to call it, decomposes comparison questions, and answers SEC filings with citations. Jun 17, 2026Read Tutorial ](https://kgptalkie.com/tutorials/generative-ai/agentic-pagerag)[ ![Corrective RAG \(CRAG\) with LangGraph and Ollama](https://kgptalkie.com/_next/image?url=%2Fimages%2Fthumbs%2Fcorrective-rag-crag.jpg&w=3840&q=75)Generative AI Corrective RAG (CRAG) with LangGraph and Ollama Build a self-correcting CRAG workflow in LangGraph that grades retrieved documents, rewrites weak queries, and falls back to web search before answering. Jun 17, 2026Read Tutorial ](https://kgptalkie.com/tutorials/generative-ai/corrective-rag-crag)[ ![PageRAG Data Ingestion with Docling & ChromaDB](https://kgptalkie.com/_next/image?url=%2Fimages%2Fthumbs%2Fpagerag-data-ingestion.jpg&w=3840&q=75)Generative AI PageRAG Data Ingestion with Docling & ChromaDB Build a page-wise PDF ingestion pipeline with Docling — filename metadata, SHA-256 deduplication, and local nomic-embed-text embeddings stored in ChromaDB. Jun 17, 2026Read Tutorial ](https://kgptalkie.com/tutorials/generative-ai/pagerag-data-ingestion)
#### Find this tutorial useful?
Subscribe to our YouTube channels for more practical production walk-throughs.
[Watch in English](https://www.youtube.com/@kgptalkie)[Watch in Hindi](https://www.youtube.com/@kgptalkie-hindi)
### Discussion & Comments
### On This Page
[Schemas and State](https://kgptalkie.com/tutorials/generative-ai/reflexion-agentic-rag#schemas-and-state)[Draft Node](https://kgptalkie.com/tutorials/generative-ai/reflexion-agentic-rag#draft-node)[Retrieve Node](https://kgptalkie.com/tutorials/generative-ai/reflexion-agentic-rag#retrieve-node)[Revise Node](https://kgptalkie.com/tutorials/generative-ai/reflexion-agentic-rag#revise-node)[Router and Graph](https://kgptalkie.com/tutorials/generative-ai/reflexion-agentic-rag#router-and-graph)[Testing Reflexion](https://kgptalkie.com/tutorials/generative-ai/reflexion-agentic-rag#testing-reflexion)[What You Built](https://kgptalkie.com/tutorials/generative-ai/reflexion-agentic-rag#what-you-built)
![](https://kgptalkie.com/_next/image?url=%2Flogo%2Fkgp-symbol-dark.png&w=64&q=75)
KGP Talkie
Learn. Build. Talk AI.
Code-first technical education. Taking developers from algorithmic basics to custom multi-agent graph loops and data science environments.
[English](https://www.youtube.com/@kgptalkie "YouTube Channel \(English\)")[Hindi](https://www.youtube.com/@kgptalkie-hindi "YouTube Channel \(Hindi\)")[](https://github.com/laxmimerit)[](https://linkedin.com/in/laxmimerit)[](https://x.com/laxmimerit)
#### Topics
  * [Generative AI](https://kgptalkie.com/tutorials/generative-ai)
  * [Machine Learning](https://kgptalkie.com/tutorials/machine-learning-data-science)
  * [Deep Learning](https://kgptalkie.com/tutorials/deep-learning)
  * [Natural Language Processing](https://kgptalkie.com/tutorials/nlp)


#### Resources
  * [About Laxmi Kant Tiwari](https://kgptalkie.com/about)
  * [YouTube Channel (English)](https://www.youtube.com/@kgptalkie)
  * [YouTube Channel (Hindi)](https://www.youtube.com/@kgptalkie-hindi)
  * [Udemy Course Store](https://kgptalkie.com/udemy-courses)
  * [Git Repositories](https://github.com/laxmimerit)


#### Newsletter
Get code cheatsheets and newly published tutorial notebooks straight to your inbox.
Your name
Email addressJoin
© 2026 KGP Talkie. All rights reserved. Created by Laxmi Kant Tiwari.
[Privacy Policy](https://kgptalkie.com/privacy)[Terms of Service](https://kgptalkie.com/terms)

