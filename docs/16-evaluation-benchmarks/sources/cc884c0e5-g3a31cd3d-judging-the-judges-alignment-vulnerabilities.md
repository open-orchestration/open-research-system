Judging the Judges: Evaluating Alignment and Vulnerabilities in
LLMs-as-Judges
AmanSinghThakur* and KartikChoudhary* and VenkatSrinikRamayapally*
UniversityofMassachusettsAmherst
|                                  | {amansinghtha,         |          |     | kartikchoudh, | vramayapally}@umass.edu                  |               |      |     |     |     |
| -------------------------------- | ---------------------- | -------- | --- | ------------- | ---------------------------------------- | ------------- | ---- | --- | --- | --- |
|                                  | SankaranVaidyanathan   |          |     |               |                                          | DieuwkeHupkes |      |     |     |     |
| UniversityofMassachusettsAmherst |                        |          |     |               |                                          |               | Meta |     |     |     |
|                                  | sankaranv@cs.umass.edu |          |     |               | dieuwkehupkes@meta.com                   |               |      |     |     |     |
|                                  |                        | Abstract |     |               | MMLU(Hendrycksetal.,2021),TruthfulQA(Lin |               |      |     |     |     |
etal.,2021),andGSM8K(Cobbeetal.,2021)as-
5202 guA 81  ]LC.sc[  6v42621.6042:viXra TheLLM-as-a-judgeparadigmoffersapoten-
sessspecificcapabilities,whileleaderboardssuch
tialsolutiontoscalabilityissuesinhumaneval-
uationoflargelanguagemodels(LLMs),but asChatbotArena(Chiangetal.,2024)andOpen
|           |            |      |           |           | LLM Leaderboard |     | (Beeching | et  | al., 2023) | rank |
| --------- | ---------- | ---- | --------- | --------- | --------------- | --- | --------- | --- | ---------- | ---- |
| there are | still many | open | questions | about its |                 |     |           |     |            |      |
strengths, weaknesses, and potential biases. models based on human or automated pairwise
Thisstudyinvestigatesthirteenmodels,ranging comparisons. Both approaches face challenges
insizeandfamily, as‘judgemodels’evaluat- in evaluating free-form text responses, as assess-
| ing answers | from | nine base | and | instruction- |     |     |     |     |     |     |
| ----------- | ---- | --------- | --- | ------------ | --- | --- | --- | --- | --- | --- |
mentcanbeasdifficultasgenerationitself(seee.g.
| tuned‘exam-takermodels’. |     |     | Wefindthatonly |     |     |     |     |     |     |     |
| ------------------------ | --- | --- | -------------- | --- | --- | --- | --- | --- | --- | --- |
Changetal.,2023;Bavarescoetal.,2024).
thebest(andlargest)modelsshowreasonable
OneapproachtoevaluatingLLMsisusingMCQ
alignmentwithhumans,thoughtheystilldiffer
benchmarkslikeMMLU,whichcompareanswer
withupto5pointsfromhuman-assignedscores.
Ourresearchhighlightstheneedforalignment log-probabilitiesinsteadofassessinggeneratedre-
metricsbeyondpercentagreement, asjudges sponsesdirectly. However,thisapproachlimitsthe
withhighagreementcanstillassignvastlydif- rangeofmeasurableabilitiesanddiffersfromhow
ferentscores. Wealsofindthatsmallermodels LLMsareusedinpractice. Lexicalmethods,such
| and the | lexical metric | contains |     | can provide |     |     |     |     |     |     |
| ------- | -------------- | -------- | --- | ----------- | --- | --- | --- | --- | --- | --- |
asexactmatch(EM)orn-gramoverlap,arepracti-
areasonablesignalinrankingtheexam-taker
calandcost-effectivebutpronetofalsenegatives
| models. | Furthererroranalysisrevealsvulnera- |     |     |     |                                        |     |     |     |     |       |
| ------- | ----------------------------------- | --- | --- | --- | -------------------------------------- | --- | --- | --- | --- | ----- |
|         |                                     |     |     |     | andoftenmisssubtlesemanticdifferences. |     |     |     |     | These |
bilitiesinjudgemodels,suchassensitivityto
promptcomplexityandabiastowardleniency. challengesareamplifiedforinstruction-tunedchat
Our findings show that even the best judge models, which tend to produce more verbose re-
modelsdifferfromhumansinthisfairlyster- sponses (Saito et al., 2023; Renze and Guven,
| ilesetup,indicatingthatcautioniswarranted |     |     |     |     | 2024). |     |     |     |     |     |
| ----------------------------------------- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- |
whenapplyingjudgemodelsinmorecomplex
Forthesereasons,humanevaluationremainsthe
scenarios.
goldstandardforevaluatingLLMresponses.
|     |     |     |     |     | Human | evaluation | is, | however, | expensive | and |
| --- | --- | --- | --- | --- | ----- | ---------- | --- | -------- | --------- | --- |
1 Introduction
|          |          |              |          |        | often impractical, |       | leading | to the  | growing    | use of |
| -------- | -------- | ------------ | -------- | ------ | ------------------ | ----- | ------- | ------- | ---------- | ------ |
| Over the | last few | years, large | language | models |                    |       |         |         |            |        |
|          |          |              |          |        | LLMs as            | judge | models  | (Lin et | al., 2021; | Islam  |
(LLMs) have demonstrated remarkable capabili- et al., 2023; Chiang and Lee, 2023; Liusie et al.,
tiesacrossvariousdomains(Radfordetal.,2019;
|     |     |     |     |     | 2024). While |     | promising | alignment | with | humans |
| --- | --- | --- | --- | --- | ------------ | --- | --------- | --------- | ---- | ------ |
Brownetal.,2020;Achiametal.,2023;AI@Meta,
hasbeennoted(Sottanaetal.,2023;Zhengetal.,
2024, i.a.). As more and more new LLMs with 2024),questionsaboutthisapproachremain. This
| different architectures |     | and | training | methods con- |     |     |     |     |     |     |
| ----------------------- | --- | --- | -------- | ------------ | --- | --- | --- | --- | --- | --- |
workexaminesLLMsasjudges,contrastingthem
tinuetobereleasedandtheircapabilitiesexpand,
|     |     |     |     |     | withhumansandautomatedmethods. |     |     |     | Unlikeprior |     |
| --- | --- | --- | --- | --- | ------------------------------ | --- | --- | --- | ----------- | --- |
accuratelyevaluatingtheirperformanceandlimi-
|     |     |     |     |     | studies, | we focus | on scenarios |     | with high | human |
| --- | --- | --- | --- | --- | -------- | -------- | ------------ | --- | --------- | ----- |
tationsbecomesincreasinglychallenging(Zheng alignment to separate task ambiguity from judge
etal.,2024;Ohmeretal.,2024;Benchekrounetal.,
|     |     |     |     |     | model limitations. |     | Using | TriviaQA | (Joshi | et al., |
| --- | --- | --- | --- | --- | ------------------ | --- | ----- | -------- | ------ | ------- |
2023;Madaanetal.,2024;Lietal.,2023a).
|     |     |     |     |     | 2017), we | evaluate | how judge | models |     | of varying |
| --- | --- | --- | --- | --- | --------- | -------- | --------- | ------ | --- | ---------- |
LLMevaluationmethodsgenerallyfallintoone architecturesandsizesassessexam-takermodels.
| of two broad       | categories. |     | Benchmarks | such as |                                          |       |          |                |     |         |
| ------------------ | ----------- | --- | ---------- | ------- | ---------------------------------------- | ----- | -------- | -------------- | --- | ------- |
|                    |             |     |            |         | In this                                  | work, | we study | the properties |     | of LLMs |
| *EqualContribution |             |     |            |         | asjudges,comparingthemwithhumansandauto- |       |          |                |     |         |
404
ProceedingsoftheFourthWorkshoponGeneration,EvaluationandMetrics(GEM22025),pages404–430
July31–August1,2025©2025AssociationforComputationalLinguistics

  Judges
|     | Human | GPT-4 | Mistral 7B |     | Llama2-70B | Llama3.1-8B |     |     |     |     |     |     |     |
| --- | ----- | ----- | ---------- | --- | ---------- | ----------- | --- | --- | --- | --- | --- | --- | --- |
EM Gemma-2B Llama2-7B Llama3-8B Llama3.1 70B Scott's Pi Score Percentage Agreement
|     | Contains | JudgeLM 7B | Llama2-13B |     | Llama3 70B |     |     |     |     |     |     |                     |     |
| --- | -------- | ---------- | ---------- | --- | ---------- | --- | --- | --- | --- | --- | --- | ------------------- | --- |
|     |          |            |            |     |            |     |     | 100 |     |     |     | Human Alignment 96% |     |
Exam Taker Models
100
|     |     |     |     |     |     |     |     | 90  |     |     |     |     |       87      88      88 |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------ |
90
| egatnecreP erocS egduJ |     |     |     |     |     |     |     | 80  |     |     |     |       74       77 |     |
| ---------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------------- | --- |
80
|     |     |     |     |     |     |     |     | 70  |       64      65      66      69 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------------------------------- | --- | --- | --- | --- |
70
|     |     |     |     |     |     |     |     | 60  |       59 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- |
60
|     |     |     |     |     |     |     |     | 50  |       47 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- |
50
40
|     | 40  |     |     |     |     |     |     |       34   |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- |
|     | 30  |     |     |     |     |     |     | 30      26 |     |     |     |     |     |
|     | 20  |     |     |     |     |     |     | 20         |     |     |     |     |     |
|     | 10  |     |     |     |     |     |     | 10         |     |     |     |     |     |
|     | 0   |     |     |     |     |     |     | 0          |     |     |     |     |     |
B7-2amalL TF 2amalL TF B31 B7-lartsiM TF B7-2amalL esaB B7 lartsiM 2amalL esaB B31 2amalL TF B07 2amalL esaB B07 4-TPG B2-ammeG ME B7-2amalL B8-3amalL sniatnoC B7-MLegduJ B7-lartsiM B07-2amalL B31-2amalL B8-1.3amalL 4-TPG B07-1.3amalL B07-3amalL
|     |     |     | (a) |     |     |     |     |     |     | (b) |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Figure1: Averagescoresassignedbyjudgemodelsandalignmentwithhumanjudges. (a)Scoresassignedto
allexam-takermodelsbythevariousjudgemodels. (b)Averagepercentagreement(blueline)andScott’sπscores
(redbars)ofjudgemodelswithhumanjudges(blackline). Errorbarsannotatestandarddeviationacrossexam-taker
models. Llama3 70B,Llama3.1 70BandGPT-4TurbohaveScott’sπcoefficientthatareindicativeofexcellent
alignment,butarestillwellbelowthehumanalignmentscore.
Exam-takermodels(base&
|     |     |     |     |     | Llama-2 |     | (7B, | 13B, 70B),Mistral | 7B,GPT-4 |     | Turbo |     |     |
| --- | --- | --- | --- | --- | ------- | --- | ---- | ----------------- | -------- | --- | ----- | --- | --- |
instruction-tuned)
|     |     |     |     |     | Llama-2 |     | (7B, | 13B, 70B), | Llama-3 |     | (8B, | 70B), |     |
| --- | --- | --- | --- | --- | ------- | --- | ---- | ---------- | ------- | --- | ---- | ----- | --- |
Judgemodels
|     |     |     |     |     | Llama-3.1 |     | (8B, | 70B),Gemma | 2B,Mistral |     | 7B,JudgeLM |     |     |
| --- | --- | --- | --- | --- | --------- | --- | ---- | ---------- | ---------- | --- | ---------- | --- | --- |
(instruction-tuned)
|     |                      |     |     |     | 7B,GPT-4 |       | Turbo |                |     |     |     |     |     |
| --- | -------------------- | --- | --- | --- | -------- | ----- | ----- | -------------- | --- | --- | --- | --- | --- |
|     | Judgemodels(lexical) |     |     |     | Exact    | Match |       | (EM), Contains |     |     |     |     |     |
Table 1: Exam-taker models and judge models We consider a wide variety of exam-taker models and judge
models;togetanin-depthoverviewoftheirabilities,weconsiderexam-takermodelsofvarioussizes&types.
matedevaluationmethods. Contrarytopriorwork, judges are rarely discriminable, while Scott’s π
wefocusonacleanscenarioinwhichhumanalign- provides a more informative signal. In some
mentisveryhigh,allowingustodistinguishambi- cases,highpercentagreementcanstillgivescores
guityandsubjectivityinthetaskitselffrompoten- thatdiffer10-20pointsfromthehuman-assigned
| tialissueswiththejudgemodels. |             |     |                 | Usingtheknowl- |          |       |      | scores(Figure2). |      |     |     |         |       |
| ----------------------------- | ----------- | --- | --------------- | -------------- | -------- | ----- | ---- | ---------------- | ---- | --- | --- | ------- | ----- |
| edge                          | benchmark   |     | TriviaQA (Joshi |                | et al.,  | 2017) | as   |                  |      |     |     |         |       |
|                               |             |     |                 |                |          |       | •    | Also Scott’s     | π is | not | all | telling | While |
| our                           | playground, |     | we investigate  | how            | thirteen |       | dif- |                  |      |     |     |         |       |
ferentjudgemodelswithvaryingarchitecturesand GPT-4 Turbo and Llama-3 achieve excellent
alignmentscores,theycandifferbyupto5points
| sizesjudgeninedifferentexam-takermodels. |     |     |     |     |     | Our |     |                  |     |                           |     |     |     |
| ---------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ------------------------- | --- | --- | --- |
|                                          |     |     |     |     |     |     |     | fromhumanscores. |     | Moreover,indiscriminating |     |     |     |
mainfindingsare:
betweenexam-takermodels,theirperformanceis
• Evenincleansetups,onlythebestmodelshave
comparabletocheaperalternativeslikeMistral
| highalignmentscores. |     |     | Amongthethirteenjudge   |     |     |     |     |                  |       |      |       |     |           |
| -------------------- | --- | --- | ----------------------- | --- | --- | --- | --- | ---------------- | ----- | ---- | ----- | --- | --------- |
|                      |     |     |                         |     |     |     |     | 7B and contains, | which | have | lower |     | alignment |
| models,onlyGPT-4     |     |     | Turbo,Llama-3.1;70B,and |     |     |     |     |                  |       |      |       |     |           |
scoresbutmoreconsistentbiases(Figure3).
| Llama-3;70B |     | achieved | strong | alignment |     | with |     |     |     |     |     |     |     |
| ----------- | --- | -------- | ------ | --------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
Throughdetailedanalysis(§5),wegaininsights
| humans. | However, |     | even these | fall | short | of  | the |                         |     |          |     |           |     |
| ------- | -------- | --- | ---------- | ---- | ----- | --- | --- | ----------------------- | --- | -------- | --- | --------- | --- |
|         |          |     |            |      |       |     |     | into judge performance. |     | Improved |     | alignment | ap- |
humanalignmentcoefficient(Figure1).
peartobedrivenfromhigherrecallratesandfewer
|     |     |     |     |     |     |     |     | false negatives. | However, | judge |     | models | struggle |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------------- | -------- | ----- | --- | ------ | -------- |
• Scott’sπ distinguishesjudgesbetterthanper- withunder-specifiedanswersandexhibitleniency,
cent alignment. In terms of percent alignment, reducingevaluationconsistency. Theyarealsosen-
405

sitive to prompt length and quality. Surprisingly, formance of models (Liu et al., 2024) and creat-
evenwhenaskedtoevaluateaverbatimmatchwith ing classifiers for pairwise grading (Huang et al.,
| areference,judgemodelssometimesfail. |     |     |     |     |     |     | 2024). |     |     |     |     |     |     |
| ------------------------------------ | --- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- |
Overall, our work highlights the strengths of We build on previous work to investigate the
the LLM-as-a-judge paradigm, while cautioning strengthsandweaknessesofLLMsasjudges. Un-
against overreliance on alignment metrics, even likepreviousstudies,wefocusoncomparingLLM
when they are high. Through error analysis, we outputswithreferenceanswersratherthanpairwise
identify common failure cases, contributing to a comparisons on open-ended tasks. With high hu-
|     |     |     |     |     |     |     | man alignment |     | in this | setting, | we  | gain | a clearer |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ------- | -------- | --- | ---- | --------- |
deeperunderstandingofthisemergingevaluation
paradigm. Withthiswork, ourobjectiveistoim- view of LLM performance. Furthermore, we ex-
proveunderstandingoftheemergingmainstream tendpreviousresearchbyconsideringmoreLLMs,
| paradigmforevaluatingLLM. |     |     |     |     |     |     | bothasjudgesandasevaluatedmodels. |     |     |     |     |     |     |
| ------------------------- | --- | --- | --- | --- | --- | --- | --------------------------------- | --- | --- | --- | --- | --- | --- |
|                           |     |     |     |     |     |     | 3 Methodology                     |     |     |     |     |     |     |
2 Relatedwork
|         |        |         |      |         |            |     | To evaluate | the | strengths | and | weaknesses |     | of the |
| ------- | ------ | ------- | ---- | ------- | ---------- | --- | ----------- | --- | --------- | --- | ---------- | --- | ------ |
| Various | recent | studies | have | used or | considered |     |             |     |           |     |            |     |        |
LLM-as-a-judgeparadigm,wefocusonacompar-
| using LLMs  |            | as judges | for     | tasks such | as   | evalu- |                    |     |        |     |       |       |        |
| ----------- | ---------- | --------- | ------- | ---------- | ---- | ------ | ------------------ | --- | ------ | --- | ----- | ----- | ------ |
|             |            |           |         |            |      |        | atively controlled |     | setup, | in  | which | judge | models |
| ating story | generation |           | (Chiang | and        | Lee, | 2023), |                    |     |        |     |       |       |        |
assessanswersofexam-takermodelsontheknowl-
| retrieval-augmented |     | generation |     | (Es | et al., | 2023), |                |     |          |     |        |     |             |
| ------------------- | --- | ---------- | --- | --- | ------- | ------ | -------------- | --- | -------- | --- | ------ | --- | ----------- |
|                     |     |            |     |     |         |        | edge benchmark |     | TriviaQA |     | (Joshi | et  | al., 2017). |
visualQA(Mañasetal.,2024),codecomprehen-
|     |     |     |     |     |     |     | Withthis | methodological |     | design, |     | itis possible | to  |
| --- | --- | --- | --- | --- | --- | --- | -------- | -------------- | --- | ------- | --- | ------------- | --- |
sion(Zhiqiangetal.,2023),multilingualevaluation
|     |     |     |     |     |     |     | focus on | the | abilities | of the | judges | in  | isolation, |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | --------- | ------ | ------ | --- | ---------- |
(Hadaetal.,2023)andmoregeneralopen-ended
withouthavingtoaddresshumandisagreementand
| tasks(Zhengetal.,2024). |     |     | Zhangetal.(2024)and |     |     |     |                     |     |     |                           |     |     |     |
| ----------------------- | --- | --- | ------------------- | --- | --- | --- | ------------------- | --- | --- | ------------------------- | --- | --- | --- |
|                         |     |     |                     |     |     |     | erroratthesametime. |     |     | Inthissection,weelaborate |     |     |     |
Sottanaetal.(2023)proposewaystostandardise
themainaspectsofourmethodology.
| LLM evaluations           |     | and                   | the role | that               | judge models |     |                |     |                            |     |     |     |     |
| ------------------------- | --- | --------------------- | -------- | ------------------ | ------------ | --- | -------------- | --- | -------------------------- | --- | --- | --- | --- |
| mightplayinsuchsolutions. |     |                       |          | Severalstudieshave |              |     |                |     |                            |     |     |     |     |
|                           |     |                       |          |                    |              |     | Evaluationdata |     | Asourtestbed,weusetheTriv- |     |     |     |     |
| demonstrated              |     | that state-of-the-art |          | LLMs               | such         | as  |                |     |                            |     |     |     |     |
iaQAdataset(Joshietal.,2017),consistingof95K
GPT-4 Turboexhibithighalignmentwithhuman question-answerpairssourcedfrom14triviaand
judgments(Sottanaetal.,2023;Zhengetal.,2024),
|        |        |                 |     |          |          |     | quiz league | websites. |     | Each | question | in  | the train |
| ------ | ------ | --------------- | --- | -------- | -------- | --- | ----------- | --------- | --- | ---- | -------- | --- | --------- |
| though | others | also illustrate |     | that the | paradigm | is  |             |           |     |      |          |     |           |
andvalidationsetisannotatedwithalistofshort
| notyetwithoutfaults. |     |     | Zengetal.(2023)propose |     |     |     |     |     |     |     |     |     |     |
| -------------------- | --- | --- | ---------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
answerscontainingaminimalsetoffactsandevi-
| a benchmark |     | for evaluating |     | the performance |     | of  |     |     |     |     |     |     |     |
| ----------- | --- | -------------- | --- | --------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
dencedocumentscollectedfromWikipediaandthe
LLMsasjudges,andotherapproacheshavebeen
|          |            |     |        |      |      |      | Web. Forourexperiments,weusethevalidationset |     |                               |     |     |     |     |
| -------- | ---------- | --- | ------ | ---- | ---- | ---- | -------------------------------------------- | --- | ----------------------------- | --- | --- | --- | --- |
| proposed | to improve | LLM | judges | such | that | they |                                              |     |                               |     |     |     |     |
|          |            |     |        |      |      |      | oftheunfiltered                              |     | partitionofthebenchmark,using |     |     |     |     |
arealignedwellwithhumans(Shankaretal.,2024; theshortanswersasreferenceanswers. Weusethe
Zhuetal.,2023).
trainingsetforfew-shotexamples.
| Despite | promising |     | results | in various | settings, |     |     |     |     |     |     |     |     |
| ------- | --------- | --- | ------- | ---------- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
Sinceexperimentsrequiremanualannotationof
| judge models |     | still suffer | from | known | issues | of  |     |     |     |     |     |     |     |
| ------------ | --- | ------------ | ---- | ----- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
theexam-takermodelresponses,weusearandom
current LLMs such as hallucinations and factual sample of 400 questions from the dataset. In Ap-
errors(Yeetal.,2023;Turpinetal.,2023)anddif-
pendixI,weshowwithabootstrappingtestthatthis
ficultyinfollowingcomplexinstructions(Lietal.,
|                      |     |     |                          |     |     |     | sample size | has | low variance |     | for | our main | result. |
| -------------------- | --- | --- | ------------------------ | --- | --- | --- | ----------- | --- | ------------ | --- | --- | -------- | ------- |
| 2023b;Heetal.,2024). |     |     | Furthermore,variousstud- |     |     |     |             |     |              |     |     |          |         |
Throughexperimentsdescribedin§3,weestablish
ieshavereportedchallengessuchaspositionbias
thathumanshavehighagreementonjudgementsof
| (Pezeshkpour |     | and Hruschka, |     | 2023; | Zheng | et al., |     |     |     |     |     |     |     |
| ------------ | --- | ------------- | --- | ----- | ----- | ------- | --- | --- | --- | --- | --- | --- | --- |
answersgiventothequestionsinthebenchmark.
| 2023; Wang | et  | al., 2023), |     | verbosity | bias | (Saito |     |     |     |     |     |     |     |
| ---------- | --- | ----------- | --- | --------- | ---- | ------ | --- | --- | --- | --- | --- | --- | --- |
etal.,2023)intheirpreferences,confusingevalua- Exam-takermodels Tounderstandthestrengths
tioncriteria(Huetal.,2024),orfocusingmoreon and weaknesses of different judges, we consider
thestyleandgrammarcomparedtofactuality(Wu answersofpre-trained(base)andinstruction-tuned
andAji,2023). Recently,Liusieetal.(2024)have (chat) ‘exam-taker models’ across a wide variety
shown that LLMs perform better in comparative ofmodelsizes. Inparticular,weconsiderLlama-2
assessment compared to absolute scoring, which (Touvronetal.,2023)in7B,13B,and70Bparam-
canbeusedforreliablymeasuringtherelativeper- etersizesforbothbaseandchatversions,Mistral
406

|     |     | 25  |     |     |     | 25  |     |     |     |               |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |
|     | 25  |     |     |     |     | 25  |     |     |     |               |     |
|     |     |     |     |     |     |     |     |     |     | Judges Judges |     |
)₅gol( erocS noitaulavE atleD 5 )₅gol( erocS noitaulavE atleD 5 5 5 EM EM
Contains Contains
Gemma-2B Gemma-2B
|     | 1   | 1   |     |     |     | 1 1 |     |     |     | Llama2-7B Llama2-7B |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------- | --- |
Llama2-13B Llama2-13B
|     | 0   | 0   |     |     |     | 0 0 |     |     |     | Llama2-70B Llama2-70B |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------------- | --- |
Llama3-8B Llama3-8B
|     | -1  | -1  |     |     |     | -1 -1 |     |     |     | Llama3-70B Llama3-70B |     |
| --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --------------------- | --- |
Llama3.1-8B Llama3.1-8B
Llama3.1-70B Llama3.1-70B
Mistral-7B Mistral-7B
|     | -5  | -5  |     |     |     | -5 -5 |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- |
JudgeLM-7B JudgeLM-7B
GPT-4 GPT-4
|     | -25 | -25 |     |     |     | -25 -25 |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------- | --- | --- | --- | --- | --- |
0 0 20 20 40 40 60 60 80 80 100 1000 0 20 20 40 40 60 60 80 80 100 100
|     |     |     | Percentage Alignment |                      |     |     | Scott's Pi Scores |     |     |     |     |
| --- | --- | --- | -------------------- | -------------------- | --- | --- | ----------------- | --- | --- | --- | --- |
|     |     |     |                      | Percentage Alignment |     |     | Scott's Pi Scores |     |     |     |     |
Figure2: Differencewithhumanevaluationscoresversusalignmentmetric. Thedeltaevaluationscoreisthe
differencebetweenthejudgeandthehumanscore;y-axesareinlogscale. Percentalignment(left)showsavery
skewweddistribution,makingitdifficulttodistinguishmodels. Scott’sπ(left)providesaclearerdifferencebetween
models,andismoreindicativeofdeviationofthegoldscore.
7B(Jiangetal.,2023)baseandchatversions,and Baselines As baselines, we use two commonly
Turbo1
GPT-4 (Achiametal.,2023)astheexam- used lexical evaluation techniques – exact match
takermodels. Thepromptsfortheexam-takermod- (EM)andcontainsmatch(contains). ForEM,are-
els contain five few-shot examples of (question, sponseisconsideredcorrectiftheresponseexactly
answer)pairsfromtheTriviaQAtrainingset. The matchesoneofthereferenceanswersforthegiven
promptsfortheinstruction-tunedmodelsaddition- question. Forcontains,ananswerisconsidered
ally include a command signaling the model to correct if at least one of the reference answers is
answer the given question in a succinct manner asub-stringoftheresponsestring. BothEMand
similartotheprovidedexamples. Thepromptsare containsmatcharecomputedinacase-insensitive
| providedinAppendixD. |     |        |     |       |               |      | manner.      |                                 |         |           |     |
| -------------------- | --- | ------ | --- | ----- | ------------- | ---- | ------------ | ------------------------------- | ------- | --------- | --- |
|                      |     |        |     |       |               |      | Alignment    | Weusetwometricstoquantifyalign- |         |           |     |
| Judge                |     | models | To  | get a | comprehensive | view |              |                                 |         |           |     |
|                      |     |        |     |       |               |      | ment between | judges:                         | percent | agreement | and |
of the strengths and weaknesses of judge mod- Scott’sPicoefficient(Scott,1955).2 Percentagree-
elsacrossdifferentmodelsizesandarchitectures,
mentexpressesasimplepercentageofthesamples
| we       | use | instruction-tuned |            |     | versions | of Llama-2 |                            |                    |     |                   |               |
| -------- | --- | ----------------- | ---------- | --- | -------- | ---------- | -------------------------- | ------------------ | --- | ----------------- | ------------- |
|          |     |                   |            |     |          |            | onwhichtwoannotatorsagree. |                    |     | Scott’sPi,denoted |               |
| (Touvron |     | et                | al., 2023) | in  | 7B, 13B, | and 70B    |                            |                    |     |                   |               |
|          |     |                   |            |     |          |            | as Scott’s                 | π, is an alignment |     | metric            | that corrects |
Llama-3
sizes, (AI@Meta, 2024) in 8B and 70B forchanceagreementbetweentwoannotatorsand
| sizes, | Llama-3.1 |     | (Dubey |     | et al., | 2024) in 8B |     |     |     |     |     |
| ------ | --------- | --- | ------ | --- | ------- | ----------- | --- | --- | --- | --- | --- |
isconsideredtoprovideamorerobustmeasureof
| and | 70B | sizes, | Mistral | 7B  | (Jiang | et al., 2023), |            |                                  |     |     |     |
| --- | --- | ------ | ------- | --- | ------ | -------------- | ---------- | -------------------------------- | --- | --- | --- |
|     |     |        |         |     |        |                | alignment. | Detailsaboutthecomputationofboth |     |     |     |
GPT-4 Turbo (Achiam et al., 2023), Gemma 2B metricsaregiveninAppendixF.
| (GemmaTeametal.,2024),andJudgeLM |     |     |     |     |     | 7B(Zhu |     |     |     |     |     |
| -------------------------------- | --- | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- |
etal.,2023)asjudges. Tomaintainparitywithhu- Human judgements As a ground-truth assess-
manandjudgeevaluation,judgepromptswerebuilt ment,weobtainhumanannotationsforeachexam-
fromhumanguidelinesinAppendixG.Thejudges
|     |     |     |     |     |     |     | taker model | answer. The | inter-human |     | alignment |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ----------- | ----------- | --- | --------- |
areinstructedtorespondwithonlyasingleword, is calculated between three human judges using
“correct” or “incorrect”. An overview of all theanswersto1200randomlysampledquestions
exam-takermodelsandjudgemodelsisshownin answers;thehumanguidelinescanbefoundinAp-
Table1. Foreaseofreading,thejudge modelsare pendix G. We then determine collective “Human
| depicted |     | in a | different | font | than the | exam-taker |     |     |     |     |     |
| -------- | --- | ---- | --------- | ---- | -------- | ---------- | --- | --- | --- | --- | --- |
2Inanearlierversionofthispaper,weusedCohen’skappa
models.
|     |     |     |     |     |     |     | (Cohen,1960)tomeasurealignment. |     |     | Ithassincecometo |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------------- | --- | --- | ---------------- | --- |
ourattentionthat–despiteit’swidespreaduse–thismetric
hassomewell-documentedtheoreticalissues(e.g.Pontiusand
1AccessedviatheOpenAIAPIbetweenMar19th,2024 Millones,2011;Chiccoetal.,2021).Fortheinterestedreader,
| andSep20,2024. |     |     |     |     |     |     | weelaborateontheseissuesinAppendixB. |     |     |     |     |
| -------------- | --- | --- | --- | --- | --- | --- | ------------------------------------ | --- | --- | --- | --- |
407

MistralLlama3.1JudgeLM Llama3
HumanContainsGPT-4 7B 70B 7B 70B EM
1
2
3
4
5
6
7
8
9
knaR
Judges
Llama3-70B 68.87% 26.65%
Llama3.1-70B 68.26% 27.29%
GPT-4 66.93% 28.54%
Llama3.1-8B 66.87% 24.65%
Llama2-13B 67.48% 23.31% 6.90%
Llama2-70B 69.46% 20.22% 9.99%
Mistral-7B 69.15% 19.50% 10.71%
JudgeLM-7B 66.06% 21.72% 8.48%
Contains 54.74% 29.96% 15.05%
Llama3-8B 69.54% 16.75% 13.46%
Llama2-7B 68.68% 13.91% 16.30%
Exam Taker Models
GPT-4 Llama2-13B Base Llama2-70B FT EM 40.58% 30.21% 29.21%
Llama2-7B Base Llama2-13B FT Mistral 7B Gemma-2B 56.86% 15.24% 12.93% 14.97%
Llama2-7B FT Llama2-70B Base Mistral-7B FT
True Positive True Negative False Negative False Positive
(a) (b)
Figure3:Judgerankingsandtrue/falsepositivesandnegatives.(a)Assignedexam-takermodelrankingsassigned
byhighlyhumanalignedjudges. Containsstayscloselytohuman-assignedrankings, aswellasGPT-4Turbo
andMistral 7B.(b)Falsepositivesandnegativesacrossdifferentjudgemodels,indescendingorderofhuman
alignment. Bothfalsenegativesandfalsepositivesincreaseashumanalignmentdecreases,butwell-alignedmodels
tendtoproducemorefalsepositivesthanfalsenegatives.
Judgment”throughamajorityvote. 4.1 Alignmentbetweenjudgemodelsand
Theaveragealignmentbetweenhumanevalua- humans
tors and the majority vote yielded a Scott’s π of
We start by computing Scott’s π scores and per-
96.2±1.07,3 whiletheaveragepercentageagree-
cent agreement between the evaluations of each
ment was 98.52%±0.42%, exceeding the align-
judgemodelandthehumanannotators. Weshow
ment previously reported in comparable studies
the result in Figure 1. We observe that percent
(Zengetal.,2024).
alignment is high for virtually all models, with
The details of this experiment are mentioned
the exception of Gemma 2B and EM. Scott’s π, on
inAppendixA.Giventhisnear-perfectalignment
the other hand, has low values for most models,
score,weconsideronlyonehumanevaluatorper
thoughitsvalueisinthehigh80sforLlama-3 70B,
sample for the rest of our experiments, to reduce
Llama-3.1 70B and GPT-4 Turbo. Nevertheless,
theoverallcostofhumanannotations. Thesetof
therestillisasignificantdisparitybetweenhuman
questionsforwhichweobtainhumanannotations
judgmentandjudgemodels: thebestscoringjudge,
isidenticalforeachexam-takermodel.
Llama-3 70B,is8pointsbehindhumanjudgment.
Notably, EM has the most variance in alignment,
4 Results whileGemma 2Bhasthelowestalignmentamongst
alljudges.
Inthissectionwediscussourmainresults,primar- In most cases, we observe that Scott’s π and
ily focusing on the relationship between evalua- percent agreement are following the same trend,
tions by various judge models and human evalu- withtheexceptionofthevaluesforGemma 2Band
ations (§ 4.1), and how that impacts their usabil- EM.Gemma 2Bshowshigherpercentagreementcom-
ity(§4.2). Todoso,weevaluatetheiralignment paredtoEM,yetityieldsthelowestScott’sπ score
with human judgment and assess how differently within the ensemble. For the percent agreement
they rank the nine exam-taker models compared of judge models, we note a 26-point difference
tohumans. InSection5,wefurtheranalysetheir between human judgment and EM, while Scott’s
precisionandrecalltofurtherinvestigatethetypes π exhibits a more substantial 64-point gap. This
oferrorsthatcanbemadebyvariousjudgemod- isalsovisibleinthegeneraldeclineofalignment
els. Detailsaboutcomputerequirementsandothers scores: whileLlama-3 8BhasaScott’sπ scoreof
costsforexperimentsaregiveninAppendixH. only 59, its percent agreement is still well above
80%. Overall, Scott’sπ appearstobebetterable
of discriminating various judge models, showing
3Thecoefficientisscaledby100foreasiercomparison
withpercentagealignment. moredivergenceacrossthetestedjudges.
408

|     |     |     |     |     |     |     | 5 Analysis |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- |
Tounderstandhowindicativethetwoalignment
metricsareoftheexpectedaccuracyoftheoverall
Tobetterunderstandthejudgemodels,weconduct
judgementofthemodels,weplot,foreachjudge
multiplecasestudiesaimedatidentifyingcommon
| model | and exam-taker |     | model, | the | difference | be- |            |                 |     |     |            |     |        |
| ----- | -------------- | --- | ------ | --- | ---------- | --- | ---------- | --------------- | --- | --- | ---------- | --- | ------ |
|       |                |     |        |     |            |     | errors and | vulnerabilities |     | in  | the judges | we  | inves- |
tweenthescoreassignedbythejudgeandthescore
|                   |                                  |     |                          |     |     |     | tigate.         | Specifically, | we     | study    | their    | precision   | and  |
| ----------------- | -------------------------------- | --- | ------------------------ | --- | --- | --- | --------------- | ------------- | ------ | -------- | -------- | ----------- | ---- |
| assignedbyahuman. |                                  |     | Inthefigure,wecanseethat |     |     |     |                 |               |        |          |          |             |      |
|                   |                                  |     |                          |     |     |     | recall and      | error         | types  | (§ 5.1), | their    | sensitivity | to   |
| forScott’sπ       | valueshigherthan80,theevaluation |     |                          |     |     |     |                 |               |        |          |          |             |      |
|                   |                                  |     |                          |     |     |     | the instruction |               | prompt | prompt   | (§ 5.2), | how         | they |
scoresarecomparativelyclosetothehumaneval-
|                |     |      |              |     |       |          | respond | to controlled |     | resposes | of specific |     | types |
| -------------- | --- | ---- | ------------ | --- | ----- | -------- | ------- | ------------- | --- | -------- | ----------- | --- | ----- |
| uation scores, |     | with | a difference | of  | up to | 5 points |         |               |     |          |             |     |       |
(§5.3),andtheextenttowhichtheyhavealeniency
intheirassignedscores(completeresultstablepro-
bias(§5.4).
| vided in  | Appendix |        | J). For | percent   | alignment, | on       |                          |     |     |     |              |     |     |
| --------- | -------- | ------ | ------- | --------- | ---------- | -------- | ------------------------ | --- | --- | --- | ------------ | --- | --- |
| the other | hand,    | even   | judges  | that have | more       | than     |                          |     |     |     |              |     |     |
|           |          |        |         |           |            |          | 5.1 Betteralignedmodels: |     |     |     | Precisionand |     |     |
| 90% may   | still    | differ | more    | than 10   | points     | in their |                          |     |     |     |              |     |     |
recallgainswitherrorspotlights
| assigned | score. | Interestingly, |     | the | deviation | from |          |         |     |           |     |        |        |
| -------- | ------ | -------------- | --- | --- | --------- | ---- | -------- | ------- | --- | --------- | --- | ------ | ------ |
|          |        |                |     |     |           |      | We first | examine | the | precision | and | recall | of the |
human-judgementsforasinglejudgemodelcanbe
|     |     |     |     |     |     |     | judgemodels. |     | AsshowninFigure4a,bothmetrics |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ----------------------------- | --- | --- | --- | --- |
quitedifferentdependingontheexam-takermodel.
|           |     |       |         |           |           |     | increasemoderatelywithalignment. |     |     |     |     | Figure3bre- |     |
| --------- | --- | ----- | ------- | --------- | --------- | --- | -------------------------------- | --- | --- | --- | --- | ----------- | --- |
| In Figure | 1a, | Gemma | 2B, for | instance, | sometimes |     |                                  |     |     |     |     |             |     |
vealsasimilartrend,withaclearerdistributionof
assignshigherscoresthanhumans,andsometimes
muchlower. Inthenextsection,wefurtherexplore falsepositivesandnegatives. Truepositivesremain
|     |     |     |     |     |     |     | consistent | across | varying | judge | quality, | whereas |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------ | ------- | ----- | -------- | ------- | --- |
thisparticularpattern.
truenegativesexhibitaslightdeclineasjudgequal-
|     |     |     |     |     |     |     | itydecreases. |     | Notably,areductioninjudgequality |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | -------------------------------- | --- | --- | --- | --- |
4.2 Exploringconsistentpatternsinjudge
leadstoanincreaseinfalsepositives.
models
|     |     |     |     |     |     |     | Next, | we analyze |     | the errors | made | by  | judge |
| --- | --- | --- | --- | --- | --- | --- | ----- | ---------- | --- | ---------- | ---- | --- | ----- |
In the previous section, we saw that none of the modelsbymanuallyannotating900outputsfrom
judgemodelswereasalignedwithhumansashu- Llama-7B Base, focusing on top performers
|                        |     |     |     |                   |     |     | GPT-4 TurboandLlama-3;70B.Wecategorizeer- |     |           |     |       |      |          |
| ---------------------- | --- | --- | --- | ----------------- | --- | --- | ----------------------------------------- | --- | --------- | --- | ----- | ---- | -------- |
| manswerewitheachother. |     |     |     | AsshowninFigure2, |     |     |                                           |     |           |     |       |      |          |
|                        |     |     |     |                   |     |     | ror types                                 | and | determine | how | often | they | are cor- |
eventhebest-alignedjudgemodelscandifferbyup
to5pointsfromhuman-assignedscores. Whilethis rectly judged as incorrect. The results in Table 2
limitstheirabilitytoperfectlyestimateexam-taker showthatbothGPT-4 TurboandLlama-3;70Bex-
|     |     |     |     |     |     |     | cel at identifying |     | answers | referring |     | to incorrect |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | ------- | --------- | --- | ------------ | --- |
modelcapabilities,judgemodelscanstillprovide
valuable insights to differentiate between exam- entities or containing too many entities. Under-
takermodels. Forexample,judgeswithconsistent specifiedandincorrectanswersaremorechalleng-
|            |     |        |           |        |     |       | ing, with | GPT-4 | Turbo | performing |     | better | on an- |
| ---------- | --- | ------ | --------- | ------ | --- | ----- | --------- | ----- | ----- | ---------- | --- | ------ | ------ |
| biases may | not | assign | identical | scores | but | could |           |       |       |            |     |        |        |
swerswithfewerentitiesthanLlama-3;70B.
rankmodelssimilarly,akintoaverystrictteacher.
| To assess | this, | we  | compare | the | rankings | given |                                         |     |     |     |     |     |     |
| --------- | ----- | --- | ------- | --- | -------- | ----- | --------------------------------------- | --- | --- | --- | --- | --- | --- |
|           |       |     |         |     |          |       | 5.2 Judgemodelsensitivitytopromptlength |     |     |     |     |     |     |
byeachjudgemodeltothenineexam-takermod-
andspecificity
els,computingSpearman’srankcorrelationcoeffi-
Next,weinvestigatehowpromptlengthandspeci-
cientsρ(Spearman,1904)withthehumanranking.
The rankings are shown in Figure 3a, with ρ and ficityaffectjudgemodels’inferencestodetermine
σ valuesinAppendixL.Mostjudgemodelshave whethertheirperformanceisinfluencedbyspeci-
|     |     |     |     |     |     |     | ficityoftheprompt. |     | Weusefourpromptversions |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | ----------------------- | --- | --- | --- | --- |
rankcorrelationsabove0.7,indicatingtheystrug-
gletodistinguishpoorermodelsbutdowellwith withvaryinglengthandspecificity.
better ones. Notably, models like contains and The first two prompts
Mistral 7B, which have divergent scores from (Without;guidelines;V1/V2,45and58tokens)
|         |      |      |      |             |     |         | askforanevaluationwithoutfurtherdetails. |     |     |     |     |     | The |
| ------- | ---- | ---- | ---- | ----------- | --- | ------- | ---------------------------------------- | --- | --- | --- | --- | --- | --- |
| humans, | show | high | rank | correlation | (ρ  | of 0.99 |                                          |     |     |     |     |     |     |
and 0.98, respectively), performing similarly to longerprompts(Guidelines;without;examples
GPT-4 TurboandoutperformingthebetterLlama and Guidelines;with;examples, 245 and 301
models–thoughwithlowersignificancevalues– tokens) provide more elaborate guidance and
indicatingthatidentifyingwhichmodelsarebetter examples. AllpromptsarelistedinAppendixM.
shouldnotbeequatedtoassigningthemthecorrect Figure 4b shows that GPT-4 Turbo,
| score. |     |     |     |     |     |     | Llama-3;70B, |     | and | Llama-3.1;70B |     |     | exhibit |
| ------ | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | ------------- | --- | --- | ------- |
409

|     |     |     |     |     |     |     |     | EM  | Llama-2 7B |     | Llama3-70b |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ---------- | --- |
Precision Recall Scott's Pi Score GPT-4 Llama2 13B Llama3.1-8B
|     |     |     |     |     |     |     |     | Mistral 7B | Llama2 70B |     | LLama3.1-70B |     |
| --- | --- | --- | --- | --- | --- | --- | --- | ---------- | ---------- | --- | ------------ | --- |
100%
1.0
| 90% |     |     |     |     |     |     | 0.9 |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
80%
0.8
70%
iP s'ttocS 0.7
60%
| 50% |     |     |     |     |     |     | 0.6 |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
0.5
40%
| 30% |             |                              |                       |                       |                                           |     | 0.4 |     |     |     |     |     |
| --- | ----------- | ---------------------------- | --------------------- | --------------------- | ----------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
|     | B2-ammeG ME | B7-2amalL B8-3amalL sniatnoC | B7-MLegduJ B7-lartsiM | B07-2amalL B31-2amalL | B8-1.3amalL 4-TPG B07-1.3amalL B07-3amalL |     |     |     |     |     |     |     |
0.3
|     |     |     |     |     |     |     |               | 45              | 58  |            | 245 | 301        |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --------------- | --- | ---------- | --- | ---------- |
|     |     |     |     |     |     |     |               | Without Without |     | Guidelines |     | Guidelines |
|     |     |     |     |     |     |     | Guidelines V1 | Guidelines V2   |     | Without    |     | With       |
|     |     |     |     |     |     |     |               |                 |     | Examples   |     | Examples   |
Judges
|     |     |     | (a) |     |     |     |     |     | (b) |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Figure 4: Precision, recall and prompt sensitivity. (a) Recall and precision improve with increasing human
alignment(R2=0.31andR2=0.21,respectively). (b)Scott’sπscoresforjudgesacrossdifferentinstructions.
Errorcode Explanation Example Proportion GPT-4recall Llama-370Brecall
|     |     |     |     |     | Henry VII, | James I, | Edward | VI, |     |     |     |     |
| --- | --- | --- | --- | --- | ---------- | -------- | ------ | --- | --- | --- | --- | --- |
Incorrectentity Responsereferstoawrongentity 86.9% 98.3% 96.6%
|                 |     |                          |     |     | Mary I and | Elizabeth   | I       |       |       |     |       |     |
| --------------- | --- | ------------------------ | --- | --- | ---------- | ----------- | ------- | ----- | ----- | --- | ----- | --- |
|                 |     | Responsecontainsonlypart |     |     | Henry VII, | Henry VIII, | Edward, |       |       |     |       |     |
| Under-specified |     |                          |     |     |            |             |         | 37.3% | 33.9% |     | 23.3% |     |
|                 |     | oftheanswer              |     |     | Mary, and  | Elizabeth   |         |       |       |     |       |     |
|                 |     |                          |     |     | Henry VII, | Edward      | VI,     |       |       |     |       |     |
Toofewentities Responsecontainstoofewentities 2.47% 80.0% 60.0%
|     |     |     |     |     | Mary I and | James I     |        |     |     |     |     |     |
| --- | --- | --- | --- | --- | ---------- | ----------- | ------ | --- | --- | --- | --- | --- |
|     |     |     |     |     | Henry VII, | Henry VIII, | Edward | VI, |     |     |     |     |
Toomanyentities Responsecontainstoomanyentities Mary I, James I, and Elizabeth I 2.7% 90.1% 90.1%
|     |     | Responseisincorrectbutcannot |     |     | I’m sorry | but I do | not know | the |     |     |     |     |
| --- | --- | ---------------------------- | --- | --- | --------- | -------- | -------- | --- | --- | --- | --- | --- |
Other beputintoanyoftheabovebuckets answer to that question 1.23% 20.0% 40.0%
Table2: ErroranalysisforGPT-4andLlama-3 70Bjudges. Theexamplequestionis“ExcludingLadyJaneGrey,
whowerethefivemonarchsoftheHouseofTudor?”,thecorrectanswer“HenryVII,HenryVIII,EdwardVI,Mary
IandElizabethI”(inanyorder).
lowvarianceinhumanagreementaspromptlength test, the evaluated answer is a repetition of the
| and  | specificity | increases. | Top    | performers | show         |     | question.  |                             |     |     |     |     |
| ---- | ----------- | ---------- | ------ | ---------- | ------------ | --- | ---------- | --------------------------- | --- | --- | --- | --- |
| high | alignment   | with       | humans | even       | with minimal |     |            |                             |     |     |     |     |
|      |             |            |        |            |              |     | InFigure5, | weobservethatwhilesomejudge |     |     |     |     |
instructions,whiletheyslightlyimprovewithmore modelscorrectlyidentifyandmarkanswersascor-
detailed prompts. In contrast, other models lose rect(firsttest)orincorrect(nextthreetests),others,
| alignment | with | increased | instructions, |     | likely due |     |     |     |     |     |     |     |
| --------- | ---- | --------- | ------------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
likeLlama-2;70B,incorrectevaluatemanydummy
todifficultyprocessingcomplexinstructions. answers, despite showing high human alignment
Inafollow-upexperiment,weinvestigatetheim- on benchmark evaluations (see Figure 1b). We
pactofreferenceorder(seeAppendixN).Figure14 hypothesize that when the answers are plausible
andFigure15showsthatlargermodelsmaintain butincorrect,judgescancorrectlyidentifythemas
consistent judgments regardless of reference or- wrongbycomparingthemwiththereference. How-
der,whilesmallermodels,exceptMistral;7B,are ever,whentheanswerisunrelated(e.g.,“Yes”,and
| moresensitivetoit. |                               |              |     |           |        |     | “Sure”),judgemodelsmaymistakenlymarkthem |        |         |          |     |              |
| ------------------ | ----------------------------- | ------------ | --- | --------- | ------ | --- | ---------------------------------------- | ------ | ------- | -------- | --- | ------------ |
|                    |                               |              |     |           |        |     | as correct,                              | though | further | research |     | is needed to |
| 5.3                | Evaluatingcontrolledresponses |              |     |           |        |     | clarifythisbehavior.                     |        |         |          |     |              |
| We                 | conduct                       | simple tests | on  | the judge | models | by  |                                          |        |         |          |     |              |
5.4 Leniencybiasinjudgemodels
havingthemevaluatedummybenchmarkresponses.
Inthefirsttest,theanswerisaverbatimreference Lastly, to get a general sense of the inherent bi-
fromthedataset(alwayscorrect). Inthenextthree asesormisalignmentintheevaluationcriteriathat
tests,theanswersareincorrect. Forthesecondand mightbepresentinthejudgemodels,weestimate
thirdtests,thedummyexam-takermodelresponds if they have a positive or negative bias in their
with“Yes”,and“Sure”respectively. Inthefourth judgment. To do so, we assume that a judge as-
410

|     | egatnecreP erocS egduJ |     |     |     |     |     |     |     |     |     | Gold Answer |     |     |
| --- | ---------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- | --- |
100
Repeater
|     | 80  |     |     |     |     |     |     |     |     |     | Yes |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Sure
60
40
20
0
|     |     | ammeG | 2-amalL |            | 3-amalL | 2-amalL | lartsiM | 2-amalL | 3-amalL | 4-TPG |     |     |     |
| --- | --- | ----- | ------- | ---------- | ------- | ------- | ------- | ------- | ------- | ----- | --- | --- | --- |
|     |     | B2    | B31     | MLegduJ B7 | B8      | B7      | B7      | B07     | B07     |       |     |     |     |
Figure5: Judgeresponsestodummyanswers. Weinvestigatehowjudgemodelsrespondtodummyanswers.
judgemodelsremainrobustwhenexam-takermodelsproduceresponsesidenticaltotheprompt(‘repeater’),butare
lessrobustwhentheresponsesare"Yes"and"Sure". Evenwhentheanswermatchesoneofthereferenceanswers
verbatim(‘Goldanswer’),judgesdonotalwaysarriveatthecorrectjudgement.
signs the correct judgment (i.e. same evaluation alwaysnecessarytodiscriminatebetweenmodels.
as the ground truth) with a probability of P and While GPT-4 Turbo and Llama-3 have excellent
c
assigns the rest of the samples to be “correct” alignmentscores,simplerandmorecost-efficient
withaprobabilityP ,whichwecalltheirleniency models,likecontains,performsimilarlyinrank-
+
bias. WeestimatethevaluesofP andP fromthe ing exam-taker models, despite lower alignment
|     |     |     |     | c   | +   |     |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
benchmarkresults4 andshowtheminFigure16a. scoresandscoredeviations. Forstudiesfocusedon
We observe that P + for most models is signifi- rankingmodelsratherthanestimatingexactscores,
cantly higher than 0.5 (Figure 16b), indicating a theseapproachescanbeassuitableasmoreexpen-
| tendencyofthejudgemodelstoevaluateresponses |     |     |     |     |     |     | siveones. |     |     |     |     |     |     |
| ------------------------------------------- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- |
as“correct”whentheirevaluationcriteriaarenot Lastly,werunexperimentstoassessjudgemod-
completelyalignedwiththeprovidedinstructions.
|              |     |     |     |     |     |     | els’ sensitivity |           | to   | prompts,     | precision,    |        | recall, er- |
| ------------ | --- | --- | --- | --- | --- | --- | ---------------- | --------- | ---- | ------------ | ------------- | ------ | ----------- |
|              |     |     |     |     |     |     | ror types,       | leniency, |      | and          | vulnerability |        | to dummy    |
| 6 Conclusion |     |     |     |     |     |     | answers.         | We        | find | that smaller |               | models | are more    |
likelytojudgepositivelywhenindoubt,thatlower-
| In this | work, we | conduct | an  | extensive | study | of  |           |        |     |                 |     |     |             |
| ------- | -------- | ------- | --- | --------- | ----- | --- | --------- | ------ | --- | --------------- | --- | --- | ----------- |
|         |          |         |     |           |       |     | alignment | models |     | lack precision, |     | and | that better |
LLMsasjudges,comparingthemtohumanjudges
|                                |     |     |     |              |     |     | models | are | more robust | across | different |     | prompts |
| ------------------------------ | --- | --- | --- | ------------ | --- | --- | ------ | --- | ----------- | ------ | --------- | --- | ------- |
| andautomatedevaluationmethods. |     |     |     | Byfocusingon |     |     |        |     |             |        |           |     |         |
butharderto"steer."Somejudgemodelsareeasily
acleanevaluationscenariowithhighinter-human
fooledbydummyanswerslike”Yes”and”Sure”
| agreement, | we  | identify | potential | issues | with | the |     |     |     |     |     |     |     |
| ---------- | --- | -------- | --------- | ------ | ---- | --- | --- | --- | --- | --- | --- | --- | --- |
andarebetteratdetectingcompletelyincorrectan-
LLM-as-a-judgeparadigm,separatefromtaskam-
swersthanpartiallyincorrectones.
biguity.
|     |     |     |     |     |     |     | Overall, |     | this work | contributes |     | to LLM | evalua- |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | --------- | ----------- | --- | ------ | ------- |
Wefindthatsmaller,cost-efficientmodels,like
tionbyassessingjudgesinaclearlydefinedframe-
| Mistral;7B, | are      | less   | effective      | than | larger | mod- |       |                                       |     |     |     |     |     |
| ----------- | -------- | ------ | -------------- | ---- | ------ | ---- | ----- | ------------------------------------- | --- | --- | --- | --- | --- |
|             |          |        |                |      |        |      | work. | OurresultshighlightthepotentialofLLMs |     |     |     |     |     |
| els such    | as GPT-4 | Turbo, | Llama-3.1;70B, |      |        | and  |       |                                       |     |     |     |     |     |
asjudgesbutcautionagainstblindlytrustingtheir
Llama-3;70B,whicharebetteralignedbutstillfall
|          |       |            |      |      |      |        | judgments, |     | even when | aligned | with | humans. | We  |
| -------- | ----- | ---------- | ---- | ---- | ---- | ------ | ---------- | --- | --------- | ------- | ---- | ------- | --- |
| short of | human | alignment. | Even | with | high | align- |            |     |           |         |      |         |     |
recommendcomputingbothpercentagreementand
ment,theirscorescandifferbyupto5pointsfrom
Scott’sπ,pairedwithqualitativeanalysis,toavoid
| human                                  | scores, | highlighting | the | need | for caution |     |       |            |             |     |     |          |       |
| -------------------------------------- | ------- | ------------ | --- | ---- | ----------- | --- | ----- | ---------- | ----------- | --- | --- | -------- | ----- |
|                                        |         |              |     |      |             |     | bias. | We discuss | limitations |     | in  | Appendix | A and |
| whenusingjudgesinmorecomplexscenarios. |         |              |     |      |             | We  |       |            |             |     |     |          |       |
plantoexpandourworktomorecomplexscenarios
| also note | that the | commonly |     | used metric | of  | per- |     |     |     |     |     |     |     |
| --------- | -------- | -------- | --- | ----------- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
inthefuture.
| cent aligned   | fails                           | to differentiate            |     | between | judges |     |     |     |     |     |     |     |     |
| -------------- | ------------------------------- | --------------------------- | --- | ------- | ------ | --- | --- | --- | --- | --- | --- | --- | --- |
| effectively.   | Wesuggestfutureworkadoptthemore |                             |     |         |        |     |     |     |     |     |     |     |     |
| robustScott’sπ |                                 | metricforbetterdistinction. |     |         |        |     |     |     |     |     |     |     |     |
References
Next,wenotethathighalignmentscoresarenot
JoshAchiam,StevenAdler,SandhiniAgarwal,Lama
4ThetheoreticalderivationoftheexpressionsforP and Ahmad, Ilge Akkaya, Florencia Leoni Aleman,
c
P , as well as the empirical validation for their estimated DiogoAlmeida,JankoAltenschmidt,SamAltman,
+
valuescanbefoundinAppendixO. ShyamalAnadkat,etal.2023. GPT-4technicalre-
411

port. arXivpreprintarXiv:2303.08774. Karl Cobbe, Vineet Kosaraju, Mohammad Bavarian,
MarkChen,HeewooJun,LukaszKaiser,Matthias
AI@Meta.2024. Llama3modelcard. Plappert, Jerry Tworek, Jacob Hilton, Reiichiro
Nakano,etal.2021. Trainingverifierstosolvemath
AnnaBavaresco,RaffaellaBernardi,LeonardoBerto- wordproblems. arXivpreprintarXiv:2110.14168.
lazzi, Desmond Elliott, Raquel Fernández, Albert
Gatt, Esam Ghaleb, Mario Giulianelli, Michael J. Cohen. 1960. A Coefficient of Agreement for
Hanna, Alexander Koller, André F. T. Martins, Nominal Scales. Educational and Psychological
PhilippMondorf,VeraNeplenbroek,SandroPezzelle, Measurement,20(1):37.
Barbara Plank, David Schlangen, Alessandro Sug-
lia, Aditya K Surikuchi, Ece Takmaz, and Alberto AbhimanyuDubey,AbhinavJauhri,AbhinavPandey,
Testoni. 2024. Llms instead of human judges? a AbhishekKadian,AhmadAl-Dahle,AieshaLetman,
largescaleempiricalstudyacross20nlpevaluation Akhil Mathur, Alan Schelten, Amy Yang, Angela
tasks. Preprint,arXiv:2406.18403. Fan,AnirudhGoyal,AnthonyHartshorn,AoboYang,
ArchiMitra, ArchieSravankumar, ArtemKorenev,
EdwardBeeching,ClémentineFourrier,NathanHabib, ArthurHinsvark,ArunRao,AstonZhang,Aurelien
SheonHan,NathanLambert,NazneenRajani,Omar Rodriguez, Austen Gregerson, Ava Spataru, Bap-
Sanseviero,LewisTunstall,andThomasWolf.2023. tiste Roziere, Bethany Biron, Binh Tang, Bobbie
Openllmleaderboard. https://huggingface.co/ Chern,CharlotteCaucheteux,ChayaNayak,Chloe
spaces/HuggingFaceH4/open_llm_leaderboard. Bi,ChrisMarra,ChrisMcConnell,ChristianKeller,
Christophe Touret, Chunyang Wu, Corinne Wong,
YoussefBenchekroun, MegiDervishi, MarkIbrahim, CristianCantonFerrer,CyrusNikolaidis,DamienAl-
Jean-BaptisteGaya,XavierMartinet,GrégoireMi- lonsius,DanielSong,DaniellePintz,DannyLivshits,
alon,ThomasScialom,EmmanuelDupoux,Dieuwke David Esiobu, Dhruv Choudhary, Dhruv Mahajan,
Hupkes,andPascalVincent.2023. Worldsense: A DiegoGarcia-Olano,DiegoPerino,DieuwkeHupkes,
syntheticbenchmarkforgroundedreasoninginlarge EgorLakomkin,EhabAlBadawy,ElinaLobanova,
languagemodels. arXivpreprintarXiv:2311.15930. EmilyDinan,EricMichaelSmith,FilipRadenovic,
FrankZhang,GabrielSynnaeve,GabrielleLee,Geor-
TomB.Brown,BenjaminMann,NickRyder,Melanie gia Lewis Anderson, Graeme Nail, Gregoire Mi-
Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind alon,GuanPang,GuillemCucurell,HaileyNguyen,
Neelakantan,PranavShyam,GirishSastry,Amanda Hannah Korevaar, Hu Xu, Hugo Touvron, Iliyan
Askell, Sandhini Agarwal, Ariel Herbert-Voss, Zarov,ImanolArrietaIbarra,IsabelKloumann,Ishan
Gretchen Krueger, Tom Henighan, Rewon Child, Misra,IvanEvtimov,JadeCopet,JaewonLee,Jan
Aditya Ramesh, Daniel M. Ziegler, Jeffrey Wu, Geffert,JanaVranes,JasonPark,JayMahadeokar,
Clemens Winter, Christopher Hesse, Mark Chen, Jeet Shah, Jelmer van der Linde, Jennifer Billock,
EricSigler,MateuszLitwin,ScottGray,Benjamin Jenny Hong, Jenya Lee, Jeremy Fu, Jianfeng Chi,
Chess, Jack Clark, Christopher Berner, Sam Mc- Jianyu Huang, Jiawen Liu, Jie Wang, Jiecao Yu,
Candlish, AlecRadford, IlyaSutskever, andDario Joanna Bitton, Joe Spisak, Jongsoo Park, Joseph
Amodei.2020. Languagemodelsarefew-shotlearn- Rocca, Joshua Johnstun, Joshua Saxe, Junteng Jia,
ers. Preprint,arXiv:2005.14165. Kalyan Vasuden Alwala, Kartikeya Upasani, Kate
Plawiak, Ke Li, Kenneth Heafield, Kevin Stone,
Yupeng Chang, Xu Wang, Jindong Wang, Yuan Wu, KhalidEl-Arini,KrithikaIyer,KshitizMalik,Kuen-
Linyi Yang, Kaijie Zhu, Hao Chen, Xiaoyuan leyChiu,KunalBhalla,LaurenRantala-Yeary,Lau-
Yi, Cunxiang Wang, Yidong Wang, et al. 2023. rensvanderMaaten,LawrenceChen,LiangTan,Liz
A survey on evaluation of large language mod- Jenkins,LouisMartin,LovishMadaan,LuboMalo,
els. ACM Transactions on Intelligent Systems and Lukas Blecher, Lukas Landzaat, Luke de Oliveira,
Technology. MadelineMuzzi,MaheshPasupuleti,MannatSingh,
Manohar Paluri, Marcin Kardas, Mathew Oldham,
Cheng-HanChiangandHung-yiLee.2023. Canlarge Mathieu Rita, Maya Pavlova, Melanie Kambadur,
languagemodelsbeanalternativetohumanevalua- Mike Lewis, Min Si, Mitesh Kumar Singh, Mona
tions? arXivpreprintarXiv:2305.01937. Hassan,NamanGoyal,NarjesTorabi,NikolayBash-
lykov,NikolayBogoychev,NiladriChatterji,Olivier
Wei-LinChiang,LianminZheng,YingSheng,Anasta- Duchenne,OnurÇelebi,PatrickAlrassy,Pengchuan
siosNikolasAngelopoulos,TianleLi,DachengLi, Zhang, Pengwei Li, Petar Vasic, Peter Weng, Pra-
HaoZhang,BanghuaZhu,MichaelJordan,JosephE. jjwal Bhargava, Pratik Dubal, Praveen Krishnan,
Gonzalez,andIonStoica.2024. Chatbotarena: An Punit Singh Koura, Puxin Xu, Qing He, Qingxiao
openplatformforevaluatingLLMsbyhumanprefer- Dong,RagavanSrinivasan,RajGanapathy,Ramon
ence. Preprint,arXiv:2403.04132. Calderer, Ricardo Silveira Cabral, Robert Stojnic,
Roberta Raileanu, Rohit Girdhar, Rohit Patel, Ro-
DavideChicco,MatthijsJ.Warrens,andGiuseppeJu- mainSauvestre,RonniePolidoro,RoshanSumbaly,
rman. 2021. The matthews correlation coefficient RossTaylor,RuanSilva,RuiHou,RuiWang,Saghar
(mcc) is more informative than cohen’s kappa and Hosseini, Sahana Chennabasappa, Sanjay Singh,
brierscoreinbinaryclassificationassessment. ieee Sean Bell, Seohyun Sonia Kim, Sergey Edunov,
access,9:78368–78381. Shaoliang Nie, Sharan Narang, Sharath Raparthy,
412

Sheng Shen, Shengye Wan, Shruti Bhosale, Shun Yu, Liron Moshkovich, Luca Wehrstedt, Madian
Zhang,SimonVandenhende,SoumyaBatra,Spencer Khabsa,ManavAvalani,ManishBhatt,MariaTsim-
Whitman,StenSootla,StephaneCollot,SuchinGu- poukelli,MartynasMankus,MatanHasson,Matthew
rurangan,SydneyBorodinsky,TamarHerman,Tara Lennie, Matthias Reso, Maxim Groshev, Maxim
Fowler,TarekSheasha,ThomasGeorgiou,Thomas Naumov,MayaLathi,MeghanKeneally,MichaelL.
Scialom,TobiasSpeckbacher,TodorMihaylov,Tong Seltzer, Michal Valko, Michelle Restrepo, Mihir
Xiao, Ujjwal Karn, Vedanuj Goswami, Vibhor Patel, Mik Vyatskov, Mikayel Samvelyan, Mike
Gupta,VigneshRamanathan,ViktorKerkez,Vincent Clark,MikeMacey,MikeWang,MiquelJubertHer-
Gonguet, Virginie Do, Vish Vogeti, Vladan Petro- moso, Mo Metanat, Mohammad Rastegari, Mun-
vic,WeiweiChu,WenhanXiong,WenyinFu,Whit- ish Bansal, Nandhini Santhanam, Natascha Parks,
neyMeers,XavierMartinet,XiaodongWang,Xiao- NatashaWhite,NavyataBawa,NayanSinghal,Nick
qing Ellen Tan, Xinfeng Xie, Xuchao Jia, Xuewei Egebo,NicolasUsunier,NikolayPavlovichLaptev,
Wang, Yaelle Goldschlag, Yashesh Gaur, Yasmine Ning Dong, Ning Zhang, Norman Cheng, Oleg
Babaei, YiWen, YiwenSong, YuchenZhang, Yue Chernoguz, Olivia Hart, Omkar Salpekar, Ozlem
Li,YuningMao,ZacharieDelpierreCoudert,Zheng Kalinli, Parkin Kent, Parth Parekh, Paul Saab, Pa-
Yan,ZhengxingChen,ZoePapakipos,AadityaSingh, van Balaji, Pedro Rittner, Philip Bontrager, Pierre
AaronGrattafiori,AbhaJain,AdamKelsey,Adam Roux,PiotrDollar,PolinaZvyagina,PrashantRatan-
Shajnfeld,AdithyaGangidi,AdolfoVictoria,Ahuva chandani,PritishYuvraj,QianLiang,RachadAlao,
Goldstand,AjayMenon,AjaySharma,AlexBoesen- RachelRodriguez, RafiAyub, RaghothamMurthy,
berg,AlexVaughan,AlexeiBaevski,AllieFeinstein, RaghuNayani,RahulMitra,RaymondLi,Rebekkah
Amanda Kallet, Amit Sangani, Anam Yunus, An- Hogan, Robin Battey, Rocky Wang, Rohan Mah-
drei Lupu, Andres Alvarado, Andrew Caples, An- eswari,RussHowes,RutyRinott,SaiJayeshBondu,
drew Gu, Andrew Ho, Andrew Poulton, Andrew Samyak Datta, Sara Chugh, Sara Hunt, Sargun
Ryan, Ankit Ramchandani, Annie Franco, Apara- Dhillon,SashaSidorov,SatadruPan,SaurabhVerma,
jitaSaraf,ArkabandhuChowdhury,AshleyGabriel, SeijiYamamoto,SharadhRamaswamy,ShaunLind-
Ashwin Bharambe, Assaf Eisenman, Azadeh Yaz- say, Shaun Lindsay, Sheng Feng, Shenghao Lin,
dan,BeauJames,BenMaurer,BenjaminLeonhardi, Shengxin Cindy Zha, Shiva Shankar, Shuqiang
BernieHuang,BethLoyd,BetoDePaola,Bhargavi Zhang,ShuqiangZhang,SinongWang,SnehaAgar-
Paranjape,BingLiu,BoWu,BoyuNi,BradenHan- wal, Soji Sajuyigbe, Soumith Chintala, Stephanie
cock,BramWasti,BrandonSpence,BraniStojkovic, Max,StephenChen,SteveKehoe,SteveSatterfield,
Brian Gamido, Britt Montalvo, Carl Parker, Carly Sudarshan Govindaprasad, Sumit Gupta, Sungmin
Burton,CatalinaMejia,ChanghanWang,Changkyu Cho,SunnyVirk,SurajSubramanian,SyChoudhury,
Kim, Chao Zhou, Chester Hu, Ching-Hsiang Chu, SydneyGoldman,TalRemez,TamarGlaser,Tamara
ChrisCai,ChrisTindal,ChristophFeichtenhofer,Da- Best, Thilo Kohler, Thomas Robinson, Tianhe Li,
monCivin,DanaBeaty,DanielKreymer,DanielLi, TianjunZhang,TimMatthews,TimothyChou,Tzook
DannyWyatt,DavidAdkins,DavidXu,DavideTes- Shaked, VarunVontimitta, VictoriaAjayi, Victoria
tuggine,DeliaDavid,DeviParikh,DianaLiskovich, Montanez,VijaiMohan,VinaySatishKumar,Vishal
DidemFoss,DingkangWang,DucLe,DustinHol- Mangla,VítorAlbiero,VladIonescu,VladPoenaru,
land, Edward Dowling, Eissa Jamil, Elaine Mont- VladTiberiuMihailescu, VladimirIvanov, WeiLi,
gomery,EleonoraPresani,EmilyHahn,EmilyWood, WenchenWang,WenwenJiang,WesBouaziz,Will
ErikBrinkman,EstebanArcaute,EvanDunbar,Evan Constable,XiaochengTang,XiaofangWang,Xiao-
Smothers, Fei Sun, Felix Kreuk, Feng Tian, Firat jianWu,XiaolanWang,XideXia,XilunWu,Xinbo
Ozgenel, Francesco Caggioni, Francisco Guzmán, Gao,YanjunChen,YeHu,YeJia,YeQi,YendaLi,
FrankKanayet,FrankSeide,GabrielaMedinaFlo- YilinZhang,YingZhang,YossiAdi,YoungjinNam,
rez,GabriellaSchwarz,GadaBadeer,GeorgiaSwee, Yu,Wang,YuchenHao,YundiQian,YuziHe,Zach
GilHalpern,GovindThattai,GrantHerman,Grigory Rait,ZacharyDeVito,ZefRosnbrick,ZhaoduoWen,
Sizov, Guangyi, Zhang, Guna Lakshminarayanan, ZhenyuYang,andZhiweiZhao.2024. Thellama3
HamidShojanazeri,HanZou,HannahWang,Han- herdofmodels. Preprint,arXiv:2407.21783.
wen Zha, Haroun Habeeb, Harrison Rudolph, He-
lenSuk,HenryAspegren,HunterGoldman,Ibrahim Shahul Es, Jithin James, Luis Espinosa-Anke, and
Damlaj, Igor Molybog, Igor Tufanov, Irina-Elena StevenSchockaert.2023. RAGAS:Automatedeval-
Veliche, Itai Gat, Jake Weissman, James Geboski, uationofretrievalaugmentedgeneration. Preprint,
James Kohli, Japhet Asher, Jean-Baptiste Gaya, arXiv:2309.15217.
JeffMarcus,JeffTang,JenniferChan,JennyZhen,
JeremyReizenstein,JeremyTeboul,JessicaZhong, Gemma Team, Thomas Mesnard, Cassidy Hardin,
Jian Jin, Jingyi Yang, Joe Cummings, Jon Carvill, RobertDadashi,SuryaBhupatiraju,ShreyaPathak,
Jon Shepard, Jonathan McPhie, Jonathan Torres, Laurent Sifre, Morgane Rivière, Mihir Sanjay
Josh Ginsburg, Junjie Wang, Kai Wu, Kam Hou Kale,JulietteLove,PouyaTafti,LéonardHussenot,
U, Karan Saxena, Karthik Prasad, Kartikay Khan- PierGiuseppeSessa,AakankshaChowdhery,Adam
delwal, Katayoun Zand, Kathy Matosich, Kaushik Roberts, Aditya Barua, Alex Botev, Alex Castro-
Veeraraghavan, Kelly Michelena, Keqian Li, Kun Ros, Ambrose Slone, Amélie Héliou, Andrea Tac-
Huang,KunalChawla,KushalLakhotia,KyleHuang, chetti, Anna Bulanova, Antonia Paterson, Beth
Lailin Chen, Lakshya Garg, Lavender A, Leandro Tsai, Bobak Shahriari, Charline Le Lan, Christo-
Silva,LeeBell,LeiZhang,LiangpengGuo,Licheng pherA.Choquette-Choo,ClémentCrepy,DanielCer,
413

Daphne Ippolito, David Reid, Elena Buchatskaya, delasCasas,FlorianBressand,GiannaLengyel,Guil-
Eric Ni, Eric Noland, Geng Yan, George Tucker, laumeLample,LucileSaulnier,etal.2023. Mistral
George-ChristianMuraru,GrigoryRozhdestvenskiy, 7B. arXivpreprintarXiv:2310.06825.
HenrykMichalewski,IanTenney,IvanGrishchenko,
Jacob Austin, James Keeling, Jane Labanowski, MandarJoshi,EunsolChoi,DanielSWeld,andLuke
Jean-Baptiste Lespiau, Jeff Stanway, Jenny Bren- Zettlemoyer.2017. TriviaQA:Alargescaledistantly
nan,JeremyChen,JohanFerret,JustinChiu,Justin supervisedchallengedatasetforreadingcomprehen-
Mao-Jones, Katherine Lee, Kathy Yu, Katie Milli- sion. arXivpreprintarXiv:1705.03551.
| can, Lars | Lowe | Sjoesund, | Lisa | Lee, Lucas | Dixon, |     |     |     |     |     |     |     |
| --------- | ---- | --------- | ---- | ---------- | ------ | --- | --- | --- | --- | --- | --- | --- |
MachelReid,MaciejMikuła,MateoWirth,Michael Junlong Li, Shichao Sun, Weizhe Yuan, Run-Ze Fan,
Sharman, Nikolai Chinaev, Nithum Thain, Olivier Hai Zhao, and Pengfei Liu. 2023a. Generative
Bachem,OscarChang,OscarWahltinez,PaigeBai- judge for evaluating alignment. arXiv preprint
| ley, Paul | Michel, | Petko | Yotov, | Rahma Chaabouni, |     | arXiv:2310.05470. |     |     |     |     |     |     |
| --------- | ------- | ----- | ------ | ---------------- | --- | ----------------- | --- | --- | --- | --- | --- | --- |
RamonaComanescu,ReenaJana,RohanAnil,Ross
McIlroy,RuiboLiu,RyanMullins,SamuelLSmith,
|     |     |     |     |     |     | Shiyang | Li, Jun | Yan, | Hai Wang, | Zheng | Tang, | Xi- |
| --- | --- | --- | --- | --- | --- | ------- | ------- | ---- | --------- | ----- | ----- | --- |
SebastianBorgeaud,SertanGirgin,SholtoDouglas, angRen,VijaySrinivasan,andHongxiaJin.2023b.
ShreePandya,SiamakShakeri,SohamDe,TedKli- Instruction-followingevaluationthroughverbalizer
menko, Tom Hennigan, Vlad Feinberg, Wojciech manipulation. arXivpreprintarXiv:2307.10558.
| Stokowiec, | Yu  | hui Chen, | Zafarali | Ahmed, | Zhitao |     |     |     |     |     |     |     |
| ---------- | --- | --------- | -------- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- |
Gong,TrisWarkentin,LudovicPeran,MinhGiang, StephanieLin,JacobHilton,andOwainEvans.2021.
Clément Farabet, Oriol Vinyals, Jeff Dean, Koray TruthfulQA:Measuringhowmodelsmimichuman
Kavukcuoglu,DemisHassabis,ZoubinGhahramani, falsehoods. arXivpreprintarXiv:2109.07958.
| Douglas | Eck, | Joelle Barral, | Fernando | Pereira, | Eli |     |     |     |     |     |     |     |
| ------- | ---- | -------------- | -------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
Collins,ArmandJoulin,NoahFiedel,EvanSenter, YinhongLiu,HanZhou,ZhijiangGuo,EhsanShareghi,
AlekAndreev,andKathleenKenealy.2024. Gemma: IvanVulic,AnnaKorhonen,andNigelCollier.2024.
Openmodelsbasedongeminiresearchandtechnol- Aligning with human judgement: The role of pair-
ogy. Preprint,arXiv:2403.08295. wisepreferenceinlargelanguagemodelevaluators.
arXivpreprintarXiv:2403.16950.
| Rishav Hada, |     | Varun Gumma, |     | Adrian de | Wynter, |     |     |     |     |     |     |     |
| ------------ | --- | ------------ | --- | --------- | ------- | --- | --- | --- | --- | --- | --- | --- |
HarshitaDiddee,MohamedAhmed,MonojitChoud- Adian Liusie, Potsawee Manakul, and Mark Gales.
| hury,KalikaBali,andSunayanaSitaram.2023. |     |     |     |     | Are |       |     |             |             |     |           |     |
| ---------------------------------------- | --- | --- | --- | --- | --- | ----- | --- | ----------- | ----------- | --- | --------- | --- |
|                                          |     |     |     |     |     | 2024. | LLM | comparative | assessment: |     | Zero-shot |     |
largelanguagemodel-basedevaluatorsthesolution
|     |     |     |     |     |     | NLG | evaluation | through | pairwise | comparisons |     | us- |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ------- | -------- | ----------- | --- | --- |
toscalingupmultilingualevaluation? arXivpreprint ing large language models. In Proceedings of the
arXiv:2309.07462. 18th Conference of the European Chapter of the
AssociationforComputationalLinguistics(Volume
| Qianyu | He, Jie | Zeng, Wenhao |     | Huang, Lina | Chen, |     |     |     |     |     |     |     |
| ------ | ------- | ------------ | --- | ----------- | ----- | --- | --- | --- | --- | --- | --- | --- |
1: LongPapers),pages139–151,St.Julian’s,Malta.
| JinXiao, | QianxiHe, | Xunzhe | Zhou, | Jiaqing | Liang, |     |     |     |     |     |     |     |
| -------- | --------- | ------ | ----- | ------- | ------ | --- | --- | --- | --- | --- | --- | --- |
AssociationforComputationalLinguistics.
| and Yanghua |     | Xiao. 2024. | Can | large | language |     |     |     |     |     |     |     |
| ----------- | --- | ----------- | --- | ----- | -------- | --- | --- | --- | --- | --- | --- | --- |
modelsunderstandreal-worldcomplexinstructions?
|     |     |     |     |     |     | Lovish Madaan, |     | Aaditya | K. Singh, | Rylan | Schaeffer, |     |
| --- | --- | --- | --- | --- | --- | -------------- | --- | ------- | --------- | ----- | ---------- | --- |
Proceedings of the AAAI Conference on Artificial AndrewPoulton, SanmiKoyejo, PontusStenetorp,
Intelligence,38(16):18188–18196.
|     |     |     |     |     |     | SharanNarang,andDieuwkeHupkes.2024. |          |               |     |             |     | Quan- |
| --- | --- | --- | --- | --- | --- | ----------------------------------- | -------- | ------------- | --- | ----------- | --- | ----- |
|     |     |     |     |     |     | tifying                             | variance | in evaluation |     | benchmarks. |     | arXiv |
DanHendrycks,CollinBurns,StevenBasart,AndyZou,
preprintarXiv:/2406.10229.
MantasMazeika,DawnSong,andJacobSteinhardt.
2021. Measuringmassivemultitasklanguageunder-
OscarMañas,BennoKrojer,andAishwaryaAgrawal.
| standing. | Preprint,arXiv:2009.03300. |     |     |     |     |           |           |     |           |             |            |     |
| --------- | -------------------------- | --- | --- | --- | --- | --------- | --------- | --- | --------- | ----------- | ---------- | --- |
|           |                            |     |     |     |     | 2024.     | Improving |     | automatic | vqa         | evaluation | us- |
|           |                            |     |     |     |     | ing large | language  |     | models.   | Proceedings |            | of  |
XinyuHu,MingqiGao,SenHu,YangZhang,Yicheng
|       |      |                 |     |            |     | the AAAI | Conference |     | on Artificial |     | Intelligence, |     |
| ----- | ---- | --------------- | --- | ---------- | --- | -------- | ---------- | --- | ------------- | --- | ------------- | --- |
| Chen, | Teng | Xu, and Xiaojun |     | Wan. 2024. | Are |          |            |     |               |     |               |     |
38(5):4171–4179.
| LLM-based | evaluators | confusing |     | nlg quality | crite- |     |     |     |     |     |     |     |
| --------- | ---------- | --------- | --- | ----------- | ------ | --- | --- | --- | --- | --- | --- | --- |
ria? arXivpreprintarXiv:2402.12055.
XeniaOhmer,EliaBruni,andDieuwkeHupkes.2024.
Hui Huang, Yingqi Qu, Jing Liu, Muyun Yang, From form (s) to meaning: Probing the semantic
and Tiejun Zhao. 2024. An empirical study of depthsoflanguagemodelsusingmultisenseconsis-
tency. arXivpreprintarXiv:2404.12145.
| LLM-as-a-Judge                          |     | for LLM | evaluation: | Fine-tuned |           |                   |     |     |         |           |     |       |
| --------------------------------------- | --- | ------- | ----------- | ---------- | --------- | ----------------- | --- | --- | ------- | --------- | --- | ----- |
| judgemodelsaretask-specificclassifiers. |     |         |             |            | Preprint, |                   |     |     |         |           |     |       |
|                                         |     |         |             |            |           | Pouya Pezeshkpour |     | and | Estevam | Hruschka. |     | 2023. |
arXiv:2403.02839.
|     |     |     |     |     |     | Large | language | models | sensitivity | to  | the order | of  |
| --- | --- | --- | --- | --- | --- | ----- | -------- | ------ | ----------- | --- | --------- | --- |
Pranab Islam, Anand Kannappan, Douwe Kiela, Re- optionsinmultiple-choicequestions. arXivpreprint
| beccaQian,NinoScherrer,andBertieVidgen.2023. |     |                                |     |     |     | arXiv:2308.11483. |     |                                |           |           |     |       |
| -------------------------------------------- | --- | ------------------------------ | --- | --- | --- | ----------------- | --- | ------------------------------ | --------- | --------- | --- | ----- |
| FinanceBench:                                |     | Anewbenchmarkforfinancialques- |     |     |     |                   |     |                                |           |           |     |       |
|                                              |     |                                |     |     |     | Robert Gilmore    |     | Pontius                        | and Marco | Millones. |     | 2011. |
| tionanswering.                               |     | arXivpreprintarXiv:2311.11944. |     |     |     |                   |     |                                |           |           |     |       |
|                                              |     |                                |     |     |     | Deathtokappa:     |     | birthofquantitydisagreementand |           |           |     |       |
Albert Q Jiang, Alexandre Sablayrolles, Arthur Men- allocationdisagreementforaccuracyassessment. Int.
sch,ChrisBamford,DevendraSinghChaplot,Diego J.RemoteSens.,32(15):4407–4429.
414

AlecRadford,JeffreyWu,RewonChild,DavidLuan, ZhiyuanZeng,JiatongYu,TianyuGao,YuMeng,Tanya
DarioAmodei,IlyaSutskever,etal.2019. Language Goyal, and Danqi Chen. 2024. Evaluating large
modelsareunsupervisedmultitasklearners. OpenAI languagemodelsatevaluatinginstructionfollowing.
| blog,1(8):9. |     |     |     |     |     |     | Preprint,arXiv:2310.07641. |     |     |     |     |
| ------------ | --- | --- | --- | --- | --- | --- | -------------------------- | --- | --- | --- | --- |
Matthew Renze and Erhan Guven. 2024. The ben- YueZhang,MingZhang,HaipengYuan,ShichunLiu,
efits of a concise chain of thought on problem- Yongyao Shi, Tao Gui, Qi Zhang, and Xuanjing
solving in large language models. arXiv preprint Huang. 2024. Llmeval: A preliminary study on
arXiv:2401.05618. howtoevaluatelargelanguagemodels. Proceedings
|     |     |     |     |     |     |     | of the AAAI | Conference |     | on Artificial Intelligence, |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | ---------- | --- | --------------------------- | --- |
Keita Saito, Akifumi Wachi, Koki Wataoka, and 38(17):19615–19622.
| Youhei | Akimoto. | 2023. | Verbosity |     | bias in | prefer- |     |     |     |     |     |
| ------ | -------- | ----- | --------- | --- | ------- | ------- | --- | --- | --- | --- | --- |
ence labeling by large language models. Preprint, ChujieZheng,HaoZhou,FandongMeng,JieZhou,and
|     |     |     |     |     |     |     | MinlieHuang.2023. |     | Onlargelanguagemodels’se- |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | ------------------------- | --- | --- |
arXiv:2310.10076.
|                 |         |                               |         |            |         |     | lectionbiasinmulti-choicequestions. |     |     | arXivpreprint |     |
| --------------- | ------- | ----------------------------- | ------- | ---------- | ------- | --- | ----------------------------------- | --- | --- | ------------- | --- |
| W.A.Scott.1955. |         | Reliabilityofcontentanalysis: |         |            |         | The | arXiv:2309.03882.                   |     |     |               |     |
| case of         | nominal | scale                         | coding. | The Public | Opinion |     |                                     |     |     |               |     |
Quarterly,17:133–139. LianminZheng,Wei-LinChiang,YingSheng,Siyuan
|     |     |     |     |     |     |     | Zhuang, | Zhanghao | Wu, | Yonghao Zhuang, | Zi Lin, |
| --- | --- | --- | --- | --- | --- | --- | ------- | -------- | --- | --------------- | ------- |
Shreya Shankar, JD Zamfirescu-Pereira, Björn Hart- Zhuohan Li, Dacheng Li, Eric Xing, et al. 2024.
mann, Aditya G Parameswaran, and Ian Arawjo. JudgingLLM-as-a-JudgewithMT-BenchandChat-
| 2024. | Who validates |     | the validators? |     | aligning | llm- |            |     |          |                       |     |
| ----- | ------------- | --- | --------------- | --- | -------- | ---- | ---------- | --- | -------- | --------------------- | --- |
|       |               |     |                 |     |          |      | bot Arena. |     | Advances | in Neural Information |     |
assistedevaluationofllmoutputswithhumanprefer- ProcessingSystems,36.
ences. arXivpreprintarXiv:2404.12272.
YuanZhiqiang,LiuJunwei,ZiQiancheng,LiuMing-
AndreaSottana,BinLiang,KaiZou,andZhengYuan. wei, Peng Xin, Lou Yiling, et al. 2023. Evalu-
2023. Evaluation metrics in the era of gpt-4: reli- ating instruction-tuned large language models on
ablyevaluatinglargelanguagemodelsonsequence codecomprehensionandgeneration. arXive-prints
| tosequencetasks. |     | arXivpreprintarXiv:2310.13800. |     |     |     |     |     |     |     |     |     |
| ---------------- | --- | ------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
arXiv:2308.01240.
| C.Spearman.1904. |     | Theproofandmeasurementofas- |     |     |     |     |               |          |       |             |       |
| ---------------- | --- | --------------------------- | --- | --- | --- | --- | ------------- | -------- | ----- | ----------- | ----- |
|                  |     |                             |     |     |     |     | Lianghui Zhu, | Xinggang | Wang, | and Xinlong | Wang. |
sociationbetweentwothings. TheAmericanJournal 2023. Judgelm: Fine-tunedlargelanguagemodels
ofPsychology,15(1):72–101. arescalablejudges. Preprint,arXiv:2310.17631.
| Hugo Touvron, |     | Louis Martin, |         | Kevin Stone, | Peter   | Al- |     |     |     |     |     |
| ------------- | --- | ------------- | ------- | ------------ | ------- | --- | --- | --- | --- | --- | --- |
| bert, Amjad   |     | Almahairi,    | Yasmine | Babaei,      | Nikolay |     |     |     |     |     |     |
Bashlykov,SoumyaBatra,PrajjwalBhargava,Shruti
| Bhosale, | et         | al. 2023. | Llama   | 2:    | Open founda- |     |     |     |     |     |     |
| -------- | ---------- | --------- | ------- | ----- | ------------ | --- | --- | --- | --- | --- | --- |
| tion and | fine-tuned | chat      | models. | arXiv | preprint     |     |     |     |     |     |     |
arXiv:2307.09288.
MilesTurpin,JulianMichael,EthanPerez,andSamuel
| Bowman.                       | 2023. | Language |            | models             | don't always |       |     |     |     |     |     |
| ----------------------------- | ----- | -------- | ---------- | ------------------ | ------------ | ----- | --- | --- | --- | --- | --- |
| say what                      | they  | think:   | Unfaithful | explanations       |              | in    |     |     |     |     |     |
| chain-of-thoughtprompting.    |       |          |            | InAdvancesinNeural |              |       |     |     |     |     |     |
| InformationProcessingSystems, |       |          |            | volume36,          |              | pages |     |     |     |     |     |
74952–74965.CurranAssociates,Inc.
PeiyiWang,LeiLi,LiangChen,DaweiZhu,Binghuai
Lin,YunboCao,QiLiu,TianyuLiu,andZhifangSui.
2023. Largelanguagemodelsarenotfairevaluators.
arXivpreprintarXiv:2305.17926.
| MinghaoWuandAlhamFikriAji.2023. |                                         |     |     |     | Styleoversub- |     |     |     |     |     |     |
| ------------------------------- | --------------------------------------- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- |
| stance:                         | Evaluationbiasesforlargelanguagemodels. |     |     |     |               |     |     |     |     |     |     |
Preprint,arXiv:2307.03025.
| Hongbin           | Ye, Tong | Liu,     | Aijia     | Zhang, Wei | Hua, | and    |     |     |     |     |     |
| ----------------- | -------- | -------- | --------- | ---------- | ---- | ------ | --- | --- | --- | --- | --- |
| Weiqiang          | Jia.     | 2023.    | Cognitive | mirage:    | A    | review |     |     |     |     |     |
| of hallucinations |          | in large | language  | models.    |      | arXiv  |     |     |     |     |     |
preprintarXiv:2309.06794.
ZhiyuanZeng,JiatongYu,TianyuGao,YuMeng,Tanya
| Goyal, | and Danqi | Chen. | 2023. | Evaluating |     | large |     |     |     |     |     |
| ------ | --------- | ----- | ----- | ---------- | --- | ----- | --- | --- | --- | --- | --- |
languagemodelsatevaluatinginstructionfollowing.
arXivpreprintarXiv:2310.07641.
415

A Limitations
|     |     |     |     |     |     |     | Sizeofthejudgedsamples |     |     |     | Aseachofthenine |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------------- | --- | --- | --- | --------------- | --- | --- |
exam-takermodelsrequireshumanannotationsfor
| In our work, | we  | have | evaluated | how | 11 different |     |     |     |     |     |     |     |     |
| ------------ | --- | ---- | --------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
eachsample,werestrictedouranalysisto400sam-
LLMsfareasjudgesinascenarioinwhichjudge-
|     |     |     |     |     |     |     | ples in | total. | This sample |     | size | also allowed | us  |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------ | ----------- | --- | ---- | ------------ | --- |
ments should be relatively straight-forward, and toconductmanualannotationsanderroranalysis
| humanalignmentishigh. |     |     | Asanystudy,ourwork |     |     |     |           |       |           |     |     |       |          |
| --------------------- | --- | --- | ------------------ | --- | --- | --- | --------- | ----- | --------- | --- | --- | ----- | -------- |
|                       |     |     |                    |     |     |     | within 75 | human | hours/200 |     | GPU | hours | (see Ap- |
hasseverallimitationsaswellasdirectionsthatwe
|     |     |     |     |     |     |     | pendix | H) and | give | reliable | confidence |     | intervals |
| --- | --- | --- | --- | --- | --- | --- | ------ | ------ | ---- | -------- | ---------- | --- | --------- |
didnotexplorebutwouldhavebeeninterestingtoo.
|     |     |     |     |     |     |     | while also | providing |     | the flexibility |     | to compare | a   |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --------- | --- | --------------- | --- | ---------- | --- |
Inthissection,wediscussboth.
|                     |     |     |                        |     |     |     | rangeofmodels. |        | Wewerenotabletoincreasethe |       |                |          |          |
| ------------------- | --- | --- | ---------------------- | --- | --- | --- | -------------- | ------ | -------------------------- | ----- | -------------- | -------- | -------- |
|                     |     |     |                        |     |     |     | size due       | to the | cost,                      | but a | statistical    | analysis | (de-     |
| Simplicityofthetask |     |     | Asmentionedintheintro- |     |     |     |                |        |                            |       |                |          |          |
|                     |     |     |                        |     |     |     | tails provided |        | in Appendix                |       | I) illustrated |          | that the |
ductionofourwork,thescenarioinwhichjudges
variancebecauseofthissamplesizewasverylow.
areusedaretypicallymuchmorecomplicatedthan
| the scenario | that | we  | focussed | on. | Specifically, |     |                   |     |     |                           |     |     |     |
| ------------ | ---- | --- | -------- | --- | ------------- | --- | ----------------- | --- | --- | ------------------------- | --- | --- | --- |
|              |      |     |          |     |               |     | Selectionofjudges |     |     | Withourselectionofjudges, |     |     |     |
judgesaremostoftendeployedinpreferencerank-
wehavestucktoautoregressivejudgesthatcanbe
ings(wheretwomodelresponsesarecompared)or
|     |     |     |     |     |     |     | used off-the-shelve, |     |     | as well | as one | LLM | specifi- |
| --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | ------- | ------ | --- | -------- |
tojudgecomplexanswersthataredifficulttoauto-
|                 |     |                              |     |     |     |     | cally trained | to  | judge. | They | are | – at the | moment |
| --------------- | --- | ---------------------------- | --- | --- | --- | --- | ------------- | --- | ------ | ---- | --- | -------- | ------ |
| maticallyparse. |     | Insuchtasks,humanagreementis |     |     |     |     |               |     |        |      |     |          |        |
ofwriting–theonesthataremostcommonlyused
oftenlow,makingitchallengingtojudgethejudges
|             |                                  |     |     |     |     |     | as LLM-judges, |        | and      | we have | tried | to be         | compre- |
| ----------- | -------------------------------- | --- | --- | --- | --- | --- | -------------- | ------ | -------- | ------- | ----- | ------------- | ------- |
| themselves. | Inourwork,wehavedeliberatelycho- |     |     |     |     |     |                |        |          |         |       |               |         |
|             |                                  |     |     |     |     |     | hensive        | across | size and | family. |       | Nevertheless, | we      |
senforasimpletask,inwhichhumanalignmentis
|     |     |     |     |     |     |     | acknowledge |     | that there | are | other | judges | that we |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --- | ---------- | --- | ----- | ------ | ------- |
high. Themainpremiseis,thatifajudgedoesnot
|         |         |             |     |        |         |         | couldhaveconsideredaswell. |     |     |     | Asincludingmore |     |     |
| ------- | ------- | ----------- | --- | ------ | ------- | ------- | -------------------------- | --- | --- | --- | --------------- | --- | --- |
| perform | well in | this simple |     | setup, | caution | is sug- |                            |     |     |     |                 |     |     |
judgesin–comparedtoincludingmoreexam-taker
gestedalsoinmorecomplexsetups–ifsomeone
|     |     |     |     |     |     |     | models– | relatively | straightforward |     |     | because | it re- |
| --- | --- | --- | --- | --- | --- | --- | ------- | ---------- | --------------- | --- | --- | ------- | ------ |
cannotdomultiplication,whywouldtheybeable
|                                       |     |     |     |     |          |     | quires only | computational |           |        | power, | no manual | an-   |
| ------------------------------------- | --- | --- | --- | --- | -------- | --- | ----------- | ------------- | --------- | ------ | ------ | --------- | ----- |
| tosolveordinarydifferentialequations. |     |     |     |     | Giventhe |     |             |               |           |        |        |           |       |
|                                       |     |     |     |     |          |     | notation,   | we            | hope that | others | may    | evaluate  | their |
poorunderstandingofwhichabilitiesofLLMsgen-
newlyproposedjudgesusingoursetupaswell.
eraliseinwhatdimensions,however,morestudies
areneededtounderstandhowourresultsgeneralise Futurework Allinall,thesedifferencesunder-
tovariousotherscenarios.
|                |     |     |                          |     |     |     | line how | finicky | using   | LLMs | as      | judges      | can be, |
| -------------- | --- | --- | ------------------------ | --- | --- | --- | -------- | ------- | ------- | ---- | ------- | ----------- | ------- |
|                |     |     |                          |     |     |     | and with | that    | confirm | the  | overall | conclusions | of      |
| Humanalignment |     |     | Inanearlierversionofthis |     |     |     |          |         |         |      |         |             |         |
paper,duetothehighcostofhumanannotations, ourstudythatmuchmoreworkisneededtobetter
|          |           |          |     |       |           |     | understandthe |     | strengthsand |     | limitationsof |     | judge |
| -------- | --------- | -------- | --- | ----- | --------- | --- | ------------- | --- | ------------ | --- | ------------- | --- | ----- |
| we opted | to select | a single |     | model | for human | an- |               |     |              |     |               |     |       |
modelsacrossawiderangeofscenariosandmodel
notationasweiterativelymodifiedtheexamtaker
|         |          |           |     |                 |     |     | accuracies. | We  | consider |     | assessing | the | strengths |
| ------- | -------- | --------- | --- | --------------- | --- | --- | ----------- | --- | -------- | --- | --------- | --- | --------- |
| prompt, | few-shot | examples, |     | and guidelines. |     | We  |             |     |          |     |           |     |           |
acrossmultipledifferentsamplesandtasks,which
| selected | the Llama2 |     | 7B for | this purpose |     | with a |     |     |     |     |     |     |     |
| -------- | ---------- | --- | ------ | ------------ | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
wouldrequiremanymorehumanannotations,out-
| randomsampleof600questions. |     |     |     | Asthisisonlya |     |     |     |     |     |     |     |     |     |
| --------------------------- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
sidethescopeofthispaperandleavesuchexperi-
| single model, | it  | is possible |     | that our | human | align- |     |     |     |     |     |     |     |
| ------------- | --- | ----------- | --- | -------- | ----- | ------ | --- | --- | --- | --- | --- | --- | --- |
mentscoresarebiasedbecauseofthat. After,we mentationforfuturework.
| have therefore      |     | extended | our      | results | with     | another |                                     |     |     |     |     |     |     |
| ------------------- | --- | -------- | -------- | ------- | -------- | ------- | ----------------------------------- | --- | --- | --- | --- | --- | --- |
|                     |     |          |          |         |          |         | B Abriefexplanationofthetheoretical |     |     |     |     |     |     |
| 600 human-annotated |     |          | examples | from    | Llama3.1 |         |                                     |     |     |     |     |     |     |
issueswithCohen’skappa
70B.
| ForLlama2        |     | 7BTheaveragealignmentamong |           |     |            |     |         |       |             |     |         |       |      |
| ---------------- | --- | -------------------------- | --------- | --- | ---------- | --- | ------- | ----- | ----------- | --- | ------- | ----- | ---- |
|                  |     |                            |           |     |            |     | Cohen’s | Kappa | Coefficient |     | (Cohen, | 1960) | is a |
| human evaluators |     | had                        | a Scott’s |     | π of 96.36 | ±   |         |       |             |     |         |       |      |
statistictomeasureinter-rateragreementforcate-
| 1.46,and         | the | average   | percent  | agreement |       | was     |                                   |           |                             |              |     |          |          |
| ---------------- | --- | --------- | -------- | --------- | ----- | ------- | --------------------------------- | --------- | --------------------------- | ------------ | --- | -------- | -------- |
|                  |     |           |          |           |       |         | goricalresponses.                 |           | Cohen’sKappacoefficientmea- |              |     |          |          |
| 98.33%±0.76%.    |     | For       | Llama3.1 | 70B,      | we    | noted   |                                   |           |                             |              |     |          |          |
|                  |     |           |          |           |       |         | sures this                        | agreement |                             | by computing |     | the      | observed |
| that the average |     | alignment | among    |           | human | evalua- |                                   |           |                             |              |     |          |          |
|                  |     |           |          |           |       |         | (percent)agreementbetweenraters(p |           |                             |              |     | )andcom- |          |
o
| torshadScott’sπ |     | of95.78±0.30,%andtheaver- |     |     |     |     |     |     |     |     |     |     |     |
| --------------- | --- | ------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
paringitwiththehypotheticalprobabilityofchance
| agepercentagreementwas98.72%±0.10%. |     |     |     |     |     | Given |             |     |                                  |     |     |     |     |
| ----------------------------------- | --- | --- | --- | --- | --- | ----- | ----------- | --- | -------------------------------- | --- | --- | --- | --- |
|                                     |     |     |     |     |     |       | agreement(p | e   | ),whichistakenasabaseline,asfol- |     |     |     |     |
thesimilarityofthesetwonumbers,webelievethat
lows:
these1200samplesprovideanadequateestimate.
|                              |     |     |     |     |     |     |     |     |     | p o | −p e |     |     |
| ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- |
|                              |     |     |     |     |     |     |     |     | κ   | ≡   |      |     | (1) |
| Inthepaper,wetaketheaverage. |     |     |     |     |     |     |     |     |     | 1−p |      |     |     |
e
416

In this equation, the chance agremeent p con- D Modelevaluationprompttemplates
o
stitutesthehypotheticalprobabilitythatobserved
In Figure 6 and Figure 7, we show the prompt
agreementoccurredbychance,giventheobserved
templates used for the base and chat exam-taker
distributionsoftheconsideredraters,undertheas-
modelsduringthequestionansweringprocess.
sumptionthattheprobabilitiestheratersassignto
theobservedlabelsareindependent. Specifically,
E JudgeLLMPrompttemplates
itisdefinedas:
InFigure8,weshowtheprompttemplateusedto
guidethejudgemodelsduringtheevaluationpro-
(cid:88) (cid:88)
p e = p (cid:100)k12 =ind p (cid:99)k1 p (cid:99)k2 cessofa400-questionsamplefromtheTriviaQA
k k unfiltereddataset.
(cid:88) n k1 n k2 1 (cid:88)
= · = n n
N N N2 k1 k2 F Metricsforjudgemodels
k k
If one of the annotators is taken to be the refer-
wherep istheestimatedprobabilitythatrater
(cid:100)k12 ence, then the annotations of the other annotator
1andrater2willclassifythesameitemask,rewrit-
canbecategorizedastruepositives,falsepositives,
tentop p undertheassumptionthatp andp
(cid:99)k1(cid:99)k2 k1 k2 true negatives, and false negatives, with the total
are independent. The crux of the issue with this
numberofeachoftheminabenchmarkbeingrep-
methodofcomputation,isthatp andp arees-
(cid:99)k1 (cid:99)k2 resentedbyT ,F ,T ,andF respectively.
P P N N
timatedindependentlyfromthedata. Assuch,the
Percent agreement is simply the ratio of the
chanceagreementadjustsfortheobservedaverage
numbersoftimestwoannotatorsagreewitheach
differencesbetweenraters,whichisinfactpartof
other relative to the total number of annotations.
whatweintendtomeasure.
Thisratiocanhavevaluesbetween0and1. Forthe
To address this issue, Scott’s Pi (Scott, 1955)
binarycase,thealignmentratioρisgivenas
instead defines the chance baseline under the as-
sumptionthattheratershavethesamedistribution, T +T
P N
ρ = . (3)
which is estimated considering the joint distribu- T +F +T +F
P P N N
tionofrater1andrater2,ratherthanconsidering
Scott’sPi,(Scott,1955),measuresthealignment
themseparately. Itdefinesp as:
e of two annotators while also taking into account
thepossibilityofagreementbypurechance. This
coefficientusuallyhasvaluesabove0inmostreal-
p e = (cid:88) p(cid:98)2 k = (cid:88)(cid:88) ( n k1 2 + N n k2 )2 (2) world situations. The value of Scott’s Pi is given
k k k belowwherep istherelativeobservedagreement,
o
and p is the hypothetical probability of chance
e
Assuch,contrarytoCohen’sKappa,itcaptures
agreement.
differencessurpassingthechanceagreementifrater
1 and rater 2 were in fact equivalent. In other
words, we compare against a baseline in which
raters would be equivalent, and we measure how
muchtheydeviatefromthat.
Note that if the empirical distributions of rater
1 and rater 2 are the same, so will the values of
Scott’sPiandCohen’sKappabe. Thisalsoimplies
thatforlargerobserved(percent)alignmentvalues,
the values for Cohen’s Kappa and Scott’s Pi will
becloser.
C Modelanddatasetdetails
InAppendixC,weshowthedifferentmodelsand
datasets used in our experiments, along with ver-
sionandlicensedetails.
417

| Prompt template for B  |     |     |     | models  |     |     |     |     |
| ---------------------- | --- | --- | --- | ------- | --- | --- | --- | --- |
exam:
| Q:  Can    | you  name  | the      | actress  | who  links  | ’The  | Darling  | Buds  | of  May’  and  |
| ---------- | ---------- | -------- | -------- | ----------- | ----- | -------- | ----- | -------------- |
| *Rosemary  | and        | Thyme’?  |          |             |       |          |       |                |
A:  Pam  Ferris
| Q:  A  neologism  |     | is  a  | new?  |     |     |     |     |     |
| ----------------- | --- | ------ | ----- | --- | --- | --- | --- | --- |
A:  Word/expression
| Q:  Who,       | in  2010,  | became         | the      | first  person  | from    | outside   | the           | British      |
| -------------- | ---------- | -------------- | -------- | -------------- | ------- | --------- | ------------- | ------------ |
| Isles  to      | win        | the  World     | Snooker  | Championship   |         | title     | since  Cliff  | Thorburn     |
| in  1980,      | and        | the  first     | non      | British        | player  | to  win   | the  title    | since  Ken   |
| Doherty        | in  19977  |                |          |                |         |           |               |              |
| A:  Neil       | Robertson  |                |          |                |         |           |               |              |
| Q:  Which      | German     | Nazi           | leader   | flew  solo     | from    | Ausberg   | in  1941      | and  landed  |
| by  parachute  |            | near  Glasgow  | on       | a  private     | peace   | mission?  |               |              |
A:  Hess
| Q:  Where     | would    | you  find  | Narita                                | airport?  |            |         |          |           |
| ------------- | -------- | ---------- | ------------------------------------- | --------- | ---------- | ------- | -------- | --------- |
| A:  Tokyo,    | Japan    |            |                                       |           |            |         |          |           |
|  oP :  Which  | cartoon  | title      | character                             | has       | a  friend  | called  | Captain  | Haddock?  |
|               | Figure6: |            | Prompttemplateforbaseexam-takermodels |           |            |         |          |           |
Prompt template for Chat exam-taker models
| You  are   | a  part    | of  a    | question  | answering   | benchmark.      |          | Look  | at  the        |
| ---------- | ---------- | -------- | --------- | ----------- | --------------- | -------- | ----- | -------------- |
| following  | examples   | on       | how  to   | answer      | the  questions  |          |       |                |
| Q:  Can    | you  name  | the      | actress   | who  links  | ’The            | Darling  | Buds  | of  May’  and  |
| *Rosemary  | and        | Thyme’?  |           |             |                 |          |       |                |
A:  Pam  Ferris
| Q:  A  neologism  |     | is  a  | new?  |     |     |     |     |     |
| ----------------- | --- | ------ | ----- | --- | --- | --- | --- | --- |
A:  Word/expression
| Q:  Who,  | in  2010,  | became  | the  | first  person  |     | from  outside  | the  | British  |
| --------- | ---------- | ------- | ---- | -------------- | --- | -------------- | ---- | -------- |
Isles  to  win  the  World  Snooker  Championship  title  since  Cliff  Thorburn
| in  1980,      | and        | the  first     | non     | British     | player  | to  win   | the  title  | since  Ken   |
| -------------- | ---------- | -------------- | ------- | ----------- | ------- | --------- | ----------- | ------------ |
| Doherty        | in  19977  |                |         |             |         |           |             |              |
| A:  Neil       | Robertson  |                |         |             |         |           |             |              |
| Q:  Which      | German     | Nazi           | leader  | flew  solo  | from    | Ausberg   | in  1941    | and  landed  |
| by  parachute  |            | near  Glasgow  | on      | a  private  | peace   | mission?  |             |              |
A:  Hess
| Q:  Where   | would  | you  find  | Narita  | airport?  |     |     |     |     |
| ----------- | ------ | ---------- | ------- | --------- | --- | --- | --- | --- |
| A:  Tokyo,  | Japan  |            |         |           |     |     |     |     |
Your  task  is  to  answer  the  following  question.  Remember  to  be  concise
| and  only  | give     | the  answer  | in         | a  few  words  |            |         |          |           |
| ---------- | -------- | ------------ | ---------- | -------------- | ---------- | ------- | -------- | --------- |
| Q:Which    | cartoon  | title        | character  | has            | a  friend  | called  | Captain  | Haddock?  |
A
|     | Figure7: |     | PrompttemplateforChatexam-takermodels |     |     |     |     |     |
| --- | -------- | --- | ------------------------------------- | --- | --- | --- | --- | --- |
418

| Asset          |     | Version                       |     |     |     |     | License    |     |
| -------------- | --- | ----------------------------- | --- | --- | --- | --- | ---------- | --- |
| TriviaQA       |     | mandarjoshi/trivia_qa         |     |     |     |     | apache-2.0 |     |
| Llama-27BBase  |     | meta-llama/Llama-2-7b-hf      |     |     |     |     | llama2     |     |
| Llama-27BChat  |     | meta-llama/Llama-2-7b-chat-hf |     |     |     |     | llama2     |     |
| Llama-213BBase |     | meta-llama/Llama-2-13b-hf     |     |     |     |     | llama2     |     |
meta-llama/Llama-2-13b-chat-hf
| Llama-213BChat |     |                                      |     |     |     |     | llama2     |     |
| -------------- | --- | ------------------------------------ | --- | --- | --- | --- | ---------- | --- |
| Llama-270BBase |     | meta-llama/Llama-2-70b-hf            |     |     |     |     | llama2     |     |
| Llama-270BChat |     | meta-llama/Llama-2-70b-chat-hf       |     |     |     |     | llama2     |     |
| Mistral7BBase  |     | mistralai/Mistral-7B-v0.1            |     |     |     |     | apache-2.0 |     |
| Mistral7BChat  |     | mistralai/Mistral-7B-Instruct-v0.2   |     |     |     |     | apache-2.0 |     |
| Llama-38BChat  |     | meta-llama/Meta-Llama-3-8B-Instruct  |     |     |     |     | llama3     |     |
| Llama-370BChat |     | meta-llama/Meta-Llama-3-70B-Instruct |     |     |     |     | llama3     |     |
meta-llama/Meta-Llama-3.1-8B-Instruct
| Llama-3.18BChat |     |     |     |     |     |     | llama3.1 |     |
| --------------- | --- | --- | --- | --- | --- | --- | -------- | --- |
Llama-3.170BChat meta-llama/Meta-Llama-3.1-70B-Instruct llama3.1
| JudgeLM    |     | BAAI/JudgeLM-7B-v1.0   |     |     |     |     | Non-commerciallicense |     |
| ---------- | --- | ---------------------- | --- | --- | --- | --- | --------------------- | --- |
| GPT-4Turbo |     | gpt-4-turbo-2024-04-09 |     |     |     |     | N/A                   |     |
Table3: Versionandlicensedetailsforthedifferentmodelsanddatasetsusedinexperiments.
|     | Prompt template for  | judge models  |            |            |               |             |                  |     |
| --- | -------------------- | ------------- | ---------- | ---------- | ------------- | ----------- | ---------------- | --- |
|     | Your  task           | is  to  look  | at  the    | following  | question,     | and  based  | on  the          |     |
|     | references           | provided,     | determine  | if         | the  model’s  | response    | is  correct  or  |     |
incorrect.  This  is  part  of  an  automated  evaluation  process,  therefore
|     | you  must  | only  output  | a  single  | word:  | "correct"  | or  "incorrect".  |     |     |
| --- | ---------- | ------------- | ---------- | ------ | ---------- | ----------------- | --- | --- |
Question:
|     | Which  Australian  | did    | Roger      | Federer  | defeat  | to  win  his  first  | Wimbledon  |     |
| --- | ------------------ | ------ | ---------- | -------- | ------- | -------------------- | ---------- | --- |
|     | Men’s  Singles     | title  | in  20037  |          |         |                      |            |     |
References:
MARK  PHILIPPOUSSIS
MARK  PHILIPPOUSSIS
Model  Response:
Mark  Philippoussis
|     | Evaluation  | (correct/incorrect):  |                                  |          |                               |     |     |          |
| --- | ----------- | --------------------- | -------------------------------- | -------- | ----------------------------- | --- | --- | -------- |
|     |             | Figure8:              | Prompttemplatesforthejudgemodels |          |                               |     |     |          |
|     |             | (cid:16)              |                                  | (cid:17) | (cid:16)                      |     |     | (cid:17) |
|     |             | TP+TN                 |                                  |          | (TP+FP)(TP+FN)+(TN+FN)(TN+FP) |     |     |          |
−
|     | p o −p | e TP+TN+FP+FN |          |                               |     | (TP+TN+FP+FN)2 |          |     |
| --- | ------ | ------------- | -------- | ----------------------------- | --- | -------------- | -------- | --- |
|     | π =    | =             |          |                               |     |                |          |     |
|     |        |               | (cid:16) |                               |     |                | (cid:17) |     |
|     | 1−p    | e             | 1−       | (TP+FP)(TP+FN)+(TN+FN)(TN+FP) |     |                |          |     |
(TP+TN+FP+FN)2
419

G HumanAnnotationGuidelines
Humanannotationguidelines
You will be given a question, a set of reference answers and the answer given
by an LLM. Your task is to judge if the answer given by the LLM is correct, as
if you were the LLMs teacher grading their exam. An answer should be counted
as correct if it is semantically equivalent to (one of the) reference answers.
In doing so, please follow the following guidelines:
• Underspecified answers (e.g. "December" instead of "December 20") should
be marked incorrect.
• Answers that have more information than requested (e.g. "December 20, in
Paris" instead of "December 20") should be marked correct, provided the
extra information is not incorrect or contrasting the rest of the answer.
• Answers with unnecessary verbosity but correct answers should be marked
correct (E.g. “Thanks for asking this question! The correct answer is:
...").
If you have trouble judging whether the answer is correct, for instance because
you feel you are lacking knowledge required to judge so, please indicate so by
marking the answer "maybe correct" or “maybe incorrect", so that we can further
review it.
420

Preliminary research involved iterative refine- JudgeModel MeanScott’sπ StdDev
| ment of | human | annotation | guidelines | to ensure |            |     |      |        |
| ------- | ----- | ---------- | ---------- | --------- | ---------- | --- | ---- | ------ |
|         |       |            |            |           | Llama3-70B |     | 0.88 | 0.0046 |
consistencyandreproducibilityacrossannotators
|                                      |     |     |     |         | Llama3.1-70B |     | 0.88 | 0.0039 |
| ------------------------------------ | --- | --- | --- | ------- | ------------ | --- | ---- | ------ |
| withgeneralEnglishsemanticknowledge. |     |     |     | CSgrad- |              |     |      |        |
|                                      |     |     |     |         | Llama3.1-8B  |     | 0.78 | 0.0050 |
uatestudentsservedasannotatorsforthisexperi-
|     |     |     |     |     | Llama2-13B |     | 0.75 | 0.0043 |
| --- | --- | --- | --- | --- | ---------- | --- | ---- | ------ |
ment. Weprovidetheguidelinesusedforhuman
|     |     |     |     |     | Llama2-70B |     | 0.69 | 0.0114 |
| --- | --- | --- | --- | --- | ---------- | --- | ---- | ------ |
evaluationbelow.
|     |     |     |     |     | Mistral-7B |     | 0.67 | 0.0108 |
| --- | --- | --- | --- | --- | ---------- | --- | ---- | ------ |
|     |     |     |     |     | JudgeLM-7B |     | 0.66 | 0.0026 |
|     |     |     |     |     | Contains   |     | 0.64 | 0.0087 |
|     |     |     |     |     | Llama3-8B  |     | 0.60 | 0.0126 |
H Experimentcosts
|     |     |     |     |     | Llama2-7B |     | 0.47 | 0.0112 |
| --- | --- | --- | --- | --- | --------- | --- | ---- | ------ |
|     |     |     |     |     | EM        |     | 0.47 | 0.29   |
|     |     |     |     |     | Gemma-2B  |     | 0.26 | 0.007  |
Thecostsforthedifferentexperimentsdescribedin
thisworkbelonginthreecategories–GPU-hours
|     |     |     |     |     | Table 4: | Weak Scott’s | π variation | for the 5 down- |
| --- | --- | --- | --- | --- | -------- | ------------ | ----------- | --------------- |
for running open-source models on one or more sampled sets indicating robustness for the evaluation
| Nvidia        | A100 GPUs,  | OpenAI    | credits            | for making  | sample        |     |     |     |
| ------------- | ----------- | --------- | ------------------ | ----------- | ------------- | --- | --- | --- |
| API calls     | to OpenAI   | models,5  | and                | human hours |               |     |     |     |
| for manual    | annotations |           | of benchmark       | responses.  | J JudgeScores |     |     |     |
| The estimated |             | costs for | the final reported | experi-     |               |     |     |     |
mentsaregiveninAppendixK.Inadditiontothis, Weshowthescoresassignedbyeachjudgemodel
toeachexam-takermodel,visualisedinFigure1a
previousunreportedexperimentsandtrialshadan
inAppendixK.
approximatecostof120GPU-hours,100USDin
OpenAIcredits,and50humanhours,bringingthe
K Exam-takermodelbasevschat
| total experimental |     | cost | for this work | to approxi- |     |     |     |     |
| ------------------ | --- | ---- | ------------- | ----------- | --- | --- | --- | --- |
analysis
mately200GPU-hours,USD125OpenAIcredits,
and75humanannotationhours.
Giventhehumanjudgmentswehaveavailable,we
taketheopportunitytoinvestigatetheperformance
differencesbetweenbaseandtheircorresponding
|     |     |     |     |     | chatmodels. | InAppendixK,weshowthescores |     |     |
| --- | --- | --- | --- | --- | ----------- | --------------------------- | --- | --- |
I StatisticalreliabilityofEvaluation
assignedbyvariousjudgemodelstofourbase-chat
sample
pairs. AccordingtothedefaultmetricEM,thebase
modelsoutperformthechatmodelsbyalargemar-
gin. Interestingly,whilethisdifferencegetssmaller
DuetocomputationalconstraintsdiscussedinAp- whentheanswersarejudgedbyhumans(second
pendixAandAppendixH,welimitourevaluation
|     |     |     |     |     | column) | or GPT-4 Turbo, | there | is still a substan- |
| --- | --- | --- | --- | --- | ------- | --------------- | ----- | ------------------- |
settorandomlysampled400questionsfromTrivi- tialdifferenceforallfourpairs,suggestingthatthe
aQA(Joshietal.,2017). Inthissection,wefurther differenceisnotmerelyaneffectoftheincreased
take5samplesof300randomlyselectedquestions
|     |     |     |     |     | verbosityofthechatmodels. |     | Furtherevidencefor |     |
| --- | --- | --- | --- | --- | ------------------------- | --- | ------------------ | --- |
fromtheevaluationsetandcalculatethemeanand
thathypothesisisprovidedbyFigure9b,inwhich
standarddeviationofScott’sPi. FromAppendixI, wecanseethatwhile14%oftheerrorsareshared
itcanbeobservedthatevenondown-sampledsets, betweenthebase-chatpairs,almostanother14%of
| theScott’sπ | valuesaresimilartoFigure1b. |     |     | Stan- |     |     |     |     |
| ----------- | --------------------------- | --- | --- | ----- | --- | --- | --- | --- |
theexamplesgetjudgedcorrectlybythebasemod-
dard deviation of all the judge models from the elsbutnotbythechatmodels,whiletheopposite
meanScott’sπ isalsominimal,barringEMlexical happensinonly2.5%ofthecases.
match.
5PricingdetailsforOpenAImodelsareavailableathttps:
//openai.com/api/pricing/
421

|     | Experiment          |     |     | GPU-hours | OpenAIcredits |     | Humanhours |     |
| --- | ------------------- | --- | --- | --------- | ------------- | --- | ---------- | --- |
|     | Mainbenchmarks      |     |     | 5         |               | 2   | -          |     |
|     | Mainevaluations     |     |     | 30        |               | 8   | 10         |     |
|     | Humanalignment      |     |     | 2         |               | -   | 9          |     |
|     | Erroranalysis       |     |     | 1.5       |               | -   | 5          |     |
|     | Controlledresponses |     |     | 15        |               | -   | -          |     |
|     | Leniencybias        |     |     | 5         |               | 5   | -          |     |
|     | Guidelinebias       |     |     | 10        |               | 5   | 1          |     |
|     | Referencebias       |     |     | 5         |               | 4   | 1          |     |
|     | Total               |     |     | 73.5      |               | 24  | 26         |     |
Table 5: Estimated costs for the final reported experiments. GPU-hours are in equivalent Nvidia A100 hours,
OpenAIcreditsareinUSD,andhumanhoursaretimespentinmanualannotation.
Examtakermodels
|     |     |     |      | Llama2 |      |     | Mistral       | GPT-4 |
| --- | --- | --- | ---- | ------ | ---- | --- | ------------- | ----- |
|     |     |     | Base |        | Chat |     | Base Instruct |       |
JudgeModels
|     |     | 7B  | 13B | 70B 7B |     | 13B 70B | 7B  |     |
| --- | --- | --- | --- | ------ | --- | ------- | --- | --- |
Llama3.18B 65.25 75.00 83.50 60.25 70.50 75.50 73.75 59.00 89.00
Llama3.170B 62.00 74.25 85.00 55.50 64.75 74.00 72.25 60.50 92.25
Llama38B 76.00 83.25 91.50 73.25 82.75 85.25 81.75 76.0 97.25
Llama370B 64.25 75.50 86.50 57.00 64.00 75.75 73.5 62.50 92.75
Llama27B 80.50 85.25 92.00 80.50 70.75 90.75 84.00 83.25 97.75
Llama213B 68.25 75.50 86.50 63.25 62.75 77.50 74.50 67.50 93.5
| Llama270B |     | 71.25 | 80.5 | 90.25 67.50 | 74.75 | 81.25 | 80.0 72.5 | 96.75 |
| --------- | --- | ----- | ---- | ----------- | ----- | ----- | --------- | ----- |
Mistral7B 72.50 80.75 90.50 69.00 74.75 82.50 80.25 72.00 96.25
| Gemma2B |     | 79.75 | 87.00 | 91.25 58.50 |      | 41 68.50 | 84.0 55.75  | 80.50 |
| ------- | --- | ----- | ----- | ----------- | ---- | -------- | ----------- | ----- |
| JudgeLM |     | 69.50 | 77.75 | 86.25 63.75 | 48.0 | 82.75    | 77.25 71.0  | 94.50 |
| GPT-4   |     | 60.50 | 71.50 | 82.50 54.50 | 59.0 | 73.0     | 69.75 56.50 | 90.0  |
ExactMatch 46.75 56.00 63.75 24.00 0.25 36.25 59.50 20.25 58.25
ContainsMatch 50.75 60.00 68.00 39.00 46.25 59.50 57.25 44.00 70.00
HumanEval 62.50 72.75 83.75 56.00 56.50 72.25 71.75 60.75 91.50
|     |     | Table6: | Judgemodelscorecardforeveryexam-takermodel. |     |     |     |     |     |
| --- | --- | ------- | ------------------------------------------- | --- | --- | --- | --- | --- |
422

Weconsidertwoalternativehypotheses: asMistral 7BperformonparwithGPT-4 Turbo,
|     |     |             |     |              |             |     | highlighting         |     | the robustness | of  | smaller models | in  |
| --- | --- | ----------- | --- | ------------ | ----------- | --- | -------------------- | --- | -------------- | --- | -------------- | --- |
| i)  | The | chat models |     | have a worse | understand- |     | maintainingrankings. |     |                |     |                |     |
ingoftheparticularpromptformat,whichis
tunedmoretofitbasemodels;or
|                                   |                                        |                                     |                          |                  |              |          |     | Judges       |     | ρ    | σ    |     |
| --------------------------------- | -------------------------------------- | ----------------------------------- | ------------------------ | ---------------- | ------------ | -------- | --- | ------------ | --- | ---- | ---- | --- |
| ii)                               | The                                    | chat models                         |                          | have ‘unlearned’ |              | some     |     |              |     |      |      |     |
|                                   |                                        |                                     |                          |                  |              |          |     | Contains     |     | 0.99 | 0.02 |     |
|                                   | knowledgeduringtheiralignmenttraining. |                                     |                          |                  |              |          |     | Mistral-7B   |     | 0.98 | 0.03 |     |
|                                   |                                        |                                     |                          |                  |              |          |     | GPT-4        |     | 0.98 | 0.03 |     |
| To                                | disentangle                            |                                     | these                    | two factors,     |              | we manu- |     |              |     |      |      |     |
|                                   |                                        |                                     |                          |                  |              |          |     | Llama2-13B   |     | 0.95 | 0.18 |     |
| allyanalyse400questionsforLlama-2 |                                        |                                     |                          |                  |              | 70Band   |     |              |     |      |      |     |
|                                   |                                        |                                     |                          |                  |              |          |     | JudgeLM-7B   |     | 0.95 | 0.05 |     |
| Llama-2                           |                                        | 70B-chat,usingourearliererrorcodes. |                          |                  |              |          |     |              |     |      |      |     |
|                                   |                                        |                                     |                          |                  |              |          |     | Llama2-7B    |     | 0.94 | 0.04 |     |
| The                               | results,                               | shown                               | in                       | Figure 9a,       | sugest       | that, at |     |              |     |      |      |     |
|                                   |                                        |                                     |                          |                  |              |          |     | Llama3.1-70B |     | 0.94 | 0.07 |     |
| leasttosomeextent,                |                                        |                                     | thedifferencebetweenbase |                  |              |          |     |              |     |      |      |     |
|                                   |                                        |                                     |                          |                  |              |          |     | Llama3-70B   |     | 0.93 | 0.05 |     |
| and                               | chat                                   | models                              | is in fact               | due to           | ‘unlearning’ | of       |     |              |     |      |      |     |
|                                   |                                        |                                     |                          |                  |              |          |     | Llama3.1-8B  |     | 0.89 | 0.10 |     |
| knowledge:                        |                                        | whilethenumberoferrorsismoreor      |                          |                  |              |          |     |              |     |      |      |     |
|                                   |                                        |                                     |                          |                  |              |          |     | Llama3-8B    |     | 0.86 | 0.07 |     |
lessequalamongmostcategories,thereisastark
|            |     |        |            |          |           |      |     | Llama2-70B |     | 0.84 | 0.13 |     |
| ---------- | --- | ------ | ---------- | -------- | --------- | ---- | --- | ---------- | --- | ---- | ---- | --- |
| difference |     | in the | incorrect  | entity   | category. | Sub- |     |            |     |      |      |     |
|            |     |        |            |          |           |      |     | Gemma-2B   |     | 0.71 | 0.20 |     |
| stantially |     | more   | often than | the base | models,   | the  |     |            |     |      |      |     |
|            |     |        |            |          |           |      |     | EM         |     | 0.67 | 0.13 |     |
chatmodelsdoanswerthequestionwithasemanti-
callyplausiblebutincorrectentity. InAppendixM- Table8: SpearmanRankCorrelationCoefficientρ.
AppendixM,weprovideexamplesofsuchcases.
The results do not show any evidence to support M Toomuchinfoconfusesjudges
| thefirsthypothesis: |     |     | thenumberoferrorswherethe |     |     |     |     |     |     |     |     |     |
| ------------------- | --- | --- | ------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
answercannotbeparsedorisjustentirelyincorrect InFigure10-13,wereporttheguidelinesweused
|     |     |     |     |     |     |     | fortheexperimentsin§5.2. |     |     | Thesimplestprompt |     |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------ | --- | --- | ----------------- | --- | --- |
doesnotdifferbetweenbaseandchatmodels.
|     |     |     |     |     |     |     | used is | Without | Guidelines |     | v1 (see Figure | 10) |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------- | ---------- | --- | -------------- | --- |
L Exam-takermodelrankingcorrelation where we define a sequential and structured pro-
|     |     |     |     |     |     |     | cessforthejudgemodel. |     |     | InWithoutGuidelinesv2 |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | --- | --------------------- | --- | --- |
InAppendixL,WeusetheSpearmanRankcorre- (seeFigure11),weaddanadditionalfocusonthe
| lation   | coefficient |        | (Spearman, | 1904)   | to  | assess the |                              |     |     |     |               |     |
| -------- | ----------- | ------ | ---------- | ------- | --- | ---------- | ---------------------------- | --- | --- | --- | ------------- | --- |
|          |             |        |            |         |     |            | overalltaskandoutcomeaswell. |     |     |     | ForGuidelines |     |
| rankings |             | of the | exam-taker | models. | To  | validate   |                              |     |     |     |               |     |
withoutexamples(seeFigure12),weprovidethe
theserankings,werandomlyselect6outof9exam- judgemodelswithdetailedinstructionsaboutthe
takermodelsacross5samples,subsequentlycalcu-
taskathand,alongwithexplicitguidelinesonhow
latingthemean(ρ)andstandarddeviation(σ)of
|              |     |                                 |     |     |     |     | to evaluate | the | answers. | Additionally, | for | Guide- |
| ------------ | --- | ------------------------------- | --- | --- | --- | --- | ----------- | --- | -------- | ------------- | --- | ------ |
| therankings. |     | Theresultsrevealthatthecontains |     |     |     |     |             |     |          |               |     |        |
lineswithexamples(seeFigure13),wealsoprovide
| model | exhibits | the | highest | stability | and | ρ among |     |     |     |     |     |     |
| ----- | -------- | --- | ------- | --------- | --- | ------- | --- | --- | --- | --- | --- | --- |
examplestothejudgemodelsforfurtherreference.
| the     | rankings,  | while       | the       | majority        | of judge        | models     |     |     |     |     |     |     |
| ------- | ---------- | ----------- | --------- | --------------- | --------------- | ---------- | --- | --- | --- | --- | --- | --- |
| achieve | a          | coefficient | exceeding |                 | 0.7, indicating | a          |     |     |     |     |     |     |
| strong  | alignment. |             | Notably,  | smaller         | models          | such       |     |     |     |     |     |     |
| Table   | 7: Scores  | of          | base      | and chat models |                 | by various |     |     |     |     |     |     |
judges
Judgemodels
|     | Base-Chat |     |      |      |      |          |       |      | GPT-4 |       | Llama-3 |      |
| --- | --------- | --- | ---- | ---- | ---- | -------- | ----- | ---- | ----- | ----- | ------- | ---- |
|     |           |     |      | EM   |      | Contains | Human |      |       |       |         |      |
|     | pair      |     |      |      |      |          |       |      |       | Turbo | 70B     |      |
|     |           |     | Base | Chat | Base | Chat     | Base  | Chat | Base  | Chat  | Base    | Chat |
Llama-27B 46.75 24.00 50.75 39.00 62.25 56.00 60.50 54.50 64.25 57.00
Mistral7B 59.50 20.25 57.25 44.00 71.75 60.75 69.75 56.50 73.50 62.50
Llama-213B 56.00 0.25 60.00 46.25 72.75 56.50 75.00 59.00 76.50 64.00
Llama-270B 63.75 36.25 68.00 59.50 83.75 72.25 82.50 73.00 86.50 75.75
423

| Incorrect | Under- | Too few |     | Too | No  |     |     |     |
| --------- | ------ | ------- | --- | --- | --- | --- | --- | --- |
Other
| entity | specified | entities |     | manyanswer |     |     |     | Both correct |
| ------ | --------- | -------- | --- | ---------- | --- | --- | --- | ------------ |
Both incorrect
120 108
| gnorW snoitseuQ fo oN |     |     |     |     |     |        |       | Base correct, Chat incorrect |
| --------------------- | --- | --- | --- | --- | --- | ------ | ----- | ---------------------------- |
| 100                   |     |     |     |     |     |        | 2.50% | Base incorrect, Chat correct |
| 80                    |     |     |     |     |     | 13.75% |       |                              |
77
60
14.00%
40
| 20  | 16  | 16  |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
7
| 0   |     | 3   | 2   | 2 1 | 1   |     |     | 69.75% |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ |
      Llama-2 70B
Base Chat
|     |     | (a) |     |     |     |     |     | (b) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
Figure9: a)DistributionofincorrectquestioncountsbyerrorcodesforLlama2 70BBasevsChatexam-taker
modelsevaluatedon400questions. b)Piechartshowingthepercentageofquestionscategorizedbythejudgment
fromBaseandChatmodels.
Question:
Which British artist’s works include ‘The First Real Target’?
| References |     | Peter Blake, | Peter | Balke, | Sir Peter | Blake |     |     |
| ---------- | --- | ------------ | ----- | ------ | --------- | ----- | --- | --- |
LLama-270B
Peter Blake
Base
LLama-270B
| Chat |     | Patrick Caulfield |     |     |     |     |     |     |
| ---- | --- | ----------------- | --- | --- | --- | --- | --- | --- |
Mistral7B
David Hockney
Base
Mistral7B
| Chat |     | Damien Hirst |                              |     |     |     |     |     |
| ---- | --- | ------------ | ---------------------------- | --- | --- | --- | --- | --- |
|      |     | Table9:      | Knowledgeunlearningexample1. |     |     |     |     |     |
Question:
|     | Who was | the first       | cricketer | to            | score 10,000 | test | runs? |           |
| --- | ------- | --------------- | --------- | ------------- | ------------ | ---- | ----- | --------- |
|     |         | Sunil Gavaskar, |           | Sunil Manohar | Gavaskar,    |      | SM    | Gavaskar, |
References
|     |     | Sunny gavaskar, |     | Gavaskar |     |     |     |     |
| --- | --- | --------------- | --- | -------- | --- | --- | --- | --- |
LLama-270B
Sunil Gavaskar
Base
LLama-270B
Sachin Tendulkar
Chat
Mistral7B
Sachin Tendulkar
Base
Mistral7B
|      |     | Sachin Tendulkarwas |                             | the           | first cricketer |     | to  | score |
| ---- | --- | ------------------- | --------------------------- | ------------- | --------------- | --- | --- | ----- |
| Chat |     | 10,000 runs         | in                          | Test matches. |                 |     |     |       |
|      |     | Table10:            | Knowledgeunlearningexample2 |               |                 |     |     |       |
424

Question:
| ‘Uncle Harry’s | Coat’ | was the first | garment produced | by which |
| -------------- | ----- | ------------- | ---------------- | -------- |
famous jacket manufacturer, based in Simonside, Newcastle Upon
Tyne?
Barbour
References
Barbour
LLama-270B
Base
| LLama-270B | Barbour |     |     |     |
| ---------- | ------- | --- | --- | --- |
Chat
| Mistral7B | Barbour |     |     |     |
| --------- | ------- | --- | --- | --- |
Base
| Mistral7B | Jack Walker | & Sons |     |     |
| --------- | ----------- | ------ | --- | --- |
Chat
|     | Table11: | Knowledgeunlearningexample3 |     |     |
| --- | -------- | --------------------------- | --- | --- |
425

Your task is to look at the following question, and based on the
references provided, determine if the model’s response is correct or
incorrect. This is part of an automated evaluation process, therefore
you must only output a single word: “correct” or "incorrect"
Question
Which Australian did Roger Federer defeat to win his first Wimbledon
Men’s Singles title in 20037
References:
MARK PHILIPPOUSSIS
MARK PHILIPPOUSSIS
Model Response:
Mark Philippoussis
Evaluation (correct/incorrect)
Figure11: WithoutGuidelinesv2prompttemplateforthejudgemodels
Review the question and examine the references provided, then evaluate
the model’s response. This is part of an automated evaluation
process, therefore you must only output a single word: "correct"
or "incorrect"
Question:
Which Australian did Roger Federer defeat to win his first Wimbledon
Men’s Singles title in 20037
References:
MARK PHILIPPOUSSIS
MARK PHILIPPOUSSIS
Model Response
Mark Philippoussis
Evaluation (correct/incorrect) :
Figure10: WithoutGuidelinesv1prompttemplateforthejudgemodels
426

With Guidelines but no examples (245 tokens)
Review the Question and Examine the Reference: Carefully read
and understand the question. Carefully read each of the reference
provided for the question:
Evaluate the LLM Response based on guidelines (1-4):
1. Given the model response, only consider the part(s) of the
response answering the question, and ignore any extra text.
2. When evaluating the language model’s answer, evaluate True if it
matches with at least one of the provided references otherwise False.
3. An answer and reference pair is considered a match if they are
semantically equivalent given the context of the question. This
determination should not require world knowledge from the human, and
if it does, consider it not a match. The answer must contain all the
information of the reference for it to be considered a match.
4. Considering there might be multiple correct answers, each answer
must match with at least one reference for the response to be
considered correct overall.
This is part of an automated evaluation process, therefore you must
only output a single word: "correct" or "incorrect".
Question:
Which Australian did Roger Federer defeat to win his first Wimbledon
Men’s Singles title in 20037
References:
MARK PHILIPPOUSSIS
MARK PHILIPPOUSSIS
Model Response:
Mark Philippoussis
Evaluation (correct/incorrect):
Figure12: GuidelineswithoutexamplesPrompttemplateforthejudgemodels
Reference Bias example 2
Your task is to look at the following question, and based on the
references provided, determine if the model’s response is correct or
incorrect. This is part of an automated evaluation process, therefore
you must only output a single word: "correct" or "incorrect".
Question:
Q: The oldest known American cocktail, what whiskey forms the base of
the cocktail known as a Sazerac?
Model Response:
RYE WHISKEY
References References
Rye Secale cereale
Centeio Rye Extract
Winter rye Ryep
Rye Rye (botany)
Ryep Rye
Secale cereale Winter rye
Rye (botany) Centeio
Rye (grain) Rye (grain)
Rye Extract Rye
Uramat Uramat
Judge Output
Judge Output
Correct Incorrect. The correct answer is
"bourbon whiskey"
Figure15: ExampleofLlama2-7Bfailingtoidentifythetaskbychangingtheorderofthereferences.
427

Wi
h Guidelines and examples (301 tokens)
You will be given a question, a set of reference answers and the
answer given by an LLM. Your task is to judge if the answer given
by the LLM is correct, as if you were the LLMs teacher grading their
exam. An answer should be counted as correct if it is semantically
equivalent to (one of the) reference answers. In doing so, please
follow the following guidelines (1-3):
1. Underspecified answers (e.g. "December" instead of "December 20")
should be marked incorrect
2. Answers that have more information than requested (e.g. "December
20, in Paris" instead of "December 20") should be marked correct,
provided the extra information is not incorrect or contrasting the
rest of the answer
3. Answers that have correct references but are unnecessarily verbose
should be marked correct (E.g. "Thanks for asking this question! The
correct answer is: ...)
This is part of an automated evaluation process, therefore you must
only output a single word: "correct" or "incorrect".
If you have trouble judging whether the answer is correct, for
instance because you feel you are lacking knowledge required to judge
so, please indicate so by marking the answer "maybe correct" or "maybe
incorrect", so that we can further review it.
Question:
Which Australian did Roger Federer defeat to win his first Wimbledon
Men’s Singles title in 20037
References:
MARK PHILIPPOUSSIS
MARK PHILIPPOUSSIS
Model Response:
Mark Philippoussis
Evaluation (correct/incorrect):
Figure13: GuidelineswithExamplesPrompttemplateforthejudgemodels
Reference Bias example 1
Your task is to look at the following question, and based on the
references provided, determine if the model’s response is correct or
incorrect. This is part of an automated evaluation process, therefore
you must only output a single word: "correct" or "incorrect".
Question:
Q: Aberdeen is known as what?
Model Response:
Granite City
References References
The Granite City Granite City
The granite city Granite City (disambiguation)
Granite City (disambiguation) The granite city
The Granite City The Granite City
Granite City The Granite City
Judge Output Judge Output
Incorrect Correct
Figure14: ExampleofLlama2-7Bgettingconfusedwhentheorderofthereferencesarechanged
428

N Judgemodelsaresensitivetoreference
rectlyidentifiedbythejudgemodeltobeincorrect,
| order |     |     |     |     |     | wouldalsobecomprisedoftwocases: |     |     |     | 1)Thejudge |     |
| ----- | --- | --- | --- | --- | --- | ------------------------------- | --- | --- | --- | ---------- | --- |
evaluatesitcorrectlyaccordingtothegivenevalua-
Weinvestigatethejudges’sensitivitytoreference
|     |     |     |     |     |     | tioncriteriawithaprobabilityofP |     |     |     | .2)Thejudge |     |
| --- | --- | --- | --- | --- | --- | ------------------------------- | --- | --- | --- | ----------- | --- |
c
orderbyprovidingthesameprompt,questionand doesnotevaluateitaccordingtothegivencriteria
modelresponsetothejudgemodels,butshuffling
|     |     |     |     |     |     | withaprobabilityof1−P |     |     | ,buttheevaluationstill |     |     |
| --- | --- | --- | --- | --- | --- | --------------------- | --- | --- | ---------------------- | --- | --- |
c
thereferenceorderinthreedifferentpermutations.
|     |     |     |     |     |     | happenstobecorrectwithaprobabilityof1−P |     |     |     |     | .   |
| --- | --- | --- | --- | --- | --- | --------------------------------------- | --- | --- | --- | --- | --- |
+
Wecomputetheconsistencyscoreofthemodelas
Withthetotalratiooftheincorrectresponsesbeing
thepercentageofquestionsforwhichitgivesthe
1−s,thetruenegativerateisthereforegivenby–
| samejudgmentallthe3times. |     |     | Weobservethatthe |     |     |     |     |     |     |     |     |
| ------------------------- | --- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- |
modelismorelikelytoevaluateananswerascor-
rectifthecorrespondingreferenceappearsearlyin t = (1−s)[P +(1−P )(1−P )]. (5)
|                                   |     |     |     |            |     | N   |     | c   | c   | +   |     |
| --------------------------------- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
| thelistofreferences(seeFigure14). |     |     |     | Thesmaller |     |     |     |     |     |     |     |
judgemodelssometimesfailtocaptureallthein- UsingEquation(5),wecanderivethefollowing.
| formation | in the prompt, | and | provide | judgement |     |     |     |     |     |     |     |
| --------- | -------------- | --- | ------- | --------- | --- | --- | --- | --- | --- | --- | --- |
basedontheirownknowledgeratherthangoingby
thereferences(seeFigure15). t N = (1−s)[P c +(1−P c )(1−P + )]
(6)
O LeniencyBias
|     |     |     |     |     |     |     | =   | P +1−P | −P +P | P   | (7) |
| --- | --- | --- | --- | --- | --- | --- | --- | ------ | ----- | --- | --- |
|     |     |     |     |     |     |     |     | c      | + c   | c + |     |
As described in § 5.4, for the purpose of the le- −sP −s+sP +sP −sP P
|        |                   |     |        |      |         |     |     | c   | +   | c   | c + |
| ------ | ----------------- | --- | ------ | ---- | ------- | --- | --- | --- | --- | --- | --- |
| niency | bias experiments, | we  | assume | that | a judge |     |     |     |     |     |     |
(8)
assignsthecorrectjudgmentwithaprobabilityof
|                                           |        |             |     |        |           |     | =   | 1−P +P | P −s+sP | −sP | P   |
| ----------------------------------------- | ------ | ----------- | --- | ------ | --------- | --- | --- | ------ | ------- | --- | --- |
| P andrandomlyassignstherestofthesamplesto |        |             |     |        |           |     |     | +      | c +     | +   | c + |
| c                                         |        |             |     |        |           |     |     |        |         |     | (9) |
| be “correct”                              | with a | probability |     | P . In | this sec- |     |     |        |         |     |     |
+
tion, we derive the mathematical expressions for = 1−s−P (1−P −s+sP )
|        |                                    |     |     |     |     |     |     |     | + c |     | c    |
| ------ | ---------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---- |
| P andP | . Weassumethatinthecaseofmisalign- |     |     |     |     |     |     |     |     |     | (10) |
c +
mentbetweentheevaluationcriteriaofguidelines = 1−s−P (1−s)(1−P ) (11)
|     |     |     |     |     |     |     |     |     | +   | c   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
andjudgemodels,theprobabilityofgettinganeval-
1−s−t
N
| uationof“correct”isindependentoftheactual |     |     |     |     |     | =⇒  | P + = |           |     |     | (12) |
| ----------------------------------------- | --- | --- | --- | --- | --- | --- | ----- | --------- | --- | --- | ---- |
|                                           |     |     |     |     |     |     |       | (1−s)(1−P | )   |     |      |
c
correctnessoftheanswer(i.e.thejudgemodelef-
1− tN
| fectivelyflipsacointogiveoutitsjudgement). |       |       |     |          | For      |                         |     |       |                  |     |      |
| ------------------------------------------ | ----- | ----- | --- | -------- | -------- | ----------------------- | --- | ----- | ---------------- | --- | ---- |
|                                            |       |       |     |          |          |                         | =   | 1−s   |                  |     | (13) |
| anygivenbenchmarkandjudgemodel,wedenote    |       |       |     |          |          |                         |     | 1−P c |                  |     |      |
| the ground-truth                           | score | as s, | and | the true | positive |                         |     |       |                  |     |      |
|                                            |       |       |     |          |          | SubstitutingthevalueofP |     |       | inEquation(4),we |     |      |
+
| andtruenegativeratesast |     | P   | andt | N ,respectively, |     |     |     |     |     |     |     |
| ----------------------- | --- | --- | ---- | ---------------- | --- | --- | --- | --- | --- | --- | --- |
get:
allnormalizedtobebetween0and1.
| Now, | based on our | assumptions, |     | the true | pos- |     |     |     |     |     |     |
| ---- | ------------ | ------------ | --- | -------- | ---- | --- | --- | --- | --- | --- | --- |
itives, where the exam-taker model response is t = s[P +(1−P )P ] (14)
|     |     |     |     |     |     |     | P   | c   | c   | +   |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
correct,andalsocorrectlyidentifiedbythejudge (cid:34) tN (cid:35)
1−
| model to | be correct, | would | be comprised |     | of two |     |     |         |           | 1−s |      |
| -------- | ----------- | ----- | ------------ | --- | ------ | --- | --- | ------- | --------- | --- | ---- |
|          |             |       |              |     |        |     |     | = s P c | +(1−P c ) |     | (15) |
1−P
| possiblecases: | 1)Thejudgeevaluatesitcorrectly |            |     |          |        |     |     |          |       | c        |      |
| -------------- | ------------------------------ | ---------- | --- | -------- | ------ | --- | --- | -------- | ----- | -------- | ---- |
|                |                                |            |     |          |        |     |     | (cid:20) |       | (cid:21) |      |
| according      | to the given                   | evaluation |     | criteria | with a |     |     |          | t     |          |      |
|                |                                |            |     |          |        |     |     | = s P    | +1− N |          | (16) |
| probabilityofP | ;and2)Thejudgedoesnoteval-     |            |     |          |        |     |     | c        |       |          |      |
|                | c                              |            |     |          |        |     |     |          | 1−s   |          |      |
uateitaccordingtothegivencriteriawithaprob-
|                                               |                                |     |     |            |     |     | t P |         | t N  |     |      |
| --------------------------------------------- | ------------------------------ | --- | --- | ---------- | --- | --- | --- | ------- | ---- | --- | ---- |
|                                               |                                |     |     |            |     | =⇒  |     | = P +1− |      |     | (17) |
| abilityof1−P                                  | , buttheevaluationstillhappens |     |     |            |     |     |     | c       |      |     |      |
|                                               | c                              |     |     |            |     |     | s   |         | 1−s  |     |      |
| to be correct                                 | with a probability             |     | of  | P + . With | the |     |     | t       | t    |     |      |
|                                               |                                |     |     |            |     | =⇒  | P   | = P +   | N −1 |     | (18) |
| totalratioofthecorrectresponsesbeings,thetrue |                                |     |     |            |     |     |     | c       |      |     |      |
|                                               |                                |     |     |            |     |     |     | s       | 1−s  |     |      |
positiverateisthereforegivenby–
|     |         |       |     |     |     | ThevaluesofP                                  |     | andP | canbeestimatedfrom |     |     |
| --- | ------- | ----- | --- | --- | --- | --------------------------------------------- | --- | ---- | ------------------ | --- | --- |
|     |         |       |     |     |     |                                               |     | c    | +                  |     |     |
|     |         |       |     |     |     | observeddatausingthederivedexpressions.       |     |      |                    |     | The |
|     | t = s[P | +(1−P | )P  | ]   | (4) |                                               |     |      |                    |     |     |
|     | P c     |       | c   | +   |     | estimatedprobabilitiesusingthismethod,withhu- |     |      |                    |     |     |
Similarly, the true negatives, where the exam- manevaluationasthereference,areshowninFig-
| taker model | response | is incorrect, |     | and also | cor- | ure16a. |     |     |     |     |     |
| ----------- | -------- | ------------- | --- | -------- | ---- | ------- | --- | --- | --- | --- | --- |
429

Tovalidatethesederivedvalues,weobservethe
| correlationbetweentheestimatedvaluesofP |     | and |     |     |     |     |
| --------------------------------------- | --- | --- | --- | --- | --- | --- |
c
| Scott’sPi(π). AsshowninFigure16b,weobserve |                     |     |     |     |     |     |
| ------------------------------------------ | ------------------- | --- | --- | --- | --- | --- |
| thattheestimatedvaluesofP                  | arehighlycorrelated |     |     |     |     |     |
c
| totheScott’sπ | valuesforthejudgemodels,witha |     |     |     |     |     |
| ------------- | ----------------------------- | --- | --- | --- | --- | --- |
Pearsoncorrelationcoefficientof0.98.
|            | π         | P P  |     |     |     |     |
| ---------- | --------- | ---- | --- | --- | --- | --- |
| Judgemodel |           | c +  |     |     |     |     |
| Gemma-2B   | 0.26 0.38 | 0.87 |     |     |     |     |
| Llama2-7B  | 0.47 0.63 | 0.75 |     |     |     |     |
| Llama3-8B  | 0.59 0.63 | 0.74 |     |     |     |     |
JudgeLM-7B
|              | 0.65 0.68 | 0.19 |     |     |     |     |
| ------------ | --------- | ---- | --- | --- | --- | --- |
| Mistral-7B   | 0.66 0.70 | 0.87 |     |     |     |     |
| Llama2-70B   | 0.69 0.66 | 0.99 |     |     |     |     |
| Llama2-13B   | 0.74 0.74 | 0.87 |     |     |     |     |
| Llama3.1-8B  | 0.77 0.77 | 0.82 |     |     |     |     |
| GPT-4        | 0.87 0.87 | 0.69 |     |     |     |     |
| Llama3.1-70B | 0.88 0.88 | 0.82 |     |     |     |     |
| Llama3-70B   | 0.88 0.87 | 0.90 |     |     |     |     |
100
90
(a)
80
erocS ycnetsisnoC
| 1.0 |     |     | 70  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
60
50
40
0.8
30
20
10
0.6
|     |     |     | Llama-2 7BLlama-2 13BMistral 7BLlama-2 70B |     | GPT-4 |     |
| --- | --- | --- | ------------------------------------------ | --- | ----- | --- |
0.4
|     |     |     | Figure 17:        | Leniency bias and | answer consistency. |         |
| --- | --- | --- | ----------------- | ----------------- | ------------------- | ------- |
|     |     |     | Consistencyscore, | definedasthe      | percentage          | ofques- |
|     |     |     | tions for which   | the judge model   | gives the same      | judg-   |
0.2
mentforthreedifferentanswerorders.
0.0
| 0.0 0.2 | 0.4 0.6 | 0.8 1.0 |     |     |     |     |
| ------- | ------- | ------- | --- | --- | --- | --- |
Scott's Pi ()
(b)
| Figure16: a)EstimatedvaluesofP |     | andP fordiffer- |     |     |     |     |
| ------------------------------ | --- | --------------- | --- | --- | --- | --- |
c +
| entjudgemodels. | b)Pearson’scorrelationcoefficient |     |     |     |     |     |
| --------------- | --------------------------------- | --- | --- | --- | --- | --- |
| betweenπandP    | forjudgemodels.                   |     |     |     |     |     |
c
430
