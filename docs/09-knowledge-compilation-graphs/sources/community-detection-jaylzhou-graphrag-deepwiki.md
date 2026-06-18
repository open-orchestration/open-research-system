# Community Detection | JayLZhou/GraphRAG | DeepWiki

Source: https://deepwiki.com/JayLZhou/GraphRAG/7.2-community-detection

Index your code with Devin
[DeepWiki](https://deepwiki.com/)
[DeepWiki](https://deepwiki.com/)
[JayLZhou/GraphRAG ](https://github.com/JayLZhou/GraphRAG "Open repository")
Index your code with
Devin
Edit WikiShare
Last indexed: 19 April 2025 ([d5a265](https://github.com/JayLZhou/GraphRAG/commits/d5a26538))
  * [GraphRAG Overview](https://deepwiki.com/JayLZhou/GraphRAG/1-graphrag-overview)
  * [System Architecture](https://deepwiki.com/JayLZhou/GraphRAG/2-system-architecture)
  * [Graph System](https://deepwiki.com/JayLZhou/GraphRAG/2.1-graph-system)
  * [BaseGraph](https://deepwiki.com/JayLZhou/GraphRAG/2.1.1-basegraph)
  * [TreeGraph](https://deepwiki.com/JayLZhou/GraphRAG/2.1.2-treegraph)
  * [ERGraph](https://deepwiki.com/JayLZhou/GraphRAG/2.1.3-ergraph)
  * [Other Graph Types](https://deepwiki.com/JayLZhou/GraphRAG/2.1.4-other-graph-types)
  * [Retrieval System](https://deepwiki.com/JayLZhou/GraphRAG/2.2-retrieval-system)
  * [Entity Retrieval](https://deepwiki.com/JayLZhou/GraphRAG/2.2.1-entity-retrieval)
  * [Relationship Retrieval](https://deepwiki.com/JayLZhou/GraphRAG/2.2.2-relationship-retrieval)
  * [Chunk Retrieval](https://deepwiki.com/JayLZhou/GraphRAG/2.2.3-chunk-retrieval)
  * [Vector Indexing](https://deepwiki.com/JayLZhou/GraphRAG/2.3-vector-indexing)
  * [Query Processing](https://deepwiki.com/JayLZhou/GraphRAG/2.4-query-processing)
  * [Configuration System](https://deepwiki.com/JayLZhou/GraphRAG/3-configuration-system)
  * [GraphRAG Methods](https://deepwiki.com/JayLZhou/GraphRAG/4-graphrag-methods)
  * [RAPTOR Method](https://deepwiki.com/JayLZhou/GraphRAG/4.1-raptor-method)
  * [LightRAG Method](https://deepwiki.com/JayLZhou/GraphRAG/4.2-lightrag-method)
  * [Other RAG Methods](https://deepwiki.com/JayLZhou/GraphRAG/4.3-other-rag-methods)
  * [Evaluation System](https://deepwiki.com/JayLZhou/GraphRAG/5-evaluation-system)
  * [LLM Integration](https://deepwiki.com/JayLZhou/GraphRAG/6-llm-integration)
  * [Utility Components](https://deepwiki.com/JayLZhou/GraphRAG/7-utility-components)
  * [Storage Systems](https://deepwiki.com/JayLZhou/GraphRAG/7.1-storage-systems)
  * [Community Detection](https://deepwiki.com/JayLZhou/GraphRAG/7.2-community-detection)


Menu
# Community Detection
Relevant source files
  * [Core/Community/BaseCommunity.py](https://github.com/JayLZhou/GraphRAG/blob/d5a26538/Core/Community/BaseCommunity.py)
  * [Core/Community/LeidenCommunity.py](https://github.com/JayLZhou/GraphRAG/blob/d5a26538/Core/Community/LeidenCommunity.py)
  * [Core/Prompt/RaptorPrompt.py](https://github.com/JayLZhou/GraphRAG/blob/d5a26538/Core/Prompt/RaptorPrompt.py)
  * [Core/Storage/ChunkKVStorage.py](https://github.com/JayLZhou/GraphRAG/blob/d5a26538/Core/Storage/ChunkKVStorage.py)
  * [Core/Storage/JsonKVStorage.py](https://github.com/JayLZhou/GraphRAG/blob/d5a26538/Core/Storage/JsonKVStorage.py)
  * [Core/Storage/__pycache__/ChunkKVStorage.cpython-311.pyc](https://github.com/JayLZhou/GraphRAG/blob/d5a26538/Core/Storage/__pycache__/ChunkKVStorage.cpython-311.pyc)


The Community Detection system in GraphRAG implements graph clustering algorithms that identify related node groups within the knowledge graph. This component creates a hierarchical community structure that improves retrieval efficiency by organizing knowledge into meaningful clusters. Community detection plays a critical role in query processing by allowing the system to identify and retrieve topically relevant subgraphs.
Sources: [Core/Community/BaseCommunity.py1-81](https://github.com/JayLZhou/GraphRAG/blob/d5a26538/Core/Community/BaseCommunity.py#L1-L81) [Core/Community/LeidenCommunity.py1-287](https://github.com/JayLZhou/GraphRAG/blob/d5a26538/Core/Community/LeidenCommunity.py#L1-L287)
## Community Detection Architecture
Community detection in GraphRAG follows a modular design with abstract interfaces and concrete implementations:
### Community Detection System Structure
Sources: [Core/Community/BaseCommunity.py5-12](https://github.com/JayLZhou/GraphRAG/blob/d5a26538/Core/Community/BaseCommunity.py#L5-L12) [Core/Community/LeidenCommunity.py23-31](https://github.com/JayLZhou/GraphRAG/blob/d5a26538/Core/Community/LeidenCommunity.py#L23-L31) [Core/Storage/JsonKVStorage.py8-14](https://github.com/JayLZhou/GraphRAG/blob/d5a26538/Core/Storage/JsonKVStorage.py#L8-L14)
### Key Components
  1. **BaseCommunity** : Abstract class defining the interface for community detection:
     * `generate_community_report()`: Creates descriptive reports for communities
     * `cluster()`: Performs community detection on the graph
  2. **LeidenCommunity** : Concrete implementation using the Leiden algorithm for hierarchical community detection:
     * Registered with name "leiden" using the `@register_community` decorator
     * Uses the graspologic library's hierarchical Leiden implementation
     * Manages community data and reports through JsonKVStorage
  3. **Storage System** :
     * `_community_reports`: JsonKVStorage for storing community descriptive reports
     * `_community_node_map`: JsonKVStorage for mapping nodes to communities
     * Enables persistence and reuse of community data


Sources: [Core/Community/BaseCommunity.py13-35](https://github.com/JayLZhou/GraphRAG/blob/d5a26538/Core/Community/BaseCommunity.py#L13-L35) [Core/Community/LeidenCommunity.py28-30](https://github.com/JayLZhou/GraphRAG/blob/d5a26538/Core/Community/LeidenCommunity.py#L28-L30) [Core/Storage/JsonKVStorage.py15-60](https://github.com/JayLZhou/GraphRAG/blob/d5a26538/Core/Storage/JsonKVStorage.py#L15-L60)
## Community Detection Process
The community detection workflow involves clustering and report generation:
### Community Detection Workflow
Sources: [Core/Community/BaseCommunity.py36-57](https://github.com/JayLZhou/GraphRAG/blob/d5a26538/Core/Community/BaseCommunity.py#L36-L57) [Core/Community/LeidenCommunity.py37-40](https://github.com/JayLZhou/GraphRAG/blob/d5a26538/Core/Community/LeidenCommunity.py#L37-L40) [Core/Community/LeidenCommunity.py70-106](https://github.com/JayLZhou/GraphRAG/blob/d5a26538/Core/Community/LeidenCommunity.py#L70-L106)
### Clustering with Leiden Algorithm
The core clustering process uses the hierarchical Leiden algorithm:
  1. **Algorithm** : Uses `hierarchical_leiden()` from graspologic library
     * Parameters: `largest_cc` (largest connected component), `max_cluster_size`, `random_seed`
     * Creates a hierarchical partition of the graph
  2. **Processing Partitions** :
     * Processes algorithm output into a node-to-community mapping with hierarchy levels
     * Each node is assigned to clusters at different hierarchy levels
     * Mapping is stored in `_community_node_map` for persistence
  3. **Hierarchical Structure** :
     * Communities are organized in levels (higher levels = broader communities)
     * Level statistics are logged (e.g., `Each level has communities: {dict(__levels)}`)


Sources: [Core/Community/LeidenCommunity.py37-64](https://github.com/JayLZhou/GraphRAG/blob/d5a26538/Core/Community/LeidenCommunity.py#L37-L64)
### Community Report Generation
After clustering, the system generates descriptive reports for each community:
  1. **Community Schema Construction** :
     * Calls `cluster_data_to_subgraphs()` on the graph to prepare subgraphs
     * Retrieves community schema with hierarchy information
  2. **Level-by-Level Processing** :
     * Processes communities level by level (typically from higher to lower)
     * Generates reports for communities at each level
  3. **Single Community Report Generation** :
     * For each community, collects: 
       * Community nodes and their metadata
       * Community edges and their relationships
       * Sub-community reports (if available)
     * Formats data as CSV-style strings for LLM processing
     * Uses LLM to generate a structured report from the data
  4. **Report Storage** :
     * Stores reports in `_community_reports` JsonKVStorage
     * Reports contain: description, key entities, relationships, and ratings


Sources: [Core/Community/LeidenCommunity.py70-106](https://github.com/JayLZhou/GraphRAG/blob/d5a26538/Core/Community/LeidenCommunity.py#L70-L106) [Core/Community/LeidenCommunity.py106-115](https://github.com/JayLZhou/GraphRAG/blob/d5a26538/Core/Community/LeidenCommunity.py#L106-L115) [Core/Community/LeidenCommunity.py162-250](https://github.com/JayLZhou/GraphRAG/blob/d5a26538/Core/Community/LeidenCommunity.py#L162-L250)
## Data Structures
The community detection system uses several specialized data structures:
### Community Hierarchy Data Model
Sources: [Core/Community/LeidenCommunity.py28-30](https://github.com/JayLZhou/GraphRAG/blob/d5a26538/Core/Community/LeidenCommunity.py#L28-L30) [Core/Community/LeidenCommunity.py42-64](https://github.com/JayLZhou/GraphRAG/blob/d5a26538/Core/Community/LeidenCommunity.py#L42-L64)
### Key Data Structures:
  1. **Node-to-Community Mapping** :

```

```

{


  "node_id": [


    {"level": 2, "cluster": "0"},


    {"level": 1, "cluster": "1"},


    {"level": 0, "cluster": "3"}


  ]


}

```

```

  2. **Community Schema (LeidenInfo)** :

```

```

{


  "community_id": {


    "level": 2,


    "cluster": "0",


    "nodes": ["node1", "node2", "node3"],


    "edges": [["node1", "node2"], ["node2", "node3"]],


    "sub_communities": ["community_id_1", "community_id_2"]


  }


}

```

```

  3. **Community Report** :

```

```

{


  "community_id": {


    "report_string": "This community represents...",


    "report_json": {


      "title": "Financial Technology Ecosystem",


      "summary": "A cluster of entities related to financial technology",


      "key_entities": ["Blockchain", "Cryptocurrency", "Banking"],


      "relationships": ["Blockchain supports Cryptocurrency"],


      "rating": 4.5


    }


  }


}

```

```



Sources: [Core/Community/LeidenCommunity.py42-64](https://github.com/JayLZhou/GraphRAG/blob/d5a26538/Core/Community/LeidenCommunity.py#L42-L64) [Core/Community/LeidenCommunity.py70-106](https://github.com/JayLZhou/GraphRAG/blob/d5a26538/Core/Community/LeidenCommunity.py#L70-L106)
## Integration with Retrieval System
Community detection enhances the retrieval pipeline in GraphRAG:
### Community-Based Retrieval Flow
Sources: [Core/Community/LeidenCommunity.py1-287](https://github.com/JayLZhou/GraphRAG/blob/d5a26538/Core/Community/LeidenCommunity.py#L1-L287)
## Use Cases and Benefits
Community detection provides several advantages in graph-based retrieval:
  1. **Efficient Navigation of Large Graphs** :
     * Communities create a hierarchical structure for more efficient traversal
     * Allows focusing on relevant subgraphs rather than searching the entire graph
  2. **Contextual Understanding** :
     * Community reports provide context about semantically related nodes
     * Helps the system understand relationships between entities
  3. **Improved Query Processing** :
     * Query can be matched to topically relevant communities first
     * Narrows search space for subsequent entity and relationship retrieval
  4. **Hierarchical Retrieval** :
     * Supports zooming in/out on information at different granularity levels
     * From broad topics (higher-level communities) to specific details (lower-level communities)


Sources: [Core/Community/LeidenCommunity.py1-3](https://github.com/JayLZhou/GraphRAG/blob/d5a26538/Core/Community/LeidenCommunity.py#L1-L3) [Core/Community/BaseCommunity.py15-23](https://github.com/JayLZhou/GraphRAG/blob/d5a26538/Core/Community/BaseCommunity.py#L15-L23)
## Implementation Notes
### LeidenCommunity Implementation
The primary implementation of community detection uses the Leiden algorithm:

```

```

# Key implementation details from LeidenCommunity.py


@register_community(name="leiden")


class LeidenCommunity(BaseCommunity):


    # ...


    


    async def clustering(self, largest_cc, max_cluster_size, random_seed):


        await self._clustering(largest_cc, max_cluster_size, random_seed)


        


    async def _clustering(self, largest_cc, max_cluster_size, random_seed):


        # Use hierarchical_leiden from graspologic library


        community_mapping = hierarchical_leiden(


            largest_cc,


            max_cluster_size=max_cluster_size,


            random_seed=random_seed,


        )


        


        # Process the mapping results


        node_communities: dict[str, list[dict[str, str]]] = defaultdict(list)


        # ...

```

```

Sources: [Core/Community/LeidenCommunity.py23-63](https://github.com/JayLZhou/GraphRAG/blob/d5a26538/Core/Community/LeidenCommunity.py#L23-L63)
### Report Generation Process
The report generation uses an LLM to create descriptive reports for each community:

```

```

# Community report generation workflow


async def _form_single_community_report(self, er_graph, community, already_reports):


    # Package community data for LLM


    describe = await self._pack_single_community_describe(er_graph, community, already_reports)


    


    # Use community report prompt template


    prompt = CommunityPrompt.COMMUNITY_REPORT.format(input_text=describe)


    


    # Get response from LLM in JSON format


    response = await self.llm.aask(prompt, format="json")


    return response

```

```

Sources: [Core/Community/LeidenCommunity.py106-115](https://github.com/JayLZhou/GraphRAG/blob/d5a26538/Core/Community/LeidenCommunity.py#L106-L115)
## Configuration and Tuning
Community detection can be configured through several parameters:  
| Parameter  | Description  | Default  | Effect  |  
| --- | --- | --- | --- |  
| `max_cluster_size`  | Maximum size for a community  | Varies  | Larger values create broader communities  |  
| `random_seed`  | Seed for randomized operations  | None  | Controls deterministic results  |  
| `enforce_sub_communities`  | Force use of sub-communities  | False  | When true, always uses hierarchical structure  |  
| `largest_cc`  | Use only largest connected component  | True  | Filter to main graph component  |  
Sources: [Core/Community/LeidenCommunity.py37-40](https://github.com/JayLZhou/GraphRAG/blob/d5a26538/Core/Community/LeidenCommunity.py#L37-L40) [Core/Community/BaseCommunity.py8-11](https://github.com/JayLZhou/GraphRAG/blob/d5a26538/Core/Community/BaseCommunity.py#L8-L11)
## Summary
The Community Detection system in GraphRAG provides a powerful mechanism for organizing graph knowledge into a hierarchical structure of related nodes. Through the Leiden algorithm implementation, it identifies meaningful clusters at different granularity levels. The system generates LLM-powered descriptive reports for each community, providing semantic context for retrieval operations. This component enhances retrieval efficiency and relevance by enabling the system to focus on topically appropriate sections of the knowledge graph when processing queries.
Sources: [Core/Community/BaseCommunity.py1-81](https://github.com/JayLZhou/GraphRAG/blob/d5a26538/Core/Community/BaseCommunity.py#L1-L81) [Core/Community/LeidenCommunity.py1-287](https://github.com/JayLZhou/GraphRAG/blob/d5a26538/Core/Community/LeidenCommunity.py#L1-L287)
Dismiss
Refresh this wiki
Enter email to refresh
### On this page
  * [Community Detection](https://deepwiki.com/JayLZhou/GraphRAG/7.2-community-detection#community-detection)
  * [Community Detection Architecture](https://deepwiki.com/JayLZhou/GraphRAG/7.2-community-detection#community-detection-architecture)
  * [Community Detection System Structure](https://deepwiki.com/JayLZhou/GraphRAG/7.2-community-detection#community-detection-system-structure)
  * [Key Components](https://deepwiki.com/JayLZhou/GraphRAG/7.2-community-detection#key-components)
  * [Community Detection Process](https://deepwiki.com/JayLZhou/GraphRAG/7.2-community-detection#community-detection-process)
  * [Community Detection Workflow](https://deepwiki.com/JayLZhou/GraphRAG/7.2-community-detection#community-detection-workflow)
  * [Clustering with Leiden Algorithm](https://deepwiki.com/JayLZhou/GraphRAG/7.2-community-detection#clustering-with-leiden-algorithm)
  * [Community Report Generation](https://deepwiki.com/JayLZhou/GraphRAG/7.2-community-detection#community-report-generation)
  * [Data Structures](https://deepwiki.com/JayLZhou/GraphRAG/7.2-community-detection#data-structures)
  * [Community Hierarchy Data Model](https://deepwiki.com/JayLZhou/GraphRAG/7.2-community-detection#community-hierarchy-data-model)
  * [Key Data Structures:](https://deepwiki.com/JayLZhou/GraphRAG/7.2-community-detection#key-data-structures)
  * [Integration with Retrieval System](https://deepwiki.com/JayLZhou/GraphRAG/7.2-community-detection#integration-with-retrieval-system)
  * [Community-Based Retrieval Flow](https://deepwiki.com/JayLZhou/GraphRAG/7.2-community-detection#community-based-retrieval-flow)
  * [Use Cases and Benefits](https://deepwiki.com/JayLZhou/GraphRAG/7.2-community-detection#use-cases-and-benefits)
  * [Implementation Notes](https://deepwiki.com/JayLZhou/GraphRAG/7.2-community-detection#implementation-notes)
  * [LeidenCommunity Implementation](https://deepwiki.com/JayLZhou/GraphRAG/7.2-community-detection#leidencommunity-implementation)
  * [Report Generation Process](https://deepwiki.com/JayLZhou/GraphRAG/7.2-community-detection#report-generation-process)
  * [Configuration and Tuning](https://deepwiki.com/JayLZhou/GraphRAG/7.2-community-detection#configuration-and-tuning)
  * [Summary](https://deepwiki.com/JayLZhou/GraphRAG/7.2-community-detection#summary)


Ask Devin about JayLZhou/GraphRAG
Fast

