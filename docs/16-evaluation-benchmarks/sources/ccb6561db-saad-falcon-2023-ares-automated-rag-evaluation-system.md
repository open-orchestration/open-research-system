ARES: An Automated Evaluation Framework for Retrieval-Augmented
|     |                            |     |     | Generation |     | Systems                               |                    |     |     |     |     |
| --- | -------------------------- | --- | --- | ---------- | --- | ------------------------------------- | ------------------ | --- | --- | --- | --- |
|     | JonSaad-Falcon             |     |     |            |     |                                       | OmarKhattab        |     |     |     |     |
|     | StanfordUniversity∗        |     |     |            |     |                                       | StanfordUniversity |     |     |     |     |
|     | jonsaadfalcon@stanford.edu |     |     |            |     | okhattab@stanford.edu                 |                    |     |     |     |     |
|     | ChristopherPotts           |     |     |            |     |                                       | MateiZaharia       |     |     |     |     |
|     | StanfordUniversity         |     |     |            |     | DatabricksandUCBerkeley               |                    |     |     |     |     |
|     | cgpotts@stanford.edu       |     |     |            |     | matei@databricks.com                  |                    |     |     |     |     |
|     | Abstract                   |     |     |            |     | ThebestdesignforaRAGsystemisnotneces- |                    |     |     |     |     |
sarilyuniversalacrossdatadomains,corpussizes,
| Evaluating | retrieval-augmented   |     |        | generation |      |                         |     |     |                   |     |     |
| ---------- | --------------------- | --- | ------ | ---------- | ---- | ----------------------- | --- | --- | ----------------- | --- | --- |
|            |                       |     |        |            |      | andcost/latencybudgets. |     |     | TotunetheirownRAG |     |     |
| (RAG)      | systems traditionally |     | relies | on         | hand |                         |     |     |                   |     |     |
4202 raM 13  ]LC.sc[  2v67490.1132:viXra
annotations for input queries, passages to re- systems, practitioners traditionally need hand an-
|             |           |     |           |     |        | notations | for test | questions, |     | passages | to retrieve |
| ----------- | --------- | --- | --------- | --- | ------ | --------- | -------- | ---------- | --- | -------- | ----------- |
| trieve, and | responses | to  | generate. | We  | intro- |           |          |            |     |          |             |
duce ARES, an Automated RAG Evaluation (toassesstheretriever),andresponsestogenerate,
| System, | for evaluating |     | RAG systems |     | along |                                          |     |     |     |     |        |
| ------- | -------------- | --- | ----------- | --- | ----- | ---------------------------------------- | --- | --- | --- | --- | ------ |
|         |                |     |             |     |       | labeledspecificallyfortheirtargetdomain. |     |     |     |     | Alter- |
the dimensions of context relevance, answer natively,theymayevaluatedifferentapproachesin
| faithfulness, | and           | answer | relevance. | By    | cre- |            |               |     |          |                |      |
| ------------- | ------------- | ------ | ---------- | ----- | ---- | ---------- | ------------- | --- | -------- | -------------- | ---- |
|               |               |        |            |       |      | production | by collecting |     | human    | preferences    | that |
| ating its     | own synthetic |        | training   | data, | ARES |            |               |     |          |                |      |
|               |               |        |            |       |      | compare    | the candidate |     | systems. | Unfortunately, |      |
finetuneslightweightLMjudgestoassessthe
quality of individual RAG components. To bothofthesestrategiesdemandhighexpertiseand
imposeconsiderableannotationcosts.
mitigatepotentialpredictionerrors,ARESuti-
lizesasmallsetofhuman-annotateddatapoints Model-basedevaluationisaninexpensivestrat-
forprediction-poweredinference(PPI).Across
egytotestgenerativeoutputquality(Zhengetal.,
eight different knowledge-intensive tasks in 2023). For instance, the open-source RAGAS
KILT,SuperGLUE,andAIS,ARESaccurately
|     |     |     |     |     |     | framework | (JamesandEs,2023)promptsanLM |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --------- | ---------------------------- | --- | --- | --- | --- |
evaluatesRAGsystemswhileusingonlyafew
forevaluatingtherelevanceofretrievedinforma-
hundredhumanannotationsduringevaluation.
tionandthefaithfulnessandaccuracyofgenerated
| Furthermore,  | ARES    | judges  | remain | effective |      |            |                                       |     |     |     |     |
| ------------- | ------- | ------- | ------ | --------- | ---- | ---------- | ------------------------------------- | --- | --- | --- | --- |
|               |         |         |        |           |      | responses. | Unfortunately,suchstrategiescurrently |     |     |     |     |
| across domain | shifts, | proving |        | accurate  | even |            |                                       |     |     |     |     |
afterchangingthetypeofqueriesand/ordocu- rely for evaluation on a fixed set of heuristically
mentsusedintheevaluatedRAGsystems. We hand-written prompts, offering little adaptability
makeourcodeanddatasetspubliclyavailable to various evaluation contexts and no guarantees
onGithub.
aboutquality.
| 1 Introduction |     |     |     |     |     | To evaluate |            | RAG   | systems | rapidly       | and accu- |
| -------------- | --- | --- | --- | --- | --- | ----------- | ---------- | ----- | ------- | ------------- | --------- |
|                |     |     |     |     |     | rately,     | we propose | ARES, |         | the Automated | RAG       |
Retrieval-augmented generation (RAG) has be- Evaluation System. ARES is the first automated
| come a prominent |     | approach | for | building | user- |     |     |     |     |     |     |
| ---------------- | --- | -------- | --- | -------- | ----- | --- | --- | --- | --- | --- | --- |
RAGevaluationsystemtogeneratetailoredLLM
facingNLPapplications,suchassystemsforques-
judgesforeachcomponentofaRAGpipeline,lead-
tionanswering(QA),fact-checking,andcustomer ingtosubstantialboostsinevaluationprecisionand
| support (Petroni | et al., | 2021; | Wang | et  | al., 2019). |     |     |     |     |     |     |
| ---------------- | ------- | ----- | ---- | --- | ----------- | --- | --- | --- | --- | --- | --- |
accuracycomparedtoexistingapproacheslikeRA-
Typically,aRAGsystemconsistsofaretrieverand
GAS.Furthermore,unlikeexistingRAGevaluation
adownstreamlanguagemodel(LM).Givenauser systems,ARESprovidesconfidenceintervalsfor
question,theretrieverfindsrelevantpassagesfrom its scoring by leveraging prediction-powered in-
acorpusandtheLMusesthesepassagestogener-
|               |                                 |     |     |     |     | ference(PPI;Angelopoulosetal.2023). |              |     |       |             | Givena |
| ------------- | ------------------------------- | --- | --- | --- | --- | ----------------------------------- | ------------ | --- | ----- | ----------- | ------ |
| atearesponse. | Thisformulationadmitsamultitude |     |     |     |     |                                     |              |     |       |             |        |
|               |                                 |     |     |     |     | corpus                              | of documents |     | and a | RAG system, | ARES   |
ofchoices: whatretrievalmodeltouse,howtodi- reportsthreeevaluationscores: contextrelevance
videthedocumentsintoretrievalchunks,andhow
|     |     |     |     |     |     | (is the retrieved |     | information |     | pertinent | to the test |
| --- | --- | --- | --- | --- | --- | ----------------- | --- | ----------- | --- | --------- | ----------- |
topromptorfinetunetheLMtousetheretrieved
question),answerfaithfulness(istheresponsegen-
information, to name only a few of the simplest erated by the language model properly grounded
designdecisions.
intheretrievedcontext),andanswerrelevance(is
∗ProjectstartedduringresearchinternshipatDatabricks theresponsealsorelevanttothequestion). Agood

RAGsystemfindsrelevantcontextsandgenerates ment and comparison of competitive approaches
| answersthatarebothfaithfulandrelevant. |     |     |     |     |     | andconfigurations. |     |     |     |     |     |
| -------------------------------------- | --- | --- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- |
ManyexistingRAGevaluationframeworksre- WemaketheAREScodeanddatasetspublicly
| quire substantial                        |     | human    | annotations | for        | scoring. | availableonGithub. |     |     |     |     |     |
| ---------------------------------------- | --- | -------- | ----------- | ---------- | -------- | ------------------ | --- | --- | --- | --- | --- |
| ARES significantly                       |     | improves | data        | efficiency | dur-     |                    |     |     |     |     |     |
| ingevaluationbyonlyrequiringthreeinputs: |     |          |             |            | anin-    | 2 RelatedWork      |     |     |     |     |     |
domainpassageset,ahumanpreferencevalidation
|     |     |     |     |     |     | RAG (Guu | et al., | 2020; | Lewis et | al., 2020; | Khat- |
| --- | --- | --- | --- | --- | --- | -------- | ------- | ----- | -------- | ---------- | ----- |
setofapproximately150annotateddatapointsor
more,andfew-shotexamplesofin-domainqueries tab et al., 2021; Izacard et al., 2022)) is now a
commonstrategyforbolsteringLLMsbycombin-
| and answers | (e.g. | five examples |     | or more), | which |                              |     |     |                   |     |     |
| ----------- | ----- | ------------- | --- | --------- | ----- | ---------------------------- | --- | --- | ----------------- | --- | --- |
|             |       |               |     |           |       | ingthemwithretrievalsystems. |     |     | Throughretrieval, |     |     |
areusedforpromptingLLMsinsyntheticdatagen-
| eration. |     |     |     |     |     | RAG helps | LM  | systems | gather | domain-specific |     |
| -------- | --- | --- | --- | --- | --- | --------- | --- | ------- | ------ | --------------- | --- |
Giventhecorpusofin-domainpassages,ARES knowledge,groundgenerationsinfactualinforma-
|                        |     |     |                       |     |     | tion (Shuster | et        | al., 2021;   | Huo et | al., 2023),      | and |
| ---------------------- | --- | --- | --------------------- | --- | --- | ------------- | --------- | ------------ | ------ | ---------------- | --- |
| proceedsinthreestages. |     |     | First,itleveragesanLM |     |     |               |           |              |        |                  |     |
|                        |     |     |                       |     |     | offer a       | degree of | transparency | or     | interpretability |     |
toconstructasyntheticdatasetofquestion–answer
pairs,derivedfromthepassagesinthecorpus. Sec- viacitingsources(Mialonetal.,2023).
ond,itdefinesthreeseparatejudgemodelstoper- MultipleLLM-basedevaluationtechniqueshave
|     |     |     |     |     |     | emergedforgaugingLLMsystems. |     |     |     | Thisisessen- |     |
| --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- | ------------ | --- |
formthreeclassificationtasks(contextrelevance,
answerfaithfulness,andanswerrelevance). These tialforrapiddeploymentinnewsettings,whereit
judgesarelightweightmodelsfine-tunedagainsta isdifficulttobuildatraditionalbenchmarkdataset
|                               |     |         |                  |          |       | from scratch. | Early    | attempts | at       | this | use LLMs |
| ----------------------------- | --- | ------- | ---------------- | -------- | ----- | ------------- | -------- | -------- | -------- | ---- | -------- |
| contrastivelearningobjective. |     |         | Third,ARESscores |          |       |               |          |          |          |      |          |
|                               |     |         |                  |          |       | out of        | the box, | as in    | MT-Bench | and  | Chatbot  |
| the different                 | RAG | systems | being            | assessed | using |               |          |          |          |      |          |
prediction-poweredinference(PPI;Angelopoulos Arena (Zheng et al., 2023). AutoCalibrate (Liu
etal.2023)toimprovemodel-basedevaluationac- et al., 2023b) seeks to align an LLM-judge with
|     |     |     |     |     |     | human | preferences, | leveraging |     | a self-refinement |     |
| --- | --- | --- | --- | --- | --- | ----- | ------------ | ---------- | --- | ----------------- | --- |
curacyandprovidestatisticalconfidenceintervals
forRAGscoring. PPIutilizesasmallsetofhuman prompttoiterativelyimprovetheLLMjudge. How-
annotateddatapointsforcomputingitsconfidence ever, AutoCalibrate does not offer any statistical
|     |     |     |     |     |     | guaranteesfortheaccuracyofitspredictions. |     |     |     |     | Other |
| --- | --- | --- | --- | --- | --- | ----------------------------------------- | --- | --- | --- | --- | ----- |
intervals;wedesignatethisannotatedsetasourhu-
manpreferencevalidationset,whichiscomposed workhasusedLLMpromptingtoevaluatesystem
ofapproximately150annotateddatapointsormore quality across natural language generation tasks,
thatdesignatebothpositiveandnegativeexamples such as translation, summarization, and dialogue
(KocmiandFedermann,2023;Fuetal.,2023;Liu
forcontextrelevance,answerfaithfulness,andan-
| swerrelevance. |     |     |     |     |     | etal.,2023a;Wangetal.,2023). |     |     |     |     |     |
| -------------- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- |
We conduct extensive empirical evaluations, Inthecontextofknowledge-intensiveNLPtasks,
demonstrating that ARES accurately scores LLMshavebeenexploredforassessingattribution
RAGsystemsacrossthesixknowledge-intensive andfactualityinLLMs(Minetal.,2023;Gekhman
datasets in KILT and SuperGLUE, beating exist- et al., 2023; Yue et al., 2023). New guidelines
ingautomatedevaluationapproacheslikeRAGAS likeLongEval(Krishnaetal.,2023)anddatasets
|         |          |            |     |           |         | like Hagrid | and | ALCE | (Kamalloo | et  | al., 2023; |
| ------- | -------- | ---------- | --- | --------- | ------- | ----------- | --- | ---- | --------- | --- | ---------- |
| by 59.3 | and 14.4 | percentage |     | points on | average |             |     |      |           |     |            |
acrosscontextrelevanceandanswerrelevanceeval- Gaoetal.,2023)provideresourcesforanalyzing
uationaccuracy,respectively. Additionally,ARES knowledge-intensiveLLMpipelines.
accurately calculates answer hallucination occur- Thetwomost-closelyrelatedprojectstoARES
rencesintheAISattributiondataset(Rashkinetal., are EXAM (Sander and Dietz, 2021) and RA-
2022),predictingwithin2.5percentagepointsof GAS(JamesandEs,2023). ToevaluateRAGsys-
thegroundtruthaverageforanswerhallucinations. tems,theEXAMmetricestimateshowmanyexam
Comparedtoannotation-basedevaluationmethods, questionsareader(simulatedasaQAsystem)can
ARESissubstantiallymoreaccurateandefficient, answercorrectlybasedonthegeneratedresponse.
requiring 78% less annotations than the baseline This requires a set of queries with several asso-
approach. We also find that ARES consistently ciated sub-questions each, which adds a burden
distinguishes competitive RAG systems that are thatARESdoesnotbring. RAGASisbasedona
only a few points apart in ground-truth metrics. handfulofheuristichand-writtenprompts. These
ThisprecisionenablesAREStoguidethedevelop- offerlittleadaptabilitytonewRAGevaluationset-

tings (e.g., new corpora) and, as we show in our evance negatives, we randomly sample in-
evaluation,substantiallyunderperformARES. domain passages unrelated to a given syn-
|     |     |     |     |     |     |     | thetic | query. | For | answer | faithfulness | and |
| --- | --- | --- | --- | --- | --- | --- | ------ | ------ | --- | ------ | ------------ | --- |
3 ARES
|     |     |     |     |     |     |     | answer | relevance |     | negatives, | we  | randomly |
| --- | --- | --- | --- | --- | --- | --- | ------ | --------- | --- | ---------- | --- | -------- |
samplesynthetically-generatedanswersfrom
| ARESproceedsinthreestages(Figure1). |     |     |                        |     |     | There |       |           |       |     |              |       |
| ----------------------------------- | --- | --- | ---------------------- | --- | --- | ----- | ----- | --------- | ----- | --- | ------------ | ----- |
|                                     |     |     |                        |     |     |       | other | passages, | which |     | were created | using |
| arethreerequiredinputs:             |     |     | anin-domainpassageset, |     |     |       |       |           |       |     |              |       |
FLAN-T5XXL.
ahumanpreferencevalidationsetofapproximately
150annotateddatapoints(ormore),andfew-shot Strong Negative Generation:
|     |     |     |     |     |     |     | 2.  |     |     |     | For | context |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------- |
examplesofin-domainqueriesandanswers(five relevancenegatives,werandomlysamplein-
ormoreexamples),whichareusedforprompting domainpassagesfromthesamedocumentas
LLMsinsyntheticdatageneration. Withourinputs thegoldpassage. Fordatasetsinwhichmul-
prepared,webeginbygeneratingsyntheticqueries tiplepassagesarenotavailableforthesame
(andtheiranswers)fromthepassagesinthetarget document, we use BM25 to retrieve the top-
corpus. Wethenusethesequery–passage–answer 10passagessimilartothepassageandsample
triplestotrainLLMjudges. Subsequently,weap- from them for our context relevance strong
ply these judges to any RAG system, scoring a negatives. For answer faithfulness and an-
sample of its in-domain query-document-answer swerrelevancenegatives,wepromptFLAN-
triples,anduseprediction-poweredinference(PPI) T5XXL(subsection4.1)togenerateacontra-
with our human preference validation set to esti- dictoryanswerusingthefew-shotpromptin
| mateaconfidenceintervalforthequalityofeach |     |     |     |     |     |     | subsectionA.5. |     |     |     |     |     |
| ------------------------------------------ | --- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- |
RAGsystem.
|     |     |     |     |     |     |     | In total, | the | number | of  | negatives generated |     |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | ------ | --- | ------------------- | --- |
3.1 LLMGenerationofSyntheticDataset equalsthenumberofpositivesgeneratedforevalu-
atingcontextrelevanceandanswerrelevance.
| We generate                           | synthetic |     | queries | and | answers | from |                        |     |     |     |     |     |
| ------------------------------------- | --------- | --- | ------- | --- | ------- | ---- | ---------------------- | --- | --- | --- | --- | --- |
| thecorpuspassagesusinggenerativeLLMs. |           |     |         |     |         | The  |                        |     |     |     |     |     |
|                                       |           |     |         |     |         |      | 3.2 PreparingLLMJudges |     |     |     |     |     |
generateddatarepresentbothpositiveandnegative
|                     |                         |          |     |                       |         |        | To prepare    | our     | RAG | evaluation   | judges,     | we use |
| ------------------- | ----------------------- | -------- | --- | --------------------- | ------- | ------ | ------------- | ------- | --- | ------------ | ----------- | ------ |
| examples            | of query–passage–answer |          |     |                       | triples | (e.g., |               |         |     |              |             |        |
|                     |                         |          |     |                       |         |        | our synthetic | dataset |     | to fine-tune | DeBERTa-v3- |        |
| relevant/irrelevant |                         | passages |     | and correct/incorrect |         |        |               |         |     |              |             |        |
Largejudges(discussedinsubsection4.1)toeval-
| answers). | For | generation, |     | the LLM | uses | our in- |     |     |     |     |     |     |
| --------- | --- | ----------- | --- | ------- | ---- | ------- | --- | --- | --- | --- | --- | --- |
uatethreedifferentcapabilities(Chenetal.,2023;
putsetoffew-shotexampleswithin-domainpas-
JamesandEs,2023):
| sages mapped |     | to in-domain |     | queries | and | answers; |     |     |     |     |     |     |
| ------------ | --- | ------------ | --- | ------- | --- | -------- | --- | --- | --- | --- | --- | --- |
themodelthengeneratesasyntheticquestionand
|     |     |     |     |     |     |     | 1. ContextRelevance: |     |     | Isthepassagereturned |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | -------------------- | --- | --- |
answerfromagivenin-domainpassage,allowing
relevantforansweringthegivenquery?
ustocreatebothpositiveandnegativetrainingex-
amples. Weincludeexamplepromptsforgenerat- 2. Answer Faithfulness: Is the answer gener-
atedfaithfultotheretrievedpassage,ordoes
ingsyntheticqueriesandanswersinA.6.
|     |     |     |     |     |     |     | it  | contain hallucinated |     | or  | extrapolated | state- |
| --- | --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | ------------ | ------ |
Forcreatingoursyntheticdata,weprimarilyuse
mentsbeyondthepassage?
| on FLAN-T5 | XXL | (discussed |     | in  | subsection | 4.1). |     |     |     |     |     |     |
| ---------- | --- | ---------- | --- | --- | ---------- | ----- | --- | --- | --- | --- | --- | --- |
ARESworkswellwiththismodel(seesection5) 3. AnswerRelevance: Istheanswergenerated
but our system can ultimately use another high- relevant given the query and retrieved pas-
| qualitymodelforgeneratingsyntheticqueriesand |     |             |     |             |     |         | sage? |     |     |     |     |     |
| -------------------------------------------- | --- | ----------- | --- | ----------- | --- | ------- | ----- | --- | --- | --- | --- | --- |
| answers.                                     | We  | then filter | out | low-quality |     | queries |       |     |     |     |     |     |
Foreachmetric,aseparateLLMwithabinary
bytestingifagivenquerycanretrieveitsoriginal
classifierheadisfine-tunedtoclassifypositiveand
| passage | as the | top result | using | its | retriever. | This |                   |     |                           |     |     |     |
| ------- | ------ | ---------- | ----- | --- | ---------- | ---- | ----------------- | --- | ------------------------- | --- | --- | --- |
|         |        |            |       |     |            |      | negativeexamples. |     | Foreachconcatenatedquery- |     |     |     |
filteringapproachhasbeenusedinpreviouswork
toisolatehigh-qualitysyntheticqueries(Daietal., document-answer,asingleLLMjudgemustclas-
sifythetripleaspositiveornegativeforthatjudge’s
2022;Saad-Falconetal.,2023).
|     |     |     |     |     |     |     | metric. | To fine-tune | these | judges, | we use | our hu- |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------------ | ----- | ------- | ------ | ------- |
Togeneratenegativesforfine-tuningourLLM
judges,werelyontwonovelstrategies,generating man preference validation set to evaluate model
improvementaftereachepoch,stoppingwhenwe
thesamenumberofnegativeswitheachstrategy:
havethreeepochswithnoimprovementinloss(see
1. WeakNegativeGeneration: Forcontextrel- subsectionA.1formoreinformation).

Figure1: OverviewofARES:Asinputs,theARESpipelinerequiresanin-domainpassageset,ahumanpreference
validationsetof150annotateddatapointsormore,andfew-shotexamplesofin-domainqueriesandanswers(fiveor
more),whichareusedforpromptingLLMsinsyntheticdatageneration. ToprepareourLLMjudgesforevaluation,
wefirstgeneratesyntheticqueriesandanswersfromthecorpuspassages. Usingourgeneratedtrainingtriplesanda
constrastivelearningframework,wefine-tuneanLLMtoclassifyquery–passage–answertriplesinthreedifferent
criteria: contextrelevance,answerfaithfulness,andanswerrelevance. Finally,weusetheLLMjudgestoscore
RAGsystemsandgenerateconfidenceboundsfortherankingusingPPIandthehumanpreferencevalidationset.
3.3 RankingRAGSystemswithConfidence apoints and the ARES judge predictions on the
| Intervals |     |     |     | non-annotateddatapointstoconstructconfidence |     |     |     |
| --------- | --- | --- | --- | -------------------------------------------- | --- | --- | --- |
intervalsforourRAGsystem’sperformance.
OncewehavepreparedourLLMjudges,weneed
Todothis,PPIusestheLLMjudgesonthehu-
tousethemtoscoreandrankthecompetingRAG
|          |                                  |     |     | man preference | validation | set to | learn a rectifier |
| -------- | -------------------------------- | --- | --- | -------------- | ---------- | ------ | ----------------- |
| systems. | Todothis,ARESsamplesthein-domain |     |     |                |            |        |                   |
query-document-answertriplesproducedbyeach functionforconstructingaconfidencesetoftheML
model’sperformance,usingeachMLpredictionin
| RAG approach, | and the | judges label | each triple, |                                |     |     |               |
| ------------- | ------- | ------------ | ------------ | ------------------------------ | --- | --- | ------------- |
|               |         |              |              | thelargernon-annotateddataset. |     |     | Theconfidence |
predictingtheircontextrelevance,answerfaithful-
setcanthenbeusedtocreateatighterconfidence
| ness, and | answer relevance. | By averaging | the in- |     |     |     |     |
| --------- | ----------------- | ------------ | ------- | --- | --- | --- | --- |
intervalfortheperformanceoftheevaluatedRAG
dividualpredictedlabelsforeachin-domaintriple,
|     |     |     |     | system(e.g. | itscontextrelevance,answerfaithful- |     |     |
| --- | --- | --- | --- | ----------- | ----------------------------------- | --- | --- |
wecalculatetheRAGsystemperformanceacross
|     |     |     |     | ness, or answer | relevance | accuracy | individually) |
| --- | --- | --- | --- | --------------- | --------- | -------- | ------------- |
eachofthethreemetrics.
comparedtosimplyusingannotatedoutputsfrom
Inprinciple,wecouldsimplyreporttheseaver-
|     |     |     |     | theevaluatedRAGsystem. |     | Bybolsteringthehu- |     |
| --- | --- | --- | --- | ---------------------- | --- | ------------------ | --- |
agescoresasqualitymetricsforeachRAGsystem.
manpreferencevalidationsetwiththemuchlarger
| However, | these scores reflect | entirely | unlabeled |     |     |     |     |
| -------- | -------------------- | -------- | --------- | --- | --- | --- | --- |
setofdatapointswithMLpredictions,PPIcande-
datawithpredictionsfromasynthetically-trained
velopreliableconfidenceintervalsforMLmodel
| LLM judge, | and hence | they may not | be entirely |     |     |     |     |
| ---------- | --------- | ------------ | ----------- | --- | --- | --- | --- |
performancethatbeatpreviousclassicalinference
| accurate. | Asanextremealternative,wecoulduse |     |     |     |     |     |     |
| --------- | --------------------------------- | --- | --- | --- | --- | --- | --- |
approaches.
justthesmallhumanpreferencevalidationsetdis-
ThePPIrectifierfunctionallowsustoestimate
cussedpreviouslyforevaluation,reportingtheex-
tent to which each RAG system agrees with (or the errors of the LLM judge and generate confi-
deviates from) the human annotations. However, denceboundsforthesuccessandfailureratesofthe
anannotation-basedevaluationapproachwouldre- RAGsystem,estimatingcontextrelevance,answer
|                |               |                 |      | faithfulness, | and answer | relevance | performance. |
| -------------- | ------------- | --------------- | ---- | ------------- | ---------- | --------- | ------------ |
| quire labeling | substantially | more generative | out- |               |            |           |              |
putsfromeachRAGsystemsseparately,whichcan Additionally,PPIallowsustoestimateconfidence
becostlybothintermsoftimeandfinancing. intervalswithaselectedlevelofprobability;forour
experiments,weuseastandard95%alpha(proba-
| To combine | the benefits | of both, | and hence |     |     |     |     |
| ---------- | ------------ | -------- | --------- | --- | --- | --- | --- |
bility)forourconfidenceinterval.
| boosttheprecisionoftheevaluation, |     |     | ARESuses |     |     |     |     |
| --------------------------------- | --- | --- | -------- | --- | --- | --- | --- |
prediction-poweredinference(PPI;Angelopoulos Withtheaccuracyconfidenceintervalforeach
et al. 2023) to predict the system scores. PPI is component of the RAG, we find the midpoint of
a recent statistical method that provides tighter eachconfidenceintervalandusethemidpointsto
confidence intervals on a small set of annotated ranktheRAGsystems. Withourranking,wecan
datapoints (i.e., our validation set) by leveraging comparedifferentRAGsystems,aswellasdiffer-
predictionsonamuchlargersetofnon-annotated entconfigurationsofthesameRAGsystem,tofind
datapoints. PPIcanleverageboththelabeleddat- thebest-performingapproachforagivendomain.

4 Experiments Wikipediaarticles,articlesonsociety/law/justice,
articlesonhistory/anthropology,elementaryschool
4.1 Models
science textbooks, 9/11 reports, and fiction).
Forourfine-tunedjudges,ARESreliesongenerat- ReCoRDfocusesondeterminingtheplaceholder
ingcheapbutqualitysyntheticqueriesandanswers entity in a statement, focusing on news articles
usingLLMs. Forgeneratingoursyntheticdatasets, fromCNNandtheDailyMail. ForMultiRCand
weuseFLAN-T5XXL(Chungetal.,2022). Wese- ReCoRD,wecreateopen-domainversionsoftheir
lectedDeBERTa-v3-Large(Heetal.,2021)forour tasks. ForMultiRC,weperformretrievaloverits
fine-tunedLLMjudge. Ourfine-tunedLLMjudges sevensetsofdomainpassages. ForReCoRD,we
allowustorankRAGsystemswithoutrelyingon performretrievaloveritsnewsarticlepassages.
externalAPIs,solelyusingfew-shotpromptsand TheefficacyofARESreliesonitsabilitytorank
deployableLLMsoncommercialGPUs. differentRAGsystemswhileonlyusingahuman
Forourin-contextlearningbaseline,weuseOpe- preferencevalidationsetanddomain-targetedLLM
nAI’s gpt-3.5-turbo-16k, version 10/23, (Brown judges. TotestthelimitsofARES,weneedtosim-
etal.,2020)inazero/few-shotsetting. Forsimilar- ulatetheexistenceofmanyRAGsystemsthatare
itysearchoverin-domainpassages,weuseFAISS separatedbysmallaccuracymarginsonoureval-
IndexFlatL2 for indexing (Johnson et al., 2019) uationmetrics. Forthis, wecreatesystemsusing
andOpenAI’stext-embedding-ada-002forgener- artificial query-passage-answer triples, in which
ating embeddings. We use simlarity search over weempiricallyknowthepositiveandnegativeex-
in-domainpassagestofilteroursyntheticqueries amples of the mock RAG system. We generate
that cannot retrieve the passage from which they these mock splits of the given datasets by select-
weregenerated. Weuseversion0.0.18ofRAGAS ing (1) The positive and negative query-passage
inourexperiments(JamesandEs,2023). matchesforcontextrelevance,and(2)thepositive
andnegativequery-passage-answermatchesforan-
4.2 Datasets
swerrelevance. Weincludepositiveandnegative
Our core experimental goal is to provide a rich examplesfromourevaluationsetsinTable7.
pictureofwhereAREScanbeappliedeffectively. For our positive triples, we can simply use the
Totestacrossmultipletypesofqueries,documents, KILT and SuperGLUE examples without any al-
andanswers,weselectedallthedatasetsfromthe teration. For gathering negative query-passage
widely-used KILT and SuperGLUE benchmarks pairs and query-passage-answer triples, we ran-
forwhichRAGisappropriate. domly sample passages and answers from either:
FromKILT(Petronietal.,2021),weuseNatural the same Wikipedia document or an entirely ran-
Questions(NQ),HotpotQA,FEVER,andWizards dom Wikipedia document. This sampling allows
of Wikipedia (WoW) (Kwiatkowski et al., 2019; ustoartificiallycreatemockRAGsystemsfortest-
Yangetal.,2018;Akhtaretal.,2023;Dinanetal., ingARES.Bysamplingbothrelatedandunrelated
2018). EachdatasetusesWikipediapassagesbut documents/answers, we hope to better gauge the
the queries and answers offer a range of applica- efficacyofARESinjudgingRAGoutputs.
tions. BothNQandHotpotQAfeaturedirectques- WedonotevaluateanswerfaithfulnessforKILT
tionsandexpectshortanswers,butNQusessingle and SuperGLUE datasets since we do not have
passages for reasoning while HotpotQA requires human-annotatedhallucinatedanswerstousefor
multiple passages for reasoning. Furthermore, evaluation. However,wedotesttheARESframe-
FEVERfocusesonfact-verification,determiningif workonrealattributiondatasetsinSection5.2.
apassagesupportsorrefutesagivenstatement,and Using the validation subsets for each KILT
expectsanoutputof“SUPPORTS”or“REFUTES”. andSuperGLUEdataset,wecreateninedifferent
WoWseekstoevaluatedialogueagentsbymapping dataset splits, ranging from 70% success rate to
user dialogue to relevant Wikipedia passages be- 90% success rate for each of the evaluated RAG
fore a chatbot generates a paragraph-length chat criteria;eachdatasetisseparatedby2.5%accuracy
responseincorporatingpassageknowledge. points (e.g. 70.0%, 72.5%, 75.0%, ..., 90.0%).
FromSuperGLUE(Wangetal.,2019),weuse Each split also represents a different mock RAG
MultiRC and ReCoRD (Khashabi et al., 2018; system. Sinceweknowthesuccesspercentagesof
Zhang et al., 2018). MultiRC focuses on di- each dataset split, we know the appropriate rank-
rectquestionsforsevendifferentdomains(News, ingofeachmockRAGsystem. Thisallowsusto

testARESsuccessatbothscoringandrankingthe Across almost all settings across the datasets
mockRAGsystemsappropriatelyacrossthethree from KILT and SuperGLUE, ARES provides a
| evaluationcriteria. |     |     |     |     |     | moreaccuraterankingofRAGsystemsthanRA-     |     |     |     |     |             |     |
| ------------------- | --- | --- | --- | --- | --- | ------------------------------------------ | --- | --- | --- | --- | ----------- | --- |
|                     |     |     |     |     |     | GAS.ARESaveragesaKendall’sτ                |     |     |     |     | 0.065higher |     |
| 4.3 Metrics         |     |     |     |     |     | forcontextrelevanceand0.132higherforanswer |     |     |     |     |             |     |
To calculate the correlation between the correct relevance than RAGAS. Additionally, the LLM-
rankingandtheARESranking,weusetheKendall judgeissubstantiallymoreaccuratethanRAGAS
rankcorrelationcoefficientorKendall’sτ: at predicting context relevance and answer rele-
|     |     |     |     |     |     | vance of | a query-passage-answer |     |     | triple. | For | con- |
| --- | --- | --- | --- | --- | --- | -------- | ---------------------- | --- | --- | ------- | --- | ---- |
(#ofconcordantpairs)−(#ofdiscordantpairs)
| τ = |     |                |     |     |     | textrelevance,ARESwithafine-tunedLLM-judge |     |     |     |     |     |     |
| --- | --- | -------------- | --- | --- | --- | ------------------------------------------ | --- | --- | --- | --- | --- | --- |
|     |     | # ofpairstotal |     |     |     |                                            |     |     |     |     |     |     |
is59.9percentagepointshigherthanRAGASwhile
|            |         |             |             |             |        | for answer | relevance, |      | our system | is       | 14.4 percent- |      |
| ---------- | ------- | ----------- | ----------- | ----------- | ------ | ---------- | ---------- | ---- | ---------- | -------- | ------------- | ---- |
| Concordant | pairs   | are defined | as          | two ordinal | val-   |            |            |      |            |          |               |      |
|            |         |             |             |             |        | age points | higher     | than | RAGAS.     | Overall, |               | ARES |
| ues in the | ranking | where       | the earlier | value       | in the |            |            |      |            |          |               |      |
providesamoreaccuratesystemforautomatically
| sequence | is lower | than the | later | value in | the se- |     |     |     |     |     |     |     |
| -------- | -------- | -------- | ----- | -------- | ------- | --- | --- | --- | --- | --- | --- | --- |
quence. Discordantpairsaredefinedastwoordinal evaluating RAG configurations than RAGAS by
leveragingdomain-adaptivetechniquesforprompt-
valuesintherankingwheretheearliervalueinthe
ingandtrainingaswellasutilizingPPItobolster
sequenceisgreaterthanorequaltothelatervalue
| inthesequence. |     | AKendall’sτ | greaterthan0.9is |     |     | modelpredictions. |            |             |     |     |              |     |
| -------------- | --- | ----------- | ---------------- | --- | --- | ----------------- | ---------- | ----------- | --- | --- | ------------ | --- |
|                |     |             |                  |     |     | As an             | additional | comparison, |     | we  | also include |     |
consideredsuccessfulbutitrangesfrom0.0to1.0.
|                 |     |             |     |               |     | the Kendall’s | τ   | for RAG | ranking | with | the | ARES |
| --------------- | --- | ----------- | --- | ------------- | --- | ------------- | --- | ------- | ------- | ---- | --- | ---- |
| In development, |     | researchers |     | and engineers |     |               |     |         |         |      |     |      |
LLMjudgewithoutPPI;foralldatasetstested,PPI
| will be comparing |     | different | RAG | configurations |     |     |     |     |     |     |     |     |
| ----------------- | --- | --------- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- | --- |
throughindividualpairwisecomparisonsofmodel improved the ranking prediction accuracy of the
|     |     |     |     |     |     | fine-tunedLLMjudge. |     |     | Furthermore,weincluded |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------------- | --- | --- | ---------------------- | --- | --- | --- |
choices,retrieverselection,anddocumentprepro-
asampledannotationsconfiguration,inwhichwe
cessing. WewanttomakesurethatAREShassatis-
factoryaccuracyinpairwisecomparisonsacrossa sampled150-datapointsfromeachmockRAGsys-
|     |     |     |     |     |     | tem, totalling | 1,350 |     | annotations. |     | Even with | all |
| --- | --- | --- | --- | --- | --- | -------------- | ----- | --- | ------------ | --- | --------- | --- |
varietyofperformancegapsbetweenRAGsystems.
|            |                                     |     |     |     |     | these annotations, |     | the | Kendall’s | τ   | for ARES | is  |
| ---------- | ----------------------------------- | --- | --- | --- | --- | ------------------ | --- | --- | --------- | --- | -------- | --- |
| Kendall’sτ | isexplicitlydesignedformeasuringthe |     |     |     |     |                    |     |     |           |     |          |     |
0.08higheronaverage,acrossbothcontextandan-
accuracyofsuchpairwisecomparisons,calculating
the correlation between a perfectly accurate pair- swerrelevance,comparedtosampledannotations,
|     |     |     |     |     |     | despiteusing78%lessannotations. |     |     |     |     | Insum,ARES |     |
| --- | --- | --- | --- | --- | --- | ------------------------------- | --- | --- | --- | --- | ---------- | --- |
wiserankingandanexperimentalpairwiseranking.
provessignificantlymoredata-efficientwithhuman
Thus,itisapopularandwidespreadmetricusedin
informationretrieval,allowingdeveloperstoeval- annotationswhilebeingmoreaccurateatscoring
thanstandardsampledannotationmethods.
| uate ranking | systems | empirically. |     | Therefore, | we  |     |     |     |     |     |     |     |
| ------------ | ------- | ------------ | --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
ComparedtotheGPT-3.5judge,ARESprovides
believeKendall’stauandpredictionaccuracypro-
amoreaccuraterankingoftheRAGsystemsthan
videmeaningfulmetricsfortestingtheefficacyof
theGPT-3.5judge,averagingaKendall’stau0.06
ARESasaRAGevaluationsystem.
higheroverbothcontextrelevanceandanswerrel-
5 Results&Analysis evance. Betweenthejudgeconfigurations,thefine-
tunedLLMjudgeofAREScanmorepreciselydis-
5.1 ARESRanking
tinguishbetweenRAGsystemsandguideconfigu-
Table1summarizesourmainevaluationofARES rationdecisionssurroundingdocumentsplitting,re-
(with DeBERTa-v3-Large as the pretrained basis trieverselection,andgenerativeLLMchoice. How-
forthejudges). WecompareagainstRAGAS(ver- ever,whilethefine-tunedLLMjudgehadahigher
sion0.0.18)andabaselinefew-shotpromptedGPT- Kendall’s tau on average, the GPT-3.5 judge is
3.5 judge (gpt-3.5-turbo-16k). For the few-shot morereadilydeployableanddoesnotrequireany
GPT-3.5judge,weprovidefew-shotexamplesfor additional fine-tuning. The GPT-3.5 judge does
guiding predictions; the prompts are included in comewithitsownqueryingcosts,whichcanvary
Appendices A.2, A.3, and A.4. For both ARES basedonthedateofqueryingaswellasthetotal
and the GPT-3.5 judge baseline, we augment the tokensusedinevaluation.
LLMwithPPI,usinga300-datapointhumanpref- Wealsowantedtobetterunderstandtheimpor-
erencevalidationsettorectifytheMLpredictions tanceofhumanannotationsforARES.Tothisend,
andproduceconfidenceintervals. we conducted two sets of experiments. First, we

ARESRankingofPseudoRAGSystems
| NQ       | HotpotQA | WoW      | FEVER |      | MultiRC |      | ReCoRD |      |     |
| -------- | -------- | -------- | ----- | ---- | ------- | ---- | ------ | ---- | --- |
| C.R A.R. | C.R A.R. | C.R A.R. | C.R   | A.R. | C.R     | A.R. | C.R    | A.R. |     |
Kendall’sTaufor
| 0.83 0.89 | 0.78 0.78 | 0.78 0.83 | 0.89 | 0.89 | 0.83 | 0.83 | 0.72 | 0.94 |     |
| --------- | --------- | --------- | ---- | ---- | ---- | ---- | ---- | ---- | --- |
SampledAnnotations
Kendall’sTau
| 0.89 0.89 | 0.94 0.89 | 0.94 0.94 | 0.72 | 0.61 | 0.83 | 0.94 | 0.89 | 0.44 |     |
| --------- | --------- | --------- | ---- | ---- | ---- | ---- | ---- | ---- | --- |
forRAGAS
Kendall’sTau
| 0.89 0.94 | 0.67 0.94 | 0.94 0.89 | 0.78 | 0.78 | 0.83 | 0.89 | 0.83 | 0.94 |     |
| --------- | --------- | --------- | ---- | ---- | ---- | ---- | ---- | ---- | --- |
forGPT-3.5Judge
Kendall’sTaufor
| 0.89 | 1.0 0.89 0.94 | 0.94 | 1.0 0.83 | 0.72 | 0.94 | 0.83 | 0.78 | 0.83 |     |
| ---- | ------------- | ---- | -------- | ---- | ---- | ---- | ---- | ---- | --- |
ARESLLMJudge
Kendall’sTau
| 0.94 | 1.0 0.94 0.94 | 1.0 | 1.0 0.89 | 0.78 | 0.94 | 0.89 | 0.83 | 0.89 |     |
| ---- | ------------- | --- | -------- | ---- | ---- | ---- | ---- | ---- | --- |
forARES
RAGASAccuracy 31.4%71.2%17.2%76.0%36.4%77.8%23.7%69.2%16.1%75.0%15.0%72.8%
GPT-3.5JudgeAccuracy73.8%95.5%75.3%71.6%84.3%85.2%60.4%59.6%72.4%60.3%81.0%65.8%
ARESAccuracy 79.3%97.2%92.3%81.3%85.7%96.1%88.4%78.5%85.8%82.7%67.8%92.3%
Table1: ARESRankingwithFine-tunedLLMJudgesvs. SampledAnnotations,RAGASandGPT-3.5Judge:
Forscoringcontextrelevanceandanswerrelevance(C.R.andA.R.inthetable,respectively),wecompareARES
withourfine-tunedLLMjudgesagainstsampledannotationsbenchmark,RAGAS,andafew-shotGPT-3.5judge.
Foroursampledannotations,wegather150annotateddatapointsfromeachmockRAGsystemandusethoselabels
toscorethesystem. RAGASalsousesGPT-3.5asitsjudgebutitusesfew-shotpromptsthatarenottargetedfor
eachevaluationdomain. Overall,wefoundthatARESrankedRAGsystemsmoreaccuratelythanRAGASand
GPT-3.5acrossalltheexploreddatasets. TheKendall’stauforARESwas0.065higheronaverageforscoring
contextrelevanceand0.132higheronaverageforscoringanswerrelevancethanRAGAS.Additionally,weinclude
theKendall’stausfortheARESLLMJudgewithoutPPIandfoundthatPPIfurtherboostedtherankingaccuracyof
thejudgeacrosstheboard. WeselectedGPT-3.5insteadofGPT-4duetothelowerfinancialcostsrequiredtorun.
ForPPIinbothARESandtheGPT-3.5judge,weused300humanannotationsforourhumanpreferencevalidation
set. ThepromptsusedfortheGPT-3.5judgesareincludedinSectionsA.2,A.3,andA.4.
used ARES with human annotation sets ranging otherbenchmarkdatasetsinvolveeithertablerea-
in size from 25 to 400 and found that 150 is the soning (ToTTo) or focus on passage summariza-
minimumnumberrequired(Table3). Second,we tion (QRECC) so we excluded them. In WoW
exploredwhetherGPT-4generationscouldreplace andCNN/DM,eachevaluationexampleincludes
humanannotationsentirely,findingthatGPT-4is a query, a retrieved passage, and a generated an-
lessgoodthanhumansinthisrole,thoughtheidea swer(whichiseitherfaithfulornon-attributedto
arguablyhaspromise(Table4). theretrievedpassage).
|     |     | Table2summarizesourAISresults. |     |     |     |     |     | Wefound |     |
| --- | --- | ------------------------------ | --- | --- | --- | --- | --- | ------- | --- |
5.2 ARESPerformanceonAIS
thatAREScaneffectivelyscoretheAISdatasets,
|                           |        | getting | within       | 2.5           | accuracy | points     | of  | the  | correct |
| ------------------------- | ------ | ------- | ------------ | ------------- | -------- | ---------- | --- | ---- | ------- |
| WoW                       | CNN/DM |         |              |               |          |            |     |      |         |
|                           |        | scores. | Furthermore, |               | for      | scoring    |     | each | system, |
|                           |        | we only | use          | 200 annotated |          | datapoints |     | for  | our hu- |
| ARESSplitPrediction 0.478 | 0.835  |         |              |               |          |            |     |      |         |
CorrectPositive/NegativeSplit 0.458 0.859 manpreferencevalidationset. OurresultsonAIS
| ARESJudgeAccuracy 62.5% | 84.0% |             |     |             |     |         |     |          |      |
| ----------------------- | ----- | ----------- | --- | ----------- | --- | ------- | --- | -------- | ---- |
|                         |       | demonstrate |     | the ability |     | of ARES | to  | reliably | dis- |
| EvaluationSetSize 707   | 510   |             |     |             |     |         |     |          |      |
tinguishfaithfulandhallucinatedanswersinreal-
| HumanPreferenceDataSize 200 | 200 |     |     |     |     |     |     |     |     |
| --------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
worldRAGsystems.
Table2: ARESResultsontheAISbenchmark
5.3 ARESRankingofExistingRAGSystems
ToevaluatewhetherAREScaneffectivelygauge We also wanted to evaluate whether ARES can
answerfaithfulnessinrealRAGsystems,wetested scoreandrankexistingRAGsystemsacrossboth
ARESontheAISattributionbenchmark(Rashkin contextrelevanceandanswerrelevance. Foreval-
et al., 2022). In AIS, we selected the Wizards uation, we selected the NQ, WoW, and FEVER
ofWikipedia(WoW)andCNN/DMdatasets;the datasetsfromKILT.Weconsidertheanswergen-

erations to be correct if they contained the KILT ARES to be successful. Additional examples for
answer in their output. For our RAG systems, PPI also continued to boost cross-domain ARES
weselectedthreedifferentretrievers(BM25,Ope- performanceinsubsequenttests.
nAIAdaembeddingswithcosinesimilaritysearch, While LLM judges in ARES were successful
| and ColBERTv2 | (Santhanam | et al., | 2022)) and |     |     |     |     |     |
| ------------- | ---------- | ------- | ---------- | --- | --- | --- | --- | --- |
incross-domainapplicationsforKILTandSuper-
threedifferentgenerativeLLMs(MPT-7b-Instruct GLUE,LLMjudgesareunabletogeneralizewhen
(Team, 2023), GPT-3.5-Turbo, and GPT-4). Ad- making more drastic shifts in domain, such as:
ditionally, we include the Facebook RAG model switchinglanguages(e.g. EnglishtoSpanish,Ger-
| (Lewis et | al., 2020), which | uses a DPR | retriever |     |     |     |     |     |
| --------- | ----------------- | ---------- | --------- | --- | --- | --- | --- | --- |
man,andotherlanguages),switchingfromtextto
(Karpukhin et al., 2020) and BART sequence-to- code(e.g. questions+passagestocodingfunctions
sequence model (Lewis et al., 2019). During re- + documentation), and switching from retrieving
| trieval, each | RAG system | only retrieves | one pas- |     |     |     |     |     |
| ------------- | ---------- | -------------- | -------- | --- | --- | --- | --- | --- |
texttoextractionofentities,webpages,orcitations.
sagetoassistgeneration.
|     |     |     |     | To test | cross-lingual | transfer, | we  | used the |
| --- | --- | --- | --- | ------- | ------------- | --------- | --- | -------- |
In Table 5, we found that ARES can reliably XGLUEdatasets(Liangetal.,2020);aLLMjudge
scoreandrankRAGsystemsinreal-worldapplica- fine-tunedonNQachievedaKendall’stauof0.33
tions,averagingaKendall’stauof0.91forcontext
overbothcontextrelevanceandanswerrelevance
relevance and 0.97 for answer relevance. Com- scoringforXGLUE.Totesttext-to-code,weused
paredtoRAGAS,ARESis0.16higherforcontext CodeSearchNet (Husain et al., 2019); an LLM
relevanceand0.15higherforanswerrelevance,on
|          |                                    |     |     | judge fine-tuned | on NQ        | achieved  | a Kendall’s | tau    |
| -------- | ---------------------------------- | --- | --- | ---------------- | ------------ | --------- | ----------- | ------ |
| average. | ARESalsoprovidedaccurateconfidence |     |     |                  |              |           |             |        |
|          |                                    |     |     | of 0.28 over     | both context | relevance | and         | answer |
bounds for its predictions, capturing the ground relevancescoringforCodeSearchNet. Totestex-
truthaverageoutcomesforcontextrelevanceand tractiontaskgeneralizability,weusedT-Rexfrom
answerrelevancemorethan95%ofthetime;onav-
KILT(Elsaharetal.,2018;Petronietal.,2021);an
erage,thePPIconfidenceintervalswere7.4points LLMjudgefine-tunedonNQachievedaKendall’s
wideforcontextrelevanceand6.1pointswidefor tauof0.38overbothcontextrelevanceandanswer
| answer relevance | (see                            | Figure 2 and | Figure 3 for |                |             |          |                   |          |
| ---------------- | ------------------------------- | ------------ | ------------ | -------------- | ----------- | -------- | ----------------- | -------- |
|                  |                                 |              |              | relevance      | scoring for | T-Rex.   | Each cross-domain |          |
| ARESvs.          | RAGAS).Amongthemodelstested,the |              |              |                |             |          |                   |          |
|                  |                                 |              |              | shift requires | in-domain   | passages | and               | few-shot |
best performing retriever was ColBERTv2 while queryexamplesforreconfiguringARESjudges.
thebestperforminggenerativeLLMwasGPT-4.
6 Conclusion
5.4 StrengthsandLimitsofCross-Domain
| Applications |     |     |     | Inthiswork,wepresentARES,anovelautomated |     |     |     |     |
| ------------ | --- | --- | --- | ---------------------------------------- | --- | --- | --- | --- |
The generalizability of the LLM judge used in evaluationframeworkforretrieval-augmentedgen-
ARES is critical for deploying our framework in eration (RAG). ARES offers a novel training
specialized domains, particularly domains where pipeline for fine-tuning lightweight LLM judges
in-domainqueries,documents,andanswersaredif- on synthetically generated queries and answers.
ficulttogather. Therefore,wewantedtotesthow AREScanevaluateeachcomponentofaRAGsys-
theLLMjudgesusedinARESwouldbeaffected temseparatelytohelpimprovesystemunderstand-
|                      |     |                       |     | ing and create | targeted | solutions, | and | it requires |
| -------------------- | --- | --------------------- | --- | -------------- | -------- | ---------- | --- | ----------- |
| bythreedomainshifts: |     | changeinquerytypefrom |     |                |          |            |     |             |
training to test (e.g. NQ to FEVER), change in onlyminimalhumanannotations. Fortheeightdif-
document type from training to test (e.g. NQ to ferentdatasetsinKILT,SuperGLUE,andAISre-
MultiRC),andchangeinbothqueryanddocument quiringRAG-basedsolutions,wefoundthatARES
type(e.g. NQtoReCoRD). canaccuratelyscoreandrankRAGsystemsbased
In Table 6, we found that the fine-tuned LLM oncontextrelevance,answerfaithfulness,andan-
judges used in ARES proved successful in cross- swerrelevancescores,beatingtheexistingRAGAS
automatedevaluationframework.
| domainapplications. | Acrossallsettings,wefound |     |     |     |     |     |     |     |
| ------------------- | ------------------------- | --- | --- | --- | --- | --- | --- | --- |
that LLM judges in ARES had strong generaliz- ARES is a flexible framework, and there may
ability,evenwhenonlyusing300datapointsinour bevariantsofitthatareevenmorepowerfulthan
human preference validation set for PPI. Further- the ones we explored here. Avenues to explore
more,wefoundthatevenwhentheLLMjudge’sac- includeGPT-4asareplacementforhumanlabeling
curacysufferedincross-domainapplications,PPI (Table4),morerobusttechniquesforthesynthetic
helpedmitigatethelossinaccuracyandstillallow datasetsusedinfine-tuningLLMjudges,utilizing

logits in LLM judge prediction to improve PPI Alec Radford, Ilya Sutskever, and Dario Amodei.
confidenceintervals,andtestingmoresophisticated 2020. Languagemodelsarefew-shotlearners.
LLMsasfine-tunedjudgesforARES.
|               |     |     |     |     |     |     | Jiawei Chen,        | Hongyu       | Lin,        | Xianpei  | Han,  | and Le Sun. |
| ------------- | --- | --- | --- | --- | --- | --- | ------------------- | ------------ | ----------- | -------- | ----- | ----------- |
|               |     |     |     |     |     |     | 2023.               | Benchmarking | large       | language |       | models in   |
| 7 Limitations |     |     |     |     |     |     | retrieval-augmented |              | generation. |          | arXiv | preprint    |
arXiv:2309.01431.
| ARES relies | on  | a small | set | of annotations |     | in the |     |     |     |     |     |     |
| ----------- | --- | ------- | --- | -------------- | --- | ------ | --- | --- | --- | --- | --- | --- |
humanpreferencevalidationset(roughly150-300 Hyung Won Chung, Le Hou, Shayne Longpre, Bar-
|                             |     |     |     |                  |     |     | ret Zoph, | Yi Tay, | William | Fedus, | Eric | Li, Xuezhi |
| --------------------------- | --- | --- | --- | ---------------- | --- | --- | --------- | ------- | ------- | ------ | ---- | ---------- |
| datapointsbutmoreisbetter). |     |     |     | Theseannotations |     |     |           |         |         |        |      |            |
Wang,MostafaDehghani,SiddharthaBrahma,etal.
oftenrequireanannotatorfamiliarwiththeRAG 2022. Scalinginstruction-finetunedlanguagemodels.
system’sdomainapplication. Whiletheseannota- arXivpreprintarXiv:2210.11416.
| tions can | be easy | to  | generate | for general-domain |     |     |     |     |     |     |     |     |
| --------- | ------- | --- | -------- | ------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
ZhuyunDai,VincentYZhao,JiMa,YiLuan,Jianmo
| applications, | more | specialized |     | domains, |     | such as |          |           |          |        |      |         |
| ------------- | ---- | ----------- | --- | -------- | --- | ------- | -------- | --------- | -------- | ------ | ---- | ------- |
|               |      |             |     |          |     |         | Ni, Jing | Lu, Anton | Bakalov, | Kelvin | Guu, | Keith B |
law,medicine,andfinance,mayrequireannotators Hall, and Ming-Wei Chang. 2022. Promptagator:
withspecializedexpertise. Few-shot dense retrieval from 8 examples. arXiv
preprintarXiv:2209.11755.
| The LLMs | used | in  | ARES | benefit | substantially |     |     |     |     |     |     |     |
| -------- | ---- | --- | ---- | ------- | ------------- | --- | --- | --- | --- | --- | --- | --- |
from GPU-based hardware with substantial stor- Emily Dinan, Stephen Roller, Kurt Shuster, Angela
|         |       |                  |     |     |        |     | Fan,MichaelAuli,andJasonWeston.2018. |     |     |     |     | Wizard |
| ------- | ----- | ---------------- | --- | --- | ------ | --- | ------------------------------------ | --- | --- | --- | --- | ------ |
| age. In | ARES, | DeBERTa-v3-Large |     |     | (304M) | and |                                      |     |     |     |     |        |
FLAN-T5-XXL(11.3B)requiredGPUswithabout of wikipedia: Knowledge-powered conversational
|     |     |     |     |     |     |     | agents. | arXivpreprintarXiv:1811.01241. |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------------------------------ | --- | --- | --- | --- |
32GBofmemorytorun,takingseveralhoursfor
fine-tuning and generation, respectively. While Hady Elsahar, Pavlos Vougiouklis, Arslen Remaci,
commercial GPUs are widely available, they are ChristopheGravier,JonathonHare,FrederiqueLafor-
|            |            |     |        |                 |     |     | est,andElenaSimperl.2018. |     |     | T-rex: | Alargescale |     |
| ---------- | ---------- | --- | ------ | --------------- | --- | --- | ------------------------- | --- | --- | ------ | ----------- | --- |
| not easily | accessible |     | to all | NLP researchers |     | and |                           |     |     |        |             |     |
alignmentofnaturallanguagewithknowledgebase
practitionersduetotheircosts.
|     |     |     |     |     |     |     | triples. | InProceedingsoftheEleventhInternational |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | --------------------------------------- | --- | --- | --- | --- |
Additionally,allofthedatasetsusedinoureval- ConferenceonLanguageResourcesandEvaluation
| uation of                        | ARES | are | in English, | a   | well-resourced |     | (LREC2018). |     |     |     |     |     |
| -------------------------------- | ---- | --- | ----------- | --- | -------------- | --- | ----------- | --- | --- | --- | --- | --- |
| languagewithabundantannotations. |      |     |             |     | Futurework     |     |             |     |     |     |     |     |
JinlanFu,See-KiongNg,ZhengbaoJiang,andPengfei
should explore how ARES can be employed in Liu.2023. Gptscore: Evaluateasyoudesire. arXiv
other languages by utilizing different LLMs for preprintarXiv:2302.04166.
theARESjudgeandthesyntheticdatageneration.
TianyuGao,HowardYen,JiatongYu,andDanqiChen.
Thiscanhelpusbetterunderstandthestrengthsand
2023. Enablinglargelanguagemodelstogenerate
| weaknessesofthecurrentARESframework. |     |     |     |     |     |     | textwithcitations. |     |     |     |     |     |
| ------------------------------------ | --- | --- | --- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- |
ZorikGekhman,JonathanHerzig,RoeeAharoni,Chen
|     |     |     |     |     |     |     | Elkind,andIdanSzpektor.2023. |     |     |     | Trueteacher:Learn- |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- | ------------------ | --- |
References
|     |     |     |     |     |     |     | ing factual | consistency | evaluation |     | with | large lan- |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ----------- | ---------- | --- | ---- | ---------- |
guagemodels.
| Mubashara | Akhtar, |     | Rami | Aly, |     | Christos |     |     |     |     |     |     |
| --------- | ------- | --- | ---- | ---- | --- | -------- | --- | --- | --- | --- | --- | --- |
Christodoulopoulos,OanaCocarascu,ZhijiangGuo,
KelvinGuu,KentonLee,ZoraTung,PanupongPasu-
| ArpitMittal,                    |     | MichaelSchlichtkrull, |     |     | JamesThorne,  |     |                            |     |     |                        |                    |     |
| ------------------------------- | --- | --------------------- | --- | --- | ------------- | --- | -------------------------- | --- | --- | ---------------------- | ------------------ | --- |
|                                 |     |                       |     |     |               |     | pat,andMingweiChang.2020.  |     |     |                        | Retrievalaugmented |     |
| andAndreasVlachos,editors.2023. |     |                       |     |     | Proceedingsof |     |                            |     |     |                        |                    |     |
|                                 |     |                       |     |     |               |     | languagemodelpre-training. |     |     | InInternationalconfer- |                    |     |
theSixthFactExtractionandVERificationWorkshop
enceonmachinelearning,pages3929–3938.PMLR.
(FEVER).AssociationforComputationalLinguistics,
Dubrovnik,Croatia.
PengchengHe,JianfengGao,andWeizhuChen.2021.
Debertav3:Improvingdebertausingelectra-stylepre-
AnastasiosN.Angelopoulos,StephenBates,ClaraFan- trainingwithgradient-disentangledembeddingshar-
| njiang, | Michael | I. Jordan, |     | and Tijana | Zrnic. | 2023. |     |     |     |     |     |     |
| ------- | ------- | ---------- | --- | ---------- | ------ | ----- | --- | --- | --- | --- | --- | --- |
ing. arXivpreprintarXiv:2111.09543.
Prediction-poweredinference.
|     |     |     |     |     |     |     | JeremyHowardandSebastianRuder.2018. |     |     |     |     | Universal |
| --- | --- | --- | --- | --- | --- | --- | ----------------------------------- | --- | --- | --- | --- | --------- |
TomB.Brown,BenjaminMann,NickRyder,Melanie
|     |     |     |     |     |     |     | language | model | fine-tuning | for | text classification. |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | ----- | ----------- | --- | -------------------- | --- |
Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind In Proceedings of the 56th Annual Meeting of the
Neelakantan,PranavShyam,GirishSastry,Amanda AssociationforComputationalLinguistics(Volume1:
Askell, Sandhini Agarwal, Ariel Herbert-Voss, LongPapers),pages328–339,Melbourne,Australia.
| Gretchen | Krueger, |     | Tom Henighan, |     | Rewon | Child, |     |     |     |     |     |     |
| -------- | -------- | --- | ------------- | --- | ----- | ------ | --- | --- | --- | --- | --- | --- |
AssociationforComputationalLinguistics.
| Aditya | Ramesh, | Daniel | M.  | Ziegler, | Jeffrey | Wu, |     |     |     |     |     |     |
| ------ | ------- | ------ | --- | -------- | ------- | --- | --- | --- | --- | --- | --- | --- |
ClemensWinter,ChristopherHesse,MarkChen,Eric SiqingHuo,NegarArabzadeh,andCharlesLAClarke.
Sigler,MateuszLitwin,ScottGray,BenjaminChess, 2023. Retrievingsupportingevidenceforllmsgener-
Jack Clark, Christopher Berner, Sam McCandlish, atedanswers. arXivpreprintarXiv:2306.13781.

HamelHusain,Ho-HsiangWu,TiferetGazit,Miltiadis Mike Lewis, Yinhan Liu, Naman Goyal, Marjan
Allamanis, and Marc Brockschmidt. 2019. Code- Ghazvininejad,AbdelrahmanMohamed,OmerLevy,
SearchNetchallenge: Evaluatingthestateofseman- VesStoyanov,andLukeZettlemoyer.2019. Bart:De-
ticcodesearch. arXivpreprintarXiv:1909.09436. noisingsequence-to-sequencepre-trainingfornatural
languagegeneration,translation,andcomprehension.
| Gautier | Izacard, | Patrick | Lewis, | Maria | Lomeli, | Lu- |     |     |     |     |     |     |
| ------- | -------- | ------- | ------ | ----- | ------- | --- | --- | --- | --- | --- | --- | --- |
cas Hosseini, Fabio Petroni, Timo Schick, Jane PatrickLewis,EthanPerez,AleksandraPiktus,Fabio
Dwivedi-Yu,ArmandJoulin,SebastianRiedel,and Petroni,VladimirKarpukhin,NamanGoyal,Hein-
Edouard Grave. 2022. Few-shot learning with re- richKüttler, MikeLewis, Wen-tauYih, TimRock-
trievalaugmentedlanguagemodels. arXivpreprint täschel,etal.2020. Retrieval-augmentedgeneration
arXiv:2208.03299. forknowledge-intensivenlptasks. AdvancesinNeu-
ralInformationProcessingSystems,33:9459–9474.
| JithinJamesandShahulEs.2023. |     |     |     | Ragas: | Evaluation |     |     |     |     |     |     |     |
| ---------------------------- | --- | --- | --- | ------ | ---------- | --- | --- | --- | --- | --- | --- | --- |
frameworkforyourretrievalaugmentedgeneration YaoboLiang,NanDuan,YeyunGong,NingWu,Fenfei
(rag)pipelines.
Guo,WeizhenQi,MingGong,LinjunShou,Daxin
Jiang,GuihongCao,XiaodongFan,RuofeiZhang,
JeffJohnson,MatthijsDouze,andHervéJégou.2019.
|               |     |            |        |      |       |      | Rahul   | Agrawal, | Edward          | Cui, | Sining Wei,  | Taroon |
| ------------- | --- | ---------- | ------ | ---- | ----- | ---- | ------- | -------- | --------------- | ---- | ------------ | ------ |
| Billion-scale |     | similarity | search | with | GPUs. | IEEE |         |          |                 |      |              |        |
|               |     |            |        |      |       |      | Bharti, | Ying     | Qiao, Jiun-Hung |      | Chen, Winnie | Wu,    |
TransactionsonBigData,7(3):535–547.
ShuguangLiu,FanYang,DanielCampos,Rangan
|                 |     |      |         |       |        |        | Majumder, | and | Ming | Zhou. | 2020. Xglue: | A new |
| --------------- | --- | ---- | ------- | ----- | ------ | ------ | --------- | --- | ---- | ----- | ------------ | ----- |
| Ehsan Kamalloo, |     | Aref | Jafari, | Xinyu | Zhang, | Nandan |           |     |      |       |              |       |
Thakur, and Jimmy Lin. 2023. Hagrid: A human- benchmarkdatasetforcross-lingualpre-training,un-
|     |     |     |     |     |     |     | derstandingandgeneration. |     |     | arXiv,abs/2004.01401. |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- | --------------------- | --- | --- |
llmcollaborativedatasetforgenerativeinformation-
seekingwithattribution.
|     |     |     |     |     |     |     | Yang Liu, | Dan | Iter, Yichong |     | Xu, Shuohang | Wang,   |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | ------------- | --- | ------------ | ------- |
|     |     |     |     |     |     |     | Ruochen   | Xu, | and Chenguang |     | Zhu. 2023a.  | G-eval: |
VladimirKarpukhin,BarlasOg˘uz,SewonMin,Patrick
Nlgevaluationusinggpt-4withbetterhumanalign-
Lewis,LedellWu,SergeyEdunov,DanqiChen,and
|                 |     |                               |     |     |     |     | ment,may2023. |     | arXivpreprintarXiv:2303.16634. |     |     |     |
| --------------- | --- | ----------------------------- | --- | --- | --- | --- | ------------- | --- | ------------------------------ | --- | --- | --- |
| WentauYih.2020. |     | Densepassageretrievalforopen- |     |     |     |     |               |     |                                |     |     |     |
domainquestionanswering.
|                 |     |                    |     |     |              |     | Yuxuan Liu, | Tianchi | Yang,  | Shaohan | Huang,      | Zihan |
| --------------- | --- | ------------------ | --- | --- | ------------ | --- | ----------- | ------- | ------ | ------- | ----------- | ----- |
|                 |     |                    |     |     |              |     | Zhang,      | Haizhen | Huang, | Furu    | Wei, Weiwei | Deng, |
| DanielKhashabi, |     | SnigdhaChaturvedi, |     |     | MichaelRoth, |     |             |         |        |         |             |       |
Shyam Upadhyay, and Dan Roth. 2018. Looking Feng Sun, and Qi Zhang. 2023b. Calibrating llm-
beyondthesurface: Achallengesetforreadingcom- basedevaluator. arXivpreprintarXiv:2309.13308.
| prehensionovermultiplesentences. |     |     |     |     | InProceedings |     |     |     |     |     |     |     |
| -------------------------------- | --- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- |
GrégoireMialon,RobertoDessì,MariaLomeli,Christo-
ofthe2018ConferenceoftheNorthAmericanChap-
forosNalmpantis,RamPasunuru,RobertaRaileanu,
teroftheAssociationforComputationalLinguistics:
|     |     |     |     |     |     |     | Baptiste | Rozière, | Timo | Schick, | Jane Dwivedi-Yu, |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | -------- | ---- | ------- | ---------------- | --- |
HumanLanguageTechnologies,Volume1(LongPa-
AsliCelikyilmaz,EdouardGrave,YannLeCun,and
pers),pages252–262.
|               |             |     |        |     |       |          | ThomasScialom.2023. |     |     | Augmentedlanguagemod- |     |     |
| ------------- | ----------- | --- | ------ | --- | ----- | -------- | ------------------- | --- | --- | --------------------- | --- | --- |
| Omar Khattab, | Christopher |     | Potts, | and | Matei | Zaharia. | els: asurvey.       |     |     |                       |     |     |
2021. Relevance-guidedsupervisionforopenqawith
|          |                                         |     |     |     |     |     | Sewon Min, | Kalpesh | Krishna, |          | Xinxi      | Lyu, Mike |
| -------- | --------------------------------------- | --- | --- | --- | --- | --- | ---------- | ------- | -------- | -------- | ---------- | --------- |
| colbert. | Transactionsoftheassociationforcomputa- |     |     |     |     |     |            |         |          |          |            |           |
|          |                                         |     |     |     |     |     | Lewis,     | Wen tau | Yih,     | Pang Wei | Koh, Mohit | Iyyer,    |
tionallinguistics,9:929–944.
|          |           |     |       |     |       |         | Luke Zettlemoyer, |                                       | and | Hannaneh | Hajishirzi. | 2023. |
| -------- | --------- | --- | ----- | --- | ----- | ------- | ----------------- | ------------------------------------- | --- | -------- | ----------- | ----- |
|          |           |     |       |     |       |         | Factscore:        | Fine-grainedatomicevaluationoffactual |     |          |             |       |
| Diederik | P. Kingma | and | Jimmy | Ba. | 2017. | Adam: A |                   |                                       |     |          |             |       |
precisioninlongformtextgeneration.
methodforstochasticoptimization.
FabioPetroni,AleksandraPiktus,AngelaFan,Patrick
| Tom Kocmi | and | Christian | Federmann. |     | 2023. | Large |     |     |     |     |     |     |
| --------- | --- | --------- | ---------- | --- | ----- | ----- | --- | --- | --- | --- | --- | --- |
language models are state-of-the-art evaluators of Lewis,MajidYazdani,NicolaDeCao,JamesThorne,
translationquality. arXivpreprintarXiv:2302.14520. YacineJernite,VladimirKarpukhin,JeanMaillard,
VassilisPlachouras,TimRocktäschel,andSebastian
KalpeshKrishna,ErinBransom,BaileyKuehl,Mohit Riedel. 2021. KILT: a benchmark for knowledge
Iyyer,PradeepDasigi,ArmanCohan,andKyleLo. intensivelanguagetasks. InProceedingsofthe2021
2023. LongEval:Guidelinesforhumanevaluationof Conference of the North American Chapter of the
| faithfulnessinlong-formsummarization. |     |     |     |     | InProceed- |     |                                         |     |     |     |     |       |
| ------------------------------------- | --- | --- | --- | --- | ---------- | --- | --------------------------------------- | --- | --- | --- | --- | ----- |
|                                       |     |     |     |     |            |     | AssociationforComputationalLinguistics: |     |     |     |     | Human |
ingsofthe17thConferenceoftheEuropeanChap-
LanguageTechnologies,pages2523–2544,Online.
teroftheAssociationforComputationalLinguistics, AssociationforComputationalLinguistics.
pages1650–1669,Dubrovnik,Croatia.Association
forComputationalLinguistics. Hannah Rashkin, Vitaly Nikolaev, Matthew Lamm,
|     |     |     |     |     |     |     | Lora Aroyo, | Michael |     | Collins, | Dipanjan | Das, Slav |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ------- | --- | -------- | -------- | --------- |
TomKwiatkowski, JennimariaPalomaki, OliviaRed- Petrov,GauravSinghTomar,IuliaTurc,andDavid
field,MichaelCollins,AnkurParikh,ChrisAlberti,
|     |     |     |     |     |     |     | Reitter.2022. |     | Measuringattributioninnaturallan- |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | --------------------------------- | --- | --- | --- |
DanielleEpstein,IlliaPolosukhin,JacobDevlin,Ken-
guagegenerationmodels.
| tonLee,etal.2019. |     |     | Naturalquestions: |     | abenchmark |     |     |     |     |     |     |     |
| ----------------- | --- | --- | ----------------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
forquestionansweringresearch. Transactionsofthe Jon Saad-Falcon, Omar Khattab, Keshav Santhanam,
Association for Computational Linguistics, 7:453– RaduFlorian,MartinFranz,SalimRoukos,Avirup
| 466. |     |     |     |     |     |     | Sil,MdArafatSultan,andChristopherPotts.2023. |     |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | --- | -------------------------------------------- | --- | --- | --- | --- | --- |

Udapdr: Unsupervised domain adaptation via llm (KingmaandBa,2017). Forourclassificationhead,
prompting and distillation of rerankers. arXiv we use a single linear classification layer and ap-
preprintarXiv:2303.00807.
|     |     |     |     |     |     | ply a 0.1 dropout | to  | the input, | which is | the final |
| --- | --- | --- | --- | --- | --- | ----------------- | --- | ---------- | -------- | --------- |
David P Sander and Laura Dietz. 2021. Exam: How hiddenstateofthe[CLS]token. Forourlearning
toevaluateretrieve-and-generatesystemsforusers schedule,weuselinearwarmupandlineardecay
| whodonot(yet)knowwhattheywant. |     |     |     |     | InDESIRES, |     |     |     |     |     |
| ------------------------------ | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- |
(HowardandRuder,2018)witha5e-6learningrate
pages136–146.
anda32trainingbatchsizeacrossallexperimental
| Keshav Santhanam, |     | Omar | Khattab, | Jon | Saad-Falcon, |     |     |     |     |     |
| ----------------- | --- | ---- | -------- | --- | ------------ | --- | --- | --- | --- | --- |
configurations.
| Christopher | Potts,    | and | Matei         | Zaharia. | 2022. Col-    |     |     |     |     |     |
| ----------- | --------- | --- | ------------- | -------- | ------------- | --- | --- | --- | --- | --- |
| BERTv2:     | Effective |     | and efficient |          | retrieval via |     |     |     |     |     |
A.2 GPTPromptingforContextRelevance
| lightweight | late | interaction. |     | In Proceedings | of the |     |     |     |     |     |
| ----------- | ---- | ------------ | --- | -------------- | ------ | --- | --- | --- | --- | --- |
Scoring
2022ConferenceoftheNorthAmericanChapterof
theAssociationforComputationalLinguistics: Hu- For the NQ, HotpotQA, MultiRC, and ReCoRD
manLanguageTechnologies,pages3715–3734,Seat-
datasets,weuse8few-shotexampleswiththefol-
| tle, United | States. | Association |     | for Computational |     |     |     |     |     |     |
| ----------- | ------- | ----------- | --- | ----------------- | --- | --- | --- | --- | --- | --- |
lowingprompttoscorecontextrelevance:
Linguistics.
KurtShuster,SpencerPoff,MoyaChen,DouweKiela, • Giventhefollowingquestionanddocument,
| and Jason | Weston. | 2021. | Retrieval |     | augmentation |     |     |     |     |     |
| --------- | ------- | ----- | --------- | --- | ------------ | --- | --- | --- | --- | --- |
youmustanalyzetheprovideddocumentand
reduceshallucinationinconversation.
determinewhetheritissufficientforanswer-
| MosaicML | NLP | Team. 2023. |     | Introducing | mpt-30b: |         |           |     |                  |     |
| -------- | --- | ----------- | --- | ----------- | -------- | ------- | --------- | --- | ---------------- | --- |
|          |     |             |     |             |          | ing the | question. | In  | your evaluation, | you |
Raisingthebarforopen-sourcefoundationmodels.
shouldconsiderthecontentofthedocument
| Accessed: | 2023-06-22. |     |     |     |     |         |            |     |              |           |
| --------- | ----------- | --- | --- | --- | --- | ------- | ---------- | --- | ------------ | --------- |
|           |             |     |     |     |     | and how | it relates | to  | the provided | question. |
AlexWang,YadaPruksachatkun,NikitaNangia,Aman-
Outputyourfinalverdictbystrictlyfollowing
preetSingh,JulianMichael,FelixHill,OmerLevy,
|            |         |     |       |            |          | thisformat: | "[[Yes]]"ifthedocumentissuffi- |     |     |     |
| ---------- | ------- | --- | ----- | ---------- | -------- | ----------- | ------------------------------ | --- | --- | --- |
| and Samuel | Bowman. |     | 2019. | Superglue: | A stick- |             |                                |     |     |     |
cientand"[[No]]"ifthedocumentprovidedis
ierbenchmarkforgeneral-purposelanguageunder-
standingsystems. Advancesinneuralinformation notsufficient. Donotprovideanyadditional
processingsystems,32.
explanationforyourdecision.
JiaanWang,YunlongLiang,FandongMeng,Haoxiang Question: <few-shotexamplehere>
Shi,ZhixuLi,JinanXu,JianfengQu,andJieZhou.
2023. Ischatgptagoodnlgevaluator? apreliminary Document: <few-shotexamplehere>
study. arXivpreprintarXiv:2303.04048.
|              |      |              |     |        |             | For FEVER, | we  | use the | following prompt | to  |
| ------------ | ---- | ------------ | --- | ------ | ----------- | ---------- | --- | ------- | ---------------- | --- |
| Zhilin Yang, | Peng | Qi, Saizheng |     | Zhang, | Yoshua Ben- |            |     |         |                  |     |
scorecontextrelevance:
gio,WilliamWCohen,RuslanSalakhutdinov,and
| ChristopherDManning.2018. |     |     |     | Hotpotqa: | Adataset |     |     |     |     |     |
| ------------------------- | --- | --- | --- | --------- | -------- | --- | --- | --- | --- | --- |
fordiverse,explainablemulti-hopquestionanswer- • Youareanexpertfact-checkingagent. Given
ing. arXivpreprintarXiv:1809.09600. the following statement and document, you
mustanalyzetheprovideddocumentandde-
XiangYue,BoshiWang,ZiruChen,KaiZhang,YuSu,
andHuanSun.2023. Automaticevaluationofattri- terminewhetheritissufficientfordetermining
butionbylargelanguagemodels. thestatement’sfactuality. Inyourevaluation,
Sheng Zhang, Xiaodong Liu, Jingjing Liu, Jianfeng youshouldconsiderthecontentofthedocu-
Gao, Kevin Duh, and Benjamin Van Durme. 2018. mentandhowitrelatestotheprovidedstate-
Record: Bridgingthegapbetweenhumanandma- ment’s factuality. Output your final verdict
| chinecommonsensereadingcomprehension. |     |     |     |     | arXiv |                                |     |     |             |     |
| ------------------------------------- | --- | --- | --- | --- | ----- | ------------------------------ | --- | --- | ----------- | --- |
|                                       |     |     |     |     |       | bystrictlyfollowingthisformat: |     |     | "[[Yes]]"if |     |
preprintarXiv:1810.12885.
thedocumentissufficientand"[[No]]"ifthe
LianminZheng,Wei-LinChiang,YingSheng,Siyuan documentisnotsufficient. Donotprovideany
| Zhuang, | Zhanghao | Wu, | Yonghao | Zhuang, | Zi Lin, |     |     |     |     |     |
| ------- | -------- | --- | ------- | ------- | ------- | --- | --- | --- | --- | --- |
additionalexplanationforyourdecision.
| Zhuohan | Li, | Dacheng | Li, Eric | Xing, | et al. 2023. |     |     |     |     |     |
| ------- | --- | ------- | -------- | ----- | ------------ | --- | --- | --- | --- | --- |
Judging llm-as-a-judge with mt-bench and chatbot Statement: <few-shotexamplehere>
arena. arXivpreprintarXiv:2306.05685.
|     |     |     |     |     |     | Document: | <few-shotexamplehere> |     |     |     |
| --- | --- | --- | --- | --- | --- | --------- | --------------------- | --- | --- | --- |
A Appendix
ForWoW,weusethefollowingprompttoscore
A.1 Fine-tuningConfigurationforLLM
contextrelevance:
Judges
For our loss function used in LLM judge train- • Youareanexpertdialogueagent. Giventhe
ing, we selected cross-entropy loss using Adam followingdialogueanddocument,youmust

analyzetheprovideddocumentanddetermine whether the answer addresses all aspects of
whether it is relevant for responding to the thequestionandprovidesonlycorrectinfor-
dialogue. Inyourevaluation,youshouldcon- mationfromthedocumentforansweringthe
sider the content of the document and how question. Outputyourfinalverdictbystrictly
it relates to the provided dialogue. Output followingthisformat: "[[Yes]]"iftheanswer
your final verdict by strictly following this isrelevantforthegivenquestionand"[[No]]"
format: "[[Yes]]"ifthedocumentisrelevant iftheanswerisnotrelevantforthegivenques-
and"[[No]]"ifthedocumentprovidedisnot tion. Donotprovideanyadditionalexplana-
relevant. Donotprovideanyadditionalexpla- tionforyourdecision.
nationforyourdecision.
|     |     |     |     | Question: | <few-shotexamplehere> |
| --- | --- | --- | --- | --------- | --------------------- |
Dialogue: <few-shotexamplehere> Document: <few-shotexamplehere>
| Document: | <few-shotexamplehere> |     |     |         |                       |
| --------- | --------------------- | --- | --- | ------- | --------------------- |
|           |                       |     |     | Answer: | <few-shotexamplehere> |
A.3 GPTPromptingforAnswerFaithfulness ForFEVER,wechangetheword"question"in
| Scoring |     |     |     | thepromptto"statement". | ForWoW,wechange |
| ------- | --- | --- | --- | ----------------------- | --------------- |
theword"question"inthepromptto"dialogue".
| For the NQ, | HotpotQA, | MultiRC, | and ReCoRD |     |     |
| ----------- | --------- | -------- | ---------- | --- | --- |
datasets,weuse8few-shotexampleswiththefol-
A.5 PromptingforGenerationofSynthetic
lowingprompttoscoreanswerfaithfulness:
QueriesandAnswers
• Giventhefollowingquestion,document,and To generate synthetic queries and answers using
answer,youmustanalyzetheprovidedanswer FLAN-T5, weusethefollowingpromptandpro-
vide5few-shotexamples:
anddeterminewhetheritisfaithfultothecon-
| tentsofthedocument. |     | Theanswermustnot |     |     |     |
| ------------------- | --- | ---------------- | --- | --- | --- |
• ExampleN
offernewinformationbeyondthecontextpro-
|                     |     |                   |     | Question: | <few-shotexamplehere> |
| ------------------- | --- | ----------------- | --- | --------- | --------------------- |
| videdinthedocument. |     | Theansweralsomust |     |           |                       |
notcontradictinformationprovidedinthedoc- Document: <few-shotexamplehere>
| ument.               | Output | your final verdict   | by strictly |         |                       |
| -------------------- | ------ | -------------------- | ----------- | ------- | --------------------- |
|                      |        |                      |             | Answer: | <few-shotexamplehere> |
| followingthisformat: |        | "[[Yes]]"iftheanswer |             |         |                       |
Weusethesamepromptingstructureforgener-
isfaithfultothedocumentand"[[No]]"ifthe
atingincorrectorcontradictoryanswers;wesimply
| answerisnotfaithfultothedocument. |     |     | Donot |     |     |
| --------------------------------- | --- | --- | ----- | --- | --- |
provide any additional explanation for your swapoutthefew-shotexamplestobeincorrector
contradictoryinstead.
decision.
Question: <few-shotexamplehere> A.6 SyntheticQueryandAnswerGeneration
Document: <few-shotexamplehere> Forgeneratingoursyntheticquestions,weusethe
followingpromptforFLAN-T5XXL:
| Answer: | <few-shotexamplehere> |     |     |     |     |
| ------- | --------------------- | --- | --- | --- | --- |
• Example#1
ForFEVER,wechangetheword"question"in
thepromptto"statement". ForWoW,wechange Document: <few-shotexamplehere>
theword"question"inthepromptto"dialogue". Query: <few-shotexamplehere>
Example#2
A.4 GPTPromptingforAnswerRelevance
| Scoring |     |     |     | Document: | <few-shotexamplehere> |
| ------- | --- | --- | --- | --------- | --------------------- |
For the NQ, HotpotQA, MultiRC, and ReCoRD Query: <few-shotexamplehere>
| datasets,weuse8few-shotexampleswiththefol- |     |     |     | Example#3 |     |
| ------------------------------------------ | --- | --- | --- | --------- | --- |
lowingprompttoscoreanswerrelevance:
|     |     |     |     | Document: | <few-shotexamplehere> |
| --- | --- | --- | --- | --------- | --------------------- |
• Giventhefollowingquestion,document,and Query: <few-shotexamplehere>
answer,youmustanalyzetheprovidedanswer
Example#4
| and | document before | determining | whether |           |                    |
| --- | --------------- | ----------- | ------- | --------- | ------------------ |
|     |                 |             |         | Document: | <in-domainpassage> |
theanswerisrelevantfortheprovidedques-
| tion. | Inyourevaluation,youshouldconsider |     |     | Query: |     |
| ----- | ---------------------------------- | --- | --- | ------ | --- |

Forgeneratingoursyntheticanswers,weusethe
followingpromptforFLAN-T5XXL:
• Example#1
Query: <few-shotexamplehere>
Document: <few-shotexamplehere>
Answer: <few-shotexamplehere>
Example#2
Query: <few-shotexamplehere>
Document: <few-shotexamplehere>
Answer: <few-shotexamplehere>
Example#3
Query: <few-shotexamplehere>
Document: <few-shotexamplehere>
Answer: <few-shotexamplehere>
Example#4
Query: <syntheticqueryhere>
Document: <in-domainpassagehere>
Answer:

Figure2: RAGSystemsEvaluationonNQ-ContextRelevance
Figure3: RAGSystemsEvaluationonNQ-AnswerRelevance

Kendall’sTaubyDataset
|     |     |     | NQ  | MultiRC | ReCoRD |     |
| --- | --- | --- | --- | ------- | ------ | --- |
PPILabeled
|     |     | C.R. | A.R. | C.R. A.R. | C.R. | A.R. |
| --- | --- | ---- | ---- | --------- | ---- | ---- |
Count
|     | 400 |      | 1.0 1.0 | 0.89 0.94 | 0.89 | 0.94 |
| --- | --- | ---- | ------- | --------- | ---- | ---- |
|     | 300 | 0.89 | 1.0     | 0.94 0.89 | 0.83 | 0.89 |
|     | 200 | 0.83 | 1.0     | 0.83 0.94 | 0.83 | 0.83 |
|     | 150 | 0.72 | 1.0     | 0.83 0.89 | 0.72 | 0.83 |
|     | 100 | 0.44 | 1.0     | 0.67 0.67 | 0.67 | 0.83 |
|     | 50  | 0.44 | 0.94    | 0.61 0.44 | 0.56 | 0.67 |
|     | 25  | 0.44 | 0.89    | 0.56 0.44 | 0.44 | 0.56 |
Table3: AnalysisofPPILabeledCountvs. ARESEfficacybyKendall’sTau: TheKendall’stauvaluesrepresent
thecorrelationbetweenthecorrectrankingandtheARESrankingofthepseudoRAGsystems. Weusethesame
experimentalset-upasdescribedinsubsection4.2. Wefindthatbelowabout100-150datapointsinthehuman
preferencevalidationset,AREScannotmeaningfullydistinguishbetweenthealternateRAGsystemsbasedontheir
accuraciesincontextrelevanceandanswerrelevance(C.R.andA.R.,respectively).
ARESRankingofPseudoRAGSystemsusingGPT-4Labels
|              |           | NQ      |           | ReCoRD    |           | MultiRC             |
| ------------ | --------- | ------- | --------- | --------- | --------- | ------------------- |
|              |           | Context | Answer    | Context   | Answer    | Context Answer      |
|              | Relevance |         | Relevance | Relevance | Relevance | Relevance Relevance |
| Kendall’sTau |           | 0.78    |           | 1.0 0.78  |           | 0.72 0.89 0.78      |
Kendall’sTauof
|     |     | 0.94 |     | 1.0 0.83 |     | 0.89 0.94 0.89 |
| --- | --- | ---- | --- | -------- | --- | -------------- |
HumanLabeledApproach
| AveragePPIRange |     | 9.2% | 6.8% | 8.2% | 9.0% | 7.7% 8.3% |
| --------------- | --- | ---- | ---- | ---- | ---- | --------- |
Accuracyon
|     |     | 79.3% | 96.7% | 88.4% | 78.3% | 85.8% 82.5% |
| --- | --- | ----- | ----- | ----- | ----- | ----------- |
RAGEvaluationSets
Table 4: GPT-4 Labels vs. Human Labels: We wanted to explore the practicality of using GPT-4 generated
labels instead of human annotations for our human preference validation set in ARES. In the experiments, we
generated500GPT-4labelsasreplacementsforhumanlabelingusingfew-shotprompts(seeSectionsA.2,A.3,
andA.4). WhileGPT-4generatedlabelsdecreasedKendall’stauinmostsettingsby0.05to0.30,theabilityto
cheaplyproduceGPT-4generatedlabelssignificantlyreducesthecostofannotation,cuttingitfromhundredsof
annotationstolessthantenforfew-shotprompts. Additionally, theefficacyofPPIcontinuesimprovingaswe
generatemoreGPT-4generatedlabels. Inthetable,wedefinePPIrangeasthenumberofpercentagepointsfrom
thelowernumbertotheuppernumberofthePPIconfidencebounding. Additionally,weusethefine-tunedLLM
judge(DeBERTa-v3-Large)forevaluation.

ARESRankingofRealRAGSystems
|     |     |     | NQ   |      | WoW  |      | FEVER     |     |
| --- | --- | --- | ---- | ---- | ---- | ---- | --------- | --- |
|     |     |     | C.R. | A.R. | C.R. | A.R. | C.R. A.R. |     |
Kendall’sTaufor
|     |     | 0.73 |     | 0.78 | 0.73 | 0.73 | 0.73 0.82 |     |
| --- | --- | ---- | --- | ---- | ---- | ---- | --------- | --- |
SampledAnnotations
Kendall’sTau
|     |     | 0.82 |     | 0.82 | 0.73 | 0.82 | 0.73 0.87 |     |
| --- | --- | ---- | --- | ---- | ---- | ---- | --------- | --- |
forRAGAS
Kendall’sTau
|     |     | 0.82 |     | 0.87 | 0.82 | 0.82 | 0.64 0.87 |     |
| --- | --- | ---- | --- | ---- | ---- | ---- | --------- | --- |
forGPT-3.5Judge
Kendall’sTau
|     |     | 0.91 |     | 0.96 | 0.91 | 1.0 | 0.73 0.87 |     |
| --- | --- | ---- | --- | ---- | ---- | --- | --------- | --- |
forARESLLMJudge
Kendall’sTau
|     |     | 1.0 |     | 0.96 | 0.91 | 1.0 | 0.82 1.0 |     |
| --- | --- | --- | --- | ---- | ---- | --- | -------- | --- |
forARES
| RAGASAccuracy   |     | 35.9% |     | 68.2% | 44.4% | 80.1% | 21.4% 75.9% |     |
| --------------- | --- | ----- | --- | ----- | ----- | ----- | ----------- | --- |
| GPT-3.5Accuracy |     | 80.5% |     | 91.2% | 81.2% | 83.5% | 61.3% 54.5% |     |
| ARESAccuracy    |     | 85.6% |     | 93.3% | 84.5% | 88.2% | 70.4% 84.0% |     |
Table5: ARESRankingonReal-WorldRAGSystems: Forscoringcontextrelevanceandanswerrelevance
(C.R.andA.R.inthetable,respectively),wecompareARESwithourfine-tunedLLMjudgesagainstsampled
annotations benchmark, RAGAS, and a few-shot GPT-3.5 judge. For our sampled annotations, we gather 150
annotateddatapointsfromeachmockRAGsystemandusethoselabelstoscorethesystem. RAGASalsouses
GPT-3.5asitsjudgebutitusesfew-shotpromptsthatarenottargetedforeachevaluationdomain. Overall,we
foundthatARESrankedRAGsystemsmoreaccuratelythanRAGASandGPT-3.5acrossalltheexploreddatasets.
Additionally,weincludetheKendall’stausfortheARESLLMJudgewithoutPPIandfoundthatPPIfurtherboosted
therankingaccuracyofthejudgeacrosstheboard. WeselectedGPT-3.5insteadofGPT-4duetothelowerfinancial
costsrequiredtorun. ForPPIinbothARESandtheGPT-3.5judge,weused300humanannotationsforourhuman
preferencevalidationset. ThepromptsusedfortheGPT-3.5judgesareincludedinSectionsA.2,A.3,andA.4.
ARESCross-DomainRankingofPseudoRAGSystems
|     | NQto      | FEVERto |      | NQto    |      | MultiRCto | NQto           | ReCoRDto  |
| --- | --------- | ------- | ---- | ------- | ---- | --------- | -------------- | --------- |
|     | FEVER     |         | NQ   | MultiRC |      | NQ        | ReCoRD         | NQ        |
|     | C.R. A.R. | C.R.    | A.R. | C.R.    | A.R. | C.R.      | A.R. C.R. A.R. | C.R. A.R. |
Kendall’sTau 0.89 0.89 1.0 0.83 0.94 0.89 1.0 0.89 0.78 0.89 0.89 0.94
Kendall’sTauof
|     | 0.89 0.78 | 0.94 |     | 1.0 0.94 | 0.89 | 0.94 | 1.0 0.83 0.89 | 0.94 1.0 |
| --- | --------- | ---- | --- | -------- | ---- | ---- | ------------- | -------- |
In-DomainLLMJudge
AveragePPIRange 8.7% 7.2% 6.5%11.5%10.2%11.3%11.9%11.5%10.5%10.1% 9.7% 6.2%
Accuracyon
RAGEvaluationSets 92.4%28.4%85.7%22.6%81.5%92.1%87.6%80.2%29.1%81.2%80.1%92.1%
Table 6: Cross-Domain Usage of Fine-tuned LLM Judges: We tested the cross-domain application of the
fine-tunedLLMjudgeintheARESframework. Wefoundthatforbothcontextrelevanceandanswerrelevance
(C.R.andA.R.inthetable,respectively),fine-tunedLLMjudgesshowedstronggeneralizabilityacrossdomains
whenchangingquerytype(e.g. NQandFEVER),documenttype(e.g. NQandMultiRC),orboth(e.g. NQand
ReCoRD).ForPPI,weused300labeledexamplesforourhumanpreferencevalidationsetbutalsofoundthat
additionalexamplesfurtherimprovedtheperformanceofARES.Furthermore,wefoundthateveninscenarios
wherethefine-tunedLLMjudge’saccuracysignificantlydroppedout-of-domain(e.g. answerrelevanceforNQ
toFEVER),PPImitigatedthedecreaseinjudgeperformance. Inthetable,wedefinePPIrangeasthenumberof
percentagepointsfromthelowerboundtotheupperboundofthePPIconfidenceinterval.

Context Answer
Query Passage Answer
Relevance Relevance
Mechanicalenergyisacombinationoftheenergyofmotionorposition.
Howcanaballthatisnot
Thistypeofenergydescribesobjectsthataremovingorcouldmove. Theballholds
movingpossessenergy 1 1
Amovingballcanhaveenergyfrommotion.Anarrowcanalsohave mechanicalenergy
ofposition?
theenergyofmotion.Botharetypesofmechanicalenergy.
OnelookatFredRooney,andyoujustknowhe’sthegoodguy.
Atraceofchildishinnocenceinhisfacegivesthelanky
WhohasaJimmy BethlehemlawyeraJimmyStewart-likequalityofquiettrust.
Stewart-likequality Inblackjeansandbutton-downshirt,he’sakindoffolkhero FredRooney 1 1
ofquiettrust? inthesouthBethlehemmeltingpotwherehe’scraftedalaw
practicecateringtoworking-classfamilies-mostlyLatino-
intheshadowofthehulkishremnantsofBethlehemSteel.
Survivingbeingshotandstabbedattheendofthepreviousfilm,
thestepfatherhasbeeninstitutionalizedinPugetSound,Washingtonsince,
spendinghistimebuildingmodelhousesintheworkshop.
AssignedanewdoctornamedJosephDanversthestepfather
beginsconfidinginhimtogainhistrust,ultimatelymurdering
Beforehemurderthe thedoctorduringasessionbystabbinghimintheneckwitha
doctorandRalphSmith, bladesmuggledoutoftheworkshop.AfterkillingDanversthestepfather
LosAngeles 1 0
wheredidthestepfather beatsasuspiciousguardnamedRalphSmithtodeathwithhisownnightstick
reside? withonlytwostrikesandtakeshisuniform,successfully
sneakingoutofthesanitarium.Checkingintoahotelafterrobbingand
murderingatravelingsalesmanthestepfatheraltershisappearance,
takesthenameDoctorGeneF.Cliffordfromthenewspaperobituaries
andtravelstoPalmMeadows,LosAngelesafterseeinganadforiton
anepisodeofDreamHouse.
AfterarrivinginNewYorkCity,Einsteinwastakentovariousplacesand
events,includingChinatown,alunchwiththeeditorsoftheNewYork
Times,andaperformanceofCarmenattheMetropolitanOpera,
wherehewascheeredbytheaudienceonhisarrival.
Whatwasthenameofthe VasilySzaitsevportrayed
Duringthedaysfollowing,hewasgiventhekeystothecitybyMayor
2006filmaboutPushkin’sdeath, Pushkininthefilm 0 0
JimmyWalkerandmetthepresidentofColumbiaUniversity,who
andwhoportrayedPushkin? PushkinReturns
describedEinsteinas"Therulingmonarchofthemind."Harry
EmersonFosdick,pastoratNewYork’sRiversideChurch,gave
Einsteinatourofthechurchandshowedhimafull-sizestatuethat
thechurchmadeofEinstein,standingattheentrance.
Table7: PositiveandNegativesEvaluationExamples
