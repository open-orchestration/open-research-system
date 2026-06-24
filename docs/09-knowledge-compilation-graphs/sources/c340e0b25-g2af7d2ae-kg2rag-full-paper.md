|     | Knowledge     |     | Graph-Guided |              | Retrieval |        | Augmented |            | Generation |        |     |     |
| --- | ------------- | --- | ------------ | ------------ | --------- | ------ | --------- | ---------- | ---------- | ------ | --- | --- |
|     | XiangrongZhu♣ |     |              | YuexiangXie♡ |           | YiLiu♣ |           | YaliangLi♡ |            | WeiHu♣ |     |     |
♣ StateKeyLaboratoryforNovelSoftwareTechnology,NanjingUniversity,China
♡
AlibabaGroup
|     |     | {xrzhu,  |                | yiliu07}.nju@gmail.com, |                             |     |     | whu@nju.edu.cn |     |     |     |     |
| --- | --- | -------- | -------------- | ----------------------- | --------------------------- | --- | --- | -------------- | --- | --- | --- | --- |
|     |     |          | {yuexiang.xyx, |                         | yaliang.li}@alibaba-inc.com |     |     |                |     |     |     |     |
|     |     | Abstract |                |                         |                             |     |     | SemanticRAG    |     |     |     |     |
Retrieval-augmented generation (RAG) has Document Retrievedchunks
emergedasapromisingtechnologyforaddress-
LLM-only
|     |     |     |     |     |     | Query |     |     |     |     | Response |     |
| --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | -------- | --- |
5202 beF 8  ]LC.sc[  1v46860.2052:viXra inghallucinationissuesintheresponsesgen-
| eratedbylargelanguagemodels(LLMs). |     |     |     |     | Ex- |     | User |     |     |     |     |     |
| ---------------------------------- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- |
LLM
istingstudiesonRAGprimarilyfocusonap-
GraphRAG
plyingsemantic-basedapproachestoretrieve
|     |     |     |     |     |     |     |     | KG  |     | Subgraph |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- |
isolatedrelevantchunks,whichignoretheirin-
| trinsicrelationships. |     |     | Inthispaper,wepropose |     |     |          |                           |     |     |     |          |     |
| --------------------- | --- | --- | --------------------- | --- | --- | -------- | ------------------------- | --- | --- | --- | -------- | --- |
|                       |     |     |                       |     |     | Figure1: | AcomparisonamongLLM-only, |     |     |     | Semantic |     |
a novel Knowledge Graph-Guided Retrieval RAG,andGraphRAGparadigms.
AugmentedGeneration(KG2RAG)framework
| that | utilizes   | knowledge     | graphs | (KGs)   | to pro- |               |     |         |             |     |      |         |
| ---- | ---------- | ------------- | ------ | ------- | ------- | ------------- | --- | ------- | ----------- | --- | ---- | ------- |
| vide | fact-level | relationships |        | between | chunks, |               |     |         |             |     |      |         |
|      |            |               |        |         |         | incorporating |     | it into | the prompts | of  | LLMs | for re- |
improvingthediversityandcoherenceofthe
sponsegeneration.
| retrieved |     | results. Specifically, |     | after | perform- |     |     |     |     |     |     |     |
| --------- | --- | ---------------------- | --- | ----- | -------- | --- | --- | --- | --- | --- | --- | --- |
ingasemantic-basedretrievaltoprovideseed Existing studies in RAG (Lewis et al., 2020;
chunks,KG2RAGemploysaKG-guidedchunk
|     |     |     |     |     |     | Yu, | 2022; | Purwar and | Sundar, | 2023; | Gao | et al., |
| --- | --- | --- | --- | --- | --- | --- | ----- | ---------- | ------- | ----- | --- | ------- |
expansionprocessandaKG-basedchunkorga- 2023;ZilettiandD’Ambrosi,2024), asshownin
nizationprocesstodeliverrelevantandimpor-
Fig.1,employkeyword-basedorsemantic-based
tantknowledgeinwell-organizedparagraphs.
approachestoretrievedocumentsorchunkshaving
ExtensiveexperimentsconductedontheHot-
|     |     |     |     |     |     | the | highest | similarities | to  | user queries. | However, |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------------ | --- | ------------- | -------- | --- |
potQAdatasetanditsvariantsdemonstratethe
|     |     |     |     |     |     | these | retrieved | chunks | can | be homogeneous |     | and |
| --- | --- | --- | --- | --- | --- | ----- | --------- | ------ | --- | -------------- | --- | --- |
advantagesofKG2RAGcomparedtoexisting
RAG-based approaches, in terms of both re- redundant,whichfailstoprovidetheintrinsicrela-
sponsequalityandretrievalquality. tionshipsamongthesechunksandcannotfurther
|     |     |     |     |     |     | activatethereasoningabilitiesofLLMs. |     |     |     |     | Further- |     |
| --- | --- | --- | --- | --- | --- | ------------------------------------ | --- | --- | --- | --- | -------- | --- |
1 Introduction
more,theretrievedchunksareoftendirectlycon-
Recently,largelanguagemodels(LLMs)(Lietal., catenated in the order of their similarity scores
|     |     |     |     |     |     | andfedintoLLMsaspartoftheprompts. |     |     |     |     |     | Sucha |
| --- | --- | --- | --- | --- | --- | --------------------------------- | --- | --- | --- | --- | --- | ----- |
2024;Renetal.,2024;Touvronetal.,2023;Brown
practicecanleadtoisolatedpiecesofinformation,
| et al., | 2020) | have achieved |     | remarkable | success |     |     |     |     |     |     |     |
| ------- | ----- | ------------- | --- | ---------- | ------- | --- | --- | --- | --- | --- | --- | --- |
across a broad range of real-world tasks, includ- limitingtheutilityofLLMsingeneratingcompre-
ing question answering (Sen et al., 2023), writ- hensiveandreliableresponses.
ingassistance(Calamoetal.,2023),codegenera- Knowledge graphs (KGs) (Auer et al., 2007;
tion (Cheng et al., 2024), and many others (Kad- Ji et al., 2022), as structured abstractions of real-
douretal.,2023;Wuetal.,2023). However,hallu- worldentitiesandtheirrelations,canbeexpected
cinations(Xuetal.,2024b;Liuetal.,2024a)inthe toeffectivelysupplementexistingsemantic-based
generatedresponsesbecomesacriticalchallenge, RAGapproachesbyintegratingstructuredfactual
which often results from containing outdated in- knowledge. KnowledgewithinaKG,represented
formationorlackingdomain-specificknowledge. in the form of triplets (head entity, relation, tail
Retrieval-augmentedgeneration(RAG)(Gaoetal., entity),isnaturallylinkedthroughoverlappingen-
2023; Fan et al., 2024) has emerged as a feasible tities. AsimplifiedworkflowforutilizingKGsin
solution to mitigate hallucinations by retrieving RAGisshowninFig.1,whererelevanttripletsare
relevantknowledgefromprovideddocumentsand retrievedtoaugmentthecontextforresponsegen-

erationinLLMs,providingfact-levelrelationships 2 Methodology
amongchunksandhighlightingimportantfactsthat
An overview of the workflow of KG2RAG is il-
maybemissedbysemantic-basedapproaches.
lustrated in Fig. 2. In the following subsections,
Shed light by such insights, in this pa-
weprovidemoredetailsfollowingtheworkflowof
per, we propose a novel Knowledge Graph-
KG2RAG,includingdocumentofflineprocessing
Guided Retrieval Augmented Generation frame-
(Sec.2.1),KG-enhancedchunkretrieval(Sec.2.2),
work, called KG2RAG. Specifically, we first per-
andKG-basedcontextorganization(Sec.2.3).
formchunkingandKG-chunkassociationduring
theofflineprocessingoftheprovideddocuments, 2.1 DocumentOfflineProcessing
establishing linkages between chunks and a spe-
Following the existing studies in RAG (Lewis
cific KG to capture the fact-level relationships
et al., 2020; Gao et al., 2023; Fan et al., 2024),
among these chunks. Based on the chunks and
all documents are first split into n chunks based
theKG,KG2RAGemploysKG-enhancedchunkre-
onthestructureofsentencesandparagraphsgiven
trieval,whichconsistsofasemantic-basedretrieval
a predefined chunk size, which can be given as
andgraph-guidedexpansion. Thesemantic-based
D = {c ,...,c }. These chunks can be further
1 n
retrieval prepares several seed chunks using em-
processed, for example, by adding relevant con-
beddingandrankingtechniques(Nussbaumetal.,
text (Jiang et al., 2023; Eibich et al., 2024), ex-
2024;LiandLi,2024). Theseseedchunksarethen
tractingmeta-information(Mombaertsetal.,2024)
usedtoextractarelevantsubgraphfromtheassoci-
(e.g.,title,abstract),andgeneratingcorresponding
ationKG,ontowhichwecanapplygraphtraversal
questions (Ma et al., 2023; Wang et al., 2024b).
algorithmstoincludethechunkscontainingover-
Since these chunk-enhancing techniques are or-
lappedorrelatedentitiesandtriplets. Suchadesign
thogonaltotheproposedmethodinthispaper,we
of graph-guided expansion provides a greater di-
recommendreferringtotheoriginalpaperformore
versity of retrieved chunks and a comprehensive
details. Hereafter, wecontinuetodenotethepro-
knowledgenetwork.
cessedchunksasD = {c ,...,c }.
1 n
After that, we incorporate a post-processing
To capture the rich fact-level relationships
stage named KG-based context organization in
among these chunks, we associate them with a
KG2RAG. On one hand, the KG-based context
KG,whichcanbeimplementedviathefollowing
organization serves as a filter to retain the most
approaches. IncaseswhereaKGisavailable,such
relevant information contained in the subgraph,
asinWebQSP(Yihetal.,2016)andCWQ(Talmor
thereby enhancing the informativeness of the re-
andBerant,2018),thechunk-KGassociationcan
trievedchunks. Ontheotherhand,itservesasan
beperformedthroughentityandrelationrecogni-
arrangertoorganizethechunksintointernallyco-
tionandlinkagealgorithms(Zhaoetal.,2023;Tian
herentparagraphswiththeknowledgegraphasa
et al., 2024). Another approach involves directly
skeleton. These semantically coherent and well-
extractingmultipleentitiesandrelationsfromthe
organizedchunksarefedintotheLLMsalongwith
chunks to form subgraphs, which can be used to
userqueriesforresponsegeneration.
combine into a complete graph. In this paper, to
We conduct a series of experiments on the
avoidrelianceonexistingKGs,weadoptthelatter
widely-usedHotpotQA(Yangetal.,2018)dataset
approach,implementingitbyprovidingappropri-
and its newly constructed variants to mitigate
ateprompts(refertoFig.3)toLLMs.
the impacts of prior knowledge on LLMs. We
Afterthisprocess,weprovidelinkagesbetween
adopt a distractor and a fullwiki setting, com-
chunksandaspecificKG,whichcanbegivenas
paring KG2RAG with several RAG-based ap-
proaches. The experimental results demonstrate G = {(h,r,t,c)|c ∈ D}, (1)
thatKG2RAGconsistentlyoutperformsbaselines
in terms of both response quality and retrieval where h, r, and t denote the head entity, relation,
quality. Moreover, we conduct an ablation study andtailentity,respectively,andcdenotesthechunk
to highlight the effectiveness of different mod- that derives the triplets. Note that the chunk-KG
ules in KG2RAG. The constructed dataset and association process is query-independent, which
sourcecodearereleasedathttps://github.com/ impliesthatitcanbeperformedoffline,onlyneeds
nju-websoft/KG2RAG to further promote the de- tobeconstructedonceforalldocuments,andsup-
velopmentandapplicationofKGsinRAG. portsincrementalupdatesfornewdocuments. As

Query:
In which part of New York City is the director of the romanticcomedy 'Big Stone
Gap' based?
Retrievedchunks
1 Big Stone Gap is a 2014 American drama romantic
|     | Semantic-based |     | comedy film written and directed by Adriana Trigiani. |     |     |     |     |     |     |     |
| --- | -------------- | --- | ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
Retrieval
Big Stone Gap had its world premiere at the Virginia
2
Film Festival on November 6, 2014.
I Love NY, also known as I Love New Year, is an
| Document |     |     | 3   |     |     |     |     |     |     |     |
| -------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Indian romantic comedy film directed by Radhika Rao.
…
+
Graph-guided
Expansion
Expandedchunks
Adriana Trigiani is an Italian American best-selling
+1 author andfilm directorbasedin Greenwich Village,
|     |     |     | New York City. |     |     |     | Organizedparagraphs |     |     |     |
| --- | --- | --- | -------------- | --- | --- | --- | ------------------- | --- | --- | --- |
Big Stone Gap is a 2014 American drama romantic
comedy film written and directed by Adriana Trigiani.
1
Thefilmhad its world premiere at the Virginia Film
√ Festival on November 6, 2014.Adriana Trigiani is an
Italian American best-selling author andfilm director
basedin Greenwich Village, New York City.
KG-basedContext
I Love NY, also known as I Love New Year, is an
|     |     |     |     |     | Organization |     | 2 Indian romantic comedy film directed by Radhika Rao. |     |     |     |
| --- | --- | --- | --- | --- | ------------ | --- | ------------------------------------------------------ | --- | --- | --- |
The main plot was taken from the Russian romantic
×
comedy "The Irony of Fate" (1976).
…
|     |     |     |     |     | Response: |     | LLMGeneration |     |     |     |
| --- | --- | --- | --- | --- | --------- | --- | ------------- | --- | --- | --- |
Greenwich Village, New York City.
WorkflowoftheproposedKG2RAG.
Figure2:
thedocumentofflineprocessingalignswithwhat LLMs for RAG. As discussed in Sec. 1, relying
vanilla RAG does, KG2RAG naturally supports solely on semantic-based retrieval may result in
addingnewdocumentstoorremovingdocuments isolatedchunks,missingcrucialfactualknowledge
from the existing knowledge base and KG effi- andtheintrinsicconnectionsamongthechunks. To
| ciently. |     |     |     |     |     | tackle | this, we regard | the retrieved | chunks | D as |
| -------- | --- | --- | --- | --- | --- | ------ | --------------- | ------------- | ------ | ---- |
q
|     |     |     |     |     |     | seed | chunks, and propose | a   | graph-guided | expan- |
| --- | --- | --- | --- | --- | --- | ---- | ------------------- | --- | ------------ | ------ |
2.2 KG-enhancedChunkRetrieval
sionprocess.
| GiventhechunksD |     | andtheassociatedKGG,the |     |     |     |     |     |     |     |     |
| --------------- | --- | ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
proposedKG2RAGsuggestsatwo-stageretrieval Graph-guidedExpansion Duringcommunica-
tionandthinkingprocesses,peopleoftenconnect
| process, | including | semantic-based |     | retrieval | and |     |     |     |     |     |
| -------- | --------- | -------------- | --- | --------- | --- | --- | --- | --- | --- | --- |
oneeventtoothersastheseeventsinvolvethesame
graph-guidedexpansion.
|     |     |     |     |     |     | entities,suchaspersonsandplaces. |     |     | Forexample, |     |
| --- | --- | --- | --- | --- | --- | -------------------------------- | --- | --- | ----------- | --- |
Semantic-basedRetrieval Duringthesemantic- Capitol Hill, Washington, D.C. connects our im-
based retrieval process, the semantic similarities pressions of Barack Obama, Donald Trump, and
betweenauserqueryq andallthechunkscanbe Joe Biden, as they all delivered their presidential
measuredas
inauguralspeechestherein2013,2017,and2021,
|     |     |             |     |       |     | respectively. | Shedlightbysuchinsights,KG2RAG |     |     |     |
| --- | --- | ----------- | --- | ----- | --- | ------------- | ------------------------------ | --- | --- | --- |
|     | S   | = {s(q,c)|c |     | ∈ D}, | (2) |               |                                |     |     |     |
suggestslinkingonechunktootherchunksthrough
wherethesimilarityfunctions(·)employsanem- theoverlappingorconnectedentitiesthattheycon-
tainforretrievedchunkexpansion.
beddingmodel(Nussbaumetal.,2024;LiandLi,
|          |          |     |       |            |            | Specifically,giventheretrievedchunksD |     |     |     | ⊆ D |
| -------- | -------- | --- | ----- | ---------- | ---------- | ------------------------------------- | --- | --- | --- | --- |
| 2024) to | transfer | the | query | and chunks | into high- |                                       |     |     |     | q   |
dimensionalrepresentations,followedbycomput- andtheKGG = {(h,r,t,c)|c ∈ D},wefirstget
therelevantsubgraphofD
| ingtheircosinesimilarity. |      |          |       |               |              |     |                | q asfollows: |         |        |
| ------------------------- | ---- | -------- | ----- | ------------- | ------------ | --- | -------------- | ------------ | ------- | ------ |
| The chunks                | with | the      | top-k | highest       | similarities |     | G0             |              |         |        |
|                           |      |          |       |               |              |     | = {(h,r,t,c)|c |              | ∈ D } ⊆ | G. (3) |
| to the query              | are  | selected | as    | the retrieved | chunks,      |     | q              |              | q       |        |
denotedbyD . Theseretrievedchunkscanbein- Afterthat,wetraversethem-hopneighborhood
q
togettheexpandedsubgraphGm,whichcan
| tegrated | into the | prompts | as  | context | and fed into | ofG |     |     |     |     |
| -------- | -------- | ------- | --- | ------- | ------------ | --- | --- | --- | --- | --- |
|          |          |         |     |         |              |     | q   |     | q   |     |

Prompt for TripletExtraction chunks. Suchadesignofgraph-guidedexpansion
helpspreventredundancyandexcessivehomogene-
Instruction:
ityamongtheretrievedandexpandedchunks,lead-
Extract informative triplets directly from the text following the
examples. Do not add any extra words, line breaks, or spaces. ing to greater diversity and the development of a
| Example 1: |     |     |     | morecomprehensiveknowledgenetwork. |     |     |     | Wepro- |
| ---------- | --- | --- | --- | ---------------------------------- | --- | --- | --- | ------ |
Text: Scott Derrickson (born July 16, 1966) is an American
|     |     |     |     | vide some | empirical | evidence | to further | confirm |
| --- | --- | --- | --- | --------- | --------- | -------- | ---------- | ------- |
director, screenwriter and producer.
| Triplets: |     |     |     | theeffectivenessoftheproposedgraph-guidedex- |     |     |     |     |
| --------- | --- | --- | --- | -------------------------------------------- | --- | --- | --- | --- |
<Scott Derrickson, born in, 1966>,
| <Scott Derrickson, nationality, America>, |     |     |     | pansioninSec.3.3. |     |     |     |     |
| ----------------------------------------- | --- | --- | --- | ----------------- | --- | --- | --- | --- |
<Scott Derrickson, occupation, director>,
<Scott Derrickson, occupation, screenwriter>, 2.3 KG-basedContextOrganization
<Scott Derrickson, occupation, producer>
| Example 2: |     |     |     | AftertheKG-enhancedchunkretrieval,KG2RAG |     |     |     |     |
| ---------- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | --- |
Text: A Kiss for Corliss is a 1949 American comedy film
|     |     |     |     | incorporates | a post-processing |     | stage | before re- |
| --- | --- | --- | --- | ------------ | ----------------- | --- | ----- | ---------- |
directed by Richard Wallace and written by Howard Dimsdale.
| Triplets:                         |     |     |     | sponsegenerationofLLMs,motivatedbythefol- |     |     |     |     |
| --------------------------------- | --- | --- | --- | ----------------------------------------- | --- | --- | --- | --- |
| <A Kiss for Corliss, year, 1949>, |     |     |     | lowingtwoconsiderations.                  |     |     |     |     |
<A Kiss for Corliss, country, America>,
Firstly,thenumberofexpandedchunksthrough
<A Kiss for Corliss, genre, comedy film>,
<A Kiss for Corliss, director, Richard Wallace>, the graph-guided expansion is tied to the triplets
<A Kiss for Corliss, writer, Howard Dimsdale>
containedintheexpandedsubgraph,whichcanbe
Target Text: <targettext> toolarge,potentiallyexceedingthecontextlength
Triplets:
andintroducingnoisethatmayobscurehelpfulin-
|     |          |                                |     | formation. | Secondly, | inspired | by human   | reading     |
| --- | -------- | ------------------------------ | --- | ---------- | --------- | -------- | ---------- | ----------- |
|     | Figure3: | Thepromptfortripletextraction. |     |            |           |          |            |             |
|     |          |                                |     | habits and | previous  | studies  | (Li, 2023; | Liu et al., |
2024b),providingsemanticallycoherentandwell-
| begivenas |     |     |     | organizedmaterialsascontextmakespositiveim- |     |     |     |     |
| --------- | --- | --- | --- | ------------------------------------------- | --- | --- | --- | --- |
pactsontheunderstandingandgenerationperfor-
|     | m   |     | 0,m), |     |     |     |     |     |
| --- | --- | --- | ----- | --- | --- | --- | --- | --- |
G = traverse(G,G (4) mance of LLMs. As a result, we propose a KG-
|       | q           |                    | q        |               |              |     |           |         |
| ----- | ----------- | ------------------ | -------- | ------------- | ------------ | --- | --------- | ------- |
|       |             |                    |          | based context | organization |     | module in | KG2RAG, |
| where | traverse(·) | can be implemented | with the |               |              |     |           |         |
whichservesasbothafilterandanarrangertomeet
breadth-firstsearch(BFS)algorithm,servingasa
theserequirements.
functionthatcapturesallentitiesinG0,correspond-
q
ingm-hopneighboringentities,andalledgeslink- Serving as a Filter Specifically, we first calcu-
ingtheseentitiestoformanexpandedsubgraph. latethesemanticsimilaritiesbetweentheexpanded
GiventheexpandedsubgraphGm,wecanread- chunks with the user query, according to Eq. (2).
q
out all the chunks associated with the graph (i.e., Basedonthesesimilarities,theexpandedsubgraph
Gmcanbetransformedintoanundirectedweighted
containingfactscorrespondingtothetripletsinthis
q
| graph)asfollows: |     |     |     | graphasfollows: |     |     |     |     |
| ---------------- | --- | --- | --- | --------------- | --- | --- | --- | --- |
Dm = {c|(h,r,t,c) ∈ Gq } ⊆ D, (5) Um = {(h ↔ t,rel : r,src : c,weight : s(q,c))
|         | q                                |     | m   | q   |            |        |     |     |
| ------- | -------------------------------- | --- | --- | --- | ---------- | ------ | --- | --- |
|         |                                  |     |     |     | |(h,r,t,c) | ∈ Gm}, |     |     |
| whereDm | isreferredtoastheexpandedchunks. |     |     |     |            | q      |     |     |
q
(6)
Discussions Severalsemantic-basedandcontext- where h ↔ t represents an undirected edge, at-
based approaches can also achieve chunk expan- tached with the corresponding relation and the
sion. For example, one can increase the value source chunk as meta information. We reuse the
of k in the aforementioned similarity-based re- semanticsimilaritiescalculatedinSec.2.2tosave
trieval process, or apply a context window ex- computingresources.
pansion (Jiang et al., 2023) (i.e., when a chunk Due to the cohesive nature of knowledge, Um
q
is retrieved, the chunks within the context win- cannaturallybedividedintopconnectedcompo-
dow are also recalled together). Different from nents, denoted by B ,1 ≤ i ≤ p, where nodes
i
these approaches, the proposed graph-guided ex- withineachconnectedcomponentB representen-
i
pansion gathers chunks that contain the same or titiesfromtheKG.Notethatmultipleedgesmay
relatedentitiesortriplets,withoutrequiringthese connect a pair of nodes due to redundant knowl-
expandedchunkstohavehighsemanticsimilarity edge,whichpromotesustogeneratethemaximum
tothequeryortobelocatedaroundtheretrieved spanningtree(MST)ofeachconnectedcomponent

tnemucoD# 12000
| forfiltering. |     | Thiscanbeformulatedas |     |     |     |     |     |     |     |     |     |     |     |
| ------------- | --- | --------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
10000
|     |     | T   | = MST(B | ).  | (7) |     | 8000 |     |     |     |     |     |     |
| --- | --- | --- | ------- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
|     |     |     | i       | i   |     |     |      |     |     |     |     |     |     |
6000
4000
Throughsuchafilteringprocess,weretainonlythe
|                                               |     |     |     |     |     |     | 2000 |     |     |     |     |     | #Triplet |
| --------------------------------------------- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | -------- |
| mostrelevantlinkinginformationbetweenentities |     |     |     |     |     |     | 0    |     |     |     |     |     |          |
|                                               |     |     |     |     |     |     | 0    | 10  | 20  |     | 30  | 40  | 50       |
andeliminateredundantedges,therebyenhancing (a) Distribution of documents according to triplet number.
knuhC# 105
theinformativenessoftheretrievedchunks.
104
| ServingasanArranger                        |     |     |     | WiththeKG-basedcon- |     |     | 103 |     |     |     |     |     |     |
| ------------------------------------------ | --- | --- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| textorganizationmodule,weaimtointegratethe |     |     |     |                     |     |     | 102 |     |     |     |     |     |     |
101
| retrievedchunksintointrinsicallyrelatedandself- |     |     |     |     |     |     |     |     |     |     |     |     | #Triplet |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- |
100
consistentparagraphswiththeKGastheskeleton.
|     |     |     |     |     |     |     | 0   | 5   | 10  |     | 15  | 20  | 25  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(b) Distribution of chunks according to triplet number.
Toachievethis,weprovidetworepresentations
foreachgeneratedMSTT ,includingatextrepre- Figure4: Statisticsoftripletextraction.
i
| sentationandatripletrepresentation. |     |     |     |     | Forthetext |     |     |     |     |     |     |     |     |
| ----------------------------------- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
representation,wepicktheedgewiththehighest
|     |     |     |     |     |     | HotpotQA-Full. |     |     | In the | distractor |     | setting, | a total |
| --- | --- | --- | --- | --- | --- | -------------- | --- | --- | ------ | ---------- | --- | -------- | ------- |
weightastheroot,andconcatenateallthechunks
|     |     |     |     |     |     | of  | ten documents |     | are provided |     | as supporting |     | ma- |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------------ | --- | ------------- | --- | --- |
linkedtotheedgesusingadepth-firstsearch(DFS)
algorithm to form a coherent paragraph. For the terials, including all useful knowledge as well as
tripletrepresentation,weconcatenatealltheedges someirrelevantcontent. Inthefullwikisetting,it
isrequiredtoidentifyusefulknowledgefromthe
| intheformof< |     | h,r,t | >withintheMST. |     |     |     |     |     |     |     |     |     |     |
| ------------ | --- | ----- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
entire66,581documentsextractedfromWikipedia.
WecalculatetherelevancescoresbetweenMSTs
and the user query based on their triplet repre- For the KG-chunk association, we provide a
sentations using a cross-encoder reranking func- manual prompt to Llama-3 (Dubey et al., 2024)
forextractingentitiesandrelationsfromthe66,581
tion(Xiaoetal.,2023):
|     |       |     |                |     |     | documents       |            | of HotpotQA, |            | resulting        |        | in a        | total of |
| --- | ----- | --- | -------------- | --- | --- | --------------- | ---------- | ------------ | ---------- | ---------------- | ------ | ----------- | -------- |
|     | R(q,T |     | ) = C(q,conc(T | )), | (8) |                 |            |              |            |                  |        |             |          |
|     |       | i   |                | i   |     | 211,356triplets |            |              | consisting | of98,226entities |        |             | and      |
|     |       |     |                |     |     | 19,813          | relations. |              | Each       | triplet          | in the | constructed |          |
whereC(·)isthecross-encoderrerankingfunction
|     |     |     |     |     |     | KG  | is linked | to  | its source | chunk. |     | We record | the |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | ---------- | ------ | --- | --------- | --- |
andconc(·)isusedtoobtainthetripletrepresenta-
numberoftripletsextractedfromeachchunkand
tions. Weusetripletrepresentationsinsteadoftext
document,andplotthecorrespondingdistributions
representationsbecausetripletsprovideaconcise
ofchunksanddocumentsinFig.4,whichshowsa
andstructuredrefinementofthekeyinformationas-
long-tailphenomenon.
sociatedwiththecorrespondingchunks,allowing
|     |     |     |     |     |     |     | Furthermore, |     | to alleviate |     | the dependence |     | on  |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ------------ | --- | -------------- | --- | --- |
relevancematchingtofocusonkeyinformation.
|             |           |                   |                             |              |         | prior     | knowledge |          | during | the       | generation  |     | process |
| ----------- | --------- | ----------------- | --------------------------- | ------------ | ------- | --------- | --------- | -------- | ------ | --------- | ----------- | --- | ------- |
| After       | computing |                   | the relevance               | scores,      | we sort |           |           |          |        |           |             |     |         |
|             |           |                   |                             |              |         | (i.e.,    | the       | training | corpus | of        | LLMs        | may | contain |
| theMSTs{T   |           | i |1 ≤            | i ≤ p}accordingtotheirrele- |              |         |           |           |          |        |           |             |     |         |
|             |           |                   |                             |              |         | Wikipedia |           | content) | and    | to better | demonstrate |     | the     |
| vance{R(q,T |           | )}totheuserqueryq |                             | indescending |         |           |           |          |        |           |             |     |         |
i
effectsofRAG,weconstructvariantsofHotpotQA.
order. Then,weincludetheirtextrepresentations
Specifically,foreachentity,werandomlyreplaceit
| inorderuntilthetop-k |     |     | constraintonthenumberof |     |     |     |     |     |     |     |     |     |     |
| -------------------- | --- | --- | ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
withanotherentityinthesamecategory,andthen
| chunks | has been | reached. |     | Finally, these | selected |     |     |     |     |     |     |     |     |
| ------ | -------- | -------- | --- | -------------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
updatethequeries,triplets,anddocumentsaccord-
chunksarefedintotheLLMsalongwiththeuser
ingly. Forexample,theentityFamilyGuycanbe
queryforresponsegeneration.
|     |     |     |     |     |     | replaced |     | with Rick | and | Morty, | and | all instances |     |
| --- | --- | --- | --- | --- | --- | -------- | --- | --------- | --- | ------ | --- | ------------- | --- |
3 Experiments of Family Guy contained in queries, triplets, and
|     |     |     |     |     |     | documents |     | would | be updated |     | to Rick | and | Morty. |
| --- | --- | --- | --- | --- | --- | --------- | --- | ----- | ---------- | --- | ------- | --- | ------ |
3.1 ExperimentSetup
Therefore,LLMshavetoidentifyandextractrel-
Datasets Weconductexperimentsonthebench- evant content from the documents rather than re-
markdatasetHotpotQA(Yangetal.,2018),where lyingonpriorknowledgeaboutFamilyGuyfrom
eachquerycanbeassociatedwithseveralmateri- trainingdatatocorrectlyanswerthequeries. Note
als(e.g.,relevantcontentinWikipedia)tohelpin there might generate lots of new triplets such as
response generation. The HotpotQA dataset con- (Rick and Morty, language, French), as the orig-
sistsoftwosettings, namedHotpotQA-Distand inal tail entity can be also transformed from En-

Hotpot-Dist Hotpot-Full Shuffle-Hotpot-Dist Shuffle-Hotpot-Full
Methods
F1 Precision Recall F1 Precision Recall F1 Precision Recall F1 Precision Recall
LLM-only 0.237 0.259 0.234 0.237 0.259 0.234 0.158 0.175 0.158 0.158 0.175 0.158
SemanticRAG 0.617 0.646 0.643 0.528 0.558 0.535 0.508 0.533 0.524 0.422 0.449 0.433
+Rerank 0.652 0.685 0.665 0.587 0.613 0.603 0.532 0.560 0.546 0.447 0.476 0.456
HybridRAG 0.653 0.676 0.655 0.551 0.582 0.558 0.520 0.548 0.534 0.443 0.473 0.446
LightRAG 0.293 0.288 0.480 0.261 0.259 0.364 0.285 0.284 0.404 0.202 0.199 0.293
GraphRAG 0.400 0.408 0.491 0.169 0.157 0.429 0.351 0.365 0.401 0.163 0.155 0.362
KG2RAG 0.663 0.690 0.683 0.631 0.665 0.643 0.545 0.572 0.566 0.507 0.539 0.512
Table1: ComparisonsintermsofresponsequalitybetweenKG2RAGandbaselines.
Hotpot-Dist Hotpot-Full Shuffle-Hotpot-Dist Shuffle-Hotpot-Full
Methods
F1 Precision Recall F1 Precision Recall F1 Precision Recall F1 Precision Recall
SemanticRAG 0.343 0.206 0.894 0.300 0.178 0.790 0.321 0.201 0.837 0.268 0.167 0.708
+Rerank 0.357 0.224 0.932 0.306 0.197 0.833 0339 0.213 0.886 0.286 0.179 0.754
HybridRAG 0.354 0.222 0.921 0.302 0.189 0.795 0.334 0.210 0.837 0.279 0.174 0.739
LightRAG 0.234 0.150 0.638 0.132 0.083 0.340 0.227 0.148 0.535 0.116 0.073 0.295
GraphRAG 0.255 0.167 0.594 0.180 0.113 0.470 0.210 0.138 0.482 0.199 0.126 0.510
KG2RAG 0.436 0.301 0.908 0.310 0.203 0.838 0.405 0.279 0.840 0.305 0.193 0.790
Table2: ComparisonsintermsofretrievalqualitybetweenKG2RAGandbaselines.
glishtoFrench. Theproducedvariantdatasetsare BM25 (Askari et al., 2023)) for chunk re-
denotedbyShuffle-HotpotQA-DistandShuffle- trieval. Theretrievedchunksaresubsequently
HotpotQA-Full,respectively. mergedthroughacross-encoderreranker.
EvaluationMetrics WecompareKG2RAGwith • GraphRAG (Edge et al., 2024), which con-
existingRAG-basedmethodsintermsofresponse structs a graph-based index with an LLM.
quality and retrieval quality, which can be influ- GraphRAGderivesaknowledgegraphfrom
enced by both the retrieved chunks and context the source documents and pre-generates
organization. Forretrievalquality,weusetheeval- communitysummariesforclusteredentities.
uation script provided by HotpotQA to measure Givenaquery,itgeneratespartialresponses
theF1score,precision,andrecallbetweenthere- with each related community summary and
trievedchunksandreferencedfacts. Forresponse aggregatesthemintothefinalanswer.
quality, we adopt the F1 score, precision, and re-
• LightRAG(Guoetal.,2024),whichactsasa
callasmetrics,comparingthegeneratedresponses
lightweightversionofGraphRAG.LightRAG
againstgroundtruthanswers.
extractsentitiesandrelationsfromthesource
Baselines In the experiments, we compare documentsandgeneratesashortdescription
KG2RAGwiththefollowingbaselinemethods: of eachentity forretrieval. Theretrieved in-
formation is unified with the query and fed
• LLM-only,whichdirectlyinstructsLLMsto intotheLLMforgeneration.
generateresponsestouserquerieswithoutany
ForKG2RAGandallbaselinemethods,weuse
additionalretrievalmechanisms.
LLaMA3-8B(Dubeyetal.,2024)astheLLMfor
• SemanticRAG(Jiangetal.,2023),whichem- KGconstructionandresponsegeneration,mxbai-
ploys a semantic-based approach to retrieve embed-large (Li and Li, 2024) as the embedding
relevant chunks. These chunks are concate- model,andbge-reranker-large(Xiaoetal.,2023)
natedintothepromptandfedintotheLLMs asthecross-encoderrerankerforbothHybridRAG
for response generation. For more details, and KG2RAG. The value of k is set to 10 unless
pleaserefertoSec.2.2. otherwisespecified.
3.2 ComparisonsandAnalyses
• Hybrid RAG (Gao et al., 2021), which
combinesasemantic-basedretrievalmethod Response Quality The comparisons in terms
withakeyword-basedretrievalmethod(e.g., of response quality between KG2RAG and the

|     |                 | ResponseQuality |             | RetrievalQuality |              |     |
| --- | --------------- | --------------- | ----------- | ---------------- | ------------ | --- |
|     |                 | F1 Precision    | Recall F1   | Precision        | Recall #Avg. |     |
|     | KG2RAG          | 0.663 0.690     | 0.683 0.436 | 0.301            | 0.908 8.11   |     |
|     | w/oorganization | 0.660 0.678     | 0.679 0.259 | 0.153            | 0.963 16.76  |     |
|     | w/oexpansion    | 0.626 0.653     | 0.645 0.473 | 0.341            | 0.842 4.41   |     |
Table3: ExperimentalresultsofanablationstudyconductedonHotpotQAinthedistractorsetting.
|     |                 | ResponseQuality |             | RetrievalQuality |              |     |
| --- | --------------- | --------------- | ----------- | ---------------- | ------------ | --- |
|     |                 | F1 Precision    | Recall F1   | Precision        | Recall #Avg. |     |
|     | KG2RAG          | 0.545 0.572     | 0.566 0.405 | 0.279            | 0.840 8.09   |     |
|     | w/oorganization | 0.538 0.563     | 0.560 0.182 | 0.102            | 0.962 24.56  |     |
|     | w/oexpansion    | 0.474 0.503     | 0.485 0.511 | 0.458            | 0.656 3.82   |     |
Table4: ExperimentalresultsofanablationstudyconductedonShuffle-HotpotQAinthedistractorsetting.
baselines are shown in Table 1. From the table, tively). In the fullwiki setting where identifying
we can observe that all methods utilizing RAG relevantchunksismorechallenging,ourproposed
achievesignificantimprovementscomparedtothe methodachievesconsistentimprovementsinboth
LLM-only approach, exceeding 29.1% improve- precisionandrecallcomparedtootherRAG-based
ments in F1 scores on the original HotpotQA methods. These results further confirm the effec-
tivenessofKG2RAGinprovidinghigh-qualityre-
and26.4%improvementsinF1scoresonShuffle-
HotpotQA. Among these RAG-based methods, trievalresultswiththehelpofKG.
KG2RAGachievesconsistentoutperformance,es-
|     |     |     | 3.3 FurtherDiscussions |     |     |     |
| --- | --- | --- | ---------------------- | --- | --- | --- |
peciallyinthefullwikisettingandontheShuffle-
| HotpotQAdataset. |     |     | AblationStudy | Weconductanablationstudyto |     |     |
| ---------------- | --- | --- | ------------- | -------------------------- | --- | --- |
In the fullwiki setting, a large pool of candi- demonstratethecontributionsofdifferentmodules
datedocuments(thousandsoftimesmorethanin inKG2RAG,includingKG-guidedexpansionand
the distractor setting) is provided to LLMs, ne- KG-basedcontextorganization. Theexperimental
cessitatinghigh-qualityretrievalresultsandeffec- results on the HotpotQA and Shuffle-HotpotQA
tive context organization. In such a challenging datasets in the distractor setting are shown in Ta-
setup, our proposed method KG2RAG achieves bles 3 and 4, where we also report the average
atleast8%improvementscomparedtobaselines, numberofretrievedchunks.
KG2RAG
demonstrating that enhances chunk re- From these results, we can observe that using
trievalthroughKG-guidedapproachesthatsurpass
onlyKG-guidedexpansionwithoutKG-basedcon-
semantic-basedandkeyword-basedmethods. Be- textorganization(denotedby“w/oorganization”in
sides, on the Shuffle-HotpotQA dataset, where thetable),KG2RAGachievessimilarperformance
LLMsshouldrelymoreonRAGratherthanprior intermsofanswerqualitybutsignificantlyworse
knowledge,ourproposedmethodachievesatleast
|     |     |     | retrieval | quality. The | reason is that, | without the |
| --- | --- | --- | --------- | ------------ | --------------- | ----------- |
2.5%and6.4%improvementsinthedistractorand KG-basedcontextorganizationmodule,thenum-
fullwikisettings,respectively. ber of retrieved chunks can be noticeably larger,
|     |     |     | potentially | containing | irrelevant chunks | that do |
| --- | --- | --- | ----------- | ---------- | ----------------- | ------- |
Retrieval Quality The experimental results not contribute positively to performance but con-
are shown in Table 2, which demonstrate that sume additional tokens. These findings confirm
KG2RAGstrikesafavorablebalancebetweenre- thecontributionoftheKG-basedcontextorganiza-
tionmoduleineffectivelyselectingandorganizing
trievalprecisionandrecall,highlightingtheeffec-
tivenessofKG-guidedexpansionandcontextorga- retrievedchunkstopreserverelevantinformation.
nization. Inthedistractorsetting,whereirrelevant With only the KG-based context organization
chunksarelimited,ourproposedmethodachieves module (denoted by “w/o expansion” in the ta-
similarperformanceinrecallbutsignificantlybet- ble), KG2RAG achieves high retrieval precision
terperformanceinprecision(morethan7.9%and andF1scorewithasignificantlysmallernumber
6.9%onHotpotQAandShuffle-HotpotQA,respec- ofchunks,butfailstoprovidebetterresponses,as

Semantic RAG
|     |     |     | F1  |     |     | Precision |     |     |     |        | Hybrid RAG |     |
| --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | ------ | ---------- | --- |
|     |     |     |     |     |     |           |     |     |     | Recall | KG2RAG     |     |
|     | 0.7 |     |     |     | 0.7 |           |     |     | 0.7 |        |            |     |
0.68
|     | 0.65 |     |     |     |     |     |     |     | 0.65 |     |     |     |
| --- | ---- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- |
0.66
0.64
|     | 0.6 |     |     |     |     |     |     |     | 0.6 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0.62
|     | 0.55 |     |      |      | 0.6 |     |      |      | 0.55 |     |           |     |
| --- | ---- | --- | ---- | ---- | --- | --- | ---- | ---- | ---- | --- | --------- | --- |
|     |      | k=5 | k=10 | k=15 |     | k=5 | k=10 | k=15 |      | k=5 | k=10 k=15 |     |
(a)ResponseQuality
|     |     |     | F1  |     |     | Precision |     |     |     | Recall |     |     |
| --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | ------ | --- | --- |
|     | 0.6 |     |     |     | 0.4 |           |     |     | 1   |        |     |     |
0.95
0.5
0.3
0.9
0.4
|     |     |     |     |     | 0.2 |     |     |     | 0.85 |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- |
0.3
0.8
|     | 0.2 |     |      |      | 0.1 |     |      |      | 0.75 |     |           |     |
| --- | --- | --- | ---- | ---- | --- | --- | ---- | ---- | ---- | --- | --------- | --- |
|     |     | k=5 | k=10 | k=15 |     | k=5 | k=10 | k=15 |      | k=5 | k=10 k=15 |     |
(b)RetrievalQuality
Figure5: Experimentalresultswithvaryingtop-konHotpotQAindistractorsetting.
|     |     |     |     | ResponseQuality |           |        |       | RetrievalQuality |     |              |      |     |
| --- | --- | --- | --- | --------------- | --------- | ------ | ----- | ---------------- | --- | ------------ | ---- | --- |
|     |     |     |     | F1              | Precision | Recall | F1    | Precision        |     | Recall #Avg. |      |     |
|     |     |     | m=1 | 0.663           | 0.690     | 0.683  | 0.436 | 0.301            |     | 0.908        | 8.11 |     |
|     |     |     | m=2 | 0.656           | 0.681     | 0.674  | 0.420 | 0.291            |     | 0.917        | 8.53 |     |
|     |     |     | m=3 | 0.658           | 0.678     | 0.675  | 0.421 | 0.284            |     | 0.924        | 8.19 |     |
Table5: ExperimentalresultsonHotpotQAinthedistractorsettingwithvaryingm.
some necessary chunks may not be retrieved us- Performancew.r.t. Varyingm InKG2RAG,m
ingonlysemantic-basedapproaches. Theseresults servesasthehyperparameterforgraphexpansion,
confirm the importance of the KG-guided expan- balancingthetrade-offbetweenretrievalprecision
sionmoduleinsuccessfullyleveragingKGtocap- andrecall. Wesetthem-hopvalueto1inthepre-
ture fact-level relationships between chunks and vious experiments. To further explore the effects
retrieve key information that might be missed by ofm,weconductexperimentswithvaryingmon
semantic-basedapproaches. HotpotQA dataset. The results are shown in Ta-
|     |     |     |     |     |     |     | ble | 5. These | results | indicate | that setting | m = 1 |
| --- | --- | --- | --- | --- | --- | --- | --- | -------- | ------- | -------- | ------------ | ----- |
Performance w.r.t. Varying k We conduct ex- isappropriatefortheexperiments,andKG2RAG
perimentswithvaryingtop-k valuesonHotpotQA showslowsensitivitytothehyperparameterm.
| in the | distractor |     | setting. | The | experimental | re- |     |     |     |     |     |     |
| ------ | ---------- | --- | -------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
sultsareshowninFig.5. Fromthesefigures, we RobustnessAnalysis Tofurtherconfirmthero-
bustnessofKG2RAGwithquality-limitedKGs,we
canobservethatKG2RAGmaintainssuperiorper-
randomlydrop5%or10%ofthetripletsfromthe
| formance |     | compared | to baselines |     | with | different k. |     |     |     |     |     |     |
| -------- | --- | -------- | ------------ | --- | ---- | ------------ | --- | --- | --- | --- | --- | --- |
When k is set to a suitable value (e.g., 5 or 10), constructedKG,andshowtheexperimentalresults
TheresultsdemonstratethatKG2RAG
| KG2RAG |     | ensures | the efficient |     | retrieval | of high- | inTable6. |     |        |             |           |         |
| ------ | --- | ------- | ------------- | --- | --------- | -------- | --------- | --- | ------ | ----------- | --------- | ------- |
|        |     |         |               |     |           |          | maintains |     | robust | performance | even with | quality |
qualitychunks,therebyprovidingcoherentandcon-
limitationsandoutperformsthebaselines.
| textually |     | consistent | contexts | for | generating | high- |     |     |     |     |     |     |
| --------- | --- | ---------- | -------- | --- | ---------- | ----- | --- | --- | --- | --- | --- | --- |
qualityresponses.
4 RelatedWork
| However,whenk |     |     | issettoatoolargevalue(e.g., |     |     |     |     |     |     |     |     |     |
| ------------- | --- | --- | --------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
15), although the retrieval recall significantly im- Retrieval-augmented Generation To address
proves,thequalityofthegeneratedresponsesdoes theissuesofhallucinations(Xuetal.,2024b;Liu
notincreaseproportionally,whichindicatessimply etal.,2024a)duetoalackofcorrespondingknowl-
increasingthenumberofchunkscannotalwaysre- edgeorcontainingoutdatedknowledge,retrieval-
sult in a better retrieval recall ratio and response augmentedgeneration(RAG)(Gaoetal.,2023;Fan
quality. KG2RAGexhibitstheleastsensitivityto etal.,2024)hasbeenproposedforretrievingrele-
thehyperparameterkcomparedtobaselines,which vantchunksfromapoolofcandidatedocumentsto
| makestheRAGprocessrobust. |     |     |     |     |     |     | assistLLMgeneration. |     |     |     |     |     |
| ------------------------- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | --- | --- | --- |

|     |     |     |           |     | ResponseQuality |           |        |       | RetrievalQuality |       |        |     |     |
| --- | --- | --- | --------- | --- | --------------- | --------- | ------ | ----- | ---------------- | ----- | ------ | --- | --- |
|     |     |     |           |     | F1              | Precision | Recall | F1    | Precision        |       | Recall |     |     |
|     |     |     | HybridRAG |     | 0.653           | 0.676     | 0.655  | 0.354 |                  | 0.222 | 0.921  |     |     |
|     |     |     | KG2RAG    |     | 0.663           | 0.690     | 0.683  | 0.436 |                  | 0.301 | 0.908  |     |     |
|     |     |     | −5%       |     | 0.662           | 0.681     | 0.676  | 0.434 |                  | 0.306 | 0.898  |     |     |
|     |     |     | −10%      |     | 0.654           | 0.688     | 0.682  | 0.432 |                  | 0.305 | 0.890  |     |     |
Table6: ExperimentalresultsonHotpotQAinthedistractorsettingwithtripletsdropped.
InatypicalRAGsystem(Lewisetal.,2020),the mentKGconsistingofpageandpassagenodes,and
documentsarefirstsegmentedintochunksbased links passage nodes with TF-IDF. The document
onlengthsandstructures, andthenencodedwith KGisemployedforretrievalexpansion. Thedocu-
an embedding model (Nussbaum et al., 2024; Li mentKGconstructedbyKGPisbasedonsentence-
and Li, 2024) and indexed for efficient retrieval. level text similarity, which essentially functions
Inspired by the idea of sliding windows (Jiao, similarlytosimplyexpandingthecontextwindow.
2006), sentence window retrieval (Jiang et al., GraphRAG (Edge et al., 2024) targets at query-
2023;Eibichetal.,2024)fetchestheneighboring focusedsummarizationtasks. GraphRAGextracts
chunks around the retrieved chunks and concate- KGs automatically from the document base with
natesthemintoasinglelargerchunkforcontexten- anLLMandanalyzesthesemanticstructureofthe
richment. However,sentencewindowretrievalonly datasetbeforequerying,bysplittingtheKGfrom
considers the physical proximity of text chunks differentlevelanddetectinglinkednodeshierarchi-
within the same document. Different from exist- cally. Different from previous studies, KG2RAG
ingstudies,KG2RAGperformsretrievalexpansion aimstoenhanceRAGwiththefact-levelstructure
based on factual associations among chunks that andfactualknowledgeofKGs.
maybeacrossmultipledocuments.
| Reranking(Ampazis,2024;Glassetal.,2022)is |     |     |     |     |     |     | 5   | Conclusion |     |     |     |     |     |
| ----------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- |
acriticaltechniqueininformationretrieval(Grems,
Inthispaper,weproposeKG2RAG,anovelframe-
| 1962;Kuoetal.,2024). |     |     | InRAGsystems,feeding |     |     |     |     |     |     |     |     |     |     |
| -------------------- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
workdesignedtoenhancetheperformanceofRAG
| the retrieved                                 | chunks         |      | along         | with      | the queries | into   |                             |         |           |               |                  |           |           |
| --------------------------------------------- | -------------- | ---- | ------------- | --------- | ----------- | ------ | --------------------------- | ------- | --------- | ------------- | ---------------- | --------- | --------- |
|                                               |                |      |               |           |             |        | throughtheintegrationofKGs. |         |           |               | Weintroducelink- |           |           |
| a deep                                        | learning-based |      | cross-encoder |           | (Xiao       | et     | al.,                        |         |           |               |                  |           |           |
|                                               |                |      |               |           |             |        | ages                        | between |           | chunks and    | a specific       |           | KG, which |
| 2023) can                                     | measure        |      | the semantic  |           | relevance   | more   |                             |         |           |               |                  |           |           |
|                                               |                |      |               |           |             |        | help                        | in      | providing | fact-level    | relationships    |           | among     |
| precisely,therebyenhancingboththeretrievaland |                |      |               |           |             |        |                             |         |           |               | KG2RAG           |           |           |
|                                               |                |      |               |           |             |        | these                       | chunks. |           | Consequently, |                  |           | suggests  |
| generation                                    | quality.       |      | KG2RAG        | organizes |             | the    | re-                         |         |           |               |                  |           |           |
|                                               |                |      |               |           |             |        | performing                  |         | the       | KG-guided     | chunk            | expansion | and       |
| trieved                                       | chunks         | into | paragraphs    | with      | KGs         | as the |                             |         |           |               |                  |           |           |
theKG-basedcontextorganizationbasedonseed
skeleton,allowingafine-grainedmeasurementof
|     |     |     |     |     |     |     | chunks |     | retrieved | by semantic-based |     | retrieval | ap- |
| --- | --- | --- | --- | --- | --- | --- | ------ | --- | --------- | ----------------- | --- | --------- | --- |
paragraph-levelrelevancetoqueries.
|                        |     |     |     |     |              |     | proaches. |     | Through | these    | processes,    | the      | retrieved |
| ---------------------- | --- | --- | --- | --- | ------------ | --- | --------- | --- | ------- | -------- | ------------- | -------- | --------- |
|                        |     |     |     |     |              |     | chunks    |     | become  | diverse, | intrinsically | related, | and       |
| LLMswithKnowledgeGraph |     |     |     |     | LLM(Lietal., |     |           |     |         |          |               |          |           |
self-consistent,formingwell-organizedparagraphs
| 2024; Ren | et al., | 2024) | is one | of  | the most | repre- |     |     |     |     |     |     |     |
| --------- | ------- | ----- | ------ | --- | -------- | ------ | --- | --- | --- | --- | --- | --- | --- |
thatcanbefedintoLLMsforhigh-qualityresponse
sentativeachievementsofcontemporaryartificial
KG2RAG
|              |       |     |        |             |     |           | generation. |     | We  | compare |     | with | existing |
| ------------ | ----- | --- | ------ | ----------- | --- | --------- | ----------- | --- | --- | ------- | --- | ---- | -------- |
| intelligence | (AI). | KGs | (Ji et | al., 2022), |     | as graph- |             |     |     |         |     |      |          |
RAG-basedapproaches,demonstratingitssuperior
| structured | relational |     | databases, | serve | as  | a crucial |     |     |     |     |     |     |     |
| ---------- | ---------- | --- | ---------- | ----- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
performanceinbothresponsequalityandretrieval
| data infrastructure |     | for | AI applications. |     |     | Research |          |     |                                      |     |     |     |     |
| ------------------- | --- | --- | ---------------- | --- | --- | -------- | -------- | --- | ------------------------------------ | --- | --- | --- | --- |
|                     |     |     |                  |     |     |          | quality. |     | Anablationstudyisalsoconductedtofur- |     |     |     |     |
indicatesthatLLMshavethepotentialtoaddress
therconfirmthecontributionsofKG-guidedchunk
tasksrelatedtoKGs,suchasknowledgegraphcom-
expansionandKG-basedcontextorganization,in-
| pletion | (Liu et | al., 2024c) | and | knowledge |     | graph |     |     |     |     |     |     |     |
| ------- | ------- | ----------- | --- | --------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
dicatingthatthesetwomodulescollaborativelyen-
questionanswering(Senetal.,2023).
hancetheeffectivenessofKG2RAG.
Recently,theresearchcommunitybeginstoex-
plore how KGs can be used to enhance the gen- Acknowledgments
| eration | capability | of  | LLMs | (Wang | et al., | 2024a; |     |     |     |     |     |     |     |
| ------- | ---------- | --- | ---- | ----- | ------- | ------ | --- | --- | --- | --- | --- | --- | --- |
Edge et al., 2024; Xu et al., 2024a). For exam- This work is supported by the National Natural
ple, KGP (Wang et al., 2024a) constructs a docu- ScienceFoundationofChina(No. 62272219).

Limitations
AbhimanyuDubey,AbhinavJauhri,AbhinavPandey,
AbhishekKadian,AhmadAl-Dahle,AieshaLetman,
Retrieval-augmented generation (RAG) is a sys- Akhil Mathur, Alan Schelten, Amy Yang, Angela
tematicengineeringframeworkthatcanberefined Fan,AnirudhGoyal,AnthonyHartshorn,AoboYang,
frommultipleperspectives,includingqueryrewrit- ArchiMitra, ArchieSravankumar, ArtemKorenev,
ArthurHinsvark,ArunRao,AstonZhang,Aurélien
| ing (Xiao | et  | al., 2023), |     | retrieval | optimization |     |            |     |        |            |     |              |      |
| --------- | --- | ----------- | --- | --------- | ------------ | --- | ---------- | --- | ------ | ---------- | --- | ------------ | ---- |
|           |     |             |     |           |              |     | Rodriguez, |     | Austen | Gregerson, |     | Ava Spataru, | Bap- |
(Eibichetal.,2024),multi-turndialogue (Yaoetal., tiste Rozière, Bethany Biron, Binh Tang, Bobbie
2023)andsoon(Gaoetal.,2023). KG2RAGonly Chern,CharlotteCaucheteux,ChayaNayak,Chloe
focuses on the part of retrieval optimization and Bi,ChrisMarra,ChrisMcConnell,ChristianKeller,
|     |     |     |     |     |     |     | Christophe |     | Touret, | Chunyang |     | Wu, Corinne | Wong, |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ------- | -------- | --- | ----------- | ----- |
aimstoperformKG-guidedretrievalexpansionand
CristianCantonFerrer,CyrusNikolaidis,DamienAl-
| KG-based | context | organization |     | to  | enhance | RAG |     |     |     |     |     |     |     |
| -------- | ------- | ------------ | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
lonsius,DanielSong,DaniellePintz,DannyLivshits,
with the structured factual knowledge from KGs, David Esiobu, Dhruv Choudhary, Dhruv Mahajan,
DiegoGarcia-Olano,DiegoPerino,DieuwkeHupkes,
| without | optimizing | other | modules. |     | However, | the |     |     |     |     |     |     |     |
| ------- | ---------- | ----- | -------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
proposedKG2RAGisorthogonalandcompatible EgorLakomkin,EhabAlBadawy,ElinaLobanova,
EmilyDinan,EricMichaelSmith,FilipRadenovic,
| withtheaforementionedmodules. |     |     |     |     | Inthefuture,we |     |     |     |     |     |     |     |     |
| ----------------------------- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
FrankZhang,GabrielSynnaeve,GabrielleLee,Geor-
will develop KG2RAG into a plug-and-play tool giaLewisAnderson,GraemeNail,GrégoireMialon,
GuanPang,GuillemCucurell,HaileyNguyen,Han-
thatcanbeeasilyintegratedwithotherapproaches,
therebybetterfacilitatingtheresearchcommunity. nahKorevaar,HuXu,HugoTouvron,IliyanZarov,
|     |     |     |     |     |     |     | Imanol | Arrieta |     | Ibarra, Isabel | M.  | Kloumann, | Ishan |
| --- | --- | --- | --- | --- | --- | --- | ------ | ------- | --- | -------------- | --- | --------- | ----- |
Misra,IvanEvtimov,JadeCopet,JaewonLee,Jan
Geffert,JanaVranes,JasonPark,JayMahadeokar,
References
|     |     |     |     |     |     |     | Jeet | Shah, | Jelmer | van der | Linde, | Jennifer | Billock, |
| --- | --- | --- | --- | --- | --- | --- | ---- | ----- | ------ | ------- | ------ | -------- | -------- |
NicholasAmpazis.2024. ImprovingRAGqualityfor Jenny Hong, Jenya Lee, Jeremy Fu, Jianfeng Chi,
largelanguagemodelswithtopic-enhancedrerank- Jianyu Huang, Jiawen Liu, Jie Wang, Jiecao Yu,
|      |          |        |      |       |        |        | Joanna | Bitton, |     | Joe Spisak, | Jongsoo | Park, | Joseph       |
| ---- | -------- | ------ | ---- | ----- | ------ | ------ | ------ | ------- | --- | ----------- | ------- | ----- | ------------ |
| ing. | In AIAI, | volume | 712, | pages | 74–87, | Corfu, |        |         |     |             |         |       |              |
|      |          |        |      |       |        |        | Rocca, | Joshua  |     | Johnstun,   | Joshua  | Saxe, | Junteng Jia, |
Greece.Springer.
|     |     |     |     |     |     |     | Kalyan | Vasuden |     | Alwala, | Kartikeya | Upasani, | Kate |
| --- | --- | --- | --- | --- | --- | --- | ------ | ------- | --- | ------- | --------- | -------- | ---- |
ArianAskari,AminAbolghasemi,GabriellaPasi,Wes- Plawiak,KeLi,KennethHeafield,KevinStone,and
selKraaij,andSuzanVerberne.2023. Injectingthe etal.2024. TheLlama3herdofmodels. CoRR.
BM25scoreastextimprovesBERT-basedre-rankers.
|     |     |     |     |     |     |     | Darren | Edge, | Ha  | Trinh, | Newman | Cheng, | Joshua |
| --- | --- | --- | --- | --- | --- | --- | ------ | ----- | --- | ------ | ------ | ------ | ------ |
CoRR.
|     |     |     |     |     |     |     | Bradley, |     | Alex | Chao, Apurva | Mody, | Steven | Truitt, |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | ---- | ------------ | ----- | ------ | ------- |
Sören Auer, Christian Bizer, Georgi Kobilarov, Jens andJonathanLarson.2024. Fromlocaltoglobal: A
Lehmann,RichardCyganiak,andZacharyG.Ives. graphRAGapproachtoquery-focusedsummariza-
| 2007. | DBpedia:Anucleusforawebofopendata. |     |     |     |     | In  | tion. | CoRR. |     |     |     |     |     |
| ----- | ---------------------------------- | --- | --- | --- | --- | --- | ----- | ----- | --- | --- | --- | --- | --- |
ISWC,volume4825,pages722–735,Busan,Korea.
|     |     |     |     |     |     |     | Matous | Eibich, | Shivay | Nagpal, | and | Alexander | Fred- |
| --- | --- | --- | --- | --- | --- | --- | ------ | ------- | ------ | ------- | --- | --------- | ----- |
Springer.
|     |     |     |     |     |     |     | Ojala.2024. |     | ARAGOG:AdvancedRAGoutputgrad- |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ----------------------------- | --- | --- | --- | --- |
ing. CoRR.
TomB.Brown,BenjaminMann,NickRyder,Melanie
| Subbiah, | Jared | Kaplan, | Prafulla | Dhariwal, |     | Arvind |     |     |     |     |     |     |     |
| -------- | ----- | ------- | -------- | --------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
WenqiFan,YujuanDing,LiangboNing,ShijieWang,
Neelakantan,PranavShyam,GirishSastry,Amanda
HengyunLi,DaweiYin,Tat-SengChua,andQingLi.
| Askell,  | Sandhini | Agarwal, |           | Ariel    | Herbert-Voss, |        |                                         |                          |     |     |     |     |         |
| -------- | -------- | -------- | --------- | -------- | ------------- | ------ | --------------------------------------- | ------------------------ | --- | --- | --- | --- | ------- |
|          |          |          |           |          |               |        | 2024.                                   | AsurveyonRAGmeetingLLMs: |     |     |     |     | Towards |
| Gretchen | Krueger, | Tom      | Henighan, |          | Rewon         | Child, |                                         |                          |     |     |     |     |         |
|          |          |          |           |          |               |        | retrieval-augmentedlargelanguagemodels. |                          |     |     |     |     | InKDD,  |
| Aditya   | Ramesh,  | Daniel   | M.        | Ziegler, | Jeffrey       | Wu,    |                                         |                          |     |     |     |     |         |
pages6491–6501,Barcelona,Spain.ACM.
ClemensWinter,ChristopherHesse,MarkChen,Eric
Sigler,MateuszLitwin,ScottGray,BenjaminChess, LuyuGao,ZhuyunDai,TongfeiChen,ZhenFan,Ben-
| Jack Clark,   | Christopher |      | Berner,    | Sam | McCandlish, |         |                                    |     |     |     |     |     |         |
| ------------- | ----------- | ---- | ---------- | --- | ----------- | ------- | ---------------------------------- | --- | --- | --- | --- | --- | ------- |
|               |             |      |            |     |             |         | jaminVanDurme,andJamieCallan.2021. |     |     |     |     |     | Comple- |
| Alec Radford, |             | Ilya | Sutskever, | and | Dario       | Amodei. |                                    |     |     |     |     |     |         |
mentlexicalretrievalmodelwithsemanticresidual
2020. Language models are few-shot learners. In embeddings. In ECIR, volume 12656, pages 146–
| NeurIPS,Virtual.CurranAssociates. |     |     |     |     |     |     | 160,Glasgow,UK.Springer. |     |     |     |     |     |     |
| --------------------------------- | --- | --- | --- | --- | --- | --- | ------------------------ | --- | --- | --- | --- | --- | --- |
MarcoCalamo,FrancescaDeLuzi,MattiaMacrì,Tom- Yunfan Gao, Yun Xiong, Xinyu Gao, Kangxiang Jia,
masoMencattini,andMassimoMecella.2023. CI- JinliuPan,YuxiBi,YiDai,JiaweiSun,QianyuGuo,
CERO:AGPT2-basedwritingassistanttoinvestigate Meng Wang, and Haofen Wang. 2023. Retrieval-
theeffectivenessofspecializedLLMs’applications augmentedgenerationforlargelanguagemodels: A
| ine-justice. | InECAI,volume372,pages3196–3203, |     |     |     |     |     |         |       |     |     |     |     |     |
| ------------ | -------------------------------- | --- | --- | --- | --- | --- | ------- | ----- | --- | --- | --- | --- | --- |
|              |                                  |     |     |     |     |     | survey. | CoRR. |     |     |     |     |     |
Kraków,Poland.IOS.
MichaelR.Glass,GaetanoRossiello,Md.FaisalMah-
WeiCheng,YuhanWu,andWeiHu.2024. Dataflow- bub Chowdhury, Ankita Naik, Pengshan Cai, and
guided retrieval augmentation for repository-level AlfioGliozzo.2022. Re2G:Retrieve,rerank,gener-
code completion. In ACL, pages 7957–7977, ate. InNAACL,pages2701–2715,Seattle,WA,USA.
| Bangkok,Thailand.ACL. |     |     |     |     |     |     | ACL. |     |     |     |     |     |     |
| --------------------- | --- | --- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |

Mandalay Grems. 1962. A survey of languages and HanchaoLiu,WenyuanXue,YifeiChen,DapengChen,
systems for information retrieval. Commun. ACM, Xiutian Zhao, Ke Wang, Liping Hou, Rongjun Li,
| 5(1):43–46. |     |     |     |     |     | andWeiPeng.2024a.           |     |     | Asurveyonhallucinationin |       |     |     |
| ----------- | --- | --- | --- | --- | --- | --------------------------- | --- | --- | ------------------------ | ----- | --- | --- |
|             |     |     |     |     |     | largevision-languagemodels. |     |     |                          | CoRR. |     |     |
ZiruiGuo,LianghaoXia,YanhuaYu,TuAo,andChao
Huang.2024. LightRAG:Simpleandfastretrieval- NelsonF.Liu,KevinLin,JohnHewitt,AshwinParan-
augmentedgeneration. CoRR. jape,MicheleBevilacqua,FabioPetroni,andPercy
|     |     |     |     |     |     | Liang. | 2024b. | Lost | in the middle: |     | How language |     |
| --- | --- | --- | --- | --- | --- | ------ | ------ | ---- | -------------- | --- | ------------ | --- |
Shaoxiong Ji, Shirui Pan, Erik Cambria, Pekka Mart- models use long contexts. Trans. Assoc. Comput.
Linguistics,12:157–173.
| tinen, and  | Philip                               | S. Yu. 2022. | A   | survey | on knowl- |     |     |     |     |     |     |     |
| ----------- | ------------------------------------ | ------------ | --- | ------ | --------- | --- | --- | --- | --- | --- | --- | --- |
| edgegraphs: | Representation,acquisition,andappli- |              |     |        |           |     |     |     |     |     |     |     |
cations. IEEETrans.NeuralNetworksLearn.Syst., YangLiu,XiaobinTian,ZequnSun,andWeiHu.2024c.
33(2):494–514. Finetuninggenerativelargelanguagemodelswithdis-
criminationinstructionsforknowledgegraphcom-
|     |     |     |     |     |     | pletion. | InISWC,Baltimore,MD,USA.Springer. |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | -------- | --------------------------------- | --- | --- | --- | --- | --- |
ZhengbaoJiang,FrankF.Xu,LuyuGao,ZhiqingSun,
| Qian Liu,                    | Jane Dwivedi-Yu, |     | Yiming | Yang,           | Jamie |            |       |       |           |     |         |       |
| ---------------------------- | ---------------- | --- | ------ | --------------- | ----- | ---------- | ----- | ----- | --------- | --- | ------- | ----- |
|                              |                  |     |        |                 |       | Xinbei Ma, | Yeyun | Gong, | Pengcheng |     | He, Hai | Zhao, |
| Callan,andGrahamNeubig.2023. |                  |     |        | Activeretrieval |       |            |       |       |           |     |         |       |
augmented generation. In EMNLP, pages 7969– andNanDuan.2023. Queryrewritingforretrieval-
| 7992,Singapore.ACL. |     |     |     |     |     | augmentedlargelanguagemodels. |     |     |     | CoRR. |     |     |
| ------------------- | --- | --- | --- | --- | --- | ----------------------------- | --- | --- | --- | ----- | --- | --- |
LaurentMombaerts,TerryDing,AdiBanerjee,Florian
| YishanJiao.2006. |     | Maintainingstreamstatisticsover |     |     |     |     |     |     |     |     |     |     |
| ---------------- | --- | ------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Felice,JonathanTaws,andTarikBorogovac.2024.
| multiscaleslidingwindows. |     |     | ACMTrans.Database |     |     |      |           |     |           |           |       |      |
| ------------------------- | --- | --- | ----------------- | --- | --- | ---- | --------- | --- | --------- | --------- | ----- | ---- |
|                           |     |     |                   |     |     | Meta | knowledge | for | retrieval | augmented | large | lan- |
Syst.,31(4):1305–1334.
CoRR.
guagemodels.
MandarJoshi,EunsolChoi,DanielS.Weld,andLuke
ZachNussbaum,JohnX.Morris,BrandonDuderstadt,
| Zettlemoyer.2017. |     | TriviaQA:Alargescaledistantly |     |     |     |                       |     |     |             |     |           |     |
| ----------------- | --- | ----------------------------- | --- | --- | --- | --------------------- | --- | --- | ----------- | --- | --------- | --- |
|                   |     |                               |     |     |     | andAndriyMulyar.2024. |     |     | Nomicembed: |     | Traininga |     |
supervisedchallengedatasetforreadingcomprehen-
|     |     |     |     |     |     | reproduciblelongcontexttextembedder. |     |     |     |     | CoRR. |     |
| --- | --- | --- | --- | --- | --- | ------------------------------------ | --- | --- | --- | --- | ----- | --- |
sion. InACL,pages1601–1611,Vancouver,Canada.
ACL.
|     |     |     |     |     |     | AnupamPurwarandRahulSundar.2023. |     |                              |     |     | Keywordaug- |     |
| --- | --- | --- | --- | --- | --- | -------------------------------- | --- | ---------------------------- | --- | --- | ----------- | --- |
|     |     |     |     |     |     | mentedretrieval:                 |     | Novelframeworkforinformation |     |     |             |     |
JeanKaddour,JoshuaHarris,MaximilianMozes,Her-
|     |     |     |     |     |     | retrievalintegratedwithspeechinterface. |     |     |     |     | InAIML- |     |
| --- | --- | --- | --- | --- | --- | --------------------------------------- | --- | --- | --- | --- | ------- | --- |
bieBradley,RobertaRaileanu,andRobertMcHardy.
Systems,pages58:1–58:5,Bangalore,India.ACM.
2023. Challengesandapplicationsoflargelanguage
models. CoRR.
XubinRen,JiabinTang,DaweiYin,NiteshV.Chawla,
|     |     |     |     |     |     | and Chao | Huang. | 2024. | A   | survey | of large | lan- |
| --- | --- | --- | --- | --- | --- | -------- | ------ | ----- | --- | ------ | -------- | ---- |
Tzu-LinKuo,Tzu-WeiChiu,Tzung-ShengLin,Sheng- guagemodelsforgraphs. InKDD,pages6616–6626,
| Yang Wu, | Chao-Wei | Huang, | and | Yun-Nung | Chen. |     |     |     |     |     |     |     |
| -------- | -------- | ------ | --- | -------- | ----- | --- | --- | --- | --- | --- | --- | --- |
Barcelona,Spain.ACM.
2024. Asurveyofgenerativeinformationretrieval.
CoRR.
PriyankaSen,SandeepMavadia,andAmirSaffari.2023.
Knowledgegraph-augmentedlanguagemodelsfor
Patrick S. H. Lewis, Ethan Perez, Aleksandra Pik- complexquestionanswering. InNLRSE,pages1–8,
tus, Fabio Petroni, Vladimir Karpukhin, Naman Toronto,Canada.ACL.
Goyal,HeinrichKüttler,MikeLewis,Wen-tauYih,
| Tim Rocktäschel, |                     | Sebastian | Riedel, |            | and Douwe |                                   |     |     |     |     |          |     |
| ---------------- | ------------------- | --------- | ------- | ---------- | --------- | --------------------------------- | --- | --- | --- | --- | -------- | --- |
|                  |                     |           |         |            |           | AlonTalmorandJonathanBerant.2018. |     |     |     |     | Thewebas |     |
| Kiela. 2020.     | Retrieval-augmented |           |         | generation | for       |                                   |     |     |     |     |          |     |
aknowledge-baseforansweringcomplexquestions.
NeurIPS,
knowledge-intensive NLP tasks. In Vir- InNAACL,pages641–651,NewOrleans,Louisiana,
| tual.CurranAssociates. |     |     |     |     |     | USA.ACL. |     |     |     |     |     |     |
| ---------------------- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- |
JiaweiLi,YizheYang,YuBai,XiaofengZhou,Yinghao XiaobinTian,ZequnSun,andWeiHu.2024. Generat-
Li,HuashanSun,YuhangLiu,XingpengSi,Yuhao
ingexplanationstounderstandandrepairembedding-
| Ye, Yixiao | Wu, Yiguan | Lin, | Bin | Xu, | Ren Bowen, |                       |     |     |                        |     |     |     |
| ---------- | ---------- | ---- | --- | --- | ---------- | --------------------- | --- | --- | ---------------------- | --- | --- | --- |
|            |            |      |     |     |            | basedentityalignment. |     |     | InICDE,pages2205–2217, |     |     |     |
Chong Feng, Yang Gao, and Heyan Huang. 2024. Utrecht,Netherlands.IEEE.
Fundamentalcapabilitiesoflargelanguagemodels
andtheirapplicationsindomainscenarios: asurvey. HugoTouvron,ThibautLavril,GautierIzacard,Xavier
In ACL, pages 11116–11141, Bangkok, Thailand. Martinet,Marie-AnneLachaux,TimothéeLacroix,
ACL.
BaptisteRozière,NamanGoyal,EricHambro,Faisal
Azhar,AurélienRodriguez,ArmandJoulin,Edouard
XianmingLiandJingLi.2024. AoE:Angle-optimized Grave,andGuillaumeLample.2023. Llama: Open
embeddingsforsemantictextualsimilarity. InACL, andefficientfoundationlanguagemodels. CoRR.
pages1825–1839,Bangkok,Thailand.ACL.
HarshTrivedi,NiranjanBalasubramanian,TusharKhot,
Yinheng Li. 2023. A practical survey on zero-shot and Ashish Sabharwal. 2022. MuSiQue: Multi-
prompt design for in-context learning. In RANLP, hopquestionsviasingle-hopquestioncomposition.
pages641–647,Varna,Bulgaria.INCOMA. Trans.Assoc.Comput.Linguistics,10:539–554.

YuWang,NedimLipka,RyanA.Rossi,AlexaF.Siu,
Ruiyi Zhang, and Tyler Derr. 2024a. Knowledge
graph prompting for multi-document question an-
swering. InAAAI,pages19206–19214,Vancouver,
Canada.AAAI.
Yujing Wang, Hainan Zhang, Liang Pang, Binghui
Guo,HongweiZheng,andZhimingZheng.2024b.
MaFeRw: Query rewriting with multi-aspect feed-
backsforretrieval-augmentedlargelanguagemodels.
CoRR.
Qingyun Wu, Gagan Bansal, Jieyu Zhang, Yiran Wu,
Shaokun Zhang, Erkang Zhu, Beibin Li, Li Jiang,
Xiaoyun Zhang, and Chi Wang. 2023. AutoGen:
Enablingnext-genLLMapplicationsviamulti-agent
conversationframework. CoRR.
Shitao Xiao, Zheng Liu, Peitian Zhang, and Niklas
Muennighoff. 2023. C-Pack: Packaged resources
toadvancegeneralChineseembedding. CoRR.
Zhentao Xu, Mark Jerome Cruz, Matthew Guevara,
TieWang,ManasiDeshpande,XiaofengWang,and
Zheng Li. 2024a. Retrieval-augmented generation
withknowledgegraphsforcustomerservicequestion
answering. InSIGIR,pages2905–2909,Washington
DC,USA.ACM.
Ziwei Xu, Sanjay Jain, and Mohan S. Kankanhalli.
2024b. Hallucinationisinevitable: Aninnatelimita-
tionoflargelanguagemodels. CoRR.
Zhilin Yang, Peng Qi, Saizheng Zhang, Yoshua Ben-
gio,WilliamW.Cohen,RuslanSalakhutdinov,and
ChristopherD.Manning.2018. HotpotQA:Adataset
fordiverse,explainablemulti-hopquestionanswer-
ing. In EMNLP, pages 2369–2380, Brussels, Bel-
gium.ACL.
Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak
Shafran,KarthikR.Narasimhan,andYuanCao.2023.
ReAct:Synergizingreasoningandactinginlanguage
models. InICLR,Kigali,Rwanda.OpenReview.net.
Wen-tauYih,MatthewRichardson,ChristopherMeek,
Ming-WeiChang,andJinaSuh.2016. Thevalueof
semanticparselabelingforknowledgebasequestion
answering. InACL,Berlin,Germany.ACL.
Wenhao Yu. 2022. Retrieval-augmented generation
acrossheterogeneousknowledge. InNAACL,pages
52–58,Seattle,WA,USA.ACL.
WenzhengZhao,YuanningCui,andWeiHu.2023. Im-
provingcontinualrelationextractionbydistinguish-
inganalogoussemantics. InACL,pages1162–1175,
Toronto,Canada.ACL.
Angelo Ziletti and Leonardo D’Ambrosi. 2024. Re-
trieval augmented text-to-SQL generation for epi-
demiological question answering using electronic
health records. In NAACL, pages 47–53, Mexico
City,Mexico.ACL.

A AdditionalExperimentalResults
|                           |     |     |     |     |     |     |          | #Inputtokens | #Outputtokens | #LLMcalls | Extractiontime |
| ------------------------- | --- | --- | --- | --- | --- | --- | -------- | ------------ | ------------- | --------- | -------------- |
|                           |     |     |     |     |     |     | LightRAG | 1,269        | 381           | 1         | 3s             |
| A.1 ResultsonMoreDatasets |     |     |     |     |     |     | GraphRAG | 2,791        | 629           | 5         | 6s             |
|                           |     |     |     |     |     |     | KG2RAG   | 561          | 22            | 1         | 1s             |
Weconductadditionalexperimentsontwodifferent
Table9: ComparisonofaverageLLMandtimecostper
datasetstoconfirmtheeffectivenessandgenerality
chunkduringKGconstruction.
ofKG2RAGinvariousscenarios.
AsshowninTable7,KG2RAGmaintainssuperi-
andGraphRAG,andisveryclosetoSemanticRAG.
orityonthewidely-usedMuSiQuedataset(Trivedi
etal.,2022)inresponseF1score,responseexact Note that KG2RAG might need a lower time for
match(EM)rate,andretrievalF1score. responsegenerationusingacondensedandinfor-
mativecontextasinput.
| Methods |     | ResponseF1 |     | ResponseEM | RetrievalF1 |     |     |     |     |     |     |
| ------- | --- | ---------- | --- | ---------- | ----------- | --- | --- | --- | --- | --- | --- |
LLM-only 0.075 0.025 - Method Avg.retrievaltime Avg.generationtime
| SemanticRAG |     | 0.367 |     | 0.248 |     | 0.365 |             |     |      |         |     |
| ----------- | --- | ----- | --- | ----- | --- | ----- | ----------- | --- | ---- | ------- | --- |
|             |     |       |     |       |     |       | SemanticRAG |     | 21ms | 2,500ms |     |
| +Rerank     |     | 0.380 |     | 0.249 |     | 0.372 |             |     |      |         |     |
|             |     |       |     |       |     |       | LightRAG    |     | 40ms | 5,600ms |     |
| HybridRAG   |     | 0.380 |     | 0.250 |     | 0.364 |             |     |      |         |     |
|             |     |       |     |       |     |       | GraphRAG    |     | 42ms | 5,500ms |     |
| LightRAG    |     | 0.248 |     | 0.170 |     | 0.289 |             |     |      |         |     |
|             |     |       |     |       |     |       | KG2RAG      |     | 25ms | 2,300ms |     |
| GraphRAG    |     | 0.231 |     | 0.156 |     | 0.273 |             |     |      |         |     |
KG2RAG
|     |     | 0.419 |     | 0.303 |     | 0.451 |     |     |     |     |     |
| --- | --- | ----- | --- | ----- | --- | ----- | --- | --- | --- | --- | --- |
Table10: Comparisonofaverageretrievalandgenera-
tiontimeperquery.
| Table7: |     | ComparisonresultsonMuSiQue. |             |     |        |         |     |     |     |     |     |
| ------- | --- | --------------------------- | ----------- | --- | ------ | ------- | --- | --- | --- | --- | --- |
| Also,   | we  | conduct                     | experiments |     | on the | typical |     |     |     |     |     |
long-contextdatasetTriviaQA(Joshietal.,2017).
| On average,                        |        | each | document | in          | this dataset | con- |     |     |     |     |     |
| ---------------------------------- | ------ | ---- | -------- | ----------- | ------------ | ---- | --- | --- | --- | --- | --- |
| tains 2,895                        | words. |      | For      | comparison, | documents    |      |     |     |     |     |     |
| inHotpotQAhaveanaverageof917words. |        |      |          |             |              | The  |     |     |     |     |     |
experimentalresultsareshowninTable8,which
confirmstheeffectivenessofKG2RAGinatypical
long-contextsetting.
| Methods     |     | ResponseF1                   | ResponsePrec. |       | ResponseRecall |       |     |     |     |     |     |
| ----------- | --- | ---------------------------- | ------------- | ----- | -------------- | ----- | --- | --- | --- | --- | --- |
| LLM-only    |     | 0.182                        |               | 0.303 |                | 0.144 |     |     |     |     |     |
| SemanticRAG |     | 0.259                        |               | 0.413 |                | 0.211 |     |     |     |     |     |
| +Rerank     |     | 0.265                        |               | 0.409 |                | 0.235 |     |     |     |     |     |
| HybridRAG   |     | 0.262                        |               | 0.415 |                | 0.229 |     |     |     |     |     |
| LightRAG    |     | 0.118                        |               | 0.157 |                | 0.237 |     |     |     |     |     |
| GraphRAG    |     | 0.127                        |               | 0.193 |                | 0.225 |     |     |     |     |     |
| KG2RAG      |     | 0.273                        |               | 0.416 |                | 0.240 |     |     |     |     |     |
| Table8:     |     | ComparisonresultsonTriviaQA. |               |       |                |       |     |     |     |     |     |
A.2 EfficiencyAnalysis
WecomparetheKGconstructioncostofKG2RAG
| with two | other | KG-enhanced |     |     | RAG approaches: |     |     |     |     |     |     |
| -------- | ----- | ----------- | --- | --- | --------------- | --- | --- | --- | --- | --- | --- |
LightRAG(Guoetal.,2024)andGraphRAG(Edge
| et al., 2024). |     | The | results, | as summarized |     | in Ta- |     |     |     |     |     |
| -------------- | --- | --- | -------- | ------------- | --- | ------ | --- | --- | --- | --- | --- |
ble9,demonstratethatKG2RAGismoreefficient
| in terms | of token | cost, | the | number | of LLM | calls, |     |     |     |     |     |
| -------- | -------- | ----- | --- | ------ | ------ | ------ | --- | --- | --- | --- | --- |
andtimecost.
| We  | calculate | the | average | retrieval |     | time and |     |     |     |     |     |
| --- | --------- | --- | ------- | --------- | --- | -------- | --- | --- | --- | --- | --- |
KG2RAG
| generation | time | of  |     | compared |     | to Ligh- |     |     |     |     |     |
| ---------- | ---- | --- | --- | -------- | --- | -------- | --- | --- | --- | --- | --- |
tRAGandGraphRAG.TheresultsinTable10in-
| dicate that | KG2RAG |     | requires |     | less time | for both |     |     |     |     |     |
| ----------- | ------ | --- | -------- | --- | --------- | -------- | --- | --- | --- | --- | --- |
retrievalandresponsegenerationthanLightRAG
