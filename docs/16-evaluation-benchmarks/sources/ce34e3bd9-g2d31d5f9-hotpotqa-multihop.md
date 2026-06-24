|     |     | HOTPOTQA:    |           | A   | Dataset  | for | Diverse,        | Explainable |     |     |     |     |     |
| --- | --- | ------------ | --------- | --- | -------- | --- | --------------- | ----------- | --- | --- | --- | --- | --- |
|     |     |              | Multi-hop |     | Question |     | Answering       |             |     |     |     |     |     |
|     |     | ZhilinYang*♠ |           |     | PengQi*♥ |     | SaizhengZhang*♣ |             |     |     |     |     |     |
YoshuaBengio♣♦ WilliamW.Cohen† RuslanSalakhutdinov♠ ChristopherD.Manning♥
♠CarnegieMellonUniversity ♥StanfordUniversity ♣Mila,Universite´ deMontre´al
|     |     |     | ♦CIFARSeniorFellow |     |     |     | †GoogleAI |     |     |     |     |     |     |
| --- | --- | --- | ------------------ | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- |
{zhiliny, rsalakhu}@cs.cmu.edu, {pengqi, manning}@cs.stanford.edu
saizheng.zhang@umontreal.ca, yoshua.bengio@gmail.com, wcohen@google.com
|     |     | Abstract |     |     |     |     | ParagraphA,ReturntoOlympus: |     |     |     |     |     |     |
| --- | --- | -------- | --- | --- | --- | --- | --------------------------- | --- | --- | --- | --- | --- | --- |
[1]ReturntoOlympusistheonlyalbumbythealterna-
|     |     |     |     |     |     |     | tive rock | band Malfunkshun. |     | [2] | It was | released | after |
| --- | --- | --- | --- | --- | --- | --- | --------- | ----------------- | --- | --- | ------ | -------- | ----- |
Existingquestionanswering(QA)datasetsfail
|     |     |     |     |     |     |     | the band | had broken | up  | and after | lead | singer | Andrew |
| --- | --- | --- | --- | --- | --- | --- | -------- | ---------- | --- | --------- | ---- | ------ | ------ |
8102 peS 52  ]LC.sc[  1v00690.9081:viXra to train QA systems to perform complex rea- Wood (later of Mother Love Bone) had died of a drug
soning and provide explanations for answers. overdosein1990. [3]StoneGossard,ofPearlJam,had
WeintroduceHOTPOTQA,anewdatasetwith compiledthesongsandreleasedthealbumonhislabel,
LoosegrooveRecords.
| 113k Wikipedia-based |     |     | question-answer |     | pairs |     |     |     |     |     |     |     |     |
| -------------------- | --- | --- | --------------- | --- | ----- | --- | --- | --- | --- | --- | --- | --- | --- |
with four key features: (1) the questions re- ParagraphB,MotherLoveBone:
quirefindingandreasoningovermultiplesup- [4]MotherLoveBonewasanAmericanrockbandthat
|         |           |            |     |         |       |     | formed in  | Seattle, | Washington |       | in 1987. |     |          |
| ------- | --------- | ---------- | --- | ------- | ----- | --- | ---------- | -------- | ---------- | ----- | -------- | --- | -------- |
|         |           |            |     |         |       |     |            |          |            |       |          | [5] | The band |
| porting | documents | to answer; |     | (2) the | ques- |     |            |          |            |       | Frontman |     | Andrew   |
|         |           |            |     |         |       |     | was active | from     | 1987 to    | 1990. | [6]      |     |          |
tions are diverse and not constrained to any Wood’spersonalityandcompositionshelpedtocatapult
|              |                |         |                |              |      |     | the group               | to the top                          | of the  | burgeoning             |        | late 1980s/early |        |
| ------------ | -------------- | ------- | -------------- | ------------ | ---- | --- | ----------------------- | ----------------------------------- | ------- | ---------------------- | ------ | ---------------- | ------ |
| pre-existing | knowledge      |         | bases          | or knowledge |      |     |                         |                                     |         |                        |        |                  |        |
|              |                |         |                |              |      |     | 1990sSeattlemusicscene. |                                     |         | [7]Wooddiedonlydaysbe- |        |                  |        |
| schemas;     | (3) we         | provide | sentence-level |              | sup- |     |                         |                                     |         |                        |        |                  |        |
|              |                |         |                |              |      |     | fore the                | scheduled                           | release | of the                 | band’s | debut            | album, |
| porting      | facts required | for     | reasoning,     | allowing     |      |     |                         |                                     |         |                        |        |                  |        |
|              |                |         |                |              |      |     | “Apple”,                | thusendingthegroup’shopesofsuccess. |         |                        |        |                  | [8]    |
QAsystemstoreasonwithstrongsupervision Thealbumwasfinallyreleasedafewmonthslater.
andexplainthepredictions;(4)weofferanew
Q:WhatwastheformerbandofthememberofMother
type of factoid comparison questions to test LoveBonewhodiedjustbeforethereleaseof“Apple”?
| QA systems’ | ability | to  | extract | relevant | facts |     | A:Malfunkshun |     |     |     |     |     |     |
| ----------- | ------- | --- | ------- | -------- | ----- | --- | ------------- | --- | --- | --- | --- | --- | --- |
andperformnecessarycomparison. Weshow Supportingfacts:1,2,4,6,7
| that HOTPOTQA |     | is challenging |     | for the | latest |        |     |            |     |        |           |           |     |
| ------------- | --- | -------------- | --- | ------- | ------ | ------ | --- | ---------- | --- | ------ | --------- | --------- | --- |
| QA systems,   | and | the supporting |     | facts   | enable |        |     |            |     |        |           |           |     |
|               |     |                |     |         |        | Figure | 1:  | An example |     | of the | multi-hop | questions | in  |
modelstoimproveperformanceandmakeex- HOTPOTQA.Wealsohighlightthesupportingfactsin
plainablepredictions. blueitalics,whicharealsopartofthedataset.
1 Introduction
First,somedatasetsmainlyfocusontestingthe
The ability to perform reasoning and inference ability of reasoning within a single paragraph or
overnaturallanguageisanimportantaspectofin- document, or single-hop reasoning. For example,
telligence. The task of question answering (QA) in SQuAD (Rajpurkar et al., 2016) questions are
provides a quantifiable and objective way to test designed to be answered given a single paragraph
|                                          |     |     |     |     |        | as  | the context, |     | and most | of  | the questions |     | can in |
| ---------------------------------------- | --- | --- | --- | --- | ------ | --- | ------------ | --- | -------- | --- | ------------- | --- | ------ |
| thereasoningabilityofintelligentsystems. |     |     |     |     | Tothis |     |              |     |          |     |               |     |        |
end,afewlarge-scaleQAdatasetshavebeenpro- fact be answered by matching the question with
posed, which sparked significant progress in this a single sentence in that paragraph. As a result, it
hasfallenshortattestingsystems’abilitytoreason
| direction. However, |     | existing | datasets | have | limita- |     |     |     |     |     |     |     |     |
| ------------------- | --- | -------- | -------- | ---- | ------- | --- | --- | --- | --- | --- | --- | --- | --- |
tionsthathinderfurtheradvancementsofmachine overalargercontext. TriviaQA(Joshietal.,2017)
reasoningovernaturallanguage,especiallyintest- and SearchQA (Dunn et al., 2017) create a more
ingQAsystems’abilitytoperformmulti-hoprea- challenging setting by using information retrieval
|               |     |        |        |        |          | to  | collect | multiple | documents |     | to  | form | the con- |
| ------------- | --- | ------ | ------ | ------ | -------- | --- | ------- | -------- | --------- | --- | --- | ---- | -------- |
| soning, where | the | system | has to | reason | with in- |     |         |          |           |     |     |      |          |
formation taken from more than one document to text given existing question-answer pairs. Nev-
arriveattheanswer. ertheless, most of the questions can be answered
|                                  |     |     |     |                   |     | by  | matching | the | question | with | a   | few nearby | sen- |
| -------------------------------- | --- | --- | --- | ----------------- | --- | --- | -------- | --- | -------- | ---- | --- | ---------- | ---- |
| ∗Theseauthorscontributedequally. |     |     |     | Theorderofauthor- |     |     |          |     |          |      |     |            |      |
tencesinonesingleparagraph,whichislimitedas
shipisdecidedthroughdicerolling.
†WorkdonewhenWWCwasatCMU. it does not require more complex reasoning (e.g.,

| overmultipleparagraphs). |          |             |           |               |          |            | 2 DataCollection |           |            |            |               |         |           |
| ------------------------ | -------- | ----------- | --------- | ------------- | -------- | ---------- | ---------------- | --------- | ---------- | ---------- | ------------- | ------- | --------- |
| Second,                  | existing | datasets    |           | that target   |          | multi-hop  |                  |           |            |            |               |         |           |
|                          |          |             |           |               |          |            | The main         | goal      | of our     | work       | is to collect |         | a diverse |
| reasoning,               | such     | as QAngaroo |           | (Welbl        | et       | al., 2018) |                  |           |            |            |               |         |           |
|                          |          |             |           |               |          |            | and explainable  |           | question   |            | answering     | dataset | that      |
| and COMPLEXWEBQUESTIONS  |          |             |           | (TalmorandBe- |          |            |                  |           |            |            |               |         |           |
|                          |          |             |           |               |          |            | requires         | multi-hop | reasoning. |            | One           | way     | to do so  |
| rant, 2018),             | are      | constructed |           | using         | existing | knowl-     |                  |           |            |            |               |         |           |
|                          |          |             |           |               |          |            | is to define     | reasoning |            | chains     | based         | on      | a knowl-  |
| edge bases               | (KBs).   | As          | a result, | these         | datasets | are        |                  |           |            |            |               |         |           |
|                          |          |             |           |               |          |            | edge base        | (Welbl    | et         | al., 2018; | Talmor        | and     | Berant,   |
| constrained              | by       | the schema  |           | of the        | KBs      | they use,  |                  |           |            |            |               |         |           |
2018). However,theresultingdatasetsarelimited
| and therefore | the | diversity |     | of questions |     | and an- |                       |     |     |     |                  |     |         |
| ------------- | --- | --------- | --- | ------------ | --- | ------- | --------------------- | --- | --- | --- | ---------------- | --- | ------- |
|               |     |           |     |              |     |         | by the incompleteness |     |     | of  | entity relations |     | and the |
swersisinherentlylimited.
|     |     |     |     |     |     |     | lack of | diversity | in  | the question |     | types. | Instead, |
| --- | --- | --- | --- | --- | --- | --- | ------- | --------- | --- | ------------ | --- | ------ | -------- |
Third,alloftheabovedatasetsonlyprovidedis-
|     |     |     |     |     |     |     | in this work, |     | we focus | on  | text-based | question | an- |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | -------- | --- | ---------- | -------- | --- |
tantsupervision;i.e.,thesystemsonlyknowwhat
sweringinordertodiversifythequestionsandan-
| the answer | is, | but do | not know | what | supporting |     |     |     |     |     |     |     |     |
| ---------- | --- | ------ | -------- | ---- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- |
swers. Theoverallsettingisthatgivensomecon-
| facts lead | to it. | This | makes | it difficult | for | models |                 |     |        |       |             |     |            |
| ---------- | ------ | ---- | ----- | ------------ | --- | ------ | --------------- | --- | ------ | ----- | ----------- | --- | ---------- |
|            |        |      |       |              |     |        | text paragraphs |     | (e.g., | a few | paragraphs, |     | or the en- |
tolearnabouttheunderlyingreasoningprocess,as
|     |     |     |     |     |     |     | tire Web) | and | a question, |     | a QA | system | answers |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | ----------- | --- | ---- | ------ | ------- |
wellastomakeexplainablepredictions.
|     |     |     |     |     |     |     | the question | by  | extracting |     | a span | of text | from the |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | ---------- | --- | ------ | ------- | -------- |
Toaddresstheabovechallenges,weaimatcre-
|          |            |      |          |     |            |      | context,     | similar | to  | Rajpurkar | et           | al. (2016). | We      |
| -------- | ---------- | ---- | -------- | --- | ---------- | ---- | ------------ | ------- | --- | --------- | ------------ | ----------- | ------- |
| ating a  | QA dataset | that | requires |     | reasoning  | over |              |         |     |           |              |             |         |
|          |            |      |          |     |            |      | additionally | ensure  |     | that it   | is necessary | to          | perform |
| multiple | documents, |      | and does | so  | in natural | lan- |              |         |     |           |              |             |         |
multi-hopreasoningtocorrectlyanswertheques-
| guage, | without | constraining |     | itself | to an | existing |     |     |     |     |     |     |     |
| ------ | ------- | ------------ | --- | ------ | ----- | -------- | --- | --- | --- | --- | --- | --- | --- |
tion.
| knowledge | base | or knowledge |     | schema. |     | We also |       |             |     |         |            |     |           |
| --------- | ---- | ------------ | --- | ------- | --- | ------- | ----- | ----------- | --- | ------- | ---------- | --- | --------- |
|           |      |              |     |         |     |         | It is | non-trivial | to  | collect | text-based |     | multi-hop |
wantittoprovidethesystemwithstrongsupervi-
|     |     |     |     |     |     |     | questions. | Inourpilotstudies,wefoundthatsim- |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --------------------------------- | --- | --- | --- | --- | --- |
sionaboutwhattexttheanswerisactuallyderived
|          |            |         |     |            |     |          | ply giving | an                    | arbitrary | set | of paragraphs |     | to crowd |
| -------- | ---------- | ------- | --- | ---------- | --- | -------- | ---------- | --------------------- | --------- | --- | ------------- | --- | -------- |
| from, to | help guide | systems |     | to perform |     | meaning- |            |                       |           |     |               |     |          |
|          |            |         |     |            |     |          | workers    | is counterproductive, |           |     | because       |     | for most |
fulandexplainablereasoning.
|                               |            |     |     |               |     |         | paragraph    | sets, | it is     | difficult | to          | ask a      | meaning- |
| ----------------------------- | ---------- | --- | --- | ------------- | --- | ------- | ------------ | ----- | --------- | --------- | ----------- | ---------- | -------- |
| We present                    | HOTPOTQA1, |     |     | a large-scale |     | dataset |              |       |           |           |             |            |          |
|                               |            |     |     |               |     |         | fulmulti-hop |       | question. | To        | addressthis | challenge, |          |
| thatsatisfiesthesedesiderata. |            |     |     | HOTPOTQA      |     | iscol-  |              |       |           |           |             |            |          |
wecarefullydesignapipelinetocollecttext-based
| lected by     | crowdsourcing |     | based   | on  | Wikipedia | ar-      |                     |     |     |                          |     |     |     |
| ------------- | ------------- | --- | ------- | --- | --------- | -------- | ------------------- | --- | --- | ------------------------ | --- | --- | --- |
|               |               |     |         |     |           |          | multi-hopquestions. |     |     | Below,wewillhighlightthe |     |     |     |
| ticles, where | crowd         |     | workers | are | shown     | multiple |                     |     |     |                          |     |     |     |
keydesignchoicesinourpipeline.
| supporting | context | documents |     | and | asked | explic- |     |     |     |     |     |     |     |
| ---------- | ------- | --------- | --- | --- | ----- | ------- | --- | --- | --- | --- | --- | --- | --- |
itly to come up with questions requiring reason- Building a Wikipedia Hyperlink Graph. We
| ing about | all of | the | documents. |     | This | ensures it |     |     |     |     |     |     |     |
| --------- | ------ | --- | ---------- | --- | ---- | ---------- | --- | --- | --- | --- | --- | --- | --- |
usetheentireEnglishWikipediadumpasourcor-
covers multi-hop questions that are more natural, pus.2 In this corpus, we make two observations:
andarenotdesignedwithanypre-existingknowl- (1)hyper-linksintheWikipediaarticlesoftennat-
| edge base | schema | in  | mind. | Moreover, |     | we also |               |     |          |         |     |          |      |
| --------- | ------ | --- | ----- | --------- | --- | ------- | ------------- | --- | -------- | ------- | --- | -------- | ---- |
|           |        |     |       |           |     |         | urally entail | a   | relation | between | two | (already | dis- |
ask the crowd workers to provide the supporting ambiguated) entities in the context, which could
facts they use to answer the question, which we potentially be used to facilitate multi-hop reason-
alsoprovideaspartofthedataset(seeFigure1for ing; (2) the first paragraph of each article often
| an example). | We  | have | carefully |     | designed | a data |          |      |             |     |            |     |         |
| ------------ | --- | ---- | --------- | --- | -------- | ------ | -------- | ---- | ----------- | --- | ---------- | --- | ------- |
|              |     |      |           |     |          |        | contains | much | information |     | that could | be  | queried |
collectionpipelinefor HOTPOTQA,sincethecol- inameaningfulway. Basedontheseobservations,
lectionofhigh-qualitymulti-hopquestionsisnon- we extract all the hyperlinks from the first para-
| trivial. | We hope | that | this pipelinealso |     | sheds | light |        |        |           |           |     |      |           |
| -------- | ------- | ---- | ----------------- | --- | ----- | ----- | ------ | ------ | --------- | --------- | --- | ---- | --------- |
|          |         |      |                   |     |       |       | graphs | of all | Wikipedia | articles. |     | With | these hy- |
on future work in this direction. Finally, we also perlinks,webuildadirectedgraphG,whereeach
collected a novel type of questions—comparison edge (a,b) indicates there is a hyperlink from the
questions—as part of HOTPOTQA, in which we firstparagraphofarticleatoarticleb.
| require | systems | to compare |     | two entities |     | on some |     |     |     |     |     |     |     |
| ------- | ------- | ---------- | --- | ------------ | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
shared properties to test their understanding of Generating Candidate Paragraph Pairs. To
generatemeaningfulpairsofparagraphsformulti-
| both language | and | common |     | concepts | such | as nu- |     |     |     |     |     |     |     |
| ------------- | --- | ------ | --- | -------- | ---- | ------ | --- | --- | --- | --- | --- | --- | --- |
merical magnitude. We make HOTPOTQA pub- hop question answering with G, we start by
liclyavailableathttps://HotpotQA.github.io. considering an example question “when was the
|     |     |     |     |     |     |     | singer and | songwriter |     | of  | Radiohead | born?” | To  |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ---------- | --- | --- | --------- | ------ | --- |
1Thenamecomesfromthefirstthreeauthors’arrivingat
themainideaduringadiscussionatahotpotrestaurant. 2https://dumps.wikimedia.org/

answer this question, one would need to first rea- Algorithm1Overalldatacollectionprocedure
sonthatthe“singerandsongwriterofRadiohead” Input: questiontyperatior 1 = 0.75, yes/noratior 2 =
| is “Thom | Yorke”, |     | and then | figure | out | his birth- | 0.5 |     |     |     |     |     |     |
| -------- | ------- | --- | -------- | ------ | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
whilenotfinisheddo
| day in | the text. | We  | call | “Thom | Yorke” | a bridge |              |     |        |     |     |     |     |
| ------ | --------- | --- | ---- | ----- | ------ | -------- | ------------ | --- | ------ | --- | --- | --- | --- |
|        |           |     |      |       |        |          | ifrandom()<r |     | 1 then |     |     |     |     |
entity in this example. Given an edge (a,b) in Uniformlysampleanentityb∈B
Uniformlysampleanedge(a,b)
| the hyperlink |     | graph | G, the | entity | of b | can usually |     |     |     |     |     |     |     |
| ------------- | --- | ----- | ------ | ------ | ---- | ----------- | --- | --- | --- | --- | --- | --- | --- |
Workersaskaquestionaboutparagraphsaandb
| be viewed | as  | a bridge | entity | that | connects | a and |     |     |     |     |     |     |     |
| --------- | --- | -------- | ------ | ---- | -------- | ----- | --- | --- | --- | --- | --- | --- | --- |
else
b. As we observe articles b usually determine the SamplealistfromL,withprobabilitiesweightedby
listsizes
| theme of | the | shared | context | between |     | a and b, but |     |     |     |     |     |     |     |
| -------- | --- | ------ | ------- | ------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- |
Uniformlysampletwoentities(a,b)fromthelist
| not all | articles | b are | suitable | for | collecting | multi- |              |     |     |        |     |     |     |
| ------- | -------- | ----- | -------- | --- | ---------- | ------ | ------------ | --- | --- | ------ | --- | --- | --- |
|         |          |       |          |     |            |        | ifrandom()<r |     |     | 2 then |     |     |     |
hop questions. For example, entities like coun- Workersaskayes/noquestiontocompareaand
b
| tries are | frequently |     | referred | to  | in Wikipedia, | but |     |     |     |     |     |     |     |
| --------- | ---------- | --- | -------- | --- | ------------- | --- | --- | --- | --- | --- | --- | --- | --- |
else
don’t necessarily have much in common with all Workers ask a question with a span answer to
incoming links. It is also difficult, for instance, compareaandb
endif
| for the | crowd | workers | to  | ask meaningful |     | multi- |     |     |     |     |     |     |     |
| ------- | ----- | ------- | --- | -------------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
endif
hop questions about highly technical entities like Workersprovidethesupportingfacts
| theIPv4protocol. |        | Toalleviatethisissue, |     |          |             | wecon- | endwhile |     |     |     |     |     |     |
| ---------------- | ------ | --------------------- | --- | -------- | ----------- | ------ | -------- | --- | --- | --- | --- | --- | --- |
| strain the       | bridge | entities              |     | to a set | of manually | cu-    |          |     |     |     |     |     |     |
rated pages in Wikipedia (see Appendix A). Af- quiresreasoningoverbothparagraphs.
B,
ter curating a set of pages we create candidate To the best of our knowledge, text-based com-
paragraphpairsbysamplingedges(a,b)fromthe
parisonquestionsareanoveltypeofquestionsthat
| hyperlinkgraphsuchthatb |     |     |     | ∈ B. |     |     |          |      |            |     |          |     |           |
| ----------------------- | --- | --- | --- | ---- | --- | --- | -------- | ---- | ---------- | --- | -------- | --- | --------- |
|                         |     |     |     |      |     |     | have not | been | considered | by  | previous |     | datasets. |
Moreimportantly,answeringthesequestionsusu-
| Comparison |     | Questions. |     | In addition |     | to ques- |     |     |     |     |     |     |     |
| ---------- | --- | ---------- | --- | ----------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
allyrequiresarithmeticcomparison,suchascom-
| tions collected |         | using | bridge |           | entities, | we also    |        |            |       |        |       |          |     |
| --------------- | ------- | ----- | ------ | --------- | --------- | ---------- | ------ | ---------- | ----- | ------ | ----- | -------- | --- |
|                 |         |       |        |           |           |            | paring | ages given | birth | dates, | which | presents | a   |
| collect         | another | type  | of     | multi-hop |           | questions— |        |            |       |        |       |          |     |
newchallengeforfuturemodeldevelopment.
| comparisonquestions. |              |     | Themainideaisthatcom- |          |          |      |            |            |     |        |     |         |     |
| -------------------- | ------------ | --- | --------------------- | -------- | -------- | ---- | ---------- | ---------- | --- | ------ | --- | ------- | --- |
| paring               | two entities |     | from                  | the same | category | usu- |            |            |     |        |     |         |     |
|                      |              |     |                       |          |          |      | Collecting | Supporting |     | Facts. | To  | enhance | the |
allyresultsininterestingmulti-hopquestions,e.g.,
|     |     |     |     |     |     |     | explainability | of  | question | answering |     | systems, | we  |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | -------- | --------- | --- | -------- | --- |
“Who has played for more NBA teams, Michael wantthemtooutputasetofsupportingfactsnec-
Jordan or Kobe Bryant?” To facilitate collecting essary to arrive at the answer, when the answer
| this type | of question, |     | we  | manually | curate | 42 lists |               |     |         |      |         |         |     |
| --------- | ------------ | --- | --- | -------- | ------ | -------- | ------------- | --- | ------- | ---- | ------- | ------- | --- |
|           |              |     |     |          |        |          | is generated. |     | To this | end, | we also | collect | the |
ofsimilarentities(denotedasL)fromWikipedia.3 sentences that determine the answers from crowd
To generate candidate paragraph pairs, we ran- workers. These supporting facts can serve as
| domly | sample | two | paragraphs | from | the | same list |                    |     |     |      |           |     |         |
| ----- | ------ | --- | ---------- | ---- | --- | --------- | ------------------ | --- | --- | ---- | --------- | --- | ------- |
|       |        |     |            |      |     |           | strong supervision |     | for | what | sentences | to  | pay at- |
andpresentthemtothecrowdworker.
|     |     |     |     |     |     |     | tentionto. | Moreover,wecannowtesttheexplain- |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | -------------------------------- | --- | --- | --- | --- | --- |
Toincreasethediversityofmulti-hopquestions, abilityofamodelbycomparingthepredictedsup-
we also introduce a subset of yes/no questions portingfactstothegroundtruthones.
| in comparison |     | questions. |     | This | complements | the |     |     |     |     |     |     |     |
| ------------- | --- | ---------- | --- | ---- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- |
Theoverallprocedureofdatacollectionisillus-
| original | scope | of comparison |     | questions |     | by offer- |     |     |     |     |     |     |     |
| -------- | ----- | ------------- | --- | --------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
tratedinAlgorithm1.
| ing new | ways | to require |     | systems | to  | reason over |     |     |     |     |     |     |     |
| ------- | ---- | ---------- | --- | ------- | --- | ----------- | --- | --- | --- | --- | --- | --- | --- |
3 ProcessingandBenchmarkSettings
| both paragraphs.  |        | For       | example, |      | consider | the en- |              |         |     |       |          |     |          |
| ----------------- | ------ | --------- | -------- | ---- | -------- | ------- | ------------ | ------- | --- | ----- | -------- | --- | -------- |
| tities Iron       | Maiden |           | (from    | the  | UK) and  | AC/DC   |              |         |     |       |          |     |          |
|                   |        |           |          |      |          |         | We collected | 112,779 |     | valid | examples | in  | total on |
| (from Australia). |        | Questions |          | like | “Is Iron | Maiden  |              |         |     |       |          |     |          |
Turk4
|           |        |     |            |         |          |         | Amazon  | Mechanical |         |            | using    | the ParlAI | in-   |
| --------- | ------ | --- | ---------- | ------- | -------- | ------- | ------- | ---------- | ------- | ---------- | -------- | ---------- | ----- |
| or AC/DC  | from   | the | UK?”       | are not | ideal,   | because |         |            |         |            |          |            |       |
|           |        |     |            |         |          |         | terface | (Miller    | et al., | 2017) (see | Appendix |            | A).To |
| one would | deduce |     | the answer |         | is “Iron | Maiden” |         |            |         |            |          |            |       |
isolatepotentialsingle-hopquestionsfromthede-
| even if   | one only   | had      | access | to         | that article. | With      |                 |         |             |          |               |     |         |
| --------- | ---------- | -------- | ------ | ---------- | ------------- | --------- | --------------- | ------- | ----------- | -------- | ------------- | --- | ------- |
|           |            |          |        |            |               |           | sired multi-hop |         | ones,       | we first | split         | out | a sub-  |
| yes/no    | questions, | one      | may    | ask        | “Are Iron     | Maiden    |                 |         |             |          |               |     |         |
|           |            |          |        |            |               |           | set of data     | called  | train-easy. |          | Specifically, |     | we      |
| and AC/DC |            | from the | same   | country?”, |               | which re- |                 |         |             |          |               |     |         |
|           |            |          |        |            |               |           | randomly        | sampled | questions   |          | (∼3–10        | per | Turker) |
3This is achieved by manually curating lists from the from top-contributing turkers, and categorized all
| Wikipedia | “List | of lists | of lists” | (https://wiki.sh/ |     |     |     |     |     |     |     |     |     |
| --------- | ----- | -------- | --------- | ----------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
y8qv).Oneexampleis“HighestMountainsonEarth”. 4https://www.mturk.com/

Name Desc. Usage #Examples to retrieve 8 paragraphs from Wikipedia as dis-
tractors, using the question as the query. We mix
train-easy single-hop training 18,089
train-medium multi-hop training 56,814 them with the 2 gold paragraphs (the ones used
train-hard hardmulti-hop training 15,661
to collect the question and answer) to construct
dev hardmulti-hop dev 7,405
test-distractor hardmulti-hop test 7,405 the distractor setting. The 2 gold paragraphs
test-fullwiki hardmulti-hop test 7,405 and the 8 distractors are shuffled before they are
Total 112,779
fed to the model. In the second setting, we fully
test the model’s ability to locate relevant facts as
Table 1: Data split. The splits train-easy, train-
well as reasoning about them by requiring it to
medium,andtrain-hardarecombinedfortraining. The
answer the question given the first paragraphs of
distractorandfullwikisettingsusedifferenttestsetsso
allWikipediaarticleswithoutthegoldparagraphs
thatthegoldparagraphsinthefullwikitestsetremain
specified. Thisfullwikisettingtrulyteststheper-
unknowntoanymodels.
formanceofthesystems’abilityatmulti-hoprea-
soning in the wild.5 The two settings present dif-
their questions into the train-easy set if an over-
ferent levels of difficulty, and would require tech-
whelming percentage in the sample only required
niquesrangingfromreadingcomprehensiontoin-
reasoning over one of the paragraphs. We sam-
formation retrieval. As shown in Table 1, we use
pled these turkers because they contributed more
separatetestsetsforthetwosettingstoavoidleak-
than70%ofourdata. Thistrain-easysetcontains
ing information, because the gold paragraphs are
18,089mostlysingle-hopexamples.
available to a model in the distractor setting, but
We implemented a question answering model
shouldnotbeaccessibleinthefullwikisetting.
based on the current state-of-the-art architectures,
We also try to understand the model’s good
which we discuss in detail in Section 5.1. Based performance on the train-medium split. Manual
on this model, we performed a three-fold cross
analysis shows that the ratio of multi-hop ques-
validation on the remaining multi-hop examples. tionsintrain-mediumissimilartothatofthehard
Among these examples, the models were able to examples (93.3% in train-medium vs. 92.0% in
correctly answer 60% of the questions with high dev), but one of the question types appears more
confidence(determinedbythresholdingthemodel frequently in train-medium compared to the hard
loss). Thesecorrectly-answeredquestions(56,814 splits (Type II: 32.0% in train-medium vs. 15.0%
in total, 60% of the multi-hop examples) are split in dev, see Section 4 for the definition of Type II
outandmarkedasthetrain-mediumsubset,which
questions). These observations demonstrate that
willalsobeusedaspartofourtrainingset.
given enough training data, existing neural archi-
Aftersplittingouttrain-easyandtrain-medium, tecturescanbetrainedtoanswercertaintypesand
we are left with hard examples. As our ultimate certain subsets of the multi-hop questions. How-
goalistosolvemulti-hopquestionanswering,we ever, train-medium remains challenging when not
focus on questions that the latest modeling tech- just the gold paragraphs are present—we show in
niques are not able to answer. Thus we constrain AppendixCthattheretrievalproblemontheseex-
ourdevandtestsetstobehardexamples. Specif- amplesareasdifficultasthatontheirhardcousins.
ically,werandomlydividethehardexamplesinto
four subsets, train-hard, dev, test-distractor, and 4 DatasetAnalysis
test-fullwiki. Statistics about the data split can be
In this section, we analyze the types of questions,
found in Table 1. In Section 5, we will show that
typesofanswers,andtypesofmulti-hopreasoning
combining train-easy, train-medium, and train-
coveredinthedataset.
hard to train models yields the best performance,
so we use the combined set as our default train- Question Types. We heuristically identified
ing set. The two test sets test-distractor and test- question types for each collected question. To
fullwiki are used in two different benchmark set- identify the question type, we first locate the cen-
tings,whichweintroducenext. tral question word (CQW) in the question. Since
We create two benchmark settings. In the first HOTPOTQA contains comparison questions and
setting,tochallengethemodeltofindthetruesup-
5Aswerequiredthecrowdworkerstousecompleteen-
portingfactsinthepresenceofnoise,foreachex-
titynamesinthequestion,themajorityofthequestionsare
ampleweemploybigramtf-idf(Chenetal.,2017) unambiguousinthefullwikisetting.

|     |     |     |     |     |     |     | AnswerType |           | %                         | Example(s)                |                |         |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --------- | ------------------------- | ------------------------- | -------------- | ------- |
|     |     |     |     |     |     |     | Person     |           | 30                        | KingEdwardII,Rihanna      |                |         |
|     |     |     |     |     |     |     | Group/Org  |           | 13                        | Cartoonito,Apalachee      |                |         |
|     |     |     |     |     |     |     | Location   |           | 10                        | FortRichardson,California |                |         |
|     |     |     |     |     |     |     | Date       |           | 9                         | 10thoreven13thcentury     |                |         |
|     |     |     |     |     |     |     | Number     |           | 8                         | 79.92million,17           |                |         |
|     |     |     |     |     |     |     | Artwork    |           | 8                         | DieschweigsameFrau        |                |         |
|     |     |     |     |     |     |     | Yes/No     |           | 6                         | -                         |                |         |
|     |     |     |     |     |     |     | Adjective  |           | 4                         | conservative              |                |         |
|     |     |     |     |     |     |     | Event      |           | 1                         | PrixBenoisdelaDanse       |                |         |
|     |     |     |     |     |     |     | Other      | proper    | 6                         | Cold War,                 | Laban Movement |         |
|     |     |     |     |     |     |     | noun       |           |                           | Analysis                  |                |         |
|     |     |     |     |     |     |     | Commonnoun |           | 5                         | comedy,bothmenandwomen    |                |         |
|     |     |     |     |     |     |     | Table2:    |           | TypesofanswersinHOTPOTQA. |                           |                |         |
|     |     |     |     |     |     |     | Multi-hop  | Reasoning |                           | Types.                    | We also        | sampled |
100examplesfromthedevandtestsetsandman-
|           |       |               |                |     |           |     | ually classified    |     | the types | of                     | reasoning required | to  |
| --------- | ----- | ------------- | -------------- | --- | --------- | --- | ------------------- | --- | --------- | ---------------------- | ------------------ | --- |
| Figure 2: | Types | of questions  | covered        | in  | HOTPOTQA. |     |                     |     |           |                        |                    |     |
|           |       |               |                |     |           |     | answereachquestion. |     |           | Besidescomparingtwoen- |                    |     |
| Question  | types | are extracted | heuristically, |     | starting  | at  |                     |     |           |                        |                    |     |
tities,therearethreemaintypesofmulti-hoprea-
| questionwordsorprepositionsprecedingthem. |     |          |          |          |     | Empty   |        |          |           |       |            |       |
| ----------------------------------------- | --- | -------- | -------- | -------- | --- | ------- | ------ | -------- | --------- | ----- | ---------- | ----- |
|                                           |     |          |          |          |     |         | soning | required | to answer | these | questions, | which |
| colored blocks                            |     | indicate | suffixes | that are | too | rare to |        |          |           |       |            |       |
showindividually. Seemaintextformoredetails. weshowinTable3accompaniedwithexamples.
|                      |         |                          |         |             |               |       | Most                                  | of the  | questions | require     | at least      | one sup- |
| -------------------- | ------- | ------------------------ | ------- | ----------- | ------------- | ----- | ------------------------------------- | ------- | --------- | ----------- | ------------- | -------- |
|                      |         |                          |         |             |               |       | portingfactfromeachparagraphtoanswer. |         |           |             |               | Ama-     |
| yes/no questions,    |         | we consider              |         | as question |               | words |                                       |         |           |             |               |          |
|                      |         |                          |         |             |               |       | jority of                             | sampled | questions |             | (42%) require | chain    |
| WH-words,            | copulas | (“is”,                   | “are”), |             | and auxiliary |       |                                       |         |           |             |               |          |
|                      |         |                          |         |             |               |       | reasoning                             | (Type   | I in      | the table), | where the     | reader   |
| verbs(“does”,“did”). |         | Becausequestionsoftenin- |         |             |               |       |                                       |         |           |             |               |          |
mustfirstidentifyabridgeentitybeforethesecond
| volve relative | clauses | beginning |           | with     | WH-words, |     |                                       |     |     |     |     |     |
| -------------- | ------- | --------- | --------- | -------- | --------- | --- | ------------------------------------- | --- | --- | --- | --- | --- |
|                |         |           |           |          |           |     | hopcanbeansweredbyfillinginthebridge. |     |     |     |     | One |
| we define      | the     | CQW as    | the first | question | word      | in  |                                       |     |     |     |     |     |
strategytoanswerthesequestionswouldbetode-
thequestionifitcanbefoundinthefirstthreeto-
kens, or the last question word otherwise. Then, compose them into consecutive single-hop ques-
|              |     |          |      |               |     |       | tions. | The bridge | entity | could | also be used | im- |
| ------------ | --- | -------- | ---- | ------------- | --- | ----- | ------ | ---------- | ------ | ----- | ------------ | --- |
| we determine |     | question | type | by extracting |     | words |        |            |        |       |              |     |
plicitlytohelpinferpropertiesofotherentitiesre-
upto2tokensawaytotherightoftheCQW,along
|     |     |     |     |     |     |     | latedtoit. | Insomequestions(TypeIII),theentity |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ---------------------------------- | --- | --- | --- | --- |
withthetokentotheleftifitisoneofafewcom-
inquestionsharescertainpropertieswithabridge
| mon prepositions |     | (e.g., | in the | cases | of “in which” |     |               |      |     |              |        |         |
| ---------------- | --- | ------ | ------ | ----- | ------------- | --- | ------------- | ---- | --- | ------------ | ------ | ------- |
|                  |     |        |        |       |               |     | entity (e.g., | they | are | collocated), | and we | can in- |
and“bywhom”).
|              |     |                  |     |             |     |       | fer its | properties | through | the | bridge entity. | An- |
| ------------ | --- | ---------------- | --- | ----------- | --- | ----- | ------- | ---------- | ------- | --- | -------------- | --- |
| We visualize |     | the distribution |     | of question |     | types |         |            |         |     |                |     |
inFigure2,andlabeltheonessharedamongmore othertypeofquestioninvolveslocatingtheanswer
entitybysatisfyingmultiplepropertiessimultane-
| than250questions. |         | Asisshown, |           | ourdatasetcov- |        |     |                     |     |     |                      |     |     |
| ----------------- | ------- | ---------- | --------- | -------------- | ------ | --- | ------------------- | --- | --- | -------------------- | --- | --- |
|                   |         |            |           |                |        |     | ously(TypeII).Here, |     |     | toanswerthequestion, |     | one |
| ers a diverse     | variety | of         | questions | centered       | around |     |                     |     |     |                      |     |     |
couldfindthesetofallentitiesthatsatisfyeachof
| entities, | locations, | events, | dates, | and | numbers, | as  |     |     |     |     |     |     |
| --------- | ---------- | ------- | ------ | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
thepropertiesmentioned,andtakeanintersection
wellasyes/noquestionsdirectedatcomparingtwo
|     |     |     |     |     |     |     | toarriveatthefinalanswer. |     |     |     | Questionscomparing |     |
| --- | --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- | --- | ------------------ | --- |
entities(“ArebothAandB...?”),tonameafew.
twoentities(Comparison)alsorequirethesystem
Answer Types. We further sample 100 exam- to understand the properties in question about the
plesfromthedataset,andpresentthetypesofan- two entities (e.g., nationality), and sometimes re-
swers in Table 2. As can be seen, HOTPOTQA quire arithmetic such as counting (as seen in the
covers a broad range of answer types, which table) or comparing numerical values (“Who is
matchesourinitialanalysisofquestiontypes. We older, A or B?”). Finally, we find that sometimes
find that a majority of the questions are about en- the questions require more than two supporting
tities in the articles (68%), and a non-negligible facts to answer (Other). In our analysis, we also
amountofquestionsalsoaskaboutvariousproper- find that for all of the examples shown in the ta-
tieslikedate(9%)andotherdescriptiveproperties ble, the supporting facts provided by the Turkers
suchasnumbers(8%)andadjectives(4%). matchexactlywiththelimitedcontextshownhere,

| ReasoningType |     | % Example(s) |     |     |     |     |     |
| ------------- | --- | ------------ | --- | --- | --- | --- | --- |
Inferring the bridge 42 Paragraph A: The 2015 Diamond Head Classic was a college basketball tournament ...
| entity to | complete | BuddyHieldwasnamedthetournament’sMVP. |     |     |     |     |     |
| --------- | -------- | ------------------------------------- | --- | --- | --- | --- | --- |
the 2nd-hop question Paragraph B: Chavano Rainier ”Buddy” Hield is a Bahamian professional basketball
| (TypeI) |     | playerfortheSacramentoKingsoftheNBA... |     |     |     |     |     |
| ------- | --- | -------------------------------------- | --- | --- | --- | --- | --- |
Q:Whichteamdoestheplayernamed2015DiamondHeadClassic’sMVPplayfor?
Comparing two enti- 27 Paragraph A: LostAlone were a British rock band ... consisted of Steven Battelle, Alan
| ties(Comparison) |     | Williamson,andMarkGibson... |     |     |     |     |     |
| ---------------- | --- | --------------------------- | --- | --- | --- | --- | --- |
Paragraph B: Guster is an American alternative rock band ... Founding members Adam
Gardner,RyanMiller,andBrianRosenworcelbegan...
Q:DidLostAloneandGusterhavethesamenumberofmembers?(yes)
ParagraphA:SeveralcurrentandformermembersofthePittsburghPirates
| Locating  | the answer | 15                         |     |     |     |     | ...JohnMilner, |
| --------- | ---------- | -------------------------- | --- | --- | --- | --- | -------------- |
| entity by | checking   | DaveParker,andRodScurry... |     |     |     |     |                |
ParagraphB:DavidGeneParker,nicknamed”TheCobra”,isanAmericanformerplayer
| multiple | properties |                          |     |     |     |     |     |
| -------- | ---------- | ------------------------ | --- | --- | --- | --- | --- |
| (TypeII) |            | inMajorLeagueBaseball... |     |     |     |     |     |
Q:WhichformermemberofthePittsburghPirateswasnicknamed”TheCobra”?
Inferring about the 6 ParagraphA:MarineTacticalAirCommandSquadron28isaUnitedStatesMarineCorps
property of an entity aviationcommandandcontrolunitbasedatMarineCorpsAirStationCherryPoint...
in question through ParagraphB:MarineCorpsAirStationCherryPoint... isaUnitedStatesMarineCorps
| a bridge | entity (Type | airfieldlocatedinHavelock,NorthCarolina,USA...   |     |     |     |     |     |
| -------- | ------------ | ------------------------------------------------ | --- | --- | --- | --- | --- |
| III)     |              | Q:WhatcityistheMarineAirControlGroup28locatedin? |     |     |     |     |     |
Other typesof reason- 2 ParagraphA:...thetownsofYodobashi,Okubo,Totsuka,andOchiaitownweremerged
ing that require more intoYodobashiward....YodobashiCameraisastorewithitsnametakenfromthetownand
| than two | supporting | ward. |     |     |     |     |     |
| -------- | ---------- | ----- | --- | --- | --- | --- | --- |
facts(Other) ParagraphB:YodobashiCameraCo.,Ltd. isamajorJapaneseretailchainspecializingin
electronics,PCs,camerasandphotographicequipment.
Q:AsidefromYodobashi,whatothertownsweremergedintothewardwhichgavethemajor
Japaneseretailchainspecializinginelectronics,PCs,cameras,andphotographicequipment
it’sname?
Table3:Typesofmulti-hopreasoningrequiredtoanswerquestionsintheHOTPOTQAdevandtestsets. Weshow
inorangebolditalicsbridgeentitiesifapplicable, blueitalicssupportingfactsfromtheparagraphsthatconnect
directlytothequestion,andgreenboldtheanswerintheparagraphorfollowingthequestion. Theremaining8%
aresingle-hop(6%)orunanswerablequestions(2%)byourjudgement.
showing that the supporting facts collected are of cal advances on question answering, including
| highquality. |     |     |     | character-levelmodels,self-attention(Wangetal., |     |     |     |
| ------------ | --- | --- | --- | ----------------------------------------------- | --- | --- | --- |
Aside from the reasoning types mentioned 2017),andbi-attention(Seoetal.,2017). Combin-
above,wealsoestimatethatabout6%ofthesam- ingthesethreekeycomponentsisbecomingstan-
pled questions can be answered with one of the dardpractice,andvariousstate-of-the-artorcom-
two paragraphs, and 2% of them unanswerable. petitive architectures (Liu et al., 2018; Clark and
We also randomly sampled 100 examples from Gardner,2017;Wangetal.,2017;Seoetal.,2017;
|              |                |           |         | Pan et al., | 2017; Salant | and Berant, | 2018; Xiong |
| ------------ | -------------- | --------- | ------- | ----------- | ------------ | ----------- | ----------- |
| train-medium | and train-hard | combined, | and the |             |              |             |             |
proportions of reasoning types are: Type I 38%, et al., 2018) on SQuAD can be viewed as simi-
Type II 29%, Comparison 20%, Other 7%, Type lar to our implemented model. To accommodate
III2%,single-hop2%,andunanswerable2%. yes/no questions, we also add a 3-way classifier
|     |     |     |     | after the | last recurrent layer | to produce | the prob- |
| --- | --- | --- | --- | --------- | -------------------- | ---------- | --------- |
5 Experiments abilities of “yes”, “no”, and span-based answers.
Duringdecoding,wefirstusethe3-wayoutputto
5.1 ModelArchitectureandTraining
|     |     |     |     | determinewhethertheansweris“yes”, |     |     | “no”, ora |
| --- | --- | --- | --- | --------------------------------- | --- | --- | --------- |
To test the performance of leading QA systems textspan. Ifitisatextspan,wefurthersearchfor
on our data, we reimplemented the architecture themostprobablespan.
| described | in Clark and | Gardner (2017) | as our |     |     |     |     |
| --------- | ------------ | -------------- | ------ | --- | --- | --- | --- |
baseline model. We note that our implementa- Supporting Facts as Strong Supervision. To
tion without weight averaging achieves perfor- evaluatethebaselinemodel’sperformanceinpre-
mance very close to what the authors reported dicting explainable supporting facts, as well as
on SQuAD (about 1 point worse in F ). Our how much they improve QA performance, we
1
implemented model subsumes the latest techni- additionally design a component to incorporate

Linear Yes/no/span Table 5. After retrieving these 10 paragraphs, we
thenusethemodeltrainedinthedistractorsetting
RNN
to evaluate its performance on these final candi-
Linear End token dateparagraphs.
concat Following previous work (Rajpurkar et al.,
RNN 2016), we use exact match (EM) and F as two
1
Linear Start token evaluationmetrics. Toassesstheexplainabilityof
concat the models, we further introduce two sets of met-
RNN ricsinvolvingthesupportingfacts. Thefirstsetfo-
cuses on evaluating the supporting facts directly,
concat
RNN 0/1 namely EM and F on the set of supporting fact
1
(is supporting facts?)
Self-Attention sentencesascomparedtothegoldset. Thesecond
Strong supervision
set features joint metrics that combine the evalu-
RNN residual
ation of answer spans and supporting facts as fol-
lows. For each example, given its precision and
Bi-Attention
recall on the answer span (P(ans),R(ans)) and the
RNN RNN supporting facts (P(sup),R(sup)), respectively, we
calculatejointF as
Char RNN Word emb Char RNN Word emb 1
paragraphs question P(joint) = P(ans)P(sup), R(joint) = R(ans)R(sup),
Figure 3: Our model architecture. Strong supervision 2P(joint)R(joint)
oversupportingfactsisusedinamulti-tasksetting. JointF = .
1 P(joint)+R(joint)
Joint EM is 1 only if both tasks achieve an ex-
such strong supervision into our model. For each
act match and otherwise 0. Intuitively, these met-
sentence, we concatenate the output of the self-
rics penalize systems that perform poorly on ei-
attention layer at the first and last positions, and
ther task. All metrics are evaluated example-by-
use a binary linear classifier to predict the prob-
example, and then averaged over examples in the
ability that the current sentence is a supporting
evaluationset.
fact. We minimize a binary cross entropy loss for
The performance of our model on the bench-
this classifier. This objective is jointly optimized
mark settings is reported in Table 4, where all
with the normal question answering objective in
numbersareobtainedwithstrongsupervisionover
a multi-task learning setting, and they share the
supportingfacts. Fromthedistractorsettingtothe
same low-level representations. With this classi-
full wiki setting, expanding the scope of the con-
fier,themodelcanalsobeevaluatedonthetaskof
textincreasesthedifficultyofquestionanswering.
supportingfactpredictiontogaugeitsexplainabil-
The performance in the full wiki setting is sub-
ity. OuroverallarchitectureisillustratedinFigure
stantially lower, which poses a challenge to exist-
3. Thoughitispossibletobuildapipelinesystem,
ingtechniquesonretrieval-basedquestionanswer-
inthisworkwefocusonanend-to-endone,which
ing. Overall, model performance in all settings
iseasiertotuneandfastertotrain.
is significantly lower than human performance as
5.2 Results shown in Section 5.3, which indicates that more
technicaladvancementsareneededinfuturework.
We evaluate our model in the two benchmark set-
We also investigate the explainability of our
tings. Inthefullwikisetting,toenableefficienttf-
model by measuring supporting fact prediction
idf retrieval among 5,000,000+ wiki paragraphs,
performance. Our model achieves 60+ support-
givenaquestionwefirstreturnacandidatepoolof
ingfactpredictionF and∼40jointF ,whichin-
atmost5,000paragraphsusinganinverted-index- 1 1
dicates there is room for further improvement in
basedfilteringstrategy6 andthenselectthetop10
termsofexplainability.
paragraphsinthepoolasthefinalcandidatesusing
In Table 6, we break down the performance
bigram tf-idf.7 Retrieval performance is shownin
on different question types. In the distractor set-
6SeeAppendixCfordetails.
ting, comparison questions have lower F scores
1
7Wechoosethenumberoffinalcandidatesas10tostay
consistentwiththedistractorsettingwherecandidatesare2 goldparagraphsplus8distractors.

|     |     |            |     |       | Answer |       | SupFact |       | Joint |       |     |     |
| --- | --- | ---------- | --- | ----- | ------ | ----- | ------- | ----- | ----- | ----- | --- | --- |
|     |     | Setting    |     | Split |        |       |         |       |       |       |     |     |
|     |     |            |     |       | EM     | F     | EM      | F     | EM    | F     |     |     |
|     |     |            |     |       |        | 1     |         | 1     |       | 1     |     |     |
|     |     | distractor |     | dev   | 44.44  | 58.28 | 21.95   | 66.66 | 11.56 | 40.86 |     |     |
|     |     | distractor |     | test  | 45.46  | 58.99 | 22.24   | 66.62 | 12.04 | 41.37 |     |     |
|     |     | fullwiki   |     | dev   | 24.68  | 34.36 | 5.28    | 40.98 | 2.54  | 17.73 |     |     |
|     |     | fullwiki   |     | test  | 25.23  | 34.40 | 5.07    | 40.69 | 2.63  | 17.85 |     |     |
Table4:Mainresults:theperformanceofquestionansweringandsupportingfactpredictioninthetwobenchmark
settings. Weencourageresearcherstoreportthesemetricswhenevaluatingtheirmethods.
| Set | MAP | MeanRank | Hits@2 |     | Hits@10 |     | Setting |     |     |     | EM  | F   |
| --- | --- | -------- | ------ | --- | ------- | --- | ------- | --- | --- | --- | --- | --- |
1
| dev  | 43.93 | 314.71 | 39.43 |     | 56.06 |     | ourmodel               |     |     |     | 44.44 | 58.28 |
| ---- | ----- | ------ | ----- | --- | ----- | --- | ---------------------- | --- | --- | --- | ----- | ----- |
| test | 43.21 | 314.05 | 38.67 |     | 55.88 |     |                        |     |     |     |       |       |
|      |       |        |       |     |       |     | –supfact               |     |     |     | 42.79 | 56.19 |
|      |       |        |       |     |       |     | –supfact,selfattention |     |     |     | 41.59 | 55.19 |
Table5: Retrievalperformanceinthefullwikisetting.
|     |     |     |     |     |     |     | –supfact,charmodel |     |     |     | 41.66 | 55.25 |
| --- | --- | --- | --- | --- | --- | --- | ------------------ | --- | --- | --- | ----- | ----- |
MeanRankisaveragedovertheranksoftwogoldpara-
| graphs.    |             |           |             |           |       |       | –supfact,train-easy              |                                         |         |                   | 41.61    | 55.12  |
| ---------- | ----------- | --------- | ----------- | --------- | ----- | ----- | -------------------------------- | --------------------------------------- | ------- | ----------------- | -------- | ------ |
|            |             |           |             |           |       |       | –supfact,train-easy,train-medium |                                         |         |                   | 31.07    | 43.61  |
|            |             |           |             |           |       |       | goldonly                         |                                         |         |                   | 48.38    | 63.58  |
| Setting    |             | BrEM      | BrF CpEM    |           | CpF   |       |                                  |                                         |         |                   |          |        |
|            |             |           | 1           |           | 1     |       | supfactonly                      |                                         |         |                   | 51.95    | 66.98  |
| distractor |             | 43.41     | 59.09 48.55 |           | 55.05 |       |                                  |                                         |         |                   |          |        |
| fullwiki   |             | 19.76     | 30.42 43.87 |           | 50.70 |       |                                  |                                         |         |                   |          |        |
|            |             |           |             |           |       |       | Table7:                          | Ablationstudyofquestionansweringperfor- |         |                   |          |        |
|            |             |           |             |           |       |       | mance                            | on the                                  | dev set | in the distractor | setting. | “– sup |
| Table 6:   | Performance | breakdown | over        | different |       | ques- |                                  |                                         |         |                   |          |        |
fact”meansremovingstrongsupervisionoversupport-
| tiontypesonthedevsetinthedistractorsetting. |           |           |       |        |           | “Br” |                       |       |            |                          |           |             |
| ------------------------------------------- | --------- | --------- | ----- | ------ | --------- | ---- | --------------------- | ----- | ---------- | ------------------------ | --------- | ----------- |
|                                             |           |           |       |        |           |      | ingfactsfromourmodel. |       |            | “–train-easy”and“–train- |           |             |
| denotes                                     | questions | collected | using | bridge | entities, | and  |                       |       |            |                          |           |             |
|                                             |           |           |       |        |           |      | medium”               | means | discarding | the                      | according | data splits |
“Cp”denotescomparisonquestions.
|     |     |     |     |     |     |     | from training. |     | “gold | only” and | “sup fact | only” refer |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ----- | --------- | --------- | ----------- |
tousingthegoldparagraphsorthesupportingfactsas
theonlycontextinputtothemodel.
thanquestionsinvolvingbridgeentities(asdefined
| in Section | 2), | which | indicates | that | better mod- |     |     |     |     |     |     |     |
| ---------- | --- | ----- | --------- | ---- | ----------- | --- | --- | --- | --- | --- | --- | --- |
eling this novel question type might need better model,whichachievesa10+F improvementover
1
neural architectures. In the full wiki setting, the notusingthesupportingfacts. Comparedwiththe
gainofstrongsupervisioninourmodel(∼2points
| performance | of  | bridge | entity questions |     | drops | sig- |     |     |     |     |     |     |
| ----------- | --- | ------ | ---------------- | --- | ----- | ---- | --- | --- | --- | --- | --- | --- |
nificantly while that of comparison questions de- inF ),ourproposedmethodofincorporatingsup-
1
creases only marginally. This is because both en- porting facts supervision is most likely subopti-
tities usually appear in the comparison questions, mal, and we leave the challenge of better model-
and thus reduces the difficulty of retrieval. Com- ingtofuturework. Atlast, weshowthatcombin-
bined with the retrieval performance in Table 5, ing all data splits (train-easy, train-medium, and
we believe that the deterioration in the full wiki train-hard) yields the best performance, which is
adoptedasthedefaultsetting.
settinginTable4islargelyduetothedifficultyof
retrievingbothentities.
|            |     |             |       |        |            |     | 5.3 EstablishingHumanPerformance |     |     |     |     |     |
| ---------- | --- | ----------- | ----- | ------ | ---------- | --- | -------------------------------- | --- | --- | --- | --- | --- |
| We perform |     | an ablation | study | in the | distractor |     |                                  |     |     |     |     |     |
setting,andreporttheresultsinTable7. Bothself- To establish human performance on our dataset,
attention and character-level models contribute we randomly sampled 1,000 examples from the
notably to the final performance, which is consis- dev and test sets, and had at least three additional
tent with prior work. This means that techniques Turkers provide answers and supporting facts for
targeted at single-hop QA are still somewhat ef- these examples. As a baseline, we treat the orig-
fective in our setting. Moreover, removing strong inal Turker during data collection as the predic-
supervision over supporting facts decreases per- tion,andthenewlycollectedanswersandsupport-
formance,whichdemonstratestheeffectivenessof ing facts as references, to evaluate human perfor-
ourapproachandtheusefulnessofthesupporting mance. For each example, we choose the answer
facts. Weestablishanestimateoftheupperbound andsupportingfactreferencethatmaximizetheF
1
ofstrongsupervisionbyonlyconsideringthesup- scoretoreportthefinalmetricstoreducetheeffect
porting facts as the oracle context input to our ofambiguity(Rajpurkaretal.,2016).

Answer SpFact Joint supportingdocumentsarecollectedaftertheques-
Setting
EM F EM F EM F tion answer pairs with information retrieval, the
|     |     |     | 1   |     | 1   | 1   |     |     |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
questionsarenotguaranteedtoinvolveinteresting
| goldonly | 65.87 | 74.67 | 59.76 | 90.41 | 41.54 | 68.15 |     |     |     |     |     |     |     |
| -------- | ----- | ----- | ----- | ----- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- |
distractor 60.88 68.99 30.99 74.67 20.06 52.37 reasoningbetweenmultipledocuments.
Human 83.60 91.40 61.50 90.04 52.30 82.55 KB-based multi-hop datasets. Recent datasets
| HumanUB | 96.80 | 98.77 | 87.40 | 97.56 | 84.60 | 96.37 |               |     |        |         |       |     |      |
| ------- | ----- | ----- | ----- | ----- | ----- | ----- | ------------- | --- | ------ | ------- | ----- | --- | ---- |
|         |       |       |       |       |       |       | like QAngaroo |     | (Welbl | et al., | 2018) | and | COM- |
PLEXWEBQUESTIONS(TalmorandBerant,2018)
Table8: Comparingbaselinemodelperformancewith
exploredifferentapproachesofusingpre-existing
| human performance |     | on  | 1,000 | random | samples. | “Hu- |     |     |     |     |     |     |     |
| ----------------- | --- | --- | ----- | ------ | -------- | ---- | --- | --- | --- | --- | --- | --- | --- |
knowledgebases(KB)withpre-definedlogicrules
manUB”standsfortheupperboundonannotatorper-
formance on HOTPOTQA. For details please refer to togeneratevalidQApairs,totestQAmodels’ca-
| themainbody. |            |         |       |             |          |           | pability     | of performing |         | multi-hop     | reasoning. |            | The    |
| ------------ | ---------- | ------- | ----- | ----------- | -------- | --------- | ------------ | ------------- | ------- | ------------- | ---------- | ---------- | ------ |
|              |            |         |       |             |          |           | diversity    | of questions  |         | and answers   |            | is largely | lim-   |
|              |            |         |       |             |          |           | ited by      | the fixed     | KB      | schemas       | or         | logical    | forms. |
| As can       | be         | seen in | Table | 8, the      | original | crowd     |              |               |         |               |            |            |        |
|              |            |         |       |             |          |           | Furthermore, |               | some of | the questions |            | might      | be an- |
| worker       | achieves   | very    | high  | performance |          | in both   |              |               |         |               |            |            |        |
|              |            |         |       |             |          |           | swerable     | by one        | text    | sentence      | due        | to the     | incom- |
| finding      | supporting | facts,  | and   | answering   |          | the ques- |              |               |         |               |            |            |        |
pletenessofKBs.
| tioncorrectly. |         | Ifthebaselinemodelwereprovided |     |            |     |          |           |                   |     |     |           |     |     |
| -------------- | ------- | ------------------------------ | --- | ---------- | --- | -------- | --------- | ----------------- | --- | --- | --------- | --- | --- |
| with the       | correct | supporting                     |     | paragraphs |     | to begin |           |                   |     |     |           |     |     |
|                |         |                                |     |            |     |          | Free-form | answer-generation |     |     | datasets. |     | MS  |
with, it achieves parity with the crowd worker MARCO(Nguyenetal.,2016)contains100kuser
in finding supporting facts, but still falls short at queries from Bing Search with human generated
| finding | the actual | answer. |     | When | distractor | para- |          |         |          |     |           |     |         |
| ------- | ---------- | ------- | --- | ---- | ---------- | ----- | -------- | ------- | -------- | --- | --------- | --- | ------- |
|         |            |         |     |      |            |       | answers. | Systems | generate |     | free-form |     | answers |
graphs are present, the performance gap between and are evaluated by automatic metrics such as
the baseline model and the crowd worker on both ROUGE-L and BLEU-1. However, the reliabil-
| tasksisenlargedto∼30%forbothEMandF |     |     |     |     |     | .   |              |         |     |              |     |         |      |
| ---------------------------------- | --- | --- | --- | --- | --- | --- | ------------ | ------- | --- | ------------ | --- | ------- | ---- |
|                                    |     |     |     |     |     | 1   | ity of these | metrics | is  | questionable |     | because | they |
We further establish the upper bound of human have been shown to correlate poorly with human
performance in HOTPOTQA, by taking the maxi- judgement(Novikovaetal.,2017).
| mum EM                                      | and        | F 1 for  | each example. |          | Here,       | we use |               |           |       |     |              |     |          |
| ------------------------------------------- | ---------- | -------- | ------------- | -------- | ----------- | ------ | ------------- | --------- | ----- | --- | ------------ | --- | -------- |
| eachTurker’sanswerinturnastheprediction,and |            |          |               |          |             |        | 7 Conclusions |           |       |     |              |     |          |
| evaluate                                    | it against | all      | other         | workers’ | answers.    | As     |               |           |       |     |              |     |          |
|                                             |            |          |               |          |             |        | We present    | HOTPOTQA, |       | a   | large-scale  |     | question |
| can be                                      | seen       | in Table | 8, most       | of       | the metrics | are    |               |           |       |     |              |     |          |
|                                             |            |          |               |          |             |        | answering     | dataset   | aimed | at  | facilitating | the | devel-   |
closeto100%,illustratingthatonmostexamples,
opmentofQAsystemscapableofperformingex-
| at least     | a subset | of Turkers      |       | agree      | with each | other,     |                 |           |           |       |               |         |         |
| ------------ | -------- | --------------- | ----- | ---------- | --------- | ---------- | --------------- | --------- | --------- | ----- | ------------- | ------- | ------- |
|              |          |                 |       |            |           |            | plainable,      | multi-hop | reasoning |       | over          | diverse | nat-    |
| showing      | high     | inter-annotator |       | agreement. |           | We also    |                 |           |           |       |               |         |         |
|              |          |                 |       |            |           |            | ural language.  |           | We also   | offer | a new         | type    | of fac- |
| note that    | crowd    | workers         | agree | less       | on        | supporting |                 |           |           |       |               |         |         |
|              |          |                 |       |            |           |            | toid comparison |           | questions | to    | test systems’ |         | ability |
| facts, which |          | could reflect   |       | that this  | task      | is inher-  |                 |           |           |       |               |         |         |
toextractandcomparevariousentitypropertiesin
entlymoresubjectivethanansweringthequestion.
text.
6 RelatedWork
Acknowledgements
Variousrecently-proposedlarge-scaleQAdatasets ThisworkispartlyfundedbytheFacebookParlAI
canbecategorizedinfourcategories.
|                 |         |                 |     |         |            |            | Research       | Award. | ZY,       | WWC,       | and            | RS          | are sup- |
| --------------- | ------- | --------------- | --- | ------- | ---------- | ---------- | -------------- | ------ | --------- | ---------- | -------------- | ----------- | -------- |
|                 |         |                 |     |         |            |            | ported         | by a   | Google    | grant,     | the DARPA      |             | grant    |
| Single-document |         | datasets.       |     | SQuAD   | (Rajpurkar |            |                |        |           |            |                |             |          |
|                 |         |                 |     |         |            |            | D17AP00001,    |        | the ONR   | grants     | N000141512791, |             |          |
| et al., 2016,   |         | 2018) questions |     | that    | are        | relatively |                |        |           |            |                |             |          |
|                 |         |                 |     |         |            |            | N000141812861, |        | and       | the Nvidia | NVAIL          |             | Award.   |
| simple          | because | they usually    |     | require | no         | more than  |                |        |           |            |                |             |          |
|                 |         |                 |     |         |            |            | SZ and         | YB are | supported | by         | Mila,          | Universite´ | de       |
onesentenceintheparagraphtoanswer.
|     |     |     |     |     |     |     | Montre´al. | PQandCDMaresupportedbytheNa- |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ---------------------------- | --- | --- | --- | --- | --- |
Multi-document datasets. TriviaQA (Joshi tional Science Foundation under Grant No. IIS-
et al., 2017) and SearchQA (Dunn et al., 2017) 1514268. Anyopinions,findings,andconclusions
contain question answer pairs that are accompa- orrecommendationsexpressedinthismaterialare
niedwithmorethanonedocumentasthecontext. those of the authors and do not necessarily reflect
This further challenges QA systems’ ability to theviewsoftheNationalScienceFoundation.
| accommodatelongercontexts. |     |     |     | However,sincethe |     |     |     |     |     |     |     |     |     |
| -------------------------- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |

| References |            |         |              |     |            |       | PranavRajpurkar,JianZhang,KonstantinLopyrev,and |               |                            |          |                |     |     |
| ---------- | ---------- | ------- | ------------ | --- | ---------- | ----- | ----------------------------------------------- | ------------- | -------------------------- | -------- | -------------- | --- | --- |
|            |            |         |              |     |            |       | PercyLiang.2016.                                |               | SQuAD:100,000+questionsfor |          |                |     |     |
| DanqiChen, | AdamFisch, |         | JasonWeston, |     | andAntoine |       |                                                 |               |                            |          |                |     |     |
|            |            |         |              |     |            |       | machine                                         | comprehension |                            | of text. | In Proceedings |     | of  |
| Bordes.    | 2017.      | Reading | Wikipedia    |     | to answer  | open- |                                                 |               |                            |          |                |     |     |
the2016ConferenceonEmpiricalMethodsinNat-
| domain | questions. |     | In Association |     | for | Computa- |     |     |     |     |     |     |     |
| ------ | ---------- | --- | -------------- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
uralLanguageProcessing(EMNLP).
tionalLinguistics(ACL).
|             |       |     |      |          |       |        | Shimi Salant | and | Jonathan | Berant. | 2018. | Contextu- |     |
| ----------- | ----- | --- | ---- | -------- | ----- | ------ | ------------ | --- | -------- | ------- | ----- | --------- | --- |
| Christopher | Clark | and | Matt | Gardner. | 2017. | Simple |              |     |          |         |       |           |     |
alizedwordrepresentationsforreadingcomprehen-
and effective multi-paragraph reading comprehen- sion. InProceedingsofthe16thAnnualConference
sion. In Proceedings of the 55th Annual Meeting of the North American Chapter of the Association
oftheAssociationofComputationalLinguistics.
forComputationalLinguistics.
| Matthew   | Dunn,  | Levent   | Sagun,  | Mike      | Higgins,  | Ugur       |                              |                |     |           |                 |           |     |
| --------- | ------ | -------- | ------- | --------- | --------- | ---------- | ---------------------------- | -------------- | --- | --------- | --------------- | --------- | --- |
|           |        |          |         |           |           |            | Minjoon                      | Seo, Aniruddha |     | Kembhavi, | Ali             | Farhadi,  | and |
| Guney,    | Volkan | Cirik,   | and     | Kyunghyun |           | Cho. 2017. |                              |                |     |           |                 |           |     |
|           |        |          |         |           |           |            | Hannaneh                     | Hajishirzi.    |     | 2017.     | Bidirectional   | attention |     |
| SearchQA: |        | A new    | Q&A     | dataset   | augmented | with       |                              |                |     |           |                 |           |     |
|           |        |          |         |           |           |            | flowformachinecomprehension. |                |     |           | InProceedingsof |           |     |
| context   | from   | a search | engine. |           | arXiv     | preprint   |                              |                |     |           |                 |           |     |
theInternationalConferenceonLearningRepresen-
| arXiv:1704.05179. |     |     |     |     |     |     | tations. |     |     |     |     |     |     |
| ----------------- | --- | --- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- |
MandarJoshi,EunsolChoi,DanielS.Weld,andLuke Alon Talmor and Jonathan Berant. 2018. The web as
| Zettlemoyer. |     | 2017. | TriviaQA: |     | A large | scale dis- |     |     |     |     |     |     |     |
| ------------ | --- | ----- | --------- | --- | ------- | ---------- | --- | --- | --- | --- | --- | --- | --- |
aknowledge-baseforansweringcomplexquestions.
tantlysupervisedchallengedatasetforreadingcom-
|             |     |                 |     |                   |          |        | In Proceedings |          | of the | 16th    | Annual             | Conference | of  |
| ----------- | --- | --------------- | --- | ----------------- | -------- | ------ | -------------- | -------- | ------ | ------- | ------------------ | ---------- | --- |
| prehension. |     | In Proceedings  |     | of                | the 55th | Annual |                |          |        |         |                    |            |     |
|             |     |                 |     |                   |          |        | the North      | American |        | Chapter | of the Association |            | for |
| Meeting     | of  | the Association |     | for Computational |          | Lin-   |                |          |        |         |                    |            |     |
ComputationalLinguistics.
guistics.
|     |     |     |     |     |     |     | Wenhui Wang, |     | Nan Yang, | Furu | Wei, Baobao |     | Chang, |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --- | --------- | ---- | ----------- | --- | ------ |
XiaodongLiu,YelongShen,KevinDuh,andJianfeng and Ming Zhou. 2017. Gated self-matching net-
| Gao.                       | 2018. | Stochastic | answer |                    | networks | for ma- |          |                |               |     |          |          |       |
| -------------------------- | ----- | ---------- | ------ | ------------------ | -------- | ------- | -------- | -------------- | ------------- | --- | -------- | -------- | ----- |
|                            |       |            |        |                    |          |         | works    | for reading    | comprehension |     | and      | question | an-   |
| chinereadingcomprehension. |       |            |        | InProceedingsofthe |          |         |          |                |               |     |          |          |       |
|                            |       |            |        |                    |          |         | swering. | In Proceedings |               | of  | the 55th | Annual   | Meet- |
56thAnnualMeetingoftheAssociationforCompu-
ingoftheAssociationforComputationalLinguistics
tationalLinguistics.
(Volume1:LongPapers),volume1,pages189–198.
ChristopherD.Manning,MihaiSurdeanu,JohnBauer,
|     |     |     |     |     |     |     | Johannes | Welbl, | Pontus | Stenetorp, |     | and Sebastian |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | ------ | ------ | ---------- | --- | ------------- | --- |
Jenny Finkel, Steven J. Bethard, and David Mc- Riedel. 2018. Constructing datasets for multi-hop
| Closky. | 2014. | The | Stanford | CoreNLP |     | natural lan- |     |     |     |     |     | Transac- |     |
| ------- | ----- | --- | -------- | ------- | --- | ------------ | --- | --- | --- | --- | --- | -------- | --- |
readingcomprehensionacrossdocuments.
| guageprocessingtoolkit. |             |     | InAssociationforCompu- |        |                 |     |          |                 |     |                  |     |     |          |
| ----------------------- | ----------- | --- | ---------------------- | ------ | --------------- | --- | -------- | --------------- | --- | ---------------- | --- | --- | -------- |
|                         |             |     |                        |        |                 |     | tions of | the Association |     | of Computational |     |     | Linguis- |
| tational                | Linguistics |     | (ACL)                  | System | Demonstrations, |     |          |                 |     |                  |     |     |          |
tics.
pages55–60.
|     |     |     |     |     |     |     | Caiming | Xiong, | Victor | Zhong, | and Richard |     | Socher. |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------ | ------ | ------ | ----------- | --- | ------- |
AlexanderHMiller,WillFeng,AdamFisch,JiasenLu,
|     |     |     |     |     |     |     | 2018. | DCN+: | Mixed | objective | and | deep | residual |
| --- | --- | --- | --- | --- | --- | --- | ----- | ----- | ----- | --------- | --- | ---- | -------- |
Dhruv Batra, Antoine Bordes, Devi Parikh, and Ja- coattentionforquestionanswering. InProceedings
son Weston. 2017. ParlAI: A dialog research soft- oftheInternationalConferenceonLearningRepre-
| wareplatform. |     | arXivpreprintarXiv:1705.06476. |     |     |     |     |     |     |     |     |     |     |     |
| ------------- | --- | ------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
sentations.
| Tri Nguyen, | Mir     | Rosenberg, |           | Xia Song, | Jianfeng    | Gao,     |                            |           |     |         |                  |     |       |
| ----------- | ------- | ---------- | --------- | --------- | ----------- | -------- | -------------------------- | --------- | --- | ------- | ---------------- | --- | ----- |
|             |         |            |           |           |             |          | Zhilin Yang,               | Saizheng  |     | Zhang,  | Jack Urbanek,    |     | Will  |
| Saurabh     | Tiwary, | Rangan     | Majumder, |           | and         | Li Deng. |                            |           |     |         |                  |     |       |
|             |         |            |           |           |             |          | Feng,                      | Alexander | H   | Miller, | Arthur Szlam,    |     | Douwe |
| 2016.       | MS      | MARCO:     | A human   |           | generated   | machine  |                            |           |     |         |                  |     |       |
|             |         |            |           |           |             |          | Kiela,andJasonWeston.2018. |           |     |         | Masteringthedun- |     |       |
|             |         |            |           |           | Proceedings | of       |                            |           |     |         |                  |     |       |
reading comprehension dataset. In geon: Grounded language learning by mechanical
the 30th AnnualConference on Neural Information turker descent. In Proceedings of the International
ProcessingSystems(NIPS).
ConferenceonLearningRepresentations.
| Jekaterina                  | Novikova, |              | Ondˇrej | Dusˇek, | Amanda       | Cercas |     |     |     |     |     |     |     |
| --------------------------- | --------- | ------------ | ------- | ------- | ------------ | ------ | --- | --- | --- | --- | --- | --- | --- |
| Curry,andVerenaRieser.2017. |           |              |         |         | Whyweneednew |        |     |     |     |     |     |     |     |
| evaluation                  | metrics   | for          | NLG.    | In      | Proceedings  | of the |     |     |     |     |     |     |     |
| Conference                  |           | on Empirical |         | Methods | in Natural   | Lan-   |     |     |     |     |     |     |     |
guageProcessing.
| BoyuanPan,         | HaoLi,                         | ZhouZhao, |                | BinCao,           |                   | DengCai, |     |     |     |     |     |     |     |
| ------------------ | ------------------------------ | --------- | -------------- | ----------------- | ----------------- | -------- | --- | --- | --- | --- | --- | --- | --- |
| andXiaofeiHe.2017. |                                |           | Memen:         | Multi-layerembed- |                   |          |     |     |     |     |     |     |     |
| ding               | with memory                    |           | networks       | for               | machine           | compre-  |     |     |     |     |     |     |     |
| hension.           | arXivpreprintarXiv:1707.09098. |           |                |                   |                   |          |     |     |     |     |     |     |     |
| Pranav Rajpurkar,  |                                | Robin     | Jia,           | and Percy         | Liang.            | 2018.    |     |     |     |     |     |     |     |
| Know               | what                           | you don’t | know:          | Unanswerable      |                   | ques-    |     |     |     |     |     |     |     |
| tions              | for SQuAD.                     |           | In Proceedings |                   | of the            | 56th An- |     |     |     |     |     |     |     |
| nual               | Meeting                        | of the    | Association    |                   | for Computational |          |     |     |     |     |     |     |     |
Linguistics.

| A DataCollectionDetails |     |     |     |     |     |     |     |     |     |     | Supporting Paragraphs |     |     |
| ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | --- |
A.1 DataPreprocessing
WedownloadedthedumpofEnglishWikipediaof
October1,2017,andextractedtextandhyperlinks
| with WikiExtractor.8 |     |         | We use | Stanford      |      | CoreNLP  |     |     |     |     |     |     |     |
| -------------------- | --- | ------- | ------ | ------------- | ---- | -------- | --- | --- | --- | --- | --- | --- | --- |
| 3.8.0 (Manning       |     | et al., | 2014)  | for           | word | and sen- |     |     |     |     |     |     |     |
| tence tokenization.  |     | We      | use    | the resulting |      | sentence |     |     |     |     |     |     |     |
Friendly Hints
| boundaries | for | collection | of  | supporting |     | facts, and |     |     |     |     |     |     |     |
| ---------- | --- | ---------- | --- | ---------- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
usetokenboundariestocheckwhetherTurkersare
Worker Input
| providing | answers | that | cover | spans | of  | entire to- |     |     |     |     |     |     |     |
| --------- | ------- | ---- | ----- | ----- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
kenstoavoidnonsensicalpartial-wordanswers.
A.2 FurtherDataCollectionDetails
|         |             |     |           |     |        |     | Figure4: | ScreenshotofourworkerinterfaceonAma- |     |     |     |     |     |
| ------- | ----------- | --- | --------- | --- | ------ | --- | -------- | ------------------------------------ | --- | --- | --- | --- | --- |
| Details | on Curating |     | Wikipedia |     | Pages. | To  |          |                                      |     |     |     |     |     |
zonMechanicalTurk.
| make sure                                    | the sampled |     | candidate |             | paragraph | pairs  |     |      |     |     |     |     |     |
| -------------------------------------------- | ----------- | --- | --------- | ----------- | --------- | ------ | --- | ---- | --- | --- | --- | --- | --- |
| areintuitiveforcrowdworkerstoaskhigh-quality |             |     |           |             |           |        |     | ·104 |     |     |     |     |     |
| multi-hop                                    | questions   |     | about,    | we manually |           | curate |     |      |     |     |     |     |     |
4
| 591 categories |     | from the | lists | of popular |     | pages by |     |     |     |     |     |     |     |
| -------------- | --- | -------- | ----- | ---------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
WikiProject.9
|                                           | Foreachcategory,wesample(a,b) |     |     |     |     |     | selpmaxEforebmuN |     |     |     |     |     |     |
| ----------------------------------------- | ----------------------------- | --- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- | --- |
| pairsfromthegraphGwherebisintheconsidered |                               |     |     |     |     |     |                  | 3   |     |     |     |     |     |
category,andmanuallycheckwhetheramulti-hop
| questioncanbeaskedgiventhepair(a,b). |     |     |     |     |     | Those |     |     |     |     |     |     |     |
| ------------------------------------ | --- | --- | --- | --- | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
2
| categories | with | a high | probability |     | of  | permitting |     |     |     |     |     |     |     |
| ---------- | ---- | ------ | ----------- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- | --- |
multi-hopquestionsareselected.
1
| Bonus | Structures. |     | To incentivize |     | crowd | work- |     |     |     |     |     |     |     |
| ----- | ----------- | --- | -------------- | --- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- |
erstoproducehigher-qualitydatamoreefficiently,
|           |      |        |         |     |        |       |     | 10  | 30 50 | 70  | 90 110 | 130 |     |
| --------- | ---- | ------ | ------- | --- | ------ | ----- | --- | --- | ----- | --- | ------ | --- | --- |
| we follow | Yang | et al. | (2018), | and | employ | bonus |     |     |       |     |        |     |     |
structures. Wemixtwosettingsinourdatacollec- QuestionLength(tokens)
| tionprocess. | Inthefirstsetting,werewardthetop |     |     |     |     |     |     |     |     |     |     |     |     |
| ------------ | -------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
(in terms of numbers of examples) workers every Figure5: Distributionoflengthsofquestionsin HOT-
| 200 examples. |     | In the | second | setting, | the | workers | POTQA. |     |     |     |     |     |     |
| ------------- | --- | ------ | ------ | -------- | --- | ------- | ------ | --- | --- | --- | --- | --- | --- |
getbonusesbasedontheirproductivity(measured
| asthenumberofexamplesperhour). |     |     |     |     |     |     | B FurtherDataAnalysis |     |     |     |     |     |     |
| ------------------------------ | --- | --- | --- | --- | --- | --- | --------------------- | --- | --- | --- | --- | --- | --- |
A.3 CrowdWorkerInterface
|     |     |     |     |     |     |     | To further | look | into the | diversity | of  | the data | in  |
| --- | --- | --- | --- | --- | --- | --- | ---------- | ---- | -------- | --------- | --- | -------- | --- |
Our crowd worker interface is based on ParlAI HOTPOTQA, we further visualized the distribu-
(Miller et al., 2017), an open-source project that tion of question lengths in the dataset in Figure
facilitates the development of dialog systems and 5. Besides being diverse in terms of types as is
data collection with a dialog interface. We adapt show in the main text, questions also vary greatly
inlength,indicatingdifferentlevelsofcomplexity
| ParlAI          | for collecting |                            | question | answer |      | pairs by  |                    |     |     |     |     |     |     |
| --------------- | -------------- | -------------------------- | -------- | ------ | ---- | --------- | ------------------ | --- | --- | --- | --- | --- | --- |
| converting      | the collection |                            | workflow |        | into | a system- | anddetailscovered. |     |     |     |     |     |     |
| orienteddialog. |                | Thisallowsustohavemorecon- |          |        |      |           |                    |     |     |     |     |     |     |
C FullWikiSettingDetails
trolovertheturkersinput,aswellasprovideturk-
| ers with | in-the-loop | feedbacks |     | or  | helpful | hints to |     |     |     |     |     |     |     |
| -------- | ----------- | --------- | --- | --- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- |
C.1 TheInvertedIndexFilteringStrategy
| help Turkers | finish | the | task, | and | therefore | speed |        |      |               |     |       |              |     |
| ------------ | ------ | --- | ----- | --- | --------- | ----- | ------ | ---- | ------------- | --- | ----- | ------------ | --- |
|              |        |     |       |     |           |       | In the | full | wiki setting, | we  | adopt | an efficient |     |
upthecollectionprocess.
PleaseseeFigure4foranexampleoftheworker inverted-index-based filtering strategy for prelim-
interfaceduringdatacollection. inary candidate paragraph retrieval. We provide
|     |     |     |     |     |     |     | details | in Algorithm | 2,  | where | we set | the control |     |
| --- | --- | --- | --- | --- | --- | --- | ------- | ------------ | --- | ----- | ------ | ----------- | --- |
8https://github.com/attardi/
|     |     |     |     |     |     |     | thresholdN |     | = 5000inourexperiments. |     |     | Forsome |     |
| --- | --- | --- | --- | --- | --- | --- | ---------- | --- | ----------------------- | --- | --- | ------- | --- |
wikiextractor
9https://wiki.sh/y8qu of the question q, its corresponding gold para-

Algorithm2InvertedIndexFilteringStrategy
| Input: | question text | q, control | threshold |     | N, ngram-to- |
| ------ | ------------- | ---------- | --------- | --- | ------------ |
WikidocinvertedindexD
Inintialize:
| Extractunigram+bigramsetr |     |     | q fromq |     |     |
| ------------------------- | --- | --- | ------- | --- | --- |
N cand =+∞
C gram =0
| whileN | cands >N do                   |     |     |     |     |
| ------ | ----------------------------- | --- | --- | --- | --- |
| C gram | =C gram                       | +1  |     |     |     |
| SetS   | overlap tobeanemptydictionary |     |     |     |     |
| forw∈r | q do                          |     |     |     |     |
ford∈D[w]do
|     | ifdnotinS | overlap | then |     |     |
| --- | --------- | ------- | ---- | --- | --- |
S overlap [d]=1
else
|     | S overlap [d]=S |     | overlap | [d]+1 |     |
| --- | --------------- | --- | ------- | ----- | --- |
endif
endfor
endfor
| S cand  | =∅             |      |      |     |     |
| ------- | -------------- | ---- | ---- | --- | --- |
| fordinS | overlap do     |      |      |     |     |
| ifS     | overlap [d]≥C  | gram | then |     |     |
|         | S cand =S cand | ∪{d} |      |     |     |
endif
endfor
| N cands | =|S cand | |     |     |     |     |
| ------- | ---------- | --- | --- | --- | --- |
endwhile
| return | S cand |     |     |     |     |
| ------ | ------ | --- | --- | --- | --- |
graphsmaynotbeincludedintheoutputcandidate
| pool S | , we set | such missing |     | gold | paragraph’s |
| ------ | -------- | ------------ | --- | ---- | ----------- |
cand
| rankas|S | |+1duringtheevaluation,soMAP |     |     |     |     |
| -------- | ---------------------------- | --- | --- | --- | --- |
cand
| and Mean | Rank reported |     | in this | paper | are upper |
| -------- | ------------- | --- | ------- | ----- | --------- |
boundsoftheirtruevalues.
C.2 Comparetrain-mediumSplittoHard
Ones
| Table 9         | shows the            | comparison |      | between | train-       |
| --------------- | -------------------- | ---------- | ---- | ------- | ------------ |
| medium          | split and hard       | examples   |      | like    | dev and test |
| under retrieval | metrics              | in         | full | wiki    | setting. As  |
| we can          | see, the performance |            | gap  | between | train-       |
| medium          | split and its        | dev/test   | is   | close,  | which im-    |
pliesthattrain-mediumsplithasasimilarlevelof
difficultyashardexamplesunderthefullwikiset-
tinginwhicharetrievalmodelisnecessaryasthe
firstprocessingstep.
| Set          | MAP   | MeanRank |        | CorAnsRank |       |
| ------------ | ----- | -------- | ------ | ---------- | ----- |
| train-medium | 41.89 |          | 288.19 |            | 82.76 |
| dev          | 42.79 |          | 304.30 |            | 97.93 |
| test         | 45.92 |          | 286.20 |            | 74.85 |
Table9:Retrievalperformancecomparisononfullwiki
| setting for | train-medium,  | dev      | and    | test with | 1,000 ran-  |
| ----------- | -------------- | -------- | ------ | --------- | ----------- |
| dom samples | each. MAP      | and      | are    | in %.     | Mean Rank   |
| averages    | over retrieval | ranks    | of two | gold      | paragraphs. |
| CorAns      | Rank refers to | the rank | of     | the gold  | paragraph   |
containingtheanswer.
