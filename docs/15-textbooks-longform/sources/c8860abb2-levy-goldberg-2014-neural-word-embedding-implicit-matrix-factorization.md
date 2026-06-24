|                             |          | Neural   | Word   | Embedding                   |                    |     |     |
| --------------------------- | -------- | -------- | ------ | --------------------------- | ------------------ | --- | --- |
|                             | as       | Implicit | Matrix |                             | Factorization      |     |     |
|                             | OmerLevy |          |        |                             | YoavGoldberg       |     |     |
| DepartmentofComputerScience |          |          |        | DepartmentofComputerScience |                    |     |     |
| Bar-IlanUniversity          |          |          |        |                             | Bar-IlanUniversity |     |     |
| omerlevy@gmail.com          |          |          |        | yoav.goldberg@gmail.com     |                    |     |     |
Abstract
| We analyze | skip-gram  |            | with negative-sampling |               | (SGNS),    | a word     | embedding   |
| ---------- | ---------- | ---------- | ---------------------- | ------------- | ---------- | ---------- | ----------- |
| method     | introduced | by Mikolov | et                     | al., and show | that it is | implicitly | factorizing |
aword-contextmatrix,whosecellsarethepointwisemutualinformation(PMI)of
| therespectivewordandcontextpairs, |     |     |     | shiftedbyaglobalconstant. |     |     | Wefindthat |
| --------------------------------- | --- | --- | --- | ------------------------- | --- | --- | ---------- |
anotherembeddingmethod,NCE,isimplicitlyfactorizingasimilarmatrix,where
| each cell | is the | (shifted) | log conditional | probability | of a word | given | its context. |
| --------- | ------ | --------- | --------------- | ----------- | --------- | ----- | ------------ |
WeshowthatusingasparseShiftedPositivePMIword-contextmatrixtorepresent
wordsimprovesresultsontwowordsimilaritytasksandoneoftwoanalogytasks.
Whendenselow-dimensionalvectorsarepreferred,exactfactorizationwithSVD
canachievesolutionsthatareatleastasgoodasSGNS’ssolutionsforwordsimi-
laritytasks.OnanalogyquestionsSGNSremainssuperiortoSVD.Weconjecture
thatthisstemsfromtheweightednatureofSGNS’sfactorization.
1 Introduction
Most tasks in natural language processing and understanding involve looking at words, and could
benefitfromwordrepresentationsthatdonottreatindividualwordsasuniquesymbols,butinstead
reflectsimilaritiesanddissimilaritiesbetweenthem.Thecommonparadigmforderivingsuchrepre-
sentationsisbasedonthedistributionalhypothesisofHarris[15],whichstatesthatwordsinsimilar
contexts have similar meanings. This has given rise to many word representation methods in the
NLPliterature,thevastmajorityofwhomcanbedescribedintermsofaword-contextmatrixM in
whicheachrowicorrespondstoaword,eachcolumnjtoacontextinwhichthewordappeared,and
eachmatrixentryM correspondstosomeassociationmeasurebetweenthewordandthecontext.
ij
WordsarethenrepresentedasrowsinM orinadimensionality-reducedmatrixbasedonM.
Recently,therehasbeenasurgeofworkproposingtorepresentwordsasdensevectors,derivedusing
various training methods inspired from neural-network language modeling [3, 9, 23, 21]. These
representations, referred to as “neural embeddings” or “word embeddings”, have been shown to
performwellinavarietyofNLPtasks[26,10,1].Inparticular,asequenceofpapersbyMikolovand
colleagues [20, 21] culminated in the skip-gram with negative-sampling (SGNS) training method
whichisbothefficienttotrainandprovidesstate-of-the-artresultsonvariouslinguistictasks. The
training method (as implemented in the word2vec software package) is highly popular, but not
well understood. While it is clear that the training objective follows the distributional hypothesis
–bytryingtomaximizethedot-productbetweenthevectorsoffrequentlyoccurringword-context
pairs,andminimizeitforrandomword-contextpairs–verylittleisknownaboutthequantitybeing
optimizedbythealgorithm,orthereasonitisexpectedtoproducegoodwordrepresentations.
Inthiswork,weaimtobroadenthetheoreticalunderstandingofneural-inspiredwordembeddings.
Specifically, we cast SGNS’s training method as weighted matrix factorization, and show that its
objectiveisimplicitlyfactorizingashiftedPMImatrix–thewell-knownword-contextPMImatrix
fromtheword-similarityliterature, shiftedbyaconstantoffset. Asimilarresultholdsalsoforthe
1

NCEembeddingmethodofMnihandKavukcuoglu[24]. Whileitisimpracticaltodirectlyusethe
veryhigh-dimensionalanddenseshiftedPMImatrix,weproposetoapproximateitwiththepositive
shiftedPMImatrix(ShiftedPPMI),whichissparse.ShiftedPPMIisfarbetteratoptimizingSGNS’s
objective,andperformsslightlybetterthanword2vecderivedvectorsonseverallinguistictasks.
Finally, we suggest a simple spectral algorithm that is based on performing SVD over the Shifted
PPMImatrix. ThespectralalgorithmoutperformsbothSGNSandtheShiftedPPMImatrixonthe
word similarity tasks, and is scalable to large corpora. However, it lags behind the SGNS-derived
representation on word-analogy tasks. We conjecture that this behavior is related to the fact that
SGNSperformsweighted matrixfactorization,givingmoreinfluencetofrequentpairs,asopposed
to SVD, which gives the same weight to all matrix cells. While the weighted and non-weighted
objectivessharethesameoptimalsolution(perfectreconstructionoftheshiftedPMImatrix),they
resultindifferentgeneralizationswhencombinedwithdimensionalityconstraints.
2 Background: Skip-GramwithNegativeSampling(SGNS)
Our departure point is SGNS – the skip-gram neural embedding model introduced in [20] trained
usingthenegative-samplingprocedurepresentedin[21]. Inwhatfollows,wesummarizetheSGNS
modelandintroduceournotation. AdetailedderivationoftheSGNSmodelisavailablein[14].
Setting and Notation The skip-gram model assumes a corpus of words w ∈ V and their
W
contexts c ∈ V , where V and V are the word and context vocabularies. In [20, 21]
C W C
the words come from an unannotated textual corpus of words w ,w ,...,w (typically n is in
1 2 n
the billions) and the contexts for word w are the words surrounding it in an L-sized window
i
w ,...,w ,w ,...,w . Other definitions of contexts are possible [18]. We denote the
i−L i−1 i+1 i+L
collectionofobservedwordsandcontextpairsasD. Weuse#(w,c)todenotethenumberoftimes
thepair(w,c)appearsinD. Similarly,#(w) = (cid:80) #(w,c(cid:48))and#(c) = (cid:80) #(w(cid:48),c)
arethenumberoftimeswandcoccurredinD,resp c e (cid:48) c ∈ t V iv C ely. w(cid:48)∈VW
Each word w ∈ V is associated with a vector w(cid:126) ∈ Rd and similarly each context c ∈ V is
W C
represented as a vector (cid:126)c ∈ Rd, where d is the embedding’s dimensionality. The entries in the
vectorsarelatent,andtreatedasparameterstobelearned. Wesometimesrefertothevectorsw(cid:126) as
rowsina|V |×dmatrixW,andtothevectors(cid:126)casrowsina|V |×dmatrixC. Insuchcases,W
W C i
(C ) refers to the vector representation of the ith word (context) in the corresponding vocabulary.
i
When referring to embeddings produced by a specific method x, we will usually use Wx and Cx
explicitly,butmayusejustW andC whenthemethodisclearfromthediscussion.
SGNS’sObjective Consideraword-contextpair(w,c).Didthispaircomefromtheobserveddata
D? Let P(D = 1|w,c) be the probability that (w,c) came from the data, and P(D = 0|w,c) =
1−P(D =1|w,c)theprobabilitythat(w,c)didnot. Thedistributionismodeledas:
1
P(D =1|w,c)=σ(w(cid:126) ·(cid:126)c)=
1+e−w(cid:126)·(cid:126)c
wherew(cid:126) and(cid:126)c(eachad-dimensionalvector)arethemodelparameterstobelearned.
ThenegativesamplingobjectivetriestomaximizeP(D = 1|w,c)forobserved(w,c)pairswhile
maximizingP(D = 0|w,c)forrandomlysampled“negative”examples(hencethename“negative
sampling”), under the assumption that randomly selecting a context for a given word is likely to
resultinanunobserved(w,c)pair. SGNS’sobjectiveforasingle(w,c)observationisthen:
logσ(w(cid:126) ·(cid:126)c)+k·E [logσ(−w(cid:126) ·(cid:126)c )] (1)
cN∼PD N
wherekisthenumberof“negative”samplesandc isthesampledcontext,drawnaccordingtothe
N
empiricalunigramdistributionP (c)= #(c). 1
D |D|
1In the algorithm described in [21], the negative contexts are sampled according to p3/4(c) = #c3/4
Z
insteadoftheunigramdistribution #c.Samplingaccordingtop3/4indeedproducessomewhatsuperiorresults
Z
onsomeofthesemanticevaluationtasks. Itisstraight-forwardtomodifythePMImetricinasimilarfashion
byreplacingthep(c)termwithp3/4(c),anddoingsoshowssimilartrendsinthematrix-basedmethodsasit
doesinword2vec’sstochasticgradientbasedtrainingmethod. Wedonotexplorethisfurtherinthispaper,
andreportresultsusingtheunigramdistribution.
2

The objective is trained in an online fashion using stochastic gradient updates over the observed
pairsinthecorpusD. Theglobalobjectivethensumsovertheobserved(w,c)pairsinthecorpus:
(cid:88) (cid:88)
·(cid:126)c)+k·E
(cid:96)= #(w,c)(logσ(w(cid:126) cN∼PD [logσ(−w(cid:126) ·(cid:126)c N )]) (2)
w∈VW c∈VC
Optimizingthisobjectivemakesobservedword-contextpairshavesimilarembeddings,whilescat-
teringunobservedpairs. Intuitively, wordsthatappearinsimilarcontextsshouldhavesimilarem-
beddings, though we are not familiar with a formal proof that SGNS does indeed maximize the
dot-productofsimilarwords.
3 SGNSasImplicitMatrixFactorization
Rd,
SGNS embeds both words and their contexts into a low-dimensional space resulting in the
wordandcontextmatricesW andC. TherowsofmatrixW aretypicallyusedinNLPtasks(such
as computing word similarities) while C is ignored. It is nonetheless instructive to consider the
productW ·C(cid:62) = M. Viewedthisway,SGNScanbedescribedasfactorizinganimplicitmatrix
| M ofdimensions|V |×|V |intotwosmallermatrices. |     |     |     |     |     |     |
| ---------------------------------------------- | --- | --- | --- | --- | --- | --- |
W C
Which matrix is being factorized? A matrix entry M corresponds to the dot product W ·C =
|     |     | ij  |     |     | i   | j   |
| --- | --- | --- | --- | --- | --- | --- |
w(cid:126) ·(cid:126)c . Thus, SGNS is factorizing a matrix in which each row corresponds to a word w ∈ V ,
i j W
eachcolumncorrespondstoacontextc ∈ V ,andeachcellcontainsaquantityf(w,c)reflecting
C
thestrengthofassociationbetweenthatparticularword-contextpair. Suchword-contextassociation
matricesareverycommonintheNLPandword-similarityliterature,seee.g. [29,2]. Thatsaid,the
objectiveofSGNS(equation2)doesnotexplicitlystatewhatthisassociationmetricis. Whatcan
wesayabouttheassociationfunctionf(w,c)? Inotherwords,whichmatrixisSGNSfactorizing?
3.1 CharacterizingtheImplicitMatrix
Considertheglobalobjective(equation2)above. Forsufficientlylargedimensionalityd(i.e. allow-
ingforaperfectreconstructionofM),eachproductw(cid:126) ·(cid:126)ccanassumeavalueindependentlyofthe
others. Undertheseconditions,wecantreattheobjective(cid:96)asafunctionofindependentw(cid:126)·(cid:126)cterms,
andfindthevaluesofthesetermsthatmaximizeit.
Webeginbyrewritingequation2:
| (cid:88) (cid:88) |     | (cid:88) (cid:88) |     |     |     |     |
| ----------------- | --- | ----------------- | --- | --- | --- | --- |
(cid:96)= #(w,c)(logσ(w(cid:126) ·(cid:126)c))+ #(w,c)(k·E [logσ(−w(cid:126) ·(cid:126)c )])
|                   |     |           |     |     | cN∼PD | N   |
| ----------------- | --- | --------- | --- | --- | ----- | --- |
| w∈VW c∈VC         |     | w∈VW c∈VC |     |     |       |     |
| (cid:88) (cid:88) |     | (cid:88)  |     |     |       |     |
= #(w,c)(logσ(w(cid:126) ·(cid:126)c))+ #(w)(k·E [logσ(−w(cid:126) ·(cid:126)c )]) (3)
|           |     |      |     | cN∼PD | N   |     |
| --------- | --- | ---- | --- | ----- | --- | --- |
| w∈VW c∈VC |     | w∈VW |     |       |     |     |
andexplicitlyexpressingtheexpectationterm:
|                         |             | (cid:88) | #(c ) |                  |                 |     |
| ----------------------- | ----------- | -------- | ----- | ---------------- | --------------- | --- |
| E                       |             |          | N     |                  |                 |     |
| cN∼PD [logσ(−w(cid:126) | ·(cid:126)c | N )]=    |       | logσ(−w(cid:126) | ·(cid:126)c N ) |     |
|D|
cN∈VC
| #(c)               |               | (cid:88) | #(c ) |                  |               |     |
| ------------------ | ------------- | -------- | ----- | ---------------- | ------------- | --- |
| = logσ(−w(cid:126) | ·(cid:126)c)+ |          | N     | logσ(−w(cid:126) | ·(cid:126)c ) | (4) |
N
| |D| |     |     | |D| |     |     |     |
| --- | --- | --- | --- | --- | --- | --- |
cN∈VC\{c}
Combiningequations3and4revealsthelocalobjectiveforaspecific(w,c)pair:
#(c)
| (cid:96)(w,c)=#(w,c)logσ(w(cid:126) |     | ·(cid:126)c)+k·#(w)· |     | logσ(−w(cid:126) | ·(cid:126)c) | (5) |
| ----------------------------------- | --- | -------------------- | --- | ---------------- | ------------ | --- |
|D|
Tooptimizetheobjective,wedefinex=w(cid:126) ·(cid:126)candfinditspartialderivativewithrespecttox:
| ∂(cid:96)             |     |     | #(c) |       |     |     |
| --------------------- | --- | --- | ---- | ----- | --- | --- |
| =#(w,c)·σ(−x)−k·#(w)· |     |     |      | ·σ(x) |     |     |
| ∂x                    |     |     |      | |D|   |     |     |
Wecomparethederivativetozero,andaftersomesimplification,arriveat:
|        |      |       |         |      |     |     |
| ------- | ---- | ------ | ------- | ---- | --- | --- |
| #(w,c)  |      |        | #(w,c)  |      |     |     |
| e2x−   |      | −1ex− |         |      | =0  |     |
| k·#(w)· | #(c) |        | k·#(w)· | #(c) |     |     |
|         |      | |D|    |         |      | |D| |     |
3

If we define y = ex, this equation becomes a quadratic equation of y, which has two solutions,
y =−1(whichisinvalidgiventhedefinitionofy)and:
|     |     |     | #(w,c) |      | #(w,c)·|D| |         | 1   |     |     |
| --- | --- | --- | ------ | ---- | ---------- | ------- | --- | --- | --- |
|     |     | y = |        |      | =          |         | ·   |     |     |
|     |     |     |        | #(c) |            | #w·#(c) | k   |     |     |
k·#(w)·
|D|
Substitutingywithexandxwithw(cid:126) ·(cid:126)creveals:
|            |                 | (cid:18)   |          |          | (cid:19) | (cid:18)   |     | (cid:19) |     |
| ---------- | --------------- | ---------- | -------- | -------- | -------- | ---------- | --- | -------- | --- |
|            |                 | #(w,c)·|D| |          | 1        |          | #(w,c)·|D| |     |          |     |
| w(cid:126) | ·(cid:126)c=log |            |          | ·        | =log     |            |     | −logk    | (6) |
|            |                 | #(w)·#(c)  |          | k        |          | #(w)·#(c)  |     |          |     |
|            |                 |            | (cid:16) | (cid:17) |          |            |     |          |     |
Interestingly, the expression log #(w,c)·|D| is the well-known pointwise mutual information
#(w)·#(c)
(PMI)of(w,c),whichwediscussindepthbelow.
Finally,wecandescribethematrixM thatSGNSisfactorizing:
|     | MSGNS | =W  | ·C  | =w(cid:126) | ·(cid:126)c =PMI(w |     | ,c )−logk |     | (7) |
| --- | ----- | --- | --- | ----------- | ------------------ | --- | --------- | --- | --- |
|     |       | ij  | i   | j i         | j                  |     | i j       |     |     |
For a negative-sampling value of k = 1, the SGNS objective is factorizing a word-context matrix
in which the association between a word and its context is measured by f(w,c) = PMI(w,c).
WerefertothismatrixasthePMImatrix, MPMI. Fornegative-samplingvaluesk > 1, SGNSis
| factorizingashiftedPMImatrixMPMIk |     |     |     | =MPMI | −logk. |     |     |     |     |
| --------------------------------- | --- | --- | --- | ----- | ------ | --- | --- | --- | --- |
Other embedding methods can also be cast as factorizing implicit word-context matrices. Using a
similar derivation, it can be shown that noise-contrastive estimation (NCE) [24] is factorizing the
(shifted)log-conditional-probabilitymatrix:
|     |     |     | (cid:18) |     | (cid:19) |     |     |     |     |
| --- | --- | --- | -------- | --- | -------- | --- | --- | --- | --- |
#(w,c)
| MNCE | =w(cid:126) | ·(cid:126)c | =log |      | −logk | =logP(w|c)−logk |     |     | (8) |
| ---- | ----------- | ----------- | ---- | ---- | ----- | --------------- | --- | --- | --- |
|      | ij          | i j         |      | #(c) |       |                 |     |     |     |
3.2 WeightedMatrixFactorization
We obtained that SGNS’s objective is optimized by setting w(cid:126) ·(cid:126)c = PMI(w,c)−logk for every
(w,c) w(cid:126) and(cid:126)c
pair. However, this assumes that the dimensionality of is high enough to allow for
perfectreconstruction.Whenperfectreconstructionisnotpossible,somew(cid:126)·(cid:126)cproductsmustdeviate
from their optimal values. Looking at the pair-specific objective (equation 5) reveals that the loss
for a pair (w,c) depends on its number of observations (#(w,c)) and expected negative samples
(k·#(w)·#(c)/|D|). SGNS’sobjectivecannowbecastasaweightedmatrixfactorizationprob-
lem, seeking the optimal d-dimensional factorization of thematrix MPMI −logk under a metric
whichpaysmorefordeviationsonfrequent(w,c)pairsthandeviationsoninfrequentones.
3.3 PointwiseMutualInformation
Pointwise mutual information is an information-theoretic association measure between a pair of
discreteoutcomesxandy,definedas:
P(x,y)
|     |     |     | PMI(x,y)=log |     |     |     |     |     | (9) |
| --- | --- | --- | ------------ | --- | --- | --- | --- | --- | --- |
P(x)P(y)
Inourcase,PMI(w,c)measurestheassociationbetweenawordwandacontextcbycalculating
the log of the ratio between their joint probability (the frequency in which they occur together)
and their marginal probabilities (the frequency in which they occur independently). PMI can be
estimatedempiricallybyconsideringtheactualnumberofobservationsinacorpus:
#(w,c)·|D|
|     |     |     | PMI(w,c)=log |     |     |     |     |     | (10) |
| --- | --- | --- | ------------ | --- | --- | --- | --- | --- | ---- |
#(w)·#(c)
TheuseofPMIasameasureofassociationinNLPwasintroducedbyChurchandHanks[8]and
widelyadoptedforwordsimilaritytasks[11,27,29].
Working with the PMI matrix presents some computational challenges. The rows of MPMI con-
tain many entries of word-context pairs (w,c) that were never observed in the corpus, for which
4

PMI(w,c) = log0 = −∞. Not only is the matrix ill-defined, it is also dense, which is a major
practical issue because of its huge dimensions |V |×|V |. One could smooth the probabilities
W C
using,forinstance,aDirichletpriorbyaddingasmall“fake”counttotheunderlyingcountsmatrix,
renderingallword-contextpairsobserved. Whiletheresultingmatrixwillnotcontainanyinfinite
values,itwillremaindense.
An alternative approach, commonly used in NLP, is to replace the MPMI matrix with MPMI, in
0
which PMI(w,c) = 0 in cases #(w,c) = 0, resulting in a sparse matrix. We note that MPMI is
0
inconsistent,inthesensethatobservedbut“bad”(uncorrelated)word-contextpairshaveanegative
matrixentry,whileunobserved(henceworse)oneshave0intheircorrespondingcell. Considerfor
example a pair of relatively frequent words (high P(w) and P(c)) that occur only once together.
There is strong evidence that the words tend not to appear together, resulting in a negative PMI
value,andhenceanegativematrixentry. Ontheotherhand,apairoffrequentwords(sameP(w)
andP(c))thatisneverobservedoccurringtogetherinthecorpus,willreceiveavalueof0.
AsparseandconsistentalternativefromtheNLPliteratureistousethepositivePMI(PPMI)metric,
inwhichallnegativevaluesarereplacedby0:
PPMI(w,c)=max(PMI(w,c),0) (11)
When representing words, there is some intuition behind ignoring negative values: humans can
easily think of positive associations (e.g. “Canada” and “snow”) but find it much harder to invent
negative ones (“Canada” and “desert”). This suggests that the perceived similarity of two words
is more influenced by the positive context they share than by the negative context they share. It
therefore makes some intuitive sense to discard the negatively associated contexts and mark them
as“uninformative”(0)instead.2 Indeed,itwasshownthatthePPMImetricperformsverywellon
semanticsimilaritytasks[5].
BothMPMIandMPPMIarewellknowntotheNLPcommunity.Inparticular,systematiccomparisons
0
of various word-context association metrics show that PMI, and more so PPMI, provide the best
results for a wide range of word-similarity tasks [5, 16]. It is thus interesting that the PMI matrix
emergesastheoptimalsolutionforSGNS’sobjective.
4 AlternativeWordRepresentations
AsSGNSwithk =1isattemptingtoimplicitlyfactorizethefamiliarmatrixMPMI,anaturalalgo-
rithmwouldbetousetherowsofMPPMIdirectlywhencalculatingwordsimilarities. ThoughPPMI
isonlyanapproximationoftheoriginalPMImatrix,itstillbringstheobjectivefunctionveryclose
to its optimum (see Section 5.1). In this section, we propose two alternative word representations
thatbuilduponMPPMI.
4.1 ShiftedPPMI
WhilethePMImatrixemergesfromSGNSwithk = 1,itwasshownthatdifferentvaluesofkcan
substantiallyimprovetheresultingembedding. Withk >1,theassociationmetricintheimplicitly
factorizedmatrixisPMI(w,c)−log(k). ThissuggeststheuseofShiftedPPMI(SPPMI),anovel
association metric which, to the best of our knowledge, was not explored in the NLP and word-
similaritycommunities:
SPPMI (w,c)=max(PMI(w,c)−logk,0) (12)
k
AswithSGNS,certainvaluesofkcanimprovetheperformanceofMSPPMIk ondifferenttasks.
4.2 SpectralDimensionalityReduction: SVDoverShiftedPPMI
Whilesparsevectorrepresentationsworkwell,therearealsoadvantagestoworkingwithdenselow-
dimensionalvectors,suchasimprovedcomputationalefficiencyand,arguably,bettergeneralization.
2Anotableexceptionisthecaseofsyntacticsimilarity. Forexample,allverbsshareaverystrongnegative
associationwithbeingprecededbydeterminers,andpasttenseverbshaveaverystrongnegativeassociationto
beprecededby“be”verbsandmodals.
5

AnalternativematrixfactorizationmethodtoSGNS’sstochasticgradienttrainingistruncatedSin-
gularValueDecomposition(SVD)–abasicalgorithmfromlinearalgebrawhichisusedtoachieve
the optimal rank d factorization with respect to L loss [12]. SVD factorizes M into the product
2
of three matrices U ·Σ·V(cid:62), where U and V are orthonormal and Σ is a diagonal matrix of sin-
gularvalues. LetΣ bethediagonalmatrixformedfromthetopdsingularvalues,andletU and
d d
V be the matrices produced by selecting the corresponding columns from U and V. The matrix
d
M =U ·Σ ·V(cid:62)isthematrixofrankdthatbestapproximatestheoriginalmatrixM,inthesense
d d d d
thatitminimizestheapproximationerrors. Thatis,M =argmin (cid:107)M(cid:48)−M(cid:107) .
d Rank(M(cid:48))=d 2
WhenusingSVD,thedot-productsbetweentherowsofW =U ·Σ areequaltothedot-products
d d
betweenrowsofM . Inthecontextofword-contextmatrices,thedense,ddimensionalrowsofW
d
areperfectsubstitutesfortheveryhigh-dimensionalrowsofM . Indeedanothercommonapproach
d
in the NLP literature is factorizing the PPMI matrix MPPMI with SVD, and then taking the rows
ofWSVD = U ·Σ andCSVD = V aswordandcontextrepresentations, respectively. However,
d d d
usingtherowsofWSVDaswordrepresentationsconsistentlyunder-performtheWSGNSembeddings
derivedfromSGNSwhenevaluatedonsemantictasks.
Symmetric SVD We note that in the SVD-based factorization, the resulting word and context
matriceshaveverydifferentproperties. Inparticular,thecontextmatrixCSVD isorthonormalwhile
the word matrix WSVD is not. On the other hand, the factorization achieved by SGNS’s training
procedureismuchmore“symmetric”,inthesensethatneitherWW2VnorCW2Visorthonormal,and
noparticularbiasisgiventoeitherofthematricesinthetrainingobjective. Wethereforepropose
achievingsimilarsymmetrywiththefollowingfactorization:
(cid:112) (cid:112)
WSVD1/2 =U
d
· Σ
d
CSVD1/2 =V
d
· Σ
d
(13)
Whileitisnottheoreticallyclearwhythesymmetricapproachisbetterforsemantictasks, itdoes
workmuchbetterempirically.3
SVDversusSGNS Thespectralalgorithmhastwocomputationaladvantagesoverstochasticgra-
dient training. First, it is exact, and does not require learning rates or hyper-parameter tuning.
Second,itcanbeeasilytrainedoncount-aggregateddata(i.e. {(w,c,#(w,c))}triplets),makingit
applicabletomuchlargercorporathanSGNS’strainingprocedure,whichrequireseachobservation
of(w,c)tobepresentedseparately.
On the other hand, the stochastic gradient method has advantages as well: in contrast to SVD, it
distinguishes between observed and unobserved events; SVD is known to suffer from unobserved
values[17],whichareverycommoninword-contextmatrices. Moreimportantly,SGNS’sobjective
weighsdifferent(w,c)pairsdifferently,preferringtoassigncorrectvaluestofrequent(w,c)pairs
while allowing more error for infrequent pairs (see Section 3.2). Unfortunately, exact weighted
SVD is a hard computational problem [25]. Finally, because SGNS cares only about observed
(and sampled) (w,c) pairs, it does not require the underlying matrix to be a sparse one, enabling
optimization of dense matrices, such as the exact PMI −logk matrix. The same is not feasible
whenusingSVD.
Aninterestingmiddle-groundbetweenSGNSandSVDistheuseofstochasticmatrixfactorization
(SMF) approaches, common in the collaborative filtering literature [17]. In contrast to SVD, the
SMF approaches are not exact, and do require hyper-parameter tuning. On the other hand, they
are better than SVD at handling unobserved values, and can integrate importance weighting for
examples,muchlikeSGNS’strainingprocedure.However,likeSVDandunlikeSGNS’sprocedure,
theSMFapproachesworkoveraggregated(w,c)statisticsallowing(w,c,f(w,c))tripletsasinput,
making the optimization objective more direct, and scalable to significantly larger corpora. SMF
approacheshaveadditionaladvantagesoverbothSGNSandSVD,suchasregularization, opening
the way to a range of possible improvements. We leave the exploration of SMF-based algorithms
forwordembeddingstofuturework.
3TheapproachcanbegeneralizedtoWSVDα =U ·(Σ )α,makingαatunableparameter.Thisobservation
d d
waspreviouslymadebyCaron[7]andinvestigatedin[6,28],showingthatdifferentvaluesofαindeedperform
betterthanothersforvarioustasks.Inparticular,settingα=0performswellformanytasks.Wedonotexplore
tuningtheαparameterinthiswork.
6

Method PMI−log k SPPMI SVD SGNS
d=100 d=500 d=1000 d=100 d=500 d=1000
k=1 0% 0.00009% 26.1% 25.2% 24.2% 31.4% 29.4% 7.40%
k=5 0% 0.00004% 95.8% 95.1% 94.9% 39.3% 36.0% 7.13%
k=15 0% 0.00002% 266% 266% 265% 7.80% 6.37% 5.97%
Table1:Percentageofdeviationfromtheoptimalobjectivevalue(lowervaluesarebetter).See5.1fordetails.
5 EmpiricalResults
Wecomparethematrix-basedalgorithmstoSGNSintwoaspects. First,wemeasurehowwelleach
algorithm optimizes the objective, and then proceed to evaluate the methods on various linguistic
tasks. Wefindthatforsometasksthereisalargediscrepancybetweenoptimizingtheobjectiveand
doingwellonthelinguistictask.
Experimental Setup All models were trained on English Wikipedia, pre-processed by removing
non-textual elements, sentence splitting, and tokenization. The corpus contains 77.5 million sen-
tences, spanning 1.5 billion tokens. All models were derived using a window of 2 tokens to each
side of the focus word, ignoring words that appeared less than 100 times in the corpus, resulting
invocabulariesof189,533termsforbothwordsandcontexts. TotraintheSGNSmodels,weused
a modified version of word2vec which receives a sequence of pre-extracted word-context pairs
[18].4 Weexperimentedwiththreevaluesofk(numberofnegativesamplesinSGNS,shiftparam-
√
eterinPMI-basedmethods): 1,5,15. ForSVD,wetakeW =U · Σ asexplainedinSection4.
d d
5.1 OptimizingtheObjective
Nowthatwehaveananalyticalsolutionfortheobjective,wecanmeasurehowwelleachalgorithm
optimizesthisobjectiveinpractice.Todoso,wecalculated(cid:96),thevalueoftheobjective(equation2)
giveneachword(andcontext)representation.5 Forsparsematrixrepresentations,wesubstitutedw(cid:126)·(cid:126)c
withthematchingcell’svalue(e.g. forSPPMI,wesetw(cid:126) ·(cid:126)c = max(PMI(w,c)−logk,0)). Each
algorithm’s (cid:96) value was compared to (cid:96) , the objective when setting w(cid:126) ·(cid:126)c = PMI(w,c)−logk,
Opt
which was shown to be optimal (Section 3.1). The percentage of deviation from the optimum is
definedby((cid:96)−(cid:96) )/((cid:96) )andpresentedintable1.
Opt Opt
WeobservethatSPPMIisindeedanear-perfectapproximationoftheoptimalsolution,eventhough
it discards a lot of information when considering only positive cells. We also note that for the
factorizationmethods,increasingthedimensionalityenablesbettersolutions,asexpected. SVDis
slightly better than SGNS at optimizing the objective for d ≤ 500 and k = 1. However, while
SGNS is able to leverage higher dimensions and reduce its error significantly, SVD fails to do so.
Furthermore,SVDbecomesveryerroneousaskincreases.Wehypothesizethatthisisaresultofthe
increasingnumberofzero-cells,whichmaycauseSVDtopreferafactorizationthatisverycloseto
thezeromatrix,sinceSVD’sL objectiveisunweighted,anddoesnotdistinguishbetweenobserved
2
andunobservedmatrixcells.
5.2 PerformanceofWordRepresentationsonLinguisticTasks
LinguisticTasksandDatasets Weevaluatedthewordrepresentationsonfourdataset, covering
wordsimilarityandrelationalanalogytasks. Weusedtwodatasetstoevaluatepairwisewordsimi-
larity: Finkelsteinetal.’sWordSim353[13]andBrunietal.’sMEN[4]. Thesedatasetscontainword
pairs together with human-assigned similarity scores. The word vectors are evaluated by ranking
the pairs according to their cosine similarities, and measuring the correlation (Spearman’s ρ) with
thehumanratings.
Thetwoanalogydatasetspresentquestionsoftheform“aistoa∗asbistob∗”,whereb∗ishidden,
andmustbeguessedfromtheentirevocabulary. TheSyntacticdataset[22]contains8000morpho-
4http://www.bitbucket.org/yoavgo/word2vecf
5Sinceitiscomputationallyexpensivetocalculatetheexactobjective,weapproximatedit.First,insteadof
enumeratingeveryobservedword-contextpairinthecorpus,wesampled10millionsuchpairs,accordingto
theirprevalence. Second,insteadofcalculatingtheexpectationtermexplicitly(asinequation4),wesampled
anegativeexample{(w,c )}foreachoneofthe10million“positive”examples,usingthecontexts’unigram
N
distribution,asdonebySGNS’soptimizationprocedure(explainedinSection2).
7

WS353(WORDSIM)[13] MEN(WORDSIM)[4] MIXEDANALOGIES[20] SYNT.ANALOGIES[22]
Representation Corr. Representation Corr. Representation Acc. Representation Acc.
SVD (k=5) 0.691 SVD (k=1) 0.735 SPPMI (k=1) 0.655 SGNS (k=15) 0.627
SPPMI (k=15) 0.687 SVD (k=5) 0.734 SPPMI (k=5) 0.644 SGNS (k=5) 0.619
SPPMI (k=5) 0.670 SPPMI (k=5) 0.721 SGNS (k=15) 0.619 SGNS (k=1) 0.59
SGNS (k=15) 0.666 SPPMI (k=15) 0.719 SGNS (k=5) 0.616 SPPMI (k=5) 0.466
SVD (k=15) 0.661 SGNS (k=15) 0.716 SPPMI (k=15) 0.571 SVD (k=1) 0.448
SVD (k=1) 0.652 SGNS (k=5) 0.708 SVD (k=1) 0.567 SPPMI (k=1) 0.445
SGNS (k=5) 0.644 SVD (k=15) 0.694 SGNS (k=1) 0.540 SPPMI (k=15) 0.353
SGNS (k=1) 0.633 SGNS (k=1) 0.690 SVD (k=5) 0.472 SVD (k=5) 0.337
SPPMI (k=1) 0.605 SPPMI (k=1) 0.688 SVD (k=15) 0.341 SVD (k=15) 0.208
Table2: Acomparisonofwordrepresentationsonvariouslinguistictasks. Thedifferentrepresentationswere
createdbythreealgorithms(SPPMI,SVD,SGNS)withd=1000anddifferentvaluesofk.
syntacticanalogyquestions,suchas“goodistobestassmartistosmartest”.TheMixeddataset[20]
contains19544questions,abouthalfofthesamekindasinSyntactic,andanotherhalfofamorese-
manticnature,suchascapitalcities(“ParisistoFranceasTokyoistoJapan”). Afterfilteringques-
tions involving out-of-vocabulary words, i.e. words that appeared in English Wikipedia less than
100times,weremainwith7118instancesinSyntacticand19258instancesinMixed. Theanalogy
questionsareansweredusingLevyandGoldberg’ssimilaritymultiplicationmethod[19],whichis
state-of-the-artinanalogyrecovery:argmax cos(b∗,a∗)·cos(b∗,b)/(cos(b∗,a)+ε).
b∗∈VW\{a∗,b,a}
Theevaluationmetricfortheanalogyquestionsisthepercentageofquestionsforwhichtheargmax
resultwasthecorrectanswer(b∗).
Results Table 2 shows the experiments’ results. On the word similarity task, SPPMI yields better
resultsthanSGNS,andSVDimprovesevenmore. However, thedifferencebetweenthetopPMI-
basedmethodandthetopSGNSconfigurationineachdatasetissmall, anditisreasonabletosay
thattheyperformon-par. Itisalsoevidentthatdifferentvaluesofk haveasignificanteffectonall
methods: SGNS generally works better with higher values of k, whereas SPPMI and SVD prefer
lowervaluesofk. Thismaybeduetothefactthatonlypositivevaluesareretained,andhighvalues
ofkmaycausetoomuchlossofinformation. AsimilarobservationwasmadeforSGNSandSVD
when observing how well they optimized the objective (Section 5.1). Nevertheless, tuning k can
significantlyincreasetheperformanceofSPPMIoverthetraditionalPPMIconfiguration(k =1).
The analogies task shows different behavior. First, SVD does not perform as well as SGNS and
SPPMI.Moreinterestingly, inthesyntacticanalogiesdataset, SGNSsignificantlyoutperformsthe
rest.Thistrendisevenmorepronouncedwhenusingtheadditiveanalogyrecoverymethod[22](not
shown).Linguisticallyspeaking,thesyntacticanalogiesdatasetisquitedifferentfromtherest,since
it relies more on contextual information from common words such as determiners (“the”, “each”,
“many”)andauxiliaryverbs(“will”,“had”)tosolvecorrectly. WeconjecturethatSGNSperforms
betteronthistaskbecauseitstrainingproceduregivesmoreinfluencetofrequentpairs,asopposed
toSVD’sobjective,whichgivesthesameweighttoallmatrixcells(seeSection3.2).
6 Conclusion
WeanalyzedtheSGNSwordembeddingalgorithms,andshowedthatitisimplicitlyfactorizingthe
(shifted)word-contextPMImatrixMPMI−logkusingper-observationstochasticgradientupdates.
We presented SPPMI, a modification of PPMI inspired by our theoretical findings. Indeed, using
SPPMIcanimproveuponthetraditionalPPMImatrix.ThoughSPPMIprovidesafarbettersolution
toSGNS’sobjective,itdoesnotnecessarilyperformbetterthanSGNSonlinguistictasks,asevident
withsyntacticanalogies. WesuspectthatthismayberelatedtoSGNSdown-weightingrarewords,
whichPMI-basedmethodsareknowntoexaggerate.
We also experimented with an alternative matrix factorization method, SVD. Although SVD was
relativelypooratoptimizingSGNS’sobjective,itperformedslightlybetterthantheothermethods
on word similarity datasets. However, SVD underperforms on the word-analogy task. One of the
main differences between the SVD and SGNS is that SGNS performs weighted matrix factoriza-
tion,whichmaybegivingitanedgeintheanalogytask. Asfutureworkwesuggestinvestigating
weightedmatrixfactorizationsofword-contextmatriceswithPMI-basedassociationmetrics.
Acknowledgements This work was partially supported by the EC-funded project EXCITEMENT
(FP7ICT-287923). WethankIdoDaganandPeterTurneyfortheirvaluableinsights.
8

References
[1] MarcoBaroni,GeorgianaDinu,andGerma´nKruszewski. Dontcount,predict! asystematiccomparison
| ofcontext-countingvs.context-predictingsemanticvectors. |     | InACL,2014. |     |
| ------------------------------------------------------- | --- | ----------- | --- |
[2] Marco Baroni and Alessandro Lenci. Distributional memory: A general framework for corpus-based
| semantics. | ComputationalLinguistics,36(4):673–721,2010. |     |     |
| ---------- | -------------------------------------------- | --- | --- |
[3] YoshuaBengio,Re´jeanDucharme,PascalVincent,andChristianJauvin. Aneuralprobabilisticlanguage
| model. JournalofMachineLearningResearch,3:1137–1155,2003. |     |     |     |
| --------------------------------------------------------- | --- | --- | --- |
[4] EliaBruni,GemmaBoleda,MarcoBaroni,andNamKhanhTran.Distributionalsemanticsintechnicolor.
InACL,2012.
[5] John A Bullinaria and Joseph P Levy. Extracting semantic representations from word co-occurrence
| statistics:acomputationalstudy. |     | BehaviorResearchMethods,39(3):510–526,2007. |     |
| ------------------------------- | --- | ------------------------------------------- | --- |
[6] John A Bullinaria and Joseph P Levy. Extracting semantic representations from word co-occurrence
| statistics:Stop-lists,stemming,andSVD. |     | BehaviorResearchMethods,44(3):890–907,2012. |     |
| -------------------------------------- | --- | ------------------------------------------- | --- |
[7] JohnCaron. ExperimentswithLSAscoring: optimalrankandbasis. InProceedingsoftheSIAMCom-
putationalInformationRetrievalWorkshop,pages157–169,2001.
[8] KennethWardChurchandPatrickHanks.Wordassociationnorms,mutualinformation,andlexicography.
Computationallinguistics,16(1):22–29,1990.
[9] RonanCollobertandJasonWeston. Aunifiedarchitecturefornaturallanguageprocessing: Deepneural
| networkswithmultitasklearning. |     | InICML,2008. |     |
| ------------------------------ | --- | ------------ | --- |
[10] RonanCollobert, JasonWeston, Le´onBottou, MichaelKarlen, KorayKavukcuoglu, andPavelKuksa.
Naturallanguageprocessing(almost)fromscratch. TheJournalofMachineLearningResearch,2011.
[11] IdoDagan,FernandoPereira,andLillianLee. Similarity-basedestimationofwordcooccurrenceproba-
| bilities. InACL,1994. |     |     |     |
| --------------------- | --- | --- | --- |
[12] C Eckart and G Young. The approximation of one matrix by another of lower rank. Psychometrika,
1:211–218,1936.
[13] LevFinkelstein,EvgeniyGabrilovich,YossiMatias,EhudRivlin,ZachSolan,GadiWolfman,andEytan
| Ruppin. | Placingsearchincontext:Theconceptrevisited. | ACMTOIS,2002. |     |
| ------- | ------------------------------------------- | ------------- | --- |
[14] YoavGoldbergandOmerLevy. word2vecexplained: derivingMikolovetal.’snegative-samplingword-
| embeddingmethod.   | arXivpreprintarXiv:1402.3722,2014. |                           |     |
| ------------------ | ---------------------------------- | ------------------------- | --- |
| [15] ZelligHarris. | Distributionalstructure.           | Word,10(23):146–162,1954. |     |
[16] Douwe Kiela and Stephen Clark. A systematic study of semantic vector space model parameters. In
WorkshoponContinuousVectorSpaceModelsandtheirCompositionality,2014.
[17] YehudaKoren,RobertBell,andChrisVolinsky. Matrixfactorizationtechniquesforrecommendersys-
| tems. Computer,2009.          |     |                                 |             |
| ----------------------------- | --- | ------------------------------- | ----------- |
| [18] OmerLevyandYoavGoldberg. |     | Dependency-basedwordembeddings. | InACL,2014. |
[19] OmerLevyandYoavGoldberg. Linguisticregularitiesinsparseandexplicitwordrepresentations. In
CoNLL,2014.
[20] TomasMikolov,KaiChen,GregCorrado,andJeffreyDean. Efficientestimationofwordrepresentations
| invectorspace. | CoRR,abs/1301.3781,2013. |     |     |
| -------------- | ------------------------ | --- | --- |
[21] TomasMikolov,IlyaSutskever,KaiChen,GregoryS.Corrado,andJeffreyDean. Distributedrepresen-
tationsofwordsandphrasesandtheircompositionality. InNIPS,2013.
[22] Tomas Mikolov, Wen-tau Yih, and Geoffrey Zweig. Linguistic regularities in continuous space word
| representations. | InNAACL,2013. |     |     |
| ---------------- | ------------- | --- | --- |
[23] AndriyMnihandGeoffreyEHinton. Ascalablehierarchicaldistributedlanguagemodel. InAdvancesin
NeuralInformationProcessingSystems,pages1081–1088,2008.
[24] Andriy Mnih and Koray Kavukcuoglu. Learning word embeddings efficiently with noise-contrastive
InNIPS,2013.
estimation.
[25] NathanSrebroandTommiJaakkola. Weightedlow-rankapproximations. InICML,2003.
[26] JosephTurian,LevRatinov,andYoshuaBengio. Wordrepresentations:asimpleandgeneralmethodfor
| semi-supervisedlearning. | InACL,2010. |     |     |
| ------------------------ | ----------- | --- | --- |
[27] PeterD.Turney. Miningthewebforsynonyms:PMI-IRversusLSAonTOEFL. InECML,2001.
[28] Peter D. Turney. Domain and function: A dual-space model of semantic relations and compositions.
JournalofArtificialIntelligenceResearch,44:533–585,2012.
[29] Peter D. Turney and Patrick Pantel. From frequency to meaning: Vector space models of semantics.
JournalofArtificialIntelligenceResearch,2010.
9
