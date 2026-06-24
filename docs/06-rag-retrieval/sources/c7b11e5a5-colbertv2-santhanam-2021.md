ColBERTv2:
Effective and Efficient Retrieval via Lightweight Late Interaction
|     | KeshavSanthanam∗ |     |     |     |     | OmarKhattab∗ |     |     | JonSaad-Falcon |     |     |     |
| --- | ---------------- | --- | --- | --- | --- | ------------ | --- | --- | -------------- | --- | --- | --- |
StanfordUniversity StanfordUniversity GeorgiaInstituteofTechnology
|     |                    |     | ChristopherPotts   |      |     |         |                                         | MateiZaharia       |       |          |          |      |
| --- | ------------------ | --- | ------------------ | ---- | --- | ------- | --------------------------------------- | ------------------ | ----- | -------- | -------- | ---- |
|     |                    |     | StanfordUniversity |      |     |         |                                         | StanfordUniversity |       |          |          |      |
|     |                    |     | Abstract           |      |     |         | relevance                               | is estimated       | using | rich yet | scalable | in-  |
|     |                    |     |                    |      |     |         | teractionsbetweenthesetwosetsofvectors. |                    |       |          |          | Col- |
|     | Neural information |     | retrieval          | (IR) | has | greatly |                                         |                    |       |          |          |      |
BERTproducesanembeddingforeverytokenin
|     | advanced  | search   | and    | other | knowledge- |        |           |                |     |            |           |     |
| --- | --------- | -------- | ------ | ----- | ---------- | ------ | --------- | -------------- | --- | ---------- | --------- | --- |
|     |           |          |        |       |            |        | the query | (and document) |     | and models | relevance |     |
|     | intensive | language | tasks. | While | many       | neural |           |                |     |            |           |     |
IR methods encode queries and documents asthesumofmaximumsimilaritiesbetweeneach
2202 luJ 01  ]RI.sc[  3v88410.2112:viXra
into single-vector representations, late queryvectorandallvectorsinthedocument.
interactionmodelsproducemulti-vectorrepre- Bydecomposingrelevancemodelingintotoken-
sentationsatthegranularityofeachtokenand
levelcomputations,lateinteractionaimstoreduce
|     | decompose | relevance | modeling |     | into | scalable |                        |     |     |                      |     |     |
| --- | --------- | --------- | -------- | --- | ---- | -------- | ---------------------- | --- | --- | -------------------- | --- | --- |
|     |           |           |          |     |      |          | theburdenontheencoder: |     |     | whereassingle-vector |     |     |
token-levelcomputations.Thisdecomposition
modelsmustcapturecomplexquery–documentre-
hasbeenshowntomakelateinteractionmore
lationshipswithinonedotproduct,lateinteraction
|     | effective, | but it | inflates | the space | footprint | of  |     |     |     |     |     |     |
| --- | ---------- | ------ | -------- | --------- | --------- | --- | --- | --- | --- | --- | --- | --- |
thesemodelsbyanorderofmagnitude. Inthis encodes meaning at the level of tokens and del-
work, we introduce ColBERTv2, a retriever egates query–document matching to the interac-
that couples an aggressive residual compres- tion mechanism. This added expressivity comes
sion mechanism with a denoised supervision atacost: existinglateinteractionsystemsimpose
strategytosimultaneouslyimprovethequality
anorder-of-magnitudelargerspacefootprintthan
|     | and space      | footprint | of           | late interaction. |                  | We    |               |                 |           |              |       |          |
| --- | -------------- | --------- | ------------ | ----------------- | ---------------- | ----- | ------------- | --------------- | --------- | ------------ | ----- | -------- |
|     |                |           |              |                   |                  |       | single-vector | models,         | as        | they must    | store | billions |
|     | evaluate       | ColBERTv2 |              | across            | a wide           | range |               |                 |           |              |       |          |
|     |                |           |              |                   |                  |       | of small      | vectors for     | Web-scale | collections. |       | Con-     |
|     | of benchmarks, |           | establishing |                   | state-of-the-art |       |               |                 |           |              |       |          |
|     |                |           |              |                   |                  |       | sidering      | this challenge, | it        | might seem   | more  | fruit-   |
qualitywithinandoutsidethetrainingdomain
while reducing the space footprint of late ful to focus instead on addressing the fragility of
interactionmodelsby6–10×. single-vector models (Menon et al., 2022) by in-
troducingnewsupervisionparadigmsfornegative
1 Introduction
mining(Xiongetal.,2020),pretraining(Gaoand
|     |     |     |     |     |     |     | Callan, 2021), | and | distillation | (Qu | et al., | 2021). |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ------------ | --- | ------- | ------ |
Neuralinformationretrieval(IR)hasquicklydomi-
natedthesearchlandscapeoverthepast2–3years, Indeed, recent single-vector models with highly-
dramaticallyadvancingnotonlypassageanddoc- tunedsupervisionstrategies(Renetal.,2021b;For-
ument search (Nogueira and Cho, 2019) but also mal et al., 2021a) sometimes perform on-par or
evenbetterthan“vanilla”lateinteractionmodels,
| many | knowledge-intensive |     |     | NLP | tasks | like open- |     |     |     |     |     |     |
| ---- | ------------------- | --- | --- | --- | ----- | ---------- | --- | --- | --- | --- | --- | --- |
domain question answering (Guu et al., 2020), and it is not necessarily clear whether late inter-
multi-hopclaimverification(Khattabetal.,2021a), actionarchitectures—withtheirfixedtoken-level
inductivebiases—admitsimilarlylargegainsfrom
andopen-endedgeneration(Paranjapeetal.,2022).
|     | ManyneuralIRmethodsfollowasingle-vector |     |     |     |     |     | improvedsupervision. |     |     |     |     |     |
| --- | --------------------------------------- | --- | --- | --- | --- | --- | -------------------- | --- | --- | --- | --- | --- |
similarityparadigm: apretrainedlanguagemodel In this work, we show that late interaction re-
is used to encode each query and each document trievers naturally produce lightweight token rep-
into a single high-dimensional vector, and rele- resentationsthatareamenabletoefficientstorage
vanceismodeledasasimpledotproductbetween off-the-shelf and that they can benefit drastically
bothvectors. Analternativeislateinteraction,in- from denoised supervision. We couple those in
|     |     |     |     |     |     |     | ColBERTv2,1 | anewlate-interactionretrieverthat |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | --------------------------------- | --- | --- | --- | --- |
troducedinColBERT(KhattabandZaharia,2020),
wherequeriesanddocumentsareencodedatafiner- employsasimplecombinationofdistillationfrom
granularityintomulti-vectorrepresentations,and
1Code,models,andLoTTEdataaremaintainedathttps:
∗Equalcontribution.
//github.com/stanford-futuredata/ColBERT

2 Background&RelatedWork
| a cross-encoder | and hard-negative |     | mining | (§3.2) |     |     |     |     |     |     |     |
| --------------- | ----------------- | --- | ------ | ------ | --- | --- | --- | --- | --- | --- | --- |
toboostqualitybeyondanyexistingmethod,and
2.1 Token-DecomposedScoringinNeuralIR
thenusesaresidualcompressionmechanism(§3.3)
|     |     |     |     |     | Many neural | IR  | approaches |     | encode | passages | as  |
| --- | --- | --- | --- | --- | ----------- | --- | ---------- | --- | ------ | -------- | --- |
toreducethespacefootprintoflateinteractionby
6–10×whilepreservingquality. Asaresult,Col- a single high-dimensional vector, trading off the
BERTv2establishesstate-of-the-artretrievalqual- higherqualityofcross-encodersforimprovedef-
itybothwithinandoutsideitstrainingdomainwith ficiency and scalability (Karpukhin et al., 2020;
|               |                 |     |              |         | Xiong et        | al., 2020; | Qu  | et       | al.,  | 2021). | Col-   |
| ------------- | --------------- | --- | ------------ | ------- | --------------- | ---------- | --- | -------- | ----- | ------ | ------ |
| a competitive | space footprint |     | with typical | single- |                 |            |     |          |       |        |        |
| vectormodels. |                 |     |              |         | BERT’s (Khattab |            | and | Zaharia, | 2020) | late   | inter- |
When trained on MS MARCO Passage Rank- action paradigm addresses this tradeoff by com-
putingmulti-vectorembeddingsandusingascal-
ing,ColBERTv2achievesthehighestMRR@10of
|                         |     |                       |     |     | able “MaxSim” |          | operator | for          | retrieval. |             | Several |
| ----------------------- | --- | --------------------- | --- | --- | ------------- | -------- | -------- | ------------ | ---------- | ----------- | ------- |
| anystandaloneretriever. |     | Inadditiontoin-domain |     |     |               |          |          |              |            |             |         |
|                         |     |                       |     |     | other systems | leverage |          | multi-vector |            | representa- |         |
quality,weseekaretrieverthatgeneralizes“zero-
shot”todomain-specificcorporaandlong-tailtop- tions, including Poly-encoders (Humeau et al.,
|     |     |     |     |     | 2020), PreTTR |     | (MacAvaney |     | et al., | 2020), | and |
| --- | --- | --- | --- | --- | ------------- | --- | ---------- | --- | ------- | ------ | --- |
ics,onesthatareoftenunder-representedinlarge
|                     |                          |     |     |     | MORES | (Gao | et al., | 2020), | but | these | target |
| ------------------- | ------------------------ | --- | --- | --- | ----- | ---- | ------- | ------ | --- | ----- | ------ |
| publictrainingsets. | Tothisend,weevaluateCol- |     |     |     |       |      |         |        |     |       |        |
BERTv2onawidearrayofout-of-domainbench- attention-based re-ranking as opposed to Col-
BERT’sscalableMaxSimend-to-endretrieval.
| marks. | These include | three Wikipedia |     | Open-QA |     |     |     |     |     |     |     |
| ------ | ------------- | --------------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
ME-BERT(Luanetal.,2021)generatestoken-
retrievaltestsand13diverseretrievalandsemantic-
similaritytasksfromBEIR(Thakuretal.,2021). In level document embeddings similar to ColBERT,
addition,weintroduceanewbenchmark,dubbed butretainsasingleembeddingvectorforqueries.
COIL(Gaoetal.,2021)alsogeneratestoken-level
LoTTE,forLong-TailTopic-stratifiedEvaluation
documentembeddings,butthetokeninteractions
| for IR | that features | 12 domain-specific |     | search |     |     |     |     |     |     |     |
| ------ | ------------- | ------------------ | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
tests, spanning StackExchange communities and are restricted to lexical matching between query
|     |     |     |     |     | anddocumentterms. |     | uniCOIL(LinandMa,2021) |     |     |     |     |
| --- | --- | --- | --- | --- | ----------------- | --- | ---------------------- | --- | --- | --- | --- |
usingqueriesfromGooAQ(Khashabietal.,2021).
|       |                       |     |           |           | limits the | token | embedding | vectors |     | of COIL | to a |
| ----- | --------------------- | --- | --------- | --------- | ---------- | ----- | --------- | ------- | --- | ------- | ---- |
| LoTTE | focuses on relatively |     | long-tail | topics in |            |       |           |         |     |         |      |
itspassages, unliketheOpen-QAtestsandmany singledimension,reducingthemtoscalarweights
thatextendmodelslikeDeepCT(DaiandCallan,
| of the BEIR | tasks, and        | evaluates | models  | on their |                |            |     |         |     |             |         |
| ----------- | ----------------- | --------- | ------- | -------- | -------------- | ---------- | --- | ------- | --- | ----------- | ------- |
|             |                   |           |         |          | 2020) and      | DeepImpact |     | (Mallia | et  | al., 2021). | To      |
| capacity    | to answer natural | search    | queries | with a   |                |            |     |         |     |             |         |
|             |                   |           |         |          | produce scalar | weights,   |     | SPLADE  |     | (Formal     | et al., |
practicalintent,unlikemanyofBEIR’ssemantic-
similaritytasks. On22of28out-of-domaintests, 2021b)andSPLADEv2(Formaletal.,2021a)pro-
duceasparsevocabulary-levelvectorthatretains
| ColBERTv2 | achieves | the highest | quality, | outper- |                |               |     |     |         |             |     |
| --------- | -------- | ----------- | -------- | ------- | -------------- | ------------- | --- | --- | ------- | ----------- | --- |
|           |          |             |          |         | the term-level | decomposition |     |     | of late | interaction |     |
formingthenextbestretrieverbyupto8%relative
gain,whileusingitscompressedrepresentations. whilesimplifyingthestorageintoonedimension
|     |     |     |     |     | pertoken. | TheSPLADEfamilyalsopiggybackson |     |     |     |     |     |
| --- | --- | --- | --- | --- | --------- | ------------------------------- | --- | --- | --- | --- | --- |
Thisworkmakesthefollowingcontributions:
thelanguagemodelingcapacityacquiredbyBERT
|     |     |     |     |     | during pretraining. |     | SPLADEv2 |     | has | been | shown |
| --- | --- | --- | --- | --- | ------------------- | --- | -------- | --- | --- | ---- | ----- |
1. WeproposeColBERTv2,aretrieverthatcom-
tobehighlyeffective,withinandacrossdomains,
binesdenoisedsupervisionandresidualcom-
anditisacentralpointofcomparisonintheexper-
| pression, | leveraging | the | token-level | decom- |     |     |     |     |     |     |     |
| --------- | ---------- | --- | ----------- | ------ | --- | --- | --- | --- | --- | --- | --- |
imentswereportoninthispaper.
| position | of late | interaction | to achieve | high |     |     |     |     |     |     |     |
| -------- | ------- | ----------- | ---------- | ---- | --- | --- | --- | --- | --- | --- | --- |
robustnesswithareducedspacefootprint. 2.2 VectorCompressionforNeuralIR
|     |     |     |     |     | There has | been | a surge | of recent | interest |     | in com- |
| --- | --- | --- | --- | --- | --------- | ---- | ------- | --------- | -------- | --- | ------- |
2. WeintroduceLoTTE,anewresourceforout-
pressingrepresentationsforIR.Izacardetal.(2020)
| of-domainevaluationofretrievers. |     |     |     | LoTTEfo- |     |     |     |     |     |     |     |
| -------------------------------- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
exploredimensionreduction,productquantization
cusesonnaturalinformation-seekingqueries (PQ),andpassagefilteringforsingle-vectorretriev-
overlong-tailtopics,animportantyetunder- ers. BPR(Yamadaetal.,2021a)learnstodirectly
studiedapplicationspace.
hashembeddingstobinarycodesusingadifferen-
|     |     |     |     |     | tiabletanhfunction. |     | JPQ(Zhanetal.,2021a)and |     |     |     |     |
| --- | --- | --- | --- | --- | ------------------- | --- | ----------------------- | --- | --- | --- | --- |
3. WeevaluateColBERTv2acrossawiderange its extension, RepCONC (Zhan et al., 2022), use
ofsettings,establishingstate-of-the-artqual- PQtocompressembeddings,andjointlytrainthe
itywithinandoutsidethetrainingdomain. queryencoderalongwiththecentroidsproduced

| byPQviaaranking-orientedloss. |     |     |     |     |     |     |     | score |     |
| ----------------------------- | --- | --- | --- | --- | --- | --- | --- | ----- | --- |
SDR(Cohenetal.,2021)usesanautoencoderto
reducethedimensionalityofthecontextualembed- MaxSim MaxSim MaxSim
dingsusedforattention-basedre-rankingandthen
appliesaquantizationschemeforfurthercompres- gnixednI enilffO
sion. DensePhrases(Leeetal.,2021a)isasystem Question Encoder Passage Encoder
| for Open-QA | that relies      | on a multi-vector |     | encod-    |     |          |     |         |     |
| ----------- | ---------------- | ----------------- | --- | --------- | --- | -------- | --- | ------- | --- |
| ing of      | passages, though | its search        | is  | conducted |     |          |     |         |     |
|             |                  |                   |     |           |     | Question |     | Passage |     |
at the level of individual vectors and not aggre- Figure 1: The late interaction architecture, given a
| gatedwithlateinteraction. |     | Veryrecently,Leeetal. |     |     |           |            |         |              |        |
| ------------------------- | --- | --------------------- | --- | --- | --------- | ---------- | ------- | ------------ | ------ |
|                           |     |                       |     |     | query and | a passage. | Diagram | from Khattab | et al. |
(2021b) propose a quantization-aware finetuning (2021b)withpermission.
methodbasedonPQtoreducethespacefootprint
2.4 Out-of-DomainEvaluationinIR
| ofDensePhrases. | WhileDensePhrasesiseffective |     |     |     |     |     |     |     |     |
| --------------- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
atOpen-QA,itsretrievalquality—asmeasuredby
Recentprogressinretrievalhasmostlyfocusedon
top-20retrievalaccuracyonNaturalQuestionsand
|     |     |     |     |     | large-data | evaluation, | where | many tens | of thou- |
| --- | --- | --- | --- | --- | ---------- | ----------- | ----- | --------- | -------- |
TriviaQA—is competitive with DPR (Karpukhin sandsofannotatedtrainingqueriesareassociated
| et al., 2020) | and considerably |     | less effective | than |     |     |     |     |     |
| ------------- | ---------------- | --- | -------------- | ---- | --- | --- | --- | --- | --- |
withthetestdomain,asinMSMARCOorNatu-
ColBERT(Khattabetal.,2021b).
|     |     |     |     |     | ralQuestions(Kwiatkowskietal.,2019). |     |     |     | Inthese |
| --- | --- | --- | --- | --- | ------------------------------------ | --- | --- | --- | ------- |
In this work, we focus on late-interaction re- benchmarks,queriestendtoreflecthigh-popularity
trievalandinvestigatecompressionusingaresidual topics like movies and athletes in Wikipedia. In
compressionapproachthatcanbeappliedoff-the- practice,user-facingIRandQAapplicationsoften
| shelf to | late interaction | models, | without | special |     |     |     |     |     |
| -------- | ---------------- | ------- | ------- | ------- | --- | --- | --- | --- | --- |
pertaintodomain-specificcorpora,forwhichlittle
training. WeshowinAppendixAthatColBERT’s to no training data is available and whose topics
representationsnaturallylendthemselvestoresid- areunder-representedinlargepubliccollections.
| ualcompression. | Techniquesinthefamilyofresid- |     |     |     |     |     |     |     |     |
| --------------- | ----------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
Thisout-of-domainregimehasreceivedrecent
| ual compression | are | well-studied | (Barnes | et al., |     |     |     |     |     |
| --------------- | --- | ------------ | ------- | ------- | --- | --- | --- | --- | --- |
attentionwiththeBEIR(Thakuretal.,2021)bench-
1996)andhavepreviouslybeenappliedacrosssev- mark. BEIR combines several existing datasets
eraldomains,includingapproximatenearestneigh-
intoaheterogeneoussuitefor“zero-shotIR”tasks,
borsearch(Weietal.,2014;Aietal.,2017),neural
spanningbio-medical,financial,andscientificdo-
networkparameterandactivationquantization(Li mains. While the BEIR datasets provide a use-
etal.,2021b,a),anddistributeddeeplearning(Chen fultestbed,manycapturebroadsemanticrelated-
| et al., 2018; | Liu et al., | 2020). | To the | best of our |                 |            |     |                    |     |
| ------------- | ----------- | ------ | ------ | ----------- | --------------- | ---------- | --- | ------------------ | --- |
|               |             |        |        |             | ness tasks—like | citations, |     | counter arguments, | or  |
knowledge,ColBERTv2isthefirstapproachtouse duplicatequestions–insteadofnaturalsearchtasks,
residualcompressionforscalableneuralIR. orelsetheyfocusonhigh-popularityentitieslike
|     |     |     |     |     | thoseinWikipedia. |     | In§4,weintroduceLoTTE,a |     |     |
| --- | --- | --- | --- | --- | ----------------- | --- | ----------------------- | --- | --- |
2.3 ImprovingtheQualityofSingle-Vector
newdatasetforout-of-domainretrieval,exhibiting
| Representations |                |              |     |             | naturalsearchqueriesoverlong-tailtopics. |     |     |     |     |
| --------------- | -------------- | ------------ | --- | ----------- | ---------------------------------------- | --- | --- | --- | --- |
| Instead         | of compressing | multi-vector |     | representa- |                                          |     |     |     |     |
3 ColBERTv2
| tions as | we do, much | recent | work has | focused |     |     |     |     |     |
| -------- | ----------- | ------ | -------- | ------- | --- | --- | --- | --- | --- |
on improving the quality of single-vector mod- We now introduce ColBERTv2, which improves
els,whichareoftenverysensitivetothespecifics thequalityofmulti-vectorretrievalmodels(§3.2)
of supervision. This line of work can be decom- whilereducingtheirspacefootprint(§3.3).
| posedintothreedirections: |     | (1)distillationofmore |     |     |     |     |     |     |     |
| ------------------------- | --- | --------------------- | --- | --- | --- | --- | --- | --- | --- |
3.1 Modeling
| expressive | architectures | (Hofstätter | et  | al., 2020; |     |     |     |     |     |
| ---------- | ------------- | ----------- | --- | ---------- | --- | --- | --- | --- | --- |
Linetal.,2020)includingexplicitdenoising(Qu ColBERTv2adoptsthelateinteractionarchitecture
et al., 2021; Ren et al., 2021b), (2) hard negative ofColBERT,depictedinFigure1. Queriesandpas-
sampling (Xiong et al., 2020; Zhan et al., 2020a, sagesareindependentlyencodedwithBERT(De-
2021b), and (3) improved pretraining (Gao and vlinetal.,2019),andtheoutputembeddingsencod-
Callan,2021;Og˘uzetal.,2021). Weadoptsimilar ingeachtokenareprojectedtoalowerdimension.
techniquesto(1)and(2)forColBERTv2’smulti- During offline indexing, every passage d in the
vectorrepresentations(see§3.2). corpusisencodedintoasetofvectors,andthese

vectors are stored. At search time, the query q is KL-Divergencelosstodistillthecross-encoder’s
encodedintoamulti-vectorrepresentation,andits scoresintotheColBERTarchitecture. WeuseKL-
similaritytoapassagediscomputedasthesumma- DivergenceasColBERTproducesscores(i.e.,the
tionofquery-side“MaxSim”operations,namely, sumofcosinesimilarities)witharestrictedscale,
thelargestcosinesimilaritybetweeneachqueryto- whichmaynotaligndirectlywiththeoutputscores
kenembeddingandallpassagetokenembeddings: of the cross-encoder. We also employ in-batch
negativesperGPU,whereacross-entropylossis
N
|     |     | (cid:88) | M         |     |     | appliedtothepositivescoreofeachqueryagainst |     |     |     |     |     |
| --- | --- | -------- | --------- | --- | --- | ------------------------------------------- | --- | --- | --- | --- | --- |
|     | S   | =        | m axQ ·DT |     | (1) |                                             |     |     |     |     |     |
|     | q,d |          | i j       |     |     | allpassagescorrespondingtootherqueriesinthe |     |     |     |     |     |
j=1
i=1
|     |     |     |     |     |     | same batch. | We  | repeat | this procedure | once | to re- |
| --- | --- | --- | --- | --- | --- | ----------- | --- | ------ | -------------- | ---- | ------ |
whereQisanmatrixencodingthequerywithN
freshtheindexandthusthesamplednegatives.
| vectorsandDencodesthepassagewithM |     |     |     |     | vectors. |     |     |     |     |     |     |
| --------------------------------- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- |
Denoisedtrainingwithhardnegativeshasbeen
| The intuition | of     | this architecture | is             | to align | each |             |               |      |     |                   |     |
| ------------- | ------ | ----------------- | -------------- | -------- | ---- | ----------- | ------------- | ---- | --- | ----------------- | --- |
|               |        |                   |                |          |      | positioned  | in recent     | work | as  | ways to bridge    | the |
| query token   | with   | the most          | contextually   | relevant |      |             |               |      |     |                   |     |
|               |        |                   |                |          |      | gap between | single-vector |      | and | interaction-based |     |
| passage       | token, | quantify          | these matches, | and      | com- |             |               |      |     |                   |     |
models,includinglateinteractionarchitectureslike
| binethepartialscoresacrossthequery. |     |     |     | Werefer |     |     |     |     |     |     |     |
| ----------------------------------- | --- | --- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
ColBERT.Ourresultsin§5revealthatsuchsuper-
toKhattabandZaharia(2020)foramoredetailed
|     |     |     |     |     |     | vision can | improve | multi-vector |     | models | dramati- |
| --- | --- | --- | --- | --- | --- | ---------- | ------- | ------------ | --- | ------ | -------- |
treatmentoflateinteraction.
cally,resultinginstate-of-the-artretrievalquality.
3.2 Supervision
|     |     |     |     |     |     | 3.3 Representation |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ------------------ | --- | --- | --- | --- | --- |
Traininganeuralretrievertypicallyrequiresposi-
tive and negative passages for each query in the WehypothesizethattheColBERTvectorscluster
training set. Khattab and Zaharia (2020) train intoregionsthatcapturehighly-specifictokense-
ColBERT using the official (cid:104)q, d+, d−(cid:105) triples mantics. We test this hypothesis in Appendix A,
ofMSMARCO.Foreachquery,apositived+ is whereevidencesuggeststhatvectorscorrespond-
human-annotated,andeachnegatived− ing to each sense of a word cluster closely, with
issampled
fromunannotatedBM25-retrievedpassages. only minor variation due to context. We exploit
Subsequent work has identified several weak- this regularity with a residual representation that
nesses in this standard supervision approach dramaticallyreducesthespacefootprintoflatein-
(see§2.3). Ourgoalistoadoptasimple,uniform teractionmodels,completelyoff-the-shelf without
supervision scheme that selects challenging neg- architectural or training changes. Given a set of
atives and avoids rewarding false positives or pe- centroidsC,ColBERTv2encodeseachvectorv as
|                         |     |     |                       |     |     | theindexofitsclosestcentroidC |     |     |     | andaquantized |     |
| ----------------------- | --- | --- | --------------------- | --- | --- | ----------------------------- | --- | --- | --- | ------------- | --- |
| nalizingfalsenegatives. |     |     | Tothisend,westartwith |     |     |                               |     |     |     | t             |     |
aColBERTmodeltrainedwithtriplesasinKhat- vectorr˜thatapproximatestheresidualr = v−C .
t
tabetal.(2021b),usingthistoindexthetraining At search time, we use the centroid index t and
|                                   |          |        |             |     |       | residualr˜recoveranapproximatev˜= |     |     |     | C   | +r˜. |
| --------------------------------- | -------- | ------ | ----------- | --- | ----- | --------------------------------- | --- | --- | --- | --- | ---- |
| passageswithColBERTv2compression. |          |        |             |     |       |                                   |     |     |     |     | t    |
| For each                          | training | query, | we retrieve | the | top-k |                                   |     |     |     |     |      |
Toencoder˜,wequantizeeverydimensionofr
passages. We feed each of those query–passage intooneortwobits. Inprinciple,ourb-bitencod-
pairs into a cross-encoder reranker. We use a ingofn-dimensionalvectorsneeds(cid:100)log|C|(cid:101)+bn
22M-parameterMiniLM(Wangetal.,2020)cross- bitspervector. Inpractice,withn = 128,weuse
encoder trained with distillation by Thakur et al. fourbytestocaptureupto232 centroidsand16or
(2021).2 Thissmallmodelhasbeenshowntoex- 32bytes(forb = 1orb = 2)toencodetheresid-
hibit very strong performance while being rela- ual. Thistotalof20or36bytespervectorcontrasts
| tively efficient |     | for inference, | making | it suitable |     |     |     |     |     |     |     |
| ---------------- | --- | -------------- | ------ | ----------- | --- | --- | --- | --- | --- | --- | --- |
withColBERT’suseof256-bytevectorencodings
fordistillation. at16-bitprecision. Whilemanyalternativescanbe
We then collect w-way tuples consisting of a exploredforcompression,wefindthatthissimple
query, a highly-ranked passage (or labeled posi- encoding largely preserves model quality, while
tive),andoneormorelower-rankedpassages. In considerably lowering storage costs against typi-
this work, we use w = 64 passages per example. cal 32- or 16-bit precision used by existing late
| Like RocketQAv2 |     | (Ren | et al., 2021b), | we  | use a | interactionsystems. |     |     |     |     |     |
| --------------- | --- | ---- | --------------- | --- | ----- | ------------------- | --- | --- | --- | --- | --- |
Thiscentroid-basedencodingcanbeconsidered
2https://huggingface.co/cross-encoder/
anaturalextensionofproductquantizationtomulti-
ms-marco-MiniLM-L-6-v2

| vectorrepresentations. |     | Productquantization(Gray, |     |     |     | 3.5 Retrieval |     |     |     |     |     |
| ---------------------- | --- | ------------------------- | --- | --- | --- | ------------- | --- | --- | --- | --- | --- |
1984;Jegouetal.,2010)compressesasinglevector
GivenaqueryrepresentationQ,retrievalstartswith
bysplittingitintosmallsub-vectorsandencoding
|     |     |     |     |     |     | candidate | generation. | For | every | vector Q | in the |
| --- | --- | --- | --- | --- | --- | --------- | ----------- | --- | ----- | -------- | ------ |
i
| each of them | using | an ID | within | a codebook. | In  |            |         |         |               |     |        |
| ------------ | ----- | ----- | ------ | ----------- | --- | ---------- | ------- | ------- | ------------- | --- | ------ |
|              |       |       |        |             |     | query, the | nearest | n probe | ≥ 1 centroids | are | found. |
ourapproach,eachrepresentationisalreadyama-
Usingtheinvertedlist,ColBERTv2identifiesthe
trixthatisnaturallydividedintoanumberofsmall
|              |             |     |        |      |        | passage | embeddings | close | to these | centroids, | de- |
| ------------ | ----------- | --- | ------ | ---- | ------ | ------- | ---------- | ----- | -------- | ---------- | --- |
| vectors (one | per token). | We  | encode | each | vector |         |            |       |          |            |     |
compressesthem,andcomputestheircosinesimi-
| using its | nearest centroid |     | plus a | residual. | Refer |                             |     |     |                  |     |     |
| --------- | ---------------- | --- | ------ | --------- | ----- | --------------------------- | --- | --- | ---------------- | --- | --- |
|           |                  |     |        |           |       | laritywitheveryqueryvector. |     |     | Thescoresarethen |     |     |
toAppendixBfortestsoftheimpactofcompres-
groupedbypassageIDforeachqueryvector,and
siononretrievalqualityandacomparisonwitha
scorescorrespondingtothesamepassagearemax-
baselinecompressionmethodforColBERTakinto
|     |     |     |     |     |     | reduced. | This | allows ColBERTv2 |     | to conduct | an  |
| --- | --- | --- | --- | --- | --- | -------- | ---- | ---------------- | --- | ---------- | --- |
BPR(Yamadaetal.,2021b).
approximate“MaxSim”operationperqueryvector.
Thiscomputesalower-boundonthetrueMaxSim
3.4 Indexing
(§3.1)usingtheembeddingsidentifiedviathein-
| Given a | corpus of | passages, | the | indexing | stage |     |     |     |     |     |     |
| ------- | --------- | --------- | --- | -------- | ----- | --- | --- | --- | --- | --- | --- |
vertedlist,whichresemblestheapproximationex-
precomputes all passage embeddings and orga- plored for scoring by Macdonald and Tonellotto
nizestheirrepresentationstosupportfastnearest- (2021)butisappliedforcandidategeneration.
| neighborsearch. | ColBERTv2dividesindexinginto |     |     |     |     |       |       |        |            |        |     |
| --------------- | ---------------------------- | --- | --- | --- | --- | ----- | ----- | ------ | ---------- | ------ | --- |
|                 |                              |     |     |     |     | These | lower | bounds | are summed | across | the |
threestages,describedbelow. query tokens, and the top-scoring n can-
candidate
Centroid Selection. In the first stage, Col- didatepassagesbasedontheseapproximatescores
BERTv2selectsasetofclustercentroidsC. These areselectedforranking,whichloadsthecomplete
| are embeddings | that | ColBERTv2 |     | uses | to sup- |     |     |     |     |     |     |
| -------------- | ---- | --------- | --- | ---- | ------- | --- | --- | --- | --- | --- | --- |
setofembeddingsofeachpassage,andconducts
portresidualencoding(§3.3)andalsofornearest- the same scoring function using all embeddings
neighbor search (§3.5). Standardly, we find that per document following Equation 1. The result
setting |C| proportionally to the square root of passagesarethensortedbyscoreandreturned.
| n   | inthecorpusworkswellempirically.3 |     |     |     |     |     |     |     |     |     |     |
| --- | --------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
embeddings
4 LoTTE:Long-Tail,Cross-Domain
KhattabandZaharia(2020)onlyclusteredthevec-
RetrievalEvaluation
torsaftercomputingtherepresentationsofallpas-
sages, butdoingsorequiresstoringthemuncom-
|     |     |     |     |     |     | We introduce |     | LoTTE (pronounced |     | latte), | a new |
| --- | --- | --- | --- | --- | --- | ------------ | --- | ----------------- | --- | ------- | ----- |
pressed. Toreducememoryconsumption,weapply
datasetforLong-TailTopic-stratifiedEvaluation
k-meansclusteringtotheembeddingsproducedby
forIR.Tocomplementtheout-of-domaintestsof
invokingourBERTencoderoveronlyasampleof
|     |     |     |     |     |     | BEIR(Thakuretal.,2021), |     |     | asmotivatedin§2.4, |     |     |
| --- | --- | --- | --- | --- | --- | ----------------------- | --- | --- | ------------------ | --- | --- |
allpassages,proportionaltothesquarerootofthe
LoTTEfocusesonnaturaluserqueriesthatpertain
collectionsize,anapproachwefoundtoperform
tolong-tailtopics,onesthatmightnotbecovered
wellinpractice.
byanentity-centricknowledgebaselikeWikipedia.
| Passage | Encoding. | Having |     | selected | the cen- |     |     |     |     |     |     |
| ------- | --------- | ------ | --- | -------- | -------- | --- | --- | --- | --- | --- | --- |
LoTTEconsistsof12testsets,eachwith500–2000
| troids,weencodeeverypassageinthecorpus. |     |     |     |     | This |     |     |     |     |     |     |
| --------------------------------------- | --- | --- | --- | --- | ---- | --- | --- | --- | --- | --- | --- |
queriesand100k–2Mpassages.
entailsinvokingtheBERTencoderandcompress-
Thetestsetsareexplicitlydividedbytopic,and
| ing the output | embeddings |     | as described |     | in §3.3, |     |     |     |     |     |     |
| -------------- | ---------- | --- | ------------ | --- | -------- | --- | --- | --- | --- | --- | --- |
eachtestsetisaccompaniedbyavalidationsetof
assigningeachembeddingtothenearestcentroid
|                                   |     |     |     |             |     | relatedbutdisjointqueriesand |             |       |          | passages. Weelect |     |
| --------------------------------- | --- | --- | --- | ----------- | --- | ---------------------------- | ----------- | ----- | -------- | ----------------- | --- |
| andcomputingaquantizedresidual.   |     |     |     | Onceachunk  |     |                              |             |       |          |                   |     |
|                                   |     |     |     |             |     | to make                      | the passage | texts | disjoint | to encourage      |     |
| ofpassagesisencoded,thecompressed |     |     |     | representa- |     |                              |             |       |          |                   |     |
morerealisticout-of-domaintransfertests,allow-
tionsaresavedtodisk.
ingforminimaldevelopmentonrelatedbutdistinct
| Index | Inversion. | To  | support | fast | nearest- |     |     |     |     |     |     |
| ----- | ---------- | --- | ------- | ---- | -------- | --- | --- | --- | --- | --- | --- |
topics. Thetest(anddev)setsincludea“pooled”
neighborsearch,wegrouptheembeddingIDsthat
|     |     |     |     |     |     | setting. | In the | pooled | setting, | the passages | and |
| --- | --- | --- | --- | --- | --- | -------- | ------ | ------ | -------- | ------------ | --- |
correspondtoeachcentroidtogether,andsavethis
queriesareaggregatedacrossalltest(ordev)topics
| invertedlisttodisk. |     | Atsearchtime,thisallowsus |     |     |     |     |     |     |     |     |     |
| ------------------- | --- | ------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
toevaluateout-of-domainretrievalacrossalarger
toquicklyfindtoken-levelembeddingssimilarto
andmorediversecorpus.
thoseinaquery.
Table1outlinesthecompositionofLoTTE.We
|     |     |     |     |     |     | derive the | topics | and passage |     | corpora from | the |
| --- | --- | --- | --- | --- | --- | ---------- | ------ | ----------- | --- | ------------ | --- |
3Werounddowntothenearestpoweroftwolargerthan
| √                |                                      |     |     |     |     | answer | posts | across various | StackExchange |     | fo- |
| ---------------- | ------------------------------------ | --- | --- | --- | --- | ------ | ----- | -------------- | ------------- | --- | --- |
| 16× n embeddings | ,inspiredbyFAISS(Johnsonetal.,2019). |     |     |     |     |        |       |                |               |     |     |

|       |             |     |     |     | Dev |     |     |     |     | Test |     |     |
| ----- | ----------- | --- | --- | --- | --- | --- | --- | --- | --- | ---- | --- | --- |
| Topic | QuestionSet |     |     |     |     |     |     |     |     |      |     |     |
#Questions #Passages Subtopics #Questions #Passages Subtopics
| Writing    | Search |     | 497   |        | 277k | ESL,Linguistics,    |     | 1071  |     | 200k   |                 | English  |
| ---------- | ------ | --- | ----- | ------ | ---- | ------------------- | --- | ----- | --- | ------ | --------------- | -------- |
|            | Forum  |     | 2003  |        |      | Worldbuilding       |     | 2000  |     |        |                 |          |
|            | Search |     | 563   |        |      | Sci-Fi,RPGs,        |     | 924   |     |        |                 | Gaming,  |
| Recreation |        |     |       |        | 263k |                     |     |       |     | 167k   |                 |          |
|            | Forum  |     | 2002  |        |      | Photography         |     | 2002  |     |        | Anime,Movies    |          |
|            | Search |     | 538   |        |      | Chemistry,          |     | 617   |     |        |                 | Math,    |
| Science    |        |     |       |        | 344k |                     |     |       |     | 1.694M |                 |          |
|            | Forum  |     | 2013  |        |      | Statistics,Academia |     | 2017  |     |        | Physics,Biology |          |
|            | Search |     | 916   |        |      | WebApps,            |     | 596   |     |        | Apple,Android,  |          |
| Technology |        |     |       | 1.276M |      |                     |     |       |     | 639k   |                 |          |
|            | Forum  |     | 2003  |        |      | Ubuntu,SysAdmin     |     | 2004  |     |        | UNIX,Security   |          |
|            | Search |     | 417   |        |      | DIY,Music,Bicycles, |     | 661   |     |        |                 | Cooking, |
| Lifestyle  |        |     |       |        | 269k |                     |     |       |     | 119k   |                 |          |
|            | Forum  |     | 2076  |        |      | CarMaintenance      |     | 2002  |     |        | Sports,Travel   |          |
|            | Search |     | 2931  |        |      |                     |     | 3869  |     |        |                 |          |
| Pooled     |        |     |       |        | 2.4M | Alloftheabove       |     |       |     | 2.8M   | Alloftheabove   |          |
|            | Forum  |     | 10097 |        |      |                     |     | 10025 |     |        |                 |          |
Table1: CompositionofLoTTEshowingtopics,questionsets,andasampleofcorrespondingsubtopics. Search
Queries are taken from GooAQ, while Forum Queries are taken directly from the StackExchange archive. The
pooleddatasetscombinethequestionsandpassagesfromeachofthesubtopics.
rums. StackExchange is a set of question-and- Q:whatisthedifferencebetweenrootandsteminlin-
|                    |     |      |                   |     |        | guistics?       | A:Arootistheformtowhichderivational |              |     |                |     |     |
| ------------------ | --- | ---- | ----------------- | --- | ------ | --------------- | ----------------------------------- | ------------ | --- | -------------- | --- | --- |
| answer communities |     | that | target individual |     | topics |                 |                                     |              |     |                |     |     |
|                    |     |      |                   |     |        | affixesareadded |                                     | toformastem. |     | Astemistheform |     |     |
(e.g.,“physics”or“bicycling”). Wegatherforums towhichinflectionalaffixesareaddedtoformaword.
| fromfiveoverarchingdomains:      |     |     | writing,recreation, |               |     |              |     |                |     |          |      |             |
| -------------------------------- | --- | --- | ------------------- | ------------- | --- | ------------ | --- | -------------- | --- | -------- | ---- | ----------- |
|                                  |     |     |                     |               |     | Q: are there | any | airbenders     |     | left? A: | the  | Fire Nation |
| science,technology,andlifestyle. |     |     |                     | Toevaluatere- |     |              |     |                |     |          |      |             |
|                                  |     |     |                     |               |     | had wiped    | out | all Airbenders |     | while    | Aang | was frozen. |
trievers,wecollectSearchandForumqueries,each Tenzinandhis3childrenaretheonlyAirbendersleft
| ofwhichisassociatedwithoneormoretargetan- |     |     |     |     |     | inKorra’stime. |     |     |     |     |     |     |
| ----------------------------------------- | --- | --- | --- | --- | --- | -------------- | --- | --- | --- | --- | --- | --- |
swer posts in its corpus. Example queries, and Q: Why are there two Hydrogen atoms on some peri-
odictables?A:someperiodictablesshowhydrogenin
shortsnippetsfrompoststhatanswertheminthe
bothplacestoemphasizethathydrogenisn’treallya
corpora,areshowninTable2. memberofthefirstgrouportheseventhgroup.
| SearchQueries. |     | Wecollectsearchqueriesfrom |     |     |     |                          |     |     |     |                  |     |     |
| -------------- | --- | -------------------------- | --- | --- | --- | ------------------------ | --- | --- | --- | ---------------- | --- | --- |
|                |     |                            |     |     |     | Q:Howcancachebethatfast? |     |     |     | A:thecachememory |     |     |
GooAQ (Khashabi et al., 2021), a recent dataset sitsrightnexttotheCPUonthesamedie(chip),itis
madeusingSRAMwhichismuch,muchfasterthan
| of Google | search-autocomplete |     | queries |     | and their |     |     |     |     |     |     |     |
| --------- | ------------------- | --- | ------- | --- | --------- | --- | --- | --- | --- | --- | --- | --- |
theDRAM.
| answer boxes, | which | we  | filter for | queries | whose |     |     |     |     |     |     |     |
| ------------- | ----- | --- | ---------- | ------- | ----- | --- | --- | --- | --- | --- | --- | --- |
answerslinktoaspecificStackExchangepost. As Table2:Examplesofqueriesandshortenedsnippetsof
Khashabietal.(2021)hypothesize,GoogleSearch answerpassagesfromLoTTE.Thefirsttwoexamples
|     |     |     |     |     |     | show “search” |     | queries, | whereas | the | last | two are “fo- |
| --- | --- | --- | --- | --- | --- | ------------- | --- | -------- | ------- | --- | ---- | ------------ |
likelymapsthesenaturalqueriestotheiranswers
by relying on a wide variety of signals for rele- rum”queries. Snippetsareshortenedforpresentation.
| vance, including |     | expert | annotations, | user | clicks, |     |     |     |     |     |     |     |
| ---------------- | --- | ------ | ------------ | ---- | ------- | --- | --- | --- | --- | --- | --- | --- |
andhyperlinksaswellasspecializedQAcompo- These queries tend to have a wider variety than
nentsforvariousquestiontypeswithaccesstothe the“search”queries,whilethesearchqueriesmay
posttitleandquestionbody. Usingthoseannota- exhibitmorenaturalpatterns. Table3comparesa
tions as ground truth, we evaluate the models on random samples of search and forum queries. It
|                |     |           |            |      |      | can be seen | that | search | queries |     | tend | to be brief, |
| -------------- | --- | --------- | ---------- | ---- | ---- | ----------- | ---- | ------ | ------- | --- | ---- | ------------ |
| their capacity | for | retrieval | using only | free | text | of          |      |        |         |     |      |              |
theanswerposts(i.e.,nohyperlinksoruserclicks, knowledge-based questions with direct answers,
question title or body, etc.), posing a significant whereasforumqueriestendtoreflectmoreopen-
challengeforIRandNLPsystemstrainedonlyon endedquestions. Bothquerysetstargettopicsthat
| publicdatasets. |     |     |     |     |     | exceedthescopeofageneral-purposeknowledge |     |     |     |     |     |     |
| --------------- | --- | --- | --- | --- | --- | ----------------------------------------- | --- | --- | --- | --- | --- | --- |
Forum Queries. We collect the forum queries repositorysuchasWikipedia.
by extracting post titles from the StackExchange Forsearchaswellasforumqueries,theresult-
communities to use as queries and collect their ingevaluationsetconsistsofaqueryandatarget
correspondinganswerpostsastargets. Weselect setofStackExchangeanswerposts(inparticular,
questions in order of their popularity and sample the answer posts from the target StackExchange
questions according to the proportional contribu- page). Similar to evaluation in the Open-QA lit-
tionofindividualcommunitieswithineachtopic. erature (Karpukhin et al., 2020; Khattab et al.,

Q:whatisxerrorinrpart? Q:issubquestiononeword? OfficialDev(7k) LocalEval(5k)
Method
Q:howtoopenagaragedoorwithoutmakingnoise? Q: MRR@10 R@50 R@1k MRR@10 R@50 R@1k
| isdocxanddotxthesame? |     |     | Q:areupvotesanddownvotes |     |     |     |     |     |     |     |     |     |
| --------------------- | --- | --- | ------------------------ | --- | --- | --- | --- | --- | --- | --- | --- | --- |
ModelswithoutDistillationorSpecialPretraining
| anonymous?               | Q:whatisthedifferencebetweendescriptive |                             |                          |           |         |         |     |      |           |     |      |     |
| ------------------------ | --------------------------------------- | --------------------------- | ------------------------ | --------- | ------- | ------- | --- | ---- | --------- | --- | ---- | --- |
|                          |                                         |                             |                          |           |         | RepBERT |     | 30.4 | - 94.3    |     | -    | - - |
| essay andnarrativeessay? |                                         |                             | Q: how                   | to change | default |         |     |      |           |     |      |     |
|                          |                                         |                             |                          |           |         | DPR     |     | 31.1 | - 95.2    |     | -    | - - |
| userprofileinchrome?     |                                         |                             | Q:doesautohotkeyneedtobe |           |         |         |     |      |           |     |      |     |
|                          |                                         |                             |                          |           |         | ANCE    |     | 33.0 | - 95.9    |     | -    | - - |
| installed?               | Q:howdoyoutagsomeoneonfacebookwith      |                             |                          |           |         |         |     |      |           |     |      |     |
|                          |                                         |                             |                          |           |         | LTRe    |     | 34.1 | - 96.2    |     | -    | - - |
| ayoutubevideo?           |                                         | Q:hasmjolnireverbeenbroken? |                          |           |         |         |     |      |           |     |      |     |
|                          |                                         |                             |                          |           |         | ColBERT |     | 36.0 | 82.9 96.8 |     | 36.7 | - - |
Q:Snoopycanbalanceonanedgeatophisdoghouse.Isany
ModelswithDistillationorSpecialPretraining
| reasongivenforthis? |     | Q:HowmanyEntswereatthe |     |     |     |     |     |     |     |     |     |     |
| ------------------- | --- | ---------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
Entmoot? Q:Whatdoesahexagonalsuntellusabout TAS-B 34.7 - 97.8 - - -
thecameralens/sensor? Q:ShouldIsimplyignoreitif SPLADEv2 36.8 - 97.9 37.9 84.9 98.0
authorsassumethatImmaleintheirresponsetomyreviewof PAIR 37.9 86.4 98.2 - - -
|               |                                      |     |     |     |     | coCondenser |     | 38.2 | - 98.4    |     | -    | - -       |
| ------------- | ------------------------------------ | --- | --- | --- | --- | ----------- | --- | ---- | --------- | --- | ---- | --------- |
| theirarticle? | Q:Whyisthe2sorbitallowerinenergythan |     |     |     |     |             |     |      |           |     |      |           |
|               |                                      |     |     |     |     | RocketQAv2  |     | 38.8 | 86.2 98.1 |     | 39.8 | 85.8 97.9 |
the2porbitalwhentheelectronsin2sareusuallyfartherfrom
|                                         |                                     |                            |     |     |        | ColBERTv2 |           | 39.7        | 86.8 98.4 |     | 40.8            | 86.3 98.3 |
| --------------------------------------- | ----------------------------------- | -------------------------- | --- | --- | ------ | --------- | --------- | ----------- | --------- | --- | --------------- | --------- |
| thenucleus?                             | Q:Aretherereasonstousecolourfilters |                            |     |     |        |           |           |             |           |     |                 |           |
| withdigitalcameras?                     |                                     | Q:Howdoesthecurrentknowhow |     |     |        |           |           |             |           |     |                 |           |
|                                         |                                     |                            |     |     |        | Table 4:  | In-domain | performance |           | on  | the development |           |
| muchtoflow,beforehavingseentheresistor? |                                     |                            |     |     | Q:What |           |           |             |           |     |                 |           |
setofMSMARCOPassageRankingaswellthe“Local
| isthedifferencebetweenFactandTruth? |     |     |     | Q:hAsaDM, |     |     |     |     |     |     |     |     |
| ----------------------------------- | --- | --- | --- | --------- | --- | --- | --- | --- | --- | --- | --- | --- |
howcanIhandlemyDruidspyingoneverythingwithWild Eval”testsetdescribedbyKhattabandZaharia(2020).
shapeasaspider? Q:Whatdoes1x1convolutionmean Dev-set results for baseline systems are from their re-
inaneuralnetwork? spectivepapers:Zhanetal.(2020b),Xiongetal.(2020)
|     |     |     |     |     |     | forDPRandANCE,Zhanetal.(2020a), |     |     |     |     | Khattaband |     |
| --- | --- | --- | --- | --- | --- | ------------------------------- | --- | --- | --- | --- | ---------- | --- |
Table 3: Comparison of a random sample of search Zaharia(2020),Hofstätteretal.(2021),GaoandCallan
queries(top)vs. forumqueries(bottom). (2021), Ren et al. (2021a), Formal et al. (2021a), and
Renetal.(2021b).
| 2021b), | we evaluate | retrieval | quality | by  | comput- |       |                |     |     |         |        |       |
| ------- | ----------- | --------- | ------- | --- | ------- | ----- | -------------- | --- | --- | ------- | ------ | ----- |
|         |             |           |         |     |         | PAIR, | and RocketQAv2 |     | to  | achieve | higher | qual- |
ingthesuccess@5(S@5)metric. Specifically,we itythanvanillaColBERT.Thesesupervisiongains
awardapointtothesystemforeachquerywhere
challengethevalueoffine-grainedlateinteraction,
itfindsanacceptedorupvoted(score≥1)answer
anditisnotinherentlyclearwhetherthestronger
fromthetargetpageinthetop-5hits. inductivebiasesofColBERT-likemodelspermitit
Appendix D reports on the breakdown of con- toacceptsimilargainsunderdistillation,especially
| stituent | communities | per | topic, | the construction |     |            |            |     |                  |     |     |         |
| -------- | ----------- | --- | ------ | ---------------- | --- | ---------- | ---------- | --- | ---------------- | --- | --- | ------- |
|          |             |     |        |                  |     | when using | compressed |     | representations. |     |     | Despite |
procedureofLoTTEaswellaslicensingconsidera- this, we find that with denoised supervision and
tions,andrelevantstatistics. Figures5and6quan- residual compression, ColBERTv2 achieves the
titativelycomparethesearchandforumqueries.
|     |     |     |     |     |     | highestqualityacrossallsystems. |     |     |     |     | Aswediscuss |     |
| --- | --- | --- | --- | --- | --- | ------------------------------- | --- | --- | --- | --- | ----------- | --- |
in§5.3,itexhibitsspacefootprintcompetitivewith
5 Evaluation
|     |     |     |     |     |     | these single-vector |     | models |     | and | much lower | than |
| --- | --- | --- | --- | --- | --- | ------------------- | --- | ------ | --- | --- | ---------- | ---- |
vanillaColBERT.
WenowevaluateColBERTv2onpassageretrieval
|     |     |     |     |     |     | Besides | the | official | dev | set, we | evaluated | Col- |
| --- | --- | --- | --- | --- | --- | ------- | --- | -------- | --- | ------- | --------- | ---- |
tasks,testingitsqualitywithinthetrainingdomain
(§5.1) as well as outside the training domain in BERTv2, SPLADEv2, and RocketQAv2 on the
“LocalEval”testsetdescribedbyKhattabandZa-
| zero-shotsettings(§5.2). |           |     | Unlessotherwisestated, |     |       |              |     |     |        |       |          |     |
| ------------------------ | --------- | --- | ---------------------- | --- | ----- | ------------ | --- | --- | ------ | ----- | -------- | --- |
|                          |           |     |                        |     |       | haria (2020) | for | MS  | MARCO, | which | consists | of  |
| we compress              | ColBERTv2 |     | embeddings             | to  | b = 2 |              |     |     |        |       |          |     |
5000queriesdisjointwiththetrainingandtheof-
bitsperdimensioninourevaluation.
|     |     |     |     |     |     | ficial dev | sets. | These | queries | are | obtained | from |
| --- | --- | --- | --- | --- | --- | ---------- | ----- | ----- | ------- | --- | -------- | ---- |
5.1 In-DomainRetrievalQuality labeled50kqueriesthatareprovidedintheofficial
MSMARCOPassageRankingtaskasadditional
Similartorelatedwork,wetrainforIRtasksonMS
|     |     |     |     |     |     | validationdata.4 |     | Onthistestset,ColBERTv2ob- |     |     |     |     |
| --- | --- | --- | --- | --- | --- | ---------------- | --- | -------------------------- | --- | --- | --- | --- |
MARCOPassageRanking(Nguyenetal.,2016).
tains40.8%MRR@10,considerablyoutperform-
Withinthetrainingdomain,ourdevelopment-setre-
|     |     |     |     |     |     | ing the | baselines, | including |     | RocketQAv2 |     | which |
| --- | --- | --- | --- | --- | --- | ------- | ---------- | --------- | --- | ---------- | --- | ----- |
sultsareshowninTable4,comparingColBERTv2
|              |         |     |         |                  |     | makes | use of | document | titles | in  | addition | to the |
| ------------ | ------- | --- | ------- | ---------------- | --- | ----- | ------ | -------- | ------ | --- | -------- | ------ |
| with vanilla | ColBERT | as  | well as | state-of-the-art |     |       |        |          |        |     |          |        |
passagetextunliketheothersystems.
single-vectorsystems.
WhileColBERToutperformssingle-vectorsys-
4Thesearesampledfromdeltabetweenqrels.dev.tsv
temslikeRepBERT,ANCE,andevenTAS-B,im- and qrels.dev.small.tsv on https://microsoft.
|     |     |     |     |     |     | github.io/msmarco/Datasets. |     |     |     | We refer | to  | Khattab and |
| --- | --- | --- | --- | --- | --- | --------------------------- | --- | --- | --- | -------- | --- | ----------- |
provementsinsupervisionsuchasdistillationfrom
|                |        |         |      |           |     | Zaharia(2020)fordetails. |     |     | AllourqueryIDswillbemade |     |     |     |
| -------------- | ------ | ------- | ---- | --------- | --- | ------------------------ | --- | --- | ------------------------ | --- | --- | --- |
| cross-encoders | enable | systems | like | SPLADEv2, |     |                          |     |     |                          |     |     |     |
publictoaidreproducibility.

ModelswithoutDistillation ModelswithDistillation
Corpus
ColBERT DPR-M ANCE MoDIR TAS-B RocketQAv2 SPLADEv2 ColBERTv2
Corpus
BEIRSearchTasks(nDCG@10)
DBPedia 39.2 23.6 28.1 28.4 38.4 35.6 43.5 44.6
FiQA 31.7 27.5 29.5 29.6 30.0 30.2 33.6 35.6
NQ 52.4 39.8 44.6 44.2 46.3 50.5 52.1 56.2
HotpotQA 59.3 37.1 45.6 46.2 58.4 53.3 68.4 66.7
NFCorpus 30.5 20.8 23.7 24.4 31.9 29.3 33.4 33.8
T-COVID 67.7 56.1 65.4 67.6 48.1 67.5 71.0 73.8
Touché(v2) - - - - - 24.7 27.2 26.3
BEIRSemanticRelatednessTasks(nDCG@10)
ArguAna 23.3 41.4 41.5 41.8 42.7 45.1 47.9 46.3
C-FEVER 18.4 17.6 19.8 20.6 22.8 18.0 23.5 17.6
FEVER 77.1 58.9 66.9 68.0 70.0 67.6 78.6 78.5
Quora 85.4 84.2 85.2 85.6 83.5 74.9 83.8 85.2
SCIDOCS 14.5 10.8 12.2 12.4 14.9 13.1 15.8 15.4
SciFact 67.1 47.8 50.7 50.2 64.3 56.8 69.3 69.3
(a)
ColBERT
BM25 ANCE
RocketQAv2 SPLADEv2 ColBERTv2
OODWikipediaOpenQA(Success@5)
NQ-dev 65.7 44.6 - - 65.6 68.9
TQ-dev 72.6 67.6 - - 74.7 76.7
SQuAD-dev 60.0 50.6 - - 60.4 65.0
LoTTESearchTestQueries(Success@5)
Writing 74.7 60.3 74.4 78.0 77.1 80.1
Recreation 68.5 56.5 64.7 72.1 69.0 72.3
Science 53.6 32.7 53.6 55.3 55.4 56.7
Technology 61.9 41.8 59.6 63.4 62.4 66.1
Lifestyle 80.2 63.8 82.3 82.1 82.3 84.7
Pooled 67.3 48.3 66.4 69.8 68.9 71.6
LoTTEForumTestQueries(Success@5)
Writing 71.0 64.0 68.8 71.5 73.0 76.3
Recreation 65.6 55.4 63.8 65.7 67.1 70.8
Science 41.8 37.1 36.5 38.0 43.7 46.1
Technology 48.5 39.4 46.8 47.3 50.8 53.6
Lifestyle 73.0 60.6 73.1 73.7 74.0 76.9
Pooled 58.2 47.2 55.7 57.7 60.1 63.4
(b)
Table 5: Zero-shot evaluation results. Sub-table (a) reports results on BEIR and sub-table (b) reports results on
the Wikipedia Open QA and the test sets of the LoTTE benchmark. On BEIR, we test ColBERTv2 and Rock-
etQAv2andcopytheresultsforANCE,TAS-B,andColBERTfromThakuretal.(2021), forMoDIRandDPR-
MSMARCO(DPR-M)fromXinetal.(2021),andforSPLADEv2fromFormaletal.(2021a).
5.2 Out-of-DomainRetrievalQuality out distillation, we see that the vanilla ColBERT
modeloutperformsthesingle-vectorsystemsDPR,
Next, we evaluate ColBERTv2 outside the train-
ANCE,andMoDIRacrossallbutthreetasks. Col-
ing domain using BEIR (Thakur et al., 2021),
BERT often outpaces all three systems by large
Wikipedia Open QA retrieval as in Khattab et al.
marginsand,infact,outperformstheTAS-Bmodel,
(2021b),andLoTTE.Wecompareagainstawide
whichutilizesdistillation,onmostdatasets. Shift-
range of recent and state-of-the-art retrieval sys-
ingourattentiontomodelswithdistillation,wesee
temsfromtheliterature.
asimilarpattern: whiledistillation-basedmodels
BEIR.WestartwithBEIR,reportingthequality
are generally stronger than their vanilla counter-
ofmodelsthatdonotincorporatedistillationfrom
parts,themodelsthatdecomposescoringintoterm-
cross-encoders, namely, ColBERT (Khattab and
level interactions, ColBERTv2 and SPLADEv2,
Zaharia,2020),DPR-MARCO(Xinetal.,2021),
arealmostalwaysthestrongest.
ANCE(Xiongetal.,2020),andMoDIR(Xinetal.,
2021), as well as models that do utilize distil-
Looking more closely into the comparison be-
lation, namely, TAS-B (Hofstätter et al., 2021),
tween SPLADEv2 and ColBERTv2, we see that
SPLADEv2(Formaletal.,2021a),andalsoRock-
ColBERTv2hasanadvantageonsixbenchmarks
etQAv2,whichwetestourselvesusingtheofficial
and ties SPLADEv2 on two, with the largest im-
checkpoint trained on MS MARCO. We divide
provements attained on NQ, TREC-COVID, and
the table into “search” (i.e., natural queries and
FiQA-2018, all of which feature natural search
questions)and“semanticrelatednes”(e.g.,citation-
queries. On the other hand, SPLADEv2 has the
relatednessandclaimverification)taskstoreflect
lead on five benchmarks, displaying the largest
thenatureofqueriesineachdataset.5
gains on Climate-FEVER (C-FEVER) and Hot-
Table 5a reports results with the official
PotQA. In C-FEVER, the input queries are sen-
nDCG@10 metric. Among the models with-
tencesmakingclimate-relatedclaimsand,asare-
sult, do not reflect the typical characteristics of
5FollowingFormaletal.(2021a),weconductourevalu-
searchqueries. InHotPotQA,queriesarewritten
ationgusingthepublicly-availabledatasetsinBEIR.Refer
to§Efordetails. bycrowdworkerswhohaveaccesstothetargetpas-

sages. This is known to lead to artificial lexical MARCO than the forum queries and, as a result,
bias(Leeetal.,2019),wherecrowdworkerscopy thelatterstressesgeneralizationmoreheavily,re-
termsfromthepassagesintotheirquestionsasin wardingterm-decomposedmodelslikeSPLADEv2
| theOpen-SQuADbenchmark. |                 |            |     |              |      |         | andColBERTv2.  |     |     |     |     |
| ----------------------- | --------------- | ---------- | --- | ------------ | ---- | ------- | -------------- | --- | --- | --- | --- |
| Wikipedia               |                 | Open       | QA. | As a further | test | of out- |                |     |     |     |     |
| of-domain               | generalization, |            |     | we evaluate  |      | the MS  | 5.3 Efficiency |     |     |     |     |
| MARCO-trained           |                 | ColBERTv2, |     | SPLADEv2,    |      | and     |                |     |     |     |     |
vanilla ColBERT on retrieval for open-domain ColBERTv2’sresidualcompressionapproachsig-
nificantlyreducesindexsizescomparedtovanilla
questionanswering,similartotheout-of-domain
|         |            |     |        |          |     |        | ColBERT. | Whereas   | ColBERT | requires | 154 GiB   |
| ------- | ---------- | --- | ------ | -------- | --- | ------ | -------- | --------- | ------- | -------- | --------- |
| setting | of Khattab |     | et al. | (2021b). | We  | report |          |           |         |          |           |
|         |            |     |        |          |     |        | to store | the index | for MS  | MARCO,   | ColBERTv2 |
Success@5(sometimesreferredtoasRecall@5),
onlyrequires16GiBor25GiBwhencompressing
whichisthepercentageofquestionswhoseshort
embeddingsto1or2bit(s)perdimension,respec-
| answer          | string | overlaps | with | one or   | more   | of the  |         |           |                |        |           |
| --------------- | ------ | -------- | ---- | -------- | ------ | ------- | ------- | --------- | -------------- | ------ | --------- |
|                 |        |          |      |          |        |         | tively, | resulting | in compression | ratios | of 6–10×. |
| top-5 passages. |        | For      | the  | queries, | we use | the de- |         |           |                |        |           |
velopment set questions of the open-domain ver- Thisstoragefigureincludes4.5GiBforstoringthe
invertedlist.
sions(Leeetal.,2019;Karpukhinetal.,2020)of
NaturalQuestions(NQ;Kwiatkowskietal.2019), This matches the storage for a typical single-
vectormodelonMSMARCO,with4-bytelossless
TriviaQA(TQ;Joshietal.2017),andSQuAD(Ra-
jpurkar et al., 2016) datasets in Table 5b. As a floating-pointstorageforone768-dimensionalvec-
baseline, we include the BM25 (Robertson et al., torforeachofthe9Mpassagesamountingtoalittle
|     |     |     |     |     |     |     | over25GiBs. | Inpractice,thestorageforasingle- |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ----------- | -------------------------------- | --- | --- | --- |
1995)resultsusingtheAnserini(Yangetal.,2018a)
toolkit. WeobservethatColBERTv2outperforms vector model could be even larger when using a
BM25,vanillaColBERT,andSPLADEv2across nearest-neighborindexlikeHNSWforfastsearch.
the three query sets, with improvements of up to Conversely,single-vectorrepresentationscouldbe
4.6pointsoverSPLADEv2. themselves compressed very aggressively (Zhan
etal.,2021a,2022),thoughoftenexacerbatingthe
| LoTTE.Next, |     | weanalyzeperformanceonthe |     |     |     |     |     |     |     |     |     |
| ----------- | --- | ------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
lossinqualityrelativetolateinteractionmethods
LoTTEtestbenchmark,whichfocusesonnatural
likeColBERTv2.
queriesoverlong-tailtopicsandexhibitsadifferent
annotation pattern to the datasets in the previous We discuss the impact of our compression
|                 |     |                             |      |              |     |          | method  | on search     | quality | in Appendix | B and        |
| --------------- | --- | --------------------------- | ---- | ------------ | --- | -------- | ------- | ------------- | ------- | ----------- | ------------ |
| OODevaluations. |     | Inparticular,LoTTEusesauto- |      |              |     |          |         |               |         |             |              |
|                 |     |                             |      |              |     |          | present | query latency | results | on the      | order of 50– |
| matic Google    |     | rankings                    | (for | the “search” |     | queries) |         |               |         |             |              |
andorganicStackExchangequestion–answerpairs 250millisecondsperqueryinAppendixC.
(for“forum”queries),complimentingthepooling-
| basedannotationofdatasetslikeTREC-COVID(in |     |     |     |     |     |     | 6 Conclusion |     |     |     |     |
| ------------------------------------------ | --- | --- | --- | --- | --- | --- | ------------ | --- | --- | --- | --- |
BEIR)andtheansweroverlapmetricsofOpen-QA
| retrieval. | WereportSuccess@5foreachcorpuson |     |     |     |     |     |               |            |     |             |          |
| ---------- | -------------------------------- | --- | --- | --- | --- | --- | ------------- | ---------- | --- | ----------- | -------- |
|            |                                  |     |     |     |     |     | We introduced | ColBERTv2, |     | a retriever | that ad- |
bothsearchqueriesandforumqueries.
|     |     |     |     |     |     |     | vances | the quality | and space | efficiency | of multi- |
| --- | --- | --- | --- | --- | --- | --- | ------ | ----------- | --------- | ---------- | --------- |
Overall, we see that ANCE and vanilla Col- vectorrepresentations. Wehypothesizedthatclus-
BERT outperform BM25 on all topics, and that ter centroids capture context-aware semantics of
the three methods using distillation are generally the token-level representations and proposed a
the strongest. Similar to the Wikipedia-OpenQA residualrepresentationthatleveragesthesepatterns
results,wefindthatColBERTv2outperformsthe todramaticallyreducethefootprintofmulti-vector
baselinesacrossalltopicsforbothquerytypes,im- systemsoff-the-shelf. Wethenexploredimproved
provinguponSPLADEv2andRocketQAv2byup supervision for multi-vector retrieval and found
to 3.7 and 8.1 points, respectively. Considering thattheirqualityimprovesconsiderablyupondistil-
thebaselines,weobservethatwhileRocketQAv2 lationfromacross-encodersystem. Theproposed
tendstohaveaslightadvantageoverSPLADEv2 ColBERTv2considerablyoutperformsexistingre-
on the “search” queries, SPLADEv2 is consider- trieversinwithin-domainandout-of-domainevalu-
ably more effective on the “forum” tests. We hy- ations,whichweconductedextensivelyacross28
pothesize that the search queries, obtained from datasets,establishingstate-of-the-artqualitywhile
Google(throughGooAQ)aremoresimilartoMS exhibitingcompetitivespacefootprint.

Acknowledgements cross-encoders,whichareknowntobeexpensive
yetpreciseduetotheirhighlyexpressivecapacity.
This research was supported in part by affiliate
members and other supporters of the Stanford
ResearchLimitations
DAWNproject—AntFinancial,Facebook,Google,
andVMware—aswellasCisco,SAP,Virtusa,and WhileweevaluateColBERTv2onawiderangeof
theNSFunderCAREERgrantCNS-1651570. Any tests,allofourbenchmarksareinEnglishand,in
opinions,findings,andconclusionsorrecommen- linewithrelatedwork,ourout-of-domaintestseval-
dationsexpressedinthismaterialarethoseofthe uatemodelsthataretrainedonMSMARCO.We
authorsanddonotnecessarilyreflecttheviewsof expectourapproachtoworkeffectivelyforother
theNationalScienceFoundation. languages and when all models are trained using
other,smallertrainingset(e.g.,NaturalQuestions),
BroaderImpact&EthicalConsiderations
butweleavesuchteststofuturework.
This work is primarily an effort toward retrieval We have observed consistent gains for Col-
models that generalize better while performing BERTv2againstexistingstate-of-the-artsystems
reasonablyefficientlyintermsofspaceconsump- acrossmanydiversesettings. Despitethis,almost
tion. Strongout-of-the-boxgeneralizationtosmall all IR datasets contain false negatives (i.e., rele-
domain-specificapplicationscanservemanyusers vant but unlabeled passages) and thus some cau-
inpractice,particularlywheretrainingdataisnot tionisneededininterpretinganyindividualresult.
available. Moreover, retrieval holds significant Nonetheless, we intentionally sought out bench-
promise for many downstream NLP tasks, as it marks with dissimilar annotation biases: for in-
canhelpmakelanguagemodelssmallerandthus stance, TREC-COVID (in BEIR) annotates the
moreefficient(i.e.,bydecouplingknowledgefrom poolofdocumentsretrievedbythesystemssubmit-
computation),moretransparent(i.e.,byallowing tedatthetimeofthecompetition,LoTTEusesau-
userstocheckthesourcesthemodelreliedonwhen tomaticGooglerankings(for“search”queries)and
makingaclaimorprediction),andeasiertoupdate StackExchangequestion–answerpairs(for“forum”
(i.e.,byallowingdeveloperstoreplaceoradddoc- queries), and the Open-QA tests rely on passage-
umentstothecorpuswithoutretrainingthemodel) answeroverlapforfactoidquestions. ColBERTv2
(Guuetal.,2020;Borgeaudetal.,2021;Khattab performedwellinallofthesesettings. Wediscuss
etal.,2021a). Nonetheless,suchworkposesrisks otherissuespertinenttoLoTTEinAppendix§D.
intermsofmisuse,particularlytowardmisinforma- Wehavecomparedwithawiderangeofstrong
tion,asretrievalcansurfaceresultsthatarerelevant baselines—including sparse retrieval and single-
yetinaccurate,dependingonthecontentsofacor- vectormodels—andfoundreliablepatternsacross
pus. Moreover, generalization from training on tests. However, we caution that empirical trends
a large-scale dataset can propagate the biases of canchangeasinnovationsareintroducedtoeachof
that dataset well beyond its typical reach to new thesefamiliesofmodelsandthatitcanbedifficult
domainsandapplications. toensureexactapple-to-applecomparisonsacross
WhileourcontributionshavemadeColBERT’s families of models, since each of them calls for
lateinteractionmoreefficientatstoragecosts,large- differentsophisticatedtuningstrategies. Wethus
scaledistillationwithhardnegativesincreasessys- primarily used results and models from the rich
tem complexity and accordingly increases train- recent literature on these problems, with models
ingcost,whencomparedwiththestraightforward likeRocketQAv2andSPLADEv2.
trainingparadigmoftheoriginalColBERTmodel. Ontherepresentationalside,wefocusonreduc-
WhileColBERTv2isefficientintermsoflatency ing the storage cost using residual compression,
andstorageatinferencetime,wesuspectthatun- achievingstronggainsinreducingfootprintwhile
derextremeresourceconstraints,simplermodelde- largely preserving quality. Nonetheless, we have
signslikeSPLADEv2orRocketQAv2couldlend notexhaustedthespaceofmoresophisticatedopti-
themselvestoeasier-to-optimizeenvironments. We mizationspossible,andwewouldexpectmoreso-
leave low-level systems optimizations of all sys- phisticatedformsofresidualcompressionandcom-
tems to future work. Another worthwhile di- posingourapproachwithdroppingtokens(Zhou
mension for future exploration of tradeoffs is re- andDevlin,2021)toopenuppossibilitiesforfur-
ranking architectures over various systems with therreductionsinspacefootprint.

References
|     |     |     |     |     |     |     | Zhuyun         | Dai and | Jamie | Callan.     | 2020.   | Context-aware |     |
| --- | --- | --- | --- | --- | --- | --- | -------------- | ------- | ----- | ----------- | ------- | ------------- | --- |
|     |     |     |     |     |     |     | term weighting |         | for   | first stage | passage | retrieval.    | In  |
StackExchangeDataDump.
|           |         |     |       |             |     |         | Proceedings |     | of the   | 43rd International |             | ACM | SIGIR     |
| --------- | ------- | --- | ----- | ----------- | --- | ------- | ----------- | --- | -------- | ------------------ | ----------- | --- | --------- |
|           |         |     |       |             |     |         | conference  | on  | research | and                | development |     | in Infor- |
| Liefu Ai, | Junqing | Yu, | Zebin | Wu, Yunfeng |     | He, and |             |     |          |                    |             |     |           |
mationRetrieval,SIGIR2020,VirtualEvent,China,
| Tao Guan. | 2017. | Optimized |     | Residual | Vector | Quan- |     |     |     |     |     |     |     |
| --------- | ----- | --------- | --- | -------- | ------ | ----- | --- | --- | --- | --- | --- | --- | --- |
July25-30,2020,pages1533–1536.ACM.
tizationforEfficientApproximateNearestNeighbor
| Search. | MultimediaSystems,23(2):169–181. |     |     |     |     |     |               |     |          |        |        |     |          |
| ------- | -------------------------------- | --- | --- | --- | --- | --- | ------------- | --- | -------- | ------ | ------ | --- | -------- |
|         |                                  |     |     |     |     |     | Jacob Devlin, |     | Ming-Wei | Chang, | Kenton |     | Lee, and |
Sören Auer, Christian Bizer, Georgi Kobilarov, Jens Kristina Toutanova. 2019. BERT: Pre-training of
|          |         |           |     |     |         |       | deep      | bidirectional | transformers |     | for         | language   | under- |
| -------- | ------- | --------- | --- | --- | ------- | ----- | --------- | ------------- | ------------ | --- | ----------- | ---------- | ------ |
| Lehmann, | Richard | Cyganiak, |     | and | Zachary | Ives. |           |               |              |     |             |            |        |
|          |         |           |     |     |         |       | standing. | In            | Proceedings  |     | of the 2019 | Conference |        |
2007. DBpedia:ANucleusforaWebofOpenData.
|     |     |     |     |     |     |     | of the | North | American | Chapter | of  | the Association |     |
| --- | --- | --- | --- | --- | --- | --- | ------ | ----- | -------- | ------- | --- | --------------- | --- |
InThesemanticweb,pages722–735.Springer.
|             |     |         |        |        |            |     | for Computational |     |        | Linguistics: | Human |       | Language |
| ----------- | --- | ------- | ------ | ------ | ---------- | --- | ----------------- | --- | ------ | ------------ | ----- | ----- | -------- |
|             |     |         |        |        |            |     | Technologies,     |     | Volume | 1 (Long      | and   | Short | Papers), |
| Christopher | F   | Barnes, | Syed A | Rizvi, | and Nasser | M   |                   |     |        |              |       |       |          |
Nasrabadi. 1996. Advances in Residual Vector pages4171–4186,Minneapolis,Minnesota.Associ-
ationforComputationalLinguistics.
| Quantization: |     | A Review. | IEEE | transactions |     | on im- |     |     |     |     |     |     |     |
| ------------- | --- | --------- | ---- | ------------ | --- | ------ | --- | --- | --- | --- | --- | --- | --- |
ageprocessing,5(2):226–262.
|     |     |     |     |     |     |     | ThomasDiggelmann, |     | JordanBoyd-Graber, |     |     |     | JannisBu- |
| --- | --- | --- | --- | --- | --- | --- | ----------------- | --- | ------------------ | --- | --- | --- | --------- |
Alexander Bondarenko, Maik Fröbe, Meriem Be- lian,MassimilianoCiaramita,andMarkusLeippold.
loucif, Lukas Gienapp, Yamen Ajjour, Alexander 2020. CLIMATE-FEVER: A Dataset for Verifica-
Panchenko, Chris Biemann, Benno Stein, Henning tionofReal-WorldClimateClaims. arXivpreprint
arXiv:2012.00614.
| Wachsmuth,MartinPotthast,etal.2020. |       |          |     |            | Overview |          |     |     |     |     |     |     |     |
| ----------------------------------- | ----- | -------- | --- | ---------- | -------- | -------- | --- | --- | --- | --- | --- | --- | --- |
| of touché                           | 2020: | Argument |     | Retrieval. | In       | Interna- |     |     |     |     |     |     |     |
tional Conference of the Cross-Language Evalua- Thibault Formal, Carlos Lassance, Benjamin Pi-
tion Forum for European Languages, pages 384– wowarski, and Stéphane Clinchant. 2021a.
| 395.Springer. |           |        |     |         |        |       | SPLADE | v2:             | Sparse |            | Lexical | and   | Expansion |
| ------------- | --------- | ------ | --- | ------- | ------ | ----- | ------ | --------------- | ------ | ---------- | ------- | ----- | --------- |
|               |           |        |     |         |        |       | Model  | for Information |        | Retrieval. |         | arXiv | preprint  |
| Sebastian     | Borgeaud, | Arthur |     | Mensch, | Jordan | Hoff- |        |                 |        |            |         |       |           |
arXiv:2109.10086.
mann,TrevorCai,ElizaRutherford,KatieMillican,
George van den Driessche, Jean-Baptiste Lespiau, ThibaultFormal,BenjaminPiwowarski,andStéphane
Bogdan Damoc, Aidan Clark, et al. 2021. Improv- Clinchant.2021b. SPLADE:SparseLexicalandEx-
| ing language |                                | models | by retrieving | from | trillions | of  |                                   |          |               |             |     |                |         |
| ------------ | ------------------------------ | ------ | ------------- | ---- | --------- | --- | --------------------------------- | -------- | ------------- | ----------- | --- | -------------- | ------- |
|              |                                |        |               |      |           |     | pansionModelforFirstStageRanking. |          |               |             |     | InProceed-     |         |
| tokens.      | arXivpreprintarXiv:2112.04426. |        |               |      |           |     |                                   |          |               |             |     |                |         |
|              |                                |        |               |      |           |     | ings of                           | the 44th | International |             | ACM | SIGIR          | Confer- |
|              |                                |        |               |      |           |     | ence on                           | Research | and           | Development |     | in Information |         |
Vera Boteva, Demian Gholipour, Artem Sokolov, and Retrieval,pages2288–2292.
| StefanRiezler.2016.                     |     |         | AFull-textLearningtoRank |            |     |        |                             |          |     |       |                  |     |           |
| --------------------------------------- | --- | ------- | ------------------------ | ---------- | --- | ------ | --------------------------- | -------- | --- | ----- | ---------------- | --- | --------- |
| Dataset                                 | for | Medical | Information              | Retrieval. |     | In Eu- |                             |          |     |       |                  |     |           |
|                                         |     |         |                          |            |     |        | LuyuGaoandJamieCallan.2021. |          |     |       | Unsupervisedcor- |     |           |
| ropeanConferenceonInformationRetrieval, |     |         |                          |            |     | pages  |                             |          |     |       |                  |     |           |
|                                         |     |         |                          |            |     |        | pus aware                   | language |     | model | pre-training     |     | for dense |
716–722.Springer.
|          |         |               |             |                 |           |       | passageretrieval.                      |                  | arXivpreprintarXiv:2108.05540. |                 |         |            |           |
| -------- | ------- | ------------- | ----------- | --------------- | --------- | ----- | -------------------------------------- | ---------------- | ------------------------------ | --------------- | ------- | ---------- | --------- |
| Chia-Yu  | Chen,   | Jungwook      | Choi,       | Daniel          | Brand,    | Ankur |                                        |                  |                                |                 |         |            |           |
|          |         |               |             |                 |           |       | LuyuGao,ZhuyunDai,andJamieCallan.2020. |                  |                                |                 |         |            | Mod-      |
| Agrawal, | Wei     | Zhang,        | and Kailash | Gopalakrishnan. |           |       |                                        |                  |                                |                 |         |            |           |
|          |         |               |             |                 |           |       | ularized                               | transfomer-based |                                |                 | ranking | framework. | In        |
| 2018.    | Adacomp | : Adaptive    |             | residual        | gradient  | com-  |                                        |                  |                                |                 |         |            |           |
|          |         |               |             |                 |           |       | Proceedings                            |                  | of the                         | 2020 Conference |         | on         | Empirical |
| pression | for     | data-parallel | distributed |                 | training. | In    |                                        |                  |                                |                 |         |            |           |
MethodsinNaturalLanguageProcessing(EMNLP),
ProceedingsoftheThirty-SecondAAAIConference
pages4180–4190,Online.AssociationforComputa-
| on Artificial |     | Intelligence, | (AAAI-18), |     | the 30th | inno- |     |     |     |     |     |     |     |
| ------------- | --- | ------------- | ---------- | --- | -------- | ----- | --- | --- | --- | --- | --- | --- | --- |
tionalLinguistics.
| vative   | Applications | of         | Artificial   | Intelligence |                | (IAAI- |           |        |      |     |       |         |       |
| -------- | ------------ | ---------- | ------------ | ------------ | -------------- | ------ | --------- | ------ | ---- | --- | ----- | ------- | ----- |
| 18), and | the          | 8th AAAI   | Symposium    |              | on Educational |        |           |        |      |     |       |         |       |
|          |              |            |              |              |                |        | Luyu Gao, | Zhuyun | Dai, | and | Jamie | Callan. | 2021. |
| Advances | in           | Artificial | Intelligence | (EAAI-18),   |                | New    |           |        |      |     |       |         |       |
Orleans,Louisiana,USA,February2-7,2018,pages COIL: Revisit exact lexical match in information
|     |     |     |     |     |     |     | retrieval | with | contextualized |     | inverted | list. | In Pro- |
| --- | --- | --- | --- | --- | --- | --- | --------- | ---- | -------------- | --- | -------- | ----- | ------- |
2827–2835.AAAIPress.
ceedingsofthe2021ConferenceoftheNorthAmer-
|                   |        |                |          |          |             |       | ican Chapter |       | of the  | Association   | for           | Computational |           |
| ----------------- | ------ | -------------- | -------- | -------- | ----------- | ----- | ------------ | ----- | ------- | ------------- | ------------- | ------------- | --------- |
| Arman             | Cohan, | Sergey         | Feldman, | Iz       | Beltagy,    | Doug  |              |       |         |               |               |               |           |
|                   |        |                |          |          |             |       | Linguistics: |       | Human   | Language      | Technologies, |               | pages     |
| Downey,           | and    | Daniel         | Weld.    | 2020.    | SPECTER:    |       |              |       |         |               |               |               |           |
|                   |        |                |          |          |             |       | 3030–3042,   |       | Online. | Association   | for           | Computational |           |
| Document-level    |        | representation |          | learning |             | using |              |       |         |               |               |               |           |
| citation-informed |        | transformers.  |          | In       | Proceedings |       | Linguistics. |       |         |               |               |               |           |
| of the            | 58th   | Annual         | Meeting  | of the   | Association |       |              |       |         |               |               |               |           |
|                   |        |                |          |          |             |       | Robert Gray. | 1984. | Vector  | quantization. |               |               | IEEE Assp |
| for Computational |        | Linguistics,   |          | pages    | 2270–2282,  |       |              |       |         |               |               |               |           |
Magazine,1(2):4–29.
Online.AssociationforComputationalLinguistics.
Nachshon Cohen, Amit Portnoy, Besnik Fetahu, and Kelvin Guu, Kenton Lee, Zora Tung, Panupong Pasu-
Amir Ingber. 2021. SDR: Efficient Neural Re- pat,andMing-WeiChang.2020. Realm: Retrieval-
ranking using Succinct Document Representation. augmented language model pre-training. arXiv
| arXivpreprintarXiv:2110.02065. |     |     |     |     |     |     | preprintarXiv:2002.08909. |     |     |     |     |     |     |
| ------------------------------ | --- | --- | --- | --- | --- | --- | ------------------------- | --- | --- | --- | --- | --- | --- |

Sebastian Hofstätter, Sophia Althammer, Michael Omar Khattab, Christopher Potts, and Matei Zaharia.
Schröder, Mete Sertkan, and Allan Hanbury. 2020. 2021a. Baleen: Robust Multi-Hop Reasoning at
Improving Efficient Neural Ranking Models with ScaleviaCondensedRetrieval. InThirty-FifthCon-
Cross-Architecture Knowledge Distillation. arXiv ferenceonNeuralInformationProcessingSystems.
preprintarXiv:2010.02666.
|     |     |     |     |     |     |     | Omar Khattab, |     | Christopher | Potts, | and | Matei | Zaharia. |
| --- | --- | --- | --- | --- | --- | --- | ------------- | --- | ----------- | ------ | --- | ----- | -------- |
Sebastian Hofstätter, Sheng-Chieh Lin, Jheng-Hong 2021b. Relevance-guided supervision for openqa
Yang, Jimmy Lin, and Allan Hanbury. 2021. Effi- withColBERT. TransactionsoftheAssociationfor
| ciently | Teaching | an Effective | Dense |     | Retriever | with |     |     |     |     |     |     |     |
| ------- | -------- | ------------ | ----- | --- | --------- | ---- | --- | --- | --- | --- | --- | --- | --- |
ComputationalLinguistics,9:929–944.
| Balanced | Topic | Aware | Sampling. |     | arXiv | preprint |     |     |     |     |     |     |     |
| -------- | ----- | ----- | --------- | --- | ----- | -------- | --- | --- | --- | --- | --- | --- | --- |
arXiv:2104.06967.
|     |     |     |     |     |     |     | Omar Khattab | and           | Matei | Zaharia. | 2020.  | Colbert:        | Ef- |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ------------- | ----- | -------- | ------ | --------------- | --- |
|     |     |     |     |     |     |     | ficient      | and effective |       | passage  | search | via contextual- |     |
Samuel Humeau, Kurt Shuster, Marie-Anne Lachaux, Proceedings of
|           |         |       |                |     |           |     | ized late | interaction | over | BERT. | In  |     |     |
| --------- | ------- | ----- | -------------- | --- | --------- | --- | --------- | ----------- | ---- | ----- | --- | --- | --- |
| and Jason | Weston. | 2020. | Poly-encoders: |     | Architec- |     |           |             |      |       |     |     |     |
the43rdInternationalACMSIGIRconferenceonre-
turesandpre-trainingstrategiesforfastandaccurate
searchanddevelopmentinInformationRetrieval,SI-
| multi-sentencescoring. |          |                  | In8thInternationalConfer- |      |       |     |           |         |        |        |      |        |       |
| ---------------------- | -------- | ---------------- | ------------------------- | ---- | ----- | --- | --------- | ------- | ------ | ------ | ---- | ------ | ----- |
|                        |          |                  |                           |      |       |     | GIR 2020, | Virtual | Event, | China, | July | 25-30, | 2020, |
| ence on                | Learning | Representations, |                           | ICLR | 2020, | Ad- |           |         |        |        |      |        |       |
pages39–48.ACM.
| dis Ababa, | Ethiopia, |     | April 26-30, | 2020. |     |     |     |     |     |     |     |     |     |
| ---------- | --------- | --- | ------------ | ----- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
OpenRe-
view.net.
|     |     |     |     |     |     |     | Tom Kwiatkowski, |         | Jennimaria |       | Palomaki, | Olivia | Red-      |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | ------- | ---------- | ----- | --------- | ------ | --------- |
|     |     |     |     |     |     |     | field,           | Michael | Collins,   | Ankur | Parikh,   |        | Chris Al- |
GautierIzacard,FabioPetroni,LucasHosseini,Nicola
|     |     |     |     |     |     |     | berti, Danielle |     | Epstein, | Illia | Polosukhin, |     | Jacob De- |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | -------- | ----- | ----------- | --- | --------- |
DeCao,SebastianRiedel,andEdouardGrave.2020.
|          |           |          |     |      |        |       | vlin, Kenton |     | Lee, Kristina |     | Toutanova, | Llion | Jones, |
| -------- | --------- | -------- | --- | ---- | ------ | ----- | ------------ | --- | ------------- | --- | ---------- | ----- | ------ |
| A memory | efficient | baseline | for | open | domain | ques- |              |     |               |     |            |       |        |
tionanswering. arXivpreprintarXiv:2012.15156. MatthewKelcey,Ming-WeiChang,AndrewM.Dai,
|              |          |              |     |          |          |         | Jakob   | Uszkoreit, | Quoc         | Le,       | and Slav | Petrov.         | 2019. |
| ------------ | -------- | ------------ | --- | -------- | -------- | ------- | ------- | ---------- | ------------ | --------- | -------- | --------------- | ----- |
|              |          |              |     |          |          |         | Natural | questions: | A            | benchmark |          | for question    | an-   |
| Herve Jegou, | Matthijs | Douze,       | and | Cordelia |          | Schmid. |         |            |              |           |          |                 |       |
|              |          |              |     |          |          |         | swering | research.  | Transactions |           | of       | the Association |       |
| 2010.        | Product  | quantization | for | nearest  | neighbor |         |         |            |              |           |          |                 |       |
forComputationalLinguistics,7:452–466.
| search. | IEEE | transactions | on  | pattern | analysis | and |     |     |     |     |     |     |     |
| ------- | ---- | ------------ | --- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- | --- |
machineintelligence,33(1):117–128.
|     |     |     |     |     |     |     | Jinhyuk Lee, | Mujeen | Sung, | Jaewoo | Kang, | and | Danqi |
| --- | --- | --- | --- | --- | --- | --- | ------------ | ------ | ----- | ------ | ----- | --- | ----- |
Yichen Jiang, Shikha Bordia, Zheng Zhong, Charles Chen. 2021a. Learning dense representations of
Dognin, Maneesh Singh, and Mohit Bansal. 2020. phrasesatscale. InProceedingsofthe59thAnnual
HoVer: Adatasetformany-hopfactextractionand Meeting of the Association for Computational Lin-
claim verification. In Findings of the Association guisticsandthe11thInternationalJointConference
forComputationalLinguistics:EMNLP2020,pages on Natural Language Processing (Volume 1: Long
3441–3460, Online. Association for Computational Papers), pages 6634–6647, Online. Association for
| Linguistics.  |          |        |     |       |        |       | ComputationalLinguistics. |      |           |         |     |       |       |
| ------------- | -------- | ------ | --- | ----- | ------ | ----- | ------------------------- | ---- | --------- | ------- | --- | ----- | ----- |
| Jeff Johnson, | Matthijs | Douze, | and | Hervé | Jégou. | 2019. |                           |      |           |         |     |       |       |
|               |          |        |     |       |        |       | Jinhyuk                   | Lee, | Alexander | Wettig, | and | Danqi | Chen. |
Billion-scale similarity search with gpus. IEEE 2021b. Phraseretrievallearnspassageretrieval,too.
| TransactionsonBigData. |        |       |        |       |     |      | arXivpreprintarXiv:2109.08133. |     |     |     |     |     |     |
| ---------------------- | ------ | ----- | ------ | ----- | --- | ---- | ------------------------------ | --- | --- | --- | --- | --- | --- |
| Mandar Joshi,          | Eunsol | Choi, | Daniel | Weld, | and | Luke |                                |     |     |     |     |     |     |
KentonLee,Ming-WeiChang,andKristinaToutanova.
| Zettlemoyer. |     | 2017. TriviaQA: |     | A large | scale | dis- |       |        |           |            |     |            |      |
| ------------ | --- | --------------- | --- | ------- | ----- | ---- | ----- | ------ | --------- | ---------- | --- | ---------- | ---- |
|              |     |                 |     |         |       |      | 2019. | Latent | retrieval | for weakly |     | supervised | open |
tantlysupervisedchallengedatasetforreadingcom-
|     |     |     |     |     |     |     | domain | question | answering. |     | In Proceedings |     | of the |
| --- | --- | --- | --- | --- | --- | --- | ------ | -------- | ---------- | --- | -------------- | --- | ------ |
InProceedingsofthe55thAnnualMeet-
| prehension. |     |     |     |     |     |     | 57th Annual |     | Meeting | of the | Association |     | for Com- |
| ----------- | --- | --- | --- | --- | --- | --- | ----------- | --- | ------- | ------ | ----------- | --- | -------- |
ingoftheAssociationforComputationalLinguistics
|         |         |          |       |            |     |      | putational | Linguistics, |     | pages | 6086–6096, |     | Florence, |
| ------- | ------- | -------- | ----- | ---------- | --- | ---- | ---------- | ------------ | --- | ----- | ---------- | --- | --------- |
| (Volume | 1: Long | Papers), | pages | 1601–1611, |     | Van- |            |              |     |       |            |     |           |
Italy.AssociationforComputationalLinguistics.
couver,Canada.AssociationforComputationalLin-
guistics.
|     |     |     |     |     |     |     | Yue Li, Wenrui |     | Ding, Chunlei |     | Liu, Baochang |     | Zhang, |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ------------- | --- | ------------- | --- | ------ |
VladimirKarpukhin,BarlasOguz,SewonMin,Patrick and Guodong Guo. 2021a. TRQ: Ternary Neural
|     |     |     |     |     |     |     | Networks | With | Residual | Quantization. |     | In  | Proceed- |
| --- | --- | --- | --- | --- | --- | --- | -------- | ---- | -------- | ------------- | --- | --- | -------- |
Lewis,LedellWu,SergeyEdunov,DanqiChen,and
|         |      |       |               |     |           |     | ings of | the | AAAI Conference |     | on  | Artificial | Intelli- |
| ------- | ---- | ----- | ------------- | --- | --------- | --- | ------- | --- | --------------- | --- | --- | ---------- | -------- |
| Wen-tau | Yih. | 2020. | Dense passage |     | retrieval | for |         |     |                 |     |     |            |          |
gence,volume35,pages8538–8546.
| open-domainquestionanswering. |            |     |           | InProceedingsof |     |         |     |     |     |     |     |     |     |
| ----------------------------- | ---------- | --- | --------- | --------------- | --- | ------- | --- | --- | --- | --- | --- | --- | --- |
| the 2020                      | Conference | on  | Empirical | Methods         |     | in Nat- |     |     |     |     |     |     |     |
ural Language Processing (EMNLP), pages 6769– ZefanLi,BingbingNi,TengLi,XiaokangYang,Wen-
|       |         |             |     |               |     |      | jun Zhang, | and     | Wen       | Gao. 2021b. | Residual  |     | Quanti- |
| ----- | ------- | ----------- | --- | ------------- | --- | ---- | ---------- | ------- | --------- | ----------- | --------- | --- | ------- |
| 6781, | Online. | Association | for | Computational |     | Lin- |            |         |           |             |           |     |         |
|       |         |             |     |               |     |      | zation     | for Low | Bit-width | Neural      | Networks. |     | IEEE    |
guistics.
TransactionsonMultimedia.
DanielKhashabi,AmosNg,TusharKhot,AshishSab-
harwal, Hannaneh Hajishirzi, and Chris Callison- Jimmy Lin and Xueguang Ma. 2021. A Few Brief
Burch. 2021. GooAQ: Open Question Answer- Notes on DeepImpact, COIL, and a Conceptual
ing with Diverse Answer Types. arXiv preprint Framework for Information Retrieval Techniques.
| arXiv:2104.08727. |     |     |     |     |     |     | arXivpreprintarXiv:2106.14807. |     |     |     |     |     |     |
| ----------------- | --- | --- | --- | --- | --- | --- | ------------------------------ | --- | --- | --- | --- | --- | --- |

Sheng-Chieh Lin, Jheng-Hong Yang, and Jimmy Lin. Barlas Og˘uz, Kushal Lakhotia, Anchit Gupta, Patrick
2020. Distilling Dense Representations for Rank- Lewis, Vladimir Karpukhin, Aleksandra Piktus,
ingusingTightly-CoupledTeachers. arXivpreprint Xilun Chen, Sebastian Riedel, Wen-tau Yih, Sonal
arXiv:2010.11386. Gupta, et al. 2021. Domain-matched Pre-training
Tasks for Dense Retrieval. arXiv preprint
Xiaorui Liu, Yao Li, Jiliang Tang, and Ming Yan. arXiv:2107.13602.
2020. A double residual compression algorithm
for efficient distributed learning. In The 23rd In- Ashwin Paranjape, Omar Khattab, Christopher Potts,
ternationalConferenceonArtificialIntelligenceand Matei Zaharia, and Christopher D Manning. 2022.
Statistics, AISTATS 2020, 26-28 August 2020, On- Hindsight:Posterior-guidedtrainingofretrieversfor
line[Palermo,Sicily,Italy],volume108ofProceed- improved open-ended generation. In International
ingsofMachineLearningResearch,pages133–143. ConferenceonLearningRepresentations.
PMLR.
Yingqi Qu, Yuchen Ding, Jing Liu, Kai Liu, Ruiyang
Ren, Wayne Xin Zhao, Daxiang Dong, Hua Wu,
Yi Luan, Jacob Eisenstein, Kristina Toutanova, and
and Haifeng Wang. 2021. RocketQA: An opti-
Michael Collins. 2021. Sparse, Dense, and Atten-
mized training approach to dense passage retrieval
tional Representations for Text Retrieval. Transac-
for open-domain question answering. In Proceed-
tions of the Association for Computational Linguis-
ings of the 2021 Conference of the North Ameri-
tics,9:329–345.
can Chapter of the Association for Computational
Linguistics: Human Language Technologies, pages
Sean MacAvaney, Franco Maria Nardini, Raffaele
5835–5847, Online. Association for Computational
Perego, Nicola Tonellotto, Nazli Goharian, and
Linguistics.
OphirFrieder.2020. Efficientdocumentre-ranking
for transformers by precomputing term representa-
PranavRajpurkar,JianZhang,KonstantinLopyrev,and
tions. InProceedingsofthe43rdInternationalACM
PercyLiang.2016. SQuAD:100,000+questionsfor
SIGIR conference on research and development in
machine comprehension of text. In Proceedings of
Information Retrieval, SIGIR 2020, Virtual Event,
the2016ConferenceonEmpiricalMethodsinNatu-
China,July25-30,2020,pages49–58.ACM.
ralLanguageProcessing,pages2383–2392,Austin,
Texas.AssociationforComputationalLinguistics.
Craig Macdonald and Nicola Tonellotto. 2021. On
approximate nearest neighbour selection for multi- Ruiyang Ren, Shangwen Lv, Yingqi Qu, Jing Liu,
stage dense retrieval. In Proceedings of the 30th WayneXinZhao, QiaoQiaoShe, HuaWu, Haifeng
ACM International Conference on Information & Wang, and Ji-Rong Wen. 2021a. PAIR: Leverag-
KnowledgeManagement,pages3318–3322. ingpassage-centricsimilarityrelationforimproving
dense passage retrieval. In Findings of the Associ-
Macedo Maia, Siegfried Handschuh, André Freitas, ation for Computational Linguistics: ACL-IJCNLP
BrianDavis,RossMcDermott,ManelZarrouk,and 2021, pages 2173–2183, Online. Association for
Alexandra Balahur. 2018. WWW’18 Open Chal- ComputationalLinguistics.
lenge: Financial Opinion Mining and Question An-
swering. InCompanionProceedingsoftheTheWeb Ruiyang Ren, Yingqi Qu, Jing Liu, Wayne Xin Zhao,
Conference2018,pages1941–1942. Qiaoqiao She, Hua Wu, Haifeng Wang, and Ji-
Rong Wen. 2021b. RocketQAv2: A Joint Training
MethodforDensePassageRetrievalandPassageRe-
Antonio Mallia, Omar Khattab, Torsten Suel, and
ranking. arXivpreprintarXiv:2110.07367.
NicolaTonellotto. 2021. Learningpassage impacts
for inverted indexes. In Proceedings of the 44th
Stephen E Robertson, Steve Walker, Susan Jones,
International ACM SIGIR Conference on Research
MichelineMHancock-Beaulieu,MikeGatford,etal.
and Development in Information Retrieval, pages
1995. OkapiatTREC-3. NISTSpecialPublication.
1723–1727.
Nandan Thakur, Nils Reimers, Andreas Rücklé, Ab-
Aditya Krishna Menon, Sadeep Jayasumana, Se-
hishekSrivastava,andIrynaGurevych.2021. BEIR:
ungyeonKim,AnkitSinghRawat,SashankJ.Reddi,
A Heterogenous Benchmark for Zero-shot Eval-
and Sanjiv Kumar. 2022. In defense of dual-
uation of Information Retrieval Models. arXiv
encodersforneuralranking.
preprintarXiv:2104.08663.
Tri Nguyen, Mir Rosenberg, Xia Song, Jianfeng Gao, James Thorne, Andreas Vlachos, Christos
Saurabh Tiwary, Rangan Majumder, and Li Deng. Christodoulopoulos, and Arpit Mittal. 2018.
2016. MSMARCO: A human-generated MAchine FEVER: a large-scale dataset for fact extraction
reading COmprehension dataset. arXiv preprint and VERification. In Proceedings of the 2018
arXiv:1611.09268. Conference of the North American Chapter of
the Association for Computational Linguistics:
Rodrigo Nogueira and Kyunghyun Cho. 2019. Pas- Human Language Technologies, Volume 1 (Long
sage Re-ranking with BERT. arXiv preprint Papers), pages 809–819, New Orleans, Louisiana.
arXiv:1901.04085. AssociationforComputationalLinguistics.

Ellen Voorhees, Tasmeer Alam, Steven Bedrick, Dina Joint Conference on Natural Language Processing
Demner-Fushman,WilliamRHersh,KyleLo,Kirk (Volume 2: Short Papers), pages 979–986, Online.
Roberts, Ian Soboroff, and Lucy Lu Wang. 2021. AssociationforComputationalLinguistics.
| TREC-COVID:    | Constructing |             | a   | Pandemic | Informa-  |                               |           |             |           |                 |              |     |
| -------------- | ------------ | ----------- | --- | -------- | --------- | ----------------------------- | --------- | ----------- | --------- | --------------- | ------------ | --- |
|                |              |             |     |          |           | Ikuya Yamada,                 |           | Akari Asai, | and       | Hannaneh        | Hajishirzi.  |     |
| tion Retrieval | Test         | Collection. |     | In ACM   | SIGIR Fo- |                               |           |             |           |                 |              |     |
|                |              |             |     |          |           | 2021b.                        | Efficient | passage     | retrieval |                 | with hashing | for |
| rum, volume    | 54,          | pages 1–12. | ACM | New      | York, NY, |                               |           |             |           |                 |              |     |
| USA.           |              |             |     |          |           | open-domainquestionanswering. |           |             |           | InProceedingsof |              |     |
the59thAnnualMeetingoftheAssociationforCom-
HenningWachsmuth,ShahbazSyed,andBennoStein. putational Linguistics and the 11th International
2018. Retrieval of the best counterargument with- Joint Conference on Natural Language Processing
out prior topic knowledge. In Proceedings of the (Volume 2: Short Papers), pages 979–986, Online.
56th Annual Meeting of the Association for Com- AssociationforComputationalLinguistics.
| putational | Linguistics | (Volume |     | 1: Long | Papers), |     |     |     |     |     |     |     |
| ---------- | ----------- | ------- | --- | ------- | -------- | --- | --- | --- | --- | --- | --- | --- |
pages 241–251, Melbourne, Australia. Association Peilin Yang, Hui Fang, and Jimmy Lin. 2018a.
forComputationalLinguistics. Anserini: Reproducible ranking baselines using
|                 |           |             |      |          |            | lucene.            | Journal | of Data | and | Information |     | Quality |
| --------------- | --------- | ----------- | ---- | -------- | ---------- | ------------------ | ------- | ------- | --- | ----------- | --- | ------- |
| David Wadden,   | Shanchuan |             | Lin, | Kyle Lo, | Lucy Lu    | (JDIQ),10(4):1–20. |         |         |     |             |     |         |
| Wang, Madeleine |           | van Zuylen, |      | Arman    | Cohan, and |                    |         |         |     |             |     |         |
ZhilinYang,PengQi,SaizhengZhang,YoshuaBengio,
| Hannaneh | Hajishirzi. | 2020. | Fact | or fiction: | Verify- |     |     |     |     |     |     |     |
| -------- | ----------- | ----- | ---- | ----------- | ------- | --- | --- | --- | --- | --- | --- | --- |
ing scientific claims. In Proceedings of the 2020 WilliamCohen, RuslanSalakhutdinov, andChristo-
Conference on Empirical Methods in Natural Lan- pher D. Manning. 2018b. HotpotQA: A dataset
guageProcessing(EMNLP),pages7534–7550,On- for diverse, explainable multi-hop question answer-
line.AssociationforComputationalLinguistics. ing. InProceedingsofthe2018ConferenceonEm-
|              |      |         |       |        |          | pirical | Methods    | in Natural |     | Language | Processing, |     |
| ------------ | ---- | ------- | ----- | ------ | -------- | ------- | ---------- | ---------- | --- | -------- | ----------- | --- |
| Wenhui Wang, | Furu | Wei, Li | Dong, | Hangbo | Bao, Nan |         |            |            |     |          |             |     |
|              |      |         |       |        |          | pages   | 2369–2380, | Brussels,  |     | Belgium. | Association |     |
Yang, and Ming Zhou. 2020. MiniLM: Deep Self- forComputationalLinguistics.
| Attention | Distillation | for | Task-Agnostic |     | Compres- |     |     |     |     |     |     |     |
| --------- | ------------ | --- | ------------- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
sion of Pre-Trained Transformers. arXiv preprint JingtaoZhan,JiaxinMao,YiqunLiu,JiafengGuo,Min
arXiv:2002.10957. Zhang, and Shaoping Ma. 2021a. Jointly Optimiz-
ingQueryEncoderandProductQuantizationtoIm-
Benchang Wei, Tao Guan, and Junqing Yu. 2014. proveRetrievalPerformance. InProceedingsofthe
Projected Residual Vector Quantization for ANN 30thACMInternationalConferenceonInformation
Search. IEEEmultimedia,21(3):41–51. &KnowledgeManagement,pages2487–2496.
Thomas Wolf, Lysandre Debut, Victor Sanh, Julien JingtaoZhan,JiaxinMao,YiqunLiu,JiafengGuo,Min
Chaumond, ClementDelangue, AnthonyMoi, Pier- Zhang,andShaopingMa.2021b. OptimizingDense
ric Cistac, Tim Rault, Remi Louf, Morgan Funtow- Retrieval Model Training with Hard Negatives. In
| icz, Joe | Davison, | Sam Shleifer, |     | Patrick | von Platen, |             |     |             |               |     |     |       |
| -------- | -------- | ------------- | --- | ------- | ----------- | ----------- | --- | ----------- | ------------- | --- | --- | ----- |
|          |          |               |     |         |             | Proceedings |     | of the 44th | International |     | ACM | SIGIR |
Clara Ma, Yacine Jernite, Julien Plu, Canwen Xu, Conference on Research and Development in Infor-
Teven Le Scao, Sylvain Gugger, Mariama Drame, mationRetrieval,pages1503–1512.
| Quentin | Lhoest, and | Alexander |     | Rush. | 2020. Trans- |     |     |     |     |     |     |     |
| ------- | ----------- | --------- | --- | ----- | ------------ | --- | --- | --- | --- | --- | --- | --- |
formers: State-of-the-art natural language process- JingtaoZhan,JiaxinMao,YiqunLiu,JiafengGuo,Min
ing. InProceedingsofthe2020ConferenceonEm- Zhang, and Shaoping Ma. 2022. Learning discrete
pirical Methods in Natural Language Processing: representations via constrained clustering for effec-
SystemDemonstrations,pages38–45,Online.Asso- tive and efficient dense retrieval. In Proceedings
ciationforComputationalLinguistics. of the Fifteenth ACM International Conference on
|     |     |     |     |     |     | Web Search |     | and Data | Mining, | WSDM | ’22, | page |
| --- | --- | --- | --- | --- | --- | ---------- | --- | -------- | ------- | ---- | ---- | ---- |
Ji Xin, Chenyan Xiong, Ashwin Srinivasan, Ankita 1328–1336.AssociationforComputingMachinery.
| Sharma, | Damien | Jose, and | Paul | N Bennett. | 2021. |     |     |     |     |     |     |     |
| ------- | ------ | --------- | ---- | ---------- | ----- | --- | --- | --- | --- | --- | --- | --- |
Zero-Shot Dense Retrieval with Momentum Adver- JingtaoZhan,JiaxinMao,YiqunLiu,MinZhang,and
|               |           |     |                  |     |       | Shaoping | Ma. | 2020a. | Learning | to  | retrieve: | How |
| ------------- | --------- | --- | ---------------- | --- | ----- | -------- | --- | ------ | -------- | --- | --------- | --- |
| sarial Domain | Invariant |     | Representations. |     | arXiv |          |     |        |          |     |           |     |
preprintarXiv:2110.07581. to train a dense retrieval model effectively and ef-
|            |         |        |        |           |       | ficiently. | arXivpreprintarXiv:2010.10469. |     |     |     |     |     |
| ---------- | ------- | ------ | ------ | --------- | ----- | ---------- | ------------------------------ | --- | --- | --- | --- | --- |
| Lee Xiong, | Chenyan | Xiong, | Ye Li, | Kwok-Fung | Tang, |            |                                |     |     |     |     |     |
Jialin Liu, Paul N Bennett, Junaid Ahmed, and JingtaoZhan,JiaxinMao,YiqunLiu,MinZhang,and
Arnold Overwijk. 2020. Approximate Nearest ShaopingMa.2020b. Repbert: Contextualizedtext
Neighbor Negative Contrastive Learning for Dense embeddings for first-stage retrieval. arXiv preprint
| Text Retrieval. |     | In International |     | Conference | on  | arXiv:2006.15498. |     |     |     |     |     |     |
| --------------- | --- | ---------------- | --- | ---------- | --- | ----------------- | --- | --- | --- | --- | --- | --- |
LearningRepresentations.
|     |     |     |     |     |     | Giulio Zhou | and | Jacob | Devlin. | 2021. | Multi-vector |     |
| --- | --- | --- | --- | --- | --- | ----------- | --- | ----- | ------- | ----- | ------------ | --- |
Ikuya Yamada, Akari Asai, and Hannaneh Hajishirzi. attention models for deep re-ranking. In Proceed-
2021a. Efficient passage retrieval with hashing for ings of the 2021 Conference on Empirical Methods
open-domainquestionanswering. InProceedingsof inNaturalLanguageProcessing,pages5452–5456,
the59thAnnualMeetingoftheAssociationforCom- OnlineandPuntaCana,DominicanRepublic.Asso-
putational Linguistics and the 11th International ciationforComputationalLinguistics.

ColBERT Random
100
75
50
25
0
1 16 256 4096
# Distinct Tokens per Cluster
noitroporP
100
75
50
25
0
4 64 1024
# Distinct Clusters per Token
(a)Numberofdistincttokens
appearingineachcluster.
noitroporP
theColBERTembeddings,whereaslessthan50%
ofclustershave≤16distincttokenswiththeran-
domembeddings. Thissuggeststhatthecentroids
effectivelymaptheColBERTsemanticspace.
Table 6 presents examples to highlight the se-
manticspacecapturedbythecentroids. Themost
frequentlyappearingtokensincluster#917relate
tophotography;theseinclude,forexample,‘pho-
tos’ and ‘photographs’. If we then examine the
(b) Number of distinct clus- additional clusters in which these tokens appear,
terseachtokenappearsin.
we find that there is substantial semantic overlap
between these new clusters (e.g., Photos-Photo,
Figure 2: Empirical CDFs analyzing semantic proper-
ties of MS MARCO token-level embeddings both en- Photo-Image-Picture) and cluster #917. We ob-
codedbyColBERTandrandomlygenerated. Theem- serveasimilareffectwithtokensappearinginclus-
beddings are partitioned into 218 clusters and corre- ter#216932,comprisingtornado-relatedterms.
spondtoroughly27,000distincttokens.
Thisanalysisindicatesthatclustercentroidscan
summarizetheColBERTrepresentationswithhigh
precision. In§3.3,weproposearesidualcompres-
A AnalysisofColBERT’sSemantic
sion mechanism that uses these centroids along
Space
with minor refinements at the dimension level to
ColBERT(KhattabandZaharia,2020)decomposes efficientlyencodelate-interactionvectors.
representationsandsimilaritycomputationatthe
B ImpactofCompression
token level. Because of this compositional archi-
tecture, we hypothesize that ColBERT exhibits a
Our residual compression approach (§3.3) pre-
“lightweight”semanticspace: withoutanyspecial
serves approximately the same quality as the un-
re-training,vectorscorrespondingtoeachsenseof
compressed embeddings. In particular, when ap-
awordwouldclusterveryclosely,withonlyminor
pliedtoavanillaColBERTmodelonMSMARCO
variationduetocontext.
whose MRR@10 is 36.2% and Recall@50 is
If this hypothesis is true, we would expect the
82.1%,thequalityofthemodelwith2-bitcompres-
embeddings corresponding to each token in the
sion is 36.2% MRR@10 and 82.3% Recall@50.
vocabulary to localize in only a small number of
With1-bitcompression,themodelachieves35.5%
regions in the embedding space, corresponding MRR@10and81.6%Recall@50.7
to the contextual “senses” of the token. To val-
We also tested the residual compression ap-
idate this hypothesis, we analyze the ColBERT
proach on late-interaction retrievers that conduct
embeddings corresponding to the tokens in the
downstream tasks, namely, ColBERT-QA (Khat-
MS MARCO Passage Ranking (Nguyen et al.,
tab et al., 2021b) for the NaturalQuestions open-
2016)collection: weperformk-meansclustering
domainQAtask,andBaleen(Khattabetal.,2021a)
onthenearly600Membeddings—corresponding
formulti-hopreasoningonHoVerforclaimverifi-
to 27,000 unique tokens—into k = 218 clusters.
cation. On the NQ dev set, ColBERT-QA’s suc-
As a baseline, we repeat this clustering with ran-
cess@5 (success@20) dropped only marginally
domembeddingsbutkeepthetruedistributionof
from 75.3% (84.3%) to 74.3% (84.2%) and
tokens. Figure2presentsempiricalcumulativedis-
its downstream Open-QA answer exact match
tribution function (eCDF) plots representing the
dropped from 47.9% to 47.7%, when using 2-bit
number of distinct non-stopword tokens appear-
compressionforretrievalandusingthesamecheck-
ingineachcluster(2a)andthenumberofdistinct
pointsofColBERT-QAotherwise.
clustersinwhicheachtokenappears(2b).6 Most
tokensappearinaverysmallfractionofthenum- 7Wecontrastthiswithanearlyimplementationofcom-
berofcentroids: inparticular,weseethatroughly pressionforColBERT,whichusedbinaryrepresentationsas
in BPR (Yamada et al., 2021a) without residual centroids,
90% of clusters have ≤ 16 distinct tokens with
andachieves34.8%(35.7%)MRR@10and80.5%(81.8%)
Recall@50with1-bit(2-bit)binarization. Liketheoriginal
6Weranktokensbynumberofclusterstheyappearinand ColBERT,thisformofcompressionreliedonaseparateFAISS
designatethetop-1%(under300)asstopwords. indexforcandidategeneration.

MostCommonClustersPerToken
ClusterID MostCommonTokens
Token Clusters
‘photos’,‘photo’,‘pictures’, ‘photos’ Photos-Photo,Photos-Pictures-Photo
917 ‘photographs’,‘images’,
‘photo’ Photo-Image-Picture,Photo-Picture-Photograph,Photo-Picture-Photography
‘photography’,‘photograph’
‘pictures’ Pictures-Picture-Images,Picture-Pictures-Artists,Pictures-Photo-Picture
‘tornado’ Tornado-Hurricane-Storm,Tornadoes-Tornado-Blizzard
‘tornado’,‘tornadoes’,‘storm’
216932
‘hurricane’,‘storms’ ‘tornadoes’ Tornadoes-Tornado-Storms,Tornadoes-Tornado-Blizzard,Tornado-Hurricane-Storm
‘storm’ Storm-Storms,Storm-Storms-Weather,Storm-Storms-Tempest
Table 6: Examples of clusters taken from all MS MARCO passages. We present the tokens that appear most
frequentlyintheselectedclustersaswellasadditionalclustersthetoptokensappearin.
250
200
150
100
50
38.50 38.75 39.00 39.25 39.50 39.75
MRR@10
)sm(
ycnetaL
yreuQ
MS MARCO LoTTE Pooled (dev) LoTTE Lifestyle (dev)
probe
1
2
4
bits
2
1
candidates
probe x 2^14
probe x 2^12
68.0 68.5 69.0 69.5 74.0 74.5 75.0 75.5 76.0
Success@5 Success@5
Figure3: Latencyvs. retrievalqualitywithvaryingparameterconfigurationsforthreedatasetsofdifferentcollec-
tion sizes. We sweep a range of values for the number of centroids per vector (probe), the number of bits used
forresidualcompression,andthenumberofcandidates. NotethatretrievalqualityismeasuredinMRR@10for
MSMARCOandSuccess@5forLoTTEdatasets. Resultstowardthebottomrightcorner(higherquality, lower
latency)arebest.

| Similarly,ontheHoVer(Jiangetal.,2020)dev   |     |     |     |     |     |     | Writing    |     |     |     |     |     |     |
| ------------------------------------------ | --- | --- | --- | --- | --- | --- | ---------- | --- | --- | --- | --- | --- | --- |
| set,Baleen’sretrievalR@100droppedfrom92.2% |     |     |     |     |     |     | Recreation |     |     |     |     |     |     |
Science
| to only | 90.6% | but its | sentence-level |     | exact | match |     |     |     |     |     |     |     |
| ------- | ----- | ------- | -------------- | --- | ----- | ----- | --- | --- | --- | --- | --- | --- | --- |
Technology
| remainedroughlythesame,goingfrom39.2%to |                                      |     |     |     |     |     | Lifestyle |     |       |     |     |     |     |
| --------------------------------------- | ------------------------------------ | --- | --- | --- | --- | --- | --------- | --- | ----- | --- | --- | --- | --- |
| 39.4%.                                  | Wehypothesizethatthesupervisionmeth- |     |     |     |     |     | Pooled    |     |       |     |     |     |     |
|                                         |                                      |     |     |     |     |     |           |     | 0 200 |     | 400 |     | 600 |
odsappliedinColBERTv2(§3.2)canalsobeap-
Words per passage
pliedtoliftqualityindownstreamtasksbyimprov-
|                                       |     |     |     |     |     |         |     | Figure4: | LoTTEwordsperpassage |     |     |     |     |
| ------------------------------------- | --- | --- | --- | --- | --- | ------- | --- | -------- | -------------------- | --- | --- | --- | --- |
| ingtherecallofretrievalforthesetasks. |     |     |     |     |     | Weleave |     |          |                      |     |     |     |     |
suchexplorationforfuturework.
[Search] Writing
[Search] Recreation
C RetrievalLatency
[Search] Science
[Search] Technology
| Figure | 3 evaluates |     | the latency |     | of ColBERTv2 |     |     |     |     |     |     |     |     |
| ------ | ----------- | --- | ----------- | --- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
[Search] Lifestyle
| across three | collections |     | of  | varying | sizes, | namely, | [Search] Pooled |     |     |     |     |     |     |
| ------------ | ----------- | --- | --- | ------- | ------ | ------- | --------------- | --- | --- | --- | --- | --- | --- |
[Forum] Writing
| MS MARCO,                                  |     | LoTTE | Pooled | (dev), | and | LoTTE | [Forum] Recreation |     |     |     |     |     |     |
| ------------------------------------------ | --- | ----- | ------ | ------ | --- | ----- | ------------------ | --- | --- | --- | --- | --- | --- |
| Lifestyle(dev),whichcontainapproximately9M |     |       |        |        |     |       | [Forum] Science    |     |     |     |     |     |     |
[Forum] Technology
| passages, | 2.4M | answer | posts, | and | 270k | answer | [Forum] Lifestyle |     |     |     |     |     |     |
| --------- | ---- | ------ | ------ | --- | ---- | ------ | ----------------- | --- | --- | --- | --- | --- | --- |
[Forum] Pooled
| posts,respectively. |        | Weaveragelatencyacrossthree |     |     |         |       |     |     |     |     |     |     |     |
| ------------------- | ------ | --------------------------- | --- | --- | ------- | ----- | --- | --- | --- | --- | --- | --- | --- |
|                     |        |                             |     |     |         |       |     |     | 5   |     | 10  | 15  | 20  |
| runs of             | the MS | MARCO                       | dev | set | and the | LoTTE |     |     |     |     |     |     |     |
Words per query
| “search”queries. |     | SearchisexecutedusingaTitan |     |     |     |     |     |          |                    |     |     |     |     |
| ---------------- | --- | --------------------------- | --- | --- | --- | --- | --- | -------- | ------------------ | --- | --- | --- | --- |
|                  |     |                             |     |     |     |     |     | Figure5: | LoTTEwordsperquery |     |     |     |     |
VGPUonaserverwithtwoIntelXeonGold6132
CPUs,eachwith28hardwareexecutioncontexts.
ThefigurevariesthreesettingsofColBERTv2. ThetopicscoveredbyLoTTEcoverawiderange
Inparticular,weevaluateindexingwith1-bitand oflinguisticphenomenagiventhediversityintop-
2-bitencoding(§3.4)andsearchingbyprobingthe icsandcommunitiesrepresented. However,since
nearest 1, 2, or 4 centroids to each query vector allpostsaresubmittedbyanonymoususerswedo
(§3.5). Whenprobingprobecentroidspervector, not have demographic information regarding the
| wescoreeitherprobe×212 |     |     |     | orprobe×214 |     |        |          |     |                   |     |       |     |         |
| ---------------------- | --- | --- | --- | ----------- | --- | ------ | -------- | --- | ----------------- | --- | ----- | --- | ------- |
|                        |     |     |     |             |     | candi- | identify | of  | the contributors. | All | posts | are | written |
datesperquery.8
inEnglish.
Tobeginwith,wenoticethatthequalityreported
|     |     |     |     |     |     |     | Passages |     | As mentioned | in  | §4, | we construct |     |
| --- | --- | --- | --- | --- | --- | --- | -------- | --- | ------------ | --- | --- | ------------ | --- |
onthex-axisvariesonlywithinarelativelynarrow
LoTTEcollectionsbyselectingpassagesfromthe
| range. | For instance, |     | the axis | ranges | from | 38.50 |               |     |         |               |     |         |     |
| ------ | ------------- | --- | -------- | ------ | ---- | ----- | ------------- | --- | ------- | ------------- | --- | ------- | --- |
|        |               |     |          |        |      |       | StackExchange |     | archive | with positive |     | scores. | We  |
through39.75forMSMARCO,andallbuttwoof
|                                     |        |         |     |               |     |            | remove | HTML      | tags from | passages |     | and filter | out |
| ----------------------------------- | ------ | ------- | --- | ------------- | --- | ---------- | ------ | --------- | --------- | -------- | --- | ---------- | --- |
| thecheapestsettingsscoreabove39.00. |        |         |     |               |     | Similarly, |        |           |           |          |     |            |     |
|                                     |        |         |     |               |     |            | empty  | passages. | For each  | passage  |     | we record  | its |
| the y-axis                          | varies | between |     | approximately |     | 50 mil-    |        |           |           |          |     |            |     |
correspondingqueryandsavethequery-to-passage
lisecondsperqueryupto250milliseconds(mostly
mappingtokeeptrackofthepostedanswerscorre-
under150milliseconds)usingourrelativelysimple
spondingtoeachquery.
Python-basedimplementation.
Digging deeper, we see that the best quality Searchqueries WeconstructthelistofLoTTE
| in these | metrics | can | be achieved |     | or approached |     |        |         |            |      |       |     |         |
| -------- | ------- | --- | ----------- | --- | ------------- | --- | ------ | ------- | ---------- | ---- | ----- | --- | ------- |
|          |         |     |             |     |               |     | search | queries | by drawing | from | GooAQ |     | queries |
closely with around 100 milliseconds of latency thatappearintheStackExchangepostarchive. We
acrossallthreedatasets,despitetheirvarioussizes first shuffle the list of GooAQ queries so that in
andcharacteristics,andthat2-bitindexingreliably
|     |     |     |     |     |     |     | cases | where | multiple queries |     | exist | for the | same |
| --- | --- | --- | --- | --- | --- | --- | ----- | ----- | ---------------- | --- | ----- | ------- | ---- |
outperforms1-bitindexingbutthelossfrommore answer passage we randomly select the query to
aggressivecompressionissmall. includeinLoTTEratherthanalwaysselectingthe
|     |     |     |     |     |     |     | first | appearing | query. We | verify | that | every | query |
| --- | --- | --- | --- | --- | --- | --- | ----- | --------- | --------- | ------ | ---- | ----- | ----- |
D LoTTE
hasatleastonecorrespondinganswerpassage.
| Domain | coverage |     | Table | 9 presents | the | full dis- |       |         |          |       |     |       |         |
| ------ | -------- | --- | ----- | ---------- | --- | --------- | ----- | ------- | -------- | ----- | --- | ----- | ------- |
|        |          |     |       |            |     |           | Forum | queries | For each | LoTTE |     | topic | and its |
tributionofcommunitiesintheLoTTEdevdataset.
constituentcommunitieswefirstcomputethefrac-
8Thesesettingsareselectedbasedonpreliminaryexplo- tionofthetotalqueriesattributedtoeachindivid-
rationoftheseparameters,whichindicatedthatperformance
|     |     |     |     |     |     |     | ual community. |     | We then | use | this distribution |     | to  |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | ------- | --- | ----------------- | --- | --- |
forlargerprobevaluestendstorequirescoringalargernum-
|     |     |     |     |     |     |     | construct | a   | truncated query | set | by  | selecting | the |
| --- | --- | --- | --- | --- | --- | --- | --------- | --- | --------------- | --- | --- | --------- | --- |
berofcandidates.

| [Search] Writing |     |     |     |     |     |     | Licensing | and Anonymity |     | The | original | Stack- |
| ---------------- | --- | --- | --- | --- | --- | --- | --------- | ------------- | --- | --- | -------- | ------ |
[Search] Recreation Exchange post archive is licensed under a Cre-
[Search] Science
[Search] Technology ativeCommonsBY-SA4.0license(sta). Personal
[Search] Lifestyle
dataisremovedfromthearchivebeforebeingup-
[Search] Pooled
|     |     |     |     |     |     |     | loaded, | though all | posts | are public; | when | we re- |
| --- | --- | --- | --- | --- | --- | --- | ------- | ---------- | ----- | ----------- | ---- | ------ |
[Forum] Writing
[Forum] Recreation
leaseLoTTEpubliclywewillincludeURLstothe
[Forum] Science
[Forum] Technology originalpostsforproperattributionasrequiredby
[Forum] Lifestyle
| [Forum] Pooled |     |     |     |     |     |     | thelicense. | TheGooAQdatasetislicensedunder |         |     |           |         |
| -------------- | --- | --- | --- | --- | --- | --- | ----------- | ------------------------------ | ------- | --- | --------- | ------- |
|                |     |     | 5   | 10  | 15  | 20  | an Apache   | license,                       | version | 2.0 | (Khashabi | et al., |
Answers per query
|     |     |     |     |     |     |     | 2021). WewillalsoreleaseLoTTEwithaCCBY- |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --------------------------------------- | --- | --- | --- | --- | --- |
Figure6: LoTTEanswersperquery SA4.0license. Thesearchqueriescanbeusedfor
non-commercialresearchpurposesonlyasperthe
GooAQlicense.
|     |         |      |      | RocketQAv2 |          | ColBERTv2 |     |     |     |     |     |     |
| --- | ------- | ---- | ---- | ---------- | -------- | --------- | --- | --- | --- | --- | --- | --- |
|     | ColBERT |      |      |            | SPLADEv2 |           |     |     |     |     |     |     |
|     |         | BM25 | ANCE |            |          |           |     |     |     |     |     |     |
Corpus
|     |     |     |     |     |     |     | E DatasetsinBEIR |     |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | --- | --- | --- | --- |
Table8liststheBEIRdatasetsweusedinourevalu-
LoTTESearchDevQueries(Success@5)
ation,includingtheirrespectivelicenseinformation
| Writing | 76.3 | 47.3 75.7 |     | 79.5 | 78.9 | 81.7 |     |     |     |     |     |     |
| ------- | ---- | --------- | --- | ---- | ---- | ---- | --- | --- | --- | --- | --- | --- |
aswellasthenumbersofdocumentsaswellasthe
| Recreation | 71.8 | 56.3 66.1 |     | 73.0 | 70.7 | 76.0 |                         |     |     |                      |     |     |
| ---------- | ---- | --------- | --- | ---- | ---- | ---- | ----------------------- | --- | --- | -------------------- | --- | --- |
|            |      |           |     |      |      |      | numberoftestsetqueries. |     |     | WerefertoThakuretal. |     |     |
| Science    | 71.7 | 52.2 66.9 |     | 67.7 | 73.4 | 74.2 |                         |     |     |                      |     |     |
Technology 52.8 35.8 55.7 54.3 56.3 59.3 (2021) for a more detailed description of each of
| Lifestyle | 73.1 | 54.4 69.8 |     | 72.4 | 71.2 | 75.8 |     |     |     |     |     |     |
| --------- | ---- | --------- | --- | ---- | ---- | ---- | --- | --- | --- | --- | --- | --- |
thedatasets.
| Pooled | 65.4 | 45.6 63.7 |     | 66.4 | 67.0 | 69.3 |     |     |     |     |     |     |
| ------ | ---- | --------- | --- | ---- | ---- | ---- | --- | --- | --- | --- | --- | --- |
OurTouchéevaluationusesanupdatedversion
LoTTEForumDevQueries(Success@5)
ofthedatainBEIR,whichweuseforevaluatingthe
| Writing | 75.5 | 66.2 74.4 |     | 75.5 | 78.1 | 80.8 |     |     |     |     |     |     |
| ------- | ---- | --------- | --- | ---- | ---- | ---- | --- | --- | --- | --- | --- | --- |
modelswerun(i.e.,ColBERTv2andRocketQAv2)
| Recreation | 69.1 | 56.6 65.9 |     | 69.0 | 68.9 | 71.8 |                   |     |     |     |     |     |
| ---------- | ---- | --------- | --- | ---- | ---- | ---- | ----------------- | --- | --- | --- | --- | --- |
| Science    | 58.2 | 51.3 56.3 |     | 56.7 | 59.9 | 62.6 | aswellasSPLADEv2. |     |     |     |     |     |
| Technology | 39.6 | 30.7 38.8 |     | 39.9 | 42.1 | 45.0 |                   |     |     |     |     |     |
Lifestyle 61.1 48.2 61.8 62.0 61.8 65.8 Dataset License #Passages #TestQueries
Pooled 59.1 47.8 57.4 58.9 60.6 63.7 ArguAna(Wachsmuthetal.,2018) CCBY4.0 8674 1406
|     |     |     |     |     |     |     | Climate-Fever(Diggelmannetal.,2020) |     |     | Notreported | 5416593 | 1535 |
| --- | --- | --- | --- | --- | --- | --- | ----------------------------------- | --- | --- | ----------- | ------- | ---- |
Table7: Zero-shotevaluationresultsonthedevsetsof DBPedia(Aueretal.,2007) CCBY-SA3.0 4635922 400
| theLoTTEbenchmark. |        |         |      |      |           |     | FEVER(Thorneetal.,2018)    |     |                  | CCBY-SA3.0  |         |      |
| ------------------ | ------ | ------- | ---- | ---- | --------- | --- | -------------------------- | --- | ---------------- | ----------- | ------- | ---- |
|                    |        |         |      |      |           |     | FiQA-2018(Maiaetal.,2018)  |     |                  | Notreported | 57638   | 648  |
|                    |        |         |      |      |           |     | HotpotQA(Yangetal.,2018b)  |     |                  | CCBY-SA4.0  | 5233329 | 7405 |
|                    |        |         |      |      |           |     | NFCorpus(Botevaetal.,2016) |     |                  | Notreported | 3633    | 323  |
|                    |        |         |      |      |           |     | NQ(Kwiatkowskietal.,2019)  |     |                  | CCBY-SA3.0  | 2681468 | 3452 |
| highest            | ranked | queries | from | each | community | as  |                            |     |                  |             |         |      |
|                    |        |         |      |      |           |     | SCIDOCS(Cohanetal.,2020)   |     | GNUGeneralPublic |             | 25657   | 1000 |
Licensev3.0
determinedby1)thequeryscoresand2)thequery SciFact(Waddenetal.,2020) CCBY-NC2.0 5183 300
|     |     |     |     |     |     |     | Quora |     |     | Notreported | 522931 | 10000 |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | --- | ----------- | ------ | ----- |
view counts. We only use queries which have an Touché-2020(Bondarenkoetal.,2020) CCBY4.0 382545 49
acceptedanswer. Weensurethateachcommunity TREC-COVID(Voorheesetal.,2021) DatasetLicense 171332 50
Agreement
contributesatleast50queriestothetruncatedset
|          |           |     |         |         |      |        |     | Table8: BEIRdatasetinformation. |     |     |     |     |
| -------- | --------- | --- | ------- | ------- | ---- | ------ | --- | ------------------------------- | --- | --- | --- | --- |
| whenever | possible. | We  | set the | overall | size | of the |     |                                 |     |     |     |     |
truncatedsettobe2000queries,thoughnotethat
WealsotestedontheOpen-QAbenchmarksNQ,
thetotalcanexceedthisduetoroundingand/orthe
TQ,andSQuAD,eachofwhichhasapproximately
| minimumper-communityquerycount. |     |     |     |     | Weremove |     |     |     |     |     |     |     |
| ------------------------------- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
9kdev-setquestionsandmuli-hopHoVer,whose
allquotationmarksandHTMLtags.
|     |     |     |     |     |     |     | developmentsethas4kclaims. |     |     | Inthecompression |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------------------- | --- | --- | ---------------- | --- | --- |
evaluation§B,weusedmodelstrainedin-domain
| Statistics | Figure | 4 plots | the | number | of  | words |     |     |     |     |     |     |
| ---------- | ------ | ------- | --- | ------ | --- | ----- | --- | --- | --- | --- | --- | --- |
onNQandHoVer,whosetrainingsetscontain79k
| perpassageineachLoTTEdevcorpus. |     |     |     |     | Figures5 |     |     |     |     |     |     |     |
| ------------------------------- | --- | --- | --- | --- | -------- | --- | --- | --- | --- | --- | --- | --- |
and 6 plot the number of words and number of and18kqueries,respectively.
| corresponding | answer |     | passages | respectively |     | per |                                  |     |     |     |     |     |
| ------------- | ------ | --- | -------- | ------------ | --- | --- | -------------------------------- | --- | --- | --- | --- | --- |
|               |        |     |          |              |     |     | F Implementation&Hyperparameters |     |     |     |     |     |
query,splitacrosssearchandforumqueries.
|     |     |     |     |     |     |     | We implement | ColBERTv2 |     | using | Python | 3.7, |
| --- | --- | --- | --- | --- | --- | --- | ------------ | --------- | --- | ----- | ------ | ---- |
DevResults Table7presentsout-of-domaineval- PyTorch 1.9, and HuggingFace Transformers
uationresultsontheLoTTEdevqueries. Continu- 4.10(Wolfetal.,2020),extendingtheoriginalim-
ingthetrendweobservedin5,ColBERTv2consis- plementationofColBERTbyKhattabandZaharia
tentlyoutperformsallothermodelswetested. (2020). WeuseFAISS1.7(Johnsonetal.,2019)for

k-meansclustering,9
thoughunlikeColBERTwe finetunedcheckpointusing32-waytrainingexam-
donotuseitfornearest-neighborsearch. Instead, ples and 150k steps. To generate the top-k pas-
weimplementourcandidategenerationmechanism sagespertrainingquery,weapplytworounds,fol-
(§3.5)usingPyTorchprimitivesinPython. lowing Khattab et al. (2021b). We start from a
|              |     |     |             |     |             | model trained | with hard triples | (akin to Khattab |
| ------------ | --- | --- | ----------- | --- | ----------- | ------------- | ----------------- | ---------------- |
| We conducted |     | our | experiments | on  | an internal |               |                   |                  |
cluster, typically using up to four 12GB Titan V etal.(2021b)),trainwithdistillation,andthenuse
GPUsforeachoftheinferencetasks(e.g.,index- thedistilledmodeltoretrieveforthesecondround
ing, computing distillation scores, and retrieval) oftraining. Preliminaryexperimentsindicatethat
and four 80GB A100 GPUs for training, though qualityhaslowsensitivitytothisinitializationand
GPUswithsmallerRAMcanbeusedviagradient two-round training, suggesting that both of them
accumulation. Usingthisinfrastructure,computing couldbeavoidedtoreducethecostoftraining.
Unlessotherwisestated,theresultsshownrep-
thedistillationscorestakesunderaday,traininga
64-waymodelonMSMARCOfor400,000steps resent a single run. The latency results in §3 are
takesaroundfivedays,andindexingtakesapprox- averagesofthreeruns. ToevaluateforOpen-QAre-
imately two hours. We very roughly estimate an trieval,weuseevaluationscriptsfromKhattabetal.
upperboundtotalof20GPU-monthsforallexperi- (2021b), which checks if the short answer string
mentation,development,andevaluationperformed appears in the (titled) Wikipedia passage. This
forthisworkoveraperiodofseveralmonths. adaptstheDPR(Karpukhinetal.,2020)evaluation
|      |          |     |     |         |      | code.10 | We use the preprocessed | Wikipedia Dec |
| ---- | -------- | --- | --- | ------- | ---- | ------- | ----------------------- | ------------- |
| Like | ColBERT, |     | our | encoder | is a |         |                         |               |
bert-base-uncased model that is shared 2018dumpreleasedbyKarpukhinetal.(2020).
betweenthequeryandpassageencodersandwhich Forout-of-domainevaluation,weelectedtofol-
has110Mparameters. Weretainthedefaultvector low Thakur et al. (2021) and set the maximum
documentlengthofColBERT,RocketQAv2, and
| dimension | suggested |     | by Khattab | and | Zaharia |     |     |     |
| --------- | --------- | --- | ---------- | --- | ------- | --- | --- | --- |
(2020) and used in subsequent work, namely, ColBERTv2 to 300 tokens on BEIR and LoTTE.
d=128. Fortheexperimentsreportedinthispaper, Formaletal.(2021a)selectedmaximumsequence
length256forSPLADEv2bothonMSMARCO
| we train | on MS | MARCO |     | training set. | We use |     |     |     |
| -------- | ----- | ----- | --- | ------------- | ------ | --- | --- | --- |
simpledefaultswithlimitedmanualexplorationon andonBEIRforbothqueriesanddocuments,and
the official development set for the learning rate weretainedthisdefaultwhentestingtheirsystem
(10−5),
batch size (32 examples), and warm up on LoTTE. Unless otherwise stated, we keep the
defaultquerymaximumsequencelengthforCol-
(for20,000steps)withlineardecay.
Hyperparameterscorrespondingtoretrievalare BERTv2andRocketQAv2,whichis32tokens. For
explored in §C. We default to probe = 2, but theArguAnatestinBEIR,asthequeriesarethem-
selveslongdocuments,wesetthemaximumquery
| use probe | =   | 4 on | the largest | datasets, | namely, |     |     |     |
| --------- | --- | ---- | ----------- | --------- | ------- | --- | --- | --- |
MS MARCO and Wikipedia. By default we set length used by ColBERTv2 and RocketQAv2 to
candidates = probe ∗ 212, but for Wikipedia 300. ForClimate-FEVER,asthequeriesarerela-
tivelylongsentenceclaims,wesetthemaximum
| we set               | candidates |     | = probe | ∗ 213      | and for MS |                                 |     |     |
| -------------------- | ---------- | --- | ------- | ---------- | ---------- | ------------------------------- | --- | --- |
|                      |            |     |         | probe∗214. |            | querylengthusedbyColBERTv2to64. |     |     |
| MARCOwesetcandidates |            |     |         | =          | We         |                                 |     |     |
leaveextensivetuningofhyperparameterstofuture WeusetheopensourceBEIRimplementation11
andSPLADEv2evaluation12
| work. |     |     |     |     |     |     |     | codeasthebasisfor |
| ----- | --- | --- | --- | --- | --- | --- | --- | ----------------- |
ourevaluationsofSPLADEv2andANCEaswell
WetrainonMSMARCOusing64-waytuples
asforBM25onLoTTE.WeusetheAnserini(Yang
| for distillation, |     | sampling | them | from | the top-500 |     |     |     |
| ----------------- | --- | -------- | ---- | ---- | ----------- | --- | --- | --- |
retrieved passages per query. The training set of et al., 2018a) toolkit for BM25 on the Wikipedia
Open-QAretrievaltestsasinKhattabetal.(2021b).
MSMARCOcontainsapproximately800kqueries,
WeusetheimplementationdevelopedbytheRock-
| thoughonlyabout500khaveassociatedlabels. |     |     |     |     | We  |     |     |     |
| ---------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- |
apply distillation using all 800k queries, where etQAv2authorsforevaluatingRocketQAv2.13
eachtrainingexamplecontainsexactlyone“posi-
tive”,definedasapassagelabeledaspositiveorthe
| top-ranked | passage |     | by the cross-encoder |     | teacher, |     |     |     |
| ---------- | ------- | --- | -------------------- | --- | -------- | --- | --- | --- |
10https://github.com/facebookresearch/DPR/blob/
irrespectiveofitslabel.
main/dpr/data/qa_validation.py
Wetrainfor400ksteps,initializingfromapre- 11https://github.com/UKPLab/beir
12https://github.com/naver/splade
9https://github.com/facebookresearch/faiss 13https://github.com/PaddlePaddle/RocketQA

| Topic   | Communities                     | #Passages | #Searchqueries | #Forumqueries |
| ------- | ------------------------------- | --------- | -------------- | ------------- |
|         | ell.stackexchange.com           | 108143    | 433            | 1196          |
|         | literature.stackexchange.com    | 4778      | 7              | 58            |
| Writing | writing.stackexchange.com       | 29330     | 23             | 163           |
|         | linguistics.stackexchange.com   | 12302     | 22             | 116           |
|         | worldbuilding.stackexchange.com | 122519    | 12             | 470           |
|         | rpg.stackexchange.com           | 89066     | 91             | 621           |
|         | boardgames.stackexchange.com    | 20340     | 67             | 179           |
Recreation
|     | scifi.stackexchange.com     | 102561 | 343 | 852 |
| --- | --------------------------- | ------ | --- | --- |
|     | photo.stackexchange.com     | 51058  | 62  | 350 |
|     | chemistry.stackexchange.com | 39435  | 245 | 267 |
|     | stats.stackexchange.com     | 144084 | 137 | 949 |
|     | academia.stackexchange.com  | 76450  | 66  | 302 |
|     | astronomy.stackexchange.com | 14580  | 15  | 88  |
Science
|            | earthscience.stackexchange.com | 6734   | 10  | 50  |
| ---------- | ------------------------------ | ------ | --- | --- |
|            | engineering.stackexchange.com  | 12064  | 16  | 77  |
|            | datascience.stackexchange.com  | 23234  | 15  | 156 |
|            | philosophy.stackexchange.com   | 27061  | 34  | 124 |
|            | superuser.com                  | 418266 | 441 | 648 |
|            | electronics.stackexchange.com  | 205891 | 118 | 314 |
| Technology | askubuntu.com                  | 296291 | 132 | 480 |
|            | serverfault.com                | 323943 | 148 | 506 |
|            | webapps.stackexchange.com      | 31831  | 77  | 55  |
|            | pets.stackexchange.com         | 10070  | 20  | 87  |
|            | lifehacks.stackexchange.com    | 7893   | 2   | 50  |
|            | gardening.stackexchange.com    | 20601  | 16  | 182 |
|            | parenting.stackexchange.com    | 18357  | 10  | 87  |
|            | crafts.stackexchange.com       | 3094   | 4   | 50  |
| Lifestyle  | outdoors.stackexchange.com     | 13324  | 16  | 76  |
|            | coffee.stackexchange.com       | 2249   | 11  | 50  |
|            | music.stackexchange.com        | 47399  | 65  | 287 |
|            | diy.stackexchange.com          | 82659  | 135 | 732 |
|            | bicycles.stackexchange.com     | 35567  | 40  | 229 |
|            | mechanics.stackexchange.com    | 27680  | 98  | 246 |
Table9: Per-communitydistributionofLoTTEdevdatasetpassagesandquestions.
