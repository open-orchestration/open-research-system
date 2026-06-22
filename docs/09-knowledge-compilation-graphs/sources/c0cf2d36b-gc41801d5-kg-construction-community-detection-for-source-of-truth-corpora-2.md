[ ![logo](https://services.dev.arxiv.org/html/static/arxiv-logomark-small-white.svg) Back to arXiv ](https://arxiv.org/)
[ ](https://arxiv.org/abs/2408.08535v1) [ ](javascript:toggleColorScheme\(\) "Toggle dark/light mode")
[ ![logo](https://services.dev.arxiv.org/html/static/arxiv-logo-one-color-white.svg) Back to arXiv ](https://arxiv.org/)
This is **experimental HTML** to improve accessibility. We invite you to report rendering errors. Use Alt+Y to toggle on accessible reporting links and Alt+Shift+Y to toggle off. Learn more [about this project](https://info.arxiv.org/about/accessible_HTML.html) and [help improve conversions](https://info.arxiv.org/help/submit_latex_best_practices.html). 
[Why HTML?](https://info.arxiv.org/about/accessible_HTML.html) [Report Issue](/html/2408.08535v1/#myForm) [Back to Abstract](https://arxiv.org/abs/2408.08535v1) [Download PDF](https://arxiv.org/pdf/2408.08535v1) [ ](javascript:toggleColorScheme\(\) "Toggle dark/light mode")
## Table of Contents
  1. [ Abstract  ](https://arxiv.org/html/2408.08535v1#abstract "Abstract")
  2. [1 Introduction](https://arxiv.org/html/2408.08535v1#S1 "In CommunityKG-RAG: Leveraging Community Structures in Knowledge Graphs for Advanced Retrieval-Augmented Generation in Fact-Checking")
  3. [2 Related Work](https://arxiv.org/html/2408.08535v1#S2 "In CommunityKG-RAG: Leveraging Community Structures in Knowledge Graphs for Advanced Retrieval-Augmented Generation in Fact-Checking")
  4. [3 Problem Statement](https://arxiv.org/html/2408.08535v1#S3 "In CommunityKG-RAG: Leveraging Community Structures in Knowledge Graphs for Advanced Retrieval-Augmented Generation in Fact-Checking")
  5. [4 CommunityKG-RAG](https://arxiv.org/html/2408.08535v1#S4 "In CommunityKG-RAG: Leveraging Community Structures in Knowledge Graphs for Advanced Retrieval-Augmented Generation in Fact-Checking")
    1. [4.1 Knowledge Graph Construction](https://arxiv.org/html/2408.08535v1#S4.SS1 "In 4 CommunityKG-RAG ‣ CommunityKG-RAG: Leveraging Community Structures in Knowledge Graphs for Advanced Retrieval-Augmented Generation in Fact-Checking")
      1. [4.1.1 Coreference Resolution](https://arxiv.org/html/2408.08535v1#S4.SS1.SSS1 "In 4.1 Knowledge Graph Construction ‣ 4 CommunityKG-RAG ‣ CommunityKG-RAG: Leveraging Community Structures in Knowledge Graphs for Advanced Retrieval-Augmented Generation in Fact-Checking")
      2. [4.1.2 Graph Construction](https://arxiv.org/html/2408.08535v1#S4.SS1.SSS2 "In 4.1 Knowledge Graph Construction ‣ 4 CommunityKG-RAG ‣ CommunityKG-RAG: Leveraging Community Structures in Knowledge Graphs for Advanced Retrieval-Augmented Generation in Fact-Checking")
      3. [4.1.3 Node Feature Embedding](https://arxiv.org/html/2408.08535v1#S4.SS1.SSS3 "In 4.1 Knowledge Graph Construction ‣ 4 CommunityKG-RAG ‣ CommunityKG-RAG: Leveraging Community Structures in Knowledge Graphs for Advanced Retrieval-Augmented Generation in Fact-Checking")
    2. [4.2 Community Detection](https://arxiv.org/html/2408.08535v1#S4.SS2 "In 4 CommunityKG-RAG ‣ CommunityKG-RAG: Leveraging Community Structures in Knowledge Graphs for Advanced Retrieval-Augmented Generation in Fact-Checking")
    3. [4.3 Community Retrieval](https://arxiv.org/html/2408.08535v1#S4.SS3 "In 4 CommunityKG-RAG ‣ CommunityKG-RAG: Leveraging Community Structures in Knowledge Graphs for Advanced Retrieval-Augmented Generation in Fact-Checking")
    4. [4.4 Top Community Selection](https://arxiv.org/html/2408.08535v1#S4.SS4 "In 4 CommunityKG-RAG ‣ CommunityKG-RAG: Leveraging Community Structures in Knowledge Graphs for Advanced Retrieval-Augmented Generation in Fact-Checking")
    5. [4.5 Top Community-to-Sentence Selection](https://arxiv.org/html/2408.08535v1#S4.SS5 "In 4 CommunityKG-RAG ‣ CommunityKG-RAG: Leveraging Community Structures in Knowledge Graphs for Advanced Retrieval-Augmented Generation in Fact-Checking")
  6. [5 Experimental Details](https://arxiv.org/html/2408.08535v1#S5 "In CommunityKG-RAG: Leveraging Community Structures in Knowledge Graphs for Advanced Retrieval-Augmented Generation in Fact-Checking")
    1. [5.1 Datasets](https://arxiv.org/html/2408.08535v1#S5.SS1 "In 5 Experimental Details ‣ CommunityKG-RAG: Leveraging Community Structures in Knowledge Graphs for Advanced Retrieval-Augmented Generation in Fact-Checking")
    2. [5.2 Baselines](https://arxiv.org/html/2408.08535v1#S5.SS2 "In 5 Experimental Details ‣ CommunityKG-RAG: Leveraging Community Structures in Knowledge Graphs for Advanced Retrieval-Augmented Generation in Fact-Checking")
    3. [5.3 Implementation Details](https://arxiv.org/html/2408.08535v1#S5.SS3 "In 5 Experimental Details ‣ CommunityKG-RAG: Leveraging Community Structures in Knowledge Graphs for Advanced Retrieval-Augmented Generation in Fact-Checking")
  7. [6 Results](https://arxiv.org/html/2408.08535v1#S6 "In CommunityKG-RAG: Leveraging Community Structures in Knowledge Graphs for Advanced Retrieval-Augmented Generation in Fact-Checking")
    1. [6.1 Main Results](https://arxiv.org/html/2408.08535v1#S6.SS1 "In 6 Results ‣ CommunityKG-RAG: Leveraging Community Structures in Knowledge Graphs for Advanced Retrieval-Augmented Generation in Fact-Checking")
    2. [6.2 Ablation](https://arxiv.org/html/2408.08535v1#S6.SS2 "In 6 Results ‣ CommunityKG-RAG: Leveraging Community Structures in Knowledge Graphs for Advanced Retrieval-Augmented Generation in Fact-Checking")
      1. [6.2.1 Performance With Different Backbone Models](https://arxiv.org/html/2408.08535v1#S6.SS2.SSS1 "In 6.2 Ablation ‣ 6 Results ‣ CommunityKG-RAG: Leveraging Community Structures in Knowledge Graphs for Advanced Retrieval-Augmented Generation in Fact-Checking")
      2. [6.2.2 Influence of Community-to-Sentence Selection](https://arxiv.org/html/2408.08535v1#S6.SS2.SSS2 "In 6.2 Ablation ‣ 6 Results ‣ CommunityKG-RAG: Leveraging Community Structures in Knowledge Graphs for Advanced Retrieval-Augmented Generation in Fact-Checking")
      3. [6.2.3 Combined Effects of Top Community and Community-to-Sentence Selection](https://arxiv.org/html/2408.08535v1#S6.SS2.SSS3 "In 6.2 Ablation ‣ 6 Results ‣ CommunityKG-RAG: Leveraging Community Structures in Knowledge Graphs for Advanced Retrieval-Augmented Generation in Fact-Checking")
  8. [7 Conclusion](https://arxiv.org/html/2408.08535v1#S7 "In CommunityKG-RAG: Leveraging Community Structures in Knowledge Graphs for Advanced Retrieval-Augmented Generation in Fact-Checking")
  9. [8 Limitations](https://arxiv.org/html/2408.08535v1#S8 "In CommunityKG-RAG: Leveraging Community Structures in Knowledge Graphs for Advanced Retrieval-Augmented Generation in Fact-Checking")
    1. [8.1 Computational Demands](https://arxiv.org/html/2408.08535v1#S8.SS1 "In 8 Limitations ‣ CommunityKG-RAG: Leveraging Community Structures in Knowledge Graphs for Advanced Retrieval-Augmented Generation in Fact-Checking")
    2. [8.2 Dependency on Entity Recognition Quality](https://arxiv.org/html/2408.08535v1#S8.SS2 "In 8 Limitations ‣ CommunityKG-RAG: Leveraging Community Structures in Knowledge Graphs for Advanced Retrieval-Augmented Generation in Fact-Checking")
  10. [A Details of Datasets](https://arxiv.org/html/2408.08535v1#A1 "In CommunityKG-RAG: Leveraging Community Structures in Knowledge Graphs for Advanced Retrieval-Augmented Generation in Fact-Checking")
  11. [B Prompt](https://arxiv.org/html/2408.08535v1#A2 "In CommunityKG-RAG: Leveraging Community Structures in Knowledge Graphs for Advanced Retrieval-Augmented Generation in Fact-Checking")
  12. [C Language Model Parameters](https://arxiv.org/html/2408.08535v1#A3 "In CommunityKG-RAG: Leveraging Community Structures in Knowledge Graphs for Advanced Retrieval-Augmented Generation in Fact-Checking")
  13. [D Computing Infrastructure](https://arxiv.org/html/2408.08535v1#A4 "In CommunityKG-RAG: Leveraging Community Structures in Knowledge Graphs for Advanced Retrieval-Augmented Generation in Fact-Checking")
  14. [E Community Statistics](https://arxiv.org/html/2408.08535v1#A5 "In CommunityKG-RAG: Leveraging Community Structures in Knowledge Graphs for Advanced Retrieval-Augmented Generation in Fact-Checking")
  15. [ References  ](https://arxiv.org/html/2408.08535v1#bib "References")


HTML conversions [sometimes display errors](https://info.dev.arxiv.org/about/accessibility_html_error_messages.html) due to content that did not convert correctly from the source. This paper uses the following packages that are not yet supported by the HTML conversion tool. Feedback on these issues are not necessary; they are known and are being worked on.
  * failed: inconsolata


Authors: achieve the best HTML results from your LaTeX submissions by following these [best practices](https://info.arxiv.org/help/submit_latex_best_practices.html).
[License: CC BY 4.0](https://info.arxiv.org/help/license/index.html#licenses-available)
arXiv:2408.08535v1 [cs.CL] 16 Aug 2024
# CommunityKG-RAG: Leveraging Community Structures in Knowledge Graphs for Advanced Retrieval-Augmented Generation in Fact-Checking
Report issue for preceding element
Rong-Ching Chang   
Department of Computer Science   
University of California, Davis   
Davis, CA   
rocchang@ucdavis.edu   
&Jiawei Zhang   
Department of Computer Science   
University of California, Davis   
Davis, CA   
jiawei@ifmlab.org   

Report issue for preceding element
###### Abstract
Report issue for preceding element
Despite advancements in Large Language Models (LLMs) and Retrieval-Augmented Generation (RAG) systems, their effectiveness is often hindered by a lack of integration with entity relationships and community structures, limiting their ability to provide contextually rich and accurate information retrieval for fact-checking. We introduce CommunityKG-RAG (Community Knowledge Graph-Retrieval Augmented Generation), a novel zero-shot framework that integrates community structures within Knowledge Graphs (KGs) with RAG systems to enhance the fact-checking process. Capable of adapting to new domains and queries without additional training, CommunityKG-RAG utilizes the multi-hop nature of community structures within KGs to significantly improve the accuracy and relevance of information retrieval. Our experimental results demonstrate that CommunityKG-RAG outperforms traditional methods, representing a significant advancement in fact-checking by offering a robust, scalable, and efficient solution.
Report issue for preceding element
##  1 Introduction
Report issue for preceding element
The occurrence of misinformation and the imperative of fact-checking are pivotal elements within the digital information ecosystem, profoundly affecting public discourse and shaping societal decisions worldwide. Concurrently, the advent of Large Language Models (LLMs) has unveiled remarkable capabilities in comprehending and producing human languages, presenting a promising avenue for bolstering fact-checking endeavors. Prior research Buchholz ([2023](https://arxiv.org/html/2408.08535v1#bib.bib4)); Li et al. ([2023b](https://arxiv.org/html/2408.08535v1#bib.bib19)); Caramancion ([2023](https://arxiv.org/html/2408.08535v1#bib.bib6)); Hoes et al. ([2023](https://arxiv.org/html/2408.08535v1#bib.bib10)); Huang and Sun ([2023](https://arxiv.org/html/2408.08535v1#bib.bib13)) has delved into directly prompting LLM models to identify false information. However, while LLMs can be instrumental in combating misinformation, their practical application still exposes two critical limitations. Firstly, these models are constrained by the cut-off date of their training data. Secondly, this issue is compounded by the tendency of LLMs to generate incorrect information or “hallucinations” Huang et al. ([2023](https://arxiv.org/html/2408.08535v1#bib.bib12)) which could jeopardize the accuracy of claim verification in fact-checking tasks.
Report issue for preceding element
In response to these challenges, Retrieval-Augmented Generation (RAG) has emerged as a promising approach. By integrating the generative capabilities of LLMs with external data retrieval, RAG significantly enhances the accuracy and relevance of the responses. For instance, Liao et al. ([2023](https://arxiv.org/html/2408.08535v1#bib.bib20)) leverages RAG by employing both the dot product and the BERT-based sequence tagging model to identify key evidences. Soleimani et al. ([2019](https://arxiv.org/html/2408.08535v1#bib.bib29)) uses the BERT model to retrieve and validate claims.
Report issue for preceding element
While RAG significantly advances the capabilities of LLMs, it, too, faces unique challenges. Firstly, language models suffer from utilizing contexts in long texts. When crucial information is located in the middle, it is less likely to be effectively utilized by language models Liu et al. ([2023](https://arxiv.org/html/2408.08535v1#bib.bib21)). Secondly, when contexts are laden with noise or contradictory information, RAG’s performance can be adversely underscored Barnett et al. ([2024](https://arxiv.org/html/2408.08535v1#bib.bib2)). Thirdly, the retrieval process plays a crucial role. Often, even if the answer to a query is present in the document corpus, it may not rank highly enough to be returned to the user Barnett et al. ([2024](https://arxiv.org/html/2408.08535v1#bib.bib2)). Further expanding on the challenges in RAG systems, knowledge retrieved by these systems does not always contribute positively Wang et al. ([2023](https://arxiv.org/html/2408.08535v1#bib.bib33)) and can sometimes detrimentally impact the original responses generated by the LLMs.
Report issue for preceding element
Acknowledging the challenges inherent in RAG systems, Knowledge Graphs (KGs) offer a structured, semantically rich framework that has a long-standing history of enhancing fact-checking efforts. KGs play a crucial role in encapsulating and organizing complex information through their inherent structure which is comprised of triples. Each triple, consisting of a subject, predicate, and object — alternatively framed as a head entity, a relation, and a tail entity i.e., (subject entity, relationship, object entity) — constitutes the core component of a KG, enabling it to represent structural facts and support symbolic reasoning effectively.
Report issue for preceding element
KGs represent data in a way that captures information about not just the entities but also the complex relationships between them. This semantic web of information allows for a deeper understanding of context, which is essential for verifying facts. Furthermore, KGs facilitate the exploration of multi-hop information pathways, allowing for the elucidation of intricate and indirect relationships critical for comprehensive fact verification. Prior work has shown promising results utilizing KGs Hu et al. ([2023](https://arxiv.org/html/2408.08535v1#bib.bib11)); Liu et al. ([2020b](https://arxiv.org/html/2408.08535v1#bib.bib23)); Ma et al. ([2023](https://arxiv.org/html/2408.08535v1#bib.bib24)). However, concurrently integrating both the structured knowledge graphs with unstructured text as inputs to LLMs is not a trivial enterprise. Prior work has tried directly including triples as input to LLMs Baek et al. ([2023](https://arxiv.org/html/2408.08535v1#bib.bib1)); Sequeda et al. ([2023](https://arxiv.org/html/2408.08535v1#bib.bib28)). Yet LLMs are not trained for leveraging triples, and this approach does not leverage the community and entity relationship. Other approaches Sun et al. ([2021](https://arxiv.org/html/2408.08535v1#bib.bib31)); Liu et al. ([2020a](https://arxiv.org/html/2408.08535v1#bib.bib22)); Yasunaga et al. ([2022](https://arxiv.org/html/2408.08535v1#bib.bib34)); Sun et al. ([2020](https://arxiv.org/html/2408.08535v1#bib.bib30)); Zhang et al. ([2022](https://arxiv.org/html/2408.08535v1#bib.bib35)); Kang et al. ([2023](https://arxiv.org/html/2408.08535v1#bib.bib15)) require training customized models or joint embeddings that are computationally expensive.
Report issue for preceding element
In light of the distinct advantages of KGs and the capabilities of RAG systems and LLMs, the absence of research on their combined application for fact-checking is notable. Although such integration —— melding KGs’ structured, semantic insights with RAG’s dynamic retrieval and LLMs’ language comprehension —— holds significant promise for advancing fact-checking technologies, the specific impact of this synergistic approach remains largely unexplored.
Report issue for preceding element
To bridge the existing research gap, we introduce a pioneering framework: CommunityKG-RAG (Community Knowledge Graph-Retrieval Augmented Generation). This innovative approach synergizes Knowledge Graphs with Retrieval-Augmented Generation and Large Language Models to enhance fact-checking capabilities. By leveraging and preserving the intricate entity relationships and community structures within KGs, our framework provides a contextually enriched and semantically aware retrieval mechanism that significantly improves the accuracy and relevance of generated responses. Specifically, we construct a comprehensive KG from fact-checking articles, employ the Louvain algorithm for community detection, and assign embeddings derived from word embeddings to each node. This approach ensures that the identified communities are both structurally coherent within the KG and highly pertinent to the fact-checking task. By harnessing this integrated framework, we offer a robust, scalable, and efficient solution to contemporary fact-checking challenges. An example of this integration and its impact on retrieval accuracy is illustrated in Figure [1](https://arxiv.org/html/2408.08535v1#S1.F1 "Figure 1 ‣ 1 Introduction ‣ CommunityKG-RAG: Leveraging Community Structures in Knowledge Graphs for Advanced Retrieval-Augmented Generation in Fact-Checking").
Report issue for preceding element
![Refer to caption](/html/2408.08535v1/x1.png) Figure 1: Comparison between no retrieval, semantic retrieval, and CommunityKG-RAG. The no retrieval and semantic retrieval fail to provide sufficient context, while our proposed method, CommunityKG-RAG, is able to by leveraging multi-hop knowledge graph information in the retrieval process enhancing accuracy and relevance. Report issue for preceding element
Our contributions are threefold:
Report issue for preceding element
  1. 1.
Utilization of Both Structured and Unstructured Data with Superior Knowledge Graph Integration: By combining the structured data of Knowledge Graphs with the unstructured data handled by LLMs, we achieve a more comprehensive and context-aware fact-checking system. We demonstrate that converting knowledge graphs back to sentences within our framework is superior to methods that use triples as context. This approach enhances the comprehensibility and relevance of the retrieved information, as demonstrated by the significant increase in accuracy.
Report issue for preceding element
  2. 2.
Context-Aware Retrieval and Multi-hop Utilization: By leveraging community structures and multi-hop paths within KGs, the framework delivers more precise and relevant information retrieval, enhancing the overall effectiveness of the fact-checking process. We are the first work to propose utilizing and combining multi-hop in KGs with RAG systems. 
Report issue for preceding element
  3. 3.
Scalability and Efficiency: The framework operates in a zero-shot manner, requiring no additional training or fine-tuning, which ensures high scalability and adaptability to various LLMs. Additionally, the knowledge graph and community detection processes only need to be performed once, allowing for repeated reuse or rapid updates.
Report issue for preceding element


##  2 Related Work
Report issue for preceding element
KGs in LLM inputs
Report issue for preceding element
Recent research has explored the integration of KGs with LLMs, where triples are directly fed into LLMs as input Baek et al. ([2023](https://arxiv.org/html/2408.08535v1#bib.bib1)); Sequeda et al. ([2023](https://arxiv.org/html/2408.08535v1#bib.bib28)). However, this approach has its limitations, particularly in its assumption that LLMs can effectively process and utilize triples despite their primary training focus on sequential data processing. This could result in an underutilization of KG’s structural information, such as subgraph structure, community structure, and relationship patterns across entities and relations of Knowledge Graphs. Addressing this, our proposed method leverages community detection results as indices for text retrieval, thus harnessing the subgraph and entity relationship structures inherent in KGs more effectively than in previous work. 
Report issue for preceding element
Other approaches to integrating knowledge graphs with language models include joint embedding training or the customization of model architectures. This can be done by representing triplets as a sequence of tokens and concatenating them with text embedding in the pre-training stage Sun et al. ([2021](https://arxiv.org/html/2408.08535v1#bib.bib31)); Liu et al. ([2020a](https://arxiv.org/html/2408.08535v1#bib.bib22)). For instance, Yasunaga et al. ([2022](https://arxiv.org/html/2408.08535v1#bib.bib34)) propose a cross-modal model to fuse text and KG to jointly pre-train the model. Sun et al. ([2020](https://arxiv.org/html/2408.08535v1#bib.bib30)) present a word-knowledge graph that unifies words and knowledge. Zhang et al. ([2022](https://arxiv.org/html/2408.08535v1#bib.bib35)) fuses representations from pre-trained language models and graph neural networks over multiple layers. Models that require additional training are computationally expensive and cumbersome. Kang et al. ([2023](https://arxiv.org/html/2408.08535v1#bib.bib15)) retrieves a relevant subgraph composed of triples by utilizing GNN for triple embedding. In contrast, our method does not necessitate additional training, offering a more efficient and adaptable solution for integrating KGs with LLMs.
Report issue for preceding element
##  3 Problem Statement
Report issue for preceding element
The goal of fact-checking task formulation is to locate the top n𝑛nitalic_n most relevant sentence, in order to classify a given claim as either refuted, supported, or not enough information as the labels by a large language model. Let P𝑃Pitalic_P represent a corpus of fact-checking articles and C𝐶{C}italic_C a set of claims. Each claim c∈C𝑐𝐶c\in Citalic_c ∈ italic_C is associated with a ground-truth label y𝑦yitalic_y. There exists a set of top k𝑘kitalic_k most relevant sentences Pc=piksubscript𝑃𝑐superscriptsubscript𝑝𝑖𝑘P_{c}={p}_{i}^{k}italic_P start_POSTSUBSCRIPT italic_c end_POSTSUBSCRIPT = italic_p start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT start_POSTSUPERSCRIPT italic_k end_POSTSUPERSCRIPT from the fact-checking articles P𝑃Pitalic_P for each claim c𝑐citalic_c. The task is formulated as optimizing the prediction y^=f⁢(C,Pc)^𝑦𝑓𝐶subscript𝑃𝑐\hat{y}=f(C,P_{c})over^ start_ARG italic_y end_ARG = italic_f ( italic_C , italic_P start_POSTSUBSCRIPT italic_c end_POSTSUBSCRIPT ), where f𝑓fitalic_f is a large language model to evaluate the truthfulness of claims based on the evidence provided.
Report issue for preceding element
![Refer to caption](/html/2408.08535v1/x2.png) Figure 2: Workflow of CommunityKG-RAG Report issue for preceding element
##  4 CommunityKG-RAG
Report issue for preceding element
In this section, we detail our novel framework CommunityKG-RAG for integrating KGs with RAG systems and LLMs to enhance fact-checking capabilities. We show an overview in Figure [2](https://arxiv.org/html/2408.08535v1#S3.F2 "Figure 2 ‣ 3 Problem Statement ‣ CommunityKG-RAG: Leveraging Community Structures in Knowledge Graphs for Advanced Retrieval-Augmented Generation in Fact-Checking"). Our approach leverages the structural advantages of KGs to provide a contextually enriched, semantically aware information retrieval mechanism, which is subsequently used to inform the generation process of LLMs.
Report issue for preceding element
###  4.1 Knowledge Graph Construction
Report issue for preceding element
We begin by constructing a KG from a corpus of fact-checking articles. The construction process involves the following three steps:
Report issue for preceding element
####  4.1.1 Coreference Resolution
Report issue for preceding element
Coreference resolution is a preprocessing step to enhance the semantic coherence of the input data prior to knowledge graph construction. This process aims to identify and cluster mentions of entities and pronouns that refer to the same real-world entities across the corpus, thereby resolving ambiguities in entity references.
Report issue for preceding element
We employ a state-of-the-art coreference resolution model by Lee et al. ([2018](https://arxiv.org/html/2408.08535v1#bib.bib17)), leveraging a deep learning approach based on SpanBERT Joshi et al. ([2020](https://arxiv.org/html/2408.08535v1#bib.bib14)), which has been pre-trained on a large corpus to capture a wide range of syntactic and semantic information.
Report issue for preceding element
####  4.1.2 Graph Construction
Report issue for preceding element
CommunityKG-RAG leverages the relationship extraction model, REBEL, proposed by Cabot and Navigli ([2021](https://arxiv.org/html/2408.08535v1#bib.bib5)) to discern entity relationships within the corpus. This process is formalized as follows:
Report issue for preceding element
Given the corpus P𝑃Pitalic_P, we extract a set of entities, denoted as E={e1,e2,…,en}𝐸subscript𝑒1subscript𝑒2…subscript𝑒𝑛E=\\{e_{1},e_{2},...,e_{n}\\}italic_E = { italic_e start_POSTSUBSCRIPT 1 end_POSTSUBSCRIPT , italic_e start_POSTSUBSCRIPT 2 end_POSTSUBSCRIPT , … , italic_e start_POSTSUBSCRIPT italic_n end_POSTSUBSCRIPT }. We construct the entity graph G=(E,R)𝐺𝐸𝑅G=(E,R)italic_G = ( italic_E , italic_R ), where R𝑅Ritalic_R comprises the set of relationships between entities. In this graph, entities (E𝐸Eitalic_E) are represented as nodes, and relationships (R𝑅Ritalic_R) are depicted as edges that link these nodes. This graph represents the intricate network of connections among entities derived from the corpus, forming the foundation of the KG.
Report issue for preceding element
This structured approach facilitates a comprehensive representation of the factual relationships within articles, thereby enabling advanced analysis and application in fact-checking and misinformation identification tasks.
Report issue for preceding element
####  4.1.3 Node Feature Embedding
Report issue for preceding element
For each node in the KG, we assign it with word embeddings derived from a pre-trained BERT model Devlin et al. ([2018a](https://arxiv.org/html/2408.08535v1#bib.bib7)). This embedding serves as the node feature vector, encapsulating the semantic information of the entity.
Report issue for preceding element
###  4.2 Community Detection
Report issue for preceding element
To leverage the community structures inherent within the Knowledge Graph (KG) for enhanced fact retrieval, we employ the Louvain algorithm Blondel et al. ([2008](https://arxiv.org/html/2408.08535v1#bib.bib3)) as a foundational tool. This algorithm is instrumental in detecting and delineating communities within the graph G𝐺Gitalic_G, by focusing on the optimization of modularity. Modularity is a scalar value between −11-1- 1 and 1111 that measures the density of links inside communities compared to links between communities. The algorithm initially treats each node as its own community and iteratively merges communities to maximize the gain in modularity. This optimization continues until no further improvement in modularity is possible, resulting in a partition of the graph into distinct communities.
Report issue for preceding element
From graph G𝐺Gitalic_G, we extract a set of communities denoted by M𝑀Mitalic_M, where each community m∈M𝑚𝑀m\in Mitalic_m ∈ italic_M represents a cluster of nodes more interconnected among themselves than with the rest of the graph. This structured approach allows us to focus our retrieval efforts on specific segments of the KG that are more likely to contain relevant and contextually rich information for fact-checking tasks.
Report issue for preceding element
###  4.3 Community Retrieval
Report issue for preceding element
Each community m𝑚mitalic_m is considered as a subgraph Gm=(Em,Rm)subscript𝐺𝑚subscript𝐸𝑚subscript𝑅𝑚G_{m}=(E_{m},R_{m})italic_G start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT = ( italic_E start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT , italic_R start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT ) comprising a subset of entity nodes Emsubscript𝐸𝑚E_{m}italic_E start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT and their relationships Rmsubscript𝑅𝑚R_{m}italic_R start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT. The embedding representation of each community denoted as φ⁢(m)𝜑𝑚\varphi(m)italic_φ ( italic_m ) is derived by averaging the BERT embeddings of the nodes within Emsubscript𝐸𝑚E_{m}italic_E start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT:
Report issue for preceding element  
|   | φ⁢(m)=1|Em|⁢∑i∈EmBERT⁢(ei)𝜑𝑚1subscript𝐸𝑚subscript𝑖subscript𝐸𝑚BERTsubscript𝑒𝑖\varphi(m)=\frac{1}{|E_{m}|}\sum_{i\in E_{m}}\text{BERT}(e_{i})italic_φ ( italic_m ) = divide start_ARG 1 end_ARG start_ARG | italic_E start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT | end_ARG ∑ start_POSTSUBSCRIPT italic_i ∈ italic_E start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT end_POSTSUBSCRIPT BERT ( italic_e start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT )  |   |  
| --- | --- | --- |  
where |Em|subscript𝐸𝑚|E_{m}|| italic_E start_POSTSUBSCRIPT italic_m end_POSTSUBSCRIPT | is the number of nodes in a community m𝑚mitalic_m and eisubscript𝑒𝑖e_{i}italic_e start_POSTSUBSCRIPT italic_i end_POSTSUBSCRIPT represents the word embedding of node i𝑖iitalic_i derived from BERT model Li et al. ([2023a](https://arxiv.org/html/2408.08535v1#bib.bib18)) as described in the section [4.1.3](https://arxiv.org/html/2408.08535v1#S4.SS1.SSS3 "4.1.3 Node Feature Embedding ‣ 4.1 Knowledge Graph Construction ‣ 4 CommunityKG-RAG ‣ CommunityKG-RAG: Leveraging Community Structures in Knowledge Graphs for Advanced Retrieval-Augmented Generation in Fact-Checking"). This approach aggregates the collective semantic attributes of the community, encapsulating a comprehensive semantic representation.
Report issue for preceding element
To convert claims into embeddings for similarity comparisons, we utilize the BERT-base Sentence Transformer model, Sentence-BERT Reimers and Gurevych ([2019](https://arxiv.org/html/2408.08535v1#bib.bib27)). Sentence-BERT is specifically optimized for generating high-quality sentence embeddings, making it ideally suited for comparing the semantic similarities between claims and community descriptions.
Report issue for preceding element
The relevance score r⁢(c,m)𝑟𝑐𝑚r(c,m)italic_r ( italic_c , italic_m ) between claim c𝑐citalic_c and community m𝑚mitalic_m is calculated as the dot product between their embeddings:
Report issue for preceding element  
|   | r⁢(c,m)=φ⁢(c)T⁢φ⁢(m)𝑟𝑐𝑚𝜑superscript𝑐𝑇𝜑𝑚r(c,m)=\varphi(c)^{T}\varphi(m)italic_r ( italic_c , italic_m ) = italic_φ ( italic_c ) start_POSTSUPERSCRIPT italic_T end_POSTSUPERSCRIPT italic_φ ( italic_m )  |   |  
| --- | --- | --- |  
###  4.4 Top Community Selection
Report issue for preceding element
To efficiently prioritize communities for deeper analysis, the top δ𝛿\deltaitalic_δ percent of communities, ranked by their relevance scores r⁢(c,m)𝑟𝑐𝑚r(c,m)italic_r ( italic_c , italic_m ), are selected. The selection threshold N𝑁Nitalic_N is determined as follows: N=⌈δ100×|M|⌉𝑁𝛿100𝑀N=\left\lceil\frac{\delta}{100}\times|M|\right\rceilitalic_N = ⌈ divide start_ARG italic_δ end_ARG start_ARG 100 end_ARG × | italic_M | ⌉, where |M|𝑀|M|| italic_M | represents the total number of communities. Consequently, the subset of most relevant communities Mc∗subscriptsuperscript𝑀𝑐M^{*}_{c}italic_M start_POSTSUPERSCRIPT ∗ end_POSTSUPERSCRIPT start_POSTSUBSCRIPT italic_c end_POSTSUBSCRIPT to claim c𝑐citalic_c is defined as:
Report issue for preceding element  
|   | Mc∗={m∈M:rank⁢(r⁢(c,m))≤N}subscriptsuperscript𝑀𝑐conditional-set𝑚𝑀rank𝑟𝑐𝑚𝑁M^{*}_{c}=\\{m\in M:\text{rank}(r(c,m))\leq N\\}italic_M start_POSTSUPERSCRIPT ∗ end_POSTSUPERSCRIPT start_POSTSUBSCRIPT italic_c end_POSTSUBSCRIPT = { italic_m ∈ italic_M : rank ( italic_r ( italic_c , italic_m ) ) ≤ italic_N }  |   |  
| --- | --- | --- |  
This selection criterion ensures that our analysis is concentrated on the communities most likely to contain relevant and substantive information pertinent to the verification of a claim c𝑐citalic_c, thus facilitating efficient and focused fact-checking.
Report issue for preceding element
###  4.5 Top Community-to-Sentence Selection
Report issue for preceding element
To identify the most pertinent sentences, a relevance score r⁢(Mc∗,p)𝑟subscriptsuperscript𝑀𝑐𝑝r(M^{*}_{c},p)italic_r ( italic_M start_POSTSUPERSCRIPT ∗ end_POSTSUPERSCRIPT start_POSTSUBSCRIPT italic_c end_POSTSUBSCRIPT , italic_p ) is computed for each sentence p𝑝pitalic_p within the top communities Mc∗subscriptsuperscript𝑀𝑐M^{*}_{c}italic_M start_POSTSUPERSCRIPT ∗ end_POSTSUPERSCRIPT start_POSTSUBSCRIPT italic_c end_POSTSUBSCRIPT. Sentences are then ranked by relevance, and the top λ𝜆\lambdaitalic_λ percent are selected, resulting in a subset Pc∗subscriptsuperscript𝑃𝑐P^{*}_{c}italic_P start_POSTSUPERSCRIPT ∗ end_POSTSUPERSCRIPT start_POSTSUBSCRIPT italic_c end_POSTSUBSCRIPT of the most relevant sentences.
Report issue for preceding element
This structured approach allows for systematic filtering and selection of significant information, a process which is crucial for robust and focused fact-checking. We use CommunityKG-RAGλδsubscriptsuperscriptCommunityKG-RAG𝛿𝜆\text{CommunityKG-RAG}^{\delta}_{\lambda}CommunityKG-RAG start_POSTSUPERSCRIPT italic_δ end_POSTSUPERSCRIPT start_POSTSUBSCRIPT italic_λ end_POSTSUBSCRIPT to represent the synergistic application of two distinct filters: the top δ𝛿\deltaitalic_δ percent for community relevance and the top λ𝜆\lambdaitalic_λ percent for sentence significance within the context of validating community-to-sentence relevance. This refined designation underscores a strategic methodological synthesis aimed at optimizing the fact-checking process by methodically concentrating on the most pivotal communities and their essential corresponding sentences.
Report issue for preceding element
##  5 Experimental Details
Report issue for preceding element
###  5.1 Datasets
Report issue for preceding element
MOCHEG This multimodal fack-checking dataset Menglong Yao et al. ([2022](https://arxiv.org/html/2408.08535v1#bib.bib25)) consists of 15,601 claims annotated with a truthfulness label collected from PolitiFact and Snopes, two popular websites for fact-checking articles. The articles and results of claim verification were produced by journalists manually. The truthfulness is labeled into three categories: supported, refuted, and NEI (not enough information). More details are included in the Appendix [A](https://arxiv.org/html/2408.08535v1#A1 "Appendix A Details of Datasets ‣ CommunityKG-RAG: Leveraging Community Structures in Knowledge Graphs for Advanced Retrieval-Augmented Generation in Fact-Checking").
Report issue for preceding element
###  5.2 Baselines
Report issue for preceding element
No Retrieval This is a naive baseline where answers are generated from the language model through prompts without context or retrieval.
Report issue for preceding element
Semantic Retrieval Following Nie et al. ([2019](https://arxiv.org/html/2408.08535v1#bib.bib26)), we extract context based on semantic similarity. Specifically, we use cosine similarity in embeddings between the prompt and the context. BERT Devlin et al. ([2018b](https://arxiv.org/html/2408.08535v1#bib.bib8)) is used to produce the embedding.
Report issue for preceding element
Knowledge-Augmented language model PromptING (KAPING) We implement KAPING proposed by Baek et al. ([2023](https://arxiv.org/html/2408.08535v1#bib.bib1)). The KAPING is a zero-shot RAG framework that proposes basing retrieval on sentence similarity between the input text and triples. The output prompt of the KAPING framework includes the original text prompt with triples as the context. Specifically, the triples are in the format of (s⁢u⁢b⁢j⁢e⁢c⁢t⁢e⁢n⁢t⁢i⁢t⁢y,r⁢e⁢l⁢a⁢t⁢i⁢o⁢n⁢s⁢h⁢i⁢p,o⁢b⁢j⁢e⁢c⁢t⁢e⁢n⁢t⁢i⁢t⁢y)𝑠𝑢𝑏𝑗𝑒𝑐𝑡𝑒𝑛𝑡𝑖𝑡𝑦𝑟𝑒𝑙𝑎𝑡𝑖𝑜𝑛𝑠ℎ𝑖𝑝𝑜𝑏𝑗𝑒𝑐𝑡𝑒𝑛𝑡𝑖𝑡𝑦(subjectentity,relationship,objectentity)( italic_s italic_u italic_b italic_j italic_e italic_c italic_t italic_e italic_n italic_t italic_i italic_t italic_y , italic_r italic_e italic_l italic_a italic_t italic_i italic_o italic_n italic_s italic_h italic_i italic_p , italic_o italic_b italic_j italic_e italic_c italic_t italic_e italic_n italic_t italic_i italic_t italic_y ). We equip KAPING with the same set of articles for retrieval.
Report issue for preceding element
###  5.3 Implementation Details
Report issue for preceding element
We conducted our experiments using the LLaMa2 7 billion model as our primary Large Language Model Touvron et al. ([2023](https://arxiv.org/html/2408.08535v1#bib.bib32)). The LLaMa2 models are open-source and widely accessible. We chose these models because they were trained on trillions of tokens, including publicly available datasets like Wikipedia, and demonstrated state-of-the-art results at the time when the texts were published. This capability enabled a thorough evaluation of our method’s zero-shot performance when applied to previously unseen corpora.
Report issue for preceding element
The availability of these models in multiple sizes enabled a comparative analysis of our proposed framework, assessing how model scale impacts performance. Furthermore, since Wikipedia was integral to their training datasets, we were able to explore the efficacy of our approach on corpora familiar to the models. The utility of this retrieval approach has been substantiated in prior research Khandelwal et al. ([2020](https://arxiv.org/html/2408.08535v1#bib.bib16)).
Report issue for preceding element
To quantitatively assess the LLMs, we measured their performance in verifying claims using accuracy as our metric. More details of the LLMs and the corresponding prompt are included in Appendices [B](https://arxiv.org/html/2408.08535v1#A2 "Appendix B Prompt ‣ CommunityKG-RAG: Leveraging Community Structures in Knowledge Graphs for Advanced Retrieval-Augmented Generation in Fact-Checking") and [C](https://arxiv.org/html/2408.08535v1#A3 "Appendix C Language Model Parameters ‣ CommunityKG-RAG: Leveraging Community Structures in Knowledge Graphs for Advanced Retrieval-Augmented Generation in Fact-Checking").
Report issue for preceding element
We use CommunityKG-RAG10025subscriptsuperscriptCommunityKG-RAG25100\text{CommunityKG-RAG}^{25}_{100}CommunityKG-RAG start_POSTSUPERSCRIPT 25 end_POSTSUPERSCRIPT start_POSTSUBSCRIPT 100 end_POSTSUBSCRIPT as the baseline. In other words, we use the top δ=25𝛿25\delta=25italic_δ = 25 percent of the most relevant communities and λ=100𝜆100\lambda=100italic_λ = 100 percent of the sentences that the community maps to as the context.
Report issue for preceding element
##  6 Results
Report issue for preceding element  
| Model  | LLaMa2 7B  |  
| --- | --- |  
| No Retrieval  | 39.79%  |  
| Semantic Retrieval  | 43.84 %  |  
| KAPING  | 39.41 %  |  
| CommunityKG-RAG10025subscriptsuperscriptCommunityKG-RAG25100\text{CommunityKG-RAG}^{25}_{100}CommunityKG-RAG start_POSTSUPERSCRIPT 25 end_POSTSUPERSCRIPT start_POSTSUBSCRIPT 100 end_POSTSUBSCRIPT  | 56.24%  |  
Table 1: Comparison of claim verification accuracy for various retrieval methods: No Retrieval, Semantic Retrieval, KAPING, and our approach, CommunityKG-RAG10025subscriptsuperscriptCommunityKG-RAG25100\text{CommunityKG-RAG}^{25}_{100}CommunityKG-RAG start_POSTSUPERSCRIPT 25 end_POSTSUPERSCRIPT start_POSTSUBSCRIPT 100 end_POSTSUBSCRIPT, which selects the top 25 percent of relevant communities and uses 100 percent of their mapped sentences as context.  Report issue for preceding element
###  6.1 Main Results
Report issue for preceding element
Overall, our proposed method, CommunityKG-RAG10025subscriptsuperscriptCommunityKG-RAG25100\text{CommunityKG-RAG}^{25}_{100}CommunityKG-RAG start_POSTSUPERSCRIPT 25 end_POSTSUPERSCRIPT start_POSTSUBSCRIPT 100 end_POSTSUBSCRIPT, not only achieves the best results but also surpasses all baselines, as detailed in Table [1](https://arxiv.org/html/2408.08535v1#S6.T1 "Table 1 ‣ 6 Results ‣ CommunityKG-RAG: Leveraging Community Structures in Knowledge Graphs for Advanced Retrieval-Augmented Generation in Fact-Checking"). The No Retrieval baseline recorded an accuracy of 39.79 percent. Employing the Semantic Retrieval strategy yielded an improvement, elevating accuracy to 43.84 percent. This increase underscores the advantages of integrating semantic context, thereby enhancing the proficiency of the language model in claim verification.
Report issue for preceding element
Conversely, the KAPING method did not enhance performance, registering a slight decline in accuracy to 39.41 percent. This outcome indicates that a language model such as LLaMa2 may struggle with retrieval contexts formatted as triples (i.e., (subject entity, relationship, object entity) ). Such structuring appears to impede the model’s capacity to effectively utilize information. This is likely due to its foundational training on sequential word prediction rather than on processing structured data like triples.
Report issue for preceding element
However, the performance of our approach, CommunityKG-RAG10025subscriptsuperscriptCommunityKG-RAG25100\text{CommunityKG-RAG}^{25}_{100}CommunityKG-RAG start_POSTSUPERSCRIPT 25 end_POSTSUPERSCRIPT start_POSTSUBSCRIPT 100 end_POSTSUBSCRIPT, was markedly superior, achieving an accuracy of 56.24 percent. This significant increase not only confirms the effectiveness of integrating community-derived knowledge into the retrieval process but also demonstrates substantial gains over conventional retrieval methods. These results validate the substantial impact that tailored, community-focused retrieval mechanisms can have on the operational effectiveness of language models in complex verification scenarios. This marked improvement reiterates the critical role of precise, context-aware retrieval strategies in augmenting the functional capabilities of language models.
Report issue for preceding element
###  6.2 Ablation
Report issue for preceding element
We conducted a series of ablation studies to understand the significance of various factors within the CommunityKG-RAG framework. Specifically, these ablation studies are designed to evaluate the impact of different backbone language models, the selection of top communities, and the extent of community-to-sentence selection.
Report issue for preceding element
####  6.2.1 Performance With Different Backbone Models
Report issue for preceding element
To demonstrate the robustness and adaptability of the proposed CommunityKG-RAG framework, we conducted an ablation study to assess how different backbone language models affect the performance on the MOCHEG fact-checking dataset. Considering the computational costs, which increase with the number of communities and community-to-sentences selection using the community (Appendix [E](https://arxiv.org/html/2408.08535v1#A5 "Appendix E Community Statistics ‣ CommunityKG-RAG: Leveraging Community Structures in Knowledge Graphs for Advanced Retrieval-Augmented Generation in Fact-Checking")), we conduct this ablation with CommunityKG-RAG2525subscriptsuperscriptCommunityKG-RAG2525\text{CommunityKG-RAG}^{25}_{25}CommunityKG-RAG start_POSTSUPERSCRIPT 25 end_POSTSUPERSCRIPT start_POSTSUBSCRIPT 25 end_POSTSUBSCRIPT. We selected the top δ=25𝛿25\delta=25italic_δ = 25 percent of the most relevant communities and the top λ=25𝜆25\lambda=25italic_λ = 25 percent of the sentences mapped to these communities to serve as the contextual input.
Report issue for preceding element
In this analysis, we compared the performance of two different backbone models: LLaMa2 7B and LLaMa3 8B. Table [2](https://arxiv.org/html/2408.08535v1#S6.T2 "Table 2 ‣ 6.2.1 Performance With Different Backbone Models ‣ 6.2 Ablation ‣ 6 Results ‣ CommunityKG-RAG: Leveraging Community Structures in Knowledge Graphs for Advanced Retrieval-Augmented Generation in Fact-Checking") illustrates the outcomes, showing that CommunityKG-RAG significantly enhances performance across both models. Specifically, when employing the CommunityKG-RAG framework, there is a notable improvement of 6.18 percentage points with LLaMa2 7B and an increase of 3.21 percentage points with LLaMa3 8B compared to the no retrieval baseline. However, we observed that the LLaMa3 8B showed a lesser improvement and accuracy over the no retrieval baseline than the 7B model despite its larger size. This may be attributed to the 8B model’s capability to explore various facets of a given issue more comprehensively, which, while generally beneficial, might lead to a less precise matching in scenarios demanding exact binary evaluations, such as our fact-checking tasks. This characteristic could also contribute to the slightly lower improvement observed with the 8B model.
Report issue for preceding element
These results underscore the effectiveness of our framework in leveraging structured community knowledge, thereby improving the accuracy of fact-checking across diverse language model architectures.
Report issue for preceding element  
| Model  | LLaMa2  | LLaMa3  |  
| --- | --- | --- |  
|   | 7B  | 8B  |  
| No Retrieval  | 39.79%  | 26.03%  |  
| CommunityKG-RAG2525subscriptsuperscriptCommunityKG-RAG2525\text{CommunityKG-RAG}^{25}_{25}CommunityKG-RAG start_POSTSUPERSCRIPT 25 end_POSTSUPERSCRIPT start_POSTSUBSCRIPT 25 end_POSTSUBSCRIPT  | 45.97%  | 29.24%  |  
Table 2: Performance comparison of no retrieval and CommunityKG-RAG with δ=25𝛿25\delta=25italic_δ = 25 and λ=25𝜆25\lambda=25italic_λ = 25 settings across different backbone models, LLaMa2 7B and LLaMa3 8B. Report issue for preceding element
####  6.2.2 Influence of Community-to-Sentence Selection
Report issue for preceding element
This section examines the influence of varying community-to-sentence selection thresholds within a consistently held community threshold of 25 percent on the performance of the CommunityKG-RAG framework using the LLaMa2 7B model. Community-to-sentence selection thresholds were adjusted to 25 percent, 50 percent, 75 percent, and 100 percent to identify the optimal level for enhancing fact-checking performance.
Report issue for preceding element  
| Model  | LLaMa2 7B  |  
| --- | --- |  
| CommunityKG-RAG2525subscriptsuperscriptCommunityKG-RAG2525\text{CommunityKG-RAG}^{25}_{25}CommunityKG-RAG start_POSTSUPERSCRIPT 25 end_POSTSUPERSCRIPT start_POSTSUBSCRIPT 25 end_POSTSUBSCRIPT  | 45.97%  |  
| CommunityKG-RAG5025subscriptsuperscriptCommunityKG-RAG2550\text{CommunityKG-RAG}^{25}_{50}CommunityKG-RAG start_POSTSUPERSCRIPT 25 end_POSTSUPERSCRIPT start_POSTSUBSCRIPT 50 end_POSTSUBSCRIPT  | 27.83%  |  
| CommunityKG-RAG7525subscriptsuperscriptCommunityKG-RAG2575\text{CommunityKG-RAG}^{25}_{75}CommunityKG-RAG start_POSTSUPERSCRIPT 25 end_POSTSUPERSCRIPT start_POSTSUBSCRIPT 75 end_POSTSUBSCRIPT  | 41.93%  |  
| CommunityKG-RAG10025subscriptsuperscriptCommunityKG-RAG25100\text{CommunityKG-RAG}^{25}_{100}CommunityKG-RAG start_POSTSUPERSCRIPT 25 end_POSTSUPERSCRIPT start_POSTSUBSCRIPT 100 end_POSTSUBSCRIPT  | 56.24%  |  
Table 3: Performance variations of the LLaMa2 7B model under the CommunityKG-RAG framework with consistent community threshold (top 25 percent) and variable community-to-sentence selection.  Report issue for preceding element
The results presented in Table [3](https://arxiv.org/html/2408.08535v1#S6.T3 "Table 3 ‣ 6.2.2 Influence of Community-to-Sentence Selection ‣ 6.2 Ablation ‣ 6 Results ‣ CommunityKG-RAG: Leveraging Community Structures in Knowledge Graphs for Advanced Retrieval-Augmented Generation in Fact-Checking") demonstrate variable model performance as community-to-sentence selection thresholds change. Initially, the performance slightly decreases to 27.83 percent when the inclusion rate of sentences is increased from 25 percent to 50 percent. This might indicate that the top 25 percent of sentences contain the most crucial information for verifying the claim, and including additional sentences up to 50 percent introduces noise or less relevant data that temporarily hinder the model’s accuracy. However, as the inclusion rate continues to increase to 75 percent and then to 100 percent, the performance improves, ultimately achieving the highest accuracy at a full 100 percent inclusion rate. This suggests that beyond the 50 percent threshold, the additional sentences contribute positively, possibly by providing necessary context that supports more accurate fact-checking.
Report issue for preceding element
This pattern highlights the critical role of extensive contextual engagement in the CommunityKG-RAG framework, demonstrating that access to a wider array of sentences associated with a carefully selected group of communities markedly improves the model’s effectiveness in accurately identifying truth and falsehood. These results underscore the nuanced balance needed in selection strategies to provide adequate context for accurate analysis without inundating the model with extraneous data.
Report issue for preceding element
####  6.2.3 Combined Effects of Top Community and Community-to-Sentence Selection
Report issue for preceding element
To further explore the efficacy of the CommunityKG-RAG framework, we conducted an analysis to understand the impact of varying the top community and community-to-sentence selection thresholds on the performance of the model. We adjusted the thresholds of both δ𝛿\deltaitalic_δ and λ𝜆\lambdaitalic_λ to 25 percent, 50 percent, 75 percent, and 100 percent to examine how the extent of considered context in both community and community-to-sentence selection affect the fact-checking capabilities of the CommunityKG-RAG framework. We show the knowledge graph community statistics in Appendix [E](https://arxiv.org/html/2408.08535v1#A5 "Appendix E Community Statistics ‣ CommunityKG-RAG: Leveraging Community Structures in Knowledge Graphs for Advanced Retrieval-Augmented Generation in Fact-Checking").
Report issue for preceding element
The results, as shown in Table [4](https://arxiv.org/html/2408.08535v1#S6.T4 "Table 4 ‣ 6.2.3 Combined Effects of Top Community and Community-to-Sentence Selection ‣ 6.2 Ablation ‣ 6 Results ‣ CommunityKG-RAG: Leveraging Community Structures in Knowledge Graphs for Advanced Retrieval-Augmented Generation in Fact-Checking"), reveal interesting trends. Initially, the increase of thresholds from 25 percent to 75 percent led to a slight decrease in performance, suggesting that adding more communities and sentences might introduce noise or less relevant information, thus compromising the model’s effectiveness. However, a significant improvement is observed when the thresholds are expanded to 100 percent. This enhancement at the highest threshold suggests that the model benefits from a more comprehensive view of the available data, possibly capturing essential contextual nuances that are otherwise missed at lower thresholds. This pattern aligns with observations from previous ablation studies concerning community-to-sentence selection.
Report issue for preceding element
Interestingly, when comparing the effects of top community selection, an increase in the number of top communities results in improved accuracy while holding community-to-sentence selection constant. This observation emerges from comparing CommunityKG-RAG5025subscriptsuperscriptCommunityKG-RAG2550\text{CommunityKG-RAG}^{25}_{50}CommunityKG-RAG start_POSTSUPERSCRIPT 25 end_POSTSUPERSCRIPT start_POSTSUBSCRIPT 50 end_POSTSUBSCRIPT versus CommunityKG-RAG5050subscriptsuperscriptCommunityKG-RAG5050\text{CommunityKG-RAG}^{50}_{50}CommunityKG-RAG start_POSTSUPERSCRIPT 50 end_POSTSUPERSCRIPT start_POSTSUBSCRIPT 50 end_POSTSUBSCRIPT, and CommunityKG-RAG7525subscriptsuperscriptCommunityKG-RAG2575\text{CommunityKG-RAG}^{25}_{75}CommunityKG-RAG start_POSTSUPERSCRIPT 25 end_POSTSUPERSCRIPT start_POSTSUBSCRIPT 75 end_POSTSUBSCRIPT to CommunityKG-RAG7575subscriptsuperscriptCommunityKG-RAG7575\text{CommunityKG-RAG}^{75}_{75}CommunityKG-RAG start_POSTSUPERSCRIPT 75 end_POSTSUPERSCRIPT start_POSTSUBSCRIPT 75 end_POSTSUBSCRIPT.
Report issue for preceding element
However, increasing both the community selection and community-to-sentence selection to 100 percent does not yield further improvements. As illustrated by the comparison between CommunityKG-RAG10025subscriptsuperscriptCommunityKG-RAG25100\text{CommunityKG-RAG}^{25}_{100}CommunityKG-RAG start_POSTSUPERSCRIPT 25 end_POSTSUPERSCRIPT start_POSTSUBSCRIPT 100 end_POSTSUBSCRIPT and CommunityKG-RAG100100subscriptsuperscriptCommunityKG-RAG100100\text{CommunityKG-RAG}^{100}_{100}CommunityKG-RAG start_POSTSUPERSCRIPT 100 end_POSTSUPERSCRIPT start_POSTSUBSCRIPT 100 end_POSTSUBSCRIPT, this finding implies that a targeted selection of highly relevant communities, along with a comprehensive examination of their associated sentences, strikes an ideal balance. It enables the model to access detailed and pertinent information effectively without being overwhelmed by extraneous data. This method provides a nuanced approach to information retrieval that maximizes accuracy while avoiding information overload.
Report issue for preceding element  
| Model  | LLaMa2 7B  |  
| --- | --- |  
| CommunityKG-RAG2525subscriptsuperscriptCommunityKG-RAG2525\text{CommunityKG-RAG}^{25}_{25}CommunityKG-RAG start_POSTSUPERSCRIPT 25 end_POSTSUPERSCRIPT start_POSTSUBSCRIPT 25 end_POSTSUBSCRIPT  | 45.97%  |  
| CommunityKG-RAG5050subscriptsuperscriptCommunityKG-RAG5050\text{CommunityKG-RAG}^{50}_{50}CommunityKG-RAG start_POSTSUPERSCRIPT 50 end_POSTSUPERSCRIPT start_POSTSUBSCRIPT 50 end_POSTSUBSCRIPT  | 43.64%  |  
| CommunityKG-RAG7575subscriptsuperscriptCommunityKG-RAG7575\text{CommunityKG-RAG}^{75}_{75}CommunityKG-RAG start_POSTSUPERSCRIPT 75 end_POSTSUPERSCRIPT start_POSTSUBSCRIPT 75 end_POSTSUBSCRIPT  | 43.60%  |  
| CommunityKG-RAG100100subscriptsuperscriptCommunityKG-RAG100100\text{CommunityKG-RAG}^{100}_{100}CommunityKG-RAG start_POSTSUPERSCRIPT 100 end_POSTSUPERSCRIPT start_POSTSUBSCRIPT 100 end_POSTSUBSCRIPT  | 54.62%  |  
Table 4: Performance metrics of the LLaMa2 7B model within the CommunityKG-RAG framework across varied thresholds of top community and community-to-sentence selection. The table details the model’s accuracy percentages at incremental selection thresholds of 25, 50, 75, and 100 percent for both community and community-to-sentence selection, illustrating how varying levels of context inclusion impact the model’s performance. Report issue for preceding element
##  7 Conclusion
Report issue for preceding element
We have introduced CommunityKG-RAG, a novel framework that integrates Knowledge Graphs with Retrieval-Augmented Generation and Large Language Models to enhance fact-checking. This approach leverages the structured data of KGs and the generative capabilities of LLMs, significantly improving the accuracy and relevance of responses.
Report issue for preceding element
CommunityKG-RAG effectively addresses key challenges such as outdated information and hallucinations by utilizing multi-hop community structures for refined and accurate retrieval within KGs. This integration enables more precise and contextually rich information retrieval, crucial for effective fact-checking. Our framework achieves superior performance without requiring any fine-tuning or additional training, demonstrating its robustness and efficiency. As the first framework to combine multi-hop community information in KGs with RAG systems, CommunityKG-RAG represents a significant advancement and promising direction for future work.
Report issue for preceding element
##  8 Limitations
Report issue for preceding element
Despite the notable success of the CommunityKG-RAG framework in enhancing claim verification accuracy, several limitations highlight areas for future research and improvement:
Report issue for preceding element
###  8.1 Computational Demands
Report issue for preceding element
The CommunityKG-RAG framework places substantial demands on computational resources compared to no retrieval or semantic retrieval. However, communities can be pre-computed and reused, making the operational phase more lightweight and dynamic. This capability enhances the model’s responsiveness to new data and trends. Further, our method has demonstrated significant accuracy improvements despite the computational demands, and, besides, our proposed method is more lightweight than methods that require training or fine-tuning a language model.
Report issue for preceding element
###  8.2 Dependency on Entity Recognition Quality
Report issue for preceding element
Our proposed method’s effectiveness heavily relies on the quality of entity recognition. There are prior works Edge et al. ([2024](https://arxiv.org/html/2408.08535v1#bib.bib9)) that rely on utilizing language models to conduct entity recognition. This could potentially introduce hallucinations. To avoid such risk, we use REBEL, a seq2seq model based on Wikipedia data. If the framework is applied to text that is significantly different from Wikipedia text, it might hinder performance. In such cases, utilizing an entity recognition method tailored to the specific domain could be beneficial. However, as shown in the Appendix [E](https://arxiv.org/html/2408.08535v1#A5 "Appendix E Community Statistics ‣ CommunityKG-RAG: Leveraging Community Structures in Knowledge Graphs for Advanced Retrieval-Augmented Generation in Fact-Checking"), our approach incorporates a comprehensive dataset with up to 48,630 nodes and 202,455 edges, which ensures a robust and extensive knowledge base. This comprehensive coverage helps mitigate potential quality issues, enhancing the reliability of the entity recognition process.
Report issue for preceding element
These limitations, alongside the outlined implementation advantages, underscore the need for ongoing refinement and testing of the CommunityKG-RAG framework to optimize its practicality and effectiveness in real-world scenarios. The ability to pre-compute communities ensures that the method remains operationally lightweight and scalable, an essential factor for broad application. Additionally, future work can consider extending this method framework into multimodality, integrating multimodal graphs or tabular data. Such extensions could further enhance the model’s capabilities and applicability in more complex and varied data environments, opening new avenues for research and practical implementation.
Report issue for preceding element
## References
Report issue for preceding element
  * Baek et al. (2023)↑ Jinheon Baek, Alham Fikri Aji, and Amir Saffari. 2023.  Knowledge-augmented language model prompting for zero-shot knowledge graph question answering.  _arXiv preprint arXiv:2306.04136_. 
  * Barnett et al. (2024)↑ Scott Barnett, Stefanus Kurniawan, Srikanth Thudumu, Zach Brannelly, and Mohamed Abdelrazek. 2024.  Seven failure points when engineering a retrieval augmented generation system.  _arXiv preprint arXiv:2401.05856_. 
  * Blondel et al. (2008)↑ Vincent D Blondel, Jean-Loup Guillaume, Renaud Lambiotte, and Etienne Lefebvre. 2008.  [Fast unfolding of communities in large networks](https://doi.org/10.1088/1742-5468/2008/10/P10008).  _Journal of Statistical Mechanics: Theory and Experiment_ , 2008(10):P10008. 
  * Buchholz (2023)↑ Mars Gokturk Buchholz. 2023.  Assessing the effectiveness of gpt-3 in detecting false political statements: A case study on the liar dataset.  _arXiv preprint arXiv:2306.08190_. 
  * Cabot and Navigli (2021)↑ Pere-Lluís Huguet Cabot and Roberto Navigli. 2021.  Rebel: Relation extraction by end-to-end language generation.  In _Findings of the Association for Computational Linguistics: EMNLP 2021_ , pages 2370–2381. 
  * Caramancion (2023)↑ Kevin Matthe Caramancion. 2023.  Harnessing the power of chatgpt to decimate mis/disinformation: Using chatgpt for fake news detection.  In _2023 IEEE World AI IoT Congress (AIIoT)_ , pages 0042–0046. IEEE. 
  * Devlin et al. (2018a)↑ Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. 2018a.  [BERT: pre-training of deep bidirectional transformers for language understanding](http://arxiv.org/abs/1810.04805).  _CoRR_ , abs/1810.04805. 
  * Devlin et al. (2018b)↑ Jacob Devlin, Ming-Wei Chang, Kenton Lee, and Kristina Toutanova. 2018b.  Bert: Pre-training of deep bidirectional transformers for language understanding.  _arXiv preprint arXiv:1810.04805_. 
  * Edge et al. (2024)↑ Darren Edge, Ha Trinh, Newman Cheng, Joshua Bradley, Alex Chao, Apurva Mody, Steven Truitt, and Jonathan Larson. 2024.  [From local to global: A graph rag approach to query-focused summarization](http://arxiv.org/abs/2404.16130). 
  * Hoes et al. (2023)↑ Emma Hoes, Sacha Altay, and Juan Bermeo. 2023.  Leveraging chatgpt for efficient fact-checking.  _PsyArXiv. April_ , 3. 
  * Hu et al. (2023)↑ Xuming Hu, Junzhe Chen, Zhijiang Guo, and Philip S. Yu. 2023.  Give me more details: Improving fact-checking with latent retrieval.  _arXiv preprint arXiv:2305.16128_. 
  * Huang et al. (2023)↑ Lei Huang, Weijiang Yu, Weitao Ma, Weihong Zhong, Zhangyin Feng, Haotian Wang, Qianglong Chen, Weihua Peng, Xiaocheng Feng, Bing Qin, and Ting Liu. 2023.  [A survey on hallucination in large language models: Principles, taxonomy, challenges, and open questions](http://arxiv.org/abs/2311.05232). 
  * Huang and Sun (2023)↑ Yue Huang and Lichao Sun. 2023.  Harnessing the power of chatgpt in fake news: An in-depth exploration in generation, detection and explanation.  _arXiv preprint arXiv:2310.05046_. 
  * Joshi et al. (2020)↑ Mandar Joshi, Danqi Chen, Yinhan Liu, Daniel S. Weld, Luke Zettlemoyer, and Omer Levy. 2020.  [SpanBERT: Improving Pre-training by Representing and Predicting Spans](https://doi.org/10.1162/tacl_a_00300).  _Transactions of the Association for Computational Linguistics_ , 8:64–77. 
  * Kang et al. (2023)↑ Minki Kang, Jin Myung Kwak, Jinheon Baek, and Sung Ju Hwang. 2023.  [Knowledge graph-augmented language models for knowledge-grounded dialogue generation](http://arxiv.org/abs/2305.18846). 
  * Khandelwal et al. (2020)↑ Urvashi Khandelwal, Omer Levy, Dan Jurafsky, Luke Zettlemoyer, and Mike Lewis. 2020.  [Generalization through memorization: Nearest neighbor language models](http://arxiv.org/abs/1911.00172). 
  * Lee et al. (2018)↑ Kenton Lee, Luheng He, and Luke Zettlemoyer. 2018.  [Higher-order coreference resolution with coarse-to-fine inference](http://arxiv.org/abs/1804.05392). 
  * Li et al. (2023a)↑ Junnan Li, Dongxu Li, Silvio Savarese, and Steven Hoi. 2023a.  Blip-2: Bootstrapping language-image pre-training with frozen image encoders and large language models.  In _International conference on machine learning_ , pages 19730–19742. PMLR. 
  * Li et al. (2023b)↑ Miaoran Li, Baolin Peng, and Zhu Zhang. 2023b.  Self-checker: Plug-and-play modules for fact-checking with large language models.  _arXiv preprint arXiv:2305.14623_. 
  * Liao et al. (2023)↑ Hao Liao, Jiahao Peng, Zhanyi Huang, Wei Zhang, Guanghua Li, Kai Shu, and Xing Xie. 2023.  [Muser: A multi-step evidence retrieval enhancement framework for fake news detection](https://doi.org/10.1145/3580305.3599873).  In _Proceedings of the 29th ACM SIGKDD Conference on Knowledge Discovery and Data Mining_. ACM. 
  * Liu et al. (2023)↑ Nelson F Liu, Kevin Lin, John Hewitt, Ashwin Paranjape, Michele Bevilacqua, Fabio Petroni, and Percy Liang. 2023.  Lost in the middle: How language models use long contexts.  _arXiv preprint arXiv:2307.03172_. 
  * Liu et al. (2020a)↑ Weijie Liu, Peng Zhou, Zhe Zhao, Zhiruo Wang, Qi Ju, Haotang Deng, and Ping Wang. 2020a.  K-bert: Enabling language representation with knowledge graph.  In _Proceedings of the AAAI Conference on Artificial Intelligence_ , volume 34, pages 2901–2908. 
  * Liu et al. (2020b)↑ Zhenghao Liu, Chenyan Xiong, Maosong Sun, and Zhiyuan Liu. 2020b.  [Fine-grained fact verification with kernel graph attention network](https://doi.org/10.18653/v1/2020.acl-main.655).  In _Proceedings of the 58th Annual Meeting of the Association for Computational Linguistics_ , pages 7342–7351, Online. Association for Computational Linguistics. 
  * Ma et al. (2023)↑ Jing Ma, Chen Chen, Chunyan Hou, and Xiaojie Yuan. 2023.  [KAPALM: Knowledge grAPh enhAnced language models for fake news detection](https://doi.org/10.18653/v1/2023.findings-emnlp.263).  In _Findings of the Association for Computational Linguistics: EMNLP 2023_ , pages 3999–4009, Singapore. Association for Computational Linguistics. 
  * Menglong Yao et al. (2022)↑ Barry Menglong Yao, Aditya Shah, Lichao Sun, Jin-Hee Cho, and Lifu Huang. 2022.  End-to-end multimodal fact-checking and explanation generation: A challenging dataset and models.  _arXiv e-prints_ , pages arXiv–2205. 
  * Nie et al. (2019)↑ Yixin Nie, Haonan Chen, and Mohit Bansal. 2019.  Combining fact extraction and verification with neural semantic matching networks.  In _Proceedings of the AAAI conference on artificial intelligence_ , volume 33, pages 6859–6866. 
  * Reimers and Gurevych (2019)↑ Nils Reimers and Iryna Gurevych. 2019.  [Sentence-bert: Sentence embeddings using siamese bert-networks](https://arxiv.org/abs/1908.10084).  In _Proceedings of the 2019 Conference on Empirical Methods in Natural Language Processing_. Association for Computational Linguistics. 
  * Sequeda et al. (2023)↑ Juan Sequeda, Dean Allemang, and Bryon Jacob. 2023.  A benchmark to understand the role of knowledge graphs on large language model’s accuracy for question answering on enterprise sql databases.  _arXiv preprint arXiv:2311.07509_. 
  * Soleimani et al. (2019)↑ Amir Soleimani, Christof Monz, and Marcel Worring. 2019.  [Bert for evidence retrieval and claim verification](http://arxiv.org/abs/1910.02655). 
  * Sun et al. (2020)↑ Tianxiang Sun, Yunfan Shao, Xipeng Qiu, Qipeng Guo, Yaru Hu, Xuanjing Huang, and Zheng Zhang. 2020.  Colake: Contextualized language and knowledge embedding.  _arXiv preprint arXiv:2010.00309_. 
  * Sun et al. (2021)↑ Yu Sun, Shuohuan Wang, Shikun Feng, Siyu Ding, Chao Pang, Junyuan Shang, Jiaxiang Liu, Xuyi Chen, Yanbin Zhao, Yuxiang Lu, Weixin Liu, Zhihua Wu, Weibao Gong, Jianzhong Liang, Zhizhou Shang, Peng Sun, Wei Liu, Xuan Ouyang, Dianhai Yu, Hao Tian, Hua Wu, and Haifeng Wang. 2021.  [Ernie 3.0: Large-scale knowledge enhanced pre-training for language understanding and generation](http://arxiv.org/abs/2107.02137). 
  * Touvron et al. (2023)↑ Hugo Touvron, Thibaut Lavril, Gautier Izacard, Xavier Martinet, Marie-Anne Lachaux, Timothée Lacroix, Baptiste Rozière, Naman Goyal, Eric Hambro, Faisal Azhar, et al. 2023.  Llama: Open and efficient foundation language models.  _arXiv preprint arXiv:2302.13971_. 
  * Wang et al. (2023)↑ Yile Wang, Peng Li, Maosong Sun, and Yang Liu. 2023.  Self-knowledge guided retrieval augmentation for large language models.  _arXiv preprint arXiv:2310.05002_. 
  * Yasunaga et al. (2022)↑ Michihiro Yasunaga, Antoine Bosselut, Hongyu Ren, Xikun Zhang, Christopher D Manning, Percy S Liang, and Jure Leskovec. 2022.  Deep bidirectional language-knowledge graph pretraining.  _Advances in Neural Information Processing Systems_ , 35:37309–37323. 
  * Zhang et al. (2022)↑ Xikun Zhang, Antoine Bosselut, Michihiro Yasunaga, Hongyu Ren, Percy Liang, Christopher D Manning, and Jure Leskovec. 2022.  Greaselm: Graph reasoning enhanced language models for question answering.  _arXiv preprint arXiv:2201.08860_. 


##  Appendix A Details of Datasets
Report issue for preceding element
The dataset was partitioned into training and testing subsets, with the training set employed for constructing the knowledge graph and verifying claim accuracy. Comprising 18,553 unique claims, each is linked to a corresponding fact-checking article and label.
Report issue for preceding element
The target variable, "truthfulness," is classified into three categories: "Supported," "Refuted," and "Not Enough Information" (NEI). The label distribution includes 7,137 "Refuted," 6,928 "Supported," and 4,488 "NEI."
Report issue for preceding element
Label assignment for "Supported," "Refuted," and "NEI" was performed following a meticulous cleaning process carried out by the authors of Menglong Yao et al. ([2022](https://arxiv.org/html/2408.08535v1#bib.bib25)). This process was conducted as the original labels derived from the fact-checking articles were marred by noise and inconsistency. Initially, the labels encompassed a broad spectrum of classifications, including "False," "Mostly False," and "Half True," totaling up to 75 different labels. This refinement was crucial as the original articles did not explicitly categorize claims into "Supported," "Refuted," or "NEI." This ambiguity could potentially impair the retrieval capabilities of large language models (LLMs). To mitigate this, we simplified the labels by mapping "Supported" to "True" and "Refuted" to "False" during the prompting and preprocessing phases.
Report issue for preceding element
##  Appendix B Prompt
Report issue for preceding element
The prompt used for all RAG systems is the following:
Report issue for preceding element
"Given the evidence provided below: {formatted_evidence}.   
Please evaluate the following claim: {claim}.   
Based on the evidence, should the claim be rated as ’True’, ’False’,   
or ’NEI’ (Not Enough Information)?"
Report issue for preceding element
The prompt used for all baseline zero shot setups is the following:
Report issue for preceding element
"Please evaluate the following claim: {claim}.   
Based on the evidence, should the claim be rated as ’True’, ’False’,   
or ’NEI’ (Not Enough Information)?"
Report issue for preceding element
##  Appendix C Language Model Parameters
Report issue for preceding element
In our experiments, we utilized the meta-llama/Llama-2-7b-chat-hf model from Hugging Face’s model hub. Our generation pipeline was configured to produce coherent and non-repetitive text. Key settings included a temperature of 0.3 to encourage predictability, a repetition penalty of 1.1 to avoid redundant content, and a limit of 200 new tokens per output to maintain focus. Custom stopping criteria were implemented to end text generation at specific tokens, ensuring outputs remained within the scope of our conversational framework.
Report issue for preceding element
##  Appendix D Computing Infrastructure
Report issue for preceding element
All computational experiments were conducted on a server configured with two NVIDIA RTX A6000 GPUs, each with 48 GB of GDDR6 memory, and two AMD EPYC 7513 32-core processors. The system also included 512 GB of DDR4 ECC RAM and a 960 GB Samsung PM983 NVMe SSD for storage.
Report issue for preceding element
##  Appendix E Community Statistics
Report issue for preceding element
We provide the knowledge graph community statistics with various top δ𝛿\deltaitalic_δ percent communities in Table [5](https://arxiv.org/html/2408.08535v1#A5.T5 "Table 5 ‣ Appendix E Community Statistics ‣ CommunityKG-RAG: Leveraging Community Structures in Knowledge Graphs for Advanced Retrieval-Augmented Generation in Fact-Checking"). These statistics demonstrate the multi-hop nature of our knowledge graphs through the metrics of average shortest path length and diameter. The average shortest path length, ranging from 4.03 to 4.28 across different community percentages, indicates that on average, multiple hops are required to traverse between nodes. The diameter values, ranging from 13 to 17, suggest the presence of long paths within the graphs, further supporting the existence of multi-hop pathways. These metrics confirm that our CommunityKG-RAG framework effectively leverages multi-hop connections, crucial for retrieving contextually rich and relevant information in fact-checking tasks.
Report issue for preceding element  
|  Metric  |  Value  |  
| --- | --- |  
|   |  Top 25 Percent  |  
|  Number of Nodes  |  20,092  |  
|  Number of Edges  |  60,770  |  
|  Avg. Degree  |  6.05  |  
|  Avg. Communities per Claim  |  2.05  |  
|  Avg. Nodes per Claim  |  5.62  |  
|  Avg. Shortest Path Length  |  4.28  |  
|  Diameter  |  17  |  
|   |  Top 50 Percent  |  
|  Number of Nodes  |  32,428  |  
|  Number of Edges  |  117,677  |  
|  Avg. Degree  |  7.26  |  
|  Avg. Communities per Claim  |  4.57  |  
|  Avg. Nodes per Claim  |  11.63  |  
|  Avg. Shortest Path Length  |  4.13  |  
|  Diameter  |  13  |  
|   |  Top 75 Percent  |  
|  Number of Nodes  |  40,669  |  
|  Number of Edges  |  159,703  |  
|  Avg. Degree  |  7.85  |  
|  Avg. Communities per Claim  |  6.85  |  
|  Avg. Nodes per Claim  |  16.60  |  
|  Avg. Shortest Path Length  |  4.07  |  
|  Diameter  |  14  |  
|   |  Top 100 Percent  |  
|  Number of Nodes  |  48,630  |  
|  Number of Edges  |  202,455  |  
|  Avg. Degree  |  8.33  |  
|  Avg. Communities per Claim  |  9.64  |  
|  Avg. Nodes per Claim  |  22.25  |  
|  Avg. Shortest Path Length  |  4.03  |  
|  Diameter  |  13  |  
Table 5: Community Statistics Report issue for preceding element
Report Issue
##### Report GitHub Issue
Title:
Content selection saved. Describe the issue below:
Description:
Submit without GitHubSubmit in GitHub
Report Issue for Selection
Generated by [ L A T E xml ![\[LOGO\]](/html/2408.08535v1/) ](https://math.nist.gov/~BMiller/LaTeXML/)
## Instructions for reporting errors
We are continuing to improve HTML versions of papers, and your feedback helps enhance accessibility and mobile support. To report errors in the HTML that will help us improve conversion and rendering, choose any of the methods listed below:
  * Click the "Report Issue" button.
  * Open a report feedback form via keyboard, use "**Ctrl + ?** ".
  * Make a text selection and click the "Report Issue for Selection" button near your cursor.
  * You can use Alt+Y to toggle on and Alt+Shift+Y to toggle off accessible reporting links at each section.


Our team has already identified [the following issues](https://github.com/arXiv/html_feedback/issues). We appreciate your time reviewing and reporting rendering errors we may not have found yet. Your efforts will help us improve the HTML versions for all readers, because disability should not be a barrier to accessing research. Thank you for your continued support in championing open access for all.
Have a free development cycle? Help support accessibility at arXiv! Our collaborators at LaTeXML maintain a [list of packages that need conversion](https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML), and welcome [developer contributions](https://github.com/brucemiller/LaTeXML/issues).

