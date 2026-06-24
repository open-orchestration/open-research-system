Constructing A Multi-hop QA Dataset for Comprehensive Evaluation of
Reasoning Steps
XanhHo♥♣,Anh-KhoaDuongNguyen♦,SakuSugawara♣,AkikoAizawa♥♣
♥ TheGraduateUniversityforAdvancedStudies,Kanagawa,Japan
♣ NationalInstituteofInformatics,Tokyo,Japan
♦ NationalInstituteofAdvancedIndustrialScienceandTechnology,Tokyo,Japan
{xanh, saku, aizawa}@nii.ac.jp
khoa.duong@aist.go.jp
Abstract
A multi-hop question answering (QA) dataset aims to test reasoning and inference skills by
requiring a model to read multiple paragraphs to answer a given question. However, current
datasets do not provide a complete explanation for the reasoning process from the question to
theanswer. Further,previousstudiesrevealedthatmanyexamplesinexistingmulti-hopdatasets
do not require multi-hop reasoning to answer a question. In this study, we present a new multi-
hop QA dataset, called 2WikiMultiHopQA, which uses structured and unstructured data. In
our dataset, we introduce the evidence information containing a reasoning path for multi-hop
questions. Theevidenceinformationhastwobenefits: (i)providingacomprehensiveexplanation
forpredictionsand(ii)evaluatingthereasoningskillsofamodel. Wecarefullydesignapipeline
and a set of templates when generating a question–answer pair that guarantees the multi-hop
stepsandthequalityofthequestions. WealsoexploitthestructuredformatinWikidataanduse
logical rules to create questions that are natural but still require multi-hop reasoning. Through
experiments,wedemonstratethatourdatasetischallengingformulti-hopmodelsanditensures
thatmulti-hopreasoningisrequired.
1 Introduction
Machine reading comprehension (MRC) aims at teaching machines to read and understand given text.
Many current models (Devlin et al., 2019; Liu et al., 2019; Yang et al., 2019) have defeated humans
on the performance of SQuAD (Rajpurkar et al., 2016; Rajpurkar et al., 2018), as shown on its leader-
board1. However, such performances do not indicate that these models can completely understand the
text. Specifically,usinganadversarialmethod,JiaandLiang(2017)demonstratedthatthecurrentmod-
els do not precisely understand natural language. Moreover, Sugawara et al. (2018) demonstrated that
many datasets contain a considerable number of easy instances that can be answered based on the first
fewwordsofthequestions.
Multi-hopMRCdatasetsrequireamodeltoreadandperformmulti-hopreasoningovermultiplepara-
graphstoansweraquestion. Currently,therearefourmulti-hopdatasetsovertextualdata: ComplexWe-
bQuestions (Talmor and Berant, 2018), QAngaroo (Welbl et al., 2018), HotpotQA (Yang et al., 2018),
andR4C(Inoueetal.,2020). Thefirsttwodatasetswerecreatedbyincorporatingthedocuments(from
WeborWikipedia)withaknowledgebase(KB).Owingtotheirbuildingprocedures,thesedatasetshave
noinformationtoexplainthepredictedanswers. Meanwhile,theothertwodatasetswerecreatedmainly
basedoncrowdsourcing. InHotpotQA,theauthorsintroducedthesentence-levelsupportingfacts(SFs)
informationthatareusedtoexplainthepredictedanswers. However,asdiscussedinInoueetal.(2020),
thetaskofclassifyingsentence-levelSFsisabinaryclassificationtaskthatisincapableofevaluatingthe
reasoningandinferenceskillsofthemodel. Further, dataanalyses(ChenandDurrett, 2019; Minetal.,
2019)revealedthatmanyexamplesinHotpotQAdonotrequiremulti-hopreasoningtosolve.
Recently, toevaluatetheinternalreasoningofthereadingcomprehensionsystem,Inoueetal.(2020)
proposed a new dataset R4C that requires systems to provide an answer and derivations. A derivation
This work is licensed under a Creative Commons Attribution 4.0 International License. License details: http://
creativecommons.org/licenses/by/4.0/.
1https://rajpurkar.github.io/SQuAD-explorer/
0202
voN
21
]LC.sc[
2v06010.1102:viXra

is a semi-structured natural language form that is used to explain the answers. R4C is created based on
HotpotQAandhas4,588questions. However,thesmallsizeofthedatasetimpliesthatthedatasetcannot
beusedasamulti-hopdatasetwithacomprehensiveexplanationfortrainingend-to-endsystems.
In this study, we create a large and high quality multi-hop dataset 2WikiMultiHopQA2 with a com-
prehensiveexplanationbycombiningstructuredandunstructureddata. Toenhancetheexplanationand
evaluationprocesswhenansweringamulti-hopquestiononWikipediaarticles,weintroducenewinfor-
mationineachsample,namelyevidencethatcontainscomprehensiveandconciseinformationtoexplain
the predictions. Evidence information in our dataset is a set of triples, where each triple is a structured
data(subjectentity,property,objectentity)obtainedfromtheWikidata(seeFigure1foranexample).
Figure 1: Example of an inference question in our dataset. The difference between our dataset and
HotpotQAistheevidenceinformationthatexplainsthereasoningpath.
Ourdatasethasfourtypesofquestions: comparison,inference,compositional,andbridgecomparison.
All questions in our dataset are created by using a set of predefined templates. Min et al. (2019) clas-
sified the comparison questions in HotpotQA in three types: multi-hop, context-dependent multi-hop,
and single-hop. Based on this classification, we removed all templates in our list that make questions
becomesingle-hoporcontext-dependentmulti-hoptoensurethatourcomparisonquestionsandbridge-
comparisonquestionsaremulti-hop. Wecarefullydesignedapipelinetoutilizetheintersectioninforma-
tionbetweenthesummary3ofWikipediaarticlesandWikidataandhaveaspecialtreatmentforeachtype
ofquestionthatguaranteesmulti-hopstepsandthequalityofthequestions. Further,byutilizingthelogi-
calruleinformationintheknowledgegraph,suchasfather(a,b)∧father(b,c) ⇒ grandfather(a,c),
wecancreatemorenaturalquestionsthatstillrequiremulti-hopreasoning.
We conducted two different evaluations on our dataset: difficulty and multi-hop reasoning of the
dataset. Toevaluatethedifficulty,weusedamulti-hopmodeltocomparetheperformanceofHotpotQA
andourdataset. Overall,theresultsfromourdatasetarelowerthanthoseobservedinHotpotQA,while
human scores are comparable on both datasets. This suggests that the number of difficult questions in
our dataset is greater than that in HotpotQA. Similar to Min et al. (2019), we used a single-hop BERT
model to test the multi-hop reasoning in our dataset. The result of our dataset is lower than the result
of HotpotQA by 8.7 F1, indicating that a lot of examples in our dataset require multi-hop reasoning to
be solved. Through experiments, we confirmed that although our dataset is generated by hand-crafted
templates and the set of predefined logical rules, it is challenging for multi-hop models and requires
multi-hopreasoning.
22WikiisacombinationofWikipediaandWikidata.
3Anothernameis“shortdescription”;Theshortdescriptionatthetopofanarticlethatsummarizesthecontent. Seealso
https://en.wikipedia.org/wiki/Wikipedia:Short_description

Insummary,ourmaincontributionsareasfollows: (1)WeuseWikipediaandWikidatatocreatealarge
andhighqualitymulti-hopdatasetthathascomprehensiveexplanationsfromquestiontoanswer. (2)We
provide new information in each sample—evidence information useful for interpreting the predictions
andtestingthereasoningandinferenceskillsofthemodel. (3)Weuselogicalrulestogenerateasimple
naturalquestionbutstillrequirethemodeltoundertakemulti-hopreasoningwhenansweringaquestion.
The full dataset, baseline model, and all information that we used when constructing the dataset are
availableathttps://github.com/Alab-NII/2wikimultihop.
2 TaskOverview
2.1 TaskFormalizationandMetrics
We formulated (1) answer prediction, (2) sentence-level SFs prediction, and (3) evidence generation
tasksasfollows:
• Input: aquestionQandasetofdocumentsD.
• Output: (1) find an answer A (a textual span in D) for Q, (2) find a set of sentence-level SFs
(sentences)inDthatamodelusedtoanswerQ,and(3)generateasetofevidenceE whichconsists
oftriplesthatdescribesthereasoningpathfromQtoA.
We evaluate the three tasks by using two evaluation metrics: exact match (EM) and F1 score. Fol-
lowingpreviouswork(Yangetal.,2018),toassesstheentirecapacityofthemodel,weintroducedjoint
metricsthatcombinetheevaluationofanswerspans,sentence-levelSFs,andevidenceasfollows:
2PjointRjoint
JointF1 = (1)
Pjoint+Rjoint
where Pjoint = PansPsupPevi and Rjoint = RansRsupRevi. (Pans, Rans), (Psup,Rsup), and
(Pevi,Revi) denote the precision and recall of the answer spans, sentence-level SFs, and evidence, re-
spectively. JointEMis1onlywhenallthethreetasksobtainanexactmatchorotherwise0.
2.2 QuestionTypes
Inourdataset,wehavethefollowingfourtypesofquestions: (1)comparison,(2)inference,(3)compo-
sitional,and(4)bridgecomparison. Theinferenceandcompositionalquestionsarethetwosubtypesof
thebridgequestionwhichcomprisesabridgeentitythatconnectsthetwoparagraphs(Yangetal.,2018).
1. Comparisonquestionisatypeofquestionthatcomparestwoormoreentitiesfromthesamegroup
insomeaspectsoftheentity(Yangetal.,2018). Forinstance,acomparisonquestioncomparestwo
or more people with the date of birth or date of death (e.g., Who was born first, Albert Einstein or
AbrahamLincoln?).
2. Inferencequestioniscreatedfromthetwotriples(e,r ,e )and(e ,r ,e )intheKB.Weutilized
1 1 1 2 2
the logical rule to acquire the new triple (e,r,e ), where r is the inference relation obtained from
2
the two relations r and r . A question–answer pair is created by using the new triple (e,r,e ),
1 2 2
its question is created from (e,r) and its answer is e . For instance, using two triples (Abraham
2
Lincoln,mother,NancyHanksLincoln)and(NancyHanksLincoln,father,JamesHanks),weobtain
a new triple (Abraham Lincoln, maternal grandfather, James Hanks). A question is: Who is the
maternalgrandfatherofAbrahamLincoln? AnanswerisJamesHanks(Section3.2).
3. Compositionalquestioniscreatedfromthetwotriples(e,r ,e )and(e ,r ,e )intheKB.Com-
1 1 1 2 2
pared with inference question, the difference is that no inference relation r exists from the two
relations r and r . For instance, there are two triples (La La Land, distributor, Summit Entertain-
1 2
ment) and (Summit Entertainment, founded by, Bernd Eichinger). There is no inference relation r
fromthetworelationsdistributorandfounded-by. Inthiscase,aquestioniscreatedfromtheentity
e and the two relations r and r : Who is the founder of the company that distributed La La Land
1 2
film? Anansweristheentitye ofthesecondtriple: BerndEichinger(Section3.2).
2

4. Bridge-comparison question is a type of question that combines the bridge question with the
comparison question. It requires both finding the bridge entities and doing comparisons to obtain
the answer. For instance, instead of directly compare two films, we compare the information of
the directors of the two films, e.g., Which movie has the director born first, La La Land or Tenet?
To answer this type of question, the model needs to find the bridge entity that connects the two
paragraphs,oneaboutthefilmandoneaboutthedirector,togetthedateofbirthinformation. Then,
makingacomparisontoobtainthefinalanswer.
3 DataCollection
3.1 WikipediaandWikidata
Inthisstudy,weutilizedbothtextdescriptionsfromWikipedia4andasetofstatementsfromWikidatato
constructourdataset. WeusedonlyasummaryfromeachWikipediaarticleasaparagraphthatdescribes
an entity. Wikidata5 is a collaborative KB that stores data in a structured format. Wikidata contains a
setofstatements(eachstatementincludespropertyandanobjectentity)todescribetheentity. Thereis
a connection between Wikipedia and Wikidata for each entity. From Wikidata, we can extract a triple
(s,r,o),wheresisasubjectentity,r isapropertyorrelation,andoisanobjectentity. Astatementfor
theentitysis(r,o). Anobjectentitycanbeanotherentityorthedatevalue. Wecategorizedallentities
basedonthevalueofthepropertyinstanceof inWikidata(AppendixA.1).
3.2 DatasetGenerationProcess
Generatingamulti-hopdatasetinourframeworkinvolvesthreemainsteps: (1)createasetoftemplates,
(2) generate data, and (3) post-process generated data. After obtaining the generated data, we used a
modeltosplitthedataintotrain,dev,andtestsets.
(1) Create a Set of Templates: For the comparison question, first, we used Spacy6 to extract named
entity recognition (NER) tags and labels for all comparison questions in the train data of HotpotQA
(17,456 questions). Then, we obtained a set of templates L by replacing the words in the questions
with the labels obtained from the NER tagger. We manually created a set of templates based on L for
entities in the top-50 most popular entities in Wikipedia. We focused on a set of specific properties of
eachentitytype(AppendixA.2)intheKB.Wealsodiscardedalltemplatesthatmadequestionsbecome
single-hop or context-dependent multi-hop as discussed in Min et al. (2019). Based on the templates
of the comparison question, we manually enhanced it to create the templates for bridge-comparison
questions(AppendixA.5). Wemanuallycreatedalltemplatesforinferenceandcompositionalquestions
(AppendixA.3andA.4).
Fortheinferencequestion,weutilizedlogicalrulesintheknowledgegraphtocreateasimplequestion
butstillrequiremulti-hopreasoning. Extractinglogicalrulesisataskintheknowledgegraphwhereinthe
targetmakesthegraphcomplete. Weobservethatlogicalrules,suchasspouse(a,b)∧mother(b,c) ⇒
mother in law(a,c), can be used to test the reasoning skill of the model. Based on the results of the
AMIE model (Gala´rraga et al., 2013), we manually checked and verified all logical rules to make it
suitablefortheWikidatarelations. Weobtained28logicalrules(AppendixA.3).
(2)GenerateData: Fromthesetoftemplatesandallentities’information, wegeneratedcomparison
questionsasdescribedinAlgorithm1(AppendixA.6). Foreachentitygroup,werandomlyselectedtwo
entities: e ande . Subsequently,weobtainedthesetofstatementsofeachentityfromWikidata. Then,
1 2
weprocessedthetwosetsofstatementstoobtainasetofmutualrelations(M)betweentwoentities. We
thenacquiredtheWikipediainformationforeachentity. ForeachrelationinM,forexample,arelation
r , we checked whether we can use this relation. Because our dataset is a span extraction dataset, the
1
answer is extracted from the Wikipedia article of each entity. With relation r , we obtained the two
1
values o and o from the two triples (e ,r ,o ) and (e ,r ,o ) of the two entities, respectively. The
1 2 1 1 1 2 1 2
4https://www.wikipedia.org
5https://www.wikidata.org
6https://spacy.io/

requirementhereisthatthevalueo mustappearintheWikipediaarticlefortheentitye , whichisthe
1 1
sameconditionforthesecondentitye .
2
When all information passed the requirements, we generated a question–answer pair that includes a
questionQ,acontextC,thesentence-levelSFsSF,theevidenceE,andananswerA. Qisobtainedby
replacingthetwotokens#nameinthetemplatebythetwoentitylabels. C isaconcatenationofthetwo
Wikipedia articles that describe the two entities. E is the two triples (e ,r ,o ) and (e ,r ,o ). SF is
1 1 1 2 1 2
a set of sentence indices where the values o and o are extracted. Based on the type of questions, we
1 2
undertakecomparisonsandobtainthefinalanswerA.
We generated bridge questions as described in Algorithm 2 (Appendix A.6). For each entity group,
we randomly selected an entity e and then obtained a set of statements of the entity from Wikidata.
Subsequently, based on the first relation information in R (the set of predefined relations), we filtered
thesetofstatementstoobtainasetof1-hopH . Next,foreachelementinH ,weperformedthesame
1 1
process to obtain a set of 2-hop H , each element in H is a tuple (e,r ,e ,r ,e ). For each tuple in
2 2 1 1 2 2
H , we obtained the Wikipedia articles for two entities e and e . Then, we checked the requirements
2 1
to ensure that this sample can become a multi-hop dataset. For instance, the two paragraphs p and p
1
describe for e and e , respectively (see Figure 2). The bridge entity requirement is that p must mention
1
e . Thespanextractionanswerrequirementisthatp mustmentione . The2-hoprequirementsarethat
1 1 2
pmustnotcontaine andp mustnotcontaine. Finally,weobtainedQ,C,SF,E,andAsimilarlyto
2 1
theprocessincomparisonquestions.
Figure2: TheRequirementsforbridgequestionsinourdataset.
(3)Post-processGeneratedData: Werandomlyselectedtwoentitiestocreateaquestionwhengen-
erating the data; therefore, a large number of no questions exist in the yes/no questions. We performed
post-processingtofinalizethedatasetthatbalancesthenumberofyesandnoquestions. Questionscould
haveseveraltrueanswersintherealworld. Toensureonesamplehasonlyoneanswer,wediscardedall
ambiguouscasesinthedataset(AppendixA.7).
CollectDistractorParagraphs: FollowingYangetal.(2018)andMinetal.(2019), weusedbigram
tf-idf (Chen et al., 2017) to retrieve the top-50 paragraphs from Wikipedia that are most similar to the
question. Then, we used the entity type of the two gold paragraphs (four gold paragraphs for bridge-
comparisonquestion)toselectthetop-8paragraphs(top-6forbridge-comparisonquestion)andconsid-
ered it as a set of distractor paragraphs. We shuffled the 10 paragraphs (including gold and distractor
paragraphs)andobtainedacontext.
Dataset Statistics (A Benchmark Setting): We used a single-hop model (Section 5.1) to split the
train,dev,andtestsets. Weconductedfive-foldcross-validationonalldata. TheaverageF1scoreofthe
modelis86.7%. Allquestionssolvedbythesingle-hopmodelareconsideredasatrain-mediumsubset.
Therestwassplitintothreesubsets: train-hard,dev,andtest(balancingthenumberofdifferenttypesof
questionsineachsubset). StatisticsofthedatasplitcanbefoundinTable1. Weusedtrain-mediumand
train-hard asthetrainingdatainourdataset.
4 DataAnalysis
Question and Answer Lengths We quantitatively analyze the properties of questions and answers
for each type of question in our dataset. The statistics of the dataset are presented in Table 2. The
compositional question has the greatest number of examples, and the inference question has the least

| Name         | Split | #Examples | TypeofQ           | #Examples |         | #Avg. Q | #Avg. A |
| ------------ | ----- | --------- | ----------------- | --------- | ------- | ------- | ------- |
| train-medium | train | 154,878   | Comparison        |           | 57,989  | 11.97   | 1.58    |
| train-hard   | train | 12,576    | Inference         |           | 7,478   | 8.41    | 3.15    |
| dev          | dev   | 12,576    | Compositional     |           | 86,979  | 11.43   | 2.05    |
| test         | test  | 12,576    | Bridge-comparison |           | 40,160  | 17.01   | 2.01    |
| Total        |       | 192,606   | Total             |           | 192,606 | 12.64   | 1.94    |
Table1: Datastatistics. Table2: Questionandanswerlengthsacrossthedifferenttype
|     |     |     | ofquestions. Qistheabbreviationfor“question”,andAisfor |     |     |     |     |
| --- | --- | --- | ------------------------------------------------------ | --- | --- | --- | --- |
“answer”.
number of examples. To ensure one question has only one possible answer, we used the information
fromWikidataandremovedmanyinferencequestionsthatmayhavemorethanoneanswer. Theaverage
question length of the inference questions is the smallest because they are created from one triple. The
averagequestionlengthofthebridge-comparisonquestionsisthelargestbecauseitcombinesbothbridge
question and comparison question. The average answer lengths of comparison and bridge-comparison
questionsaresmallerthaninferenceandcompositionalquestions. Thisisbecausetherearemanyyes/no
questionsinthecomparisonquestions.
| ReasoningType | Example |     |     |     |     |     |     |
| ------------- | ------- | --- | --- | --- | --- | --- | --- |
Comparison ParagraphA:TheodorHaecker(June4,1879-April9,1945)wasa...
question: Paragraph B: Harry Vaughan Watkins (10 September 1875 – 16 May 1945)
| comparingtwo | wasaWelshrugbyunionplayer... |     |     |     |     |     |     |
| ------------ | ---------------------------- | --- | --- | --- | --- | --- | --- |
Q:Wholivedlonger,TheodorHaeckerorHarryVaughanWatkins?
entities
Compositional ParagraphA:Versus(Versace)isthediffusionlineofItalian...,agiftbythe
question: inferring founderGianniVersacetohissister,DonatellaVersace. ...
thebridgeentityto ParagraphB:GianniVersace...Versacewasshotandkilledoutside...
| findtheanswer | Q:WhydidthefounderofVersusdie? |     |     |     |     |     |     |
| ------------- | ------------------------------ | --- | --- | --- | --- | --- | --- |
Inferencequestion: ParagraphA: DambarShah(? –1645)wasthekingoftheGorkhaKingdom
| usinglogicalrules | ...HewasthefatherofKrishnaShah. |     |     | ... |     |     |     |
| ----------------- | ------------------------------- | --- | --- | --- | --- | --- | --- |
andinferringthe ParagraphB:KrishnaShah(? –1661)...HewasthefatherofRudraShah.
| bridgeentity | Q:WhoisthegrandchildofDambarShah? |     |     |     |     |     |     |
| ------------ | --------------------------------- | --- | --- | --- | --- | --- | --- |
Bridge-comparison ParagraphA:FAQ:FrequentlyAskedQuestionsisafeature-lengthdystopian
question: inferring movie,writtenanddirectedbyCarlosAtanesandreleasedin2004. ...
thebridgeentity ParagraphB:TheBigMoney...directedbyJohnPaddyCarstairs...
| anddoing | ParagraphC:CarlosAtanesisaSpanishfilmdirector... |     |     |     |     |     |     |
| -------- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- |
comparisons ParagraphD:JohnPaddyCarstairswasaprolificBritishfilmdirector...
Q: Are both director of film FAQ: Frequently Asked Questions and director of
filmTheBigMoneyfromthesamecountry?
|     | Table3: | Typesofmulti-hopreasoninginourdataset. |     |     |     |     |     |
| --- | ------- | -------------------------------------- | --- | --- | --- | --- | --- |
Multi-hop Reasoning Types Table 3 presents different types of multi-hop reasonings in our dataset.
Comparisonquestionsrequirequantitativeorlogicalcomparisonsbetweentwoentitiestoobtainthean-
swer. Thesystemisrequiredtounderstandthepropertiesinthequestion(e.g.,dateofbirth). Composi-
tionalquestionsrequirethesystemtoanswerseveralprimitivequestionsandcombinethem. Forinstance,
to answer the question Why did the founder of Versus die?, the system must answer two sub-questions
sequentially: (1)WhoisthefounderofVersus? and(2)Whydidhe/shedie?. Inferencequestionsrequire
thatthesystemunderstandsseverallogicalrules. Forinstance,tofindthegrandchild,first,itshouldfind
thechild. Then,basedonthechild,continuetofindthechild. Bridge-comparisonquestionsrequireboth
findingthebridgeentityanddoingacomparisontoobtainthefinalanswer.

Answer Types We preserved all information when generating the data; hence, we used the answer
information (both string and Wikidata id) to classify the types of answers. Based on the value of the
propertyinstanceof inWikidata,weobtained708uniquetypesofanswers. Thetop-5typesofanswers
in our dataset are: yes/no (31.2%), date (16.9%; e.g., July 10, 2010), film (13.5%; e.g., La La Land),
human(11.7%;e.g.,GeorgeWashington),andbigcity(4.7%;e.g.,Chicago). Fortheremainingtypesof
answers(22.0%),theyarevarioustypesofentitiesinWikidata.
5 Experiments
5.1 EvaluatetheDatasetQuality
Weconductedtwodifferentevaluationsonourdataset: evaluatethedifficultyandthemulti-hopreason-
ing. Toevaluatethedifficulty,weusedthemulti-hopmodelasdescribedinYangetal.(2018)toobtain
the results on HotpotQA (distractor setting) and our dataset. Table 4 presents the results. For the SFs
prediction task, the scores on our dataset are higher than those on HotpotQA. However, for the answer
prediction task, the scores on our dataset are lower than those on HotpotQA. Overall, on the joint met-
rics, the scores on our dataset are lower than those on HotpotQA. This indicates that given the human
performance on both datasets is comparable (see Section 5.3), the number of difficult questions in our
datasetisgreaterthanthatinHotpotQA.
Answer SpFact Joint
Dataset
EM F1 EM F1 EM F1
HotpotQA 44.48 58.54 20.68 65.66 10.97 40.52
OurDataset 34.14 40.95 26.47 66.94 9.22 26.76
Table4: Results(%)ofthemulti-hopmodelonHotpotQA(Yangetal.,2018)andourdataset. “SpFact”
istheabbreviationforthesentence-levelsupportingfactspredictiontask.
Similar to Min et al. (2019), we used a single-hop BERT model (Devlin et al., 2019) to test the
multi-hop reasoning in our dataset. The F1 score on HotpotQA is 64.6 (67.0 F1 in Min et al. (2019));
meanwhile, the F1 score on our dataset is 55.9. The result of our dataset is lower than the result of
HotpotQA by 8.7 F1. It indicates that a large number of examples in our dataset require multi-hop
reasoning to be solved. Moreover, it is verified that our data generation and our templates guarantee
multi-hopreasoning. Insummary,theseresultsshowthatourdatasetischallengingformulti-hopmodels
andrequiresmulti-hopreasoningtobesolved.
Figure3: Ourbaselinemodel. TherightpartisthebaselinemodelofHotpotQA(Yangetal.,2018).

5.2 BaselineResults
We modified the baseline model in Yang et al. (2018) and added a new component (the orange block
in Figure 3) to perform the evidence generation task. We re-used several techniques of the previous
baseline, such as bi-attention, to predict the evidence. Our evidence information is a set of triples, with
eachtripleincludingsubjectentity,relation,andobjectentity. First,weusedthequestiontopredictthe
relations and then used the predicted relations and the context (after predicting sentence-level SFs) to
obtainthesubjectandobjectentities.
Table 5 presents the results of our baseline model. We used the evaluation metrics as described in
Section 2.1. As shown in the table, the scores of the sentence-level SFs prediction task are quite high.
This is a binary classification task that classifies whether each sentence is a SF. As discussed, this task
is incapable of evaluating the reasoning and inference skills of the model. The scores of the evidence
generation task are quite low which indicates this task is difficult. Our error analysis shows that the
model can predict one correct triple in the set of the triples. However, accurately obtaining the set of
triplesisextremelychallenging. ThisisthereasonwhytheEMscoreisverylow. Webelievethatadding
theevidencegenerationtaskisappropriatetotestthereasoningandinferenceskills.
|     | Answer | SpFact | Evidence | Joint |
| --- | ------ | ------ | -------- | ----- |
Split/Task
|      | EM          | F1 EM F1    | EM F1      | EM F1     |
| ---- | ----------- | ----------- | ---------- | --------- |
| Dev  | 35.30 42.45 | 23.85 64.31 | 1.08 14.77 | 0.37 5.03 |
| Test | 36.53 43.93 | 24.99 65.26 | 1.07 14.94 | 0.35 5.41 |
Table5: Results(%)ofthebaselinemodel.
Toinvestigatethedifficultyofeachtypeofquestion,wecategorizedtheperformanceforeachtypeof
question(onthetestsplit). Table6showstheresults. Fortheanswerpredictiontask,themodelobtained
highscoresoninferenceandcompositionalquestions. Meanwhile,forthesentence-levelSFsprediction
task,themodelobtainedhighscoresoncomparisonandbridge-comparisonquestions. Overall,thejoint
metric score of the inference question is the lowest. This indicates that this type of question is more
challenging for the model. The evidence generation task has the lowest score for all types of questions
whencomparedwiththeothertwotasks. Thissuggeststhattheevidencegenerationtaskischallenging
foralltypesofquestions.
|     | Answer | SpFact | Evidence | Joint |
| --- | ------ | ------ | -------- | ----- |
TypeofQuestion
|               | EM F1       | EM F1       | EM F1      | EM F1     |
| ------------- | ----------- | ----------- | ---------- | --------- |
| Comparison    | 26.49 27.86 | 26.76 65.02 | 0.00 12.40 | 0.00 2.45 |
| Inference     | 41.10 62.60 | 10.77 49.45 | 0.00 2.85  | 0.00 1.40 |
| Compositional | 50.40 59.94 | 18.28 57.44 | 2.57 17.65 | 0.84 9.19 |
Bridge-Comparison 18.47 20.45 43.74 89.16 0.00 19.17 0.00 3.60
| Table6: Results(%)ofthebaselinemodelondifferenttypesofquestions. |     |     |     |     |
| ---------------------------------------------------------------- | --- | --- | --- | --- |
5.3 HumanPerformance
We obtained a human performance on 100 samples that are randomly chosen from the test split. Each
sample was annotated by three workers (graduate students). We provided the question, context, and a
set of predefined relations (for the evidence generation task) and asked a worker to provide an answer,
a set of sentence-level SFs, and a set of evidence. Similar to the previous work (Yang et al., 2018),
we computed the upper bound for human performance by acquiring the maximum EM and F1 for each
sample. AlltheresultsarepresentedinTable7.
Theworkersachievedhigherperformancethanthatofthemodel. Thehumanperformanceforthean-
swerpredictiontaskis91.0EMand91.8F1. Therestillseemstoberoomforimprovement,whichmight
be because the mismatch information between Wikipedia and Wikidata makes questions unanswerable

Answer SpFact Evidence Joint
Setting
EM F1 EM F1 EM F1 EM F1
Model 50.00 58.48 29.00 69.90 0.00 16.74 0.00 9.79
Human(average) 80.67 82.34 85.33 92.63 57.67 75.63 53.00 66.69
HumanUpperBound(UB) 91.00 91.79 88.00 93.75 64.00 78.81 62.00 75.25
Table7: Comparingbaselinemodelperformancewithhumanperformance(%)on100randomsamples.
(see Section 5.4 for an analysis). The human performance of the answer prediction task on our dataset
(91.8F1UB)showsarelativelysmallgapagainstthatonHotpotQA(98.8F1UB;borrowedfromtheir
paper). Although the baseline model is able to predict the answer and sentence-level SFs, it is not very
effective at finding the evidence. We also observe that there is a large gap between the performance of
human and the model in the evidence generation task (78.8 and 16.7 F1). Therefore, this could be a
new challenging task for explaining multi-hop reasoning. We conjecture that the main reason why the
score of the evidence generation task was low is the ambiguity in the names of Wikidata. For example,
inWikidata, onepersoncanhavemultiplenames. Weuseonlyonenameinthegroundtruth, whilethe
workers can use other names. Future research might explore these issues to ensure the quality of the
dataset. Overall, our baseline results are far behind human performance. This shows that our dataset is
challengingandthereisampleroomforimprovementinthefuture.
5.4 AnalysisofMismatchedExamplesbetweenWikipediaandWikidata
As mentioned in Section 5.3, there are unanswerable questions in our dataset due to the mismatch in-
formation between Wikipedia articles and Wikidata knowledge. In the dataset generation process, for a
triple (s,r,o), we first checked whether the object entity o appears or not in the Wikipedia article that
describes the entity s. Our assumption is that the first sentence in the article in which the object entity
o appears is the most important, which we decided to use for the QA pair generation. For instance, we
obtainedatriple: (LordWilliamBeauclerk,mother,LadyDianadeVere)fromWikidata,andweobtained
a paragraph p from the Wikipedia article that describes “Lord William Beauclerk”. We used the object
entity“LadyDianadeVere”toobtainthefirstsentenceinp“BeauclerkwasthesecondsonofCharles
Beauclerk, 1st Duke of St Albans, and his wife Lady Diana de Vere, ....” From this sentence, we can
inferthatthemotherof“LordWilliamBeauclerk”is“LadyDianadeVere”. However,becauseweonly
checked whether the object entity o appears in the sentence or not, there could be a semantic mismatch
betweenthesentenceandthetriple. Forinstance,weobtainedatriple: (RakelDink,spouse,HrantDink)
from Wikidata, while we obtained the first sentence from Wikipedia article: “Rakel Dink (born 1959)
is a Turkish Armenian human rights activist and head of the Hrant Dink Foundation.” Obviously, from
thissentence, wecannotinferthat“HrantDink”isthespouseof“RakelDink”. Therefore, wedefined
heuristics to exclude these mismatched cases as much as possible. In particular, we found that some
exampleshavesubjectentitiesthataresimilar/equaltotheirobjectentitiesandarelikelytobecomemis-
matchedcases. Forsuchcases,wemanuallycheckedthesamplesanddecidedtouseorremovethemfor
our final dataset. Nonetheless, there are still cases that our heuristics cannot capture. To estimate how
manymismatchedcasesourheuristicscannotcaptureinthedataset,werandomlyselected100samples
in the training set and manually checked them. We obtained eight out of 100 samples that have a mis-
match between Wikipedia article and Wikidata triple. For the next version of the dataset, we plan to
improve our heuristics by building a list of keywords for each relation to check the correspondence be-
tweenWikipediasentenceandWikidatatriple. Forinstance,weobservedthatfortherelation“mother”,
thesentencesoftencontainphrases: “sonof”,“daughterof”,“hismother”,and“hermother”.
6 RelatedWork
Multi-hop questions in MRC domain Currently, four multi-hop MRC datasets proposed for tex-
tual data: ComplexWebQuestions (Talmor and Berant, 2018), QAngaroo (Welbl et al., 2018), Hot-
potQA (Yang et al., 2018), and R4C (Inoue et al., 2020). Recently, Chen et al. (2020) introduced the

HybridQAdataset—amulti-hopquestionansweringoverbothtabularandtextualdata. Thedatasetwas
createdbycrowdsourcingbasedonWikipediatablesandWikipediaarticles.
Multi-hopquestionsinKBdomain Questionansweringovertheknowledgegraphhasbeeninvesti-
gated for decades. However, most current datasets (Berant et al., 2013; Bordes et al., 2015; Yih et al.,
2015;Diefenbachetal.,2017)consistofsimplequestions(single-hop). Zhangetal.(2018b)introduced
the METAQA dataset that contains both single-hop and multi-hop questions. Abujabal et al. (2017) in-
troduced the ComplexQuestions dataset comprising 150 compositional questions. All of these datasets
aresolvedbyusingtheKBonly. OurdatasetisconstructedbasedontheintersectionbetweenWikipedia
andWikidata. Therefore,itcanbesolvedbyusingstructuredorunstructureddata.
Compositional Knowledge Base Inference Extracting Horn rules from the KB has been studied ex-
tensively in the Inductive Logic Programming literature (Quinlan, 1990; Muggleton, 1995). From the
KB, there are several approaches that mine association rules (Agrawal et al., 1993) and several mine
logical rules (Schoenmackers et al., 2010; Gala´rraga et al., 2013). We observed that these rules can be
usedtotestthereasoningskillofthemodel. Therefore,inthisstudy,weutilizedthelogicalrulesinthe
form: r (a,b)∧r (b,c) ⇒ r(a,c). ComplexWebQuestionsandQAngaroodatasetsarealsoutilizedKB
1 2
whenconstructingthedataset,buttheydonotutilizethelogicalrulesaswedid.
RC datasets with explanations Table 8 presents several existing datasets that provide explanations.
HotpotQA and R4C are the most similar works to ours. HotpotQA provides a justification explanation
(collectionsofevidencetosupportthedecision)intheformofasetofsentence-levelSFs. R4Cprovides
bothjustificationandintrospectiveexplanations(howadecisionismade). Ourstudyalsoprovidesboth
justification and introspective explanations. The difference is that the explanation in our dataset is a set
oftriples, whereeachtripleisastructureddataobtainedfromWikidata. Meanwhile, theexplanationin
R4C is a set of semi-structured data. R4C is created based on HotpotQA and has 4,588 questions. The
small size of the dataset implies that it cannot be used for training end-to-end neural network models
involvingthemulti-hopreasoningwithcomprehensiveexplanation.
Explanations
Task/Dataset Size
Justification Introspective
Ourwork 192,606
R4C(Inoueetal.,2020) 4,588
CoS-E(Rajanietal.,2019) 19,522
HotpotQA(Yangetal.,2018) 112,779
ScienceExamQA(Jansenetal.,2016) 363
Table8: Comparisonwithotherdatasetswithexplanations.
7 Conclusion
Inthisstudy,wepresented2WikiMultiHopQA—alargeandhighqualitymulti-hopdatasetthatprovides
comprehensive explanations for predictions. We utilized logical rules in the KB to create more natural
questionsthatstillrequiremulti-hopreasoning. Throughexperiments,wedemonstratedthatourdataset
ensures multi-hop reasoning while being challenging for the multi-hop models. We also demonstrated
that bootstrapping the multi-hop MRC dataset is beneficial by utilizing large-scale available data on
WikipediaandWikidata.
Acknowledgments
We would like to thank An Tuan Dao, Johannes Mario Meissner Blanco, Kazutoshi Shinoda, Napat
Thumwanit, Taichi Iki, Thanakrit Julavanich, and Vitou Phy for their valuable support in the procedure
of constructing the dataset. We thank the anonymous reviewers for suggestions on how to improve the
datasetandthepaper. ThisworkwassupportedbyJSPSKAKENHIGrantNumber18H03297.

References
Abdalghani Abujabal, Mohamed Yahya, Mirek Riedewald, and Gerhard Weikum. 2017. Automated template
generationforquestionansweringoverknowledgegraphs. InProceedingsofthe26thInternationalConference
onWorldWideWeb,WWW’17,page1191–1200,RepublicandCantonofGeneva,CHE.InternationalWorld
WideWebConferencesSteeringCommittee.
RakeshAgrawal, TomaszImieliundefinedski, andArunSwami. 1993. Miningassociationrulesbetweensetsof
itemsinlargedatabases. InProceedingsofthe1993ACMSIGMODInternationalConferenceonManagement
ofData,SIGMOD’93,page207–216,NewYork,NY,USA.AssociationforComputingMachinery.
JonathanBerant,AndrewChou,RoyFrostig,andPercyLiang. 2013. SemanticparsingonFreebasefromquestion-
answerpairs. InProceedingsofthe2013ConferenceonEmpiricalMethodsinNaturalLanguageProcessing,
pages1533–1544,Seattle,Washington,USA,October.AssociationforComputationalLinguistics.
AntoineBordes,NicolasUsunier,SumitChopra,andJasonWeston. 2015. Large-scalesimplequestionanswering
withmemorynetworks. volumeabs/1506.02075.
JifanChenandGregDurrett. 2019. UnderstandingdatasetdesignchoicesforMulti-hopreasoning. InProceed-
ingsofthe2019ConferenceoftheNorthAmericanChapteroftheAssociationforComputationalLinguistics:
HumanLanguageTechnologies,Volume1(LongandShortPapers),pages4026–4032,Minneapolis,Minnesota,
June.AssociationforComputationalLinguistics.
DanqiChen,AdamFisch,JasonWeston,andAntoineBordes. 2017. ReadingWikipediatoansweropen-domain
questions. InProceedingsofthe55thAnnualMeetingoftheAssociationforComputationalLinguistics(Volume
1: LongPapers),pages1870–1879,Vancouver,Canada,July.AssociationforComputationalLinguistics.
Wenhu Chen, Hanwen Zha, Zhi yu Chen, Wenhan Xiong, Hong Wang, and Wei Wang. 2020. HybridQA: A
datasetofmulti-hopquestionansweringovertabularandtextualdata. ArXiv,abs/2004.07347.
JacobDevlin,Ming-WeiChang,KentonLee,andKristinaToutanova. 2019. BERT:Pre-trainingofdeepbidirec-
tionaltransformersforlanguageunderstanding. InProceedingsofthe2019ConferenceoftheNorthAmerican
ChapteroftheAssociationforComputationalLinguistics:HumanLanguageTechnologies,Volume1(Longand
ShortPapers),pages4171–4186,Minneapolis,Minnesota,June.AssociationforComputationalLinguistics.
DennisDiefenbach,ThomasTanon,KamalSingh,andPierreMaret. 2017. Questionansweringbenchmarksfor
Wikidata. 10.
Luis Antonio Gala´rraga, Christina Teflioudi, Katja Hose, and Fabian Suchanek. 2013. AMIE: Association rule
mining under incomplete evidence in ontological knowledge bases. In Proceedings of the 22nd International
ConferenceonWorldWideWeb,WWW’13,page413–422,NewYork,NY,USA.AssociationforComputing
Machinery.
NaoyaInoue,PontusStenetorp,andKentaroInui. 2020. R4C:AbenchmarkforevaluatingRCsystemstogetthe
rightanswerfortherightreason. InProceedingsofthe58thAnnualMeetingoftheAssociationforComputa-
tionalLinguistics,pages6740–6750,Online,July.AssociationforComputationalLinguistics.
PeterJansen,NiranjanBalasubramanian,MihaiSurdeanu,andPeterClark. 2016. What’sinanexplanation?Char-
acterizing knowledge and inference requirements for elementary science exams. In Proceedings of COLING
2016, the 26th International Conference on Computational Linguistics: Technical Papers, pages 2956–2965,
Osaka,Japan,December.TheCOLING2016OrganizingCommittee.
Robin Jia and Percy Liang. 2017. Adversarial examples for evaluating reading comprehension systems. In
Proceedingsofthe2017ConferenceonEmpiricalMethodsinNaturalLanguageProcessing,pages2021–2031,
Copenhagen,Denmark,September.AssociationforComputationalLinguistics.
Yinhan Liu, Myle Ott, Naman Goyal, Jingfei Du, Mandar Joshi, Danqi Chen, Omer Levy, Mike Lewis, Luke
Zettlemoyer,andVeselinStoyanov. 2019. RoBERTa: ArobustlyoptimizedBERTpretrainingapproach. vol-
umeabs/1907.11692.
ChristopherD.Manning,MihaiSurdeanu,JohnBauer,JennyFinkel,PrismaticInc,StevenJ.Bethard,andDavid
Mcclosky. 2014. TheStanfordCoreNLPnaturallanguageprocessingtoolkit. InInACL,SystemDemonstra-
tions.
SewonMin,EricWallace,SameerSingh,MattGardner,HannanehHajishirzi,andLukeZettlemoyer. 2019. Com-
positionalquestionsdonotnecessitatemulti-hopreasoning. InProceedingsofthe57thAnnualMeetingofthe
Association for Computational Linguistics, pages 4249–4257, Florence, Italy, July. Association for Computa-
tionalLinguistics.

StephenMuggleton. 1995. InverseentailmentandProgol.
J. R. Quinlan. 1990. Learning logical definitions from relations. volume 5, page 239–266, USA, September.
KluwerAcademicPublishers.
NazneenFatemaRajani,BryanMcCann,CaimingXiong,andRichardSocher. 2019. Explainyourself! Leverag-
inglanguagemodelsforcommonsensereasoning. InProceedingsofthe57thAnnualMeetingoftheAssociation
forComputationalLinguistics,pages4932–4942,Florence,Italy,July.AssociationforComputationalLinguis-
tics.
Pranav Rajpurkar, Jian Zhang, Konstantin Lopyrev, and Percy Liang. 2016. SQuAD: 100,000+ questions for
machine comprehension of text. In Proceedings of the 2016 Conference on Empirical Methods in Natural
LanguageProcessing,pages2383–2392,Austin,Texas,November.AssociationforComputationalLinguistics.
PranavRajpurkar, RobinJia, and PercyLiang. 2018. Knowwhatyou don’tknow: Unanswerablequestions for
SQuAD. InProceedingsofthe56thAnnualMeetingoftheAssociationforComputationalLinguistics(Volume
2: ShortPapers),pages784–789,Melbourne,Australia,July.AssociationforComputationalLinguistics.
StefanSchoenmackers,JesseDavis,OrenEtzioni,andDanielWeld. 2010. Learningfirst-orderHornclausesfrom
webtext. InProceedingsofthe2010ConferenceonEmpiricalMethodsinNaturalLanguageProcessing,pages
1088–1098,Cambridge,MA,October.AssociationforComputationalLinguistics.
Saku Sugawara, Kentaro Inui, Satoshi Sekine, and Akiko Aizawa. 2018. What makes reading comprehension
questionseasier? InProceedingsofthe2018ConferenceonEmpiricalMethodsinNaturalLanguageProcess-
ing,pages4208–4219,Brussels,Belgium,October-November.AssociationforComputationalLinguistics.
Alon Talmor and Jonathan Berant. 2018. The web as a knowledge-base for answering complex questions. In
Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational
Linguistics:HumanLanguageTechnologies,Volume1(LongPapers),pages641–651,NewOrleans,Louisiana,
June.AssociationforComputationalLinguistics.
Johannes Welbl, Pontus Stenetorp, and Sebastian Riedel. 2018. Constructing datasets for multi-hop reading
comprehensionacrossdocuments. volume6,pages287–302.TransactionsoftheAssociationforComputational
Linguistics.
ZhilinYang,PengQi,SaizhengZhang,YoshuaBengio,WilliamCohen,RuslanSalakhutdinov,andChristopherD.
Manning. 2018. HotpotQA:Adatasetfordiverse,explainablemulti-hopquestionanswering. InProceedings
of the 2018 Conference on Empirical Methods in Natural Language Processing, pages 2369–2380, Brussels,
Belgium,October-November.AssociationforComputationalLinguistics.
Zhilin Yang, Zihang Dai, Yiming Yang, Jaime Carbonell, Russ R Salakhutdinov, and Quoc V Le. 2019. XL-
Net: Generalized autoregressive pretraining for language understanding. In Advances in Neural Information
ProcessingSystems32,pages5753–5763.CurranAssociates,Inc.
Wen-tau Yih, Ming-Wei Chang, Xiaodong He, and Jianfeng Gao. 2015. Semantic parsing via staged query
graph generation: Question answering with knowledge base. In Proceedings of the 53rd Annual Meeting of
theAssociationforComputationalLinguisticsandthe7thInternationalJointConferenceonNaturalLanguage
Processing (Volume 1: Long Papers), pages 1321–1331, Beijing, China, July. Association for Computational
Linguistics.
YuyuZhang,HanjunDai,ZornitsaKozareva,AlexanderJ.Smola,andLeSong. 2018b. Variationalreasoningfor
question answering with knowledge graph. In The Thirty-Second AAAI Conference on Artificial Intelligence
(AAAI-18).

A DataCollectionDetails
A.1 DataPreprocessing
We used both dump7 and online version of Wikipedia and Wikidata. We downloaded the dump of
EnglishWikipediaonJanuary1,2020,andthedumpofEnglishWikidataonDecember31,2019. From
Wikidata and Wikipedia, we obtained 5,950,475 entities. Based on the value of the property instance
of in Wikidata, we categorized all entities into 23,763 groups. In this dataset, we focused on the most
popularentities(top-50forcomparisonquestions). Whencheckingtherequirementstoensurethemulti-
hop reasoning of the dataset, several entities in the multi-path are not present in the dump version; in
suchsituations,weusedtheonlineversionofWikipediaandWikidata.
We observed that the quality of the dataset depends on the quality of the intersection information
between Wikipedia and Wikidata. Specifically, for the property related to date information, such as
publication date and date of birth, information between Wikipedia and Wikidata is quite consistent.
Meanwhile, for the property occupation, information between Wikipedia and Wikidata is inconsistent.
Forinstance,theWikipediaoftheentityEbenezerAdamisasfollows: “EbenezerAdamwasaGhanaian
educationist and politician.”; meanwhile, the value from Wikidata of the property occupation is politi-
cian. Insuchsituations,wemanuallycheckallsamplesrelatedtothepropertytoensuredatasetquality.
For the property related to the country name, we handled many different similar names by using the
aliasesoftheentityandthesetofdemonyms. Moreover,toguaranteethequalityofthedataset,weonly
focusedonthesetofpropertieswithhighconsistencybetweenWikipediaandWikidata.
WeusedbothStanfordCoreNLP(Manningetal.,2014)andSpacytoperformsentencesegmentation
forthecontext.
A.2 ComparisonQuestions
Table 9 presents all information of our comparison question. We can use more entities and properties
fromWikidatatocreateadataset. Inthisversionofthedataset,wefocusedonthetop-50popularentities
in Wikipedia and Wikidata. To ensure dataset quality, we used the set of properties as described in the
table. For each combination between the entity and the property, we have various templates for asking
questionstoensurediversityinthequestions.
A.3 InferenceQuestions
We argued that logical rules are difficult to apply to multi-hop questions. We obtained a set of 50
inference relations, but we cannot use all of it into the dataset. For instance, the logical rule is
placeofbirth(a,b) ∧ country(b,c) ⇒ nationality(a,c); this rule easily fails after checking the re-
quirements. To guarantee the multi-hop reasoning of the question, the document describing a person
a having a place of birth b should not contain the information about the country c. However, most
paragraphsdescribinghumansoftencontaininformationontheirnationality.
Theotherissueisensuringthateachsamplehasonlyonecorrectansweronthetwogoldparagraphs.
Withthelogicalrulebeingchild(a,b)∧child(b,c) ⇒ grandchild(a,c), ifahasmorethanonechild,
for instance a has three children b , b and b , then each b has their own children. Therefore, for the
1 2 3
question “Who is the grandchild of a?”, there are several possible answers to this question. To address
this issue in our dataset, we only utilized the relation that has only one value in the triple on Wikidata.
Thatisthereasonwhythenumberofinferencequestionsinourdatasetisquitesmall. Table10describes
allinferencerelationsusedinourdataset.
In most cases, this rule will be correct. However, several rules can be false in some cases. In such
situations,basedontheWikidatainformation,wedouble-checkedthenewtriplebeforedecidingwhether
touseit. Forinstance,theruleisdoctoral advisor(a,b)∧employer(b,c) ⇒ educated at(a,c),ahas
an advisor is b, b works at c, and we can infer that a studies at c. There can be exceptions that b works
at many places, and c is one of them, but a does not study at c. We used Wikidata to check whether a
studiesatcbeforedecidingtouseit.
Toobtainthequestion,weusedthesetoftemplatesinTable11.
7https://dumps.wikimedia.org/

| EntityType | Property      |             | #Templates |
| ---------- | ------------- | ----------- | ---------- |
| Human      | dateofbirth   |             | 7          |
|            | dateofdeath   |             | 3          |
|            | date of birth | and date of | 2          |
death(yearold)
|                                 | occupation           |     | 18  |
| ------------------------------- | -------------------- | --- | --- |
|                                 | countryofcitizenship |     | 11  |
|                                 | placeofbirth         |     | 1   |
| Film                            | publicationdate      |     | 5   |
|                                 | director             |     | 2   |
|                                 | producer             |     | 2   |
|                                 | countryoforigin      |     | 7   |
| Album                           | publicationdate      |     | 5   |
|                                 | producer             |     | 2   |
| Musicalgroup                    | inception            |     | 4   |
|                                 | countryoforigin      |     | 7   |
| Song                            | publicationdate      |     | 5   |
| Museum,Airport,Magazine,Railway | inception            |     | 1-3 |
station,Business,Building,Churchbuilding,
| Highschool,School,University       | country |     | 4   |
| ---------------------------------- | ------- | --- | --- |
| Mountain,River,Island,Lake,Village | country |     | 4   |
Table9: TemplatesofComparisonquestions.
A.4 CompositionalQuestions
Forthistypeofquestion,weutilizedvariousentitiesandpropertiesonWikidata. Weusedthefollowing
properties(13properties)asthefirstrelation: composer,creator,director,editor,father,foundedby,has
part, manufacturer, mother, performer, presenter, producer, and spouse. Further, we used the following
properties (22 properties) as the second relation: date of birth, date of death, place of birth, country of
citizenship,placeofdeath,causeofdeath,spouse,occupation,educatedat,awardreceived,father,place
ofburial,child,employer,religion,fieldofwork,mother,inception,country,foundedby,studentof,and
placeofdetention. Acompositionalquestionwascreatedbycombiningthefirstrelationandthesecond
relation(ignoreduplicatecase).
We used the following entities (15 entities) to create this type of question: human, film, animated
feature film, album, university, film production company, business, television program, candy, written
work,literarywork,musicalgroup,song,magazine,newspaper. Weobtainedatotalof799templates.

| Relation1       | Relation2   | InferenceRelation   |     |     |
| --------------- | ----------- | ------------------- | --- | --- |
| spouse          | spouse      | co-husband/co-wife  |     |     |
| spouse          | father      | father-in-law       |     |     |
| spouse          | mother      | mother-in-law       |     |     |
| spouse          | sibling     | sibling-in-law      |     |     |
| spouse          | child       | child/stepchild     |     |     |
| father          | father      | paternalgrandfather |     |     |
| father          | mother      | paternalgrandmother |     |     |
| father          | spouse      | mother/stepmother   |     |     |
| father          | child       | sibling             |     |     |
| father          | sibling     | uncle/aunt          |     |     |
| mother          | mother      | maternalgrandmother |     |     |
| mother          | father      | maternalgrandfather |     |     |
| mother          | spouse      | father/stepfather   |     |     |
| mother          | child       | sibling             |     |     |
| mother          | sibling     | uncle/aunt          |     |     |
| child           | child       | grandchild          |     |     |
| child           | sibling     | child               |     |     |
| child           | mother      | wife                |     |     |
| child           | father      | husband             |     |     |
| child           | spouse      | child-in-law        |     |     |
| sibling         | sibling     | sibling             |     |     |
| sibling         | spouse      | sibling-in-law      |     |     |
| sibling         | mother      | mother              |     |     |
| sibling         | father      | father              |     |     |
| doctoralstudent | educatedat  | employer            |     |     |
| doctoralstudent | fieldofwork | fieldofwork         |     |     |
| doctoraladvisor | employer    | educatedat          |     |     |
| doctoraladvisor | fieldofwork | fieldofwork         |     |     |
Table10: Inferencerelationinformationinourdataset.
| Relation |     | Template(s) |     |     |
| -------- | --- | ----------- | --- | --- |
aunt,child-in-law,child,co-husband,
co-wife,father-in-law,father,grandchild,
Whoisthe#relationof#name?
grandfather,grandmother,husband,
Whois#name’s#relation?
mother-in-law,mother,sibling-in-law,
sibling,stepchild,stepfather,stepmother,
uncle,wife
| educatedat |     | Which#instance | of answerdid#name |     |
| ---------- | --- | -------------- | ----------------- | --- |
studyat?
|     |     | Which#instance | of answerdid#name |     |
| --- | --- | -------------- | ----------------- | --- |
graduatefrom?
| employer |     | Which #instance | of answer | does |
| -------- | --- | --------------- | --------- | ---- |
#nameworkat?
Wheredoes#namework?
| fieldofstudy |     | Whatisthefieldofstudyof#name? |     |     |
| ------------ | --- | ----------------------------- | --- | --- |
Table11: TemplatesofInferencequestion.

A.5 Bridge-comparisonQuestions
Thetop-3popularentitiesonWikipediaandWikidataarehuman,taxon,andfilm. Inthistypeofquestion,
wefocusedonthecombinationbetweenhumanandfilm. Table12presentsthecombinationbetweenthe
relationsfromthetwoentitieshumanandfilminourdataset.
Relation1 Relation2
director dateofbirth
director dateofdeath
director countryofcitizenship
producer dateofbirth
producer dateofdeath
producer countryofcitizenship
Table12: Bridge-comparisonquestion’sinformation.
Foreach rowinTable 12, we haveseveralways toaska question. Forinstance, in thefirstrow, with
thecombinationofthetworelationsdirector anddateofbirth,wehavevariouswaystoaskaquestion,
asshowninTable13. Toavoidambiguouscases,weensuredthateachfilmweusedhasonlyonedirector
oroneproducer. Atotalof62templateswasobtainedforthistypeofquestion.
Templates
Whichfilmhasthedirectorbornfirst,#nameor#name?
Whichfilmwhosedirectorwasbornfirst,#nameor#name?
Whichfilmhasthedirectorwhowasbornfirst,#nameor#name?
Whichfilmhasthedirectorbornearlier,#nameor#name?
Whichfilmhasthedirectorwhowasbornearlier,#nameor#name?
Whichfilmwhosedirectorisyounger,#nameor#name?
Whichfilmhasthedirectorbornlater,#nameor#name?
Whichfilmhasthedirectorwhowasbornlater,#nameor#name?
Whichfilmhasthedirectorwhoisolderthantheother,#nameor#name?
Whichfilmhasthedirectorwhoisolder,#nameor#name?
Table13: TemplatesofBridge-comparisonquestions.
A.6 GenerateData
The algorithms for generating comparison questions and bridge questions are described in Algorithm 1
andAlgorithm2,respectively.
A.7 Post-processGeneratedData
For the bridge questions, we created the data from the two triples (e,r ,e ) and (e ,r ,e ). When we
1 1 1 2 2
have another triple (e,r ,e ) that has the same entity and the property with the first triple, it becomes
1 1∗
an ambiguous case. Hence, we discarded all such cases in our dataset based on the information from
Wikidata.
For the comparison questions, when a question is asked for comparing two entities about numerical
valuesandthevaluesofthetwoentitiesareequal,weremoveit.

Algorithm1:ComparisonQuestionGenerationProcedure
Input: Setofalltemplates,allentitiesinthesamegroup,WikipediaandWikidatainformation
foreachentity
Output: Aquestion–answerpairwiththeseinformation: questionQ,answerA,contextC,
sentence-levelSFsSF,andevidencesE
whilenotfinisheddo
1
Randomlychoosetwoentitiese ande ;
2 1 2
Obtainalltriples(relationsandobjects)ofeachentityfromWikidata;
3
Obtainasetofmutualrelations(M)betweentwoentities;
4
ObtainWikipediainformationofeachentity;
5
foreachrelationinM do
6
ifpassrequirementsthen
7
Chooseatemplaterandomly;
8
GenerateaquestionQ;
9
ObtainacontextC;
10
ObtainanevidenceE;
11
ComputeananswerA;
12
Computesentence-levelSFsSF;
13
end
14
end
15
end
16
Algorithm2:BridgeQuestionGenerationProcedure
Input: SetofrelationsR,WikipediaandWikidatainformationforeachentity
Output: Aquestion–answerpairwiththeseinformation: questionQ,answerA,contextC,
sentence-levelSFsSF,evidencesE
whilenotfinisheddo
1
Randomlychooseanentitye;
2
Obtainasetofstatements(relationsandobjects)oftheentityfromWikidata;
3
FilterthesetofstatementsbasedonthefirstrelationinformationinRtoobtainasetof1-hop
4
H ;
1
ForeachelementinH ,dothesameprocess(fromLine3)toobtainasetof2-hopH ,each
5 1 2
elementinH isatuple(e,r ,e ,r ,e );
2 1 1 2 2
foreachtupleinH do
6 2
ObtainWikipediaarticlesfortwoentities: eande ;
7 1
ifpassrequirementsthen
8
Chooseatemplaterandomlybasedonr andr ;
9 1 2
GenerateaquestionQ;
10
ObtainacontextC;
11
ObtainanevidenceE;
12
ObtainananswerA;
13
Computesentence-levelSFsSF;
14
end
15
end
16
end
17
