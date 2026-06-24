MuSiQue: Multihop Questions via Single-hop Question Composition
(cid:15)HarshTrivedi(cid:5) NiranjanBalasubramanian(cid:5) TusharKhot† AshishSabharwal†
(cid:5)StonyBrookUniversity,StonyBrook,U.S.A.
{hjtrivedi,niranjan}@cs.stonybrook.edu
†AllenInstituteforAI,Seattle,U.S.A.
{tushark,ashishs}@allenai.org
|     |     | Abstract |     |     |     | Disconnected Question                |     |     |     | Connected Question                   |     |     |
| --- | --- | -------- | --- | --- | --- | ------------------------------------ | --- | --- | --- | ------------------------------------ | --- | --- |
|     |     |          |     |     |     | Armageddon in Retrospect was written |     |     |     | Armageddon in Retrospect was written |     |     |
|     |     |          |     |     |     | by the author who was best known     |     |     |     | by the author who was best           |     |     |
Multihopreasoningremainsanelusivegoal for what 1969 satire novel?  known for what novel?
asexistingmultihopbenchmarksareknown Q Slaughterhouse-Five Q' Slaughterhouse-Five
to be largely solvable via shortcuts. Can Who's the author of  Who's the author of
2202 yaM 5  ]LC.sc[  3v37500.8012:viXra Armageddon in Retrospect?  Armageddon in Retrospect?
wecreateaquestionanswering(QA)dataset Q1 A1': Kurt Vonnegut Q1' A1: Kurt Vonnegut
that,byconstruction,requirespropermulti-
|     |     |     |     |     |     | What 1969 satire novel was A1'  |     |     |     | What novel was A1 best   |     |     |
| --- | --- | --- | --- | --- | --- | ------------------------------- | --- | --- | --- | ------------------------ | --- | --- |
hopreasoning? Tothisend,weintroducea best known for?  known for?
|           |            |       |                     |     |       | Q2 A2': Slaughterhouse-Five |     |     |     | Q2' A2: Slaughterhouse-Five |     |     |
| --------- | ---------- | ----- | ------------------- | --- | ----- | --------------------------- | --- | --- | --- | --------------------------- | --- | --- |
| bottom-up | approach   |       | that systematically |     | se-   |                             |     |     |     |                             |     |     |
| lects     | composable | pairs | of single-hop       |     | ques- | Context                     |     |     |     |                             |     |     |
Armageddon in Retrospect is ... written by Kurt Vonnegut.
The Book of Satyrlike Adventures is ... written by Gaius Petronius.
tionsthatareconnected,i.e.,whereonerea- Kurt Vonnegut ... most famous for satirical novel Slaughterhouse-Five (1969).
soning step critically relies on information Jaroslav Hašek ... is best known for his novel "The Good Soldier Švejk".
Harper Lee ... is best known for her novel "To Kill a Mockingbird"
| from  | another. | This      | bottom-up | methodol- |         |           |                                        |        |     |          |            |       |
| ----- | -------- | --------- | --------- | --------- | ------- | --------- | -------------------------------------- | ------ | --- | -------- | ---------- | ----- |
| ogy   | lets us  | explore   | a vast    | space of  | ques-   |           |                                        |        |     |          |            |       |
|       |          |           |           |           |         | Figure1:  | Generatingconnectedmultihopquestionsby |        |     |          |            |       |
| tions | and add  | stringent | filters   | as        | well as |           |                                        |        |     |          |            |       |
|       |          |           |           |           |         | composing | carefully                              | chosen |     | pairs of | single-hop | ques- |
other mechanisms targeting connected rea- tions. Left: A HotpotQA question that would have
soning.Itprovidesfine-grainedcontrolover
|                  |           |         |            |                |        | been filtered | out        | by  | our approach |             | for not   | requiring  |
| ---------------- | --------- | ------- | ---------- | -------------- | ------ | ------------- | ---------- | --- | ------------ | ----------- | --------- | ---------- |
| the construction |           | process | and        | the properties |        |               |            |     |              |             |           |            |
|                  |           |         |            |                |        | connected     | reasoning; |     | it can       | be answered |           | using just |
| of the           | resulting | k-hop   | questions. |                | We use |               |            |     |              |             |           |            |
|                  |           |         |            |                |        | Q2 without    | knowing    |     | the answer   | to          | Q1 (since | there is   |
| this methodology |           | to      | create     | MuSiQue-Ans,   |        |               |            |     |              |             |           |            |
onlyonepersonmentionedinthecontextasbeingbest
a new multihop QA dataset with 25K 2-4 knownforasatiricalnovel). Right: Aconnectedques-
| hopquestions. |     | Relativetoexistingdatasets, |     |     |     |     |     |     |     |     |     |     |
| ------------- | --- | --------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
tionthatforcesmodelstoreasonthroughbothintended
| MuSiQue-Ans |     | is more | difficult | overall | (3x |     |     |     |     |     |     |     |
| ----------- | --- | ------- | --------- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
hops(sincetherearemultiplepeoplementionedinthe
increaseinhuman-machinegap),andharder
contextasbeingbestknownforsomenovel).
| to cheat | via | disconnected | reasoning |     | (e.g., a |     |     |     |     |     |     |     |
| -------- | --- | ------------ | --------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
single-hopmodelhasa30pointdropinF1).
Wefurtheraddunanswerablecontrastques-
|               |            |     |                |          |          | and obtain   | high | scores | (Min    | et      | al., 2019a; | Chen |
| ------------- | ---------- | --- | -------------- | -------- | -------- | ------------ | ---- | ------ | ------- | ------- | ----------- | ---- |
| tions         | to produce | a   | more stringent |          | dataset, |              |      |        |         |         |             |      |
|               |            |     |                |          |          | and Durrett, |      | 2019;  | Trivedi | et al., | 2020).      | Such |
| MuSiQue-Full. |            | We  | hope our       | datasets | will     |              |      |        |         |         |             |      |
help the NLP community develop models shortcutsarisefromvariousfactors,suchasoverly
thatperformgenuinemultihopreasoning.1 specific sub-questions, train-test leakage, and in-
|                |     |     |     |     |     | sufficient                                 | distractors. |         | These   | factors | allow | mod-     |
| -------------- | --- | --- | --- | --- | --- | ------------------------------------------ | ------------ | ------- | ------- | ------- | ----- | -------- |
| 1 Introduction |     |     |     |     |     | elstocircumventconnectedreasoning—theyneed |              |         |         |         |       |          |
|                |     |     |     |     |     | not read                                   | the          | context | to find | answers | to    | previous |
MultihopQAdatasetsaredesignedtosupportthe
sub-question(s)orusetheseanswerstoanswerthe
| development | and | evaluation | of  | models | that per- |     |     |     |     |     |     |     |
| ----------- | --- | ---------- | --- | ------ | --------- | --- | --- | --- | --- | --- | --- | --- |
latersub-questionsthatdependonthem.
| form multiple    | steps       | of        | reasoning | in order | to an-     |            |           |          |     |           |             |         |
| ---------------- | ----------- | --------- | --------- | -------- | ---------- | ---------- | --------- | -------- | --- | --------- | ----------- | ------- |
|                  |             |           |           |          |            | The        | left hand | side     | of  | Fig. 1    | illustrates | an in-  |
| swer a question. |             | Recent    | work,     | however, | shows      |            |           |          |     |           |             |         |
|                  |             |           |           |          |            | stance     | of this   | problem  | in  | an actual | question    | (Q)     |
| that on existing |             | datasets, | models    | often    | need not   |            |           |          |     |           |             |         |
|                  |             |           |           |          |            | taken from | the       | HotpotQA |     | dataset   | (Yang       | et al., |
| even connect     | information |           | across    | all      | supporting |            |           |          |     |           |             |         |
2018). Thisquestionhastheover-specificationis-
| facts,2 because |     | they can | exploit | reasoning | short- |     |     |     |     |     |     |     |
| --------------- | --- | -------- | ------- | --------- | ------ | --- | --- | --- | --- | --- | --- | --- |
sue. Atfirstglance,itappearstorequireamodelto
cutsandotherartifactstofindthecorrectanswers
|       |     |     |     |                 |     | identify | Kurt | Vonnegut | as  | the author | of  | Armaged- |
| ----- | --- | --- | --- | --------------- | --- | -------- | ---- | -------- | --- | ---------- | --- | -------- |
| 1Code |     |     |     | https://github. |     |          |      |          |     |            |     |          |
and datasets available at doninRetrospect,andthenusethisinformationto
com/stonybrooknlp/musique.
|     |     |     |     |     |     | answer | the final | question |     | about | the famous | satire |
| --- | --- | --- | --- | --- | --- | ------ | --------- | -------- | --- | ----- | ---------- | ------ |
2Forexample,theyoftendon’tevenuseinformationfrom
onesupportingfacttoselectanother. novel he authored. However, this framing of the

questionisinsufficienttoenforcethatmodelsmust demonstrate that -Ans is more challenging and
performconnectedmultihopreasoningtoarriveat less cheatable tha(cid:15)n two prior multihop reasoning
the correct answer. A model can, in fact, find the datasets,HotpotQA(Yangetal.,2018)and2Wiki-
correct answer to this question from the context MultihopQA (Ho et al., 2020). In particular, it
withoutfindingtheanswertoQ1. Thisisbecause, has 3x the human-machine gap, and a substan-
even if a model does not know that A1 refers to tially lower disconnected reasoning (DiRe) score
Kurt Vonnegut, there happens to be only one per- whichcapturestheextenttowhichadatasetcanbe
son best known for a satirical novel mentioned in cheatedviadisconnectedreasoning(Trivedietal.,
thecontext. 2020). We also show how various features of our
Contrastthiswiththequestionontheright(Q’), datasetconstructionpipelinehelpincreasedataset
which cannot be answered by simply returning a difficulty and reduce cheatability. Lastly, by in-
novelthatsomeonewasbestknownfor. Thereare corporatingthenotionofinsufficientcontext(Ra-
threepossibleanswersinthecontextandchoosing jpurkar et al., 2018; Trivedi et al., 2020), we also
between them requires knowing which author is release a variant of our dataset, -Full, having
referenced. This is a desirable multihop question ∼50Kmultihopquestionswhichf(cid:15)ormcontrasting
thatrequiresconnectedreasoning. pairs(Kaushiketal.,2019;Gardneretal.,2020)of
answerable and unanswerable questions. -Full
Prior work has characterized such reasoning,
where a model arrives at the correct answer
isevenmorechallengingandhardertoche(cid:15)aton.
We hope our bottom-up multihop dataset
without using all supporting facts, as Discon-
construction methodology and our challenging
nected Reasoning (Trivedi et al., 2020). While
datasets with a mixed number of hops will help
thischaracterizationenablesfilteringorautomati-
develop proper multihop reasoning systems and
callytransformingexistingdatasets(Trivedietal.,
decomposition-basedmodels.
2020), we ask a different question: How can we
construct a new multihop dataset that, by design,
2 RelatedWork
enforcesconnectedreasoning?
Wemaketwomaincontributionstowardsthis: Multihop QA. -Ans is closest to HotpotQA
1) A new dataset construction approach:
(Yang et al., 2018(cid:15)) and 2WikiMultihopQA (Ho
et al., 2020). HotpotQA was constructed by
We introduce a bottom-up process for build-
directly crowdsourcing 2-hop questions without
ing challenging multihop reading comprehension
considering the difficulty of composition and has
QA datasets by carefully selecting and compos-
been shown to be largely solvable without multi-
ing single-hop questions obtained from existing
hop reasoning (Min et al., 2019a; Chen and Dur-
datasets. The key ideas behind our approach are:
rett, 2019; Trivedi et al., 2020). While 2Wiki-
(i) Composing multihop questions from a large
MultihopQA was also constructed via composi-
collection of single-hop questions, which allows
tion,theyusealimitedsetofhand-authoredcom-
a systematic exploration of a vast space of candi-
positionalrules,makingiteasyforlargelanguage
date multihopquestions. (ii)Applying a stringent
models. We show that -Ans is harder and less
setoffiltersthatensurenosub-questioncanbean-
sweredwithoutfindingtheanswertotheprevious
cheatable than both of(cid:15)these. Other multihop
datasets (Khashabi et al., 2018; Dua et al., 2019,
sub-questions it is connected to (a key property
inter alia) focus on different challenges such as
weformallydefineaspartoftheMuSiQuecondi-
multiple modalitites (Chen et al., 2020; Talmor
tion,Eqn.(2)). (iii)Reducingtrain-testleakageat
etal.,2021),open-domainQA(Gevaetal.,2021;
thelevelofeachsingle-hopquestion,therebymit-
Khot et al., 2020), fact verification (Jiang et al.,
igating the impact of simple memorization tricks.
2020), science explanations (Jansen et al., 2018),
(iv)Addingdistractorcontextsthatcannotbeeas-
andrelationextraction(Welbletal.,2018),among
ilyidentified. (v)Creatingunanswerablemultihop
others. Extending our ideas to these challenges is
questionsatthesub-questionlevel.
aninterestingavenueforfuturework.
2) A new challenge dataset and empiri-
cal analysis: We build a new multihop QA Unanswerable QA. Prior works have used
dataset, MuSiQue-Ans (abbreviated as -Ans), unanswerable questions for robust reasoning in
with ∼25K 2-4 hop questions with six(cid:15)differ- single-hop (Rajpurkar et al., 2018) and multi-
ent composition structures (cf. Table 1). We hop (Ferguson et al., 2020; Trivedi et al., 2020)

settings. IIRC (Ferguson et al., 2020) focuses on simplicity, we assume these probabilities are in-
open-domain QA where the unanswerable ques- dependent across various q . M can correctly an-
i
tions are identified by crowdsourcing questions swer a k-hop question Q by identifying and per-
where relevant knowledge couldn’t be retrieved forming all its k reasoning steps. This will suc-
from Wikipedia. Our idea to make unanswerable ceedwithprobabilityatmostpk. Alternatively,as
multihop questions by removing support para- anextremecase,itcan“cheat”byidentifyingand
graphs is most similar to Trivedi et al. (2020). performing only the last step q (the “end ques-
k
Whiletheyrelyonannotations(potentiallyincom- tion”) without considering the output of q (or
k−1
plete)toidentifythesesupportparagraphs,wecan othersteps)atall. Thiscouldsucceedwithproba-
usethebridgeentitiestoremoveanypotentialsup- bility as much as r, whichdoes not decrease with
portparagraphs(containingthebridgeentity)and kandisthusundesirablewhenconstructingmulti-
betterensureunanswerability. hopdatasets. Ourgoalistocreatemultihopques-
tionsthatenforceconnectedreasoning,i.e.,where
| Question | Decomposition |     |     | and | Composition. |     |              |                     |     |     |       |         |        |
| -------- | ------------- | --- | --- | --- | ------------ | --- | ------------ | ------------------- | --- | --- | ----- | ------- | ------ |
|          |               |     |     |     |              |     | r (cid:28) p | and, in particular, |     | r   | < pk, | so that | models |
MultihopQAdatasetshavebeendecomposedinto
haveanincentivetoperformallkreasoningsteps.
| simpler        | questions | (Min    | et      | al., 2019b; | Talmor      | and      |     |     |     |     |     |     |     |
| -------------- | --------- | ------- | ------- | ----------- | ----------- | -------- | --- | --- | --- | --- | --- | --- | --- |
| Berant,        | 2018)     | and     | special | meaning     | representa- |          |     |     |     |     |     |     |     |
| tions (Wolfson |           | et al., | 2020).  | Our         | dataset     | creation |     |     |     |     |     |     |     |
Notsurprisingly,theconnectedreasoningprop-
| pipeline | naturally | provides |     | question | decomposi- |     |     |     |     |     |     |     |     |
| -------- | --------- | -------- | --- | -------- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
ertyisoftennotsatisfiedbyexistingdatasets(Min
| tions, which |     | can can | help | develop | interpretable |     |         |             |     |              |     |       |         |
| ------------ | --- | ------- | ---- | ------- | ------------- | --- | ------- | ----------- | --- | ------------ | --- | ----- | ------- |
|              |     |         |      |         |               |     | et al., | 2019a; Chen |     | and Durrett, |     | 2019; | Trivedi |
models(Minetal.,2019b;Khotetal.,2021).
|          |           |          |      |           |           |         | et al., | 2020),        | and never | optimized |              | for | during |
| -------- | --------- | -------- | ---- | --------- | --------- | ------- | ------- | ------------- | --------- | --------- | ------------ | --- | ------ |
| Recent   | work      | has      | also | used      | bottom-up | ap-     |         |               |           |           |              |     |        |
|          |           |          |      |           |           |         | dataset | construction. |           | As a      | consequence, |     | models |
| proaches | to create | multihop |      | questions | (Pan      | et al., |         |               |           |           |              |     |        |
areabletoexploitartifactsinexistingdatasetsthat
| 2021; Yoran   |     | et al., 2021) |         | using | rule-based | meth-     |            |            |     |      |        |       |         |
| ------------- | --- | ------------- | ------- | ----- | ---------- | --------- | ---------- | ---------- | --- | ---- | ------ | ----- | ------- |
|               |     |               |         |       |            |           | allow them | to achieve |     | high | scores | while | bypass- |
| ods. However, |     | their         | primary | goal  | was        | data aug- |            |            |     |      |        |       |         |
ingsomeofthereasoningsteps,thusnegatingthe
| mentation     | to  | improve    | on  | downstream |      | datasets. |                                        |     |            |     |           |     |         |
| ------------- | --- | ---------- | --- | ---------- | ---- | --------- | -------------------------------------- | --- | ---------- | --- | --------- | --- | ------- |
|               |     |            |     |            |      |           | mainpurposeofbuildingmultihopdatasets. |     |            |     |           |     | Prior   |
| The questions |     | themselves |     | haven’t    | been | shown to  |                                        |     |            |     |           |     |         |
|               |     |            |     |            |      |           | work (Trivedi                          | et  | al., 2020) | has | attempted |     | to mea- |
bechallengingorlesscheatable.
|     |     |     |     |     |     |     | sure the | extent        | of connected |          | reasoning | in     | current |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------------- | ------------ | -------- | --------- | ------ | ------- |
|     |     |     |     |     |     |     | models   | and datasets. |              | However, | due       | to the | design  |
3 MultihopReasoningDesiderata
|     |     |     |     |     |     |     | of existing | datasets, | this | approach |     | is only | able to |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --------- | ---- | -------- | --- | ------- | ------- |
Multihop question answering can be seen as a se- measurethisbyablatingthepre-requisitesofeach
quenceofinter-dependentreasoningstepsleading reasoning step, i.e., the supporting facts. Rather
| totheanswer. |     | Initsmostgeneralform,theserea- |     |     |     |     |           |          |     |         |     |        |         |
| ------------ | --- | ------------------------------ | --- | --- | --- | --- | --------- | -------- | --- | ------- | --- | ------ | ------- |
|              |     |                                |     |     |     |     | than only | measure, | we  | propose | a   | method | to con- |
soning steps and the dependencies can be viewed structmultihopQAdatasetsthatdirectlyoptimize
| as directed | acyclic | graph | (DAG), |     | G . Each | node | forthiscondition. |     |     |     |     |     |     |
| ----------- | ------- | ----- | ------ | --- | -------- | ---- | ----------------- | --- | --- | --- | --- | --- | --- |
Q
q
| i in this | graph | represents |     | a reasoning |     | step or a |     |     |     |     |     |     |     |
| --------- | ----- | ---------- | --- | ----------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
“hop”,e.g.,asingle-hopquestioninmultihopQA
or a KB relation traversal in graph-based KBQA. Consider question Q on the left hand side of
An edge (q j ,q i ) ∈ edges(G Q ) indicates that the Fig.1. Itcanbeansweredintwosteps,Q1andQ2.
reasoning step q relies critically on the output of However,theinformationinQ2itselfissufficient
i
the predecessor step q . For example, in Fig. 1, to uniquely identify A2 from the context, even
j
Q2(cid:48)
the single-hop question depends on the an- withoutconsideringA1. Thatis,whilethereisan
swer to Q1(cid:48), and the graph G is a linear chain intendeddependencybetweenQ1andQ2,Q2can
Q(cid:48)
Q1(cid:48) → Q2(cid:48). be answered correctly without requiring the out-
Giventhisframing,akeydesirablepropertyfor put of its predecessor question Q1. Our approach
multihop reasoning isconnected reasoning: Per- constructs multihop questions that prevent this is-
forming each step q correctly should require the sue,andtherebyrequirethedesiredconnectedrea-
i
outputofallitspredecessorstepsq . soning. Specifically, we carefully choose which
j
AnalyticalIntuition: SupposeamodelM can single-hopquestionstocomposeandwhatcontext
answer each q correctly with probability p, and to use such that each constituent single-hop ques-
i
it can also answer q without the output of all its tion necessitates the answers from one or more
i
| predecessor | steps | with | probability |     | r ≤ | p. For | previousquestions. |     |     |     |     |     |     |
| ----------- | ----- | ---- | ----------- | --- | --- | ------ | ------------------ | --- | --- | --- | --- | --- | --- |

Graph Question Decomposition
Who succeeded the first President of 1.WhowasthefirstPresidentofNamibia?SamNujoma
Namibia?HifikepunyePohamba 2.WhosucceededSamNujoma?HifikepunyePohamba
What currency is used where Billy Giles 1.AtwhatlocationdidBillyGilesdie?Belfast
died?poundsterling 2.WhatpartoftheUKisBelfastlocatedin?NorthernIreland
3.WhatistheunitofcurrencyinNorthernIreland?poundsterling
WhenwasthefirstestablishmentthatMc- 1.WhatisMcDonaldizationnamedafter?McDonald’s
Donaldizationisnamedafter,openinthe 2.WhichstateisHorndeanlocatedin?England
countryHorndeanislocated?1974 3.WhendidthefirstMcDonald’sopeninEngland?1974
WhendidNapoleonoccupythecitywhere 1.WhobroughtLouisXVIstyletothecourt?MarieAntoinette
the mother of the woman who brought 2.Who’smotherofMarieAntoinette?MariaTheresa
LouisXVIstyletothecourtdied?1805 3.InwhatcitydidMariaTheresadie?Vienna
4.WhendidNapoleonoccupyVienna?1805
How many Germans live in the colonial 1.WhatcontinentisArubain?SouthAmerica
holdinginAruba’scontinentthatwasgov- 2.WhatcountryisPrazeres?Portugal
ernedbyPrazeres’scountry?5million 3.ColonialholdinginSouthAmericagovernedbyPortugal?Brazil
4.HowmanyGermansliveinBrazil?5million
When did the people who captured 1.WhatisPhilipsburgcapitalof?SaintMartin
Malakoff come to the region where 2.SaintMartinislocatedonwhatterrainfeature?Caribbean
Philipsburgislocated?1625 3.WhocapturedMalakoff?French
4.WhendidtheFrenchcometotheCaribbean?1625
Table1: Thesixreasoninggraphshapes(2-hopto4-hop)presentinMuSiQue,alongwithsamplequestions.
4 ConnectedReasoningviaComposition This process of composing multihop questions
canbechainedtogethertoformcandidatereason-
The central issue we want to address is ensur-
ing graphs of various shapes and sizes (examples
ing connected reasoning. Our solution is to use a
in Table 1). Formally, each multihop question Q
bottom-up approach where we compose multihop
hasanunderlyingDAGG representingthecom-
Q
questions from a large pool of single-hop ques-
positionofthesingle-hopquestionsq ,q ,...,q ,
1 2 n
tions. As we show later, this approach allows us
which form the nodes of G . A directed edge
Q
toexplorealargespaceofmultihopquestionsand
(q ,q ) indicates that q depends on the answer of
j i i
carefully select ones that require connected rea-
the previous sub-question q . a is the answer to
j i
soning. Additionally, with each multihop ques-
q ,andthereby,a istheanswertoQ.
i n
tion, we will have associated constituent ques-
tions, their answers and supporting paragraphs, 4.2 EnsuringConnectedReasoning
which can help develop more interpretable mod-
Given the graph G associated with a question
Q
els. Here we describe the high-level process and
Q, ensuring connected reasoning requires ensur-
describethespecificsinthenextsection.
ing that for each edge (q ,q ) ∈ edges(G ), ar-
j i Q
4.1 MultihopviaSingle-hopComposition riving at answer a i using q i , necessitates the use
ofa . Inotherwords,withouta ,thereisn’tsuffi-
As mentioned earlier, multihop questions can be j j
cientinformationinq toarriveata .
viewed as a sequence of reasoning steps where i i
The existence of such information can be
answer from one reasoning step is used to iden-
probedbytrainingastrongQAmodelM onsub-
tify the next reasoning step. Therefore, we can
questions (q ) with the mention of their predeces-
usesingle-hopquestionscontaininganswersfrom i
sor’s answer (a ) masked out (removed). If, on
other questions to construct potential multihop j
held out data, the model can identify a subques-
questions. E.g., in Fig. 1, Q2’ mentions A1’, and
tion’sanswer(a )withoutitspredecessor’sanswer
hence single-hop questions Q1’ and Q2’ can be i
(a ),wesaytheedge(q ,q )isdisconnected. For-
composed to create a DAG Q1(cid:48) → Q2(cid:48) and mul- j j i
mally,wesayQrequiresconnectedreasoningif:
tihop question Q’ (right). Concretely, to create a
multihopquestionfromtwosingle-hopquestions, ∀(q ,q ) ∈ edges(G ) : M(q mj) (cid:54)= a (1)
j i Q i i
we have a composability criteria: Two single-
hop question answer tuples (q ,a ) and (q ,a ) where q
mj
denotes the subquestion formed from
1 1 2 2 i
are composable into a multihop question Q with q bymaskingoutthementionoftheanswera .
i j
a as a valid answer if a is a named entity and it Consider the masked questions Q2 and Q2’ in
2 1
ismentionedinq . See§5:S2fordetailedcriteria. Fig. 1. While Q2 can easily be answered without
2

answer A1, Q2’ can’t be answered without A1’ questions can compound into an intolerably large
andQ’hencesatisfiescondition(1). percentage in the composed multihop questions.
Tomitigatethis,wefirstremovequestionsthatare
4.3 ReadingComprehensionSetting
likely annotation errors. Since manually identify-
Whileourproposedframeworkmakesnoassump- ing such questions at scale is laborious, we use a
tionsaboutthechoiceofthemodel,andisapplica- model-based approach. We remove the questions
bletoopen-domainsetting,wefocusontheRead- for which none of five large trained QA models3
ing Comprehension (RC) setting, where we’ve a can predict the associated answer with > 0 an-
fixedsetofparagraphsascontext,C. swer F1. Furthermore, we remove (i) erroneous
InaRCsetting,apartfromrequiringthedepen- questions where the answer spans are not in the
dence between the reasoning steps, we also want context, (ii) questions with < 20 word context as
themodeltodependonthecontexttoanswereach we found them to be too easy, and (iii) questions
question. While this requirement seems unneces- with>300wordcontexttopreventfinalmultihop
sary,previousworkshaveshownthatRCdatasets question context from being too long for current
oftenhaveartifactsthatallowmodelstopredictthe long-rangetransformermodels.
answer without the context (Kaushik and Lipton,
S2. Find Composable Single-hop Pairs. To
2018)andcanevenmemorizetheanswers(Lewis
create 2-hop questions, we first collect distinct
et al., 2021) due to train-test leakage. As we will
single-hop question pairs with a bridge entity.
show later, previous multihop RC datasets can be
Specifically,wefindpairs(q ,p ,a )and(q ,p ,
cheated via such shortcuts. To ensure the depen- 1 1 1 2 2
a ) such that (i) a is a named entity also men-
dencebetweenthequestionandcontext,wemod- 2 1
tioned in q , (ii) a is not in q , and (iii) p (cid:54)= p .
ifytherequiredconditioninEqn.(1)to: 2 2 1 1 2
Suchpairscanbecombinedtoforma2-hopques-
∀(q
j
,q
i
) ∈ edges(G
Q
) : M(q
i
mj;C) (cid:54)= a
i
tion (Q, {p
1
, p
2
}, a
2
). To ensure the mentions
(a and its occurrence in q denoted e ) refer to
∧ ∀q ∈ nodes(G ) : M(q ;φ) (cid:54)= a (2) 1 2 2
i Q i i
the same entity, we ensure: 1. Spacy entity tag-
In summary, we want multihop reading com- ger (Honnibal et al., 2020) tags a 1 and e 2 as en-
prehensionquestionsthatsatisfycondition(2)for tities of the same type. 2. A Wikipedia search
a strong trained model M. If it does, we say with a 1 and e 2 returns identical 1st result. 3. A
that the question satisfies the MuSiQue condi- SOTA Wikification model (Wu et al., 2020) re-
tion. Our dataset construction pipeline optimizes turnsthesameresultfora 1 ande 2 . Atalaterstep
forthisconditionasdescribednext. (S7)whenhumanswritecomposedquestionsfrom
DAGs,theygettoremovequestionscontaininger-
5 DatasetConstructionPipeline roneouspairs. Only8%ofthepairsareprunedin
thatstep,indicatingthatstepS2isquiteeffective.
Thehigh-levelschematicofthepipelineisshown
in Fig. 2. We begin with a large set of RC single-
S3. Filter Disconnected Single-hop Pairs. We
hop questions from 5 English Wikipedia-based
want connected 2-hop questions – questions that
datasets,SQuAD(Rajpurkaretal.,2016),Natural
cannot be answered without using the answers
Questions(Kwiatkowskietal.,2019),MLQA(en-
of the constituent single-hop questions. The
en) (Lewis et al., 2020b), T-REx (ElSahar et al.,
MuSiQue condition (2) states that for a 2-hop
2018), Zero Shot RE (Levy et al., 2017), where
question to be connected, either sub-question q
i
instances are of the form (q ,p ,a ) referring to
i i i should not be correctly answered without its con-
thequestion,theassociatedparagraph,andthean-
text (M(q ,φ) (cid:54)= a ) and the tail question q
i i 2
swer, respectively. For Natural Questions, as the
should not be correctly answered when a is re-
1
context is very long (entire Wikipedia page), we moved from it (M(qm1,C) (cid:54)= a ). Accordingly
2 2
use the annotated long answer (usually a para-
we use a two step filtering process to find con-
graph)fromthedatasetasthecontext,andthean-
nected 2-hop questions. For simplicity, and be-
notatedshortanswerastheanswer. Then,wetake
causethesecondconditionalreadyfilterssometail
thefollowingtwosteps:
3Tworandom-seedvariantsofRoBERTa-large(Liuetal.,
S1. Find Good Single-hop Questions. Even a
2019), two random-seeds of Longformer-Large (Beltagy
tolerably small percentage of issues in single-hop etal.,2020)andoneUnifiedQA(Khashabietal.,2020).

|     |     |     | 2017K 1-Hop Qns |     |     | 760K 1-Hop Qns |       | 12M 2-Hop Qns |     |             | 3.2M 2-Hop Qns |     |     |
| --- | --- | --- | --------------- | --- | --- | -------------- | ----- | ------------- | --- | ----------- | -------------- | --- | --- |
|     |     |     |                 |     |     |                | Find  |               |     | Filter out  |                |     |     |
Find Good
|          |     |     |     |     | Single-Hop  |     | Composable  |         |     | Disconnected  |            |     |     |
| -------- | --- | --- | --- | --- | ----------- | --- | ----------- | ------- | --- | ------------- | ---------- | --- | --- |
|          |     |     |     |     |             |     | Sin g le    | - H op  |     | Sin g         | le - H op  |     |     |
| MuSiQue  |     |     |     |     | Questions   |     | P a ir      | s       |     |               |            |     |     |
|          |     |     |     |     |             |     |             |         |     | P             | a ir s     |     |     |
(♫)
|     |     |     |     |     | 1   |     | Te2xt |     |     |     | 3   |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- |
Pipeline
|     |     |     | All Single-Hop  |     |     | Good Single-Hop  |     | Composable       |     |     |                  | Connected   | 4   |
| --- | --- | --- | --------------- | --- | --- | ---------------- | --- | ---------------- | --- | --- | ---------------- | ----------- | --- |
|     |     |     | Questions       |     |     | Questions        |     | 2-Hop Questions  |     |     | 2-Hop Questions  |             |     |
Build
Multihop
50K 2-4 Hop Qns 25K 2-4 Hop Qns 25K 2-4 Hop Qns 27K 2-4 Hop Qns 78K 2-4 Hop Qns Questions
|     |             | Add Un- |     |     | Build         |     | Crowdsource  |     |     | Minimize    |     |     |     |
| --- | ----------- | ------- | --- | --- | ------------- | --- | ------------ | --- | --- | ----------- | --- | --- | --- |
|     | answerable  |         |     |     | Contexts for  |     | Question     |     |     | Train-Test  |     |     |     |
sufficient
|               |     | Questions  |              |          | Questions  |     | Compositions  |     | Train | Leakage  |     |     |     |
| ------------- | --- | ---------- | ------------ | -------- | ---------- | --- | ------------- | --- | ----- | -------- | --- | --- | --- |
|               |     | 8          |              | Positive | 7          |     | 6             |     |       |          | 5   |     |     |
| insufficient  |     |            | Distractors  |          |            |     |               |     |       |          |     |     |     |
Dev Test
|     |     |     |     |     |     | Composed |     | Reduced Train- |     |     |     | Multi (2-4)   |     |
| --- | --- | --- | --- | --- | --- | -------- | --- | -------------- | --- | --- | --- | ------------- | --- |
MuSiQue-Full MuSiQue-Ans Questions  Test Leakage  Hop Questions
Figure 2: MuSiQue construction pipeline. MuSiQue pipline takes single-hop questions from existing datasets,
explores the space of multihop questions that can be composed from them, and generates dataset of challenging
multihopquestionsthataredifficulttocheaton. MuSiQuepipelinealsomakesunanswerablemultihopquestions
thatmakesthefinaldatasetsignificantlymorechallenging.
questions, our current implementation enforces swer semantically match the correct answer (e.g.,
thefirstconditiononlyontheheadquestion,q . "Barack Obama" and "President Barack Obama"
1
FilteringHeadNodes: Wecollectallquestions overlap with 0.8 answer F1). Controlling these
that appear at least once as the head of compos- thresholdsprovidesawaytotrade-offbetweenthe
(q
able 2-hop questions 1 ) to create a set of head degree of cheatability allowed in the dataset and
nodes. We create 5-fold train-test splits of this thesizeofthefinaldataset. Weaimtolimitcheata-
set and train two Longformer-Large models (dif- bilitywhileretainingareasonabledatasetsize.
ferentseeds)persplit(trainonthree, validateand Finally, only 2-hop questions for which both
test on one). We generate answer predictions us- headandtailnodeareacceptablearekept. Wecall
ingthe2modelsontheircorrespondingtestsplits thisprocessDisconnectionFiltering.
| resultingin2predictionsperquestion. |          |     |             |     |               | Weaccept |     |                         |     |     |     |            |     |
| ----------------------------------- | -------- | --- | ----------- | --- | ------------- | -------- | --- | ----------------------- | --- | --- | --- | ---------- | --- |
|                                     |          |     |             |     |               |          | S4. | BuildMultihopQuestions. |     |     |     | Wenowhavea |     |
| a head                              | question | if, | on average, |     | the predicted | an-      |     |                         |     |     |     |            |     |
swers’ word overlap (computed using answer f1) set of connected 2-hop questions, which form di-
|     |     |     |     |     |     |     | rectededgesofagraph. |     |     |     | AnysubsetDAGofitcan |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | --- | ------------------- | --- | --- |
withtheanswerlabelis<0.5.
|           |      |        |     |           |     |            | be used | to  | create | a connected |     | multihop | question. |
| --------- | ---- | ------ | --- | --------- | --- | ---------- | ------- | --- | ------ | ----------- | --- | -------- | --------- |
| Filtering | Tail | Nodes: |     | We create | a   | unique set |         |     |        |             |     |          |           |
of masked single-hop questions that occur as a Weuse6typesofreasoninggraphswith2-4hops
|           |      |        |            |     |       |           | asshowninTable |     |     | 1. Toavoidverylongquestions, |     |     |     |
| --------- | ---- | ------ | ---------- | --- | ----- | --------- | -------------- | --- | --- | ---------------------------- | --- | --- | --- |
| tail node | (q ) | in any | composable |     | 2-hop | question. |                |     |     |                              |     |     |     |
2
|             |            |     |          |     |        |           | we limit | single-hop |     | questions |     | to ≤ 10 | tokens, the |
| ----------- | ---------- | --- | -------- | --- | ------ | --------- | -------- | ---------- | --- | --------- | --- | ------- | ----------- |
| If the same | single-hop |     | question |     | occurs | in two 2- |          |            |     |           |     |         |             |
hopquestionswithdifferentmaskedentities, they total length of questions in 2,3-hops to ≤ 15, and
|          |       |        |      |            |     |           | 3-hops  | to  | ≤ 20  | tokens.     | To ensure | diversity, | we          |
| -------- | ----- | ------ | ---- | ---------- | --- | --------- | ------- | --- | ----- | ----------- | --------- | ---------- | ----------- |
| both are | added | to the | set. | We combine |     | the gold- |         |     |       |             |           |            |             |
|          |       |        |      |            |     |           | (1) cap | the | reuse | of bridging |           | entities   | and single- |
paragraphwith9distractorparagraphs(retrieved4
|           |          |     |         |            |     |             | hop | questions | at  | 25 and | 100 | multihop | questions |
| --------- | -------- | --- | ------- | ---------- | --- | ----------- | --- | --------- | --- | ------ | --- | -------- | --------- |
| using the | question |     | without | the masked |     | entities as |     |           |     |        |     |          |           |
query). Asbefore,wecreate5-foldtrain-testsplits respectively (2) remove any n-hop question that’s
subsetofanym-hopquestion(m>n>1).
| and use  | 2 Longformer-Large |              |        | models | to        | get 2 an-   |                                |     |     |     |     |           |     |
| -------- | ------------------ | ------------ | ------ | ------ | --------- | ----------- | ------------------------------ | --- | --- | --- | --- | --------- | --- |
| swer and | support            | predictions. |        |        | We accept | a tail      |                                |     |     |     |     |           |     |
|          |                    |              |        |        |           |             | S5. MinimizeTrain-TestLeakage. |     |     |     |     | Wedevisea |     |
| question | if either          | mean         | answer |        | F1 ≤      | 0.25, or if |                                |     |     |     |     |           |     |
proceduretocreatetrain,validationandtestsplits
| it’s≤ 0.75andmeansupportF1< |            |     |      |     | 1.0.      |           |              |             |         |        |               |             |     |
| --------------------------- | ---------- | --- | ---- | --- | --------- | --------- | ------------ | ----------- | ------- | ------ | ------------- | ----------- | --- |
|                             |            |     |      |     |           |           | such         | that models |         | cannot | achieve       | high-scores | via |
| The                         | thresholds | for | head | and | tail node | filtering |              |             |         |        |               |             |     |
|                             |            |     |      |     |           |           | memorization |             | enabled |        | by train-test | leakage,    | an  |
werechosenviaamanualinspectionofafewpre-
|          |            |     |        |        |             |     | issue        | observed | in                               | some | existing        | datasets | (Lewis      |
| -------- | ---------- | --- | ------ | ------ | ----------- | --- | ------------ | -------- | -------------------------------- | ---- | --------------- | -------- | ----------- |
| dictions | in various |     | ranges | of the | parameters, | and |              |          |                                  |      |                 |          |             |
|          |            |     |        |        |             |     | etal.,2021). |          | Ourprocedureensuresthatthetrain- |      |                 |          |             |
| gauging  | at what    | F1  | values | does   | the model’s | an- |              |          |                                  |      |                 |          |             |
|          |            |     |        |        |             |     | ing          | set has  | no overlap                       |      | with validation |          | or the test |
4WeusetheBM25algorithmviaElasticsearch. sets,andtriestokeeptheoverlapbetweenvalida-

tionandtestsetsminimal. 2-hop 3-hop 4-hop Total(24,814)
WeconsidertwomultihopquestionsQ andQ
i j Train 14376 4387 1175 19938
to overlap if any of the following are common
Dev 1252 760 405 2417
between Q i and Q j : (i) single-hop question (ii) Test 1271 763 425 2459
answer to any single-hop question (iii) associated
paragraph to any single-hop question. To mini- Table2:DatasetstatisticsofMuSiQue-Ans.MuSiQue-
mizesuchoverlap,wetakeasetofmultihopques- Fullcontainstwicethenumberofquestionsineachcat-
egoryabove–oneanswerableandoneunanswerable.
tions,greedilyfindasubsetofgivensize(S)which
least overlaps with its complement (S’), and then
removeoverlappingquestionsfromS’,togettrain
tioned task on 20 examples each. We manually
(S) and dev+test set (S’). Then, we split dev+test
evaluatedtheseannotationsforcorrectnessandco-
to dev and test similarly. We ensure the distribu-
herence, and selected 17 workers to annotate the
tion of source datasets of single-hop questions in
full dataset. To ensure dataset quality, we car-
train,devandtestaresimilar,andalsocontrolthe
ried out crowdsourcing in 9 batches, reading 10-
proportionof2-4hopquestions.
20 random examples from each worker after each
batch and sending relevant feedback via email, if
S6. Build Contexts for Questions. For an n-
needed. Workers were paid 25, 40, and 60 cents
hop question, the context has 20 paragraphs con-
for each 2, 3, and 4 hop question, amounting to
taining: (i)supporting paragraphsassociatedwith
∼15USDperhour,totaling∼11KUSD.
its single-hop questions {p , p ... p }, (ii) dis-
1 2 n
We refer to the dataset at this stage as
tractorparagraphsretrievedusingaquerythatisa
MuSiQue-Ansor -Ans.
concatenationofsingle-hopquestionsfromwhich
allintermediateanswermentionsareremoved. To (cid:15)
S8. Add Unanswerable Questions. For each
make distractor paragraphs harder to identify, we
answerablemultihopRCinstancewecreateacor-
retrieve them from the set of gold-paragraphs for
responding unanswerable multihop RC instance
thefilteredsingle-hopquestion(S1).
using the procedure similar to the one proposed
in (Trivedi et al., 2020). For a multihop question
S7. CrowdsourceQuestionCompositions. We
werandomlysampleanyofitssingle-hopquestion
crowdsource question compositions on Amazon
andmakeitunanswerablebyensuringtheanswer
MTurk, where workers composed coherent ques-
to that single-hop question doesn’t appear in any
tionsfromourfinalDAGsofsingle-hopquestions.
of the paragraphs in context (except this require-
In the interface (Fig. 3), workers could see a list
ment,thecontextisbuiltasdescribedinS6). Since
ofsingle-hopquestionswiththeirassociatedpara-
one of the single-hop questions is unanswerable,
graphsandhowtheyareconnectedviabridgeen-
thewholemultihopquestionisunanswerable.
tities. They were first asked to check whether all
pairsofmentionsofbridgeentitiesindeedreferto Thetasknowistopredictwhetherthequestion
thesameunderlyingentity. Iftheyanswered‘yes’ isanswerable,andpredicttheanswerandsupport
for each pair,5 they were asked to compose a nat- ifit’sanswerable. Giventhequestionsforanswer-
ural language question ensuring that information able and unanswerable pair are identical and the
from all single-hop questions in the DAG is used, context marginally changes, models that rely on
and the answer to the composed question is the shortcutsfindthisnewtaskverydifficult. Wecall
same as the last single-hop question. If they an- thedatasetatthisstageMuSiQue-Fullor -Full,
swered‘no’foranyofthepairs,wediscardedthat andbothdatasetstogetherasMuSiQue. (cid:15)
question. Our tutorial provided them with several
Final Dataset. The statistics for -Ans ( -
handwrittengoodandbadexamplesforeachofthe
Full has twice the number of questi(cid:15)ons in ea(cid:15)ch
2-4 hop compositions. Workers were encouraged
cell) are shown in Table 2. MuSiQue constitutes
to write short questions and make implicit infer-
unique21020single-hopquestions,4132answers
ences when possible. They were allowed to split
to multihop questions, 19841 answers to single-
questionsintotwosentencesifneeded.
hop questions, and 7676 supporting paragraphs.
We carried out a qualification round where 100
MuSiQuehas6typesofreasoninggraphsand2-4
workers participated to perform the aforemen-
hops(cf.Table1forexamples).
5Theyansweredyes92%ofthetime,onaverage.

In summary, our construction pipeline allows Human Score UB Agr
ustoproduceadatasetwithmixedhops, multiple
AnswerF1 78.0 88.6 84.1
typesofreasoninggraphs,andunanswerablesub-
SupportF1 93.9 97.3 91.4
questions,allofwhichmakeforamorechalleng-
ingandlesscheatabledataset(aswewillquantify Table3: Humanperformance(scoreandupperbound)
inSection8). Questiondecomposition,whichisa andagreementonMuSiQue-Ans.
natural outcome of our construction pipeline, can
also be used to aid decomposition-based QA re-
mancewithtwoothersimilardatasets(HotpotQA
search(Minetal.,2019b;Khotetal.,2021).
and 2WikiMultihopQA), and show that -Ans is
6 DatasetQualityAssessment closetothemunderthesemetrics(§8). (cid:15)
Quality of -Ans. To assess the quality of - Quality of -Full. We perform an additional
Ans, we fir(cid:15)st evaluate how well humans can (cid:15)an- manual valid(cid:15)ation to assess dataset quality of -
swer questions in it. Note that we already have Full. Recall that -Full shares the answera(cid:15)ble
goldanswersandsupportingparagraphsfromour questions with (cid:15)-Ans, the only extra task in
constructionpipeline. Thisgoalisthereforenotto -Full being de(cid:15)termining the answerability of a
determine gold labels, but rather to measure how (cid:15)questionfromthegivencontext. Toassesstheva-
wellhumansperformonthetasktreatingourgold lidityofthistask,wesampled50randominstances
labelsascorrect. from -Full, and one of the authors determined
We sample 125 questions from -Ans valida- the an(cid:15)swerability of each question from its con-
tionandtestsets,andobtain3annot(cid:15)ations(answer text. We found that in 45 out of the 50 instances
andsupportingparagraphs)foreachquestion. We (90%)thehumanpredictedanswerabilitymatched
usedAmazonMechanicalTurk,6 selectingcrowd- thegoldlabel,showingthat -Fullisaalsohigh-
sourceworkersasdescribedin§7.3. qualitydataset. (cid:15)
Workers were shown the question and all para-
Multihop Nature of MuSiQue. Finally, we as-
graphs in the context, and were asked to high-
sess the extent to which -Ans satisfies the
lighttheanswerspanandcheckmarkthesupport-
MuSiQue condition (Eqn. 2(cid:15)) for connected rea-
ing paragraphs. Our interface (Fig. 4) allowed
soning. To this end, we first estimate what per-
forsearching,sorting,andfilteringthelistofpara-
centage of head and tail questions in the valida-
graphs easily with interactive text-overlap-based
tion set would we retain if we were to repeat our
search queries. The instructions included worked
disconnection filtering procedure (S3) with mod-
outexamples.
elstrainedonthefinaltrainingdata. Thiscaptures
We compute human performance by compar-
thefractionofthequestionsin -Ansthatsatisfy
ing against gold labels for answer and support
the MuSiQue condition. We the(cid:15)n compare it with
in two ways: 1) Human Score—the most fre-
therespectivenumbersfromtheoriginalstepS3.
quent answer and support among the three anno-
In the original disconnection filtering step, we
tators breaking ties at random (the strategy used
retainedonly26.5%ofthetailquestions,whereas
byRajpurkaretal.(2018)),and2)HumanUpper
we would have retained 79.0% of the tail ques-
Bound (UB)—the answer and support that maxi-
tions had we filtered the final validation dataset.
mizesthescore(asdonebyYangetal.(2018)).
Forheadquestions,weseealessdramaticbutstill
Furthermore, to assess how well human agree
significant effect—we originally retained 74.5%
witheachother(ignoringourgoldlabels),wealso
questions, and would now have retained 87.7%
computetheHumanAgreement(Agr)score(Ra-
hadwefilteredthefinalvalidationset. Thisshows
jpurkar et al., 2016; Yang et al., 2018). Specifi-
that vastly more questions in -Ans satisfy the
cally, we treat one of 3 annotations, chosen ran-
MuSiQueconditionthanwhatw(cid:15)estartedwith.
domly,aspredicted,andevaluateitagainstrestof
theannotations,whicharetreatedascorrect.
7 ExperimentalSetup
Table 3 demonstrates that -Ans is a high-
quality dataset. Furthermore(cid:15), as we will dis- 7.1 Datasets
cuss in §7.3, we also compare our human perfor-
We compare our datasets (MuSiQue-Ans and
6https://www.mturk.com MuSiQue-Full) with two similar multihop RC

datasets: distractor-setting of HotpotQA (Yang AllenNLP (Gardner et al., 2017). We experi-
et al., 2018) and 2WikiMultihopQA (Ho et al., ment with 2 types of models: (1) Multihop Mod-
2020).7 Both datasets have 10 paragraphs as con- els, which are in principle capable of employing
text. HQ and 2W have 2-hop and 2,4-hop ques- desired reasoning, and have demonstrated com-
tions respectively. Additionally, HQ has sentence petitive performance on previous multihop QA
supportand2Whasentity-relationtuplessupport, datasets. They help probe the extent to which
butwedon’tusethisannotationinourtrainingor a dataset can be solved by current models. (2)
evaluationforafaircomparison. Artifact-based Models, which are restricted in
HQ,2W,and -Anshave90K,167K,and20K some way that prohibits them from doing desired
|          |                    |               |     |     |        |      | reasoning(discussedshortly). |     |     |     | Theyhelpprobethe |     |     |
| -------- | ------------------ | ------------- | --- | --- | ------ | ---- | ---------------------------- | --- | --- | --- | ---------------- | --- | --- |
| training | instance(cid:15)s, | respectively. |     | For | a fair | com- |                              |     |     |     |                  |     |     |
parison,weuseequalsizedtrainingsetsinallour extenttowhichadatasetcanbecheated. Next,we
experiments,obtainedbyrandomlysampling20K describethesemodelsfor -Ansand -Full. For
instances each from HQ and 2W, and referred to HQand2W,theyworksim(cid:15)ilarto -A(cid:15)ns.
asHQ-20kand2W-20k,respectively.
(cid:15)
|     |     |     |     |     |     |     | 7.2.1 | MultihopModels |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----- | -------------- | --- | --- | --- | --- | --- |
Notation. Instancesin -Ans,HQ,and2Ware End2End (EE) Model. This model takes
of the form (Q,C;A,P s(cid:15) ). Given a question Q (Q,C) as input, runs it through a transformer,
| and context | C   | consisting | of  | a set of | paragraphs, |     |              |      |     |        |            |      |     |
| ----------- | --- | ---------- | --- | -------- | ----------- | --- | ------------ | ---- | --- | ------ | ---------- | ---- | --- |
|             |     |            |     |          |             |     | and predicts | (A,P | )   | as the | output for | -Ans | and |
s
| the task | is to | predict | the answer | A   | and identify |     |               |     |        |                               |     |     |     |
| -------- | ----- | ------- | ---------- | --- | ------------ | --- | ------------- | --- | ------ | ----------------------------- | --- | --- | --- |
|          |       |         |            |     |              |     | (A,P s ,S)for |     | -Full. | WeuseLongfo(cid:15)rmer-Large |     |     |     |
supporting paragraphs P s ∈ C. -Ans addition- as it’s one of(cid:15)the few transformer architectures
| ally has     | gold   | decomposition |     | G Q(cid:15)(§3), | which | can   |         |         |        |          |          |     |         |
| ------------ | ------ | ------------- | --- | ---------------- | ----- | ----- | ------- | ------- | ------ | -------- | -------- | --- | ------- |
|              |        |               |     |                  |       |       | that is | able to | fit    | the full | context, | and | follow  |
| be leveraged | during | training.     |     | Instances        | in    | -Full |         |         |        |          |          |     |         |
|              |        |               |     |                  |       |       | Beltagy | et al.  | (2020) | for      | answer   | and | support |
areofform(Q,C;A,P ,S),wherethere’s(cid:15)anad- prediction. Answerability prediction is done via
s
ditionalbinaryclassificationtasktopredictS,the
binaryclassificationusingCLStoken.
answerabilityofQbasedonC,alsoreferredtoas
NotethatourLongformerEEmodelisastrong
contextsufficiency(Trivedietal.,2020).
|          |     |       |     |         |     |        | model for      | multihop |            | reasoning.  | When    | trained     | on    |
| -------- | --- | ----- | --- | ------- | --- | ------ | -------------- | -------- | ---------- | ----------- | ------- | ----------- | ----- |
|          |     |       |     |         |     |        | full datasets, |          | its answer | F1          | is 78.4 | (within     | 3 pts |
| Metrics. | For | -Ans, | HQ, | and 2W, | we  | report |                |          |            |             |         |             |       |
|          |     |       |     |         |     |        | of published   | SOTA     |            | (Groeneveld | et      | al., 2020)) | on    |
thestandardF1b(cid:15)asedmetricsforanswer(An)and
HQ,and87.7(SOTA)on2W.
| support | identification |     | (Sp); see | Yang | et al. (2018) |     |     |     |     |     |     |     |     |
| ------- | -------------- | --- | --------- | ---- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
for details. To make a fair comparison across Select+Answer (SA) Model. This model, in-
datasets,weuseonlyparagraph-levelsupportF1.
|     |        |           |         |     |            |     | spired  | by Quark | (Groeneveld |     | et al.,    | 2020)  | and   |
| --- | ------ | --------- | ------- | --- | ---------- | --- | ------- | -------- | ----------- | --- | ---------- | ------ | ----- |
| For | -Full, | we follow | Trivedi | et  | al. (2020) | to  |         |          |             |     |            |        |       |
|     |        |           |         |     |            |     | SAE (Tu | et al.,  | 2020),      | has | two parts. | First, | a se- |
combin(cid:15)esufficiencypredictionS withAnandSp, lector ranksandselectstheK mostrelevantpara-
| whicharedenotedasAn+SfandSp+Sf. |     |     |     |     | Instances |     |        |     |     |               |     |       |       |
| ------------------------------- | --- | --- | --- | --- | --------- | --- | ------ | --- | --- | ------------- | --- | ----- | ----- |
|                                 |     |     |     |     |           |     | graphs | C ⊆ | C.8 | Specifically, |     | given | (Q,C) |
K
| in -Fullareevaluatedinpairs. |     |     |     | ForeachQwitha |     |     |           |               |     |       |           |     |     |
| ---------------------------- | --- | --- | --- | ------------- | --- | --- | --------- | ------------- | --- | ----- | --------- | --- | --- |
|                              |     |     |     |               |     |     | as input, | it classifies |     | every | paragraph | P   | ∈ C |
suf(cid:15)ficientcontextC,thereisapairedinstancewith
|     |     |     |     |     |     |     | as relevant | or  | not, | and is trained | with | the | cross- |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ---- | -------------- | ---- | --- | ------ |
C(cid:48).
Q and an insufficient context For An+Sf, if a entropy loss. Second, for MuSiQue-Ans, the an-
modelincorrectlypredictscontextsufficiency(yes
|     |     |     |     |     |     |     | swerer | predicts | the | answer | and supporting |     | para- |
| --- | --- | --- | --- | --- | --- | --- | ------ | -------- | --- | ------ | -------------- | --- | ----- |
orno)foreitheroftheinstancesinapair,itgets0
|     |     |     |     |     |     |     | graphs | based | only | on C K . | For MuSiQue-Full, |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | ----- | ---- | -------- | ----------------- | --- | --- |
pts on that pair. Otherwise, it gets same An score it additionally predicts answerability. Both com-
| on that | pair as | it gets | on the | answerable | instance |     |     |     |     |     |     |     |     |
| ------- | ------- | ------- | ------ | ---------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
ponentsaretrainedindividuallyusingannotations
| inthatpair. | Scoresareaveragedacrossallpairsof |     |     |     |     |     |           |        |          |     |           |     |          |
| ----------- | --------------------------------- | --- | --- | --- | --- | --- | --------- | ------ | -------- | --- | --------- | --- | -------- |
|             |                                   |     |     |     |     |     | available | in the | dataset. | We  | implement | a   | selector |
instancesinthedataset. LikewiseforSp+Sf. usingRoBERTa-large(Liuetal.,2019),andanan-
swererusingLongformer-Large.
7.2 Models
Our models are Transformer-based (Vaswani Step Execution (EX) Model. Similar to prior
work(TalmorandBerant,2018;Minetal.,2019b;
etal.,2017)languagemodels(Devlinetal.,2019),
|     |     |     |     |     |     |     | Qietal.,2021;Khotetal.,2021), |     |     |     | thismodelper- |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------------------- | --- | --- | --- | ------------- | --- | --- |
implementedusingPyTorch(Paszkeetal.,2019),
HuggingFaceTransformers(Wolfetal.,2019)and forms explicit, step-by-step multihop reasoning,
byfirstdecomposingtheQintoaDAGG
|                         |     |     |     |                        |     |     |     |     |     |     |     | Q   | having |
| ----------------------- | --- | --- | --- | ---------------------- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |
| 7Forbrevity,weuseHQ,2W, |     |     |     | -Ans/FulltorefertoHot- |     |     |     |     |     |     |     |     |        |
potQA,2WikiMultihopQA,MuSiQue-Ans/Full,resp. 8Kisahyperparameter,chosenfrom{3,5,7}.
(cid:15)

single-hop questions, and then calling single-hop paragraph p ∈ P and predicts an answer to Q
s
modelrepeatedlytoexecutethisdecomposition. based solely on p. This model can’t access full
Thedecomposer istrainedwithgolddecompo- supporting information as all considered datasets
sitions,andisimplementedwithBART-large. haveatleast2supportingparagraphs.
The executor takes C and the predicted DAG
7.2.3 CheatabilityScore
G , and outputs (A,P ) for MuSiQue-Ans and
Q s
WecomputetheDiRescoreofalldatasets,which
(A,P ,S) for MuSiQue-Full. It calls single-hop
s
measures the extent to which the datasets can be
model M repeatedly while traversing G along
s Q
cheated by strong models via Disconnected Rea-
theedgesandsubstitutingtheanswers.
soning (Trivedi et al., 2020). We report scores
Model M is trained on only single-hop
s
basedontheSAmodelsinceitperformedthebest.
instances—taking (q ,C) as input, and produc-
i
ing (A,P ) or (A,P ,S ) as the output. Here P
i si i i 7.3 HumanPerformance
refers to the supporting paragraph for q and S
i i
Apartfromassessingthehumanperformancelevel
refers to whether C is sufficient to answer q . For
i
on -Ans, as discussed in §6, we also obtain hu-
MuSiQue-Full,theanswererpredictsQashaving
sufficientcontextifM predictsallq tohavesuf-
man(cid:15)performanceonHQand2W.Forafaircom-
s i
parison, we use the same crowdsourcing work-
ficient context. We implement 2 such single-hop
ers,annotationguidelines,andinterfaceacrossthe
modelsM : End2EndandSelect+Answer,abbre-
s
3 datasets. We sample 125 questions from each
viatedasEX(EE)andEX(SA)respectively
dataset, shufflethemallintoone set, andobtain3
We don’t experiment with this model on HQ,
annotationsperquestionforanswerandsupport.
sinceitneedsground-truthdecompositionandin-
To select the workers, we ran a qualification
termediateanswers,whicharen’tavailableinHQ.
roundwhereeachworkerwasrequiredtoidentify
Baseline (RNN) Model. The filtering steps in answer and support for at least 25 questions. We
ourpipelineusetransformer-basedmodels,which then selected workers who had more than 75 An
could make MuSiQue particularly difficult for andSpscoresonalldatasets. 7outof15workers
transformer-based models. A natural question werequalifiedforrestofthevalidation.
then is, can a strong non-transformer model per-
8 EmpiricalFindings
form better on MuSiQue? To answer this, we
evaluate our re-implementation of a strong RNN-
We now discuss our findings, demonstrating that
based baseline (Yang et al., 2018) (see their orig-
MuSiQue is a challenging multihop dataset that
inal paper for details). To verify our implemen-
is harder to cheat on than existing datasets (§8.1)
tation, we trained it on full HotpotQA and found
and that the steps in the MuSiQue construction
its performance to be 64.0 An (answer F1) on the
pipeline are individually valuable (§8.2). Finally,
validationset,betterthanwhat’sreportedbyYang
weexploreavenuesforfuturework(§8.3).
etal.(2018)(58.3An). Wethususethismodelas
For HQ and 2W, we report validation set per-
astrongnon-transformerbaseline.
formance. For -Ansand -Full,Table5reports
7.2.2 Artifact-basedModels
testsetnumber(cid:15)s;allelseis(cid:15)onthevalidationset.
The Q-Only Model takes only Q as input (no 8.1 MuSiQueisaChallengingDataset
C)andgeneratesoutputAfor -Ansand(A,S)
Compared to HQ and 2W, both variants of
for -Full. We implement(cid:15)this with BART-
MuSiQuearelesscheatableviashortcutsandhave
large(cid:15)(Lewis et al., 2020a). The C-Only Model
alargerhuman-to-modelgap.
takesonlyC asinput(noQ)andpredicts(A,P )
s
for -Ans and (A,P ,S) for -Full. We im- Higher Human-Model Gap. Top two sections
s
plem(cid:15)entthiswithanEELongfor(cid:15)mer-Largemodel of Table4 show -Ans hasa significantlyhigher
withemptyQ. The1-ParaModel,likeMinetal. human-modelgap(cid:15)(computedasHumanScoremi-
(2019a);ChenandDurrett(2019),issimilartoSA nus best model score) than the other datasets, for
model with K=1. Instead of training the selector both answer and supporting paragraph identifica-
to rank all P the highest, we train it to rank any tion. In fact, for both the other datasets, support-
s
paragraph containing the answer A as the high- ingparagraphidentificationhasevensurpassedthe
est. Theanswererthentakesasinputoneselected human score, whereas for -Ans, there is 14 pts
(cid:15)

HQ-20K 2W-20K -Ans
An|Sp An|Sp An|Sp
(cid:15)
-uH nam
Score 84.5|92.5 83.2|99.3 78.0|93.9
UB 91.8|96.0 89.0|100 88.6|97.3
pohitluM sledoM
RNN 51.0|82.4 52.7|94.9 13.6|41.9
EE 72.9|94.3 72.9|97.6 42.3|67.6
SA 74.9|94.6 79.5|99.0 47.3|72.3
EX(EE) — 79.8|97.5 45.6|77.8
EX(SA) — 71.2|98.1 49.8|79.2
tcafitrA sledoM
-Ans -Full
An|Sp An+Sf|Sp+Sf
(cid:15) (cid:15)
1-Para 64.8| — 60.1| — 32.0| —
C-only 18.4|67.6 50.1|92.0 3.4| 0.0
Q-only 19.6| — 27.0| — 4.6| —
DiReScore 68.8|93.0 63.4|98.5 37.8|63.4
Table 4: Compared to the other datasets considered,
-Ans has a much larger human-model gap (higher
gapbetweentopandmiddlesections),andismuchless (cid:15)
cheatable(lowerscoresinbottomtwosections).
gap. Additionally, -Anshasa∼27ptgapinan-
swer F1, whereas H(cid:15)Q and 2W have a gap of only
10and5,respectively.
Ourbestmodel,EX(SA),scores57.9,47.9,and
28.1answerF1on2,3,and4-hopquestionsof -
Ans,resp. TheEEmodel,ontheotherhand,sta(cid:15)ys
around42%irrespectiveofthenumberofhops.
LowerCheatability. The3rdsectionofTable4
showsthattheperformanceofartifact-basedmod-
els (§7.2.2) is much higher on HQ and 2W than
on -Ans. E.g., the 1-Para model achieves 64.8
and(cid:15)60.1 answer score on HQ and 2W, resp., but
only 32.0 on -Ans. Support identification in
both datasets c(cid:15)an be done to a surprisingly high
degree (67.6 and 92.0 F1) even without the ques-
tion(C-onlymodel),butfailson -Ans.9
Similarly,thelastrowofTable(cid:15)4showsthatthe
DiReanswerscoresofHQand2W(68.8and63.4)
arehigh,indicatingthatevendisconnectedreason-
ing (bypassing reasoning steps) can achieve such
high scores. In contrast, this number is signifi-
cantlylower(37.8)for -Ans.
Theseresultsdemons(cid:15)tratethat -Ansissignifi-
cantlylesscheatableviashortcut-(cid:15)basedreasoning.
MuSiQue-Full: Even More Challenging. Ta-
ble 5 shows that -Full is significantly more dif-
ficultandlessche(cid:15)atablethan -Ans.
Intuitively, because the an(cid:15)swerable and unan-
swerable instances are very similar but have dif-
9Even when -Ans is modified to have 10 paragraphs
likeHQ,C-onlysupportscoreremainslow;cf.Table7.
(cid:15)
pohitluM
sledoM
EE 40.7|69.4 24.0|25.6
SA 52.3|75.2 34.8|42.1
Ex(EE) 46.4|78.1 32.2|44.2
Ex(SA) 49.0|80.6 32.2|44.3
tcafitrA sledoM
1-Para 35.7| — 2.3| —
C-only 3.7| 0.0 1.6| 1.1
Q-only 4.6| — 0.0| —
Table5: -Fullisharder(toprow)andlesscheatable
(bottomrow)than -Ans. Note: -Fullhasastricter
(cid:15)
metricthatoperatesoverinstancepairs(§7.1:metrics).
(cid:15) (cid:15)
ferent labels, it’s difficult for models to do well
on both instances if they learn to rely on short-
cuts (Kaushik et al., 2019; Gardner et al., 2020).
Allartifact-basedmodelsbarelygetanyAn+Sfor
Sp+Sfscore. Forallmultihopmodelstoo, theAn
dropsby14-17ptsandSpby33-44pts.
8.2 DatasetConstructionStepsareValuable
Next, we show that the key steps of our dataset
constructionpipeline(§5)arevaluable.
Disconnection Filter (step 3). To assess the ef-
fect of Disconnection Filter (DF), we ablate it
from the pipeline, ie., skip the filtering compos-
able 2-hop questions to connected 2-hop ques-
tions. As we don’t have human-generated com-
posedquestionsfortheresultingquestions,weuse
a seq2seq BART-large model that’s trained (using
MuSiQue) to compose questions from input de-
compositionDAG.Forafaircomparison,weran-
domlysubsampletrainsetfromablatedpipelineto
beofthesamesizeastheoriginaltrainset.
1-Para C-only EE
An|Sp An|Sp An|Sp
32.0| — 3.4| 0.0 42.3|67.6
\DF 59.2| — 8.6|22.4 60.6|71.1 (cid:15)
\RL 85.1| — 69.5|42.3 87.3|79.3
(cid:15)
(cid:15)
Table 6: Disconnection Filter (DF, step 5) and Re-
duced Train-Test Leakage (RL, step 3) of MuSiQue
pipeline are crucial for its difficulty (EE model) and
lesscheatability(1-ParaandC-onlymodels).
Table 6 shows that DF is crucial for increas-
ing difficulty and reducing cheatability of the
dataset. Without DF, both multihop and artifact-
based models do much better on the resulting
datasets.

Reduced Train-Test Leakage (step 5). To as- Second, using 20 paragraphs instead of 10
sesstheeffectofReducedtrain-testLeakage(RL), makes the dataset more difficult and less cheat-
wecreateadatasetthetraditionalway,witharan- able. Interestingly, the effect is stronger if we
dompartitionintotrain,validation,andtestsplits. use PD, indicating the synergy between two ap-
For uniformity, we ensure the distribution of 2-4 proachestocreatechallengingdistractors.
| hop questions | in   | development | set       | of the resulting |     |                                    |     |     |     |     |     |     |
| ------------- | ---- | ----------- | --------- | ---------------- | --- | ---------------------------------- | --- | --- | --- | --- | --- | --- |
|               |      |             |           |                  |     | 8.3 PotentialAvenuesforImprovement |     |     |     |     |     |     |
| dataset from  | both | ablated     | pipelines | remains          | the |                                    |     |     |     |     |     |     |
same as in the original development set. Like DF Better Decomposition. We train our EX(SA)
ablation,wealsonormalizetrainsetsizes. modelusingground-truthdecompositions. On -
Table 6 shows that without a careful split, the Ans, (An, Sp) improve by (9.4, 7.3) pts, and(cid:15)on
dataset is highly solvable by multihop models -Full,(An+Sf,Sp+Sf)improveby(7.3,6.9)pts.
(An=87.3). Importantly, most of this high score (cid:15)The improvements with the EX(EE) model are
can also be achieved by artifact-based models: 1- slightly lower. This shows that although improv-
para (An=85.1) and C-only (An=69.5), revealing ingquestiondecompositionwillbehelpful,it’sin-
thehighcheatabilityofsuchasplit. sufficienttoreachhumanparityonthedataset.
Harder Distractors (step 7). To assess the ef- Better Transformer. While Longformer can fit
fect of distractors in -Ans, we create 4 varia- long context, there are arguably more effective
| tions. Two | vary | the(cid:15)number | of  | distractors: | (i) |     |     |     |     |     |     |     |
| ---------- | ---- | ----------------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
pretrainedtransformersforshorterinput,e.g.,T5.
10 paragraphs and (ii) 20 paragraphs; and two Moreover, since T5 uses relative position embed-
varythesource: (i)Fullwikipedia(FW)10 and(ii) dings, it can be used for longer text, although at
goldcontextparagraphsfromthegoodsingle-hop a significant memory and computation cost. We
questions from step 1. We refer to the last setting managedtotrainSAwithT5-largeonMuSiQue,12
as positive distractors (PD), as these paragraphs but didn’t use it for the rest of our experiments
are likely to appear as supporting (positive) para- because of high computational cost. Over Long-
graphsinourfinaldataset.
formerSA,T5SAshowedamodestimprovement
|             |       |        |        |       |     | of(6.1,0.7)on |     | -Ansand(1.7,2.0)on |     |     |     | -Full.   |
| ----------- | ----- | ------ | ------ | ----- | --- | ------------- | --- | ------------------ | --- | --- | --- | -------- |
| Ctxt Corpus |       | 1-Para | C-Only |       | EE  |               |     |                    |     |     |     |          |
|             |       |        |        |       |     |               |     | (cid:15)           |     |     |     | (cid:15) |
|             | An|Sp |        | An|Sp  | An|Sp |     | 9 Conclusion  |     |                    |     |     |     |          |
10 FW 42.5| — 12.5|77.7 57.2|87.6 Constructing multihop datasets is a tricky pro-
| 10    | PD 28.0| | —   | 5.5|34.6  | 54.1|80.2 |     |             |        |           |     |            |     |           |
| ----- | -------- | --- | --------- | --------- | --- | ----------- | ------ | --------- | --- | ---------- | --- | --------- |
|       |          |     |           |           |     | cess.       | It can | introduce |     | shortcuts  | and | artifacts |
|       | 41.7|    |     | 12.4|66.4 | 50.3|80.8 |     |             |        |           |     |            |     |           |
| 20 FW |          | —   |           |           |     | that models | can    | exploit   | to  | circumvent |     | the need  |
20 PD 32.0| — 3.4| 0.0 42.3|67.6 for multihop reasoning. A bottom-up process of
| (cid:15)                           |                      |     |          |             |           | constructing    | multihop   |             | from     | single-hop |           | questions |
| ---------------------------------- | -------------------- | --- | -------- | ----------- | --------- | --------------- | ---------- | ----------- | -------- | ---------- | --------- | --------- |
| Table 7:                           | Positive Distractors |     | (PD) are | more        | effective |                 |            |             |          |            |           |           |
|                                    |                      |     |          |             |           | allows          | systematic | exploration |          | of         | a large   | space     |
| than using                         | Full Wikipedia       |     | (FW) for | choosing    | distrac-  |                 |            |             |          |            |           |           |
|                                    |                      |     |          |             |           | of multihop     | candidates |             | and      | greater    | control   | over      |
| tors,asshownbylowerscoresofmodels. |                      |     |          | Theeffectof |           |                 |            |             |          |            |           |           |
|                                    |                      |     |          |             |           | which questions |            | we          | compose. |            | We showed | how       |
usingPDismorepronouncedwhencombinedwiththe
useof20(ratherthan10)distractorparagraphs. to use such a carefully controlled process to cre-
|     |     |     |     |     |     | ate a challenging |     | dataset | that, | by  | design, | requires |
| --- | --- | --- | --- | --- | --- | ----------------- | --- | ------- | ----- | --- | ------- | -------- |
Table 7 shows that all models find PD signif- connected reasoning by reducing potential rea-
icantly harder than FW. In particular, PD makes soning shortcuts, minimizing train-test leakage,
| support       | identification | extremely |             | difficult | for C- |               |      |        |            |     |                 |        |
| ------------- | -------------- | --------- | ----------- | --------- | ------ | ------------- | ---- | ------ | ---------- | --- | --------------- | ------ |
|               |                |           |             |           |        | and including |      | harder | distractor |     | contexts.       | Empir- |
| only, whereas | Table          | 4         | showed that | C-only    | suc-   |               |      |        |            |     |                 |        |
|               |                |           |             |           |        | ical results  | show | that   | -Ans       | has | a substantially |        |
ceeds on HQ and 2W to a high degree (67.6 and higher human-model g(cid:15)ap and is significantly less
92.0 Sp). This would have also been true for - cheatable via disconnected reasoning than previ-
| Ans (66.4 | Sp) had | we used | Wikipedia | as  | the d(cid:15)is- |               |     |             |     |            |     |            |
| --------- | ------- | ------- | --------- | --- | ---------------- | ------------- | --- | ----------- | --- | ---------- | --- | ---------- |
|           |         |         |           |     |                  | ous datasets. |     | The dataset |     | also comes |     | with unan- |
tractor construction corpus like HQ and 2W. This swerable questions, and question decompositions
underscoresthevalueofselectingtherightcorpus which we hope spurs further work in developing
fordistractorselection,andensuringdistributional
modelsthatgetrightanswersfortherightreasons.
shiftcan’tbeexploitedtobypassreasoning.11
suredretrievedcontextsfromFWare20-300words,likePD.
10WeusedtheWikipediacorpusfromPetronietal.(2021). 12SAworkedbestfor7selectedparagraphs,wherethean-
11Oursingle-hopdatasetsarewikipedia-based,andween- swerer(T5)hadtoprocess∼1100wordpiecesonaverage.

| Acknowledgments |       |            |     |        |               |     | Zhou. | 2020.      | Evaluating |          | models’ |     | local deci- |
| --------------- | ----- | ---------- | --- | ------ | ------------- | --- | ----- | ---------- | ---------- | -------- | ------- | --- | ----------- |
|                 |       |            |     |        |               |     | sion  | boundaries | via        | contrast | sets.   | In  | Findings    |
| The authors     | thank | the action |     | editor | and reviewers |     |       |            |            |          |         |     |             |
ofEMNLP.
| for their | valuable | feedback. |     | This work | was | sup- |     |     |     |     |     |     |     |
| --------- | -------- | --------- | --- | --------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
portedinpartbytheNationalScienceFoundation
|     |     |     |     |     |     |     | Matt Gardner, |     | Joel | Grus, | Mark |     | Neumann, |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ---- | ----- | ---- | --- | -------- |
undergrantIIS-1815358. OyvindTafjord,PradeepDasigi,NelsonF.Liu,
|     |     |     |     |     |     |     | Matthew      | Peters, | Michael |           | Schmitz, | and    | Luke S. |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ------- | ------- | --------- | -------- | ------ | ------- |
|     |     |     |     |     |     |     | Zettlemoyer. |         | 2017.   | AllenNLP: |          | A deep | seman-  |
References
|     |     |     |     |     |     |     | ticnaturallanguageprocessingplatform. |     |     |     |     |     | arXiv |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------------- | --- | --- | --- | --- | --- | ----- |
preprintarXiv:1803.07640.
IzBeltagy,MatthewE.Peters,andArmanCohan.
| 2020.      | Longformer:       |               | The long-document |       |             | trans- |               |           |           |           |          |            |           |
| ---------- | ----------------- | ------------- | ----------------- | ----- | ----------- | ------ | ------------- | --------- | --------- | --------- | -------- | ---------- | --------- |
|            |                   |               |                   |       |             |        | Mor Geva,     | Daniel    | Khashabi, |           | Elad     | Segal,     | Tushar    |
| former.    | arXiv:2004.05150. |               |                   |       |             |        |               |           |           |           |          |            |           |
|            |                   |               |                   |       |             |        | Khot,         | Dan       | Roth,     | and       | Jonathan | Berant.    | 2021.     |
|            |                   |               |                   |       |             |        | Did Aristotle |           | Use       | a Laptop? |          | A Question | An-       |
| Jifan Chen | and               | Greg Durrett. |                   | 2019. | Understand- |        |               |           |           |           |          |            |           |
|            |                   |               |                   |       |             |        | swering       | Benchmark |           | with      | Implicit |            | Reasoning |
ingdatasetdesignchoicesformulti-hopreason-
|     |     |     |     |     |     |     | Strategies. |     | TACL. |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ----- | --- | --- | --- | --- |
ing. InNAACL-HLT.
|           |       |         |              |       |          |        | Dirk Groeneveld,     |            | Tushar |       | Khot,    | Mausam, | and        |
| --------- | ----- | ------- | ------------ | ----- | -------- | ------ | -------------------- | ---------- | ------ | ----- | -------- | ------- | ---------- |
| Wenhu     | Chen, | Hanwen  | Zha, Zhiyu   | Chen, |          | Wenhan |                      |            |        |       |          |         |            |
|           |       |         |              |       |          |        | Ashish               | Sabharwal. |        | 2020. | A simple |         | yet strong |
| Xiong,    | Hong  | Wang,   | and William  |       | Wang.    | 2020.  |                      |            |        |       |          |         |            |
|           |       |         |              |       |          |        | pipelineforHotpotQA. |            |        |       | InEMNLP. |         |            |
| Hybridqa: | A     | dataset | of multi-hop |       | question | an-    |                      |            |        |       |          |         |            |
sweringovertabularandtextualdata. Findings XanhHo,A.Nguyen,SakuSugawara,andAkiko
| ofEMNLP2020. |     |     |     |     |     |     | Aizawa. | 2020. |     | Constructing |     | a multi-hop | qa  |
| ------------ | --- | --- | --- | --- | --- | --- | ------- | ----- | --- | ------------ | --- | ----------- | --- |
datasetforcomprehensiveevaluationofreason-
| Jacob Devlin,  |               | Ming-Wei | Chang,       | Kenton    | Lee,         | and     |                     |           |           |               |             |           |            |
| -------------- | ------------- | -------- | ------------ | --------- | ------------ | ------- | ------------------- | --------- | --------- | ------------- | ----------- | --------- | ---------- |
|                |               |          |              |           |              |         | ingsteps.           | InCOLING. |           |               |             |           |            |
| Kristina       | Toutanova.    |          | 2019.        | BERT:     | Pre-training |         |                     |           |           |               |             |           |            |
|                |               |          |              |           |              |         | Matthew             | Honnibal, |           | Ines Montani, |             | Sofie     | Van Lan-   |
| of deep        | bidirectional |          | transformers |           | for language |         |                     |           |           |               |             |           |            |
|                |               |          |              |           |              |         | deghem,             | and       | Adriane   |               | Boyd.       | 2020.     | SpaCy:     |
| understanding. |               | InNAACL. |              |           |              |         |                     |           |           |               |             |           |            |
|                |               |          |              |           |              |         | Industrial-strength |           |           | natural       | language    |           | processing |
| Dheeru         | Dua,          | Yizhong  | Wang,        | Pradeep   |              | Dasigi, | inPython.           |           |           |               |             |           |            |
| Gabriel        | Stanovsky,    |          | Sameer       | Singh,    | and          | Matt    |                     |           |           |               |             |           |            |
|                |               |          |              |           |              |         | Peter Jansen,       |           | Elizabeth |               | Wainwright, |           | Steven     |
| Gardner.       | 2019.         | DROP:    |              | A reading | compre-      |         |                     |           |           |               |             |           |            |
|                |               |          |              |           |              |         | Marmorstein,        |           | and       | Clayton       |             | Morrison. | 2018.      |
hensionbenchmarkrequiringdiscretereasoning
|                 |     |                 |          |        |           |     | WorldTree:     |               | A corpus   |     | of explanation |     | graphs     |
| --------------- | --- | --------------- | -------- | ------ | --------- | --- | -------------- | ------------- | ---------- | --- | -------------- | --- | ---------- |
| overparagraphs. |     | InNAACL.        |          |        |           |     |                |               |            |     |                |     |            |
|                 |     |                 |          |        |           |     | for elementary |               | science    |     | questions      |     | supporting |
|                 |     |                 |          |        |           |     | multi-hop      |               | inference. |     | In Proceedings |     | of the     |
| Hady ElSahar,   |     | P. Vougiouklis, |          | Arslen | Remaci,   |     |                |               |            |     |                |     |            |
|                 |     |                 |          |        |           |     | Eleventh       | International |            |     | Conference     |     | on Lan-    |
| C. Gravier,     |     | Jonathon        | S. Hare, | F.     | Laforest, | and |                |               |            |     |                |     |            |
E. Simperl. 2018. T-REx: A large scale align- guageResourcesandEvaluation(LREC2018),
ment of natural language with knowledge base Miyazaki, Japan. European Language Re-
sourcesAssociation(ELRA).
| triples. | InLREC.   |      |          |          |     |     |         |         |        |         |        |       |           |
| -------- | --------- | ---- | -------- | -------- | --- | --- | ------- | ------- | ------ | ------- | ------ | ----- | --------- |
|          |           |      |          |          |     |     | Yichen  | Jiang,  | Shikha | Bordia, |        | Zheng | Zhong,    |
| James    | Ferguson, | Matt | Gardner, | Hannaneh |     | Ha- |         |         |        |         |        |       |           |
|          |           |      |          |          |     |     | Charles | Dognin, |        | Maneesh | Singh, |       | and Mohit |
jishirzi,TusharKhot,andPradeepDasigi.2020.
|     |     |     |     |     |     |     | Bansal. | 2020. | HoVer: |     | A dataset |     | for many- |
| --- | --- | --- | --- | --- | --- | --- | ------- | ----- | ------ | --- | --------- | --- | --------- |
IIRC:Adatasetofincompleteinformationread-
|     |     |     |     | InEMNLP. |     |     | hop fact | extraction |     | and | claim | verification. | In  |
| --- | --- | --- | --- | -------- | --- | --- | -------- | ---------- | --- | --- | ----- | ------------- | --- |
ingcomprehensionquestions.
EMNLP.
| Matt Gardner, |               | Yoav    | Artzi,   | Victoria | Basmova,  |         |                |          |            |          |       |                   |         |
| ------------- | ------------- | ------- | -------- | -------- | --------- | ------- | -------------- | -------- | ---------- | -------- | ----- | ----------------- | ------- |
|               |               |         |          |          |           |         | Divyansh       | Kaushik, |            | Eduard   | Hovy, | and               | Zachary |
| Jonathan      | Berant,       | Ben     | Bogin,   |          | Sihao     | Chen,   |                |          |            |          |       |                   |         |
|               |               |         |          |          |           |         | Lipton.        | 2019.    |            | Learning | the   | difference        | that    |
| Pradeep       | Dasigi,       | Dheeru  |          | Dua,     | Yanai     | Elazar, |                |          |            |          |       |                   |         |
|               |               |         |          |          |           |         | makes          | a        | difference |          | with  | counterfactually- |         |
| Ananth        | Gottumukkala, |         | Nitish   | Gupta,   |           | Hanna   |                |          |            |          |       |                   |         |
|               |               |         |          |          |           |         | augmenteddata. |          | InICLR.    |          |       |                   |         |
| Hajishirzi,   |               | Gabriel | Ilharco, | Daniel   | Khashabi, |         |                |          |            |          |       |                   |         |
Kevin Lin, Jiangming Liu, Nelson F. Liu, Divyansh Kaushik and Zachary C. Lipton. 2018.
Phoebe Mulcaire, Qiang Ning, Sameer Singh, How much reading does reading comprehen-
Noah A. Smith, Sanjay Subramanian, Reut sion require? a critical investigation of popular
Tsarfaty, Eric Wallace, A. Zhang, and Ben benchmarks. InEMNLP.

Daniel Khashabi, Snigdha Chaturvedi, Michael Yinhan Liu, Myle Ott, Naman Goyal, Jingfei
Roth, Shyam Upadhyay, and Dan Roth. 2018. Du, Mandar Joshi, Danqi Chen, Omer Levy,
Looking beyond the surface:a challenge set Mike Lewis, Luke Zettlemoyer, and Veselin
for reading comprehension over multiple sen- Stoyanov. 2019. RoBERTa: A robustly opti-
| tences. | InNAACL. |     |     |     |     | mizedbertpretrainingapproach. |     |     |     | arXivpreprint |     |
| ------- | -------- | --- | --- | --- | --- | ----------------------------- | --- | --- | --- | ------------- | --- |
arXiv:1907.11692.
| Daniel Khashabi, |     | Sewon | Min, | Tushar | Khot, |     |     |     |     |     |     |
| ---------------- | --- | ----- | ---- | ------ | ----- | --- | --- | --- | --- | --- | --- |
AshishSabhwaral,OyvindTafjord,PeterClark,
|     |     |     |     |     |     | Sewon | Min, Eric | Wallace, | Sameer |     | Singh, Matt |
| --- | --- | --- | --- | --- | --- | ----- | --------- | -------- | ------ | --- | ----------- |
and Hannaneh Hajishirzi. 2020. UnifiedQA: Gardner,HannanehHajishirzi,andLukeZettle-
Crossing format boundaries with a single qa moyer. 2019a. Compositional questions do not
| system. | FindingsofEMNLP. |     |     |     |     |                                |     |     |     |        |     |
| ------- | ---------------- | --- | --- | --- | --- | ------------------------------ | --- | --- | --- | ------ | --- |
|         |                  |     |     |     |     | necessitatemulti-hopreasoning. |     |     |     | InACL. |     |
TusharKhot,PeterClark,MichalGuerquin,Peter
|         |            |            |     |       |       | Sewon Min,   | Victor | Zhong,      | Luke | S.     | Zettlemoyer, |
| ------- | ---------- | ---------- | --- | ----- | ----- | ------------ | ------ | ----------- | ---- | ------ | ------------ |
| Jansen, | and Ashish | Sabharwal. |     | 2020. | QASC: |              |        |             |      |        |              |
|         |            |            |     |       |       | and Hannaneh |        | Hajishirzi. |      | 2019b. | Multi-hop    |
A dataset for question answering via sentence reading comprehension through question de-
| composition.         |        | InAAAI.   |                     |            |          |                          |      |       |         |        |             |
| -------------------- | ------ | --------- | ------------------- | ---------- | -------- | ------------------------ | ---- | ----- | ------- | ------ | ----------- |
|                      |        |           |                     |            |          | compositionandrescoring. |      |       |         | InACL. |             |
| Tushar Khot,         | Daniel | Khashabi, |                     | Kyle       | Richard- |                          |      |       |         |        |             |
|                      |        |           |                     |            |          | Liangming                | Pan, | Wenhu | Chen,   | Wenhan | Xiong,      |
| son, Peter           | Clark, | and       | Ashish              | Sabharwal. | 2021.    |                          |      |       |         |        |             |
|                      |        |           |                     |            |          | Min-Yen                  | Kan, | and   | William | Yang   | Wang. 2021. |
| Textmodularnetworks: |        |           | Learningtodecompose |            |          |                          |      |       |         |        |             |
Unsupervisedmulti-hopquestionansweringby
| tasks in | the language |     | of existing | models. | In  |                     |     |     |          |     |     |
| -------- | ------------ | --- | ----------- | ------- | --- | ------------------- | --- | --- | -------- | --- | --- |
|          |              |     |             |         |     | questiongeneration. |     |     | InNAACL. |     |     |
NAACL.
|                    |            |                 |           |              |            | Adam          | Paszke,     | Sam      | Gross,           | Francisco | Massa,       |
| ------------------ | ---------- | --------------- | --------- | ------------ | ---------- | ------------- | ----------- | -------- | ---------------- | --------- | ------------ |
| Tom Kwiatkowski,   |            | Jennimaria      |           | Palomaki,    | Olivia     |               |             |          |                  |           |              |
|                    |            |                 |           |              |            | Adam          | Lerer,      | James    | Bradbury,        |           | Gregory      |
| Redfield,          | Michael    | Collins,        |           | Ankur        | P. Parikh, |               |             |          |                  |           |              |
|                    |            |                 |           |              |            | Chanan,       | Trevor      | Killeen, | Zeming           |           | Lin, Natalia |
| Chris Alberti,     |            | Danielle        | Epstein,  | Illia        | Polo-      |               |             |          |                  |           |              |
|                    |            |                 |           |              |            | Gimelshein,   |             | Luca     | Antiga,          | Alban     | Desmaison,   |
| sukhin,            | Jacob      | Devlin,         | Kenton    | Lee,         | Kristina   |               |             |          |                  |           |              |
|                    |            |                 |           |              |            | Andreas       | Kopf,       | Edward   |                  | Yang,     | Zachary De-  |
| Toutanova,         |            | Llion Jones,    |           | Matthew      | Kelcey,    |               |             |          |                  |           |              |
|                    |            |                 |           |              |            | Vito,         | Martin      | Raison,  | Alykhan          | Tejani,   | Sasank       |
| Ming-Wei           | Chang,     | Andrew          |           | M. Dai,      | Jakob      |               |             |          |                  |           |              |
|                    |            |                 |           |              |            | Chilamkurthy, |             | Benoit   | Steiner,         | Lu        | Fang, Junjie |
| Uszkoreit,         | Quoc       | V. Le,          | and       | Slav Petrov. | 2019.      |               |             |          |                  |           |              |
|                    |            |                 |           |              |            | Bai,          | and Soumith |          | Chintala.        | 2019.     | PyTorch:     |
| Natural            | questions: | A               | benchmark | for          | question   |               |             |          |                  |           |              |
|                    |            |                 |           |              |            | An imperative |             | style,   | high-performance |           | deep         |
| answeringresearch. |            | TACL,7:453–466. |           |              |            |               |             |          |                  |           |              |
InNeurIPS,pages8024–8035.
learninglibrary.
OmerLevy,MinjoonSeo,EunsolChoi,andLuke
|                              |     |                 |     |          |         | Fabio Petroni, |        | Aleksandra | Piktus,  |          | Angela Fan, |
| ---------------------------- | --- | --------------- | --- | -------- | ------- | -------------- | ------ | ---------- | -------- | -------- | ----------- |
| Zettlemoyer.                 |     | 2017. Zero-shot |     | relation | extrac- |                |        |            |          |          |             |
|                              |     |                 |     |          |         | Patrick        | Lewis, | Majid      | Yazdani, |          | Nicola De   |
| tionviareadingcomprehension. |     |                 |     | InCoNLL. |         |                |        |            |          |          |             |
|                              |     |                 |     |          |         | Cao,           | James  | Thorne,    | Yacine   | Jernite, | Vassilis    |
Mike Lewis, Yinhan Liu, Naman Goyal, Mar- Plachouras, Tim Rocktäschel, and Sebastian
|                    |     |             |     |          |     | Riedel. | 2021. | KILT: | A benchmark |     | for knowl- |
| ------------------ | --- | ----------- | --- | -------- | --- | ------- | ----- | ----- | ----------- | --- | ---------- |
| jan Ghazvininejad, |     | Abdelrahman |     | Mohamed, |     |         |       |       |             |     |            |
OmerLevy,VeselinStoyanov,andLukeZettle- edgeintensivelanguagetasks. InNAACL.
| moyer. | 2020a. | BART: | Denoising | sequence-to- |     |          |        |      |              |     |            |
| ------ | ------ | ----- | --------- | ------------ | --- | -------- | ------ | ---- | ------------ | --- | ---------- |
|        |        |       |           |              |     | Peng Qi, | Haejun | Lee, | Oghenetegiri |     | "TG" Sido, |
sequencepre-trainingfornaturallanguagegen-
|                |              |            |                |              |        | and Christopher   |            | D.        | Manning. | 2021.      | Answer-      |
| -------------- | ------------ | ---------- | -------------- | ------------ | ------ | ----------------- | ---------- | --------- | -------- | ---------- | ------------ |
| eration,       | translation, | and        | comprehension. |              | In     |                   |            |           |          |            |              |
| ACL.           |              |            |                |              |        | ing open-domain   |            | questions |          | of varying | reason-      |
|                |              |            |                |              |        | ingstepsfromtext. |            |           | InEMNLP. |            |              |
| Patrick Lewis, |              | Barlas     | Og˘uz,         | Ruty Rinott, | Se-    |                   |            |           |          |            |              |
|                |              |            |                |              |        | Pranav            | Rajpurkar, | Robin     | Jia,     | and        | Percy Liang. |
| bastian        | Riedel,      | and Holger |                | Schwenk.     | 2020b. |                   |            |           |          |            |              |
MLQA: Evaluating cross-lingual extractive 2018. Know what you don’t know: Unanswer-
| questionanswering. |     | InACL. |     |     |     | ablequestionsforSQuAD. |     |     |     | InACL. |     |
| ------------------ | --- | ------ | --- | --- | --- | ---------------------- | --- | --- | --- | ------ | --- |
Patrick Lewis, Pontus Stenetorp, and Sebastian Pranav Rajpurkar, Jian Zhang, Konstantin Lopy-
Riedel. 2021. Question and answer test-train rev,andPercyLiang.2016. SQuAD:100,000+
overlap in open-domain question answering questions for machine comprehension of text.
| datasets. | InEACL. |     |     |     |     | InEMNLP. |     |     |     |     |     |
| --------- | ------- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- |

Alon Talmor and Jonathan Berant. 2018. The Ori Yoran, Alon Talmor, and Jonathan Berant.
web as a knowledge-base for answering com- 2021. Turning tables: Generating examples
plexquestions. InNAACL. from semi-structured tables for endowing lan-
|              |     |        |       |     |        |         | guage models | with reasoning | skills. arXiv |
| ------------ | --- | ------ | ----- | --- | ------ | ------- | ------------ | -------------- | ------------- |
| Alon Talmor, | Ori | Yoran, | Amnon |     | Catav, | Dan La- |              |                |               |
preprintarXiv:2107.07261.
| hav, Yizhong   |          | Wang,         | Akari | Asai,  | Gabriel     | Il-   |     |     |     |
| -------------- | -------- | ------------- | ----- | ------ | ----------- | ----- | --- | --- | --- |
| harco,         | Hannaneh | Hajishirzi,   |       | and    | Jonathan    | Be-   |     |     |     |
| rant. 2021.    |          | MultiModalQA: |       |        | Complex     | ques- |     |     |     |
| tion answering |          | over          | text, | tables | and images. | In    |     |     |     |
ICLR.
HarshTrivedi,NiranjanBalasubramanian,Tushar
| Khot,andAshishSabharwal.2020. |                 |        |           |                     | Ismultihop |        |     |     |     |
| ----------------------------- | --------------- | ------ | --------- | ------------------- | ---------- | ------ | --- | --- | --- |
| QA in                         | DiRe condition? |        | Measuring |                     | and        | reduc- |     |     |     |
| ingdisconnectedreasoning.     |                 |        |           | InEMNLP.            |            |        |     |     |     |
| Ming Tu,                      | Kevin           | Huang, | Guangtao  |                     | Wang,      | Jing   |     |     |     |
| Huang,                        | Xiaodong        | He,    | and       | Bowen               | Zhou.      | 2020.  |     |     |     |
| Select,answerandexplain:      |                 |        |           | Interpretablemulti- |            |        |     |     |     |
| hop reading                   | comprehension   |        |           | over                | multiple   | doc-   |     |     |     |
InAAAI.
uments.
| Ashish Vaswani, |     | Noam | Shazeer, |     | Niki | Parmar, |     |     |     |
| --------------- | --- | ---- | -------- | --- | ---- | ------- | --- | --- | --- |
JakobUszkoreit,LlionJones,AidanNGomez,
| Łukasz  | Kaiser, | and | Illia Polosukhin. |     |          | 2017. At- |     |     |     |
| ------- | ------- | --- | ----------------- | --- | -------- | --------- | --- | --- | --- |
| tention | is all  | you | need.             | In  | NeurIPS, | pages     |     |     |     |
5998–6008.
| Johannes    | Welbl,        | Pontus       | Stenetorp, |          | and        | Sebastian  |     |     |     |
| ----------- | ------------- | ------------ | ---------- | -------- | ---------- | ---------- | --- | --- | --- |
| Riedel.     | 2018.         | Constructing |            | datasets |            | for multi- |     |     |     |
| hop reading | comprehension |              |            | across   | documents. |            |     |     |     |
TACL,6:287–302.
| Thomas     | Wolf,         | Lysandre   |               | Debut, | Victor    | Sanh,     |     |     |     |
| ---------- | ------------- | ---------- | ------------- | ------ | --------- | --------- | --- | --- | --- |
| Julien     | Chaumond,     |            | Clement       |        | Delangue, | An-       |     |     |     |
| thony Moi, | Pierric       |            | Cistac,       | Tim    | Rault,    | R’emi     |     |     |     |
| Louf,      | Morgan        | Funtowicz, |               | and    | Jamie     | Brew.     |     |     |     |
| 2019.      | Huggingface’s |            | transformers: |        |           | State-of- |     |     |     |
ArXiv,
| the-art | natural | language |     | processing. |     |     |     |     |     |
| ------- | ------- | -------- | --- | ----------- | --- | --- | --- | --- | --- |
abs/1910.03771.
| Tomer Wolfson,              |      | Mor       | Geva,        | Ankit  | Gupta,  | Matt   |     |     |     |
| --------------------------- | ---- | --------- | ------------ | ------ | ------- | ------ | --- | --- | --- |
| Gardner,                    | Yoav | Goldberg, |              | Daniel | Deutch, | and    |     |     |     |
| JonathanBerant.2020.        |      |           | Breakitdown: |        |         | Aques- |     |     |     |
| tionunderstandingbenchmark. |      |           |              |        | TACL.   |        |     |     |     |
LedellWu,FabioPetroni,MartinJosifoski,Sebas-
| tianRiedel,andLukeZettlemoyer.2020.        |     |     |     |     |     | Zero- |     |     |     |
| ------------------------------------------ | --- | --- | --- | --- | --- | ----- | --- | --- | --- |
| shotentitylinkingwithdenseentityretrieval. |     |     |     |     |     | In    |     |     |     |
EMNLP.
| Zhilin Yang,                        | Peng    | Qi, | Saizheng |        | Zhang, | Yoshua    |     |     |     |
| ----------------------------------- | ------- | --- | -------- | ------ | ------ | --------- | --- | --- | --- |
| Bengio,                             | William | W.  | Cohen,   | Ruslan |        | Salakhut- |     |     |     |
| dinov,andChristopherD.Manning.2018. |         |     |          |        |        | Hot-      |     |     |     |
potQA:Adatasetfordiverse,explainablemulti-
| hopquestionanswering. |     |     |     | InEMNLP. |     |     |     |     |     |
| --------------------- | --- | --- | --- | -------- | --- | --- | --- | --- | --- |

A Appendix
| Figure 3 shows       | our annotation | interface | for the     |
| -------------------- | -------------- | --------- | ----------- |
| question composition | task.          | Figure    | 4 shows our |
annotationinterfaceforestablishinghumanscores
| on MuSiQue-Ans, | 2WikiMultihopQA |     | and Hot- |
| --------------- | --------------- | --- | -------- |
potQA.

Figure 3: Annotation interface used for the question composition task. Workers could see decomposition graph
andpassageassociatedwithsubquestions.

Figure4: AnnotationinterfaceusedforestablishinghumanscoresonMuSiQue-Ans,HotpotQAand2WikiMulti-
hopQA.
