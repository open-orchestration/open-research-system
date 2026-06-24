Speech and Language Processing. Daniel Jurafsky & James H. Martin. Copyright © 2026. All
| rights reserved. | Draft of | January | 6, 2026. |     |     |     |     |     |     |     |
| ---------------- | -------- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- |
CHAPTER
| 11  | Information                                            |           |     |        | Retrieval          |     |     | and        |     |              |
| --- | ------------------------------------------------------ | --------- | --- | ------ | ------------------ | --- | --- | ---------- | --- | ------------ |
|     | Retrieval-Augmented                                    |           |     |        |                    |     |     | Generation |     |              |
|     | On two                                                 | occasions |     | I have | been asked,—“Pray, |     | Mr. | Babbage,   | if  | you put into |
|     | themachinewrongfigures,willtherightanswerscomeout?”... |           |     |        |                    |     |     |            |     | Iamnotable   |
rightlytoapprehendthekindofconfusionofideasthatcouldprovokesucha
|     | question.         |          |            |            |                |                  |              |          | Babbage(1864) |              |
| --- | ----------------- | -------- | ---------- | ---------- | -------------- | ---------------- | ------------ | -------- | ------------- | ------------ |
|     | People            | need to  | know       | things.    | So pretty      | much             | as soon      | as there | were          | computers    |
|     | we were asking    | them     | questions. |            | By 1961        | there            | was a system |          | to answer     | questions    |
|     | about American    | baseball |            | statistics | like           | “How many        | games        | did      | the           | Yankees play |
|     | in July?”         | (Green   | et al.,    | 1961).     | Even fictional |                  | computers    | in       | the 1970s     | like Deep    |
|     | Thought, invented |          | by Douglas |            | Adams in       | The Hitchhiker’s |              | Guide    | to            | the Galaxy,  |
Everything”.1
|     | answered “the                           | Ultimate |                                                  | Question | Of Life, | The | Universe,                     | and |     | And |
| --- | --------------------------------------- | -------- | ------------------------------------------------ | -------- | -------- | --- | ----------------------------- | --- | --- | --- |
|     | becausesomuchknowledgeisencodedintext,  |          |                                                  |          |          |     | systemswereansweringquestions |     |     |     |
|     | athuman-levelperformanceevenbeforeLLMs: |          |                                                  |          |          |     | IBM’sWatsonsystemwontheTV     |     |     |     |
|     | game-showJeopardy!                      |          | in2011,surpassinghumansatansweringquestionslike: |          |          |     |                               |     |     |     |
WILLIAM WILKINSON’S “AN ACCOUNT OF THE
PRINCIPALITIES OF WALLACHIA AND MOLDOVIA”
|     |     | INSPIRED THIS AUTHOR’S MOST FAMOUS NOVEL |     |     |     |     |     |     | 2   |     |
| --- | --- | ---------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Itfollowsnaturally,then,thatanimportantfunctionoflargelanguagemodelsis
|     | tofillhumaninformationneeds.     |      |       |           | Andsincealotofinformationisonline,finding |         |     |                 |     |            |
| --- | -------------------------------- | ---- | ----- | --------- | ----------------------------------------- | ------- | --- | --------------- | --- | ---------- |
|     | the information                  | that | fills | our needs | is closely                                | related | to  | web information |     | retrieval, |
|     | thetaskperformedbysearchengines. |      |       |           | Indeed,thedistinctionisbecomingevermore   |         |     |                 |     |            |
fuzzy,asmodernsearchenginesareintegratedwithlargelanguagemodels.
factoid Consider some simple information needs, for example factoid questions that
questions
canbemetwithfactsexpressedinshorttextslikethefollowing:
(11.1) WhereistheLouvreMuseumlocated?
(11.2) Wheredoestheenergyinanuclearexplosioncomefrom?
(11.3) Howtogetascriptlinlatex?
|     | TogetanLLMtoanswerthesequestions,wecanjustpromptit! |     |     |     |     |     |     |     | Forexamplea |     |
| --- | --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ----------- | --- |
pretrainedLLMthathasbeeninstruction-tunedonansweringquestions(instruction-
tuningisinChapter10)coulddirectlyanswerthefollowingquestion
|     | Where | is the | Louvre |     | Museum | located? |     |     |     |     |
| --- | ----- | ------ | ------ | --- | ------ | -------- | --- | --- | --- | --- |
byperformingconditionalgenerationgiventhisprefix,andtaketheresponseasthe
answer. Thisworksbecauselargelanguagemodelshaveprocessedalotoffactsin
|     | their pretraining             | data, | including |     | the location                              | of the | Louvre, | and | have | encoded this |
| --- | ----------------------------- | ----- | --------- | --- | ----------------------------------------- | ------ | ------- | --- | ---- | ------------ |
|     | informationintheirparameters. |       |           |     | Factualknowledgeofthistypeseemstobestored |        |         |     |      |              |
intheconnectionsintheverylargefeedforwardlayersoftransformermodels(Geva
etal.,2021;Mengetal.,2022).
1 Theanswerwas42,butunfortunatelythequestionwasneverrevealed.
2 Theanswer,ofcourse,is‘WhoisBramStoker’,andthenovelwasDracula.

2 CHAPTER11 • RETRIEVAL-BASEDMODELS
SimplypromptinganLLMisusefulformanygenerationtasks,includingthose
involvingfacts. Butthefactthatknowledgeisstoredinthefeedforwardweightsof
the LLM leads to a number of problems with prompting as a method for correctly
generatingfactualtextsoranswers.
The first and main problem is that LLMs are often incorrect when generating
hallucinate answers or other texts about facts! Large language models hallucinate. A hallu-
cination is a response that is not faithful to the facts of the world. That is, when
askedquestions,largelanguagemodelssometimesmakeupanswersthatsoundrea-
sonable. Forexample,Dahletal.(2024)foundthatwhenaskedquestionsaboutthe
legaldomain(likeaboutparticularlegalcases),largelanguagemodelshallucinated
from 69% to 88% of the time! LLMs sometimes give incorrect factual responses
even when the correct facts are stored in the parameters; this seems to be caused
bythefeedforwardlayersfailingtorecalltheknowledgestoredintheirparameters
(Jiangetal.,2024).
And it’s not always possible to tell when language models are hallucinating,
calibrated partlybecauseLLMsaren’twell-calibrated.Inacalibratedsystem,theconfidence
ofasysteminthecorrectnessofitsanswerishighlycorrelatedwiththeprobability
ofananswerbeingcorrect.Soifacalibratedsystemiswrong,atleastitmighthedge
itsanswerortellustogocheckanothersource. Butsincelanguagemodelsarenot
well-calibrated,theyoftengiveaverywronganswerwithcompletecertainty(Zhou
etal.,2024).
Asecondproblemwithmeetinguserinformationneedswithsimpleprompting
methodsisthatpromptingalargelanguagemodeltoanswerfromitspretrainedpa-
rametersdoesn’tallowustoaskquestionsaboutproprietarydata. Wewouldliketo
uselanguagemodelstohelpwithuserinformationneedsaboutproprietarydatalike
personalemail. Orforthehealthcareapplicationwemightwanttoapplyalanguage
modeltomedicalrecords. Oracompanymayhaveinternaldocumentsthatcontain
answers for customer service or internal use. Or legal firms need to ask questions
about legal discovery from proprietary documents. None of this data (hopefully)
wasinthelargeweb-basedcorporathatlargelanguagemodelsarepretrainedon.
Afinalissuewithusinglargelanguagemodelstoanswerknowledgequestionsis
thattheyarestatic;theywerepretrainedonce,ataparticulartime. Thismeansthat
LLMs cannot talk about about rapidly changing information (like something that
happened last week) since they won’t have up-to-date information from after their
releasedata.
One solution to all these problems with simple prompting for generating fac-
tual text is to give a language model external sources of knowledge, for example
proprietary texts like medical or legal records, personal emails, or corporate docu-
ments, and to use those documents in answering questions. This method is called
RAG retrieval-augmentedgenerationorRAG,andthatisthemethodwewillfocuson
information in this chapter. In RAG we use information retrieval (IR) techniques to retrieve
retrieval
documentsthatarelikelytohaveinformationthatmighthelpanswerthequestion.
Thenweusealargelanguagemodeltogenerateananswergiventhesedocuments.
Basingouranswersonretrieveddocumentscansolvesomeoftheproblemswith
usingsimplepromptingtoanswerquestions. First,ithelpsensurethattheansweris
groundedinfactsfromsomecurateddataset. Andthesystemcangivetheuserthe
answeraccompaniedbythecontextofthepassageordocumentitcamefrom. This
information can help users have confidence in the accuracy of the answer (or help
them spot when it is wrong!). And these retrieval techniques can be used on any
proprietarydatawewant,suchaslegalormedicaldataforthoseapplications.

|     |                                              |     |     |     |     | 11.1 | • INFORMATIONRETRIEVAL |                          |     |     | 3   |
| --- | -------------------------------------------- | --- | --- | --- | --- | ---- | ---------------------- | ------------------------ | --- | --- | --- |
|     | We’llbeginbyintroducinginformationretrieval, |     |     |     |     |      |                        | thetaskofchoosingthemost |     |     |     |
relevantdocumentfromadocumentsetgivenauser’squeryexpressingtheirinfor-
|     | mation    | need.    | We’ll see      | the classic |            | method   | based on   | cosines      | of sparse | tf-idf    | vec- |
| --- | --------- | -------- | -------------- | ----------- | ---------- | -------- | ---------- | ------------ | --------- | --------- | ---- |
|     | tors,     | modern   | neural ‘dense’ |             | retrievers | based    | on instead | representing |           | queries   | and  |
|     | documents | neurally | with           | BERT        | or other   | language | models.    |              | We then   | introduce | the  |
retrieval-augmentedgenerationparadigm.
|     | Finally, | we’ll | discuss | various | datasets | with | questions | and | answers | that | can be |
| --- | -------- | ----- | ------- | ------- | -------- | ---- | --------- | --- | ------- | ---- | ------ |
usedforfinetuningLLMsininstructiontuningandforuseasbenchmarksforeval-
uation.
| 11.1 | Information |     | Retrieval |     |     |     |     |     |     |     |     |
| ---- | ----------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
information
InformationretrievalorIRisthenameofthefieldencompassingtheretrievalof
retrieval
IR all manner of media based on user information needs. The resulting IR system is
|     | oftencalledasearchengine. |     |     |     | Ourgoalinthissectionistogiveasufficientoverview |     |     |     |     |     |     |
| --- | ------------------------- | --- | --- | --- | ----------------------------------------------- | --- | --- | --- | --- | --- | --- |
ofIRtoseeitsapplicationtolargelanguagemodelsmeetinguserinformationneeds.
ReaderswithmoreinterestspecificallyininformationretrievalshouldseetheHis-
toricalNotessectionattheendofthechapter.
adhocretrieval The IR task we consider is called ad hoc retrieval, in which a user poses a
|     | query | to a retrieval | system, | which | then | returns | an ordered | set | of documents |     | from |
| --- | ----- | -------------- | ------- | ----- | ---- | ------- | ---------- | --- | ------------ | --- | ---- |
document some collection. A document refers to whatever unit of text the system indexes
|     | and  | retrieves    | (web pages,  | scientific |        | papers, | news articles,   | or  | even  | shorter | passages   |
| --- | ---- | ------------ | ------------ | ---------- | ------ | ------- | ---------------- | --- | ----- | ------- | ---------- |
|     | like | paragraphs). | A collection |            | refers | to a    | set of documents |     | being | used    | to satisfy |
collection
|     | user       | requests. | A collection                                              | can | mean | the entire | web, | in which | case | we  | are doing |
| --- | ---------- | --------- | --------------------------------------------------------- | --- | ---- | ---------- | ---- | -------- | ---- | --- | --------- |
|     | websearch. |           | Butacollectioncanalsobeasmallercorporaterepo,orevenasetof |     |      |            |      |          |      |     |           |
websearch
term documentsusedbyoneperson. termreferstoawordinacollection,butitmayalso
query includephrases. Finally,aqueryrepresentsauser’sinformationneedexpressedas
asetofterms.
Document
| Document         |     |             |     | Document |     |     |        |     |     |     |     |
| ---------------- | --- | ----------- | --- | -------- | --- | --- | ------ | --- | --- | --- | --- |
| DocumenDtocument |     | Processing  |     |          |     |     | Search |     |     |     |     |
Index
| DocumeDntocument |          | & Indexing |     |     |     |     |           |     |          |                |     |
| ---------------- | -------- | ---------- | --- | --- | --- | --- | --------- | --- | -------- | -------------- | --- |
| Document         | Document |            |     |     |     |     |           |     |          |                |     |
|                  |          |            |     |     |     |     |           |     | Document | Do c u m e n t |     |
|                  |          |            |     |     |     |     | Maximize: |     |          | D o c u m e nt |     |
Do c u m e n t
| document collection |     |     |     |     |     |     | Document  |     |     | D o c Ru ma | e nnkted  |
| ------------------- | --- | --- | --- | --- | --- | --- | --------- | --- | --- | ----------- | --------- |
Documents
Relevance
Score
|     |     | Query  |     | Query |     |     |     |     |     |     |     |
| --- | --- | ------ | --- | ----- | --- | --- | --- | --- | --- | --- | --- |
query
|     |     | Processing |     | Vector |     |     |     |     |     |     |     |
| --- | --- | ---------- | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
Figure11.1 ThearchitectureofanadhocIRsystem. Documentrankingisbasedoncomputingascorefor
eachcandidatedocumentgiventhequery,expressinghowrelevantitislikelytobetomeettheusersinformation
need.TherearetwoclassesofIRsystems,basedonthetwoclassesofvectorsthatareusedtorepresentqueries
and documents: sparse vectors and dense vectors. These two kinds of retrieval differ in the details of the
indexingandscoringmechanisms.
Thehigh-levelarchitectureofanadhocretrievalengineisshowninFig.11.1.
|     | This                    | figure abstracts |          | over the                                         | two classes |              | of IR systems, | which | are        | based | on the    |
| --- | ----------------------- | ---------------- | -------- | ------------------------------------------------ | ----------- | ------------ | -------------- | ----- | ---------- | ----- | --------- |
|     | two                     | classes of       | vectors  | that are                                         | used        | to represent | queries        | and   | documents: |       | sparse    |
|     | vectorsanddensevectors. |                  |          | Insparseretrieval,werepresentdocumentsandqueries |             |              |                |       |            |       |           |
|     | with                    | count vectors,   | weighted |                                                  | by tf-idf   | or BM25.     | In             | dense | retrieval, | we    | represent |

4 CHAPTER11 • RETRIEVAL-BASEDMODELS
documentsandquerieswithembeddings,computedfromlanguagemodels(either
encoderordecodermodels). We’lldiscusssparseretrievalintherestofthissection,
andturntodenseretrievalinSection11.3.
11.1.1 Representingdocumentsasvectors
vectorspace In the vector space model of information retrieval (Salton, 1971) a document is
model
representedasavectorofcountsofthewordsitcontains.
Wesometimescallthiskindofmodelabag-of-wordsmodel. Fig.11.2shows
bagofwords the intuition: we are representing a text document as if it were a bag of words,
that is, an unordered set of words with their position ignored, keeping only their
frequencyinthedocument. Intheexampleinthefigure,insteadofrepresentingthe
word order in all the phrases like “It manages to be whimsical and romantic”, we
simplynotethattheworditoccurred5timesintheentireexcerpt, thewordslove,
recommend,andmovieonce,andsoon.
adventure 1
and 3
fairy 1
I love this movie! It's sweet,
fairy it genre 1
but with satirical humor. The always loveto
it great 1
dialogue is great and the whimsical it I
adventure scenes are fun... and seen are anyone have 1
It manages to be whimsical frien h d appy dialogue humor 1
recommend I 5
and romantic while laughing adventure
at the conventions of the who sweet of m sa o t v ir ie ical it i s t atirical 6 1
f r a e i c ry o m ta m le e g n e d n i r t e to . I j u w s o t u a ld b out sev i e t ra I l but to y r e o t mantic I seen 2
anyone. I've seen it several again it the humor sweet 1
the seen would the 4
times, and I'm always happy to scenes I themanages times 1
to see it again whenever I the
have a friend who hasn't fun I and times and to 3
seen it yet! whenever about while whimsical 1
have would 1
conventions
with yet 1
… …
Figure11.2 Intuition of the classic vector space model applied to a single document. The position of the
wordsisignored(thebag-of-wordsassumption)andwemakeuseofthefrequencyofeachword.
WecouldthusimaginerepresentingthedocumentinFig.11.2asthevector[13
1111156121413111](ifwelimitedourselvestothese18dimensionsand
ignoredalltheotherwordsinEnglish).
Moregenerally,wecanrepresentasetofdocumentsasaterm-documentma-
term-document trix in which each row represents a word in the vocabulary and each column rep-
matrix
resents a document from some collection of documents. Fig. 11.3 shows a small
selection from a term-document matrix showing the occurrence of four words in
fourplaysbyShakespeare. Eachcellinthismatrixrepresentsthenumberoftimesa
particularword(definedbytherow)occursinaparticulardocument(definedbythe
column). Thusfoolappeared58timesinTwelfthNight.
A document is represented as a count vector, a column in Fig. 11.4. In the
exampleinFig.11.4, we’vechosentomakethedocumentvectorsofdimension4,
just so they fit on the page; in real term-document matrices, the document vectors
would have dimensionality |V|, the vocabulary size. The first dimension for both
thesevectorscorrespondstothenumberoftimesthewordbattleoccurs,andwecan

11.1 • INFORMATIONRETRIEVAL 5
AsYouLikeIt TwelfthNight JuliusCaesar HenryV
battle 1 0 7 13
good 114 80 62 89
fool 36 58 1 4
wit 20 15 2 3
Figure11.3 The term-document matrix for four words in four Shakespeare plays. Each
cellcontainsthenumberoftimesthe(row)wordoccursinthe(column)document.
compareeachdimension,notingforexamplethatthevectorsforAsYouLikeItand
TwelfthNighthavesimilarvalues(1and0,respectively)forthefirstdimension.
AsYouLikeIt TwelfthNight JuliusCaesar HenryV
battle 1 0 7 13
good 114 80 62 89
fool 36 58 1 4
wit 20 15 2 3
Figure11.4 Theterm-documentmatrixforfourwordsinfourShakespeareplays. Thered
boxesshowthateachdocumentisrepresentedasacolumnvectoroflengthfour.
Since 4-dimensional spaces are hard to visualize, Fig. 11.5 shows a visualiza-
tion of the four document vectors in two dimensions; we’ve arbitrarily chosen the
dimensionscorrespondingtothewordsbattleandfool.
Henry V [4,13]
10 Julius Caesar [1,7]
5 As You Like It [36,1]
5 10 15 20 25 30
elttab
40
15
Twelfth Night [58,0]
35 40 45 50 55 60
fool
Figure11.5 AspatialvisualizationofthedocumentvectorsforthefourShakespeareplay
documents,showingjusttwoofthedimensions,correspondingtothewordsbattleandfool.
Thecomedieshavehighvaluesforthefooldimensionandlowvaluesforthebattledimension.
Twodocumentsthataresimilarwilltendtohavesimilarwords,andiftwodoc-
umentshavesimilarwordstheircolumnvectorswilltendtobesimilar. Thevectors
forthecomediesAsYouLikeIt[1,114,36,20]andTwelfthNight[0,80,58,15]looka
lotmorelikeeachother(morefoolsandwitthanbattles)thantheylooklikeJulius
Caesar[7,62,1,2]orHenryV[13,89,4,3].
11.1.2 Termweighting: tf-idfandBM25
Infact, inIR,wedon’t userawwordcountslike[11143620] forAsYouLikeIt,
or [1 3 1 1 1 1 1 5 6 1 2 1 4 1 3 1 1 1] for the document in Fig. 11.2. Instead we
termweight computeatermweightforeachdocumentword. Twotermweightingschemesare
BM25 common: tf-idfandavariantoftf-idfcalledBM25.
Tf-idf(the‘-’hereisahyphen,notaminussign)istheproductoftwoterms,the
termfrequencytfandtheinversedocumentfrequencyidf.

6 CHAPTER11 • RETRIEVAL-BASEDMODELS
| The | term frequency |     | term | tells us | how frequent | the | word | is; words | that occur |
| --- | -------------- | --- | ---- | -------- | ------------ | --- | ---- | --------- | ---------- |
moreofteninadocumentarelikelytobeinformativeaboutthedocument’scontents.
| We usually | use | the log | of  | the word | frequency, | rather | than | the raw | count. The |
| ---------- | --- | ------- | --- | -------- | ---------- | ------ | ---- | ------- | ---------- |
10
intuitionisthatawordappearing100timesinadocumentdoesn’tmakethatword
| 100timesmorelikelytoberelevanttothemeaningofthedocument.      |     |     |     |     |                    |     |     | Wealsoneed        |        |
| ------------------------------------------------------------- | --- | --- | --- | --- | ------------------ | --- | --- | ----------------- | ------ |
| todosomethingspecialwithcountsof0,sincewecan’ttakethelogof0.3 |     |     |     |     |                    |     |     |                   | Soifwe |
| definecount(t,d)astherawcountoftermt                          |     |     |     |     | indocumentd,thentf |     |     | t,d ,thetfoftermt |        |
| indocumentd                                                   |     | is  |     |     |                    |     |     |                   |        |
(cid:40)
|     |     |     | 1+log | count(t,d) |     | if count(t,d)>0 |     |     |     |
| --- | --- | --- | ----- | ---------- | --- | --------------- | --- | --- | --- |
10
|     |     | tf t,d = |     |     |     |           |     |     | (11.4) |
| --- | --- | -------- | --- | --- | --- | --------- | --- | --- | ------ |
|     |     |          | 0   |     |     | otherwise |     |     |        |
Ifweuselogweighting,termswhichoccur0timesinadocumentwouldhavetf=0,
| 1 times | in a document |     | tf=1+log | (1)=1+0=1, |     | 10  | times | in a document | tf= |
| ------- | ------------- | --- | -------- | ---------- | --- | --- | ----- | ------------- | --- |
10
| 1+log | (10)=2,100timestf=1+log |           |     |       | (100)=3,1000timestf=4,andsoon. |                 |     |              |        |
| ----- | ----------------------- | --------- | --- | ----- | ------------------------------ | --------------- | --- | ------------ | ------ |
| 10    |                         |           |     |       | 10                             |                 |     |              |        |
| The   | document                | frequency |     | df of | a term                         | t is the number |     | of documents | it oc- |
t
| curs in.        | Terms  | that        | occur in | only a few         | documents | are       | useful     | for discriminating |             |
| --------------- | ------ | ----------- | -------- | ------------------ | --------- | --------- | ---------- | ------------------ | ----------- |
| those documents |        | from        | the rest | of the collection; |           | terms     | that occur | across             | the entire  |
| collection      | aren’t | as helpful. |          | The inverse        | document  | frequency |            | or idf             | term weight |
(SparckJones,1972)isdefinedas:
N
|     |     |     |     | idf t =log |     |     |     |     | (11.5) |
| --- | --- | --- | --- | ---------- | --- | --- | --- | --- | ------ |
10df
t
| where N                 | is the | total | number | of documents                                 | in  | the collection, |     | and df t is | the number |
| ----------------------- | ------ | ----- | ------ | -------------------------------------------- | --- | --------------- | --- | ----------- | ---------- |
| ofdocumentsinwhichtermt |        |       |        | occurs. Thefewerdocumentsinwhichatermoccurs, |     |                 |     |             |            |
thehigherthisweight;thelowestweightof0isassignedtotermsthatoccurinevery
document.
| Here | are some | idf | values | for some | words | in the corpus | of  | Shakespeare | plays, |
| ---- | -------- | --- | ------ | -------- | ----- | ------------- | --- | ----------- | ------ |
rangingfromextremelyinformativewordsthatoccurinonlyoneplaylikeRomeo,
tothosethatoccurinafewlikesaladorFalstaff,tothosethatareverycommonlike
foolorsocommonastobecompletelynon-discriminativesincetheyoccurinall37
playslikegoodorsweet.4
|                        |     |     |     | Word        | df  | idf                             |     |     |     |
| ---------------------- | --- | --- | --- | ----------- | --- | ------------------------------- | --- | --- | --- |
|                        |     |     |     | Romeo       | 1   | 1.57                            |     |     |     |
|                        |     |     |     | salad       | 2   | 1.27                            |     |     |     |
|                        |     |     |     | Falstaff    | 4   | 0.967                           |     |     |     |
|                        |     |     |     | forest      | 12  | 0.489                           |     |     |     |
|                        |     |     |     | battle      | 21  | 0.246                           |     |     |     |
|                        |     |     |     | wit         | 34  | 0.037                           |     |     |     |
|                        |     |     |     | fool        | 36  | 0.012                           |     |     |     |
|                        |     |     |     | good        | 37  | 0                               |     |     |     |
|                        |     |     |     | sweet       | 37  | 0                               |     |     |     |
| Thetf-idfvalueforwordt |     |     |     | indocumentd |     | isthentheproductoftermfrequency |     |     |     |
tf andIDF:
t,d
|          |          |      |             | tf-idf(t,d)=tf |       | ·idf    |         |                   |         |
| -------- | -------- | ---- | ----------- | -------------- | ----- | ------- | ------- | ----------------- | ------- |
|          |          |      |             |                | t,d   | t       |         |                   | (11.6)  |
| 3 We can | also use | this | alternative | formulation,   | which | we have | used in | earlier editions: | tft,d = |
log (count(t,d)+1)
10
| 4 SweetwasoneofShakespeare’sfavoriteadjectives, |     |     |     |     |     | afactprobablyrelatedtotheincreaseduseof |     |     |     |
| ----------------------------------------------- | --- | --- | --- | --- | --- | --------------------------------------- | --- | --- | --- |
sugarinEuropeanrecipesaroundtheturnofthe16thcentury(Jurafsky,2014,p.175).

11.1 • INFORMATIONRETRIEVAL 7
11.1.3 DocumentScoring
Oncewehaverepresentedeachdocumentandqueryasaweightedvector,weneed
toscoreeachdocument.Ourgoalistomeasuretherelevanceofthedocumenttothe
user’sinformationneed, asexpressedintheirquery. Intheclassictf-idfmodelwe
estimatethisrelevanceofadocumentbymeasuringitsgeometricsimilarityinvector
spacetothequery.Thatis,wemakethesimplifyingassumptionthatdocumentsthat
havesimilarwordstothequeryaremorerelevanttotheuser.
WeusethecosinesimilarityfunctionintroducedinChapter5,scoringdocument
d bythecosineofitsvectordwiththequeryvectorq:
q·d
score(q,d)=cos(q,d)= (11.7)
|q||d|
Another way to think of the cosine computation is as the dot product of unit vec-
tors;wecanfirstnormalizeboththequeryanddocumentvectortounitvectors,by
dividingbytheirlengths,andthentakethedotproduct:
q d
score(q,d)=cos(q,d)= · (11.8)
|q| |d|
WecanspelloutEq.11.8,usingthetf-idfvaluesandspellingoutthedotproduct
asasumofproducts:
(cid:88) tf-idf(t,q) tf-idf(t,d)
score(q,d)= (cid:113) · (cid:113) (11.9)
t∈q (cid:80) qi∈q tf-idf2(q i ,q) (cid:80) di∈d tf-idf2(d i ,d)
Now let’s use Eq. 11.9 to walk through an example of a tiny query against a
collectionof4nanodocuments,computingtf-idfvaluesandseeingtherankofthe
documents.We’llassumeallwordsinthefollowingqueryanddocumentsaredown-
casedandpunctuationisremoved:
Query: sweetlove
Doc1: Sweetsweetnurse! Love?
Doc2: Sweetsorrow
Doc3: Howsweetislove?
Doc4: Nurse!
Fig.11.6showsthecomputationofthetf-idfcosinebetweenthequeryandDoc-
ument1,andthequeryandDocument2. Thecosineisthenormalizeddotproduct
of tf-idf values, so for the normalization we must need to compute the document
vector lengths |q|, |d |, and |d | for the query and the first two documents using
1 2
Eq.11.4,Eq.11.5,Eq.11.6,andEq.11.9(computationsforDocuments3and4are
alsoneededbutareleftasanexerciseforthereader). Thedotproductbetweenthe
vectorsisthesumoverdimensionsoftheproduct,foreachdimension,ofthevalues
of the two tf-idf vectors for that dimension. This product is only non-zero where
both the query and document have non-zero values, so for this example, in which
only sweet and love have non-zero values in the query, the dot product will be the
sumoftheproductsofthoseelementsofeachvector.
Document 1 has a higher cosine with the query (0.747) than Document 2 has
with the query (0.0779), and so the tf-idf cosine model would rank Document 1
above Document 2. This ranking is intuitive given the vector space model, since
Document1hasbothtermsincludingtwoinstancesofsweet,whileDocument2is

| 8 CHAPTER11 |     | • RETRIEVAL-BASEDMODELS |     |     |     |     |     |     |     |     |
| ----------- | --- | ----------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Query
| word   | cnt tf df | idf tf-idf  | n’lized=tf-idf/|q| |     |     |     |     |     |     |     |
| ------ | --------- | ----------- | ------------------ | --- | --- | --- | --- | --- | --- | --- |
| sweet  | 1 1 3     | 0.125 0.125 | 0.383              |     |     |     |     |     |     |     |
| nurse  | 0 0 2     | 0.301 0     | 0                  |     |     |     |     |     |     |     |
| love   | 1 1 2     | 0.301 0.301 | 0.924              |     |     |     |     |     |     |     |
| how    | 0 0 1     | 0.602 0     | 0                  |     |     |     |     |     |     |     |
| sorrow | 0 0 1     | 0.602 0     | 0                  |     |     |     |     |     |     |     |
| is     | 0 0 1     | 0.602 0     | 0                  |     |     |     |     |     |     |     |
√
|q|= .1252+.3012=.326
|        |                        | Document1          |       |     |     |                     | Document2          |         |        |     |
| ------ | ---------------------- | ------------------ | ----- | --- | --- | ------------------- | ------------------ | ------- | ------ | --- |
| word   | cnt tf                 | tf-idf n’lized     | ×q    |     | cnt | tf                  | tf-idf             | n’lized | ×q     |     |
| sweet  | 2 1.301                | 0.163 0.357        | 0.137 |     | 1   | 1.000               | 0.125              | 0.203   | 0.0779 |     |
| nurse  | 1 1.000                | 0.301 0.661        | 0     |     | 0   | 0                   | 0                  | 0       | 0      |     |
| love   | 1 1.000                | 0.301 0.661        | 0.610 |     | 0   | 0                   | 0                  | 0       | 0      |     |
| how    | 0 0                    | 0 0                | 0     |     | 0   | 0                   | 0                  | 0       | 0      |     |
| sorrow | 0 0                    | 0 0                | 0     |     | 1   | 1.000               | 0.602              | 0.979   | 0      |     |
| is     | 0 0                    | 0 0                | 0     |     | 0   | 0                   | 0                  | 0       | 0      |     |
| √      |                        |                    |       |     |     | √                   |                    |         |        |     |
| |d |=  | .1632+.3012+.3012=.456 |                    |       |     | |d  | |= .1252+.6022=.615 |                    |         |        |     |
| 1      |                        |                    |       |     | 2   |                     |                    |         |        |     |
|        | Cosine:                | (cid:80) ofcolumn: | 0.747 |     |     | Cosine:             | (cid:80) ofcolumn: |         | 0.0779 |     |
Figure11.6 Computation of tf-idf cosine score between the query and nano-documents 1 (0.747) and 2
(0.0779),usingEq.11.4,Eq.11.5,Eq.11.6andEq.11.9.
|     | missing | one of the | terms. | We leave | the computation |     | for | Documents | 3 and | 4 as an |
| --- | ------- | ---------- | ------ | -------- | --------------- | --- | --- | --------- | ----- | ------- |
exerciseforthereader.
|     |                                                           | Inpractice,therearemanyvariantsandapproximationstoEq.11.9. |     |     |     |     |     |     |     | Forexam-   |
| --- | --------------------------------------------------------- | ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ---------- |
|     | ple,wemightchoosetosimplifyprocessingbyremovingsometerms. |                                                            |     |     |     |     |     |     |     | Toseethis, |
let’sstartbyexpandingtheformulafortf-idfinEq.11.9toexplicitlymentionthetf
andidftermsfromEq.11.6:
|     |     |            |     | (cid:88)  | tf t,q ·idf | t   |           | tf        | ·idf t |         |
| --- | --- | ---------- | --- | --------- | ----------- | --- | --------- | --------- | ------ | ------- |
|     |     | score(q,d) | =   |           |             |     | ·         | t,d       |        | (11.10) |
|     |     |            |     | (cid:113) |             |     | (cid:113) |           |        |         |
|     |     |            |     | (cid:80)  | tf-idf2(q   | ,q) | (cid:80)  | tf-idf2(d | ,d)    |         |
|     |     |            |     | t∈q       | qi∈q        | i   |           | di∈d      | i      |         |
Inonecommonvariantoftf-idfcosine,forexample,wedroptheidftermforthe
|     | document. | Eliminatingthesecondcopyoftheidfterm(sincetheidenticaltermis |     |     |     |     |     |     |     |     |
| --- | --------- | ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- |
alreadycomputedforthequery)turnsouttosometimesresultinbetterperformance:
|     |     |            |     |           | tf ·idf   |     |             | tf        | ·idf |         |
| --- | --- | ---------- | --- | --------- | --------- | --- | ----------- | --------- | ---- | ------- |
|     |     |            |     | (cid:88)  | t,q       | t   |             | t,d       | t    |         |
|     |     | score(q,d) | =   | (cid:113) |           |     | · (cid:113) |           |      | (11.11) |
|     |     |            |     | (cid:80)  | tf-idf2(q |     | (cid:80)    | tf-idf2(d |      |         |
|     |     |            |     | t∈q       |           | ,q) |             |           | ,d)  |         |
|     |     |            |     |           | qi∈q      | i   |             | di∈d      | i    |         |
Othervariantsoftf-idfeliminatevariousotherterms.
|     |     | A slightly more | complex | variant | in the | tf-idf | family | is the | BM25 | weighting |
| --- | --- | --------------- | ------- | ------- | ------ | ------ | ------ | ------ | ---- | --------- |
BM25
scheme(sometimescalledOkapiBM25aftertheOkapiIRsysteminwhichitwas
|     | introduced | (Robertson | et  | al., 1995)). | BM25 | adds | two | parameters: | k, a | knob that |
| --- | ---------- | ---------- | --- | ------------ | ---- | ---- | --- | ----------- | ---- | --------- |
adjuststhebalancebetweentermfrequencyandIDF,andb,whichcontrolstheim-
portanceofdocumentlengthnormalization.TheBM25scoreofadocumentdgiven

11.1 • INFORMATIONRETRIEVAL 9
aqueryqis:
IDF weightedtf
(cid:122) (cid:125)(cid:124) (cid:123)(cid:122) (cid:125)(cid:124) (cid:123)
(cid:88) (cid:18) N (cid:19) tf t,d
log (cid:16) (cid:16) (cid:17)(cid:17) (11.12)
t∈q df t k 1−b+b |d | a d v | g| +tf t,d
where |d | is the length of the average document. When k is 0, BM25 reverts to
avg
no use of term frequency, just a binary selection of terms in the query (plus idf).
A large k results in raw term frequency (plus idf). b ranges from 1 (scaling by
documentlength)to0(nolengthscaling). Manningetal.(2008)suggestreasonable
valuesarek=[1.2,2]andb=0.75. Kamphuisetal.(2020)isausefulsummaryof
themanyminorvariantsofBM25.
Stopwords Inthepastitwascommontoremovehigh-frequencywordsfromboth
thequeryanddocumentbeforerepresentingthem. Thelistofsuchhigh-frequency
stoplist wordstoberemovediscalledastoplist. Theintuitionisthathigh-frequencyterms
(oftenfunctionwordslikethe, a, to)carrylittlesemanticweightandmaynothelp
with retrieval, and can also help shrink the inverted index files we describe below.
The downside of using a stop list is that it makes it difficult to search for phrases
thatcontainwordsinthestoplist. Forexample,commonstoplistswouldreducethe
phrasetobeornottobetothephrasenot.InmodernIRsystems,theuseofstoplists
is much less common, partly due to improved efficiency and partly because much
oftheirfunctionisalreadyhandledbyIDFweighting,whichdownweightsfunction
wordsthatoccurineverydocument.Nonetheless,stopwordremovalisoccasionally
usefulinvariousNLPtaskssoisworthkeepinginmind.
11.1.4 Efficientlyfindingdocuments: theInvertedIndex
Inordertocomputescores,weneedtoefficientlyfinddocumentsthatcontainwords
inthequery. (Anydocumentthatcontainsnoneofthequerytermswillhaveascore
of0andcanbeignored.)ThebasicsearchprobleminIRisthustofindalldocuments
d∈Cthatcontainatermq∈Q.
invertedindex The data structure for this task is the inverted index, which we use for mak-
ing this search efficient, and also conveniently storing useful information like the
documentfrequencyandthecountofeachtermineachdocument.
Aninvertedindex,givenaqueryterm,givesalistofdocumentsthatcontainthe
postings term. Itconsistsoftwoparts,adictionaryandthepostings. Thedictionaryisalist
ofterms(designedtobeefficientlyaccessed),eachpointingtoapostingslistforthe
term. A postings list is the list of document IDs associated with each term, which
canalsocontaininformationlikethetermfrequencyoreventheexactpositionsof
terms in the document. The dictionary can also store the document frequency for
eachterm. Forexample,asimpleinvertedindexforour4sampledocumentsabove,
witheachwordcontainingitsdocumentfrequencyin{},andapointertoapostings
listthatcontainsdocumentIDsandtermcountsin[],mightlooklikethefollowing:
how{1} → 3[1]
is{1} → 3[1]
love{2} → 1[1]→3[1]
nurse{2} → 1[1]→4[1]
sorrow{1} → 2[1]
sweet{3} → 1[2]→2[1]→3[1]

| 10 CHAPTER11 | • RETRIEVAL-BASEDMODELS |        |          |           |     |          |             |     |           |        |           |
| ------------ | ----------------------- | ------ | -------- | --------- | --- | -------- | ----------- | --- | --------- | ------ | --------- |
|              | Given                   | a list | of terms | in query, | we  | can very | efficiently |     | get lists | of all | candidate |
documents,togetherwiththeinformationnecessarytocomputethetf-idfscoreswe
need.
| 11.2 | Evaluation | of  | Information-Retrieval |     |     |     |     |     | Systems |     |     |
| ---- | ---------- | --- | --------------------- | --- | --- | --- | --- | --- | ------- | --- | --- |
Wemeasuretheperformanceofrankedretrievalsystemsusingthesameprecision
|     | and recall | metrics | we have | been | using. | We  | make the | assumption |     | that | each docu- |
| --- | ---------- | ------- | ------- | ---- | ------ | --- | -------- | ---------- | --- | ---- | ---------- |
mentreturnedbytheIRsystemiseitherrelevanttoourpurposesornotrelevant.
Precisionisthefractionofthereturneddocumentsthatarerelevant,andrecallisthe
|     | fraction of    | all relevant |                                                         | documents | that | are returned. |     | More | formally, | let’s | assume a |
| --- | -------------- | ------------ | ------------------------------------------------------- | --------- | ---- | ------------- | --- | ---- | --------- | ----- | -------- |
|     | systemreturnsT |              | rankeddocumentsinresponsetoaninformationrequest,asubset |           |      |               |     |      |           |       |          |
Rofthesearerelevant,adisjointsubset,N,aretheremainingirrelevantdocuments,
|     | andU documentsinthecollectionasawholearerelevanttothisrequest. |     |     |     |     |     |     |     |     |     | Precision |
| --- | -------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- |
andrecallarethendefinedas:
|     |     |     |     |            |     | |R|     |     | |R| |     |     |         |
| --- | --- | --- | --- | ---------- | --- | ------- | --- | --- | --- | --- | ------- |
|     |     |     |     | Precision= |     | Recall= |     |     |     |     | (11.13) |
|     |     |     |     |            |     | |T|     |     | |U| |     |     |         |
Unfortunately,thesemetricsdon’tadequatelymeasuretheperformanceofasystem
|     | that ranks | the documents |     | it returns. |     | If we | are comparing |     | the performance |     | of two |
| --- | ---------- | ------------- | --- | ----------- | --- | ----- | ------------- | --- | --------------- | --- | ------ |
rankedretrievalsystems,weneedametricthatpreferstheonethatrankstherelevant
|     | documents | higher. | We  | need | to adapt | precision | and | recall | to capture |     | how well a |
| --- | --------- | ------- | --- | ---- | -------- | --------- | --- | ------ | ---------- | --- | ---------- |
systemdoesatputtingrelevantdocumentshigherintheranking.
|     | Let’sturntoanexample. |     |     | AssumethetableinFig.11.7givesrank-specificpre- |     |     |     |     |     |     |     |
| --- | --------------------- | --- | --- | ---------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
cisionandrecallvaluescalculatedasweproceeddownthroughasetofrankeddoc-
umentsforaparticularquery;theprecisionsarethefractionofrelevantdocuments
seenatagivenrank,andrecallsthefractionofrelevantdocumentsfoundatthesame
rank. Therecallmeasuresinthisexamplearebasedonthisqueryhaving9relevant
documentsinthecollectionasawhole.
|     | Note | that recall | is  | non-decreasing; |     | when | a relevant | document |     | is encountered, |     |
| --- | ---- | ----------- | --- | --------------- | --- | ---- | ---------- | -------- | --- | --------------- | --- |
recallincreases,andwhenanon-relevantdocumentisfounditremainsunchanged.
|     | Precision, | on the | other | hand,      | jumps      | up and | down,    | increasing | when | relevant | doc-      |
| --- | ---------- | ------ | ----- | ---------- | ---------- | ------ | -------- | ---------- | ---- | -------- | --------- |
|     | uments are | found, | and   | decreasing | otherwise. |        | The most | common     |      | way to   | visualize |
precision-recall precision and recall is to plot precision against recall in a precision-recall curve,
curve
liketheoneshowninFig.11.8forthedataintable11.7.
|     | Fig.11.8showsthevaluesforasinglequery. |     |     |     |     |     | Butwe’llneedtocombinevalues |     |     |     |     |
| --- | -------------------------------------- | --- | --- | --- | --- | --- | --------------------------- | --- | --- | --- | --- |
forallthequeries,andinawaythatletsuscompareonesystemtoanother.Oneway
ofdoingthisistoplotaveragedprecisionvaluesat11fixedlevelsofrecall(0to100,
|     | in steps of | 10). | Since we’re | not | likely | to have | datapoints |     | at these | exact | levels, we |
| --- | ----------- | ---- | ----------- | --- | ------ | ------- | ---------- | --- | -------- | ----- | ---------- |
interpolated useinterpolatedprecisionvaluesforthe11recallvaluesfromthedatapointswedo
precision
have. Wecanaccomplishthisbychoosingthemaximumprecisionvalueachieved
|     | atanylevelofrecallatorabovetheonewe’recalculating. |     |                                 |     |     |     |     |     | Inotherwords, |     |         |
| --- | -------------------------------------------------- | --- | ------------------------------- | --- | --- | --- | --- | --- | ------------- | --- | ------- |
|     |                                                    |     | IntPrecision(r)=maxPrecision(i) |     |     |     |     |     |               |     | (11.14) |
i>=r
Thisinterpolationschemenotonlyletsusaverageperformanceoverasetofqueries,
|     | but also helps | smooth | over | the | irregular | precision | values | in  | the original |     | data. It is |
| --- | -------------- | ------ | ---- | --- | --------- | --------- | ------ | --- | ------------ | --- | ----------- |
designedtogivesystemsthebenefitofthedoubtbyassigningthemaximumpreci-
|     | sionvalueachievedathigherlevelsofrecallfromtheonebeingmeasured. |     |     |     |     |     |     |     |     |     | Fig.11.9 |
| --- | --------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | -------- |
andFig.11.10showtheresultinginterpolateddatapointsfromourexample.

|            | 11.2 • EVALUATIONOFINFORMATION-RETRIEVALSYSTEMS |           |     |               |            |               | 11   |
| ---------- | ----------------------------------------------- | --------- | --- | ------------- | ---------- | ------------- | ---- |
|            | Rank                                            | Judgment  |     | Precision     |            | Recall        |      |
|            |                                                 |           |     |               | Rank       | Rank          |      |
|            | 1                                               | R         |     | 1.0           |            | .11           |      |
|            | 2                                               | N         |     | .50           |            | .11           |      |
|            | 3                                               | R         |     | .66           |            | .22           |      |
|            | 4                                               | N         |     | .50           |            | .22           |      |
|            | 5                                               | R         |     | .60           |            | .33           |      |
|            | 6                                               | R         |     | .66           |            | .44           |      |
|            | 7                                               | N         |     | .57           |            | .44           |      |
|            | 8                                               | R         |     | .63           |            | .55           |      |
|            | 9                                               | N         |     | .55           |            | .55           |      |
|            | 10                                              | N         |     | .50           |            | .55           |      |
|            | 11                                              | R         |     | .55           |            | .66           |      |
|            | 12                                              | N         |     | .50           |            | .66           |      |
|            | 13                                              | N         |     | .46           |            | .66           |      |
|            | 14                                              | N         |     | .43           |            | .66           |      |
|            | 15                                              | R         |     | .47           |            | .77           |      |
|            | 16                                              | N         |     | .44           |            | .77           |      |
|            | 17                                              | N         |     | .41           |            | .77           |      |
|            | 18                                              | R         |     | .44           |            | .88           |      |
|            | 19                                              | N         |     | .42           |            | .88           |      |
|            | 20                                              | N         |     | .40           |            | .88           |      |
|            | 21                                              | N         |     | .38           |            | .88           |      |
|            | 22                                              | N         |     | .36           |            | .88           |      |
|            | 23                                              | N         |     | .35           |            | .88           |      |
|            | 24                                              | N         |     | .33           |            | .88           |      |
|            | 25                                              | R         |     | .36           |            | 1.0           |      |
| Figure11.7 | Rank-specific                                   | precision | and | recall values | calculated | as we proceed | down |
throughasetofrankeddocuments(assumingthecollectionhas9relevantdocuments).
1.0
0.8
noisicerP
0.6
0.4
0.2
0.0
|     | 0.0 | 0.2 | 0.4 | 0.6 |     | 0.8 1.0 |     |
| --- | --- | --- | --- | --- | --- | ------- | --- |
Recall
| Figure11.8                         | Theprecisionrecallcurveforthedataintable11.7. |               |                                          |        |             |                     |              |
| ---------------------------------- | --------------------------------------------- | ------------- | ---------------------------------------- | ------ | ----------- | ------------------- | ------------ |
| Given                              | curves such                                   | as that in    | Fig. 11.10                               | we     | can compare | two systems         | or ap-       |
| proaches                           | by comparing                                  | their curves. | Clearly,                                 | curves | that        | are higher          | in precision |
| acrossallrecallvaluesarepreferred. |                                               |               | However,thesecurvescanalsoprovideinsight |        |             |                     |              |
| into the                           | overall behavior                              | of a system.  | Systems                                  | that   | are         | higher in precision | toward       |
theleftmayfavorprecisionoverrecall,whilesystemsthataremoregearedtowards
recallwillbehigherathigherlevelsofrecall(totheright).
meanaverage
| A second | way to evaluate | ranked | retrieval | is  | mean | average precision | (MAP), |
| -------- | --------------- | ------ | --------- | --- | ---- | ----------------- | ------ |
precision

12 CHAPTER11 • RETRIEVAL-BASEDMODELS
InterpolatedPrecision Recall
1.0 0.0
1.0 .10
.66 .20
.66 .30
.66 .40
.63 .50
.55 .60
.47 .70
.44 .80
.36 .90
.36 1.0
Figure11.9 InterpolateddatapointsfromFig.11.7.
Interpolated Precision Recall Curve
1
0.9
0.8
0.7
0.6
0.5
0.4
0.3
0.2
0.1
0
0 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1
Recall
noisicerP
Figure11.10 An11pointinterpolatedprecision-recallcurve. Precisionateachofthe11
standardrecalllevelsisinterpolatedforeachqueryfromthemaximumatanyhigherlevelof
recall.Theoriginalmeasuredprecisionrecallpointsarealsoshown.
which provides a single metric that can be used to compare competing systems or
approaches. In this approach, we again descend through the ranked list of items,
but nowwe note theprecision only at thosepoints where arelevant item hasbeen
encountered(forexampleatranks1,3,5,6butnot2or4inFig.11.7). Forasingle
query, we average these individual precision measurements over the return set (up
to some fixed cutoff). More formally, if we assume that R is the set of relevant
r
documentsatorabover,thentheaverageprecision(AP)forasinglequeryis
1 (cid:88)
AP= Precision r (d) (11.15)
|R |
r
d∈Rr
wherePrecision (d)istheprecisionmeasuredattherankatwhichdocumentdwas
r
found. For an ensemble of queries Q, we then average over these averages, to get
ourfinalMAPmeasure:
1 (cid:88)
MAP= AP(q) (11.16)
|Q|
q∈Q
TheMAPforthesinglequery(hence=AP)inFig.11.7is0.6.

|      |             | 11.3 | •         | INFORMATIONRETRIEVALWITHDENSEVECTORS |      |     |       |         |     |     | 13  |
| ---- | ----------- | ---- | --------- | ------------------------------------ | ---- | --- | ----- | ------- | --- | --- | --- |
| 11.3 | Information |      | Retrieval |                                      | with |     | Dense | Vectors |     |     |     |
Theclassictf-idforBM25algorithmsforIRhavelongbeenknowntohaveacon-
|     | ceptual      | flaw: they | work                                                     | only | if there | is exact | overlap | of  | words | between | the query |
| --- | ------------ | ---------- | -------------------------------------------------------- | ---- | -------- | -------- | ------- | --- | ----- | ------- | --------- |
|     | anddocument. |            | Inotherwords,theuserposingaquery(oraskingaquestion)needs |      |          |          |         |     |       |         |           |
toguessexactlywhatwordsthewriteroftheanswermighthaveused,anissuecalled
thevocabularymismatchproblem(Furnasetal.,1987).
|     | The            | solution    | to this       | problem | is       | to use  | an approach | that           | can  | handle    | synonymy: |
| --- | -------------- | ----------- | ------------- | ------- | -------- | ------- | ----------- | -------------- | ---- | --------- | --------- |
|     | instead        | of (sparse) | word-count    |         | vectors, | using   | (dense)     | embeddings.    |      | This      | idea was  |
|     | first proposed |             | for retrieval | in      | the last | century | under       | the            | name | of Latent | Semantic  |
|     | Indexing       | approach    | (Deerwester   |         | et al.,  | 1990),  | but         | is implemented |      | in modern | times     |
viaencoderslikeBERT.
Themostpowerfulapproachistopresentboththequeryandthedocumenttoa
|     | singleencoder,                     |     | allowingthetransformerself-attentiontoseeallthetokensofboth |     |          |          |                                 |                |     |         |              |
| --- | ---------------------------------- | --- | ----------------------------------------------------------- | --- | -------- | -------- | ------------------------------- | -------------- | --- | ------- | ------------ |
|     | the query                          | and | the document,                                               |     | and thus | building | a                               | representation |     | that is | sensitive to |
|     | themeaningsofbothqueryanddocument. |     |                                                             |     |          |          | Thenalinearlayercanbeputontopof |                |     |         |              |
the[CLS]tokentopredictasimilarityscoreforthequery/documenttuple:
z=BERT(q;[SEP];d)[CLS]
|     |                                      |           |         | score(q,d)=softmax(U(z)) |           |     |                                    |         |         |           | (11.17) |
| --- | ------------------------------------ | --------- | ------- | ------------------------ | --------- | --- | ---------------------------------- | ------- | ------- | --------- | ------- |
|     | ThisarchitectureisshowninFig.11.11a. |           |         |                          |           |     | Usuallytheretrievalstepisnotdoneon |         |         |           |         |
|     | an entire                            | document. | Instead |                          | documents | are | broken                             | up into | smaller | passages, | such    |
asnon-overlappingfixed-lengthchunksofsay100tokens,andtheretrieverencodes
|     | andretrievesthesepassagesratherthanentiredocuments. |         |        |        |      |           |         |     | Thequeryanddocument |     |            |
| --- | --------------------------------------------------- | ------- | ------ | ------ | ---- | --------- | ------- | --- | ------------------- | --- | ---------- |
|     | have to                                             | be made | to fit | in the | BERT | 512-token | window, |     | for example         | by  | truncating |
thequeryto64tokensandtruncatingthedocumentifnecessarysothatit,thequery,
|     | [CLS],and[SEP]fitin512tokens. |     |            |     |               | TheBERTsystemtogetherwiththelinearlayer |      |              |     |          |            |
| --- | ----------------------------- | --- | ---------- | --- | ------------- | --------------------------------------- | ---- | ------------ | --- | -------- | ---------- |
|     | U can then                    | be  | fine-tuned | for | the relevance |                                         | task | by gathering |     | a tuning | dataset of |
relevantandnon-relevantpassages.
|     | The                 | problem | with | the full                                           | BERT | architecture |     | in Fig. | 11.11a | is the | expense in |
| --- | ------------------- | ------- | ---- | -------------------------------------------------- | ---- | ------------ | --- | ------- | ------ | ------ | ---------- |
|     | computationandtime. |         |      | Withthisarchitecture,everytimewegetaquery,wehaveto |      |              |     |         |        |        |            |
passeverysingledocumentinourentirecollectionthroughaBERTencoderjointly
|     | withthenewquery! |     | Thisenormoususeofresourcesisimpracticalforrealcases. |     |     |     |     |     |     |     |     |
| --- | ---------------- | --- | ---------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Attheotherendofthecomputationalspectrumisamuchmoreefficientarchi-
|     | tecture,                                                            | the bi-encoder.                         |           | In      | this architecture |          | we                             | can encode | the       | documents | in the        |
| --- | ------------------------------------------------------------------- | --------------------------------------- | --------- | ------- | ----------------- | -------- | ------------------------------ | ---------- | --------- | --------- | ------------- |
|     | collection                                                          | only                                    | one time  | by      | using two         | separate | encoder                        | models,    |           | one to    | encode the    |
|     | query and                                                           | one                                     | to encode | the     | document.         | We       | encode                         | each       | document, |           | and store all |
|     | theencodeddocumentvectorsinadvance.                                 |                                         |           |         |                   |          | Whenaquerycomesin,weencodejust |            |           |           |               |
|     | this query                                                          | and                                     | then use  | the dot | product           | between  |                                | the query  | vector    | and       | the precom-   |
|     | puteddocumentvectorsasthescoreforeachcandidatedocument(Fig.11.11b). |                                         |           |         |                   |          |                                |            |           |           | For           |
|     | example,                                                            | ifweusedBERT,wewouldhavetwoencodersBERT |           |         |                   |          |                                |            |           | andBERT   | and           |
|     |                                                                     |                                         |           |         |                   |          |                                |            |           | Q         | D             |
[CLS]
|     | we could | represent | the | query | and document |     | as the |     | token | of the | respective |
| --- | -------- | --------- | --- | ----- | ------------ | --- | ------ | --- | ----- | ------ | ---------- |
encoders(Karpukhinetal.,2020):
|     |                |     |         |         | z q =BERT    | Q (q)[CLS] |                |     |          |     |             |
| --- | -------------- | --- | ------- | ------- | ------------ | ---------- | -------------- | --- | -------- | --- | ----------- |
|     |                |     |         |         | z d =BERT    | D (d)[CLS] |                |     |          |     |             |
|     |                |     |         |         | score(q,d)=z |            | q ·z           | d   |          |     | (11.18)     |
|     | The bi-encoder |     | is much | cheaper | than         | a full     | query/document |     | encoder, |     | but is also |
lessaccurate,sinceitsrelevancedecisioncan’ttakefulladvantageofallthepossi-

| 14 CHAPTER11 | •   | RETRIEVAL-BASEDMODELS |     |     |     |     |     |     |     |     |
| ------------ | --- | --------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
s(q,d)
s(q,d)
•
U
z
| z CLS |       |     |          |     | z   | CLS_Q |       | CLS_D |          |     |
| ----- | ----- | --- | -------- | --- | --- | ----- | ----- | ----- | -------- | --- |
|       |       |     |          | …   |     |       |       |       |          | …   |
|       |       |     |          | …   |     |       |       |       |          | …   |
|       |       |     |          | …   |     |       |       |       |          | …   |
|       |       |     |          | …   |     |       |       |       |          | …   |
|       |       |     |          | …   |     |       |       |       |          | …   |
|       |       |     |          | …   |     |       |       |       |          | …   |
| Query | [sep] |     | Document |     |     |       | Query |       | Document |     |
|       | (a)   |     |          |     |     |       |       | (b)   |          |     |
Figure11.11 Twowaystododenseretrieval,illustratedbyusinglinesbetweenlayerstoschematicallyrep-
resentself-attention: (a)Useasingleencodertojointlyencodequeryanddocumentandfinetunetoproducea
relevancescorewithalinearlayerovertheCLStoken.Thisistoocompute-expensivetouseexceptinrescoring
(b)Useseparateencodersforqueryanddocument,andusethedotproductbetweenCLStokenoutputsforthe
queryanddocumentasthescore.Thisislesscompute-expensive,butnotasaccurate.
|     | ble meaning | interactions |     | between | all | the tokens | in the | query | and the tokens | in the |
| --- | ----------- | ------------ | --- | ------- | --- | ---------- | ------ | ----- | -------------- | ------ |
document.
Therearenumerousapproachesthatlieinbetweenthefullencoderandthebi-
encoder. Oneintermediatealternativeistousecheapermethods(likeBM25)asthe
|     | first pass | relevance | ranking |     | for each | document, | take the | top       | N ranked documents, |           |
| --- | ---------- | --------- | ------- | --- | -------- | --------- | -------- | --------- | ------------------- | --------- |
|     | and use    | expensive | methods |     | like the | full BERT | scoring  | to rerank | only                | the top N |
documentsratherthanthewholeset.
ColBERT Another intermediate approach is the ColBERT approach of Khattab and Za-
|     | haria(2020)andKhattabetal.(2021),showninFig.11.12. |     |     |     |     |     |     | Thismethodseparately |     |     |
| --- | -------------------------------------------------- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- |
encodesthequeryanddocument,butratherthanencodingtheentirequeryordoc-
umentintoonevector,itseparatelyencodeseachofthemintocontextualrepresen-
|     | tationsforeachtoken. |     |     | TheseBERTrepresentationsofeachdocumentwordcanbe |     |     |     |     |     |     |
| --- | -------------------- | --- | --- | ----------------------------------------------- | --- | --- | --- | --- | --- | --- |
pre-storedforefficiency.Therelevancescorebetweenaqueryqandadocumentdis
asumofmaximumsimilarity(MaxSim)operatorsbetweentokensinqandtokens
|     | in d. Essentially, |     | for                             | each token | in q, | ColBERT | finds                     | the most | contextually | simi- |
| --- | ------------------ | --- | ------------------------------- | ---------- | ----- | ------- | ------------------------- | -------- | ------------ | ----- |
|     | lartokenind,       |     | andthensumsupthesesimilarities. |            |       |         | Arelevantdocumentwillhave |          |              |       |
tokensthatarecontextuallyverysimilartothequery.
|     | Moreformally,aquestionqistokenizedas[q |     |     |     |     |     | ,...,q | ],prependedwitha[CLS] |     |     |
| --- | -------------------------------------- | --- | --- | --- | --- | --- | ------ | --------------------- | --- | --- |
|     |                                        |     |     |     |     |     | 1      | n                     |     |     |
andaspecial[Q]token,truncatedtoN=32tokens(orpaddedwith[MASK]tokensif
|     | itisshorter),andpassedthroughBERTtogetoutputvectorsq=[q |         |                                                     |             |         |              |             |             | ,...,q      | ]. The   |
| --- | ------------------------------------------------------- | ------- | --------------------------------------------------- | ----------- | ------- | ------------ | ----------- | ----------- | ----------- | -------- |
|     |                                                         |         |                                                     |             |         |              |             |             | 1           | N        |
|     | passage                                                 | d with  | tokens                                              | [d 1 ,...,d | m ], is | processed    | similarly,  | including   | a [CLS]     | and      |
|     | special[D]token.                                        |         | Alinearlayerisappliedontopofdandqtocontroltheoutput |             |         |              |             |             |             |          |
|     | dimension,                                              | so      | as to keep                                          | the         | vectors | small        | for storage | efficiency, | and vectors | are      |
|     | rescaled                                                | to unit | length,                                             | producing   | the     | final vector | sequences   |             | E q (length | N) and E |
d
|     | (lengthm). | TheColBERTscoringmechanismis: |     |     |     |     |     |     |     |     |
| --- | ---------- | ----------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
N
(cid:88)
|     |     |     |     | score(q,d)= |     |     | m xE ·E |     |     |         |
| --- | --- | --- | --- | ----------- | --- | --- | ------- | --- | --- | ------- |
|     |     |     |     |             |     | m   | a qi dj |     |     | (11.19) |
j= 1
i=1
|     | While | the interaction |     | mechanism |     | has no | tunable parameters, |     | the ColBERT | ar- |
| --- | ----- | --------------- | --- | --------- | --- | ------ | ------------------- | --- | ----------- | --- |

11.3 • INFORMATIONRETRIEVALWITHDENSEVECTORS 15
s(q,d)
∑
MaxSim MaxSim MaxSim
norm norm norm norm norm norm
…
…
…
…
…
…
Query Document
Figure11.12 AsketchoftheColBERTalgorithmatinferencetime. Thequeryanddoc-
umentarefirstpassedthroughseparateBERTencoders. Similaritybetweenqueryanddoc-
umentiscomputedbysummingasoftalignmentbetweenthecontextualrepresentationsof
tokens in the query and the document. Training is end-to-end. (Various details aren’t de-
picted;forexamplethequeryisprependedbya[CLS]and[Q:]tokens,andthedocument
by[CLS]and[D:]tokens).FigureadaptedfromKhattabandZaharia(2020).
chitecture still needs to be trained end-to-end to fine-tune the BERT encoders and
trainthelinearlayers(andthespecial[Q]and[D]embeddings)fromscratch. Itis
trainedontriples(cid:104)q,d+,d−(cid:105)ofqueryq, positivedocumentd+ andnegativedocu-
mentd− toproduceascoreforeachdocumentusingEq.11.19, optimizingmodel
parametersusingacross-entropyloss.
All the supervised algorithms (like ColBERT or the full-interaction version of
theBERTalgorithmappliedforreranking)needtrainingdataintheformofqueries
together with relevant and irrelevant passages or documents (positive and negative
examples). There are various semi-supervised ways to get labels; some datasets
(likeMSMARCORanking,Section11.5)containgoldpositiveexamples. Negative
examples can be sampled randomly from the top-1000 results from some existing
IRsystem. Ifdatasetsdon’thavelabeledpositiveexamples, iterativemethodslike
relevance-guidedsupervisioncanbeused(Khattabetal.,2021)whichrelyonthe
factthatmanydatasetscontainshortanswerstrings. Inthismethod,anexistingIR
systemisusedtoharvestexamplesthatdocontainshortanswerstrings(thetopfew
aretakenaspositives)ordon’tcontainshortanswerstrings(thetopfewaretakenas
negatives),theseareusedtotrainanewretriever,andthentheprocessisiterated.
Efficiencyisanimportantissue,sinceeverypossibledocumentmustberanked
for its similarity to the query. For sparse word-count vectors, the inverted index
allows this very efficiently. For dense vector algorithms finding the set of dense
document vectors that have the highest dot product with a dense query vector is
an instance of the problem of nearest neighbor search. Modern systems there-
Faiss foremakeuseofapproximatenearestneighborvectorsearchalgorithmslikeFaiss
(Johnsonetal.,2017).

| 16 CHAPTER11 | •                   | RETRIEVAL-BASEDMODELS |     |     |            |     |     |       |     |     |
| ------------ | ------------------- | --------------------- | --- | --- | ---------- | --- | --- | ----- | --- | --- |
| 11.4         | Retrieval-Augmented |                       |     |     | Generation |     |     | (RAG) |     |     |
Theinformationretrievaltechniquesweintroducedinthepriorsectioncanbeinte-
gratedintolanguagemodelsviaamethodcalledretrieval-augmentedgeneration
orRAG.InthebasicRAGscenariothatwewilldescribeinthissection,weuseIR
|     | techniques                     | to retrieve |     | documents | from                                   | some | specified | store | of documents | that are |
| --- | ------------------------------ | ----------- | --- | --------- | -------------------------------------- | ---- | --------- | ----- | ------------ | -------- |
|     | likelytohaveusefulinformation. |             |     |           | Thenweusealargelanguagemodeltogenerate |      |           |       |              |          |
ananswerconditionedonthesedocumentsinadditiontotheoriginalquery.
|     | As we               | summarized |             | in the      | introduction | to         | the chapter, | there          | are       | many goals of  |
| --- | ------------------- | ---------- | ----------- | ----------- | ------------ | ---------- | ------------ | -------------- | --------- | -------------- |
|     | retrieval-augmented |            | generation. |             | RAG          | can help   | mitigate     | hallucination, |           | by giving      |
|     | the model           | a set      | of trusted  | documents.  |              | RAG        | can also     | help           | language  | models gen-    |
|     | erate factual       | text       | about       | proprietary |              | data, like | personal     | email,         | or health | records, or    |
|     | company-internal    |            | documents,  |             | or other     | legal      | documents.   | RAG            | can       | also help with |
theproblemthatknowledgeisdynamicandtime-sensitive,forexampleifweknow
theuser’sinformationneedreferencesdatafromatimeafteralanguagemodelwas
trained.
|     | ARAGsystemisbasedontwomajorcomponents: |     |     |     |     |     |     | theretrieverandthegener- |     |     |
| --- | -------------------------------------- | --- | --- | --- | --- | --- | --- | ------------------------ | --- | --- |
ator,(thelatterissometimescalled,forhistoricalreasons,thereader(Chenetal.,
2017)). Fig.11.13sketchesoutthisstandardmodelforansweringquestions.
User prompt:
|     |     | Retriever |     |     |     |     | Generator |     |     |     |
| --- | --- | --------- | --- | --- | --- | --- | --------- | --- | --- | --- |
When was
the premiere of
| The Magic Flute? |     |     |     |     |     | Prompt  |     |     |                  |     |
| ---------------- | --- | --- | --- | --- | --- | ------- | --- | --- | ---------------- | --- |
|                  |     |     |     |     |     |         |     | LLM | 1791, according  |     |
formulation
to this page
Indexed Docs
|     |     |     |     | Relevant |     |     | Knowledge |     |     |     |
| --- | --- | --- | --- | -------- | --- | --- | --------- | --- | --- | --- |
Citation
|     |     | Corpus of |     | Docs |     |     |     |     |     |     |
| --- | --- | --------- | --- | ---- | --- | --- | --- | --- | --- | --- |
Documents
Figure11.13 Retrieval-augmentedgenerationtakesasinputauserprompt(whichmayexpressaninforma-
tionneedlikethisquestionexample),andacorpusofdocumentsthatmaybeusefulinmeetingtheinformation
need.Themethodhastwostages:retrieval,whichreturnsrelevantdocumentsfromthecollection,andgenera-
tion,inwhichanLLMgeneratestextgiventhedocumentsasaprompt.Somegenerationsincludeaknowledge
citationthatcanhelptheuserdecidewhethertotrustthegeneration,orfollowupiftheyareinterested.
retrieval-
augmented Inthefirststageoftheretrieval-augmentedgeneration,orRAGmodelshown
generation inFig.11.13weretrieverelevantpassagesfromsomeprespecifiedtextcollection,
RAG
|     | for example | using | the | dense | retrievers | of the | previous | section. | In the | second gen- |
| --- | ----------- | ----- | --- | ----- | ---------- | ------ | -------- | -------- | ------ | ----------- |
eratestage,wetakethesetofretrievedpassages,integrateitwiththeuserprompt,
|     | and pass | some version |     | of these | to  | a large language |     | model | to generate | an answer |
| --- | -------- | ------------ | --- | -------- | --- | ---------------- | --- | ----- | ----------- | --------- |
conditionedonthesetwothings.
|     | ForexampleimaginetheuserasksthequestionWhat |       |         |                                                  |     |     |     | year | was | the premiere |
| --- | ------------------------------------------- | ----- | ------- | ------------------------------------------------ | --- | --- | --- | ---- | --- | ------------ |
|     | of The                                      | Magic | Flute?. | Wepassthisquestiontoadenseretrieverandreturnase- |     |     |     |      |     |              |
riesofpassagesaboutTheMagicFlute.
Theideaofretrieval-augmentedgenerationistoconditionontheretrievedpas-
sages,jointlywithsomeprompttext,forexamplelike“Basedonthesetexts,answer
|     | this question:”. |     | Thus given | a   | document | collection | D   | and a | user query | q, the most |
| --- | ---------------- | --- | ---------- | --- | -------- | ---------- | --- | ----- | ---------- | ----------- |
basicRAGalgorithmis:
,thetop-krelevantpassagesfromD
|     | 1. CallaretrievertoreturnR(q)=d |     |     |     |     | 1 ···d | k   |     |     |     |
| --- | ------------------------------- | --- | --- | --- | --- | ------ | --- | --- | --- | --- |

11.4 • RETRIEVAL-AUGMENTEDGENERATION(RAG) 17
2. Createapromptthatincludesqandtheretrievedpassages
3. CallanLLMwiththeprompt
Theresultingpromptsmightlooksomethinglike:
SchematicofaRAGPrompt
retrieved passage 1
retrieved passage 2
...
retrieved passage k
Based on these texts, answer this question: What year
was the premiere of The Magic Flute?
Thetaskforthelanguagemodelisthentogeneratetextaccordingtothisproba-
bilitymodel:
n
(cid:89)
p(x ,...,x ) = p(x|R(q); Answerthefollowingquestion... ; q;x )
1 n i <i
i=1
There are many augmentations of this basic RAG paradigm. One addition is
the use of agent-based RAG. In the RAG paradigm described so far, a search is
always run and then retrieved passages are combined with the user’s question in a
prompt. Butinactualapplications,wemaynotwanttorunretrievalforeveryuser
turn. Orwemaywanttoretrievefromdifferentcollectionsfordifferentuserneeds
(sometimes the web, other times a private collection). In agent-based RAG, the
systemdecideswhentocallaretrievalagentandforwhichcollection.
Anotherresearchareahastodowiththerelationshipbetweentheretrieverand
the generator. For example there may be noise in the retrieved passages; some of
themmaybeirrelevantorwrong,orinanunhelpfulorder. Howcanweencourage
the LLM to focus on the good passages? Some RAG architectures add a reranker
thatreranksorreorderspassagesaftertheyareretrieved.Orsomecomplexquestions
mayrequiremulti-hoparchitectures,inwhichaqueryisusedtoretrievedocuments,
whicharethenappendedtotheoriginalqueryforasecondstageofretrieval.
Another class of solutions is to train the LLM for RAG. The basic version of
RAG describe above involves no training; we take an off-the-shelf LLM, and give
it the passages and a prompt and hope that it will correctly figure out which pas-
sagesareusefulorrelevantingeneratingtheanswer. Onelearningvariantinvolves
instruction-tuning an LLM, by first creating a dataset of questions annotated with
retrievedpassagesandcorrectanswers,andtheninstruction-tuningtheLLMtocor-
rectlyanswerthequestionsfromthepassages.Analternativemethodistodothisvia
test-timecompute,promptingtheLLMtoanswerthequestionandsimultaneouslyto
generatereflectionsonwhichpassageswereuseful. Theprocessofgeneratingthese
reflectionsmayleadtheLLMtoimproveatidentifyinggoodpassages. Theresult-
ingreflectiontextcanalsobeusedforin-contextlearning,forexamplebyusingthe
textaspartofapromptforfurtherquestions.
InadditiontotrainingtheLLM,wecouldtraintheIRengine. Afterall,theIR
engineitselfhasnotbeenoptimizedfortheRAGscenario. Itmightnothavebeen

18 CHAPTER11 • RETRIEVAL-BASEDMODELS
trained,orifitwas,itwaslikelytrainedforsimpleIRorfactoidquestion-answering
tasks, not fortheRAGscenario wheretheretrieved passagesarespecifically tobe
usedbyanotherLLMforgeneratingtexts. Wecanaddressthismismatchfortrain-
ableIRalgorithmsbydoingend-to-endtrainingoftheentirearchitectureonsome
setofquestionsandanswers,trainingtheparametersoftheIRmodelaswellasthe
LLM.
Finally,itisgenerallyusefulforLLMstogivetheuserevidenceforanyfactual
knowledge statement. This can be in the form of knowledge citations, such as URLs of a
citations
trustedsourceorcitationreferencestoparticularliterature. Forexampleaquestion
answeringsystemmightgeneratenumberedpointerstoURLsasfollows:
Q:WhichfilmshaveGongLiasamemberoftheircast?
A:TheStoryofQiuJu[1], FarewellMyConcubine[2], TheMonkey
King2[3],Mulan[3],SaturdayFiction[3]...
The simplest way for generating knowledge citations is to specify it as part of
theprompt. ForexampleGaoetal.(2023)employapromptwithtextlike:
‘‘Write an answer for the given question using only the
provided search results (some of which might be irrelevant)
and cite them properly... Always cite for any factual claim".
11.5 Datasets
Therearescoresofdatasetsthatcontaininformationneedsintheformofquestions,
annotated with the answer. These can be used both for instruction tuning and for
evaluationofthequestionansweringabilitiesoflanguagemodels.
We can distinguish the datasets along many dimensions, summarized nicely in
Rogersetal.(2023).Oneistheoriginalpurposeofthequestionsinthedata,whether
they were natural information-seeking questions, or whether they were questions
designedforprobing: evaluatingortestingsystemsorhumans.
Natural On the natural side there are datasets like Natural Questions (Kwiatkowski
Questions
etal.,2019),asetofanonymizedEnglishqueriestotheGooglesearchengineand
their answers. The answers are created by annotators based on Wikipedia infor-
mation, and include a paragraph-length long answer and a short span answer. For
examplethequestion“Whenarehopsaddedtothebrewingprocess?” hastheshort
answertheboilingprocessandalonganswerwhichisanentireparagraphfromthe
WikipediapageonBrewing.
MSMARCO AsimilarnaturalquestionsetistheMSMARCO(MicrosoftMachineReading
Comprehension)collectionofdatasets,including1millionrealanonymizedEnglish
questionsfromMicrosoftBingquerylogstogetherwithahumangeneratedanswer
and 9 million passages (Bajaj et al., 2016), that can be used both to test retrieval
rankingandquestionanswering.
Although many datasets focus on English, natural information-seeking ques-
tion datasets exist in other languages. The DuReader dataset is a Chinese QA re-
sourcebasedonsearchenginequeriesandcommunityQA(Heetal.,2018). TyDi
TyDiQA QAdatasetcontains204Kquestion-answerpairsfrom11typologicallydiverselan-
guages,includingArabic,Bengali,Kiswahili,Russian,andThai(Clarketal.,2020).
In the TYDI QA task, a systemis given aquestion and thepassages froma Wiki-
pediaarticleandmust(a)selectthepassagecontainingtheanswer(or NULL ifno
passagecontainstheanswer),and(b)marktheminimalanswerspan(orNULL).

11.5 • DATASETS 19
MMLU OntheprobingsidearedatasetslikeMMLU(MassiveMultitaskLanguageUn-
derstanding), a commonly-used dataset of 15908 knowledge and reasoning ques-
tionsin57areasincludingmedicine,mathematics,computerscience,law,andoth-
ers. MMLUquestionsaresourcedfromvariousexamsforhumans,suchastheUS
GraduateRecordExam,MedicalLicensingExamination,andAdvancedPlacement
exams. Sothequestionsdon’trepresentpeople’sinformationneeds, butratherare
designed to test human knowledge for academic or licensing purposes. Fig. 11.14
showssomeexamples,withthecorrectanswersinbold.
MMLUexamples
CollegeComputerScience
Any set of Boolean operators that is sufficient to represent all Boolean ex-
pressionsissaidtobecomplete. WhichofthefollowingisNOTcomplete?
(A)AND,NOT
(B)NOT,OR
(C)AND,OR
(D)NAND
CollegePhysics
The primary source of the Sun’s energy is a series of thermonuclear
reactions in which the energy produced is c2 times the mass difference
between
(A)twohydrogenatomsandoneheliumatom
(B)fourhydrogenatomsandoneheliumatom
(C)sixhydrogenatomsandtwoheliumatoms
(D)threeheliumatomsandonecarbonatom
InternationalLaw
Whichofthefollowingisatreaty-basedhumanrightsmechanism?
(A)TheUNHumanRightsCommittee
(B)TheUNHumanRightsCouncil
(C)TheUNUniversalPeriodicReview
(D)TheUNspecialmandates
Prehistory
Unlike most other early civilizations, Minoan culture shows little evidence
of
(A)trade.
(B)warfare.
(C)thedevelopmentofacommonreligion.
(D)conspicuousconsumptionbyelites.
Figure11.14 ExampleproblemsfromMMLU
Someofthequestiondatasetsdescribedaboveaugmenteachquestionwithpas-
sage(s)fromwhichtheanswercanbeextracted.Thesedatasetsweremainlycreated
reading for an earlier QA task called reading comprehension in which a model is given
comprehension
a question and a document and is required to extract the answer from the given
document. We sometimes call the task of question answering given one or more
openbook documents (for example via RAG), the open book QA task, while the task of an-

| 20 CHAPTER11 | •   | RETRIEVAL-BASEDMODELS |     |     |     |     |     |     |     |     |     |
| ------------ | --- | --------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
sweringdirectlyfromtheLMwithnoretrievalcomponentatallistheclosedbook
closedbook
QAtask.5
|     |     | Thusdatasets |     | likeNatural |     | Questions | canbe | treatedasopen |     |     | bookif the |
| --- | --- | ------------ | --- | ----------- | --- | --------- | ----- | ------------- | --- | --- | ---------- |
solveruseseachquestion’sattacheddocument,orclosedbookifthedocumentsare
notused,whiledatasetslikeMMLUaresolelyclosedbook.
|     | Another         |           | dimension                                 | of  | variation   | is the | format     | of the         | answer: | multiple-choice |            |
| --- | --------------- | --------- | ----------------------------------------- | --- | ----------- | ------ | ---------- | -------------- | ------- | --------------- | ---------- |
|     | versusfreeform. |           | Andofcoursetherearevariationsinprompting, |     |             |        |            |                |         | likewhetherthe  |            |
|     | model           | is just   | the question                              |     | (zero-shot) | or     | also given | demonstrations |         | of              | answers to |
|     | similar         | questions | (few-shot).                               |     | MMLU        | offers | both       | zero-shot      | and     | few-shot        | prompt     |
options.
| 11.6 | Evaluating                                               |     | Question |          | Answering |     |             |                    |     |             |          |
| ---- | -------------------------------------------------------- | --- | -------- | -------- | --------- | --- | ----------- | ------------------ | --- | ----------- | -------- |
|      | Two techniques                                           |     | are      | commonly | employed  |     | to evaluate | question-answering |     |             | systems, |
|      | withthechoicedependingonthetypeofquestionandQAsituation. |     |          |          |           |     |             |                    |     | Formultiple |          |
choicequestionslikeinMMLU,wereportexactmatch:
|     |     | Exactmatch: |     | The%ofpredictedanswersthatmatchthegoldanswer |     |     |     |     |     |     |     |
| --- | --- | ----------- | --- | -------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
exactly.
Forquestionswithfreetextanswers,likeNaturalQuestions,wecommonlyevalu-
|     | atedwithtokenF |     | 1   | scoretoroughlymeasurethepartialstringoverlapbetweenthe |     |     |     |     |     |     |     |
| --- | -------------- | --- | --- | ------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- |
answerandthereferenceanswer:
|     |     | F score: | The | average | token | overlap | between | predicted |     | and gold | an- |
| --- | --- | -------- | --- | ------- | ----- | ------- | ------- | --------- | --- | -------- | --- |
1
|     |     | swers. | Treatthepredictionandgoldasabagoftokens,andcomputeF |     |     |     |     |     |     |     |     |
| --- | --- | ------ | --------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
1
|     |     | foreachquestion,thenreturntheaverageF |     |     |     |     |     | overallquestions. |     |     |     |
| --- | --- | ------------------------------------- | --- | --- | --- | --- | --- | ----------------- | --- | --- | --- |
1
| 11.7 | Summary |     |     |     |     |     |     |     |     |     |     |
| ---- | ------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Thischapterintroducedthetasksofinformationretrievalandtheuseofretrieval
|     | augmented |     | generation | (RAG) | to  | use retrieved | passages |     | to improve | question | an- |
| --- | --------- | --- | ---------- | ----- | --- | ------------- | -------- | --- | ---------- | -------- | --- |
sweringandotherfactualgenerationsfromLLMs.
|     | •   | We focus | in this | chapter | on              | the use | of information |          | retrieval | for question | an-        |
| --- | --- | -------- | ------- | ------- | --------------- | ------- | -------------- | -------- | --------- | ------------ | ---------- |
|     |     | swering  | and     | related | factually-based |         | tasks.         | The idea | is to     | meet the     | user’s in- |
formationneedsbydrawingonthematerialinsomesetofdocuments(which
mightbetheweb).
• InformationRetrieval(IR)isthetaskofreturningdocumentstoauserbased
|     |     | on their | information |     | need as | expressed | in  | a query. | In ranked | retrieval, | the |
| --- | --- | -------- | ----------- | --- | ------- | --------- | --- | -------- | --------- | ---------- | --- |
documentsarereturnedinrankedorder.
• TwoparadigmsforIRaresparseretrievalanddenseretrieval.Bothparadigms
useadocument’ssimilaritytothequeryasanestimateofitsrelevancetothe
user’sinformationneed
• Insparseretrievaltechniques,werepresentboththequeryandthedocument
assparsevectorsoftheunigramcountsofthewordstheycontain,eachcount
weightedbytf-idforBM25.Thenthequery-documentsimilaritycanbemea-
suredbythecosinebetweenthesesparsevectors.
5 Thisrepurposesthewordfortypesofexamsinwhichstudentsareallowedto‘opentheirbooks’or
not.

HISTORICALNOTES 21
• Theinvertedindexisastoragemechanismforsparseretrievalthatmakesit
veryefficienttofinddocumentsthathaveaparticularword.
• Indenseretrievaltechniques,documentsorqueriesareinsteadrepresentedas
embeddings(densevectors)computedbyalanguagemodel(whetherencoder-
onlymodelsliketheBERTfamily,ordecoder-only). Document-querysimi-
larityiscomputedasdotproductorcosineintheyembeddingspace.
• For dense retrieval, FAISS is an approximate nearest neighbor vector search
algorithm that makes it very efficient to find the k most similar document
embeddingstoaqueryembedding,makingitquicktodoranking.
• Rankedretrievalisgenerallyevaluatedbymeanaverageprecisionorinter-
polatedprecision.
• Retrievalcanbeincorporatedintolanguagemodelingviaretrieval-augmented
generation.Intheretrievalstep,theuserqueryispassedtothesearchengine
toretrieveasetofrelevantdocumentsorpassages. Inthegenerationstage,
a large language model is prompted with the query and a set of documents
retrievedfromthecollection,andthenconditionallygeneratesananswer.
• Factualtaskslikequestionansweringcanbeevaluatedbyexactmatchwitha
known answer if only a single answer is given, with token F score for free
1
textanswers.
Historical Notes
Question answering was one of the earliest NLP tasks. By 1961 the BASEBALL
system (Green et al., 1961) answered questions about baseball games like “Where
did the Red Sox play on July 7” by querying a structured database of game infor-
mation. Thedatabasewasstoredasakindofattribute-valuematrixwithvaluesfor
attributesofeachgame:
Month = July
Place = Boston
Day = 7
Game Serial No. = 96
(Team = Red Sox, Score = 5)
(Team = Yankees, Score = 3)
Each question was constituency-parsed using the algorithm of Zellig Harris’s
TDAPprojectattheUniversityofPennsylvania,essentiallyacascadeoffinite-state
transducers (see the historical discussion in Joshi and Hopely 1999 and Karttunen
1999). Theninacontentanalysisphaseeachwordorphrasewasassociatedwitha
programthatcomputedpartsofitsmeaning. Thusthephrase‘Where’hadcodeto
assign the semantics Place = ?, with the result that the question “Where did the
RedSoxplayonJuly7”wasassignedthemeaning
Place = ?
Team = Red Sox
Month = July
Day = 7
Thequestionisthenmatchedagainstthedatabasetoreturntheanswer.

22 CHAPTER11 • RETRIEVAL-BASEDMODELS
TheProtosynthexsystemofSimmonsetal.(1964),givenaquestion,formeda
queryfromthecontentwordsinthequestion, andthenretrievedcandidateanswer
sentences in the document, ranked by their frequency-weighted term overlap with
thequestion. Thequeryandeachretrievedsentencewerethenparsedwithdepen-
dencyparsers,andthesentencewhosestructurebestmatchesthequestionstructure
selected. Thus the question What do worms eat? would match worms eat grass:
both have the subject worms as a dependent of eat, in the version of dependency
grammarusedatthetime,whilebirdseatwormshasbirdsasthesubject:
What do worms eat Worms eat grass Birds eat worms
Simmons(1965)summarizesotherearlyQAsystems.
By the 1970s, systems used predicate calculus as the meaning representation
LUNAR language. TheLUNARsystem(Woodsetal.1972, Woods1978)wasdesignedto
beanaturallanguageinterfacetoadatabaseofchemicalfactsaboutlunargeology.It
couldanswerquestionslikeDoanysampleshavegreaterthan13percentaluminum
byparsingthemintoalogicalform
(TEST (FOR SOME X16 / (SEQ SAMPLES) : T ; (CONTAIN’ X16
(NPR*X17/(QUOTEAL203))(GREATERTHAN13PCT))))
Bythe1990squestionansweringshiftedtomachinelearning.ZelleandMooney
(1996) proposed to treat question answering as a semantic parsing task, by creat-
ingtheProlog-basedGEOQUERYdatasetofquestionsaboutUSgeography. This
model was extended by Zettlemoyer and Collins (2005) and 2007. By a decade
later, neural models were applied to semantic parsing (Dong and Lapata 2016, Jia
andLiang2016),andthentoknowledge-basedquestionansweringbymappingtext
toSQL(Iyeretal.,2017).
[TBD:HistoryofIR.]
Meanwhile,aparadigmforansweringquestionsthatdrewmoreoninformation-
retrievalwasinfluencedbytheriseofthewebinthe1990s. TheU.S.government-
sponsoredTREC(TextREtrievalConference)evaluations,runannuallysince1992,
provideatestbedforevaluatinginformation-retrievaltasksandtechniques(Voorhees
andHarman,2005). TREC addedaninfluentialQAtrackin1999, whichledtoa
wide variety of factoid and non-factoid question answering systems competing in
annualevaluations.
At that same time, Hirschman et al. (1999) introduced the idea of using chil-
dren’s reading comprehension tests to evaluate machine text comprehension algo-
rithms. Theyacquiredacorpusof120passageswith5questionseachdesignedfor
3rd-6th grade children, built an answer extraction system, and measured how well
the answers given by their system corresponded to the answer key from the test’s
publisher. Their algorithm focused on word overlap as a feature; later algorithms
addednamedentityfeaturesandmorecomplexsimilaritybetweenthequestionand
theanswerspan(RiloffandThelen2000,Ngetal.2000).
The DeepQA component of the Watson Jeopardy! system was a large and so-
phisticatedfeature-basedsystemdevelopedjustbeforeneuralsystemsbecamecom-
mon. It is described in a series of papers in volume 56 of the IBM Journal of Re-
searchandDevelopment,e.g.,Ferrucci(2012).
Early neural reading comprehension systems drew on the insight common to
earlysystemsthatanswerfindingshouldfocusonquestion-passagesimilarity.Many

EXERCISES 23
ofthearchitecturaloutlinesoftheseneuralsystemswerelaidoutinHermannetal.
| (2015),Chenetal.(2017),andSeoetal.(2017). |     |     |     |     |     | Thesesystemsfocusedondatasets |     |
| ----------------------------------------- | --- | --- | --- | --- | --- | ----------------------------- | --- |
likeRajpurkaretal.(2016)andRajpurkaretal.(2018)andtheirsuccessors,usually
usingseparateIRalgorithmsasinputtoneuralreadingcomprehensionsystems.The
paradigmofusingdenseretrievalwithaspan-basedreader,oftenwithasingleend-
| to-end architecture, |                                                           | is exemplified                                             |     | by  | systems | like Lee et al. | (2019) or Karpukhin |
| -------------------- | --------------------------------------------------------- | ---------------------------------------------------------- | --- | --- | ------- | --------------- | ------------------- |
| etal.(2020).         | Animportantresearchareawithdenseretrievalforopen-domainQA |                                                            |     |     |         |                 |                     |
| istrainingdata:      |                                                           | usingself-supervisedmethodstoavoidhavingtolabelpositiveand |     |     |         |                 |                     |
negativepassages(Sachanetal.,2023).
Earlyworkonlargelanguagemodelsshowedthattheystoredsufficientknowl-
| edge in              | the pretraining |            | process    | to answer  | questions        | (Petroni        | et al., 2019; Raffel |
| -------------------- | --------------- | ---------- | ---------- | ---------- | ---------------- | --------------- | -------------------- |
| et al., 2020;        | Radford         | et         | al., 2019; | Roberts    | et al.,          | 2020), at first | not competitively    |
| with special-purpose |                 | question   |            | answerers, | but quickly      | surpassing      | them. Retrieval-     |
| augmented            | generation      | algorithms |            | were       | first introduced | as a            | way to improve lan-  |
guagemodelingwordprediction(Khandelwaletal.,2019),butwerequicklyapplied
toquestionanswering(Izacardetal.,2022;Rametal.,2023;Shietal.,2023).
Exercises

| 24 Chapter11 |     | •   | Retrieval-basedModels |     |     |     |     |     |     |     |
| ------------ | --- | --- | --------------------- | --- | --- | --- | --- | --- | --- | --- |
Babbage,C.1864. PassagesfromtheLifeofaPhilosopher. Johnson, J., M. Douze, and H. Je´gou. 2017. Billion-
| Longman. |     |     |     |     |     | scale similarity | search | with GPUs. | ArXiv | preprint |
| -------- | --- | --- | --- | --- | --- | ---------------- | ------ | ---------- | ----- | -------- |
arXiv:1702.08734.
| Bajaj, P., | D. Campos, | N.  | Craswell, | L. Deng, | J. G. ando |     |     |     |     |     |
| ---------- | ---------- | --- | --------- | -------- | ---------- | --- | --- | --- | --- | --- |
Xiaodong Liu, R. Majumder, A. McNamara, B. Mitra, Joshi,A.K.andP.Hopely.1999. Aparserfromantiquity.
T.Nguye,M.Rosenberg,X.Song,A.Stoica,S.Tiwary, InA.Kornai,ed.,ExtendedFiniteStateModelsofLan-
andT.Wang.2016. MSMARCO:Ahumangenerated guage,6–15.CambridgeUniversityPress.
MAchineReadingCOmprehensiondataset.NeurIPS.
|                                                   |     |     |     |     |     | Jurafsky,D.2014. | TheLanguageofFood. |     | W.W.Norton, |     |
| ------------------------------------------------- | --- | --- | --- | --- | --- | ---------------- | ------------------ | --- | ----------- | --- |
| Chen,D.,A.Fisch,J.Weston,andA.Bordes.2017.Reading |     |     |     |     |     | NewYork.         |                    |     |             |     |
Wikipediatoansweropen-domainquestions.ACL. Kamphuis,C.,A.P.deVries,L.Boytsov,andJ.Lin.2020.
Clark, J. H., E. Choi, M. Collins, D. Garrette, WhichBM25doyoumean? alarge-scalereproducibil-
T. Kwiatkowski, V. Nikolaev, and J. Palomaki. 2020. itystudyofscoringvariants. EuropeanConferenceon
| TyDi QA: | A benchmark |     | for information-seeking |     | ques- | InformationRetrieval. |     |     |     |     |
| -------- | ----------- | --- | ----------------------- | --- | ----- | --------------------- | --- | --- | --- | --- |
tionansweringintypologicallydiverselanguages.TACL, Karpukhin,V.,B.Og˘uz,S.Min,P.Lewis,L.Wu,S.Edunov,
| 8:454–470. |     |     |     |     |     | D.Chen,andW.-t.Yih.2020.Densepassageretrievalfor |     |     |     |     |
| ---------- | --- | --- | --- | --- | --- | ------------------------------------------------ | --- | --- | --- | --- |
Dahl,M.,V.Magesh,M.Suzgun,andD.E.Ho.2024.Large open-domainquestionanswering.EMNLP.
| legalfictions: | Profilinglegalhallucinationsinlargelan- |     |     |     |     |                   |                  |     |                 |     |
| -------------- | --------------------------------------- | --- | --- | --- | --- | ----------------- | ---------------- | --- | --------------- | --- |
|                |                                         |     |     |     |     | Karttunen,L.1999. | CommentsonJoshi. |     | InA.Kornai,ed., |     |
guagemodels.JournalofLegalAnalysis,16:64–93.
ExtendedFiniteStateModelsofLanguage,16–18.Cam-
bridgeUniversityPress.
Deerwester,S.C.,S.T.Dumais,T.K.Landauer,G.W.Fur-
nas,andR.A.Harshman.1990. Indexingbylatentse- Khandelwal,U.,O.Levy,D.Jurafsky,L.Zettlemoyer,and
manticsanalysis.JASIS,41(6):391–407.
|     |     |     |     |     |     | M.Lewis.2019. | Generalizationthroughmemorization: |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------- | ---------------------------------- | --- | --- | --- |
Dong, L.andM.Lapata.2016. Languagetologicalform Nearestneighborlanguagemodels.ICLR.
withneuralattention.ACL. Khattab, O., C. Potts, and M. Zaharia. 2021. Relevance-
Ferrucci,D.A.2012.Introductionto“ThisisWatson”.IBM guidedsupervisionforOpenQAwithColBERT. TACL,
| JournalofResearchandDevelopment,56(3/4):1:1–1:15. |        |              |     |           |           | 9:929–944.                   |     |     |                      |     |
| ------------------------------------------------- | ------ | ------------ | --- | --------- | --------- | ---------------------------- | --- | --- | -------------------- | --- |
|                                                   |        |              |     |           |           | Khattab,O.andM.Zaharia.2020. |     |     | ColBERT:Efficientand |     |
| Furnas, G.                                        | W., T. | K. Landauer, | L.  | M. Gomez, | and S. T. |                              |     |     |                      |     |
effectivepassagesearchviacontextualizedlateinterac-
| Dumais. | 1987. | The | vocabulary | problem | in human- |     |     |     |     |     |
| ------- | ----- | --- | ---------- | ------- | --------- | --- | --- | --- | --- | --- |
tionoverBERT.SIGIR.
| system | communication. |     | Communications |     | of the ACM, |     |     |     |     |     |
| ------ | -------------- | --- | -------------- | --- | ----------- | --- | --- | --- | --- | --- |
30(11):964–971.
|     |     |     |     |     |     | Kwiatkowski, | T., J. Palomaki, | O.  | Redfield, | M. Collins, |
| --- | --- | --- | --- | --- | --- | ------------ | ---------------- | --- | --------- | ----------- |
Gao,T.,H.Yen,J.Yu,andD.Chen.2023. Enablinglarge A.Parikh, C.Alberti, D.Epstein, I.Polosukhin, J.De-
vlin,K.Lee,K.Toutanova,L.Jones,M.Kelcey,M.-W.
languagemodelstogeneratetextwithcitations.EMNLP.
|           |              |     |            |        |             | Chang, | A. M. Dai, J. Uszkoreit, |                          | Q. Le, and | S. Petrov. |
| --------- | ------------ | --- | ---------- | ------ | ----------- | ------ | ------------------------ | ------------------------ | ---------- | ---------- |
| Geva, M., | R. Schuster, |     | J. Berant, | and O. | Levy. 2021. |        |                          |                          |            |            |
|           |              |     |            |        |             | 2019.  | Naturalquestions:        | Abenchmarkforquestionan- |            |            |
Transformerfeed-forwardlayersarekey-valuememories.
sweringresearch.TACL,7:452–466.
EMNLP.
|     |     |     |     |     |     | Lee,K.,M.-W.Chang,andK.Toutanova.2019. |     |     |     | Latentre- |
| --- | --- | --- | --- | --- | --- | -------------------------------------- | --- | --- | --- | --------- |
Green, B. F., A. K. Wolf, C. Chomsky, and K. Laughery. trievalforweaklysupervisedopendomainquestionan-
Pro-
| 1961. | Baseball: | Anautomaticquestionanswerer. |     |     |     | swering.ACL. |     |     |     |     |
| ----- | --------- | ---------------------------- | --- | --- | --- | ------------ | --- | --- | --- | --- |
ceedingsoftheWesternJointComputerConference19.
|                |        |        |         |         |        | Manning,C.D.,P.Raghavan,andH.Schu¨tze.2008. |     |     |     | Intro- |
| -------------- | ------ | ------ | ------- | ------- | ------ | ------------------------------------------- | --- | --- | --- | ------ |
| He, W., K.Liu, | J.Liu, | Y.Lyu, | S.Zhao, | X.Xiao, | Y.Liu, |                                             |     |     |     |        |
ductiontoInformationRetrieval.Cambridge.
Y.Wang,H.Wu,Q.She,X.Liu,T.Wu,andH.Wang.
Meng,K.,D.Bau,A.Andonian,andY.Belinkov.2022.Lo-
| 2018.                                     | DuReader: | a Chinese | machine | reading | compre-  |                                           |                |          |             |          |
| ----------------------------------------- | --------- | --------- | ------- | ------- | -------- | ----------------------------------------- | -------------- | -------- | ----------- | -------- |
|                                           |           |           |         |         |          | catingandeditingfactualassociationsinGPT. |                |          |             | NeurIPS, |
| hensiondatasetfromreal-worldapplications. |           |           |         |         | Workshop |                                           |                |          |             |          |
| onMachineReadingforQuestionAnswering.     |           |           |         |         |          | volume36.                                 |                |          |             |          |
|                                           |           |           |         |         |          | Ng, H. T.,                                | L. H. Teo, and | J. L. P. | Kwan. 2000. | A ma-    |
Hermann,K.M.,T.Kocisky,E.Grefenstette,L.Espeholt,
chinelearningapproachtoansweringquestionsforread-
| W.Kay,M.Suleyman,andP.Blunsom.2015. |     |     |     |     | Teaching |     |     |     |     |     |
| ----------------------------------- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- |
ingcomprehensiontests.EMNLP.
machinestoreadandcomprehend.NeurIPS.
Hirschman,L.,M.Light,E.Breck,andJ.D.Burger.1999. Petroni,F.,T.Rockta¨schel,S.Riedel,P.Lewis,A.Bakhtin,
|     |     |     |     |     |     | Y.Wu,andA.Miller.2019. |     | Languagemodelsasknowl- |     |     |
| --- | --- | --- | --- | --- | --- | ---------------------- | --- | ---------------------- | --- | --- |
DeepRead:Areadingcomprehensionsystem.ACL.
|                     |             |                               |         |                   |     | edgebases? | EMNLP.               |     |                  |     |
| ------------------- | ----------- | ----------------------------- | ------- | ----------------- | --- | ---------- | -------------------- | --- | ---------------- | --- |
| Iyer, S.,           | I. Konstas, | A.                            | Cheung, | J. Krishnamurthy, | and |            |                      |     |                  |     |
|                     |             |                               |         |                   |     | Radford,   | A., J. Wu, R. Child, | D.  | Luan, D. Amodei, | and |
| L.Zettlemoyer.2017. |             | Learninganeuralsemanticparser |         |                   |     |            |                      |     |                  |     |
fromuserfeedback.ACL. I.Sutskever.2019. Languagemodelsareunsupervised
multitasklearners.OpenAItechreport.
| Izacard, G., | P. Lewis, | M.          | Lomeli, | L. Hosseini, | F. Petroni,    |             |                |          |         |            |
| ------------ | --------- | ----------- | ------- | ------------ | -------------- | ----------- | -------------- | -------- | ------- | ---------- |
|              |           |             |         |              |                | Raffel, C., | N. Shazeer, A. | Roberts, | K. Lee, | S. Narang, |
| T. Schick,   | J.        | Dwivedi-Yu, | A.      | Joulin,      | S. Riedel, and |             |                |          |         |            |
M.Matena,Y.Zhou,W.Li,andP.J.Liu.2020.Exploring
| E. Grave. | 2022. | Few-shot | learning | with | retrieval aug- |     |     |     |     |     |
| --------- | ----- | -------- | -------- | ---- | -------------- | --- | --- | --- | --- | --- |
thelimitsoftransferlearningwithaunifiedtext-to-text
mentedlanguagemodels.ArXivpreprint.
transformer.JMLR,21(140):1–67.
| Jia,R.andP.Liang.2016. |     |     | Datarecombinationforneural |     |     |                                     |     |     |             |     |
| ---------------------- | --- | --- | -------------------------- | --- | --- | ----------------------------------- | --- | --- | ----------- | --- |
|                        |     |     |                            |     |     | Rajpurkar,P.,R.Jia,andP.Liang.2018. |     |     | Knowwhatyou |     |
semanticparsing.ACL.
don’tknow:UnanswerablequestionsforSQuAD.ACL.
Jiang,C.,B.Qi,X.Hong,D.Fu,Y.Cheng,F.Meng,M.Yu,
|                        |     |     |                        |     |     | Rajpurkar, | P., J. Zhang, K. | Lopyrev, | and P. Liang. | 2016. |
| ---------------------- | --- | --- | ---------------------- | --- | --- | ---------- | ---------------- | -------- | ------------- | ----- |
| B.Zhou,andJ.Zhou.2024. |     |     | Onlargelanguagemodels’ |     |     |            |                  |          |               |       |
SQuAD:100,000+questionsformachinecomprehension
hallucinationwithregardtoknownfacts.NAACLHLT.
oftext.EMNLP.

Exercises 25
Ram,O.,Y.Levine,I.Dalmedigos,D.Muhlgay,A.Shashua,
K. Leyton-Brown, and Y. Shoham. 2023. In-context
retrieval-augmentedlanguagemodels.ArXivpreprint.
Riloff, E. and M. Thelen. 2000. A rule-based ques-
tionansweringsystemforreadingcomprehensiontests.
ANLP/NAACLworkshoponreadingcomprehensiontests.
Roberts, A., C.Raffel, andN.Shazeer.2020. Howmuch
knowledge can you pack into the parameters of a lan-
guagemodel? EMNLP.
Robertson, S., S. Walker, S. Jones, M. M. Hancock-
Beaulieu, and M. Gatford. 1995. Okapi at TREC-3.
OverviewoftheThirdTextREtrievalConference(TREC-
3).
Rogers,A.,M.Gardner,andI.Augenstein.2023.QAdataset
explosion: A taxonomy of NLP resources for question
answeringandreadingcomprehension.ACMComputing
Surveys,55(10):1–45.
Sachan, D. S., M. Lewis, D. Yogatama, L. Zettlemoyer,
J.Pineau, andM.Zaheer.2023. Questionsareallyou
needtotrainadensepassageretriever. TACL,11:600–
616.
Salton,G.1971.TheSMARTRetrievalSystem:Experiments
inAutomaticDocumentProcessing.PrenticeHall.
Seo,M.,A.Kembhavi,A.Farhadi,andH.Hajishirzi.2017.
Bidirectionalattentionflowformachinecomprehension.
ICLR.
Shi,W.,S.Min,M.Yasunaga,M.Seo,R.James,M.Lewis,
L.Zettlemoyer,andW.-t.Yih.2023.REPLUG:Retrieval-
augmentedblack-boxlanguagemodels.ArXivpreprint.
Simmons,R.F.1965.AnsweringEnglishquestionsbycom-
puter:Asurvey.CACM,8(1):53–70.
Simmons, R.F., S.Klein, andK.McConlogue.1964. In-
dexinganddependencylogicforansweringEnglishques-
tions.AmericanDocumentation,15(3):196–204.
SparckJones,K.1972. Astatisticalinterpretationofterm
specificityanditsapplicationinretrieval.JournalofDoc-
umentation,28(1):11–21.
Voorhees,E.M.andD.K.Harman.2005. TREC:Experi-
mentandEvaluationinInformationRetrieval.MITPress.
Woods,W.A.1978.Semanticsandquantificationinnatural
languagequestionanswering.InM.Yovits,ed.,Advances
inComputers,2–64.Academic.
Woods,W.A.,R.M.Kaplan,andB.L.Nash-Webber.1972.
Thelunarsciencesnaturallanguageinformationsystem:
Finalreport.TechnicalReport2378,BBN.
Zelle, J. M. and R. J. Mooney. 1996. Learning to parse
database queries using inductive logic programming.
AAAI.
Zettlemoyer, L. and M. Collins. 2005. Learning to map
sentencestologicalform: Structuredclassificationwith
probabilisticcategorialgrammars. UncertaintyinArtifi-
cialIntelligence,UAI’05.
Zettlemoyer, L. and M. Collins. 2007. Online learning
of relaxed CCG grammars for parsing to logical form.
EMNLP/CoNLL.
Zhou, K., J.Hwang, X.Ren, andM.Sap.2024. Relying
ontheunreliable:Theimpactoflanguagemodels’reluc-
tancetoexpressuncertainty.ACL.
