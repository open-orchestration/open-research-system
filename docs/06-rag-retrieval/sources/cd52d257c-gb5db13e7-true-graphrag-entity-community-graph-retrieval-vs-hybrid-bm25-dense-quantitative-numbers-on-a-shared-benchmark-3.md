[ ![logo](https://services.dev.arxiv.org/html/static/arxiv-logomark-small-white.svg) Back to arXiv ](https://arxiv.org/)
[ ](https://arxiv.org/abs/2507.03226v3) [ ](javascript:toggleColorScheme\(\) "Toggle dark/light mode")
[ ![logo](https://services.dev.arxiv.org/html/static/arxiv-logo-one-color-white.svg) Back to arXiv ](https://arxiv.org/)
This is **experimental HTML** to improve accessibility. We invite you to report rendering errors. Use Alt+Y to toggle on accessible reporting links and Alt+Shift+Y to toggle off. Learn more [about this project](https://info.arxiv.org/about/accessible_HTML.html) and [help improve conversions](https://info.arxiv.org/help/submit_latex_best_practices.html). 
[Why HTML?](https://info.arxiv.org/about/accessible_HTML.html) [Report Issue](/html/2507.03226v3/#myForm) [Back to Abstract](https://arxiv.org/abs/2507.03226v3) [Download PDF](https://arxiv.org/pdf/2507.03226v3) [ ](javascript:toggleColorScheme\(\) "Toggle dark/light mode")
## Table of Contents
  1. [ Abstract  ](https://arxiv.org/html/2507.03226v3#abstract "Abstract")
  2. [1 Introduction](https://arxiv.org/html/2507.03226v3#S1 "In Towards Practical GraphRAG: Efficient Knowledge Graph Construction and Hybrid Retrieval at Scale")
  3. [2 Related Work](https://arxiv.org/html/2507.03226v3#S2 "In Towards Practical GraphRAG: Efficient Knowledge Graph Construction and Hybrid Retrieval at Scale")
  4. [3 Methodology](https://arxiv.org/html/2507.03226v3#S3 "In Towards Practical GraphRAG: Efficient Knowledge Graph Construction and Hybrid Retrieval at Scale")
    1. [3.1 Knowledge Graph Construction](https://arxiv.org/html/2507.03226v3#S3.SS1 "In 3 Methodology ‣ Towards Practical GraphRAG: Efficient Knowledge Graph Construction and Hybrid Retrieval at Scale")
      1. [3.1.1 Preprocessing Pipeline](https://arxiv.org/html/2507.03226v3#S3.SS1.SSS1 "In 3.1 Knowledge Graph Construction ‣ 3 Methodology ‣ Towards Practical GraphRAG: Efficient Knowledge Graph Construction and Hybrid Retrieval at Scale")
      2. [3.1.2 Dependency-Based Triple Extraction](https://arxiv.org/html/2507.03226v3#S3.SS1.SSS2 "In 3.1 Knowledge Graph Construction ‣ 3 Methodology ‣ Towards Practical GraphRAG: Efficient Knowledge Graph Construction and Hybrid Retrieval at Scale")
      3. [3.1.3 LLM-Based Extraction](https://arxiv.org/html/2507.03226v3#S3.SS1.SSS3 "In 3.1 Knowledge Graph Construction ‣ 3 Methodology ‣ Towards Practical GraphRAG: Efficient Knowledge Graph Construction and Hybrid Retrieval at Scale")
      4. [3.1.4 Graph Storage](https://arxiv.org/html/2507.03226v3#S3.SS1.SSS4 "In 3.1 Knowledge Graph Construction ‣ 3 Methodology ‣ Towards Practical GraphRAG: Efficient Knowledge Graph Construction and Hybrid Retrieval at Scale")
    2. [3.2 Efficient Hybrid Graph Retrieval](https://arxiv.org/html/2507.03226v3#S3.SS2 "In 3 Methodology ‣ Towards Practical GraphRAG: Efficient Knowledge Graph Construction and Hybrid Retrieval at Scale")
      1. [3.2.1 Query Entity Identification](https://arxiv.org/html/2507.03226v3#S3.SS2.SSS1 "In 3.2 Efficient Hybrid Graph Retrieval ‣ 3 Methodology ‣ Towards Practical GraphRAG: Efficient Knowledge Graph Construction and Hybrid Retrieval at Scale")
      2. [3.2.2 Graph Query Execution](https://arxiv.org/html/2507.03226v3#S3.SS2.SSS2 "In 3.2 Efficient Hybrid Graph Retrieval ‣ 3 Methodology ‣ Towards Practical GraphRAG: Efficient Knowledge Graph Construction and Hybrid Retrieval at Scale")
      3. [3.2.3 Relevance Ranking and Context Selection](https://arxiv.org/html/2507.03226v3#S3.SS2.SSS3 "In 3.2 Efficient Hybrid Graph Retrieval ‣ 3 Methodology ‣ Towards Practical GraphRAG: Efficient Knowledge Graph Construction and Hybrid Retrieval at Scale")
      4. [3.2.4 Context Integration with LLM](https://arxiv.org/html/2507.03226v3#S3.SS2.SSS4 "In 3.2 Efficient Hybrid Graph Retrieval ‣ 3 Methodology ‣ Towards Practical GraphRAG: Efficient Knowledge Graph Construction and Hybrid Retrieval at Scale")
  5. [4 Experiments](https://arxiv.org/html/2507.03226v3#S4 "In Towards Practical GraphRAG: Efficient Knowledge Graph Construction and Hybrid Retrieval at Scale")
    1. [4.1 Datasets](https://arxiv.org/html/2507.03226v3#S4.SS1 "In 4 Experiments ‣ Towards Practical GraphRAG: Efficient Knowledge Graph Construction and Hybrid Retrieval at Scale")
    2. [4.2 Evaluation Methodology](https://arxiv.org/html/2507.03226v3#S4.SS2 "In 4 Experiments ‣ Towards Practical GraphRAG: Efficient Knowledge Graph Construction and Hybrid Retrieval at Scale")
      1. [4.2.1 CCM Chat Evaluation](https://arxiv.org/html/2507.03226v3#S4.SS2.SSS1 "In 4.2 Evaluation Methodology ‣ 4 Experiments ‣ Towards Practical GraphRAG: Efficient Knowledge Graph Construction and Hybrid Retrieval at Scale")
      2. [4.2.2 CCM Code Proposal Evaluation](https://arxiv.org/html/2507.03226v3#S4.SS2.SSS2 "In 4.2 Evaluation Methodology ‣ 4 Experiments ‣ Towards Practical GraphRAG: Efficient Knowledge Graph Construction and Hybrid Retrieval at Scale")
    3. [4.3 Results and Analysis](https://arxiv.org/html/2507.03226v3#S4.SS3 "In 4 Experiments ‣ Towards Practical GraphRAG: Efficient Knowledge Graph Construction and Hybrid Retrieval at Scale")
      1. [4.3.1 System Performance Result On CCM Chat](https://arxiv.org/html/2507.03226v3#S4.SS3.SSS1 "In 4.3 Results and Analysis ‣ 4 Experiments ‣ Towards Practical GraphRAG: Efficient Knowledge Graph Construction and Hybrid Retrieval at Scale")
      2. [4.3.2 System Performance Result on CCM Code Proposal](https://arxiv.org/html/2507.03226v3#S4.SS3.SSS2 "In 4.3 Results and Analysis ‣ 4 Experiments ‣ Towards Practical GraphRAG: Efficient Knowledge Graph Construction and Hybrid Retrieval at Scale")
      3. [4.3.3 Qualitative Insight](https://arxiv.org/html/2507.03226v3#S4.SS3.SSS3 "In 4.3 Results and Analysis ‣ 4 Experiments ‣ Towards Practical GraphRAG: Efficient Knowledge Graph Construction and Hybrid Retrieval at Scale")
  6. [5 Conclusion, Limitation and Future Work](https://arxiv.org/html/2507.03226v3#S5 "In Towards Practical GraphRAG: Efficient Knowledge Graph Construction and Hybrid Retrieval at Scale")
  7. [6 GenAI Usage Disclosure](https://arxiv.org/html/2507.03226v3#S6 "In Towards Practical GraphRAG: Efficient Knowledge Graph Construction and Hybrid Retrieval at Scale")


[License: CC BY-NC-SA 4.0](https://info.arxiv.org/help/license/index.html#licenses-available)
arXiv:2507.03226v3 [cs.AI] 18 Dec 2025
11institutetext: SAP, Palo Alto, CA, USA   
11email: {congmin.min, sahil.bansal01, joyce.pan01, abbas.keshavarzi, rhea.mathew}@sap.com, amarviswanathan@gmail.com
# Towards Practical GraphRAG: Efficient Knowledge Graph Construction and Hybrid Retrieval at Scale
Report issue for preceding element
Congmin Min  Sahil Bansal Sahil Bansal, Joyce Pan, and Abbas Keshavarzi contributed equally to this work. Joyce Pan  Abbas Keshavarzi  Rhea Mathew  Amar Viswanathan Kannan 
Report issue for preceding element
###### Abstract
Report issue for preceding element
We propose a scalable and cost-efficient framework for deploying Graph-based Retrieval-Augmented Generation (GraphRAG) in enterprise environments. While GraphRAG has shown promise for multi-hop reasoning and structured retrieval, its adoption has been limited due to reliance on expensive large language model (LLM)-based extraction and complex traversal strategies. To address these challenges, we introduce two core innovations: (1) an efficient knowledge graph construction pipeline that leverages dependency parsing to achieve 94%94\% of LLM-based performance (61.87%61.87\% vs. 65.83%65.83\%) while significantly reducing costs and improving scalability; and (2) a hybrid retrieval strategy that fuses vector similarity with graph traversal using Reciprocal Rank Fusion (RRF), maintaining separate embeddings for entities, chunks, and relations to enable multi-granular matching. We evaluate our framework on two enterprise datasets focused on legacy code migration and demonstrate improvements of up to 15%15\% and 4.35%4.35\% over vanilla vector retrieval baselines using LLM-as-Judge evaluation metrics. These results validate the feasibility of deploying GraphRAG in production enterprise environments, demonstrating that careful engineering of classical NLP techniques can match modern LLM-based approaches while enabling practical, cost-effective, and domain-adaptable retrieval-augmented reasoning at scale.
Report issue for preceding element
##  1 Introduction
Report issue for preceding element
Retrieval-Augmented Generation (RAG) has emerged as a practical framework for enhancing LLMs by grounding their outputs in external knowledge sources. In a standard RAG pipeline, a user query triggers the retrieval of semantically relevant passages from a document corpus using dense-vector retrieval. These retrieved passages are then fed to an LLM as contextual input, anchoring its responses in factual content. This architecture helps reduce hallucinations and enables the model to stay current with evolving information without the need for expensive model retraining [lewis2020retrieval]. In enterprise settings, RAG allows organizations to integrate proprietary data so that generated responses align with the latest domain-specific knowledge [gao2023retrieval].
Report issue for preceding element
Modern enterprise resource planning (ERP) systems - used for finance, procurement, HR, and manufacturing - generate vast volumes of structured and unstructured data across interconnected modules. Enterprise queries often involve reasoning over configuration rules, transactional dependencies, change logs, and migration notes or cookbooks that are distributed across documents and systems in modern ERP systems. For example, assessing the impact of a custom code migration in S/4HANA 111S/4HANA is an in-memory databse that the next-generation ERP system runs on. may require linking legacy Advanced Business Application Programming (ABAP) 222ABAP is a high-level programming language within the ERP ecosystem. functions with deprecation reports, compatibility matrices, and policy guidelines. Traditional RAG systems treat documents as isolated units, limiting relational reasoning capabilities. Graph-based retrieval addresses this limitation by modeling entity relationships and enabling structure-aware context selection, making it well-suited for enterprise applications where understanding dependencies between components and processes is critical.
Report issue for preceding element
However, deploying GraphRAG in enterprise settings introduces two core challenges:
Report issue for preceding element
  1. 1.
Computational cost of graph construction. Building a knowledge graph (KG) at enterprise scale requires large-scale entity and relation extraction. When this process relies on LLMs or heavyweight NLP pipelines, it incurs significant GPU costs, leading to high latency and limited refresh frequency for dynamic content.
Report issue for preceding element
  2. 2.
Retrieval latency and scalability. Querying large graphs for relevant subgraphs introduces significant latency. Complex traversal and ranking operations struggle to meet real-time performance requirements at scale, even with optimized databases (DBs).
Report issue for preceding element


In this paper, we propose a GraphRAG framework for enterprise-scale deployment with three key contributions:
Report issue for preceding element
  1. 1.
Efficient Knowledge Graph Construction. A pipeline using dependency parsing that achieves competitive performance while reducing reliance on expensive LLM-based extraction.
Report issue for preceding element
  2. 2.
Hybrid Retrieval Strategy. Combining vector similarity with graph traversal using RRF [cormack2009reciprocal] to improve retrieval effectiveness.
Report issue for preceding element
  3. 3.
Real-World Legacy Code Migration Application. First application of GraphRAG to enterprise legacy code migration, demonstrating significant improvements over dense retrieval baselines.
Report issue for preceding element


These contributions enable explainable, accurate, and scalable retrieval-augmented reasoning in complex enterprise environments.
Report issue for preceding element
##  2 Related Work
Report issue for preceding element
RAG combines dense-vector retrieval with language models (LM) to ground generation in external knowledge [lewis2020retrieval]. While effective for simple queries, traditional RAG systems treat documents as isolated units, limiting their effectiveness for relational reasoning over structured knowledge [barnett2024seven, bruckhaus2024rag]. This has motivated the development of graph-based approaches that explicitly model entity relationships.
Report issue for preceding element
To address these gaps, the GraphRAG paradigm was introduced, embedding a structured knowledge graph (KG) between the retrieval and generation stages [han2024retrieval]. GraphRAG [edge2024local] pioneered the integration of KGs into RAG by constructing entity-relation graphs from retrieved passages and organizing them into semantic communities through LLM-based summarization. This approach demonstrated significant improvements in multi-hop reasoning but incurs substantial computational costs due to extensive LLM usage during both construction and query-time summarization. Recent work has focused on improving GraphRAG efficiency. LightRAG [guo2025lightragsimplefastretrievalaugmented] introduces dual-level entity-relation indexing to accelerate retrieval, while HippoRAG [jimenez2024hipporag] employs Personalized PageRank for memory-inspired graph traversal. FastGraphRAG [fastgraphrag2025] proposes optimizations for faster subgraph extraction. Most recently, SubGCache [zhu2025subgcache] addresses query-time latency through subgraph-level key-value (KV) caching to reduce redundant LLM inference during retrieval. However, all these systems rely on LLM-based KG construction, which presents a fundamental scalability bottleneck for large enterprise corpora. While query-time optimizations like SubGCache improve retrieval efficiency, the upstream construction cost remains prohibitive for dynamic, large-scale deployments.
Report issue for preceding element
In contrast to prior work, we address the construction bottleneck by demonstrating that dependency-based extraction—leveraging classical NLP techniques—achieves 94% of LLM-based performance while significantly reducing computational costs. We further introduce a hybrid retrieval strategy combining vector similarity with efficient graph traversal via RRF, maintaining separate embeddings for entities, chunks, and relations. Unlike previous GraphRAG systems that focus primarily on reasoning capabilities or query-time efficiency, our framework addresses both construction scalability and retrieval effectiveness, enabling practical GraphRAG deployment in cost-sensitive enterprise environments. We validate our approach on real-world legacy code migration tasks, demonstrating the first application of GraphRAG to this domain.
Report issue for preceding element
##  3 Methodology
Report issue for preceding element
Our GraphRAG framework comprises two core components designed for scalable enterprise deployment:
Report issue for preceding element
  1. 1.
Flexible KG Construction, supporting both dependency-based and LLM-based extraction modes, enabling cost-accuracy trade-offs based on deployment requirements
Report issue for preceding element
  2. 2.
Hybrid Graph Retrieval, combining efficient graph traversal with vector-based ranking to retrieve high-recall, semantically relevant contexts.
Report issue for preceding element


###  3.1 Knowledge Graph Construction
Report issue for preceding element
We support two interchangeable construction pipelines: a dependency-based approach that leverages linguistic structure for fast, cost-effective extraction, and a LLM-based approach that achieves higher accuracy on smaller datasets. Both produce entity-relation graphs stored in a unified backend graph DB for downstream retrieval.
Report issue for preceding element
![Refer to caption](/html/2507.03226v3/x1.png) Figure 1: Dual Extraction Architecture for Knowledge Graph Construction Report issue for preceding element
Figure [1](https://arxiv.org/html/2507.03226v3#S3.F1 "Figure 1 ‣ 3.1 Knowledge Graph Construction ‣ 3 Methodology ‣ Towards Practical GraphRAG: Efficient Knowledge Graph Construction and Hybrid Retrieval at Scale") illustrates our dual knowledge graph construction pipeline, which supports both an LLM-based extraction path, a lightweight dependency-parser-based alternative, and a combination of the two. Input documents pass through a series of preprocessing and filtering stages before triples are extracted, normalized, and materialized in the target graph store.
Report issue for preceding element
####  3.1.1 Preprocessing Pipeline
Report issue for preceding element
Input documents arrive in diverse formats (PDF, HTML, XLSX, CSV) and undergo standardized preprocessing. We parse documents using Docling333<https://github.com/docling-project/docling> to extract text while preserving structural metadata, then apply hierarchical chunking [hearst-1997-text] that respects discourse boundaries by splitting at section headers. When a section exceeds 20482048 characters, we apply recursive character-level splitting with a 200200-character overlap. Each chunk is segmented into sentences using SpaCy 444<https://spacy.io/>, and we filter sentences lacking verb phrases to reduce downstream processing overhead—an optimization that significantly improves efficiency for large corpora.
Report issue for preceding element
####  3.1.2 Dependency-Based Triple Extraction
Report issue for preceding element
We draw upon dependency grammar theory [de-marneffe-etal-2021-universal], which posits that a sentence’s syntactic structure can be represented as a graph of binary head–dependent relations. A core contribution of our work in this paper demonstrates that dependency parsing can achieve competitive knowledge extraction performance while maintaining enterprise-scale efficiency. We leverage SpaCy’s dependency parser to extract entity-relation triples directly from syntactic structure. For example, for the sentence "SAP launched Joule for Consultants", the dependency parser produces a tree structure (Figure [2](https://arxiv.org/html/2507.03226v3#S3.F2 "Figure 2 ‣ 3.1.2 Dependency-Based Triple Extraction ‣ 3.1 Knowledge Graph Construction ‣ 3 Methodology ‣ Towards Practical GraphRAG: Efficient Knowledge Graph Construction and Hybrid Retrieval at Scale")) identifying "launched" as the root verb with "SAP" as subject (nsubj), "Joule" as direct object (dobj), and "Consultants" as prepositional object. From this structure, we extract triples: ("SAP", "launched", "Joule") and ("Joule", "for", "Consultants"). Ideally, "Joule for Consultants" should be recognized as an named entity and merged as one token, and then it should be parsed as one direct object of the predicate "launched".
Report issue for preceding element
![Refer to caption](/html/2507.03226v3/new_Example.png) Figure 2: SpaCy Generated Parse Tree Report issue for preceding element
Algorithm [6](https://arxiv.org/html/2507.03226v3#footnote6 "footnote 6 ‣ Algorithm 1 ‣ 3.1.2 Dependency-Based Triple Extraction ‣ 3.1 Knowledge Graph Construction ‣ 3 Methodology ‣ Towards Practical GraphRAG: Efficient Knowledge Graph Construction and Hybrid Retrieval at Scale") formalizes our dependency extraction logic. We construct a custom SpaCy processing pipeline that incorporates:
Report issue for preceding element
  * •
Passive voice handling to normalize active/passive constructions
Report issue for preceding element
  * •
Phrasal merging to capture multi-token entities (e.g., "Supplier management")
Report issue for preceding element
  * •
Coreference resolution to map pronouns and mentions to canonical entities
Report issue for preceding element
  * •
Dependency triple extraction identifying subject-verb-object patterns
Report issue for preceding element
  * •
Linear extraction heuristics to capture relationships missed by dependency parsing
Report issue for preceding element


Algorithm 1 Dependency-Based Knowledge Graph Construction with Coreference666Notation: Bold denotes control flow keywords, SmallCaps denotes function calls, and typewriter denotes variables.
1nlp←BuildPipeline()\texttt{nlp}\leftarrow\textsc{BuildPipeline()}\pdfrefobj⊳\triangleright includes: customized tokenizer, passive & phrasal merges, entity merging, and coreference ++ span resolver 
2Entities←∅;Relations←∅\texttt{Entities}\leftarrow\emptyset;\ \texttt{Relations}\leftarrow\emptyset
3foreachtextinTextsdo
4doc←nlp(text)\texttt{doc}\leftarrow\texttt{nlp(text)}
5dep_triples←ExtractDependencyTriples(doc)\texttt{dep\\_triples}\leftarrow\textsc{ExtractDependencyTriples(doc)}
6linear_triples←LinearExtractor(doc)\texttt{linear\\_triples}\leftarrow\textsc{LinearExtractor(doc)}
7all_triples←dep_triples∪linear_triples\texttt{all\\_triples}\leftarrow\texttt{dep\\_triples}\cup\texttt{linear\\_triples}
8coref_map←BuildCorefMap(doc)\texttt{coref\\_map}\leftarrow\textsc{BuildCorefMap(doc)}
9resolved_triples←{(coref_map.get​(h,h),r,coref_map.get​(o,o))|(h,r,o)∈all_triples}\texttt{resolved\\_triples}\leftarrow\\{(\texttt{coref\\_map.get}(h,h),r,\texttt{coref\\_map.get}(o,o))\ |\ (h,r,o)\in\texttt{all\\_triples}\\}
10filtered_triples←{(Normalize(h),r,Normalize(o))|(h,r,o)∈resolved_triples,\texttt{filtered\\_triples}\leftarrow\\{(\textsc{Normalize}(h),r,\textsc{Normalize}(o))\ |\ (h,r,o)\in\texttt{resolved\\_triples},
11len(h)≥2∧len(o)≥2∧h.lower()∉WORD_FILTER∧o.lower()∉WORD_FILTER}\texttt{len}(h)\geq 2\wedge\texttt{len}(o)\geq 2\wedge h.\texttt{lower()}\notin\texttt{WORD\\_FILTER}\wedge o.\texttt{lower()}\notin\texttt{WORD\\_FILTER}\\}
12foreach(h,r,o)(h,r,o)infiltered_triplesdo
13Entities←Entities∪{(Id(h),name=h,type="Concept"),\texttt{Entities}\leftarrow\texttt{Entities}\cup\\{(\textsc{Id}(h),\ \textit{name}=h,\ \textit{type}=\text{"Concept"}),
14(Id(o),name=o,type="Concept")}(\textsc{Id}(o),\ \textit{name}=o,\ \textit{type}=\text{"Concept"})\\}
15confidence←ScoreRelation​(r,h,o)\texttt{confidence}\leftarrow\textsc{ScoreRelation}(r,h,o)\pdfrefobj⊳\triangleright optional heuristic 
16Relations←Relations∪{(head=h,relation=r,tail=o,confidence=confidence)}\texttt{Relations}\leftarrow\texttt{Relations}\cup\\{(\textit{head}=h,\ \textit{relation}=r,\ \textit{tail}=o,\ \textit{confidence}=\texttt{confidence})\\}
17endfor
18endfor
19returnEntities,Relations\texttt{Entities},\texttt{Relations}
Report issue for preceding element
For each document, we extract dependency-based and linear triples, resolve coreferences to canonical forms, and apply normalization, filtering short entities (<2<2 characters), removing stopwords, and standardizing entity names for graph DB compatibility. Each relation is assigned a confidence score based on syntactic features. A key advantage of this approach is domain agnosticism—the method requires no domain-specific training or customization, making it directly applicable across diverse enterprise contexts. As we demonstrate in Section [4](https://arxiv.org/html/2507.03226v3#S4 "4 Experiments ‣ Towards Practical GraphRAG: Efficient Knowledge Graph Construction and Hybrid Retrieval at Scale"), this dependency-based extraction achieves 94%94\% of LLM-based performance (61.87%61.87\% vs. 65.83%65.83\%) while processing documents orders of magnitude faster and at significantly lower cost.
Report issue for preceding element
####  3.1.3 LLM-Based Extraction
Report issue for preceding element
For critical document collections or text with complex ambiguity where maximum accuracy is required, our framework supports LLM-based extraction using GPT777https://platform.openai.com/docs/models family of models with few-shot prompting. Users can select extraction mode based on their cost-performance requirements and document characteristics, enabling practical deployment across varying enterprise scenarios.
Report issue for preceding element
####  3.1.4 Graph Storage
Report issue for preceding element
Extracted entities and relations are stored in a graph DB (i.e. iGraph [igraph]) with vector embeddings generated for each entity, chunk, and relation using OpenAI’s text-embedding-3-large888https://platform.openai.com/docs/models/text-embedding-3-large model. These embeddings enable hybrid retrieval that combines graph structure with semantic similarity, as described in Section [3.2](https://arxiv.org/html/2507.03226v3#S3.SS2 "3.2 Efficient Hybrid Graph Retrieval ‣ 3 Methodology ‣ Towards Practical GraphRAG: Efficient Knowledge Graph Construction and Hybrid Retrieval at Scale").
Report issue for preceding element
###  3.2 Efficient Hybrid Graph Retrieval
Report issue for preceding element
At query time, we employ a cascaded retrieval strategy that combines efficient graph traversal with vector-based ranking. First, we conduct a high-recall one-hop graph traversal to identify candidate nodes. Second, based on candidate nodes, we perform 1-hop traversal to retrieve neighbors to obtain subgraphs. Next, we apply a dense vector-based re-ranking step using embeddings and cosine similarity to refine the result set. The selected subgraph, along with relevant source text chunks and extracted query entities, is then passed to an LLM to generate response. Our retrieval approach aligns with the classical cascaded architecture in information retrieval (IR), where an initial recall-oriented stage (e.g., BM25 or dense vector search) is followed by a precision-oriented neural re-ranker [mogotsi2010christopher, nogueira2020passagererankingbert, adjali2024multi]. Our one-hop traversal effectively retrieves semantically related nodes while keeping the candidate set size tractable—crucial for scaling to large enterprise graphs.
Report issue for preceding element
Figure [3](https://arxiv.org/html/2507.03226v3#S3.F3 "Figure 3 ‣ 3.2 Efficient Hybrid Graph Retrieval ‣ 3 Methodology ‣ Towards Practical GraphRAG: Efficient Knowledge Graph Construction and Hybrid Retrieval at Scale") illustrates the major components in our indexing and retrieval pipeline. During indexing, the KG is stored in both vector DB and graph DB. For our experiments, we use the open-source library Milvus [2021milvus] for storing embeddings and high-performance iGraph to store the graph in memory. Milvus stores nodes, chunks and relation embeddings for fast similarity lookup at query time, and iGraph stores nodes and edges for fast traversal. The following sections describe the major components for the retrieval processes. Algorithm [2](https://arxiv.org/html/2507.03226v3#alg2 "Algorithm 2 ‣ 3.2 Efficient Hybrid Graph Retrieval ‣ 3 Methodology ‣ Towards Practical GraphRAG: Efficient Knowledge Graph Construction and Hybrid Retrieval at Scale") provides the complete retrieval procedure.
Report issue for preceding element
![Refer to caption](/html/2507.03226v3/x2.png) Figure 3: GraphRAG Retrieval Architecture Report issue for preceding element Algorithm 2 GraphRAG Hybrid Retrieval
1Eseed←NounPhraseExtraction​(Q)∪VectorSearch​(Q,𝒱,k=5)E_{\text{seed}}\leftarrow\textsc{NounPhraseExtraction}(Q)\cup\textsc{VectorSearch}(Q,\mathcal{V},k{=}5)\pdfrefobj⊳\triangleright Extract seed entities via noun phrases and top-5 vector similarity 
2R←∅;C​h←∅R\leftarrow\emptyset;\ Ch\leftarrow\emptyset
3foreacheeinEseedE_{\text{seed}}do
4v←ExactMatch​(e,G)v\leftarrow\textsc{ExactMatch}(e,G)\pdfrefobj⊳\triangleright Case-insensitive match in graph GG
5ifvv found then
6N←Get1HopNeighbors​(v,G)N\leftarrow\textsc{Get1HopNeighbors}(v,G)
7sampled←SampleRelations​(N,k)\texttt{sampled}\leftarrow\textsc{SampleRelations}(N,k)\pdfrefobj⊳\triangleright k=100k{=}100 for small/medium, k=200k{=}200 for large graphs 
8R←R∪sampled.relationsR\leftarrow R\cup\texttt{sampled.relations}
9C​h←C​h∪sampled.chunksCh\leftarrow Ch\cup\texttt{sampled.chunks}
10endif
11endfor
12Lgraph(c​h)←RankBySimilarity​(C​h,Q,𝒱)L_{\text{graph}}^{(ch)}\leftarrow\textsc{RankBySimilarity}(Ch,Q,\mathcal{V})\pdfrefobj⊳\triangleright Rank chunks by cosine similarity 
13Lgraph(r)←RankBySimilarity​(R,Q,𝒱)L_{\text{graph}}^{(r)}\leftarrow\textsc{RankBySimilarity}(R,Q,\mathcal{V})\pdfrefobj⊳\triangleright Rank relations by cosine similarity 
14Lvector←DenseVectorSearch​(Q,𝒱)L_{\text{vector}}\leftarrow\textsc{DenseVectorSearch}(Q,\mathcal{V})\pdfrefobj⊳\triangleright Pure vector search on all chunks 
15Lfused←RecipRankFusion​(Lgraph(c​h),Lvector,k=60)L_{\text{fused}}\leftarrow\textsc{RecipRankFusion}(L_{\text{graph}}^{(ch)},L_{\text{vector}},k{=}60)\pdfrefobj⊳\triangleright Hybrid fusion for chunks 
16C​htop-k←SelectTop​(Lfused,k)Ch_{\text{top-k}}\leftarrow\textsc{SelectTop}(L_{\text{fused}},k)
17Rtop-2k←SelectTop​(Lgraph(r),2​k)R_{\text{top-2k}}\leftarrow\textsc{SelectTop}(L_{\text{graph}}^{(r)},2k)
18𝒞←{C​htop-k,Rtop-2k,Eseed}\mathcal{C}\leftarrow\\{Ch_{\text{top-k}},R_{\text{top-2k}},E_{\text{seed}}\\}
19return𝒞\mathcal{C}
Report issue for preceding element
####  3.2.1 Query Entity Identification
Report issue for preceding element
In contrast to other GraphRAG methods [guo2025lightragsimplefastretrievalaugmented, jimenez2024hipporag, fastgraphrag2025] that solely rely on LLMs for entity identification, we employ an optimized variant of SpaCy’s noun phrase extractor we developed to efficiently pinpoint key concepts within the query. Additionally, we conduct a similarity search between the full query and node embeddings to retrieve the top-​k\text{top-}k, where k=5k=5 relevant nodes from the graph. The entities obtained from both approaches are then merged and used as seed nodes for relation extraction. We maintain separate vector embeddings for entities, chunks, and relations to enable multi-granular similarity matching during retrieval.
Report issue for preceding element
####  3.2.2 Graph Query Execution
Report issue for preceding element
Starting from seed query nodes, we use case insensitive exact match to query the graph for relevant relations. Once a node is matched with a query node, it performs 11-hop traversal of all neighbors and filtered by a neighbor controlling parameter r​a​n​d​o​m​_​k​_​r​e​l​a​t​i​o​n​srandom\\_k\\_relations. For small to medium size graph, r​a​n​d​o​m​_​k​_​r​e​l​a​t​i​o​n​s=100random\\_k\\_relations=100 is sufficient, for larger ones, we set the parameter to 200200 akin to Yasunaga et al [yasunaga2022deepbidirectionallanguageknowledgegraph]. This yields a candidate set of entity-to-entity relations and entity-to-chunk associations.
Report issue for preceding element
####  3.2.3 Relevance Ranking and Context Selection
Report issue for preceding element
Once the candidate relations are obtained through case insensitive exact match and graph traversal, they are split into two groups: entity-to-entity relations and entity-to-chunk relations. Both chunk and relation embeddings are retrieved from the vector DB, which are then used to compute cosine similarity with the query. Chunks and relations are then sorted by similarity scores, and top-​k\text{top-}k chunks and top-​k∗2\text{top-}k*2 relations are returned. In selecting top-​k\text{top-}k chunks, our GraphRAG approach employs RRF to combine results from dense vector search and 1-hop graph traversal, balancing semantic similarity with structural entity relationships for improved context selection. This hybrid strategy balances structural relationships captured by the graph with semantic understanding from embeddings.
Report issue for preceding element
####  3.2.4 Context Integration with LLM
Report issue for preceding element
Once the top-​k\text{top-}k chunks and top-​k∗2\text{top-}k*2 relations are produced, we send them along with query entities as the context for LLM to consume and generate answers. Context is a dictionary with three keys: C​o​n​t​e​x​t={”​c​h​u​n​k​s​”:c​h​u​n​k​_​l​i​s​t,”​r​e​l​a​t​i​o​n​s​”:r​e​l​a​t​i​o​n​_​l​i​s​t,”​e​n​t​i​t​y​”:e​n​t​i​t​y​_​l​i​s​t}Context=\\{"chunks":chunk\\_list,"relations":relation\\_list,"entity":entity\\_list\\}, which provides a much richer context than standard RAG alone.
Report issue for preceding element
##  4 Experiments
Report issue for preceding element
###  4.1 Datasets
Report issue for preceding element
We evaluate our framework on Custom Code Migration (CCM) 999Custom code migration is the process of identifying, analyzing, updating, and transferring custom-built ABAP components from an old system to a new one., a real-world enterprise use-case requiring technical understanding of ABAP code migration and system evolution.
Report issue for preceding element
CCM resource corpus consists of 550550 PDF documents, including Cookbooks and Notes related to ABAP code migration. These documents are preprocessed into approximately 20002000 text chunks, each with a length of 20482048 characters and an overlap of 200200 characters. This processed corpus serves as the foundation for both KG construction and dense vector representation in our experiments.
Report issue for preceding element
Two test datasets are designed to evaluate different aspects of the system. CCM Chat includes 150150 question-answer pairs focused on code migration topics, including error analysis, implementation differences, and best practices for transitioning from legacy to S/4HANA systems. CCM Code Proposal comprises 200200 legacy code examples, each containing the legacy code alongside the migrated version.
Report issue for preceding element
Using the CCM resource corpus, our method yields a KG with 3915539155 nodes, 4761347613 entity-to-entity relations, 6368163681 entity-to-chunk relation, resulting in an average node degree of 1.521.52 and a highest degree of 236236. This relatively sparse structure reflects the technical, domain-specific nature of the corpus while maintaining sufficient connectivity for effective graph traversal.
Report issue for preceding element
###  4.2 Evaluation Methodology
Report issue for preceding element
####  4.2.1 CCM Chat Evaluation
Report issue for preceding element
We employ two complementary evaluation techniques:  (i) Semantic Alignment Scoreand  (ii) RAGAS Score.
Report issue for preceding element
Semantic Alignment Score uses an LLM-based classifier to compare the generated response against a reference (ground truth) answer. The LLM is prompted to assign a discrete semantic coverage score:  (i) 0if the answer fails to cover any part of the ground truth,  (ii) 0.50.5if it partially captures key information, and  (iii) 11if it fully aligns with the reference answer.  An overall performance metric is computed as a weighted average:
Report issue for preceding element  
|   | Semantic Alignment Score=(0.5×P0.5+1.0×P1.0)×100%\text{Semantic Alignment Score}=(0.5\times P_{0.5}+1.0\times P_{1.0})\times 100\%  |   |  
| --- | --- | --- |  
where P0.5P_{0.5} and P1.0P_{1.0} represent the proportions of responses assigned scores of 0.50.5 and 1.01.0, respectively. This metric provides a nuanced assessment that accounts for partial correctness, common in technical question answering where responses may capture some but not all relevant information.
Report issue for preceding element
RAGAS Score [es2025ragasautomatedevaluationretrieval] assesses both the retrieval quality and generative accuracy using three metrics:  (i) Context Precision, which measures the proportion of retrieved chunks that are relevant to the question;  (ii) Faithfulness, which quantifies how much of the generated answer is grounded in the retrieved content; and  (iii) Answer Relevancy, which evaluates how directly the generated response addresses the original query. This is computed by generating follow-up questions based on the response and comparing their cosine similarity to the original query—a higher similarity indicates stronger relevance.
Report issue for preceding element
####  4.2.2 CCM Code Proposal Evaluation
Report issue for preceding element
We adopt an LLM-as-a-Judge framework to systematically compare generated migration code with ground truth. The evaluation uses a structured two-stage prompt design:  (i) a system prompt that defines the evaluation task, instructing the judge to compare dense vector and graph-based generated code against human-created ground truth across five technical dimensions (as listed below), and  (ii) a user prompt that provides all four code inputs (legacy code, ground truth, dense vector output, graph output) and requests structured output.  Each evaluation instance includes the original legacy code, the reference migrated version created by human experts, and two system-generated outputs—one produced using dense vector retrieval and the other via graph-based retrieval. The judge outputs both a winner selection and detailed scoring breakdowns in JSON format as shown in101010Complete evaluation prompts and code examples are available in our code repository at <https://anonymous.4open.science/r/graphrag-pakdd2026-evaluation-3FBC> (anonymized for review)..
Report issue for preceding element
Evaluation proceeds in two stages:  (i) Pairwise Comparison, where the LLM selects the more accurate candidate based on similarity to the ground truth; and  (ii) Rubric Scoring, where each output is rated (1-5 scale) across five criteria: Syntax Correctness, Logical Correctness, S/4HANA Compatibility, Optimization and Efficiency, and Readability .
Report issue for preceding element
###  4.3 Results and Analysis
Report issue for preceding element
####  4.3.1 System Performance Result On CCM Chat
Report issue for preceding element
In Table [1](https://arxiv.org/html/2507.03226v3#S4.T1 "Table 1 ‣ 4.3.1 System Performance Result On CCM Chat ‣ 4.3 Results and Analysis ‣ 4 Experiments ‣ Towards Practical GraphRAG: Efficient Knowledge Graph Construction and Hybrid Retrieval at Scale") and Table [2](https://arxiv.org/html/2507.03226v3#S4.T2 "Table 2 ‣ 4.3.1 System Performance Result On CCM Chat ‣ 4.3 Results and Analysis ‣ 4 Experiments ‣ Towards Practical GraphRAG: Efficient Knowledge Graph Construction and Hybrid Retrieval at Scale"), both variants of GraphRAG, one using GPT-4o and the other using dependency graph as triplet creation model, show at least 12%12\% improvement in context precision score compared to dense vector retrieval. In terms of semantic alignment (abbreviated as No Cov., Partial Cov., and Full Cov. in Table [2](https://arxiv.org/html/2507.03226v3#S4.T2 "Table 2 ‣ 4.3.1 System Performance Result On CCM Chat ‣ 4.3 Results and Analysis ‣ 4 Experiments ‣ Towards Practical GraphRAG: Efficient Knowledge Graph Construction and Hybrid Retrieval at Scale")), the No Cov. rate is reduced by 32%32\% for both variants, while the Full Cov. (complete alignment with ground truth) rate increases by at least 19%19\%. Table [2](https://arxiv.org/html/2507.03226v3#S4.T2 "Table 2 ‣ 4.3.1 System Performance Result On CCM Chat ‣ 4.3 Results and Analysis ‣ 4 Experiments ‣ Towards Practical GraphRAG: Efficient Knowledge Graph Construction and Hybrid Retrieval at Scale") shows that both GraphRAG variants substantially improve answer completeness, with weighted averages of 65.83%65.83\% and 61.87%61.87\% compared to 50.80%50.80\% for dense retrieval. This improvement primarily stems from increased full-coverage responses (58.99%58.99\% and 51.08%51.08\% vs. 42.88%42.88\%) and reduced no-coverage failures (27.34%27.34\% vs. 40.29%40.29\%), demonstrating that graph-structured retrieval better captures complete entity-grounded context for technical queries.
Report issue for preceding element
Notably, the dependency graph-based GraphRAG model retains 94%94\% of the GPT-4o variant’s performance in context precision. It achieves comparable results in No Cov. and reaches 86.6%86.6\% of the GPT-4o variant’s performance in Full Cov. highlighting its strong performance with a lighter KG construction pipeline.
Report issue for preceding element
Table 1: RAGAS evaluation on CCM chat  
| Method  |  Context Precision  | Faithfulness  |  Answer Relevancy  | Avg.  |  
| --- | --- | --- | --- | --- |  
|  Dense Vector (ada-002)  | 54.35%  | 77.18%  | 82.92%  | 71.48%  |  
|  GraphRAG (GPT-4o)  | 63.82%  | 74.24%  | 89.43%  | 75.83%  |  
| GraphRAG (Dependency)  | 61.07%  | 72.76%  | 90.97%  | 74.93%  |  
Report issue for preceding element Table 2: Semantic Alignment evaluation on CCM chat  
| Method  |  No Cov. (0)  |  Partial Cov. (0.5)  |  Full Cov. (1)  |  Weighted Avg.  |  
| --- | --- | --- | --- | --- |  
|  Dense Vector (ada-002)  | 40.29%  | 15.85%  | 42.88%  | 50.80%  |  
|  GraphRAG (GPT-4o)  | 27.34%  | 13.67%  | 58.99%  | 65.83%  |  
| GraphRAG (Dependency)  | 27.34%  | 21.58%  | 51.08%  | 61.87%  |  
Report issue for preceding element
####  4.3.2 System Performance Result on CCM Code Proposal
Report issue for preceding element
In Table [3](https://arxiv.org/html/2507.03226v3#S4.T3 "Table 3 ‣ 4.3.2 System Performance Result on CCM Code Proposal ‣ 4.3 Results and Analysis ‣ 4 Experiments ‣ Towards Practical GraphRAG: Efficient Knowledge Graph Construction and Hybrid Retrieval at Scale") and Table [4](https://arxiv.org/html/2507.03226v3#S4.T4 "Table 4 ‣ 4.3.2 System Performance Result on CCM Code Proposal ‣ 4.3 Results and Analysis ‣ 4 Experiments ‣ Towards Practical GraphRAG: Efficient Knowledge Graph Construction and Hybrid Retrieval at Scale") on CCM Code Proposal dataset, both GraphRAG variants outperform dense retrieval in terms of winning rate and average score, where average score measures an average across all five evaluation criteria and winning rate is defined as the ratio of cases in which a model’s response is preferred over the baseline according to the LLM-as-a-Judge assessment. The GraphRAG system leveraging dependency parsing achieves performance on par with GPT-4o variant, indicating that dependency graph-based GraphRAG is a strong alternative to LLM-based triplet extraction in retrieval tasks on this dataset.
Report issue for preceding element
Table 3: LLM-as-a-Judge on CCM Code Proposal (GPT-4o-based)  
| Method  |  Winning Rate  |  Avg. Score (1–5)  |  
| --- | --- | --- |  
|  Dense Vector (ada-002)  | 23%  | 3.48  |  
| GraphRAG (GPT-4o)  | 77%  | 4.04  |  
Report issue for preceding element Table 4: LLM-as-a-Judge on CCM Code Proposal (Dependency Graph-based)  
| Method  |  Winning Rate  |  Avg. Score (1–5)  |  
| --- | --- | --- |  
|  Dense Vector (ada-002)  | 21.5%  | 3.43  |  
| GraphRAG (Dependency)  | 78.5%  | 4.03  |  
Report issue for preceding element
####  4.3.3 Qualitative Insight
Report issue for preceding element
Our method is effective in retrieving content tied to key entities. For example, in CCM chat, given question "How do I handle custom code that references VBBS111111VBBS is a legacy database table that stores summarized sales requirement totals. after the S/4HANA conversion?", dense retriever fails to extract content that specifically address VBBS table. In contrast, GraphRAG selects content explicitly mentioning "VBBS" and includes relevance sentences: “… If the VBBS is used in customer code, … The solution is to create a view on VBBE 121212VBBE is a database table that stores individual, detailed sales requirments for Material Requirements Planning (MRP).”. This illustrates our system’s strength in extracting semantically focused context.
Report issue for preceding element
In CCM Code Proposal, GraphRAG exhibits structured multi-entity reasoning that dense retrieval lacks. Dense vector retrieval correctly updates the transaction code but fails to migrate the corresponding screen references, retaining the obsolete SAPMM03S/RM03S structures that cause runtime errors in S/4HANA. GraphRAG, by traversing entity relationships in the KG (linking transactions to their required screen structures), correctly identifies that MSC3N requires SAPLMGMM/RMMG1 and performs complete migration of both components. Please refer to prompts and evaluation samples131313Complete evaluation prompts and code examples: <https://anonymous.4open.science/r/graphrag-pakdd2026-evaluation-3FBC> for more details.
Report issue for preceding element
##  5 Conclusion, Limitation and Future Work
Report issue for preceding element
In this work, we present a scalable method for constructing enterprise-grade graph-based GraphRAG systems from unstructured text. To address key scalability challenges in real-world enterprise environments, our approach centers on two core components:  (i) KG construction using efficient dependency parsing to complement LLM-based approach, and  (ii) lightweight, hybrid subgraph retrieval to ensure low-latency query-time performance.  We validate our framework on two use cases, CCM Chat and CCM Code Proposal, and observe consistent performance improvements over a baseline RAG system. Notably, KGs generated using a robust, open-source dependency parser achieved performance comparable to GPT-4o, as measured by both LLM-as-a-Judge and RAGAS evaluation metrics.
Report issue for preceding element
Our approach offers a promising path for scaling GraphRAG systems by alleviating the bottleneck of sole dependence on LLMs for KG construction. Nevertheless, two limitations warrant future investigation. First, while dependency parsing provides a lightweight and scalable method for extracting knowledge triples, it may miss context-dependent or implicit relations not directly expressed in surface syntax. Second, although our method demonstrates strong performance in code migration domain, its generalizability to other settings remains an open question. Future work includes evaluating the approach on broader public benchmarks such as HotpotQA to assess its applicability beyond enterprise use cases. Additionally, investigating advanced graph traversal strategies beyond one-hop and integrating with recent query-time optimizations like SubGCache represent promising directions for further improving retrieval efficiency.
Report issue for preceding element
##  6 GenAI Usage Disclosure
Report issue for preceding element
We employed ChatGPT and Claude to assist in rephrasing certain sections of the paper for improved clarity. All core content, including research design, data analysis, and result interpretation, was conducted without the aid of generative AI tools.
Report issue for preceding element
Report Issue
##### Report GitHub Issue
Title:
Content selection saved. Describe the issue below:
Description:
Submit without GitHubSubmit in GitHub
Report Issue for Selection
Generated by [ L A T E xml ![\[LOGO\]](/html/2507.03226v3/) ](https://math.nist.gov/~BMiller/LaTeXML/)
## Instructions for reporting errors
We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:
  * Click the "Report Issue" button.
  * Open a report feedback form via keyboard, use "**Ctrl + ?** ".
  * Make a text selection and click the "Report Issue for Selection" button near your cursor.
  * You can use Alt+Y to toggle on and Alt+Shift+Y to toggle off accessible reporting links at each section.


Our team has already identified [the following issues](https://github.com/arXiv/html_feedback/issues). We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.
Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a [list of packages that need conversion](https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML), and welcome [developer contributions](https://github.com/brucemiller/LaTeXML/issues).

