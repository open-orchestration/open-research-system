Speech and Language Processing. Daniel Jurafsky & James H. Martin. Copyright © 2026. All
| rights reserved. | Draft | of January | 6,  | 2026. |     |     |     |     |     |     |
| ---------------- | ----- | ---------- | --- | ----- | --- | --- | --- | --- | --- | --- |
CHAPTER
| 5   | Embeddings |     |     |     |     |     |     |     |     |     |
| --- | ---------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
荃者所以在鱼，得鱼而忘荃
Netsareforfish;
Onceyougetthefish,youcanforgetthenet.
|     | 言者所以在意，得意而忘言 |     |     |     | Wordsareformeaning; |     |     |     |     |     |
| --- | ------------ | --- | --- | --- | ------------------- | --- | --- | --- | --- | --- |
Onceyougetthemeaning,youcanforgetthewords
庄子(Zhuangzi),Chapter26
|     | TheasphaltthatLosAngelesisfamousforoccursmainlyonitsfreeways. |     |          |            |       |             |     |         |           | But      |
| --- | ------------------------------------------------------------- | --- | -------- | ---------- | ----- | ----------- | --- | ------- | --------- | -------- |
|     | in the middle                                                 | of  | the city | is another | patch | of asphalt, | the | La Brea | tar pits, | and this |
asphaltpreservesmillionsoffossilbonesfromthelastoftheIceAgesofthePleis-
|     | toceneEpoch. |     | OneofthesefossilsistheSmilodon,orsaber-toothedtiger,instantly |     |     |     |     |     |     |     |
| --- | ------------ | --- | ------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
recognizablebyitslongcanines.Fivemillionyearsagoorso,acompletelydifferent
|     | saber-tooth                  | tiger     | called   | Thylacosmilus |            | lived |     |     |     |     |
| --- | ---------------------------- | --------- | -------- | ------------- | ---------- | ----- | --- | --- | --- | --- |
|     | in Argentina                 | and       | other    | parts of      | South      | Amer- |     |     |     |     |
|     | ica. Thylacosmilus           |           | was      | a marsupial   | whereas    |       |     |     |     |     |
|     | Smilodonwasaplacentalmammal, |           |          |               | butThy-    |       |     |     |     |     |
|     | lacosmilus                   | had       | the same | long upper    | canines    |       |     |     |     |     |
|     | and, like                    | Smilodon, | had      | a protective  |            | bone  |     |     |     |     |
|     | flange on                    | the lower | jaw.     | The           | similarity | of    |     |     |     |     |
thesetwomammalsisoneofmanyexamples
|     | of parallel | or convergent |     | evolution, | in  | which particular |     | contexts | or environments |     |
| --- | ----------- | ------------- | --- | ---------- | --- | ---------------- | --- | -------- | --------------- | --- |
leadtotheevolutionofverysimilarstructuresindifferentspecies(Gould,1980).
|     | The          | role of                                                        | context | is also important |            | in the     | similarity | of a less | biological | kind    |
| --- | ------------ | -------------------------------------------------------------- | ------- | ----------------- | ---------- | ---------- | ---------- | --------- | ---------- | ------- |
|     | of organism: | the                                                            | word.   | Words             | that occur | in similar | contexts   | tend      | to have    | similar |
|     | meanings.    | Thislinkbetweensimilarityinhowwordsaredistributedandsimilarity |         |                   |            |            |            |           |            |         |
distributional in what they mean is called the distributional hypothesis. The hypothesis was
hypothesis
firstformulatedinthe1950sbylinguistslikeJoos(1950),Harris(1954),andFirth
|     | (1957), who | noticed | that   | words            | which | are synonyms | (like      | oculist  | and eye-doctor) |     |
| --- | ----------- | ------- | ------ | ---------------- | ----- | ------------ | ---------- | -------- | --------------- | --- |
|     | tended to   | occur   | in the | same environment |       | (e.g.,       | near words | like eye | or examined)    |     |
withtheamountofmeaningdifferencebetweentwowords“correspondingroughly
|     | totheamountofdifferenceintheirenvironments”(Harris,1954,p. |     |     |     |     |     |     |     | 157). |     |
| --- | ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ----- | --- |
Inthischapterweintroduceembeddings,vectorrepresentationsofthemeaning
embeddings
|     | ofwordsthatarelearneddirectlyfromworddistributionsintexts. |     |     |     |     |     |     |     | Embeddingslie |     |
| --- | ---------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | ------------- | --- |
|     | attheheartoflargelanguagemodelsandothermodernapplications. |     |     |     |     |     |     |     | Thestaticem-  |     |
beddingsweintroducehereunderliethemorepowerfuldynamicorcontextualized
embeddingslikeBERTthatwewillseeinChapter9andChapter8.
Thelinguisticfieldthatstudiesembeddingsandtheirmeaningsiscalledvector
vector semantics. Embeddings are also the first example in this book of representation
semantics
representation learning, automatically learning useful representations of the input text. Finding
learning
|     | such self-supervised |     | ways | to learn | representations |              | of language, |              | instead   | of creat- |
| --- | -------------------- | --- | ---- | -------- | --------------- | ------------ | ------------ | ------------ | --------- | --------- |
|     | ing representations  |     | by   | hand via | feature         | engineering, | is           | an important | principle | of        |
modernNLP(Bengioetal.,2013).

2 CHAPTER5 • EMBEDDINGS
5.1 Lexical Semantics
Let’s begin by introducing some basic principles of word meaning. How should
we represent the meaning of a word? In the n-gram models of Chapter 3, and in
classicalNLPapplications,ouronlyrepresentationofawordisasastringofletters,
or an index in a vocabulary list. This representation is not that different from a
traditioninphilosophy,perhapsyou’veseenitinintroductorylogicclasses,inwhich
the meaning of words is represented by just spelling the word with small capital
letters;representingthemeaningof“dog”asDOG,and“cat”asCAT,orbyusingan
apostrophe(DOG’).
Representingthemeaningofawordbycapitalizingitisaprettyunsatisfactory
model.YoumighthaveseenaversionofajokedueoriginallytosemanticistBarbara
Partee(Carlson,1977):
Q:What’sthemeaningoflife?
A:LIFE’
Surelywecandobetterthanthis!Afterall,we’llwantamodelofwordmeaning
todoallsortsofthingsforus. Itshouldtellusthatsomewordshavesimilarmean-
ings(catissimilartodog),othersareantonyms(coldistheoppositeofhot),some
havepositiveconnotations(happy)whileothershavenegativeconnotations(sad). It
shouldrepresentthefactthatthemeaningsofbuy,sell,andpayofferdifferingper-
spectivesonthesameunderlyingpurchasingevent. (IfIbuysomethingfromyou,
you’ve probably sold it to me, and I likely paid you.) More generally, a model of
wordmeaningshouldallowustodrawinferencestoaddressmeaning-relatedtasks
likequestion-answeringordialogue.
Inthissectionwesummarizesomeofthesedesiderata,drawingonresultsinthe
lexical linguisticstudyofwordmeaning,whichiscalledlexicalsemantics;we’llreturnto
semantics
andexpandonthislistinAppendixGandChapter21.
LemmasandSenses Let’sstartbylookingathowoneword(we’llchoosemouse)
mightbedefinedinadictionary(simplifiedfromtheonlinedictionaryWordNet):
mouse (N)
1. any of numerous small rodents...
2. a hand-operated device that controls a cursor...
lemma Here the form mouse is the lemma, also called the citation form. The form
citationform mousewouldalsobethelemmaforthewordmice;dictionariesdon’thaveseparate
definitionsforinflectedformslikemice. Similarlysingisthelemmaforsing,sang,
sung. In many languages the infinitive form is used as the lemma for the verb, so
Spanishdormir“tosleep”isthelemmaforduermes“yousleep”.Thespecificforms
wordform sungorcarpetsorsingorduermesarecalledwordforms.
As the example above shows, each lemma can have multiple meanings; the
lemma mouse can refer to the rodent or the cursor control device. We call each
oftheseaspectsofthemeaningofmouseawordsense. Thefactthatlemmascan
be polysemous (have multiple senses) can make interpretation difficult (is some-
onewhosearchesfor“mouseinfo”lookingforapetorawidget?). Chapter9and
Appendix G will discuss the problem of polysemy, and introduce word sense dis-
ambiguation, the task of determining which sense of a word is being used in a
particularcontext.
Synonymy One important component of word meaning is the relationship be-
tween word senses. For example when one word has a sense whose meaning is

5.1 • LEXICALSEMANTICS 3
identical to a sense of another word, or nearly identical, we say the two senses of
synonym thosetwowordsaresynonyms. Synonymsincludesuchpairsas
couch/sofa vomit/throwup filbert/hazelnut car/automobile
Amoreformaldefinitionofsynonymy(betweenwordsratherthansenses)isthat
twowordsaresynonymousiftheyaresubstitutableforoneanotherinanysentence
without changing the truth conditions of the sentence, the situations in which the
sentencewouldbetrue.
While substitutions between some pairs of words like car / automobile or wa-
ter/H Oaretruthpreserving,thewordsarestillnotidenticalinmeaning. Indeed,
2
probablynotwowordsareabsolutelyidenticalinmeaning. Oneofthefundamental
principleof tenetsofsemantics,calledtheprincipleofcontrast(Girard1718,Bre´al1897,Clark
contrast
1987),statesthatadifferenceinlinguisticformisalwaysassociatedwithsomedif-
ference in meaning. For example, the word H O is used in scientific contexts and
2
wouldbeinappropriateinahikingguide—waterwouldbemoreappropriate—and
thisgenredifferenceispartofthemeaningoftheword. Inpractice,thewordsyn-
onymisthereforeusedtodescribearelationshipofapproximateorroughsynonymy.
Word Similarity While words don’t have many synonyms, most words do have
lotsofsimilarwords. Catisnotasynonymofdog,butcatsanddogsarecertainly
similarwords.Inmovingfromsynonymytosimilarity,itwillbeusefultoshiftfrom
talking about relations between word senses (like synonymy) to relations between
words(likesimilarity). Dealingwithwordsavoidshavingtocommittoaparticular
representationofwordsenses,whichwillturnouttosimplifyourtask.
similarity Thenotionofwordsimilarityisveryusefulinlargersemantictasks. Knowing
howsimilartwowordsarecanhelpincomputinghowsimilarthemeaningoftwo
phrasesorsentencesare,averyimportantcomponentoftaskslikequestionanswer-
ing,paraphrasing,andsummarization.Onewayofgettingvaluesforwordsimilarity
istoaskhumanstojudgehowsimilaronewordistoanother. Anumberofdatasets
have resulted from such experiments. For example the SimLex-999 dataset (Hill
et al., 2015) gives values on a scale from 0 to 10, like the examples below, which
range from near-synonyms (vanish, disappear) to pairs that scarcely seem to have
anythingincommon(hole,agreement):
vanish disappear 9.8
belief impression 5.95
muscle bone 3.65
modest flexible 0.98
hole agreement 0.3
WordRelatedness Themeaningoftwowordscanberelatedinwaysotherthan
relatedness similarity. One such class of connections is called word relatedness (Budanitsky
association andHirst,2006),alsotraditionallycalledwordassociationinpsychology.
Considerthemeaningsofthewordscoffeeandcup. Coffeeisnotsimilartocup;
they share practically no features (coffee is a plant or a beverage, while a cup is a
manufacturedobjectwithaparticularshape). Butcoffeeandcupareclearlyrelated;
they are associated by co-participating in an everyday event (the event of drinking
coffee out of a cup). Similarly scalpel and surgeon are not similar but are related
eventively(asurgeontendstomakeuseofascalpel).
One common kind of relatedness between words is if they belong to the same
semanticfield semanticfield. Asemanticfieldisasetofwordswhichcoveraparticularsemantic
domainandbearstructuredrelationswitheachother. Forexample,wordsmightbe

| 4 CHAPTER5 | • EMBEDDINGS |          |        |          |       |              |           |          |        |       |
| ---------- | ------------ | -------- | ------ | -------- | ----- | ------------ | --------- | -------- | ------ | ----- |
|            | related      | by being | in the | semantic | field | of hospitals | (surgeon, | scalpel, | nurse, | anes- |
thetic,hospital),restaurants(waiter,menu,plate,food,chef),orhouses(door,roof,
topicmodels kitchen,family,bed). Semanticfieldsarealsorelatedtotopicmodels,likeLatent
DirichletAllocation,LDA,whichapplyunsupervisedlearningonlargesetsoftexts
|     | toinducesetsofassociatedwordsfromtext. |     |     |     |     |     | Semanticfieldsandtopicmodelsare |     |     |     |
| --- | -------------------------------------- | --- | --- | --- | --- | --- | ------------------------------- | --- | --- | --- |
veryusefultoolsfordiscoveringtopicalstructureindocuments.
InAppendixGwe’llintroducemorerelationsbetweensenseslikehypernymy
orIS-A,antonymy(opposites)andmeronymy(part-wholerelations).
connotations Connotation Finally,wordshaveaffectivemeaningsorconnotations. Theword
connotationhasdifferentmeaningsindifferentfields,buthereweuseittomeanthe
aspectsofaword’smeaningthatarerelatedtoawriterorreader’semotions,senti-
|     | ment,opinions,orevaluations. |       |        |      | Forexamplesomewordshavepositiveconnotations |              |           |      |       |       |
| --- | ---------------------------- | ----- | ------ | ---- | ------------------------------------------- | ------------ | --------- | ---- | ----- | ----- |
|     | (wonderful)                  | while | others | have | negative                                    | connotations | (dreary). | Even | words | whose |
meaningsaresimilarinotherwayscanvaryinconnotation;considerthedifference
inconnotationsbetweenfake,knockoff,forgery,ontheonehand,andcopy,replica,
|     | reproduction     | on  | the                                                          | other, | or innocent | (positive | connotation)        | and | naive    | (negative |
| --- | ---------------- | --- | ------------------------------------------------------------ | ------ | ----------- | --------- | ------------------- | --- | -------- | --------- |
|     | connotation).    |     | Somewordsdescribepositiveevaluation(great,love)andothersneg- |        |             |           |                     |     |          |           |
|     | ative evaluation |     | (terrible,                                                   | hate). | Positive    | or        | negative evaluation |     | language | is called |
sentiment sentiment, as we saw in Appendix K, and word sentiment plays a role in impor-
|     | tant tasks | like | sentiment | analysis, | stance | detection, | and | applications | of  | NLP to the |
| --- | ---------- | ---- | --------- | --------- | ------ | ---------- | --- | ------------ | --- | ---------- |
languageofpoliticsandconsumerreviews.
Earlyworkonaffectivemeaning(Osgoodetal.,1957)foundthatwordsvaried
alongthreeimportantdimensionsofaffectivemeaning:
|     | valence:              | thepleasantnessofthestimulus               |                                        |                                                 |              |          |             |       |         |        |
| --- | --------------------- | ------------------------------------------ | -------------------------------------- | ----------------------------------------------- | ------------ | -------- | ----------- | ----- | ------- | ------ |
|     | arousal:              | theintensityofemotionprovokedbythestimulus |                                        |                                                 |              |          |             |       |         |        |
|     | dominance:            |                                            | thedegreeofcontrolexertedbythestimulus |                                                 |              |          |             |       |         |        |
|     | Thus                  | words                                      | like                                   | happy                                           | or satisfied | are high | on valence, | while | unhappy | or an- |
|     | noyedarelowonvalence. |                                            |                                        | Excitedishighonarousal,whilecalmislowonarousal. |              |          |             |       |         |        |
Controllingishighondominance,whileawedorinfluencedarelowondominance.
Eachwordisthusrepresentedbythreenumbers,correspondingtoitsvalueoneach
ofthethreedimensions:
|     |                         |        |            |                                                 | Valence | Arousal          | Dominance      |         |              |             |
| --- | ----------------------- | ------ | ---------- | ----------------------------------------------- | ------- | ---------------- | -------------- | ------- | ------------ | ----------- |
|     |                         |        | courageous |                                                 | 8.0     | 5.5              | 7.4            |         |              |             |
|     |                         |        | music      |                                                 | 7.7     | 5.6              | 6.5            |         |              |             |
|     |                         |        | heartbreak |                                                 | 2.5     | 5.7              | 3.6            |         |              |             |
|     |                         |        | cub        |                                                 | 6.7     | 4.0              | 4.2            |         |              |             |
|     | Osgood                  | et     | al. (1957) | noticed                                         | that    | in using         | these 3        | numbers | to represent | the         |
|     | meaning                 | of a   | word,      | the model                                       | was     | representing     | each word      | as      | a point      | in a three- |
|     | dimensional             | space, | a          | vector                                          | whose   | three dimensions | corresponded   |         | to           | the word’s  |
|     | ratingonthethreescales. |        |            | Thisrevolutionaryideathatwordmeaningcouldberep- |         |                  |                |         |              |             |
|     | resented                | as a   | point in   | space                                           | (e.g.,  | that part        | of the meaning | of      | heartbreak   | can be      |
representedasthepoint[2.5,5.7,3.6])wasthefirstexpressionofthevectorseman-
ticsmodelsthatweintroducenext.
| 5.2 Vector | Semantics: |     |     | The | Intuition |     |     |     |     |     |
| ---------- | ---------- | --- | --- | --- | --------- | --- | --- | --- | --- | --- |
vector
|     | Vector | semantics | is  | the standard | way | to represent | word | meaning | in NLP, | helping |
| --- | ------ | --------- | --- | ------------ | --- | ------------ | ---- | ------- | ------- | ------- |
semantics

|                                                                |           |        | 5.2 • VECTORSEMANTICS: |                   |           |            | THEINTUITION |           | 5    |
| -------------------------------------------------------------- | --------- | ------ | ---------------------- | ----------------- | --------- | ---------- | ------------ | --------- | ---- |
| usmodelmanyoftheaspectsofwordmeaningwesawintheprevioussection. |           |        |                        |                   |           |            |              |           | The  |
| roots of the                                                   | model lie | in the | 1950s when             | two               | big ideas | converged: | Osgood’s     |           | 1957 |
| idea mentioned                                                 | above     | to     | use a point in         | three-dimensional |           | space      | to           | represent | the  |
connotationofaword,andtheproposalbylinguistslikeJoos(1950),Harris(1954),
| and Firth    | (1957) to       | define | the meaning | of a word   | by its        | distribution |       | in language |     |
| ------------ | --------------- | ------ | ----------- | ----------- | ------------- | ------------ | ----- | ----------- | --- |
| use, meaning | its neighboring |        | words or    | grammatical | environments. |              | Their | idea        | was |
thattwowordsthatoccurinverysimilardistributions(whoseneighboringwordsare
similar)havesimilarmeanings.
Forexample,supposeyoudidn’tknowthemeaningofthewordongchoi(are-
centborrowingfromCantonese)butyouseeitinthefollowingcontexts:
(5.1) Ongchoiisdelicioussauteedwithgarlic.
(5.2) Ongchoiissuperboverrice.
(5.3) ...ongchoileaveswithsaltysauces...
Andsupposethatyouhadseenmanyofthesecontextwordsinothercontexts:
(5.4) ...spinachsauteedwithgarlicoverrice...
(5.5) ...chardstemsandleavesaredelicious...
(5.6) ...collardgreensandothersaltyleafygreens
| The fact | that ongchoi |     | occurs with words | like | rice and | garlic | and | delicious | and |
| -------- | ------------ | --- | ----------------- | ---- | -------- | ------ | --- | --------- | --- |
salty,asdowordslikespinach,chard,andcollardgreensmightsuggestthatongchoi
greens.1
| is a leafy | green similar | to  | these other leafy |     | We  | can | implement | the | same |
| ---------- | ------------- | --- | ----------------- | --- | --- | --- | --------- | --- | ---- |
intuitioncomputationallybyjustcountingwordsinthecontextofongchoi.
| Figure5.1             | A two-dimensional |                                                           | (t-SNE) visualization |        | of 200-dimensional |       |      | word2vec | em-   |
| --------------------- | ----------------- | --------------------------------------------------------- | --------------------- | ------ | ------------------ | ----- | ---- | -------- | ----- |
| beddings for          | some words        | close                                                     | to the word           | sweet, | showing that       | words | with | similar  | mean- |
| ingsarenearbyinspace. |                   | VisualizationcreatedusingtheTensorBoardEmbeddingProjector |                       |        |                    |       |      |          |       |
https://projector.tensorflow.org/.
Theideaofvectorsemanticsistorepresentawordasapointinamultidimen-
| sional semantic | space | that | is derived (in | different | ways | we’ll | see) from | the | distri- |
| --------------- | ----- | ---- | -------------- | --------- | ---- | ----- | --------- | --- | ------- |
embeddings butionsofwordneighbors. Vectorsforrepresentingwordsarecalledembeddings.
| The word                              | “embedding” | derives | historically | from                          | its mathematical |     | sense | as a | map- |
| ------------------------------------- | ----------- | ------- | ------------ | ----------------------------- | ---------------- | --- | ----- | ---- | ---- |
| pingfromonespaceorstructuretoanother, |             |         |              | althoughthemeaninghasshifted; |                  |     |       |      | see  |
theendofthechapter.
Fig.5.1showsavisualizationofembeddingslearnedbytheword2vecalgorithm,
showingthelocationofselectedwords(neighborsof“sweet”)projecteddownfrom
1 It’sinfactIpomoeaaquatica,arelativeofmorningglorysometimescalledwaterspinachinEnglish.

6 CHAPTER5 • EMBEDDINGS
200-dimensionalspaceintoa2-dimensionalspace. Notethatthenearestneighbors
of sweet are semantically related words like honey, candy, juice, chocolate. This
idea that similar words are neighbors in high-dimensional space offers enormous
powertolanguagemodelsandotherNLPapplications. Forexamplethesentiment
classifiersofChapter4dependonthesamewordsappearinginthetrainingandtest
sets. But by representing words as embeddings, a classifier can assign sentiment
as long as it sees some words with similar meanings. And as we’ll see, vector
semanticmodelsliketheonesshowedinFig.5.1canbelearnedautomaticallyfrom
textwithoutsupervision.
In this chapter we’ll begin with a simple pedagogical model of embeddings in
whichthemeaningofawordisdefinedbyavectorwiththecountsofnearbywords.
Weintroducethismodelasahelpfulwaytounderstandtheconceptofvectorsand
whatitmeansforavectortobearepresentationofwordmeaning,butmoresophis-
ticatedvariantslikethetf-idfmodelwewillintroduceinChapter11areimportant
methods you should understand. We will see that this method results in very long
vectorsthataresparse,i.e.mostlyzeros(sincemostwordssimplyneveroccurinthe
contextofothers).We’llthenintroducetheword2vecmodelfamilyforconstructing
short,densevectorsthathaveevenmoreusefulsemanticproperties.
We’ll also introduce the cosine, the standard way to use embeddings to com-
putesemanticsimilarity,betweentwowords,twosentences,ortwodocuments,an
importanttoolinpracticalapplications.
5.3 Simple count-based embeddings
“Themostimportantattributesofavectorin3-spaceare{Location,Location,Location}”
RandallMunroe,thehoverfromhttps://xkcd.com/2358/
Let’snowintroducethefirstwaytocomputewordvectorembeddings.Thissim-
plestvectormodelofmeaningisbasedontheco-occurrencematrix,awayofrep-
resentinghowoftenwordsco-occur. We’lldefineaparticularkindofco-occurrence
word-context matrix,theword-contextmatrix,inwhicheachrowinthematrixrepresentsaword
matrix
inthevocabularyandeachcolumnrepresentshowofteneachotherwordinthevo-
cabulary appears nearby. This matrix is thus of dimensionality |V|×|V| and each
cell records the number of times the row (target) word and the column (context)
wordco-occurnearbyinsometrainingcorpus.
Whatdowemeanby‘nearby’? Wecouldimplementvariousmethods,butlet’s
startwithaverysimpleone:acontextwindowaroundtheword,let’ssayof4words
to the left and 4 words to the right. If we do that, each cell will represents the
number of times (in some training corpus) the column word occurs in such a ±4
wordwindowaroundtherowword.
Let’sseehowthisworksfor4words: cherry,strawberry,digital,andinforma-
tion. Foreachwordwetookasingleinstancefromacorpus, andweshowthe±4
wordwindowfromthatinstance:
istraditionallyfollowedby cherry pie,atraditionaldessert
oftenmixed,suchas strawberry rhubarbpie. Applepie
computerperipheralsandpersonal digital assistants. Thesedevicesusually
acomputer. Thisincludes information availableontheinternet
If we then take every occurrence of each word in a large corpus and count the
contextwordsaroundit,wegetaword-contextco-occurrencematrix.Thefullword-

5.3 • SIMPLECOUNT-BASEDEMBEDDINGS 7
contextco-occurrencematrixisverylarge,becauseforeachwordinthevocabulary
(since |V|) we have to count how often it occurs with every other word in the vo-
cabulary,hencedimensionality|V|×|V|. Let’sthereforeinsteadsketchtheprocess
onasmallerscale. Imaginethatwearegoingtolookatonlythe4words,andonly
consider the following 3 context words: a, computer, and pie. Furthermore let’s
assumeweonlycountoccurrencesinthemini-corpusabove.
So before looking at Fig. 5.2, compute by hand the counts for these 3 context
wordsforthefourwordscherry,strawberry,digital,andinformation.
a computer pie
cherry 1 0 1
strawberry 0 0 2
digital 0 1 0
information 1 1 0
Figure5.2 Co-occurrencevectorsforfourwordswithcountsfromthe4windowsabove,
showingjust3ofthepotentialcontextworddimensions. Thevectorforcherryisoutlinedin
red.Notethatarealvectorwouldhavevastlymoredimensionsandthusbeevensparser.
HopefullyyourcountmatcheswhatisshowninFig.5.2,sothateachcellrepre-
sentsthenumberoftimesaparticularword(definedbytherow)occursinapartic-
ularcontext(definedbythewordcolumn).
Each row, then, is a vector representing a word. To review some basic linear
vector algebra,avectoris,atheart,justalistorarrayofnumbers. Socherryisrepresented
asthelist[1,0,1](thefirstrowvectorinFig.5.2)andinformation isrepresentedas
thelist[1,1,0](thefourthrowvector).
vectorspace Avectorspaceisacollectionofvectors,andischaracterizedbyitsdimension.
dimension Vectorsina3-dimensionalvectorspacehaveanelementforeachdimensionofthe
space. Wewilllooselyrefertoavectorina3-dimensionalspaceasa3-dimensional
vector, with one element along each dimension. In the example in Fig. 5.2, we’ve
chosentomakethedocumentvectorsofdimension3,justsotheyfitonthepage;in
realterm-documentmatrices,thedocumentvectorswouldhavedimensionality|V|,
thevocabularysize.
Theorderingofthenumbersinavectorspaceindicatesthedifferentdimensions
on which documents vary. The third dimension for all these vectors corresponds
to the number of times pie occurs in the context. The second dimension for all of
them corresponds to the number of times the word computer occurs. Notice that
thevectorsforinformationanddigitalhavethesamevalue(1)forthis“computer”
dimension.
Inreality,wedon’tcomputewordvectorsonasinglecontextwindow. Instead,
wecomputethemoveranentirecorpus. Let’sseewhatsomerealcountslooklike.
Let’s look at some vectors computed in this way. Fig. 5.3 shows a subset of the
word-word co-occurrence matrix for these four words, where, again because it’s
impossibletovisualizeall|V|possiblecontextwordsonthepageofthistextbook,
weshowasubsetof6ofthedimensions,withcountscomputedfromtheWikipedia
corpus(Davies,2015).
Note in Fig. 5.3 that the two words cherry and strawberry are more similar to
eachother(bothpieandsugartendtooccurintheirwindow)thantheyaretoother
wordslikedigital;conversely,digitalandinformationaremoresimilartoeachother
than,say,tostrawberry.
Wecanthinkofthevectorforadocumentasapointin|V|-dimensionalspace;
thusthedocumentsinFig.5.3arepointsin3-dimensionalspace. Fig.5.4showsa
spatialvisualization.

| 8 CHAPTER5 |             | • EMBEDDINGS |                                                                   |     |              |      |      |        |     |       |     |
| ---------- | ----------- | ------------ | ----------------------------------------------------------------- | --- | ------------ | ---- | ---- | ------ | --- | ----- | --- |
|            |             |              | aardvark                                                          |     | ... computer |      | data | result | pie | sugar | ... |
|            |             | cherry       |                                                                   | 0   | ...          | 2    | 8    | 9      | 442 | 25    | ... |
|            | strawberry  |              |                                                                   | 0   | ...          | 0    | 0    | 1      | 60  | 19    | ... |
|            |             | digital      |                                                                   | 0   | ...          | 1670 | 1683 | 85     | 5   | 4     | ... |
|            | information |              |                                                                   | 0   | ...          | 3325 | 3982 | 378    | 5   | 13    | ... |
|            | Figure5.3   |              | Co-occurrencevectorsforfourwordsintheWikipediacorpus,showingsixof |     |              |      |      |        |     |       |     |
Thevectorfordigitalisoutlinedin
thedimensions(hand-pickedforpedagogicalpurposes).
red.Notethatarealvectorwouldhavevastlymoredimensionsandthusbemuchsparser,i.e.
wouldhavezerovaluesinmostdimensions.
4000
|     |     |     |     | retupmoc |      |     | information   |     |     |     |     |
| --- | --- | --- | --- | -------- | ---- | --- | ------------- | --- | --- | --- | --- |
|     |     |     |     |          | 3000 |     |  [3982,3325]  |     |     |     |     |
digital
2000  [1683,1670]
1000
|     |     |     |     |     |     | 1000 2000 | 3000 4000 |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --------- | --------- | --- | --- | --- | --- |
 data
|     | Figure5.4 |     | Aspatialvisualizationofwordvectorsfordigitalandinformation,showingjust |     |     |     |     |     |     |     |     |
| --- | --------- | --- | ---------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
twoofthedimensions,correspondingtothewordsdataandcomputer.
|     |                       | Note that | |V|,    | the dimensionality                                 |     | of the | vector, | is generally | the  | size of  | the vo- |
| --- | --------------------- | --------- | ------- | -------------------------------------------------- | --- | ------ | ------- | ------------ | ---- | -------- | ------- |
|     | cabulary,             | often     | between | 10,000                                             | and | 50,000 | words   | (using the   | most | frequent | words   |
|     | inthetrainingcorpus;  |           |         | keepingwordsafteraboutthemostfrequent50,000orsois  |     |        |         |              |      |          |         |
|     | generallynothelpful). |           |         | Sincemostofthesenumbersarezerothesearesparsevector |     |        |         |              |      |          |         |
representations;thereareefficientalgorithmsforstoringandcomputingwithsparse
matrices.
|     |     | It’s also    | possible | to apply     | various | kinds          | of weighting |               | functions | to the    | counts |
| --- | --- | ------------ | -------- | ------------ | ------- | -------------- | ------------ | ------------- | --------- | --------- | ------ |
|     | in  | these cells. | The      | most popular |         | such weighting | is           | tf-idf, which | we’ll     | introduce | in     |
Chapter11,buttherehavehistoricallybeenawidevarietyofotherweightings.
Nowthatwehavesomeintuitions,let’smoveontoexaminethedetailsofcom-
putingwordsimilarity.
| 5.4 Cosine |     | for     | measuring  |         | similarity |        |       |          |         |          |      |
| ---------- | --- | ------- | ---------- | ------- | ---------- | ------ | ----- | -------- | ------- | -------- | ---- |
|            | To  | measure | similarity | between | two        | target | words | v and w, | we need | a metric | that |
takestwovectors(ofthesamedimensionality,eitherbothwithwordsasdimensions,
henceoflength|V|,orbothwithdocumentsasdimensions,oflength|D|)andgives
ameasureoftheirsimilarity.Byfarthemostcommonsimilaritymetricisthecosine
oftheanglebetweenthevectors.
Thecosine—likemostmeasuresforvectorsimilarityusedinNLP—isbasedon
thedotproductoperatorfromlinearalgebra,alsocalledtheinnerproduct:
dotproduct
innerproduct
N
(cid:88)
|     |     | dotproduct(v,w)=v·w= |     |     |     | v   | w =v w | +v w  | +...+v | w   |       |
| --- | --- | -------------------- | --- | --- | --- | --- | ------ | ----- | ------ | --- | ----- |
|     |     |                      |     |     |     | i   | i 1    | 1 2 2 |        | N N | (5.7) |
i=1
Thedotproductactsasasimilaritymetricbecauseitwilltendtobehighjustwhen
|     | thetwovectorshavelargevaluesinthesamedimensions. |     |     |     |     |     |     | Alternatively,vectorsthat |     |     |     |
| --- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- | --- |

|     |     |     | 5.4 • | COSINEFORMEASURINGSIMILARITY |     |     |     | 9   |
| --- | --- | --- | ----- | ---------------------------- | --- | --- | --- | --- |
havezerosindifferentdimensions—orthogonalvectors—willhaveadotproductof
0,representingtheirstrongdissimilarity.
| This raw     | dot product,               | however, | has | a problem | as a | similarity | metric: | it favors |
| ------------ | -------------------------- | -------- | --- | --------- | ---- | ---------- | ------- | --------- |
| longvectors. | Thevectorlengthisdefinedas |          |     |           |      |            |         |           |
vectorlength
(cid:118)
|     |     |     |     | (cid:117) N |     |     |     |     |
| --- | --- | --- | --- | ----------- | --- | --- | --- | --- |
(cid:117)(cid:88)
|     |     |     | |v| | = (cid:116) | v2  |     |     |       |
| --- | --- | --- | --- | ----------- | --- | --- | --- | ----- |
|     |     |     |     |             | i   |     |     | (5.8) |
i=1
Thedotproductishigherifavectorislonger,withhighervaluesineachdimension.
| More frequent | words | have | longer vectors, | since | they tend | to co-occur | with | more |
| ------------- | ----- | ---- | --------------- | ----- | --------- | ----------- | ---- | ---- |
wordsandhavehigherco-occurrencevalueswitheachofthem.Therawdotproduct
| thuswillbehigherforfrequentwords. |     |     |     | Butthisisaproblem;we’dlikeasimilarity |     |     |     |     |
| --------------------------------- | --- | --- | --- | ------------------------------------- | --- | --- | --- | --- |
metricthattellsushowsimilartwowordsareregardlessoftheirfrequency.
| We modify                                    | the | dot product | to normalize |     | for the vector           | length | by dividing | the |
| -------------------------------------------- | --- | ----------- | ------------ | --- | ------------------------ | ------ | ----------- | --- |
| dotproductbythelengthsofeachofthetwovectors. |     |             |              |     | Thisnormalizeddotproduct |        |             |     |
turnsouttobethesameasthecosineoftheanglebetweenthetwovectors,following
fromthedefinitionofthedotproductbetweentwovectorsaandb:
|     |     |     | a·b | = |a||b|cosθ |     |     |     |     |
| --- | --- | --- | --- | ------------ | --- | --- | --- | --- |
a·b
|     |     |     |     | = cosθ |     |     |     | (5.9) |
| --- | --- | --- | --- | ------ | --- | --- | --- | ----- |
|a||b|
cosine Thecosinesimilaritymetricbetweentwovectorsvandwthuscanbecomputedas:
N
(cid:88)
vw
i i
v·w
|     |     | cosine(v,w)= |        | =                 | i=1               |     |     |        |
| --- | --- | ------------ | ------ | ----------------- | ----------------- | --- | --- | ------ |
|     |     |              |        | (cid:118)         | (cid:118)         |     |     | (5.10) |
|     |     |              | |v||w| | (cid:117)         | N (cid:117)       | N   |     |        |
|     |     |              |        | (cid:117)(cid:88) | (cid:117)(cid:88) |     |     |        |
|     |     |              |        |                   | v2(cid:116)       | w2  |     |        |
(cid:116)
|                               |     |                  |                                      |      | i          | i        |       |             |
| ----------------------------- | --- | ---------------- | ------------------------------------ | ---- | ---------- | -------- | ----- | ----------- |
|                               |     |                  |                                      |      | i=1 i=1    |          |       |             |
| For some applications         |     | we pre-normalize |                                      | each | vector, by | dividing | it by | its length, |
| creatingaunitvectoroflength1. |     |                  | Thuswecouldcomputeaunitvectorfromaby |      |            |          |       |             |
unitvector
| dividingitby|a|. | Forunitvectors,thedotproductisthesameasthecosine. |     |     |     |     |     |     |     |
| ---------------- | ------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
Thecosinevaluerangesfrom1forvectorspointinginthesamedirection,through
| 0fororthogonalvectors,to-1forvectorspointinginoppositedirections. |     |     |     |     |     |     |     | Butsince |
| ----------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | -------- |
rawfrequencyvaluesarenon-negative,thecosineforthesevectorsrangesfrom0–1.
Let’sseehowthecosinecomputeswhichofthewordscherryordigitaliscloser
inmeaningtoinformation,justusingrawcountsfromthefollowingshortenedtable:
|     |     |             |         | pie data | computer |     |     |     |
| --- | --- | ----------- | ------- | -------- | -------- | --- | --- | --- |
|     |     |             | cherry  | 442 8    | 2        |     |     |     |
|     |     |             | digital | 5 1683   | 1670     |     |     |     |
|     |     | information |         | 5 3982   | 3325     |     |     |     |
442∗5+8∗3982+2∗3325
| cos(cherry,information) |     | =   | √          |     | √              |     | =.018 |     |
| ----------------------- | --- | --- | ---------- | --- | -------------- | --- | ----- | --- |
|                         |     |     | 4422+82+22 |     | 52+39822+33252 |     |       |     |
5∗5+1683∗3982+1670∗3325
| cos(digital,information) |     | =   | √              |     | √              |     |     | =.996 |
| ------------------------ | --- | --- | -------------- | --- | -------------- | --- | --- | ----- |
|                          |     |     | 52+16832+16702 |     | 52+39822+33252 |     |     |       |
Themodeldecidesthatinformationiswayclosertodigitalthanitistocherry,a
| resultthatseemssensible. |     | Fig.5.5showsavisualization. |     |     |     |     |     |     |
| ------------------------ | --- | --------------------------- | --- | --- | --- | --- | --- | --- |

10 CHAPTER5 • EMBEDDINGS
’eip‘ :1 noisnemiD
500
cherry
|     |     |     |      | digital |      |      | information |     |     |
| --- | --- | --- | ---- | ------- | ---- | ---- | ----------- | --- | --- |
|     |     | 500 | 1000 | 1500    | 2000 | 2500 | 3000        |     |     |
Dimension 2: ‘computer’
| Figure5.5 | A (rough) | graphical | demonstration |     | of cosine | similarity, | showing | vectors | for |
| --------- | --------- | --------- | ------------- | --- | --------- | ----------- | ------- | ------- | --- |
threewords(cherry,digital,andinformation)inthetwodimensionalspacedefinedbycounts
ofthewordscomputerandpienearby.Thefiguredoesn’tshowthecosine,butithighlightsthe
angles;notethattheanglebetweendigitalandinformationissmallerthantheanglebetween
cherryandinformation.Whentwovectorsaremoresimilar,thecosineislargerbuttheangle
| issmaller; | thecosinehasitsmaximum(1)whentheanglebetweentwovectorsissmallest |     |     |     |     |     |     |     |     |
| ---------- | ---------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
(0◦);thecosineofallotheranglesislessthan1.
Cosinesimilaritycanbeusedtoestimatewordsimilarity,fortaskslikefinding
wordparaphrases,trackingchangesinwordmeaning,orautomaticallydiscovering
meaningsofwordsindifferentcorpora.Forexample,wecanfinethe10mostsimilar
| words to | any target word | w by | computing |     | the cosines | between | w   | and each | of the |
| -------- | --------------- | ---- | --------- | --- | ----------- | ------- | --- | -------- | ------ |
|V|−1otherwords,sorting,andlookingatthetop10.
5.5 Word2vec
Intheprevioussectionswesawhowtorepresentawordasasparse,longvectorwith
| dimensions                  | corresponding | to  | words                         | in the | vocabulary. | We  | now introduce    |     | a more |
| --------------------------- | ------------- | --- | ----------------------------- | ------ | ----------- | --- | ---------------- | --- | ------ |
| powerfulwordrepresentation: |               |     | embeddings,shortdensevectors. |        |             |     | Unlikethevectors |     |        |
we’veseensofar,embeddingsareshort,withnumberofdimensionsdrangingfrom
| 50-1000,ratherthanthemuchlargervocabularysize|V|.Thesed |                 |        |     |           |            |     | dimensionsdon’t |        |          |
| ------------------------------------------------------- | --------------- | ------ | --- | --------- | ---------- | --- | --------------- | ------ | -------- |
| have a clear                                            | interpretation. | And    | the | vectors   | are dense: |     | instead of      | vector | entries  |
| being sparse,                                           | mostly-zero     | counts | or  | functions | of counts, |     | the values      | will   | be real- |
valuednumbersthatcanbenegative.
ItturnsoutthatdensevectorsworkbetterineveryNLPtaskthansparsevectors.
Whilewedon’tcompletelyunderstandallthereasonsforthis,wehavesomeintu-
itions.Representingwordsas300-dimensionaldensevectorsrequiresourclassifiers
tolearnfarfewerweightsthanifwerepresentedwordsas50,000-dimensionalvec-
tors,andthesmallerparameterspacepossiblyhelpswithgeneralizationandavoid-
| ing overfitting. | Dense          | vectors | may             | also do   | a better   | job           | of capturing | synonymy. |           |
| ---------------- | -------------- | ------- | --------------- | --------- | ---------- | ------------- | ------------ | --------- | --------- |
| For example,     | in a sparse    | vector  | representation, |           | dimensions |               | for synonyms |           | like car  |
| and automobile   | dimension      | are     | distinct        | and       | unrelated; | sparse        | vectors      | may       | thus fail |
| to capture       | the similarity | between | a               | word with | car        | as a neighbor | and          | a word    | with      |
automobileasaneighbor.
skip-gram Inthissectionweintroduceonemethodforcomputingembeddings: skip-gram
withnegativesampling,sometimescalledSGNS.Theskip-gramalgorithmisone
SGNS
word2vec of two algorithms in a software package called word2vec, and so sometimes the
| algorithm | is loosely referred        |     | to as word2vec |                   | (Mikolov | et         | al. 2013a,            | Mikolov    | et al. |
| --------- | -------------------------- | --- | -------------- | ----------------- | -------- | ---------- | --------------------- | ---------- | ------ |
| 2013b).   | Theword2vecmethodsarefast, |     |                | efficienttotrain, |          |            | andeasilyavailableon- |            |        |
| line with | code and pretrained        |     | embeddings.    |                   | Word2vec | embeddings |                       | are static | em-    |

5.5 • WORD2VEC 11
static beddings,meaningthatthemethodlearnsonefixedembeddingforeachwordinthe
embeddings
vocabulary. InChapter9we’llintroducemethodsforlearningdynamiccontextual
embeddingslikethepopularfamilyofBERTrepresentations,inwhichthevector
foreachwordisdifferentindifferentcontexts.
The intuition of word2vec is that instead of counting how often each context
wordcoccursnear,say,apricot,we’llinsteadtrainaclassifieronabinaryprediction
task: “Is word c likely to show up near apricot?” We don’t actually care about
this prediction task; instead we’ll take the learned classifier weights as the word
embeddings.
Therevolutionaryintuitionhereisthatwecanjustuserunningtextasimplicitly
supervised training data for such a classifier; a word c that occurs near the target
wordapricotactsasgold‘correctanswer’tothequestion“Iswordclikelytoshow
self-supervision up near apricot?” This method, often called self-supervision, avoids the need for
anysortofhand-labeledsupervisionsignal. Thisideawasfirstproposedinthetask
ofneurallanguagemodeling,whenBengioetal.(2003)andCollobertetal.(2011)
showed that a neural language model (a neural network that learned to predict the
next word from prior words) could just use the next word in running text as its
supervisionsignal,andcouldbeusedtolearnanembeddingrepresentationforeach
wordaspartofdoingthispredictiontask.
We’ll see how to do neural networks in the next chapter, but word2vec is a
much simpler model than the neural network language model, in two ways. First,
word2vec simplifies the task (making it binary classification instead of word pre-
diction). Second,word2vecsimplifiesthearchitecture(trainingalogisticregression
classifier instead of a multi-layer neural network with hidden layers that demand
moresophisticatedtrainingalgorithms). Theintuitionofskip-gramis:
1. Treatthetargetwordandaneighboringcontextwordaspositiveexamples.
2. Randomlysampleotherwordsinthelexicontogetnegativesamples.
3. Uselogisticregressiontotrainaclassifiertodistinguishthosetwocases.
4. Usethelearnedweightsastheembeddings.
5.5.1 Theclassifier
Let’s start by thinking about the classification task, and then turn to how to train.
Imagineasentencelikethefollowing,withatargetwordapricot,andassumewe’re
usingawindowof±2contextwords:
... lemon, a [tablespoon of apricot jam, a] pinch ...
c1 c2 w c3 c4
Our goal is to train a classifier such that, given a tuple (w,c) of a target word
w paired with a candidate context word c (for example (apricot, jam), or perhaps
(apricot, aardvark))itwillreturntheprobabilitythatcisarealcontextword(true
forjam,falseforaardvark):
P(+|w,c) (5.11)
The probability that word c is not a real context word for w is just 1 minus
Eq.5.11:
P(−|w,c)=1−P(+|w,c) (5.12)
How does the classifier compute the probability P? The intuition of the skip-
grammodelistobasethisprobabilityonembeddingsimilarity: awordislikelyto

12 CHAPTER5 • EMBEDDINGS
| occurnearthetargetifitsembeddingvectorissimilartothetargetembedding. |            |         |                                                   |             |             |         |             |               | To        |
| -------------------------------------------------------------------- | ---------- | ------- | ------------------------------------------------- | ----------- | ----------- | ------- | ----------- | ------------- | --------- |
| compute                                                              | similarity | between | these                                             | dense       | embeddings, |         | we rely on  | the intuition | that      |
| two vectors                                                          | are        | similar | if they                                           | have a high | dot         | product | (after all, | cosine        | is just a |
| normalizeddotproduct).                                               |            |         | Inotherwords:                                     |             |             |         |             |               |           |
|                                                                      |            |         | Similarity(w,c)≈c·w                               |             |             |         |             |               | (5.13)    |
| Thedotproductc·w                                                     |            |         | isnotaprobability,it’sjustanumberrangingfrom−∞to∞ |             |             |         |             |               |           |
(sincetheelementsinword2vecembeddingscanbenegative,thedotproductcanbe
negative).Toturnthedotproductintoaprobability,we’llusethelogisticorsigmoid
functionσ(x),thefundamentalcoreoflogisticregression:
1
|     |     |     | σ(x)= |     |     |     |     |     | (5.14) |
| --- | --- | --- | ----- | --- | --- | --- | --- | --- | ------ |
1+exp(−x)
Wemodeltheprobabilitythatwordcisarealcontextwordfortargetwordwas:
1
|     |     | P(+|w,c) |     | = σ(c·w)= |     |     |     |     | (5.15) |
| --- | --- | -------- | --- | --------- | --- | --- | --- | --- | ------ |
1+exp(−c·w)
Thesigmoidfunctionreturnsanumberbetween0and1,buttomakeitaprobability
we’llalsoneedthetotalprobabilityofthetwopossibleevents(cisacontextword,
| andcisn’tacontextword)tosumto1. |     |     |     |     | Wethusestimatetheprobabilitythatwordc |     |     |     |     |
| ------------------------------- | --- | --- | --- | --- | ------------------------------------- | --- | --- | --- | --- |
isnotarealcontextwordforwas:
|     |     | P(−|w,c) |     | = 1−P(+|w,c) |     |     |     |     |     |
| --- | --- | -------- | --- | ------------ | --- | --- | --- | --- | --- |
1
|     |     |     |     | = σ(−c·w)= |     |     |     |     | (5.16) |
| --- | --- | --- | --- | ---------- | --- | --- | --- | --- | ------ |
1+exp(c·w)
| Equation          | 5.15 | gives us | the probability                                      |     | for one | word, | but there | are many | context |
| ----------------- | ---- | -------- | ---------------------------------------------------- | --- | ------- | ----- | --------- | -------- | ------- |
| wordsinthewindow. |      |          | Skip-grammakesthesimplifyingassumptionthatallcontext |     |         |       |           |          |         |
wordsareindependent,allowingustojustmultiplytheirprobabilities:
L
(cid:89)
|     |     |     | P(+|w,c | 1:L ) | =   | σ(c ·w) |     |     | (5.17) |
| --- | --- | --- | ------- | ----- | --- | ------- | --- | --- | ------ |
i
i=1
L
(cid:88)
|     |     |     | logP(+|w,c | )   | =   | logσ(c | ·w) |     | (5.18) |
| --- | --- | --- | ---------- | --- | --- | ------ | --- | --- | ------ |
|     |     |     |            | 1:L |     |        | i   |     |        |
i=1
Insummary,skip-gramtrainsaprobabilisticclassifierthat,givenatesttargetword
| wanditscontextwindowofLwordsc |     |     |     |     | ,assignsaprobabilitybasedonhowsimilar |     |     |     |     |
| ----------------------------- | --- | --- | --- | --- | ------------------------------------- | --- | --- | --- | --- |
1:L
| thiscontextwindowistothetargetword. |     |     |     |     | Theprobabilityisbasedonapplyingthe |     |     |     |     |
| ----------------------------------- | --- | --- | --- | --- | ---------------------------------- | --- | --- | --- | --- |
logistic(sigmoid)functiontothedotproductoftheembeddingsofthetargetword
| witheachcontextword. |     |     | Tocomputethisprobability,wejustneedembeddingsfor |     |     |     |     |     |     |
| -------------------- | --- | --- | ------------------------------------------------ | --- | --- | --- | --- | --- | --- |
eachtargetwordandcontextwordinthevocabulary.
| Fig. | 5.6 shows | the | intuition | of the | parameters | we’ll | need. Skip-gram |     | actually |
| ---- | --------- | --- | --------- | ------ | ---------- | ----- | --------------- | --- | -------- |
storestwoembeddingsforeachword,oneforthewordasatarget,andoneforthe
| wordconsideredascontext. |         |            | Thustheparametersweneedtolearnaretwomatrices |           |     |       |            |           |        |
| ------------------------ | ------- | ---------- | -------------------------------------------- | --------- | --- | ----- | ---------- | --------- | ------ |
| W and                    | C, each | containing | an                                           | embedding | for | every | one of the | |V| words | in the |
vocabularyV.2
Let’snowturntolearningtheseembeddings(whichistherealgoal
oftrainingthisclassifierinthefirstplace).
2 Inprinciplethetargetmatrixandthecontextmatrixcouldusedifferentvocabularies,butwe’llsimplify
byassumingonesharedvocabularyV.

5.5 • WORD2VEC 13
1..d
aardvark 1
apricot
W target words
… …
= zebra |V|
aardvark |V|+1
𝜽 apricot
C context & noise
… … words
zebra 2|V|
Figure5.6 Theembeddingslearnedbytheskipgrammodel.Thealgorithmstorestwoem-
beddingsforeachword,thetargetembedding(sometimescalledtheinputembedding)and
thecontextembedding(sometimescalledtheoutputembedding).Theparameterθthattheal-
gorithmlearnsisthusamatrixof2|V|vectors,eachofdimensiond,formedbyconcatenating
twomatrices,thetargetembeddingsWandthecontext+noiseembeddingsC.
5.5.2 Learningskip-gramembeddings
The learning algorithm for skip-gram embeddings takes as input a corpus of text,
andachosenvocabularysizeN.Itbeginsbyassigningarandomembeddingvector
for each of the N vocabulary words, and then proceeds to iteratively shift the em-
beddingofeachwordwtobemoreliketheembeddingsofwordsthatoccurnearby
intexts, andlessliketheembeddingsofwordsthatdon’toccurnearby. Let’sstart
byconsideringasinglepieceoftrainingdata:
... lemon, a [tablespoon of apricot jam, a] pinch ...
c1 c2 w c3 c4
Thisexamplehasatargetwordw(apricot),and4contextwordsintheL=±2
window,resultingin4positivetraininginstances(ontheleftbelow):
positiveexamples+ negativeexamples-
w c pos w c neg w c neg
apricot tablespoon apricot aardvark apricot seven
apricot of apricot my apricot forever
apricot jam apricot where apricot dear
apricot a apricot coaxial apricot if
For training a binary classifier we also need negative examples. In fact skip-
gram with negative sampling (SGNS) uses more negative examples than positive
examples(withtheratiobetweenthemsetbyaparameterk). Soforeachofthese
(w,c ) training instances we’ll create k negative samples, each consisting of the
pos
targetwplusa‘noiseword’c . Anoisewordisarandomwordfromthelexicon,
neg
constrained not to be the target word w. The table right above shows the setting
where k=2, so we’ll have 2 negative examples in the negative training set − for
eachpositiveexamplew,c .
pos
The noise words are chosen according to their weighted unigram probability
p (w),whereα isaweight. Ifweweresamplingaccordingtounweightedproba-
α
bilityP(w),itwouldmeanthatwithunigramprobabilityP(“the”)wewouldchoose
the word the as a noise word, with unigram probability P(“aardvark”) we would
chooseaardvark,andsoon. Butinpracticeitiscommontosetα =0.75,i.e. use

14 CHAPTER5 • EMBEDDINGS
theweightingP (w):
3
4
count(w)α
P α (w)= (cid:80) count(w(cid:48))α (5.19)
w(cid:48)
Settingα =.75givesbetterperformancebecauseitgivesrarenoisewordsslightly
higher probability: for rare words, P (w)>P(w). To illustrate this intuition, it
α
mighthelptoworkouttheprobabilitiesforanexamplewithα=.75andtwoevents,
P(a)=0.99andP(b)=0.01:
.99.75
P (a) = =0.97
α .99.75+.01.75
.01.75
P α (b) = .99.75+.01.75 =0.03 (5.20)
Thususingα =.75increasestheprobabilityoftherareeventbfrom0.01to0.03.
Given the set of positive and negative training instances, and an initial set of
embeddings,thegoalofthelearningalgorithmistoadjustthoseembeddingsto
• Maximizethesimilarityofthetargetword,contextwordpairs(w,c )drawn
pos
fromthepositiveexamples
• Minimizethesimilarityofthe(w,c )pairsfromthenegativeexamples.
neg
Ifweconsideroneword/contextpair(w,c )withitsknoisewordsc ...c ,
pos neg
1
negk
we can express these two goals as the following loss function L to be minimized
(hencethe−);herethefirsttermexpressesthatwewanttheclassifiertoassignthe
real context word c a high probability of being a neighbor, and the second term
pos
expressesthatwewanttoassigneachofthenoisewordsc ahighprobabilityof
negi
beinganon-neighbor,allmultipliedbecauseweassumeindependence:
(cid:34) k (cid:35)
(cid:89)
L(w,c ,c ) = −log P(+|w,c ) P(−|w,c )
pos neg* pos negi
i=1
(cid:34) k (cid:35)
(cid:88)
= − logP(+|w,c )+ logP(−|w,c )
pos negi
i=1
(cid:34) k (cid:35)
(cid:88) (cid:0) (cid:1)
= − logP(+|w,c )+ log 1−P(+|w,c )
pos negi
i=1
(cid:34) k (cid:35)
(cid:88)
= − logσ(c pos ·w)+ logσ(−c negi ·w) (5.21)
i=1
That is, we want to maximize the dot product of the word with the actual context
words,andminimizethedotproductsofthewordwiththeknegativesamplednon-
neighborwords.
Weminimizethislossfunctionusingstochasticgradientdescent. Fig.5.7shows
theintuitionofonestepoflearning.
To get the gradient, we need to take the derivative of Eq. 5.21 with respect to
thedifferentembeddings. Itturnsoutthederivativesarethefollowing(weleavethe

5.5 • WORD2VEC 15
aardvark
move apricot and jam closer,
apricot w increasing c pos (cid:122) w
W
“…apricot jam…”
zebra
!
aardvark
move apricot and matrix apart
decreasing c (cid:122) w
jam c neg1
pos
C
matrix c neg1
k=2
Tolstoy c neg2 move apricot and Tolstoy apart
decreasing c (cid:122) w
neg2
zebra
Figure5.7 Intuitionofonestepofgradientdescent.Theskip-grammodeltriestoshiftem-
beddingssothetargetembeddings(hereforapricot)arecloserto(haveahigherdotproduct
with)contextembeddingsfornearbywords(herejam)andfurtherfrom(lowerdotproduct
with)contextembeddingsfornoisewordsthatdon’toccurnearby(hereTolstoyandmatrix).
proofasanexerciseattheendofthechapter):
∂L
= [σ(c pos ·w)−1]w (5.22)
∂c
pos
∂L
∂c
= [σ(c negi ·w)]w (5.23)
negi
k
∂L (cid:88)
∂w
= [σ(c pos ·w)−1]c pos + [σ(c negi ·w)]c negi (5.24)
i=1
Theupdateequationsgoingfromtimestept tot+1instochasticgradientdescent
arethus:
ct+1 = ct −η[σ(ct ·wt)−1]wt (5.25)
pos pos pos
ct+1 = ct −η[σ(ct ·wt)]wt (5.26)
negi negi negi
(cid:34) k (cid:35)
(cid:88)
wt+1 = wt−η [σ(ct ·wt)−1]ct + [σ(ct ·wt)]ct (5.27)
pos pos negi negi
i=1
Justasinlogisticregression,then,thelearningalgorithmstartswithrandomlyini-
tializedWandCmatrices,andthenwalksthroughthetrainingcorpususinggradient
descenttomoveWandCsoastominimizethelossinEq.5.21bymakingtheup-
datesin(Eq.5.25)-(Eq.5.27).
Recallthattheskip-grammodellearnstwoseparateembeddingsforeachwordi:
target thetargetembeddingw andthecontextembeddingc,storedintwomatrices,the
embedding i i
context targetmatrixWandthecontextmatrixC. It’scommontojustaddthemtogether,
embedding
representingwordiwiththevectorw +c. AlternativelywecanthrowawaytheC
i i
matrixandjustrepresenteachwordibythevectorw.
i
As with the simple count-based methods like tf-idf, the context window size
affects the performance of skip-gram embeddings, and experiments often tune the
contextwindowsizeparameteronadevset.

16 CHAPTER5 • EMBEDDINGS
5.5.3 Otherkindsofstaticembeddings
fasttext There are many kinds of static embeddings. An extension of word2vec, fasttext
(Bojanowskietal.,2017),addressesaproblemwithword2vecaswehavepresented
it so far: it has no good way to deal with unknown words—words that appear in
a test corpus but were unseen in the training corpus. A related problem is word
sparsity,suchasinlanguageswithrichmorphology,wheresomeofthemanyforms
for each noun and verb may only occur rarely. Fasttext deals with these problems
byusingsubwordmodels,representingeachwordasitselfplusabagofconstituent
n-grams,withspecialboundarysymbols<and>addedtoeachword.Forexample,
withn=3thewordwherewouldberepresentedbythesequence<where>plusthe
charactern-grams:
<wh, whe, her, ere, re>
Then a skipgram embedding is learned for each constituent n-gram, and the word
whereisrepresentedbythesumofalloftheembeddingsofitsconstituentn-grams.
Unknownwordscanthenbepresentedonlybythesumoftheconstituentn-grams.
Rohde,Gonnerman,Plaut ModelingWordMeaningUsingLexicalCo-Occurrence
Afasttextopen-sourcelibrary,includingpretrainedembeddingsfor157languages,
isavailableathttps://fasttext.cc.
AnotherverywidelyusedstaticembeddingmodelisGloVe(Penningtonetal.,
2014), short for GFR RlA U NoS C SbE IAal Vectors, because the model is based on capturing global
CHINA
corpusstatistics. GloVeisbasedonratiosofprobabilitiesfromtheword-wordco-
WRIST
EAUSRIOAPE
ARAMNKLE occurrencematrixA.AFMREICRAICA
E FI A NS RH HG A OE FN RU AE DC L Y D EE ER Itturnsoutthat BR d A M e Z O IL n SC s OW eembeddingslikeword2vecactuallyhaveanelegantmath-
TOE LEG ematicalrelationshipwithcount-basedembeddings,inwhichword2veccanbeseen
FOOT
TOOTNHOHSEEAD asimplicitlyoptim
T
Hi
O
Az
K
W
Y
iA
O
nIIgafunctionofacountmatrixwithaparticular(PPMI)weight-
ing(LevyandGoldberg,2014c).
MONTREAL
MOUSE
CHAICTALAGNOTA
5.6 Visualizing Embeddings
DOG
CAT
TURTLE
PKUIPTPTYEN COW LION NASHVILLE
OYSTER “Iseewellinmanydimensionsaslongasthedimensionsarearoundtwo.”
ThelateeconomistMartinShubik
BULL
Figure8:MultidimensionalscValiinsgufaorlithzrienegnouenmclbasesdesd.ings is an important goal in helping understand, apply, and
improvethesemodelsofwordmeaning. Buthowcanwevisualizea(forexample)
100-dimensionalvector?
The simplest way to visualize the meaning of a word
WRIST
ANKLE w embedded in a space is to list the most similar words to
SHOULDER
ARM
LEG w by sorting the vectors for all words in the vocabulary by
HAND
FOOT theircosinewiththevectorforw. Forexamplethe7closest
HEAD
NOSE
FINGER wordstofrogusingaparticularsetofembeddingscomputed
TOE
FACE with the GloVe algorithm are: frogs, toad, litoria, lepto-
EAR
EYE
TOOTH dactylidae,rana,lizard,andeleutherodactylus(Pennington
DOG
CAT etal.,2014).
PUPPY
KITTEN
COW Yet another visualization method is to use a clustering
MOUSE
TURTLE algorithm to show a hierarchical representation of which
OYSTER
LION
BULL words are similar to others in the embedding space. The
CHICAGO
ATLANTA uncaptioned figure on the left uses hierarchical clustering
MONTREAL
NASHVILLE
TOKYO of some embedding vectors for nouns as a visualization
CHINA
RUSSIA method(Rohdeetal.,2006).
AFRICA
ASIA
EUROPE
AMERICA
BRAZIL
MOSCOW
FRANCE
HAWAII
Figure9:Hierarchicalclusteringforthreenounclassesusingdistancesbasedonvectorcorrelations.
20

|     |     |     |     | 5.7 | •   | SEMANTICPROPERTIESOFEMBEDDINGS |     |     |     |     | 17  |
| --- | --- | --- | --- | --- | --- | ------------------------------ | --- | --- | --- | --- | --- |
Probablythemostcommonvisualizationmethod,how-
ever,istoprojectthe100dimensionsofaworddowninto2
|     |     |     |     | dimensions. |      | Fig.5.1showedonesuchvisualization,asdoes |     |        |        |       |          |
| --- | --- | --- | --- | ----------- | ---- | ---------------------------------------- | --- | ------ | ------ | ----- | -------- |
|     |     |     |     | Fig.        | 5.9, | using a projection                       |     | method | called | t-SNE | (van der |
MaatenandHinton,2008).
| 5.7 Semantic |     | properties |     |     | of  | embeddings |     |     |     |     |     |
| ------------ | --- | ---------- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- |
Inthissectionwebrieflysummarizesomeofthesemanticpropertiesofembeddings
thathavebeenstudied.
|     | Different | types | of  | similarity | or  | association: | One | parameter |     | of vector | semantic |
| --- | --------- | ----- | --- | ---------- | --- | ------------ | --- | --------- | --- | --------- | -------- |
modelsthatisrelevanttobothsparsePPMIvectorsanddenseword2vecvectorsis
|     | thesizeofthecontextwindowusedtocollectcounts. |     |     |     |     |     |     | Thisisgenerallybetween1 |     |     |     |
| --- | --------------------------------------------- | --- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | --- |
and10wordsoneachsideofthetargetword(foratotalcontextof2-20words).
|     | Thechoicedependsonthegoalsoftherepresentation. |     |     |     |     |     |     |     | Shortercontextwindows |     |     |
| --- | ---------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --------------------- | --- | --- |
tendtoleadtorepresentationsthatareabitmoresyntactic,sincetheinformationis
comingfromimmediatelynearbywords.Whenthevectorsarecomputedfromshort
contextwindows,themostsimilarwordstoatargetwordwtendtobesemantically
|     | similarwordswiththesamepartsofspeech. |     |     |     |     |     | Whenvectorsarecomputedfromlong |     |     |     |     |
| --- | ------------------------------------- | --- | --- | --- | --- | --- | ------------------------------ | --- | --- | --- | --- |
contextwindows,thehighestcosinewordstoatargetwordwtendtobewordsthat
aretopicallyrelatedbutnotsimilar.
|     | For | example | Levy | and | Goldberg | (2014a) | showed | that | using | skip-gram | with a |
| --- | --- | ------- | ---- | --- | -------- | ------- | ------ | ---- | ----- | --------- | ------ |
windowof±2,themostsimilarwordstothewordHogwarts(fromtheHarryPotter
|     | series) | were | names | of other | fictional | schools: | Sunnydale |     | (from | Buffy the | Vampire |
| --- | ------- | ---- | ----- | -------- | --------- | -------- | --------- | --- | ----- | --------- | ------- |
Slayer)orEvernight(fromavampireseries).Withawindowof±5,themostsimilar
|     | words | to Hogwarts |     | were | other words | topically | related |     | to the | Harry Potter | series: |
| --- | ----- | ----------- | --- | ---- | ----------- | --------- | ------- | --- | ------ | ------------ | ------- |
Dumbledore,Malfoy,andhalf-blood.
It’salsooftenusefultodistinguishtwokindsofsimilarityorassociationbetween
first-order words (Schu¨tze and Pedersen, 1993). Two words have first-order co-occurrence
co-occurrence
(sometimescalledsyntagmaticassociation)iftheyaretypicallynearbyeachother.
Thuswroteisafirst-orderassociateofbookorpoem.Twowordshavesecond-order
second-order co-occurrence (sometimes called paradigmatic association) if they have similar
co-occurrence
|     | neighbors.                          | Thuswroteisasecond-orderassociateofwordslikesaidorremarked. |     |     |     |                                            |     |     |     |     |     |
| --- | ----------------------------------- | ----------------------------------------------------------- | --- | --- | --- | ------------------------------------------ | --- | --- | --- | --- | --- |
|     | Analogy/RelationalSimilarity:       |                                                             |     |     |     | Anothersemanticpropertyofembeddingsistheir |     |     |     |     |     |
|     | abilitytocapturerelationalmeanings. |                                                             |     |     |     | Inanimportantearlyvectorspacemodelof       |     |     |     |     |     |
parallelogram cognition, RumelhartandAbrahamson(1973)proposedtheparallelogrammodel
model
|     | forsolvingsimpleanalogyproblemsoftheformaistobasa*istowhat?. |     |     |     |     |     |     |     |     |     | Insuch |
| --- | ------------------------------------------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- | ------ |
problems,asystemisgivenaproblemlikeapple:tree::grape:?,i.e.,appleistotree
|     | asgrapeisto |     |     | ,andmustfillinthewordvine. |     |     |     | Intheparallelogrammodel,il- |     |       |           |
| --- | ----------- | --- | --- | -------------------------- | --- | --- | --- | --------------------------- | --- | ----- | --------- |
|     |             |     |     |                            |     |     |     |                             |     | #   » | #       » |
lustratedinFig.5.8,thevectorfromthewordappletothewordtree(=tree−apple)
#        »
isaddedtothevectorforgrape(grape);thenearestwordtothatpointisreturned.
Inearlyworkwithsparseembeddings,scholarsshowedthatsparsevectormod-
|     | els of    | meaning        | could | solve    | such     | analogy      | problems   | (Turney            |               | and Littman, | 2005),           |
| --- | --------- | -------------- | ----- | -------- | -------- | ------------ | ---------- | ------------------ | ------------- | ------------ | ---------------- |
|     | but the   | parallelogram  |       | method   | received | more         | modern     | attention          |               | because      | of its suc-      |
|     | cess with | word2vec       |       | or GloVe | vectors  | (Mikolov     |            | et al. 2013c,      |               | Levy and     | Goldberg #     » |
|     | 2014b,    | Pennington     |       | et al.   | 2014).   | For example, | the        | result             | of the        | expression   | king−            |
|     | #     »   | #            » |       |          |          | #         »  |            | #      »           | #           » |              | #     »          |
|     | man+woman |                | is a  | vector   | close to | queen.       | Similarly, | Paris−France+Italy |               |              | results          |
#         »
|     | in a vector | that | is close | to  | Rome. | The embedding |     | model | thus | seems to | be extract- |
| --- | ----------- | ---- | -------- | --- | ----- | ------------- | --- | ----- | ---- | -------- | ----------- |

18 CHAPTER5 • EMBEDDINGS
tree
apple
vine
grape
Figure5.8 Theparallelogrammodelforanalogyproblems(RumelhartandAbrahamson,
# » # » # » # »
1973):thelocationofvinecanbefoundbysubtractingapplefromtreeandaddinggrape.
ingrepresentationsofrelationslikeMALE-FEMALE,orCAPITAL-CITY-OF,oreven
COMPARATIVE/SUPERLATIVE,asshowninFig.5.9fromGloVe.
(a) (b)
Figure5.9 RelationalpropertiesoftheGloVevectorspace,shownbyprojectingvectorsontotwodimensions.
# » # » # » # »
(a)king−man+womanisclosetoqueen.(b)offsetsseemtocapturecomparativeandsuperlativemorphology
(Penningtonetal.,2014).
Foraa:b::a∗:b∗ problem, meaningthealgorithmisgivenvectorsa, b, and
a∗andmustfindb∗,theparallelogrammethodisthus:
bˆ∗=argmin distance(x,b−a+a∗)
(5.28)
x
withsomedistancefunction,suchasEuclideandistance.
There are some caveats. For example, the closest value returned by the paral-
lelogram algorithm in word2vec or GloVe embedding spaces is usually not in fact
b* but one of the 3 input words or their morphological variants (i.e., cherry:red ::
potato:x returns potato or potatoes instead of brown), so these must be explicitly
excluded. Furthermore while embedding spaces perform well if the task involves
frequent words, small distances, and certain relations (like relating countries with
their capitals or verbs/nouns with their inflected forms), the parallelogram method
with embeddings doesn’t work as well for other relations (Linzen 2016, Gladkova
etal.2016,Schluter2018,Ethayarajhetal.2019a),andindeedPetersonetal.(2020)
argue that the parallelogram method is in general too simple to model the human
cognitiveprocessofforminganalogiesofthiskind.

|     |     |     |     | 5.8 | •   | BIASANDEMBEDDINGS |     |     | 19  |
| --- | --- | --- | --- | --- | --- | ----------------- | --- | --- | --- |
5.7.1 EmbeddingsandHistoricalSemantics
Embeddingscanalsobeausefultoolforstudyinghowmeaningchangesovertime,
| by computing | multiple                                                  | embedding |     | spaces, | each from | texts | written | in a particular |     |
| ------------ | --------------------------------------------------------- | --------- | --- | ------- | --------- | ----- | ------- | --------------- | --- |
| timeperiod.  | ForexampleFig.5.10showsavisualizationofchangesinmeaningin |           |     |         |           |       |         |                 |     |
Englishwordsoverthelasttwocenturies,computedbybuildingseparateembedding
CspHaAcePsTfoErRea5c.hDdeYcNadAeMfrIoCmShOisCtoIrAicLalRcEoPrpRoEraSlEikNeTGAoToIgOleNnS-gOraFmWsO(LRinDeMtaEl.A,2N0I1N2G)
79
andtheCorpusofHistoricalAmericanEnglish(Davies,2012).
| Figure5.10 | A t-SNE | visualization | of  | the semantic | change | of  | 3 words | in English | using |
| ---------- | ------- | ------------- | --- | ------------ | ------ | --- | ------- | ---------- | ----- |
Figure5.1: Two-dimensionalvisualizationofsemanticchangeinEnglishusingSGNS
| word2vec | vectors. The | modern sense | of  | each word, | and | the grey | context | words, | are com- |
| -------- | ------------ | ------------ | --- | ---------- | --- | -------- | ------- | ------ | -------- |
vectors (see Section 5.8 for the visualization algorithm). A, The word gay shifted
| putedfromthemostrecent(modern)time-pointembeddingspace. |     |     |     |     |     |     | Earlierpointsarecom- |     |     |
| ------------------------------------------------------- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- |
frommeaning“cheerful”or“frolicsome”toreferringtohomosexuality. putedfromearlierhistoricalembeddingspaces. Thevisualizationsshowthechangesinthe A,Intheearly
2w0otrhdcgeanytfurroymbmroeaadncinagsstrreelfaeterdretdot“och“ecearfsutli”ngoro“ufrtosliecesdosm”e;”wtoithreftehrreinrgisteoohfotmeolesvexisuiaolnitya,nd
rthaedidoeviteslompmeaenntinogftshheifmteoddetron““ttrraannssmmisitstioinng”sseignnsealosf”.brCoa,dAcawsftuflroumnditesrowreignitnaalspernosceesosfof
psoewjoirnagtisoened,sa,sanitdsthhieftpeedjofrraotimonmofeathneinwgo“rdfualwl ofuflaawseit”sthoiftmedeafrnoimngm“etaenrirnibgl“efuolrlaofppawalel”ing”
[t2o1m2]e.aning“terribleorappalling”(Hamiltonetal.,2016).
that adverbials (e.g., actually) have a general tendency to undergo subjectification
5.8 BiaswhaernedtheEy smhifbt ferodmdoibnjegctisve statements about the world (e.g., “Sorry, the car is
actuallybroken”)tosubjectivestatements(e.g., “Ican’tbelieveheactuallydidthat”,
| indicating                                   | surprise/disbelief). |            |                                       |             |         |           |                   |        |          |
| -------------------------------------------- | -------------------- | ---------- | ------------------------------------- | ----------- | ------- | --------- | ----------------- | ------ | -------- |
| In addition                                  | to their             | ability to | learn                                 | word        | meaning | from      | text, embeddings, |        | alas,    |
| also reproduce                               | the implicit         | biases     | and                                   | stereotypes |         | that were | latent            | in the | text. As |
| 5th.e2.p2riorCseoctmionpjuutstasthioowneadl, |                      |            | leimnbgeuddisintgisccsatnurdouieghsly |             |         | model     | relational        |        | similar- |
| ity: ‘queen’                                 | as the closest       | word       | to ‘king’                             | -           | ‘man’   | + ‘woman’ | implies           | the    | analogy  |
Therearealsoanumberofrecentworksanalyzingsemanticchangeusingcomputational
| man:woman::king:queen. |     | Butthesesameembeddinganalogiesalsoexhibitgender |     |     |     |     |     |     |     |
| ---------------------- | --- | ----------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
msteertehootdysp.e[s2.00F]ourseexlaamtepnltesBemolaunktbiacsaineatlayls.is(2t0o1a6n)afilynzdethhoawt twheorcdlomseesatnoincgcuspbartoioanden
atond‘cnoamrprouwteropverorgtriammem. e[1r1’3-]‘umsaenr’a+w‘cwoo-omcacnu’rriennwceorvde2cvtoercsetmobpeedrdfoinrgmstaraniunemdboenr of
| news text | is ‘homemaker’, | and | that | the embeddings |     | similarly | suggest | the | analogy |
| --------- | --------------- | --- | ---- | -------------- | --- | --------- | ------- | --- | ------- |
historical case-studies on semantic change, and [252] perform a similar set of small-
| ‘father’isto‘doctor’as‘mother’isto‘nurse’. |     |     |     |     | ThiscouldresultinwhatCrawford |     |     |     |     |
| ------------------------------------------ | --- | --- | --- | --- | ----------------------------- | --- | --- | --- | --- |
scale case-studies using temporal topic models. [87] construct point-wise mutual
allocational (2017) and Blodgett et al. (2020) call an allocational harm, when a system allo-
harm
icnaftoersmreastoiounr-cbeass(ejdobesmobrecdrdedinitg)suannfadirfloyutnoddtihffaetresnetmgarnotuipcsc.hFaonrgeexsaumnpcloevaerlgeodribtyhmthseir
mtheatthuosdeheamdbreedadsionngasbalesapgarreteomfeanstewaritchhhfourmhainrinjugdpgomteennttisa.l[p1r2o9g]raanmdm[1e1rs9]oursdeo“cntoeursral”
mightthusincorrectlydownweightdocumentswithwomen’snames.
word-embedding methods to detect linguistic change points. Finally, [257] analyze
Itturnsoutthatembeddingsdon’tjustreflectthestatisticsoftheirinput,butalso
bias h i st o r i c al c o - o cc u r r e n c es t o t e s t w h e th er s yn o n y m s te n d to c h a n g e in s i m i la r w a y s.
| a m p l i f y | b ia s ; g e n d e r | e d te r m s | b e c o m | e m or e | g e n d er | ed i n em | b e d d in g | s pa c e | t h a n th e y |
| ------------- | -------------------- | ------------ | --------- | -------- | ---------- | --------- | ------------ | -------- | -------------- |
amplification
wereintheinputtextstatistics(Zhaoetal.2017,Ethayarajhetal.2019b,Jiaetal.
| 2020), and | biases are | more exaggerated |     | than | in actual | labor | employment |     | statistics |
| ---------- | ---------- | ---------------- | --- | ---- | --------- | ----- | ---------- | --- | ---------- |
(Gargetal.,2018).
Embeddingsalsoencodetheimplicitassociationsthatareapropertyofhuman
| reasoning. | The Implicit | Association |     | Test (Greenwald |     | et al., | 1998) | measures | peo- |
| ---------- | ------------ | ----------- | --- | --------------- | --- | ------- | ----- | -------- | ---- |

20 CHAPTER5 • EMBEDDINGS
ple’sassociationsbetweenconcepts(like‘flowers’or‘insects’)andattributes(like
‘pleasantness’ and ‘unpleasantness’) by measuring differences in the latency with
which they label words in the various categories.3 Using such methods, people
in the United States have been shown to associate African-American names with
unpleasant words (more than European-American names), male names more with
mathematicsandfemalenameswiththearts,andoldpeople’snameswithunpleas-
antwords(Greenwaldetal.1998,Noseketal.2002a,Noseketal.2002b). Caliskan
etal.(2017)replicatedallthesefindingsofimplicitassociationsusingGloVevectors
and cosine similarity instead of human latencies. For example African-American
nameslike‘Leroy’and‘Shaniqua’hadahigherGloVecosinewithunpleasantwords
while European-American names (‘Brad’, ‘Greg’, ‘Courtney’) had a higher cosine
withpleasantwords. Theseproblemswithembeddingsareanexampleofarepre-
representational sentationalharm(Crawford2017,Blodgettetal.2020),whichisaharmcausedby
harm
asystemdemeaningorevenignoringsomesocialgroups.Anyembedding-awareal-
gorithmthatmadeuseofwordsentimentcouldthusexacerbatebiasagainstAfrican
Americans.
Recent research focuses on ways to try to remove these kinds of biases, for
examplebydevelopingatransformationoftheembeddingspacethatremovesgen-
derstereotypesbutpreservesdefinitionalgender(Bolukbasietal.2016,Zhaoetal.
2017) or changing the training procedure (Zhao et al., 2018). However, although
debiasing these sorts of debiasing may reduce bias in embeddings, they do not eliminate it
(GonenandGoldberg,2019),andthisremainsanopenproblem.
Historical embeddings are also being used to measure biases in the past. Garg
et al. (2018) used embeddings from historical texts to measure the association be-
tween embeddings for occupations and embeddings for names of various ethnici-
tiesorgenders(forexampletherelativecosinesimilarityofwomen’snamesversus
men’s to occupation words like ‘librarian’ or ‘carpenter’) across the 20th century.
They found that the cosines correlate with the empirical historical percentages of
women or ethnic groups in those occupations. Historical embeddings also repli-
catedoldsurveysofethnicstereotypes;thetendencyofexperimentalparticipantsin
1933toassociateadjectiveslike‘industrious’or‘superstitious’with, e.g., Chinese
ethnicity,correlateswiththecosinebetweenChineselastnamesandthoseadjectives
usingembeddingstrainedon1930stext. Theyalsowereabletodocumenthistorical
genderbiases,suchasthefactthatembeddingsforadjectivesrelatedtocompetence
(‘smart’,‘wise’,‘thoughtful’,‘resourceful’)hadahighercosinewithmalethanfe-
malewords, andshowedthatthisbiashasbeenslowlydecreasingsince1960. We
return in later chapters to this question about the role of bias in natural language
processing.
5.9 Evaluating Vector Models
The most important evaluation metric for vector models is extrinsic evaluation on
tasks, i.e., using vectors in an NLP task and seeing whether this improves perfor-
manceoversomeothermodel.
3 Roughlyspeaking,ifhumansassociate‘flowers’with‘pleasantness’and‘insects’with‘unpleasant-
ness’,whentheyareinstructedtopushagreenbuttonfor‘flowers’(daisy,iris,lilac)and‘pleasantwords’
(love,laughter,pleasure)andaredbuttonfor‘insects’(flea,spider,mosquito)and‘unpleasantwords’
(abuse,hatred,ugly)theyarefasterthaninanincongruousconditionwheretheypusharedbuttonfor
‘flowers’and‘unpleasantwords’andagreenbuttonfor‘insects’and‘pleasantwords’.

5.10 • SUMMARY 21
Nonethelessitisusefultohaveintrinsicevaluations. Themostcommonmetric
is to test their performance on similarity, computing the correlation between an
algorithm’swordsimilarityscoresandwordsimilarityratingsassignedbyhumans.
WordSim-353 (Finkelstein et al., 2002) is a commonly used set of ratings from 0
to 10 for 353 noun pairs; for example (plane, car) had an average score of 5.77.
SimLex-999(Hilletal.,2015)isamorecomplexdatasetthatquantifiessimilarity
(cup,mug)ratherthanrelatedness(cup,coffee),andincludesconcreteandabstract
adjective, nounandverbpairs. TheTOEFLdatasetisasetof80questions, each
consisting of a target word with 4 additional word choices; the task is to choose
which is the correct synonym, as in the example: Levied is closest in meaning to:
imposed,believed,requested,correlated(LandauerandDumais,1997). Allofthese
datasetspresentwordswithoutcontext.
Slightly more realistic are intrinsic similarity tasks that include context. The
StanfordContextualWordSimilarity(SCWS)dataset(Huangetal.,2012)andthe
Word-in-Context(WiC)dataset(PilehvarandCamacho-Collados,2019)offerricher
evaluation scenarios. SCWS gives human judgments on 2,003 pairs of words in
theirsententialcontext,whileWiCgivestargetwordsintwosententialcontextsthat
are either in the same or different senses; see Appendix G. The semantic textual
similaritytask(Agirreetal.2012,Agirreetal.2015)evaluatestheperformanceof
sentence-level similarity algorithms, consisting of a set of pairs of sentences, each
pairwithhuman-labeledsimilarityscores.
Anothertaskusedforevaluationistheanalogytask,discussedonpage17,where
thesystemhastosolveproblemsoftheformaistobasa*istob*,givena,b,anda*
andhavingtofindb*(TurneyandLittman,2005). Anumberofsetsoftupleshave
been created for this task (Mikolov et al. 2013a, Mikolov et al. 2013c, Gladkova
et al. 2016), covering morphology (city:cities::child:children), lexicographic rela-
tions(leg:table::spout:teapot)andencyclopediarelations(Beijing:China::Dublin:Ireland),
somedrawingfromtheSemEval-2012Task2datasetof79differentrelations(Jur-
gensetal.,2012).
Allembeddingalgorithmssufferfrominherentvariability. Forexamplebecause
of randomness in the initialization and the random negative sampling, algorithms
like word2vec may produce different results even from the same dataset, and in-
dividual documents in a collection may strongly impact the resulting embeddings
(Tianetal.2016,HellrichandHahn2016,AntoniakandMimno2018). Whenem-
beddings are used to study word associations in particular corpora, therefore, it is
bestpracticetotrainmultipleembeddingswithbootstrapsamplingoverdocuments
andaveragetheresults(AntoniakandMimno,2018).
5.10 Summary
• Invectorsemantics,awordismodeledasavector—apointinhigh-dimensional
space,alsocalledanembedding. Inthischapterwefocusonstaticembed-
dings,whereeachwordismappedtoafixedembedding.
• Vector semantic models fall into two classes: sparse and dense. In sparse
modelseachdimensioncorrespondstoawordinthevocabularyV andcells
arefunctionsofco-occurrencecounts. Theword-contextorterm-termma-
trixhasarowforeach(target)wordinthevocabularyandacolumnforeach
contextterminthevocabulary.

22 CHAPTER5 • EMBEDDINGS
• Dense vector models typically have dimensionality 50–1000. Word2vec al-
gorithms like skip-gram are a popular way to compute dense embeddings.
Skip-gramtrainsalogisticregressionclassifiertocomputetheprobabilitythat
two words are ‘likely to occur nearby in text’. This probability is computed
fromthedotproductbetweentheembeddingsforthetwowords.
• Skip-gramusesstochasticgradientdescenttotraintheclassifier,bylearning
embeddingsthathaveahighdotproductwithembeddingsofwordsthatoccur
nearbyandalowdotproductwithnoisewords.
• Other important embedding algorithms include GloVe, a method based on
ratiosofwordco-occurrenceprobabilities.
• Whether using sparse or dense vectors, word and document similarities are
computedbysomefunctionofthedotproductbetweenvectors. Thecosine
oftwovectors—anormalizeddotproduct—isthemostpopularsuchmetric.
Historical Notes
The idea of vector semantics arose out of research in the 1950s in three distinct
fields: linguistics, psychology, and computer science, each of which contributed a
fundamentalaspectofthemodel.
The idea that meaning is related to the distribution of words in context was
widespread in linguistic theory of the 1950s, among distributionalists like Zellig
Harris,MartinJoos,andJ.R.Firth,andsemioticianslikeThomasSebeok. AsJoos
(1950)putit,
thelinguist’s“meaning”ofamorpheme...isbydefinitionthesetofconditional
probabilitiesofitsoccurrenceincontextwithallothermorphemes.
The idea that the meaning of a word might be modeled as a point in a multi-
dimensionalsemanticspacecamefrompsychologistslikeCharlesE.Osgood,who
hadbeenstudyinghowpeoplerespondedtothemeaningofwordsbyassigningval-
uesalongscaleslikehappy/sadorhard/soft. Osgoodetal.(1957)proposedthatthe
meaning of a word in general could be modeled as a point in a multidimensional
Euclidean space, and that the similarity of meaning between two words could be
modeledasthedistancebetweenthesepointsinthespace.
Afinalintellectualsourceinthe1950sandearly1960swasthefieldthencalled
mechanical mechanicalindexing,nowknownasinformationretrieval.Inwhatbecameknown
indexing
as the vector space model for information retrieval (Salton 1971, Sparck Jones
1986),researchersdemonstratednewwaystodefinethemeaningofwordsinterms
ofvectors(Switzer,1965), andrefinedmethodsforwordsimilaritybasedonmea-
sures of statistical association between words like mutual information (Giuliano,
1965) and idf (Sparck Jones, 1972), and showed that the meaning of documents
could be represented in the same vector spaces used for words. Around the same
time, (Cordier,1965) showed that factoranalysis of wordassociation probabilities
couldbeusedtoformdensevectorrepresentationsofwords.
Some of the philosophical underpinning of the distributional way of thinking
came from the late writings of the philosopher Wittgenstein, who was skeptical of
the possibility of building a completely formal theory of meaning definitions for
eachword. Wittgensteinsuggestedinsteadthat“themeaningofawordisitsusein
thelanguage”(Wittgenstein,1953,PI43).Thatis,insteadofusingsomelogicallan-
guagetodefineeachword,ordrawingondenotationsortruthvalues,Wittgenstein’s

HISTORICALNOTES 23
ideaisthatweshoulddefineawordbyhowitisusedbypeopleinspeakingandun-
derstandingintheirday-to-dayinteractions,thusprefiguringthemovementtoward
embodiedandexperientialmodelsinlinguisticsandNLP(GlenbergandRobertson
2000,LakeandMurphy2021,Bisketal.2020,BenderandKoller2020).
Moredistantlyrelatedistheideaofdefiningwordsbyavectorofdiscretefea-
tures,whichhasrootsatleastasfarbackasDescartesandLeibniz(Wierzbicka1992,
Wierzbicka 1996). By the middle of the 20th century, beginning with the work of
Hjelmslev (Hjelmslev, 1969) (originally 1943) and fleshed out in early models of
generative grammar (Katz and Fodor, 1963), the idea arose of representing mean-
semantic ingwithsemanticfeatures,symbolsthatrepresentsomesortofprimitivemeaning.
feature
Forexamplewordslikehen,rooster,orchick,havesomethingincommon(theyall
describechickens)andsomethingdifferent(theirageandsex),representableas:
hen +female, +chicken, +adult
rooster -female, +chicken, +adult
chick +chicken, -adult
Thedimensionsusedbyvectormodelsofmeaningtodefinewords,however,are
onlyabstractlyrelatedtothisideaofasmallfixednumberofhand-builtdimensions.
Nonetheless, there has been some attempt to show that certain dimensions of em-
bedding models do contribute some specific compositional aspect of meaning like
theseearlysemanticfeatures.
Theuseofdensevectorstomodelwordmeaning,andindeedthetermembed-
ding, grew out of the latent semantic indexing (LSI) model (Deerwester et al.,
1988)recastasLSA(latentsemanticanalysis)(Deerwesteretal.,1990). InLSA
SVD singularvaluedecomposition—SVD—isappliedtoaterm-documentmatrix(each
cell weighted by log frequency and normalized by entropy), and then the first 300
dimensionsareusedastheLSAembedding. SingularValueDecomposition(SVD)
is a method for finding the most important dimensions of a dataset, those dimen-
sionsalongwhichthedatavariesthemost. LSAwasthenquicklywidelyapplied:
asacognitivemodel(LandauerandDumais,1997),andfortaskslikespellchecking
(Jones and Martin, 1997), language modeling (Bellegarda 1997, Coccaro and Ju-
rafsky 1998, Bellegarda 2000), morphology induction (Schone and Jurafsky 2000,
SchoneandJurafsky2001b),multiwordexpressions(MWEs)(SchoneandJurafsky,
2001a), and essay grading (Rehder et al., 1998). Related models were simultane-
ouslydevelopedandappliedtowordsensedisambiguationbySchu¨tze(1992). LSA
alsoledtotheearliestuseofembeddingstorepresentwordsinaprobabilisticclas-
sifier,inthelogisticregressiondocumentrouterofSchu¨tzeetal.(1995).Theideaof
SVDontheterm-termmatrix(ratherthantheterm-documentmatrix)asamodelof
meaningforNLPwasproposedsoonafterLSAbySchu¨tze(1992). Schu¨tzeapplied
the low-rank (97-dimensional) embeddings produced by SVD to the task of word
sense disambiguation, analyzed the resulting semantic space, and also suggested
possibletechniqueslikedroppinghigh-orderdimensions. SeeSchu¨tze(1997).
A number of alternative matrix models followed on from the early SVD work,
including Probabilistic Latent Semantic Indexing (PLSI) (Hofmann, 1999), Latent
DirichletAllocation(LDA)(Bleietal.,2003),andNon-negativeMatrixFactoriza-
tion(NMF)(LeeandSeung,1999).
TheLSAcommunityseemstohavefirstusedtheword“embedding”inLandauer
etal.(1997),inavariantofitsmathematicalmeaningasamappingfromonespace
or mathematical structure to another. In LSA, the word embedding seems to have
describedthemappingfromthespaceofsparsecountvectorstothelatentspaceof
SVDdensevectors. Althoughthewordthusoriginallymeantthemappingfromone

24 CHAPTER5 • EMBEDDINGS
spacetoanother,ithasmetonymicallyshiftedtomeantheresultingdensevectorin
thelatentspace,anditisinthissensethatwecurrentlyusetheword.
| By the | next decade, | Bengio | et al. (2003) | and | Bengio | et al. (2006) | showed | that |
| ------ | ------------ | ------ | ------------- | --- | ------ | ------------- | ------ | ---- |
neurallanguagemodelscouldalsobeusedtodevelopembeddingsaspartofthetask
| ofwordprediction. | CollobertandWeston(2007),CollobertandWeston(2008),and |     |     |     |     |     |     |     |
| ----------------- | ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- |
Collobertetal.(2011)thendemonstratedthatembeddingscouldbeusedtorepresent
| wordmeaningsforanumberofNLPtasks. |                |            |               | Turianetal.(2010)comparedthevalue |             |         |        |         |
| --------------------------------- | -------------- | ---------- | ------------- | --------------------------------- | ----------- | ------- | ------ | ------- |
| of different                      | kinds of       | embeddings | for different |                                   | NLP tasks.  | Mikolov | et al. | (2011)  |
| showed                            | that recurrent | neural     | nets could    | be used                           | as language | models. | The    | idea of |
simplifyingthehiddenlayeroftheseneuralnetlanguagemodelstocreatetheskip-
| gram (and                                                          | also CBOW) | algorithms | was        | proposed | by Mikolov              | et al. | (2013a).    | The   |
| ------------------------------------------------------------------ | ---------- | ---------- | ---------- | -------- | ----------------------- | ------ | ----------- | ----- |
| negativesamplingtrainingalgorithmwasproposedinMikolovetal.(2013b). |            |            |            |          |                         |        |             | There |
| are numerous                                                       | surveys    | of static  | embeddings | and      | their parameterizations |        | (Bullinaria |       |
andLevy2007,BullinariaandLevy2012,LapesaandEvert2014,KielaandClark
2014,Levyetal.2015).
SeeManningetal.(2008)andChapter11foradeeperunderstandingoftherole
| of vectors                                                       | in information | retrieval, | including |     | how to compare | queries              | with | docu-  |
| ---------------------------------------------------------------- | -------------- | ---------- | --------- | --- | -------------- | -------------------- | ---- | ------ |
| ments,moredetailsontf-idf,andissuesofscalingtoverylargedatasets. |                |            |           |     |                |                      |      | SeeKim |
| (2019)foraclearandcomprehensivetutorialonword2vec.               |                |            |           |     |                | Cruse(2004)isauseful |      |        |
introductorylinguistictextonlexicalsemantics.
Exercises

|     |     |     |     |     |     |     |     |     |     | Exercises | 25  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --------- | --- |
Agirre, E., C. Banea, C. Cardie, D. Cer, M. Diab, Carlson,G.N.1977. ReferencetokindsinEnglish. Ph.D.
A.Gonzalez-Agirre,W.Guo,I.Lopez-Gazpio,M.Mar- thesis,UniversityofMassachusetts,Amherst.Forward.
| itxalar, | R. Mihalcea, | G.  | Rigau, L. | Uria, and | J. Wiebe. |               |                         |     |     |               |     |
| -------- | ------------ | --- | --------- | --------- | --------- | ------------- | ----------------------- | --- | --- | ------------- | --- |
|          |              |     |           |           |           | Clark,E.1987. | Theprincipleofcontrast: |     |     | Aconstrainton |     |
2015. SemEval-2015task2:Semantictextualsimilarity,
|                                            |     |     |     |     |          | language | acquisition. | In B. | MacWhinney, |     | ed., Mecha- |
| ------------------------------------------ | --- | --- | --- | --- | -------- | -------- | ------------ | ----- | ----------- | --- | ----------- |
| English,Spanishandpilotoninterpretability. |     |     |     |     | SemEval- |          |              |       |             |     |             |
nismsoflanguageacquisition,1–33.LEA.
15.
|     |     |     |     |     |     | Coccaro,N.andD.Jurafsky.1998. |     |     | Towardsbetterintegra- |     |     |
| --- | --- | --- | --- | --- | --- | ----------------------------- | --- | --- | --------------------- | --- | --- |
Agirre,E.,M.Diab,D.Cer,andA.Gonzalez-Agirre.2012.
tionofsemanticpredictorsinstatisticallanguagemodel-
| SemEval-2012task6: |     | Apilotonsemantictextualsimi- |     |     |     |     |     |     |     |     |     |
| ------------------ | --- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ing.ICSLP.
larity.SemEval-12.
|     |     |     |     |     |     | Collobert,R.andJ.Weston.2007. |     |     | Fastsemanticextraction |     |     |
| --- | --- | --- | --- | --- | --- | ----------------------------- | --- | --- | ---------------------- | --- | --- |
Antoniak,M.andD.Mimno.2018. Evaluatingthestability usinganovelneuralnetworkarchitecture.ACL.
ofembedding-basedwordsimilarities.TACL,6:107–119.
Collobert,R.andJ.Weston.2008.Aunifiedarchitecturefor
Bellegarda,J.R.1997.Alatentsemanticanalysisframework
|     |     |     |     |     |     | naturallanguageprocessing: |     |     | Deepneuralnetworkswith |     |     |
| --- | --- | --- | --- | --- | --- | -------------------------- | --- | --- | ---------------------- | --- | --- |
forlarge-spanlanguagemodeling.EUROSPEECH.
multitasklearning.ICML.
| Bellegarda,J.R.2000.               |     | Exploitinglatentsemanticinforma- |     |                  |     |                                |        |         |            |                 |            |
| ---------------------------------- | --- | -------------------------------- | --- | ---------------- | --- | ------------------------------ | ------ | ------- | ---------- | --------------- | ---------- |
|                                    |     |                                  |     |                  |     | Collobert,                     | R., J. | Weston, | L. Bottou, |                 | M. Karlen, |
| tioninstatisticallanguagemodeling. |     |                                  |     | Proceedingsofthe |     |                                |        |         |            |                 |            |
|                                    |     |                                  |     |                  |     | K.Kavukcuoglu,andP.Kuksa.2011. |        |         |            | Naturallanguage |            |
IEEE,89(8):1279–1296.
processing(almost)fromscratch.JMLR,12:2493–2537.
Bender,E.M.andA.Koller.2020.ClimbingtowardsNLU:
Cordier,B.1965.Factor-analysisofcorrespondences.COL-
Onmeaning,form,andunderstandingintheageofdata.
ING1965.
ACL.
Bengio,Y.,A.Courville,andP.Vincent.2013. Represen- Crawford, K. 2017. The trouble with bias. Keynote at
| tationlearning: |     | Areviewandnewperspectives. |     |     | IEEE | NeurIPS. |     |     |     |     |     |
| --------------- | --- | -------------------------- | --- | --- | ---- | -------- | --- | --- | --- | --- | --- |
Transactions on Pattern Analysis and Machine Intelli- Cruse,D.A.2004. MeaninginLanguage: anIntroduction
gence,35(8):1798–1828. toSemanticsandPragmatics. OxfordUniversityPress.
| Bengio,Y.,R.Ducharme,P.Vincent,andC.Jauvin.2003. |     |     |     |     |     | Secondedition. |     |     |     |     |     |
| ------------------------------------------------ | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- |
Aneuralprobabilisticlanguagemodel. JMLR,3:1137– Davies, M. 2012. Expanding horizons in historical lin-
| 1155. |     |     |     |     |     | guisticswiththe400-millionwordCorpusofHistorical |     |     |     |     |     |
| ----- | --- | --- | --- | --- | --- | ------------------------------------------------ | --- | --- | --- | --- | --- |
Bengio,Y.,H.Schwenk,J.-S.Sene´cal,F.Morin,andJ.-L. AmericanEnglish.Corpora,7(2):121–157.
Gauvain.2006.Neuralprobabilisticlanguagemodels.In
|     |     |     |     |     |     | Davies,M.2015. | TheWikipediaCorpus: |     |     | 4.6millionarti- |     |
| --- | --- | --- | --- | --- | --- | -------------- | ------------------- | --- | --- | --------------- | --- |
InnovationsinMachineLearning,137–186.Springer.
cles,1.9billionwords.AdaptedfromWikipedia.https:
//www.english-corpora.org/wiki/.
Bisk,Y.,A.Holtzman,J.Thomason,J.Andreas,Y.Bengio,
J.Chai,M.Lapata,A.Lazaridou,J.May,A.Nisnevich,
Deerwester,S.C.,S.T.Dumais,G.W.Furnas,R.A.Harsh-
| N.Pinto,andJ.Turian.2020. |     |     | Experiencegroundslan- |     |     |     |     |     |     |     |     |
| ------------------------- | --- | --- | --------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
man,T.K.Landauer,K.E.Lochbaum,andL.Streeter.
guage.EMNLP.
1988.Computerinformationretrievalusinglatentseman-
| Blei,D.M.,A.Y.Ng,andM.I.Jordan.2003.LatentDirich- |     |     |     |     |     | ticstructure:USPatent4,839,853. |     |     |     |     |     |
| ------------------------------------------------- | --- | --- | --- | --- | --- | ------------------------------- | --- | --- | --- | --- | --- |
letallocation.JMLR,3(5):993–1022.
Deerwester,S.C.,S.T.Dumais,T.K.Landauer,G.W.Fur-
Blodgett,S.L.,S.Barocas,H.Daume´III,andH.Wallach. nas,andR.A.Harshman.1990. Indexingbylatentse-
| 2020. Language(technology)ispower:Acriticalsurvey |     |     |     |     |     | manticsanalysis.JASIS,41(6):391–407. |     |     |     |     |     |
| ------------------------------------------------- | --- | --- | --- | --- | --- | ------------------------------------ | --- | --- | --- | --- | --- |
of“bias”inNLP.ACL. Ethayarajh,K.,D.Duvenaud,andG.Hirst.2019a. Towards
Bojanowski,P.,E.Grave,A.Joulin,andT.Mikolov.2017. understandinglinearwordanalogies.ACL.
Enrichingwordvectorswithsubwordinformation.TACL,
|     |     |     |     |     |     | Ethayarajh,K.,D.Duvenaud,andG.Hirst.2019b. |     |     |     |     | Under- |
| --- | --- | --- | --- | --- | --- | ------------------------------------------ | --- | --- | --- | --- | ------ |
5:135–146.
standingundesirablewordembeddingassociations.ACL.
Bolukbasi,T.,K.-W.Chang,J.Zou,V.Saligrama,andA.T.
|             |                                  |     |     |     |     | Finkelstein, | L., E.      | Gabrilovich, | Y.         | Matias, | E. Rivlin, |
| ----------- | -------------------------------- | --- | --- | --- | --- | ------------ | ----------- | ------------ | ---------- | ------- | ---------- |
| Kalai.2016. | Manistocomputerprogrammeraswoman |     |     |     |     |              |             |              |            |         |            |
|             |                                  |     |     |     |     | Z. Solan,    | G. Wolfman, | and          | E. Ruppin. | 2002.   | Placing    |
istohomemaker?Debiasingwordembeddings.NeurIPS.
|     |     |     |     |     |     | search in | context: | The concept | revisited. |     | ACM Trans- |
| --- | --- | --- | --- | --- | --- | --------- | -------- | ----------- | ---------- | --- | ---------- |
Bre´al,M.1897.EssaideSe´mantique:Sciencedessignifica-
actionsonInformationSystems,20(1):116—-131.
tions.Hachette.
|             |        |           |                  |     |          | Firth, J. R. | 1957. | A synopsis | of linguistic | theory | 1930– |
| ----------- | ------ | --------- | ---------------- | --- | -------- | ------------ | ----- | ---------- | ------------- | ------ | ----- |
| Budanitsky, | A. and | G. Hirst. | 2006. Evaluating |     | WordNet- |              |       |            |               |        |       |
1955. InStudiesinLinguisticAnalysis.PhilologicalSo-
| basedmeasuresoflexicalsemanticrelatedness. |     |     |     |     | Compu- |     |     |     |     |     |     |
| ------------------------------------------ | --- | --- | --- | --- | ------ | --- | --- | --- | --- | --- | --- |
ciety.ReprintedinPalmer,F.(ed.)1968.SelectedPapers
tationalLinguistics,32(1):13–47.
ofJ.R.Firth.Longman,Harlow.
| Bullinaria, | J. A. and | J. P. Levy. | 2007. | Extracting | seman- |     |     |     |     |     |     |
| ----------- | --------- | ----------- | ----- | ---------- | ------ | --- | --- | --- | --- | --- | --- |
tic representations from word co-occurrence statistics: Garg, N., L. Schiebinger, D. Jurafsky, and J. Zou. 2018.
Wordembeddingsquantify100yearsofgenderandeth-
| A computational |     | study. | Behavior | research | methods, |                 |                                   |     |     |     |     |
| --------------- | --- | ------ | -------- | -------- | -------- | --------------- | --------------------------------- | --- | --- | --- | --- |
|                 |     |        |          |          |          | nicstereotypes. | ProceedingsoftheNationalAcademyof |     |     |     |     |
39(3):510–526.
Sciences,115(16):E3635–E3644.
| Bullinaria,J.A.andJ.P.Levy.2012. |     |     |     | Extractingsemantic |     |     |     |     |     |     |     |
| -------------------------------- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- | --- | --- |
representationsfromwordco-occurrencestatistics:stop- Girard,G.1718. Lajustessedelalanguefranc¸oise: oules
lists,stemming,andSVD. Behaviorresearchmethods, diffe´rentessignificationsdesmotsquipassentpoursyn-
| 44(3):890–907. |     |     |     |     |     | onimes.Laurentd’Houry,Paris. |     |     |     |     |     |
| -------------- | --- | --- | --- | --- | --- | ---------------------------- | --- | --- | --- | --- | --- |
Caliskan,A.,J.J.Bryson,andA.Narayanan.2017.Seman-
ticsderivedautomaticallyfromlanguagecorporacontain
human-likebiases.Science,356(6334):183–186.

| 26 Chapter5 |     | • Embeddings |     |     |     |     |     |     |     |     |     |
| ----------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Giuliano, V. E. 1965. The interpretation of word Kim, E. 2019. Optimize computational efficiency
associations. Statistical Association Methods For of skip-gram with negative sampling. https://
Mechanized Documentation. Symposium Proceed- aegis4048.github.io/optimize_computational_
ings. Washington, D.C., USA, March 17, 1964. efficiency_of_skip-gram_with_negative_
| https://nvlpubs.nist.gov/nistpubs/Legacy/ |     |     |     |     |     | sampling. |     |     |     |     |     |
| ----------------------------------------- | --- | --- | --- | --- | --- | --------- | --- | --- | --- | --- | --- |
MP/nbsmiscellaneouspub269.pdf.
|     |     |     |     |     |     | Lake, B. | M. and | G. L. Murphy. | 2021. | Word | meaning in |
| --- | --- | --- | --- | --- | --- | -------- | ------ | ------------- | ----- | ---- | ---------- |
mindsandmachines.PsychologicalReview.Inpress.
| Gladkova,A.,A.Drozd,andS.Matsuoka.2016. |     |     |     |     | Analogy- |     |     |     |     |     |     |
| --------------------------------------- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- |
baseddetectionofmorphologicalandsemanticrelations
Landauer,T.K.andS.T.Dumais.1997.AsolutiontoPlato’s
| with word | embeddings: | what | works | and what | doesn’t. |     |     |     |     |     |     |
| --------- | ----------- | ---- | ----- | -------- | -------- | --- | --- | --- | --- | --- | --- |
problem:TheLatentSemanticAnalysistheoryofacqui-
NAACLStudentResearchWorkshop.
|     |     |     |     |     |     | sition,induction,andrepresentationofknowledge. |     |     |     |     | Psy- |
| --- | --- | --- | --- | --- | --- | ---------------------------------------------- | --- | --- | --- | --- | ---- |
chologicalReview,104:211–240.
Glenberg,A.M.andD.A.Robertson.2000.Symbolground-
ingandmeaning:Acomparisonofhigh-dimensionaland Landauer,T.K.,D.Laham,B.Rehder,andM.E.Schreiner.
| embodiedtheoriesofmeaning. |     |     | Journalofmemoryand |     |     |       |                                        |     |     |     |     |
| -------------------------- | --- | --- | ------------------ | --- | --- | ----- | -------------------------------------- | --- | --- | --- | --- |
|                            |     |     |                    |     |     | 1997. | Howwellcanpassagemeaningbederivedwith- |     |     |     |     |
language,43(3):379–401.
|                             |     |     |                      |     |     | outusingwordorder?        |     | AcomparisonofLatentSemantic |     |     |     |
| --------------------------- | --- | --- | -------------------- | --- | --- | ------------------------- | --- | --------------------------- | --- | --- | --- |
| Gonen,H.andY.Goldberg.2019. |     |     | Lipstickonapig:Debi- |     |     | Analysisandhumans.COGSCI. |     |                             |     |     |     |
asingmethodscoverupsystematicgenderbiasesinword Lapesa,G.andS.Evert.2014. Alargescaleevaluationof
embeddingsbutdonotremovethem.NAACLHLT. distributionalsemanticmodels: Parameters,interactions
Gould,S.J.1980.ThePanda’sThumb.PenguinGroup. andmodelselection.TACL,2:531–545.
|            |                   |     |         |             |     | Lee, D.D.andH.S.Seung. |                 |     | 1999.  | Learningthe    | partsof |
| ---------- | ----------------- | --- | ------- | ----------- | --- | ---------------------- | --------------- | --- | ------ | -------------- | ------- |
| Greenwald, | A.G., D.E.McGhee, |     | andJ.L. | K.Schwartz. |     |                        |                 |     |        |                |         |
|            |                   |     |         |             |     | objects                | by non-negative |     | matrix | factorization. | Nature, |
1998.Measuringindividualdifferencesinimplicitcogni-
| tion:theimplicitassociationtest. |     |     | Journalofpersonality |     |     | 401(6755):788–791. |     |     |     |     |     |
| -------------------------------- | --- | --- | -------------------- | --- | --- | ------------------ | --- | --- | --- | --- | --- |
andsocialpsychology,74(6):1464–1480. Levy,O.andY.Goldberg.2014a. Dependency-basedword
embeddings.ACL.
| Hamilton, W.L., | J.Leskovec, |     | andD.Jurafsky.2016. |     | Di- |     |     |     |     |     |     |
| --------------- | ----------- | --- | ------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
achronicwordembeddingsrevealstatisticallawsofse- Levy,O.andY.Goldberg.2014b. Linguisticregularitiesin
manticchange.ACL. sparseandexplicitwordrepresentations.CoNLL.
Harris,Z.S.1954. Distributionalstructure. Word,10:146– Levy,O.andY.Goldberg.2014c. Neuralwordembedding
| 162. |     |     |     |     |     | asimplicitmatrixfactorization.NeurIPS. |     |     |     |     |     |
| ---- | --- | --- | --- | --- | --- | -------------------------------------- | --- | --- | --- | --- | --- |
Hellrich, J. and U. Hahn. 2016. Bad company— Levy,O.,Y.Goldberg,andI.Dagan.2015. Improvingdis-
Neighborhoods in neural embedding spaces considered tributionalsimilaritywithlessonslearnedfromwordem-
| harmful.COLING.                        |     |     |     |             |     | beddings.TACL,3:211–225. |               |     |           |        |            |
| -------------------------------------- | --- | --- | --- | ----------- | --- | ------------------------ | ------------- | --- | --------- | ------ | ---------- |
|                                        |     |     |     |             |     | Lin, Y.,                 | J.-B. Michel, | E.  | Lieberman | Aiden, | J. Orwant, |
| Hill,F.,R.Reichart,andA.Korhonen.2015. |     |     |     | Simlex-999: |     |                          |               |     |           |        |            |
W.Brockman,andS.Petrov.2012.Syntacticannotations
Evaluatingsemanticmodelswith(genuine)similarityes-
timation.ComputationalLinguistics,41(4):665–695. fortheGoogleBooksNGramcorpus.ACL.
Hjelmslev,L.1969. PrologomenatoaTheoryofLanguage. Linzen, T.2016. Issuesinevaluatingsemanticspacesus-
UniversityofWisconsinPress. TranslatedbyFrancisJ. ingwordanalogies. 1stWorkshoponEvaluatingVector-
SpaceRepresentationsforNLP.
Whitfield;originalDanishedition1943.
Hofmann,T.1999. Probabilisticlatentsemanticindexing. Manning,C.D.,P.Raghavan,andH.Schu¨tze.2008. Intro-
| SIGIR-99. |     |     |     |     |     | ductiontoInformationRetrieval.Cambridge. |     |     |     |     |     |
| --------- | --- | --- | --- | --- | --- | ---------------------------------------- | --- | --- | --- | --- | --- |
Mikolov,T.,K.Chen,G.S.Corrado,andJ.Dean.2013a.Ef-
Huang,E.H.,R.Socher,C.D.Manning,andA.Y.Ng.2012.
ficientestimationofwordrepresentationsinvectorspace.
| Improving                                | word representations |     | via | global context | and      |                   |                 |                                 |     |                 |     |
| ---------------------------------------- | -------------------- | --- | --- | -------------- | -------- | ----------------- | --------------- | ------------------------------- | --- | --------------- | --- |
| multiplewordprototypes.ACL.              |                      |     |     |                |          | ICLR2013.         |                 |                                 |     |                 |     |
|                                          |                      |     |     |                |          | Mikolov,          | T., S.Kombrink, | L.Burget,                       |     | J.H.Cˇernocky`, | and |
| Jia,S.,T.Meng,J.Zhao,andK.-W.Chang.2020. |                      |     |     |                | Mitigat- |                   |                 |                                 |     |                 |     |
|                                          |                      |     |     |                |          | S.Khudanpur.2011. |                 | Extensionsofrecurrentneuralnet- |     |                 |     |
inggenderbiasamplificationindistributionbyposterior
worklanguagemodel.ICASSP.
regularization.ACL.
Jones,M.P.andJ.H.Martin.1997.Contextualspellingcor- Mikolov, T., I. Sutskever, K. Chen, G. S. Corrado, and
J.Dean.2013b.Distributedrepresentationsofwordsand
rectionusinglatentsemanticanalysis.ANLP.
phrasesandtheircompositionality.NeurIPS.
| Joos, M. 1950. | Description |     | of language | design. | JASA, |          |           |          |           |        |          |
| -------------- | ----------- | --- | ----------- | ------- | ----- | -------- | --------- | -------- | --------- | ------ | -------- |
|                |             |     |             |         |       | Mikolov, | T., W.-t. | Yih, and | G. Zweig. | 2013c. | Linguis- |
22:701–708.
ticregularitiesincontinuousspacewordrepresentations.
| Jurgens,D.,S.M.Mohammad,P.Turney,andK.Holyoak. |     |     |                         |     |     | NAACLHLT. |     |     |     |     |     |
| ---------------------------------------------- | --- | --- | ----------------------- | --- | --- | --------- | --- | --- | --- | --- | --- |
| 2012. SemEval-2012task2:                       |     |     | Measuringdegreesofrela- |     |     |           |     |     |     |     |     |
Nosek,B.A.,M.R.Banaji,andA.G.Greenwald.2002a.
tionalsimilarity.*SEM2012.
|     |     |     |     |     |     | Harvesting | implicit | group | attitudes | and beliefs | from a |
| --- | --- | --- | --- | --- | --- | ---------- | -------- | ----- | --------- | ----------- | ------ |
Katz,J.J.andJ.A.Fodor.1963.Thestructureofasemantic
|     |     |     |     |     |     | demonstrationwebsite. |     |     | GroupDynamics: |     | Theory,Re- |
| --- | --- | --- | --- | --- | --- | --------------------- | --- | --- | -------------- | --- | ---------- |
theory.Language,39:170–210.
search,andPractice,6(1):101.
Kiela,D.andS.Clark.2014.Asystematicstudyofsemantic Nosek,B.A.,M.R.Banaji,andA.G.Greenwald.2002b.
vectorspacemodelparameters. EACL2ndWorkshopon Math=male,me=female,thereforemath(cid:54)=me.Journalof
ContinuousVectorSpaceModelsandtheirComposition-
personalityandsocialpsychology,83(1):44.
ality(CVSC).
Osgood,C.E.,G.J.Suci,andP.H.Tannenbaum.1957.The
MeasurementofMeaning.UniversityofIllinoisPress.

Exercises 27
Pennington,J.,R.Socher,andC.D.Manning.2014.GloVe: Turney,P.D.andM.L.Littman.2005. Corpus-basedlearn-
Globalvectorsforwordrepresentation.EMNLP. ingofanalogiesandsemanticrelations. MachineLearn-
ing,60(1-3):251–278.
Peterson,J.C.,D.Chen,andT.L.Griffiths.2020.Parallelo-
gramsrevisited:Exploringthelimitationsofvectorspace vanderMaaten,L.andG.E.Hinton.2008.Visualizinghigh-
modelsforsimpleanalogies.Cognition,205. dimensionaldatausingt-SNE.JMLR,9:2579–2605.
Pilehvar,M.T.andJ.Camacho-Collados.2019. WiC:the Wierzbicka, A.1992. Semantics, Culture, andCognition:
word-in-context dataset for evaluating context-sensitive UniversityHumanConceptsinCulture-SpecificConfigu-
| meaningrepresentations.NAACLHLT. |     |     |     |     | rations.OxfordUniversityPress. |
| -------------------------------- | --- | --- | --- | --- | ------------------------------ |
Rehder, B., M. E. Schreiner, M. B. W. Wolfe, D. Laham, Semantics: PrimesandUniversals.
|                                    |     |                 |               |        | Wierzbicka, A.1996.    |
| ---------------------------------- | --- | --------------- | ------------- | ------ | ---------------------- |
| T. K. Landauer,                    |     | and W. Kintsch. | 1998. Using   | Latent | OxfordUniversityPress. |
| SemanticAnalysistoassessknowledge: |     |                 | Sometechnical |        |                        |
Wittgenstein,L.1953.PhilosophicalInvestigations.(Trans-
considerations.DiscourseProcesses,25(2-3):337–354.
latedbyAnscombe,G.E.M.).Blackwell.
Rohde,D.L.T.,L.M.Gonnerman,andD.C.Plaut.2006. Zhao, J., T. Wang, M. Yatskar, V. Ordonez, and K.-
Animprovedmodelofsemanticsimilaritybasedonlexi- W. Chang. 2017. Men also like shopping: Reducing
calco-occurrence.CACM,8:627–633.
genderbiasamplificationusingcorpus-levelconstraints.
| Rumelhart,D.E.andA.A.Abrahamson.1973.Amodelfor |     |     |     |     | EMNLP. |
| ---------------------------------------------- | --- | --- | --- | --- | ------ |
analogicalreasoning.CognitivePsychology,5(1):1–28. Zhao,J.,Y.Zhou,Z.Li,W.Wang,andK.-W.Chang.2018.
Salton,G.1971.TheSMARTRetrievalSystem:Experiments Learninggender-neutralwordembeddings.EMNLP.
inAutomaticDocumentProcessing.PrenticeHall.
Schluter,N.2018.Thewordanalogytestingcaveat.NAACL
HLT.
| Schone,P.andD.Jurafsky.2000. |     |     | Knowlege-freeinduction |     |     |
| ---------------------------- | --- | --- | ---------------------- | --- | --- |
ofmorphologyusinglatentsemanticanalysis.CoNLL.
| Schone, P. | and D. Jurafsky. | 2001a. | Is knowledge-free | in- |     |
| ---------- | ---------------- | ------ | ----------------- | --- | --- |
ductionofmultiwordunitdictionaryheadwordsasolved
| problem?                      | EMNLP. |     |                      |     |     |
| ----------------------------- | ------ | --- | -------------------- | --- | --- |
| Schone,P.andD.Jurafsky.2001b. |        |     | Knowledge-freeinduc- |     |     |
tionofinflectionalmorphologies.NAACL.
| Schu¨tze,H.1992. | Dimensionsofmeaning. |     | Proceedingsof |     |     |
| ---------------- | -------------------- | --- | ------------- | --- | --- |
Supercomputing’92.IEEEPress.
Schu¨tze,H.1997.AmbiguityResolutioninLanguageLearn-
| ing–ComputationalandCognitiveModels. |     |     |     | CSLI,Stan- |     |
| ------------------------------------ | --- | --- | --- | ---------- | --- |
ford,CA.
| Schu¨tze,H.,D.A.Hull,andJ.Pedersen.1995. |     |     |     | Acompar- |     |
| ---------------------------------------- | --- | --- | --- | -------- | --- |
isonofclassifiersanddocumentrepresentationsforthe
routingproblem.SIGIR-95.
| Schu¨tze,H.andJ.Pedersen.1993.      |     |     | Avectormodelforsyn- |     |     |
| ----------------------------------- | --- | --- | ------------------- | --- | --- |
| tagmaticandparadigmaticrelatedness. |     |     | 9thAnnualCon-       |     |     |
ferenceoftheUWCentrefortheNewOEDandTextRe-
search.
| SparckJones,K.1972. |     | Astatisticalinterpretationofterm |     |     |     |
| ------------------- | --- | -------------------------------- | --- | --- | --- |
specificityanditsapplicationinretrieval.JournalofDoc-
umentation,28(1):11–21.
| SparckJones,K.1986. |     | SynonymyandSemanticClassifica- |     |     |     |
| ------------------- | --- | ------------------------------ | --- | --- | --- |
tion.EdinburghUniversityPress,Edinburgh.Republica-
tionof1964PhDThesis.
| Switzer, P.       | 1965.       | Vector images             | in document    | retrieval. |     |
| ----------------- | ----------- | ------------------------- | -------------- | ---------- | --- |
| Statistical       | Association | Methods                   | For Mechanized | Docu-      |     |
| mentation.        | Symposium   | Proceedings.              | Washington,    | D.C.,      |     |
| USA,March17,1964. |             | https://nvlpubs.nist.gov/ |                |            |     |
nistpubs/Legacy/MP/nbsmiscellaneouspub269.
pdf.
| Tian,Y.,V.Kulkarni,B.Perozzi,andS.Skiena.2016. |            |     |                | On       |     |
| ---------------------------------------------- | ---------- | --- | -------------- | -------- | --- |
| the convergent                                 | properties | of  | word embedding | methods. |     |
ArXivpreprintarXiv:1605.03956.
| Turian,J.,L.Ratinov,andY.Bengio.2010. |     |     | Wordrepresen- |     |     |
| ------------------------------------- | --- | --- | ------------- | --- | --- |
tations:asimpleandgeneralmethodforsemi-supervised
learning.ACL.
