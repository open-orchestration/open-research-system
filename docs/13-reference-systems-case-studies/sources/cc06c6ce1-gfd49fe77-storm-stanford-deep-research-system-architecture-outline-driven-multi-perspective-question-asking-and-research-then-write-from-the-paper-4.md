Index your code with Devin
[DeepWiki](https://deepwiki.com/)
[DeepWiki](https://deepwiki.com/)
[stanford-oval/storm ](https://github.com/stanford-oval/storm "Open repository")
Index your code with
Devin
Edit WikiShare
Last indexed: 19 November 2025 ([fb951a](https://github.com/stanford-oval/storm/commits/fb951af7))
  * [Overview](https://deepwiki.com/stanford-oval/storm/1-overview)
  * [Installation and Setup](https://deepwiki.com/stanford-oval/storm/1.1-installation-and-setup)
  * [System Architecture](https://deepwiki.com/stanford-oval/storm/1.2-system-architecture)
  * [STORM Wiki Generation System](https://deepwiki.com/stanford-oval/storm/2-storm-wiki-generation-system)
  * [STORMWikiRunner](https://deepwiki.com/stanford-oval/storm/2.1-stormwikirunner)
  * [Knowledge Curation Module](https://deepwiki.com/stanford-oval/storm/2.2-knowledge-curation-module)
  * [Outline and Article Generation Modules](https://deepwiki.com/stanford-oval/storm/2.3-outline-and-article-generation-modules)
  * [STORM Data Structures](https://deepwiki.com/stanford-oval/storm/2.4-storm-data-structures)
  * [Co-STORM Collaborative System](https://deepwiki.com/stanford-oval/storm/3-co-storm-collaborative-system)
  * [CoStormRunner](https://deepwiki.com/stanford-oval/storm/3.1-costormrunner)
  * [Knowledge Base System](https://deepwiki.com/stanford-oval/storm/3.2-knowledge-base-system)
  * [Agent System](https://deepwiki.com/stanford-oval/storm/3.3-agent-system)
  * [Collaborative Modules](https://deepwiki.com/stanford-oval/storm/3.4-collaborative-modules)
  * [Core Infrastructure](https://deepwiki.com/stanford-oval/storm/4-core-infrastructure)
  * [Language Model Integration](https://deepwiki.com/stanford-oval/storm/4.1-language-model-integration)
  * [Retrieval Modules](https://deepwiki.com/stanford-oval/storm/4.2-retrieval-modules)
  * [Encoder System](https://deepwiki.com/stanford-oval/storm/4.3-encoder-system)
  * [Utilities and Helpers](https://deepwiki.com/stanford-oval/storm/4.4-utilities-and-helpers)
  * [Abstract Interfaces](https://deepwiki.com/stanford-oval/storm/4.5-abstract-interfaces)
  * [Usage and Examples](https://deepwiki.com/stanford-oval/storm/5-usage-and-examples)
  * [STORM Examples](https://deepwiki.com/stanford-oval/storm/5.1-storm-examples)
  * [Co-STORM Examples](https://deepwiki.com/stanford-oval/storm/5.2-co-storm-examples)
  * [Streamlit Frontend Demo](https://deepwiki.com/stanford-oval/storm/5.3-streamlit-frontend-demo)
  * [Package and Development](https://deepwiki.com/stanford-oval/storm/6-package-and-development)


Menu
# Overview
Relevant source files
  * [.github/workflows/python-package.yml](https://github.com/stanford-oval/storm/blob/fb951af7/.github/workflows/python-package.yml)
  * [README.md](https://github.com/stanford-oval/storm/blob/fb951af7/README.md?plain=1)
  * [knowledge_storm/__init__.py](https://github.com/stanford-oval/storm/blob/fb951af7/knowledge_storm/__init__.py)
  * [knowledge_storm/lm.py](https://github.com/stanford-oval/storm/blob/fb951af7/knowledge_storm/lm.py)
  * [setup.py](https://github.com/stanford-oval/storm/blob/fb951af7/setup.py)


This document provides a comprehensive overview of the STORM (Synthesis of Topic Outlines through Retrieval and Multi-perspective question asking) repository. STORM is a language model-powered system that generates Wikipedia-like articles from scratch using Internet search. The repository contains two distinct operational modes: **STORM** for automated article generation and **Co-STORM** for human-AI collaborative knowledge curation.
For detailed installation instructions and quick start guides, see [Installation and Setup](https://deepwiki.com/stanford-oval/storm/1.1-installation-and-setup). For architecture details, see [System Architecture](https://deepwiki.com/stanford-oval/storm/1.2-system-architecture). For STORM-specific implementation, see [STORM Wiki Generation System](https://deepwiki.com/stanford-oval/storm/2-storm-wiki-generation-system). For Co-STORM implementation, see [Co-STORM Collaborative System](https://deepwiki.com/stanford-oval/storm/3-co-storm-collaborative-system).
## What is STORM?
STORM is a multi-stage language model system that automates the research and writing process for long-form articles with citations. The system addresses the challenge of generating comprehensive, well-structured content by breaking the problem into two fundamental stages:
  1. **Pre-writing stage** : Conducts Internet-based research to collect references and generates a hierarchical outline
  2. **Writing stage** : Uses the outline and references to generate full-length articles with proper citations


The core innovation is **perspective-guided question asking** : instead of directly prompting language models to ask questions, STORM discovers different perspectives by surveying existing articles on similar topics and uses these perspectives to guide the question-asking process. Questions are asked through **simulated conversations** between a Wikipedia writer and a topic expert, both powered by language models, grounded in Internet sources.
Sources: [README.md1-55](https://github.com/stanford-oval/storm/blob/fb951af7/README.md?plain=1#L1-L55)
## What is Co-STORM?
Co-STORM extends STORM with a **collaborative discourse protocol** that enables human participation in the knowledge curation process. The system implements three types of agents:
  * **Co-STORM LLM experts** : Generate answers grounded in external knowledge sources and raise follow-up questions
  * **Moderator** : Generates thought-provoking questions inspired by retrieved information not yet discussed
  * **Human user** : Can observe the discourse passively or actively engage by injecting utterances to steer the conversation


Co-STORM maintains a **dynamic mind map** (`KnowledgeBase`) that organizes collected information into a hierarchical concept structure. This shared conceptual space helps reduce cognitive load during long, in-depth conversations and enables the system to continuously reorganize information as the discourse progresses.
Sources: [README.md56-70](https://github.com/stanford-oval/storm/blob/fb951af7/README.md?plain=1#L56-L70)
## Core Package Structure
The STORM repository is distributed as the `knowledge-storm` package on PyPI (current version 1.1.1). The package exposes eight main modules:  
| Module  | Purpose  | Key Classes  |  
| --- | --- | --- |  
| `storm_wiki`  | STORM pipeline implementation  |  `STORMWikiRunner`, `STORMWikiRunnerArguments`  |  
| `collaborative_storm`  | Co-STORM implementation  |  `CoStormRunner`, `RunnerArgument`  |  
| `interface`  | Abstract base classes  |  `InformationTable`, `Article`, `Retriever`, `Module`, `Engine`, `Agent`  |  
| `lm`  | Language model wrappers  |  `LitellmModel` (supports 100+ LLM providers)  |  
| `rm`  | Retrieval module implementations  |  `YouRM`, `BingSearch`, `VectorRM`, etc. (11 total)  |  
| `encoder`  | Text embedding generation  | `Encoder`  |  
| `utils`  | Helper functions  |  `ArticleTextProcessing`, `FileIOHelper`, `WebPageHelper`  |  
| `dataclass`  | Core data structures  |  `Information`, `DialogueTurn`, `ConversationTurn`  |  
The package structure enables users to import only what they need while maintaining clear separation between abstract interfaces and concrete implementations.
Sources: [setup.py17-38](https://github.com/stanford-oval/storm/blob/fb951af7/setup.py#L17-L38) [knowledge_storm/__init__.py1-10](https://github.com/stanford-oval/storm/blob/fb951af7/knowledge_storm/__init__.py#L1-L10)
## System Architecture: Code Entity View
The following diagram maps the natural language system description to actual code entities:
This architecture shows how user-facing entry points (example scripts and frontend) instantiate runner classes, which in turn coordinate language models, retrieval modules, and data structures.
Sources: [README.md104-217](https://github.com/stanford-oval/storm/blob/fb951af7/README.md?plain=1#L104-L217) [knowledge_storm/__init__.py1-10](https://github.com/stanford-oval/storm/blob/fb951af7/knowledge_storm/__init__.py#L1-L10)
## STORM vs Co-STORM: Operational Paradigms
The repository implements two distinct operational paradigms that share infrastructure but differ fundamentally in execution:
### STORM: Linear 4-Stage Pipeline
The STORM pipeline executes deterministically through four discrete stages:
  1. **Knowledge Curation** : Simulates conversations between `ConvSimulator` (writer) and topic expert to collect information. Uses perspective-guided question asking to ensure breadth and depth.
  2. **Outline Generation** : Organizes collected information into a hierarchical structure using the `StormInformationTable`.
  3. **Article Generation** : Populates outline sections with content, section by section, using retrieved information.
  4. **Article Polishing** : Adds lead section and optionally removes duplicate content.


Each stage completes fully before the next begins. Results are stored in `StormArticle` with proper citation management.
### Co-STORM: Iterative Collaborative Loop
Co-STORM operates iteratively:
  1. **Warm Start** : `warm_start()` initializes experts and creates initial `KnowledgeBase` structure
  2. **Conversation Loop** : `step()` method repeatedly invokes agents based on turn policy
  3. **Dynamic Knowledge Organization** : `KnowledgeBase` continuously reorganizes via `InsertInformationModule` and `ExpandNodeModule`
  4. **Report Generation** : Final article synthesized from organized `KnowledgeBase`


The system uses `ConversationTurn` objects to track discourse history and supports both observation mode (user watches) and active mode (user participates).
Sources: [README.md40-70](https://github.com/stanford-oval/storm/blob/fb951af7/README.md?plain=1#L40-L70) [README.md104-217](https://github.com/stanford-oval/storm/blob/fb951af7/README.md?plain=1#L104-L217)
## Infrastructure Layer: Shared Components
Both STORM and Co-STORM rely on a common infrastructure layer that provides provider-agnostic access to external services:
### Language Model Integration
The `LitellmModel` class ([lm.py192-269](https://github.com/stanford-oval/storm/blob/fb951af7/lm.py#L192-L269)) wraps the `litellm` library to provide:
  * **Universal LLM access** : Supports 100+ providers through a single interface
  * **Two-tier caching** : LRU memory cache (3000 entries) plus disk cache to reduce API costs
  * **Thread-safe token tracking** : `prompt_tokens` and `completion_tokens` counters with lock protection
  * **Task-specific model assignment** : Different models can be assigned to different tasks (e.g., cheaper models for conversation, powerful models for generation)


The system configures multiple specialized language models per runner (5 for STORM, 6 for Co-STORM) to optimize cost-quality tradeoffs.
Sources: [knowledge_storm/lm.py1-269](https://github.com/stanford-oval/storm/blob/fb951af7/knowledge_storm/lm.py#L1-L269) [README.md92-101](https://github.com/stanford-oval/storm/blob/fb951af7/README.md?plain=1#L92-L101)
### Retrieval Module Layer
The repository provides 11 retrieval module implementations, all conforming to a unified interface:  
| Retrieval Module  | Type  | Key Features  |  
| --- | --- | --- |  
| `YouRM`  | Web Search  | You.com search API integration  |  
| `BingSearch`  | Web Search  | Bing Search API with configurable results  |  
| `BraveRM`  | Web Search  | Brave Search engine  |  
| `SerperRM`  | Web Search  | Serper.dev API wrapper  |  
| `DuckDuckGoSearchRM`  | Web Search  | DuckDuckGo search  |  
| `TavilySearchRM`  | Web Search  | Tavily search API  |  
| `SearXNG`  | Web Search  | SearXNG meta-search  |  
| `GoogleSearch`  | Web Search  | Google Custom Search API  |  
| `VectorRM`  | Vector Search  | Qdrant vector database for custom documents  |  
| `AzureAISearch`  | Specialized  | Azure Cognitive Search  |  
| `StanfordOvalArxivRM`  | Specialized  | ArXiv paper search  |  
All retrieval modules implement the `retrieve(query: str, exclude_urls: list)` method and return `Information` objects with URL, snippets, and titles. The `VectorRM` uses the `Encoder` class for semantic similarity matching against user-provided documents.
Sources: [README.md92-101](https://github.com/stanford-oval/storm/blob/fb951af7/README.md?plain=1#L92-L101) [knowledge_storm/rm.py1-50](https://github.com/stanford-oval/storm/blob/fb951af7/knowledge_storm/rm.py#L1-L50) (note: full rm.py likely extends beyond shown lines)
## Data Flow and Transformation
### STORM Data Pipeline
STORM transforms data through discrete stages:
  1. Topic → Search queries via perspective-guided question asking
  2. Queries → `Information` objects via retrieval module
  3. `Information` → `DialogueTurn` objects (Q&A pairs with citations)
  4. `DialogueTurn` → `StormInformationTable` (URL-indexed, supports semantic search)
  5. `StormInformationTable` → `StormArticle` (outline + sections + citations)


### Co-STORM Data Flow
Co-STORM maintains dynamic data structures:
  1. `ConversationTurn` objects capture each utterance with role and metadata
  2. `Information` objects assigned UUIDs for citation tracking
  3. `InsertInformationModule` maps information to appropriate `KnowledgeNode` in tree
  4. `KnowledgeBase` continuously reorganizes as new information arrives
  5. `ExpandNodeModule` creates child nodes when topics warrant deeper exploration
  6. Final report generated by traversing organized knowledge tree


Sources: [README.md1-70](https://github.com/stanford-oval/storm/blob/fb951af7/README.md?plain=1#L1-L70) Diagram 4 from high-level overview
## Multi-LLM System Design
Both STORM and Co-STORM implement a **multi-LLM system paradigm** where different tasks are assigned to different language model instances:
### STORM Task Assignment (5 LMs)  
| Configuration Method  | Task  | Rationale  |  
| --- | --- | --- |  
| `set_conv_simulator_lm()`  | Conversation simulation, query splitting  | Cheaper/faster model acceptable  |  
| `set_question_asker_lm()`  | Question generation  | Cheaper/faster model acceptable  |  
| `set_outline_gen_lm()`  | Outline structure creation  | More powerful model needed  |  
| `set_article_gen_lm()`  | Section writing with citations  | Most powerful model needed  |  
| `set_article_polish_lm()`  | Lead section and refinement  | Powerful model needed  |  
### Co-STORM Task Assignment (6 LMs)  
| Configuration Method  | Task  | Rationale  |  
| --- | --- | --- |  
| `set_question_answering_lm()`  | Expert utterance generation  | Powerful model for quality responses  |  
| `set_discourse_manage_lm()`  | Turn policy decisions  | Moderate model for coordination  |  
| `set_utterance_polishing_lm()`  | Utterance refinement  | Powerful model for final output  |  
| `set_warmstart_outline_gen_lm()`  | Initial KB structure  | Moderate model  |  
| `set_question_asking_lm()`  | Moderator questions  | Moderate model  |  
| `set_knowledge_base_lm()`  | KB operations (insert, expand)  | Moderate model  |  
This design allows optimization for cost-quality tradeoffs: use cheaper models (e.g., `gpt-3.5-turbo`) for intermediate steps and more powerful models (e.g., `gpt-4o`) for user-facing outputs.
Sources: [README.md104-217](https://github.com/stanford-oval/storm/blob/fb951af7/README.md?plain=1#L104-L217) [knowledge_storm/lm.py192-269](https://github.com/stanford-oval/storm/blob/fb951af7/knowledge_storm/lm.py#L192-L269)
## Technology Stack Summary
The repository is built on:
  * **litellm** : Universal LLM provider interface supporting OpenAI, Azure, Anthropic, Together, Groq, and 100+ others
  * **dspy** : Framework for language model programming with modular components
  * **qdrant-client** : Vector database integration for semantic search over custom documents
  * **Search APIs** : Direct integration with 8+ web search engines


The modular design with abstract interfaces ([interface.py](https://github.com/stanford-oval/storm/blob/fb951af7/interface.py)) enables custom implementations of any component while maintaining compatibility with the rest of the system.
Sources: [README.md72-101](https://github.com/stanford-oval/storm/blob/fb951af7/README.md?plain=1#L72-L101) [requirements.txt](https://github.com/stanford-oval/storm/blob/fb951af7/requirements.txt) (implied), [knowledge_storm/lm.py1-44](https://github.com/stanford-oval/storm/blob/fb951af7/knowledge_storm/lm.py#L1-L44)
## Usage Patterns
### STORM: Fully Automated Pipeline

```

```

from knowledge_storm import STORMWikiRunnerArguments, STORMWikiRunner, STORMWikiLMConfigs


from knowledge_storm.lm import LitellmModel


from knowledge_storm.rm import YouRM


 


# Configure LMs


lm_configs = STORMWikiLMConfigs()


lm_configs.set_conv_simulator_lm(LitellmModel(model='gpt-3.5-turbo', ...))


lm_configs.set_article_gen_lm(LitellmModel(model='gpt-4o', ...))


# ... configure other LMs


 


# Initialize runner


engine_args = STORMWikiRunnerArguments(...)


rm = YouRM(ydc_api_key=..., k=engine_args.search_top_k)


runner = STORMWikiRunner(engine_args, lm_configs, rm)


 


# Execute pipeline


runner.run(


    topic="Quantum Computing",


    do_research=True,


    do_generate_outline=True,


    do_generate_article=True,


    do_polish_article=True


)

```

```

The `run()` method executes all stages sequentially. Boolean flags control which stages execute (useful for resuming from intermediate results).
### Co-STORM: Interactive Collaboration

```

```

from knowledge_storm.collaborative_storm.engine import CoStormRunner, RunnerArgument


from knowledge_storm.lm import LitellmModel


from knowledge_storm.rm import BingSearch


 


# Configure runner


lm_config = CollaborativeStormLMConfigs()


# ... set 6 specialized LMs


runner_argument = RunnerArgument(topic="Climate Change", ...)


rm = BingSearch(bing_search_api_key=..., k=...)


costorm_runner = CoStormRunner(lm_config, runner_argument, rm)


 


# Warm start


costorm_runner.warm_start()


 


# Iterative discourse


for i in range(num_turns):


    # Observe mode: system generates next turn


    conv_turn = costorm_runner.step()


    


    # OR Active mode: user provides input


    # costorm_runner.step(user_utterance="Tell me more about...")


 


# Generate final report


costorm_runner.knowledge_base.reorganize()


article = costorm_runner.generate_report()

```

```

The `step()` method advances the conversation by one turn. Without arguments, agents generate utterances automatically. With `user_utterance`, the human steers the conversation.
Sources: [README.md104-217](https://github.com/stanford-oval/storm/blob/fb951af7/README.md?plain=1#L104-L217)
## Key Design Principles
  1. **Abstraction through Interfaces** : [interface.py](https://github.com/stanford-oval/storm/blob/fb951af7/interface.py) defines abstract contracts (`InformationTable`, `Article`, `Retriever`, `Module`, `Engine`, `Agent`) that enable custom implementations
  2. **Provider Agnosticism** : The `LitellmModel` wrapper and multiple RM implementations allow switching between providers without code changes
  3. **Modular Pipeline Design** : STORM's 4-stage pipeline and Co-STORM's agent system are composed of swappable modules
  4. **Multi-LLM Optimization** : Different tasks assigned to different models optimize cost-quality tradeoffs
  5. **Caching Strategy** : Two-tier LRU + disk caching reduces redundant API calls and costs
  6. **Thread-Safe Operations** : Token tracking and concurrent operations protected by locks
  7. **DSPy Integration** : Both systems leverage DSPy's language model programming paradigm for modular, declarative specifications


These principles enable the system to scale from research prototypes to production deployments while maintaining flexibility for customization.
Sources: [README.md273-292](https://github.com/stanford-oval/storm/blob/fb951af7/README.md?plain=1#L273-L292) [knowledge_storm/lm.py115-123](https://github.com/stanford-oval/storm/blob/fb951af7/knowledge_storm/lm.py#L115-L123) [knowledge_storm/interface.py1-50](https://github.com/stanford-oval/storm/blob/fb951af7/knowledge_storm/interface.py#L1-L50) (implied)
Dismiss
Refresh this wiki
Enter email to refresh
### On this page
  * [Overview](https://deepwiki.com/stanford-oval/storm#overview)
  * [What is STORM?](https://deepwiki.com/stanford-oval/storm#what-is-storm)
  * [What is Co-STORM?](https://deepwiki.com/stanford-oval/storm#what-is-co-storm)
  * [Core Package Structure](https://deepwiki.com/stanford-oval/storm#core-package-structure)
  * [System Architecture: Code Entity View](https://deepwiki.com/stanford-oval/storm#system-architecture-code-entity-view)
  * [STORM vs Co-STORM: Operational Paradigms](https://deepwiki.com/stanford-oval/storm#storm-vs-co-storm-operational-paradigms)
  * [STORM: Linear 4-Stage Pipeline](https://deepwiki.com/stanford-oval/storm#storm-linear-4-stage-pipeline)
  * [Co-STORM: Iterative Collaborative Loop](https://deepwiki.com/stanford-oval/storm#co-storm-iterative-collaborative-loop)
  * [Infrastructure Layer: Shared Components](https://deepwiki.com/stanford-oval/storm#infrastructure-layer-shared-components)
  * [Language Model Integration](https://deepwiki.com/stanford-oval/storm#language-model-integration)
  * [Retrieval Module Layer](https://deepwiki.com/stanford-oval/storm#retrieval-module-layer)
  * [Data Flow and Transformation](https://deepwiki.com/stanford-oval/storm#data-flow-and-transformation)
  * [STORM Data Pipeline](https://deepwiki.com/stanford-oval/storm#storm-data-pipeline)
  * [Co-STORM Data Flow](https://deepwiki.com/stanford-oval/storm#co-storm-data-flow)
  * [Multi-LLM System Design](https://deepwiki.com/stanford-oval/storm#multi-llm-system-design)
  * [STORM Task Assignment (5 LMs)](https://deepwiki.com/stanford-oval/storm#storm-task-assignment-5-lms)
  * [Co-STORM Task Assignment (6 LMs)](https://deepwiki.com/stanford-oval/storm#co-storm-task-assignment-6-lms)
  * [Technology Stack Summary](https://deepwiki.com/stanford-oval/storm#technology-stack-summary)
  * [Usage Patterns](https://deepwiki.com/stanford-oval/storm#usage-patterns)
  * [STORM: Fully Automated Pipeline](https://deepwiki.com/stanford-oval/storm#storm-fully-automated-pipeline)
  * [Co-STORM: Interactive Collaboration](https://deepwiki.com/stanford-oval/storm#co-storm-interactive-collaboration)
  * [Key Design Principles](https://deepwiki.com/stanford-oval/storm#key-design-principles)


Ask Devin about stanford-oval/storm
Fast

