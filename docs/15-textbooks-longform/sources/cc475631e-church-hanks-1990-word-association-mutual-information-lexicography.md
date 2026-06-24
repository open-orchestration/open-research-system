WORD ASSOCIATION NORMS, /IUTUAL INFORMATION,
AND LEXICOGRAPHY
Kenneth Ward Church
Bell Laboratories Murray Hill, N.J.
Patrick Hanks
Collins Publishers Glasgow, Scotland
The term word association is used in a very particular sense in the psycholinguistic literature. (Generally
speaking, subjects respond quicker than normal to the word nurse if it follows a highly associated word such
as doctor.) We will extend the term to provide the basis for a statistical description of a variety of interesting
linguistic phenomena, ranging from semantic relations of the doctor/nurse type (content word/content word)
to lexico-syntactic co-occurrence constraints between verbs and prepositions (content word/function word).
This paper will propose an objective measure based on the information theoretic notion of mutual
information, for estimating word association norms from computer readable corpora. (The standard method
of obtaining word association norms, testing a few thousand :mbjects on a few hundred words, is both costly
and unreliable.) The proposed measure, the association ratio, estimates word association norms directly
from computer readable corpora, making it possible to estimate norms for tens of thousands of words.
1 MEANINGA ND ASSOCIATION 2 PRACTICALA PPLICATIONS
It is common practice in linguistics to classify words not The proposed statistical description has a large number of
only on the basis of their meanings but also on the basis of potentially important applications, including: (a) constrain-
their co-occurrence with other words. Running through the ing the language model both for speech recognition and
whole Firthian tradition, for example, is the theme that optical character recognition (OCR), (b) providing disam-
"You shall know a word by the company it keeps" (Firth, biguation cues for parsing highly ambiguous syntactic struc-
1957). tures such as noun compounds, conjunctions, and preposi-
On the one hand, bank co-occurs with words and expres- tional phrases, (c) retrieving texts from large databases
sion such as money, notes, loan, account, investment, (e.g. newspapers, patents), (d) enhancing the productivity
clerk, official, manager, robbery, vaults, working in a, of computational linguists in compiling lexicons of lexico-
its actions, First National, of England, and so forth. On synWctic facts, and (e) enhancing the productivity of lexi-
the other hand, we find bank co-occurring with river, cographers in identifying normal and conventional usage.
swim, boat, east (and of course West and South, which Consider the optical character recognizer (OCR) appli-
have acquired special meanings of their own), on top of cation. Suppose that we have an OCR device as in Kahan et
the, and of the Rhine. (Hanks 1987, p. 127) al. (1987), and it has assigned about equal probability to
The search for increasingly delicate word classes is not new. having recognized farm and form, where the context is
In lexicography, for example, it goes back at least to the either: (1) federal credit or (2) some of.
"verb patterns" described in Hornby's Advanced Learner's
Dictionary (first edition 1948). What is new is that facili- farm
ties for the computational storage and analysis of large • federal ~form credit
bodies of natural language have developed significantly in
recent years, so that it is now becoming possible to test and
/farm
apply informal assertions of this kind in a more rigorous
way, and to see what company our words do keep.
22 Computational Linguistics Volume 16, Number 1, March 1990

Kenneth Church and Patrick Hanks  Word Association Norms, Mutual Information, and Lexicography
The proposed association measure can make use of the fact
Informally, mutual information compares the probability
that farm is much more likely in the first context and form  of observing x and y together (the joint probability) with
is much more likely in the second to resolve the ambiguity.  the  probabilities  of  observing  x  and  y  independently
| Note  that  alternative disambiguation  |     |     | methods  | based on  |     |     |     |     |     |
| --------------------------------------- | --- | --- | -------- | --------- | --- | --- | --- | --- | --- |
(chance). If there is a genuine association between x and y,
syntactic constraints such as part of speech are unlikely to  then the joint probability P(x,y) will be much larger than
help in this case since both form and farm are commonly  chance P(x) P(y), and consequently I(x,y) >> 0. If there is
used as nouns.  no interesting relationship between x and y, then P(x,y)
P(x) P(y), and thus, I(x,y) ~ O. If x and y are in comple-
mentary distribution, then P(x,y) will be much less than
P(x) P(y), forcing I(x,y) << 0.
3  WORD ASSOCIATION AND
PSYCHOLINGUISTICS  In our application, word probabilities P(x) and P(y) are
estimated by counting the number of observations of x and
Word association norms are well known to be an important
|     |     |     |     |     | y in a corpus, f  | (x) andf(y),  | and normalizing by N, the  |     |     |
| --- | --- | --- | --- | --- | ----------------- | ------------- | -------------------------- | --- | --- |
factor in psycholinguistic research, especially in the area of
size of the corpus. (Our examples use a number of different
| lexical  retrieval.  | Generally  | speaking,  | subjects  | respond  |     |     |     |     |     |
| -------------------- | ---------- | ---------- | --------- | -------- | --- | --- | --- | --- | --- |
corpora with different sizes: 15 million words for the 1987
quicker than normal to the word nurse if it follows a highly
AP corpus, 36 million words for the 1988 AP corpus, and
associated word such as doctor.
8.6 million tokens for the tagged corpus.) Joint probabili-
| Some  results  | and  implications  |     | are  summarized  | from  |     |     |     |     |     |
| -------------- | ------------------ | --- | ---------------- | ----- | --- | --- | --- | --- | --- |
ties, P(x,y), are estimated by counting the number of times
reaction-time experiments in which subjects either (a)  that x is followed by y in a window of w words, fw (x,y), and
classified successive strings of letters as words and non-
normalizing by N.
| words,  or  | (b)  pronounced  | the  | strings.  Both  | types of  |     |     |     |     |     |
| ----------- | ---------------- | ---- | --------------- | --------- | --- | --- | --- | --- | --- |
The window size parameter allows us to look at different
| response  | to words  (e.g.  | BUTTER)  | were consistently  |     |     |     |     |     |     |
| --------- | ---------------- | -------- | ------------------ | --- | --- | --- | --- | --- | --- |
scales. Smaller window sizes will identify fixed expressions
faster when preceded by associated words (e.g. BREAD)
(idioms such as bread and butter) and other relations that
| rather than unassociated words (e.g. NURSE)  |     |     |     | (Meyer  |     |     |     |     |     |
| -------------------------------------------- | --- | --- | --- | ------- | --- | --- | --- | --- | --- |
hold over short ranges; larger window sizes will highlight
et al. 1975, p. 98)  semantic concepts and other relationships that hold over
Much of this psycholinguistic research is based on empiri-
larger scales.
cal estimates of word association norms as in Palermo and
Table 1 may help show the contrast. 2 In fixed expres-
Jenkins (1964),  perhaps the most influential study of its  sions, such as bread and butter and drink and drive, the
kind, though extremely small and somewhat dated. This
words of interest are separated by a fixed number of words
study measured 200 words by asking a few thousand sub-
|     |     |     |     |     | and there is very little variance. In the  |     |     | 1988  | AP, it was  |
| --- | --- | --- | --- | --- | ------------------------------------------ | --- | --- | ----- | ----------- |
jects to write down a word after each of the 200 words to be  found that  the two words are always exactly two words
measured. Results are reported in tabular form, indicating
apart whenever they are found near each other (within five
which words were written down, and by how many subjects,
|                     |            |       |                     |      | words).  That      | is,  the  | mean  separation  | is  two,  | and  the  |
| ------------------- | ---------- | ----- | ------------------- | ---- | ------------------ | --------- | ----------------- | --------- | --------- |
| factored  by grade  | level and  | sex.  | The  word  doctor,  | for  | variance is zero.  |           |                   |           |           |
example, is reported on pp. 98-100 to be most often associ-
Compounds also have very fixed word order (little vari-
| ated with nurse, followed by sick, health, medicine,  |     |     |     | hospi-  |              |                                               |     |     |     |
| ----------------------------------------------------- | --- | --- | --- | ------- | ------------ | --------------------------------------------- | --- | --- | --- |
|                                                       |     |     |     |         | ance),  but  | the average separation is closer to one word  |     |     |     |
tal, man, sickness, lawyer, and about 70 more words.  rather than two. In contrast, relations such as man/woman
|     |     |     |     |     | are less fixed, as indicated  |     | by a  larger variance in their  |     |     |
| --- | --- | --- | --- | --- | ----------------------------- | --- | ------------------------------- | --- | --- |
separation. (The nearly zero value for the mean separation
4  AN INFORMATION THEORETIC MEASURE  for man/women indicates the words appear about equally
We propose an alternative measure, the association ratio,
for measuring word association norms, based on the infor-
Table 1. Mean and Variance of the Separation Between
| mation  theoretic  | concept  | of mutual  | information. 1 The  |     |     |     |     |     |     |
| ------------------ | -------- | ---------- | ------------------- | --- | --- | --- | --- | --- | --- |
X and Y
proposed measure is more objective and less costly than the
Separation
subjective method employed in Palermo and Jenkins (1964).
The association ratio can be scaled up to provide robust
|     |     |     |     |     | Relation  | Word x  | Word y  | Mean  | Variance  |
| --- | --- | --- | --- | --- | --------- | ------- | ------- | ----- | --------- |
estimates of word association norms for a large portion of
|     |     |     |     |     | Fixed  | break  | butter  | 2.00  | 0.00  |
| --- | --- | --- | --- | --- | ------ | ------ | ------- | ----- | ----- |
the language. Using the association ratio measure, the five
|     |     |     |     |     |     | drink  | drive  | 2.00  | 0.00  |
| --- | --- | --- | --- | --- | --- | ------ | ------ | ----- | ----- |
most associated words are, in order: dentists, nurses, treat-
|     |     |     |     |     | Compound  | computer  | scientist  | 1.12  | O. I 0  |
| --- | --- | --- | --- | --- | --------- | --------- | ---------- | ----- | ------- |
ing, treat, and hospitals.
|           |                         |     |            |           |     | United  | States  | 0.98  | 0.14  |
| --------- | ----------------------- | --- | ---------- | --------- | --- | ------- | ------- | ----- | ----- |
| What  is  | "mutual  information?"  |     | According  | to  Fano  |     |         |         |       |       |
(1961), if two points (words), x and y, have probabilities
|     |     |     |     |     | Semantic  | man  | woman  | 1.46  | 8.07  |
| --- | --- | --- | --- | --- | --------- | ---- | ------ | ----- | ----- |
P(x) and P(y), then their mutual information, I(x,y), is  man  women  - 0.12  13.08
defined to be
|     |                           |          |     |     | Lexical  | refraining  | from  | 1.11  | 0.20  |
| --- | ------------------------- | -------- | --- | --- | -------- | ----------- | ----- | ----- | ----- |
|     |                           | P(x, y)  |     |     |          | coming      | from  | 0.83  | 2.89  |
|     | I(x, y) =- log2 P(x)P(y)  |          |     |     |          | keeping     | from  | 2.14  | 5.53  |
Computational Linguistics Volume 16, Number 1, March 1990  23

Kenneth Church and Patrick Hanks  Word Association Norms, Mutual Information, and Lexicography
often in either order.)  Lexical relations come in several  tional  beneft  of assuring  that  Z f(x,y)  =  ~ f(x)  =
| varieties.  | There  | are  some like refraining from  |     |     |     | that  are  | Zf(y)  | = N.  |     |     |     |     |     |
| ----------- | ------ | ------------------------------- | --- | --- | --- | ---------- | ------ | ----- | --- | --- | --- | --- | --- |
When I(x, y) is large, the association ratio produces very
| fairly  fixed,  | others  | such  | as  coming from  |     | that  | may  be  |     |     |     |     |     |     |     |
| --------------- | ------- | ----- | ---------------- | --- | ----- | -------- | --- | --- | --- | --- | --- | --- | --- |
credible results not unlike those reported in Palermo and
| separated  | by an argument, and still  |     |     | others like keeping  |     |     |     |     |     |     |     |     |     |
| ---------- | -------------------------- | --- | --- | -------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
from that are almost certain to be separated by an argu-  Jenkins (1964), as illustrated in Table 3. In contrast, when
I(x, y) ---:0 , the pairs are less interesting. (As a very rough
ment.
rule; of thumb, we have observed that pairs with I(x, y) > 3
The ideal window size is different in each case. For the
remainder of this paper, the window size, w, will be set to  tend to be interesting, and pairs with smaller I(x, y)  are
|     |     |     |     |     |     |     | generally not.  |     | One can  | make this  | statement  |     | precise by  |
| --- | --- | --- | --- | --- | --- | --- | --------------- | --- | -------- | ---------- | ---------- | --- | ----------- |
five words as a compromise; this setting is large enough to
calibrating the measure with subjective measures. Alterna-
show some of the constraints between verbs and arguments,
but not so large that it would wash out constraints that  tively, one could make estimates of the variance and then
|     |     |     |     |     |     |     | make statements  |     | about confidence levels,  |     |     | e.g. with 95%  |     |
| --- | --- | --- | --- | --- | --- | --- | ---------------- | --- | ------------------------- | --- | --- | -------------- | --- |
make use of strict adjacency)
Since the association ratio becomes unstable when the  confidence, P(x, y) > e(x) P(y).)
counts are very small, we will not discuss word pairs with  If I(x, y)  << 0, we would predict that x  and y are in
complementary distribution. However, we are rarely able
f(x,y)  _< 5. An improvement would make use of t-scores,
|                      |     |     |                              |     |     |           | to observe I(x, y)  |     | << 0 because our corpora  |     |     |     | are too small  |
| -------------------- | --- | --- | ---------------------------- | --- | --- | --------- | ------------------- | --- | ------------------------- | --- | --- | --- | -------------- |
| and throw out pairs  |     |     | that  were not significant.  |     |     | Unfortu-  |                     |     |                           |     |     |     |                |
nately, this requires an estimate of the variance off(x,y),  (and our measurement techniques are too crude). Suppose,
for example, that both x and y appear about 10 times per
which goes beyond the scope of this paper. For the remain-
|     |     |     |     |     |     |     | million words of text. Then, P(x)  |     |     |     | =   | P(y)  | =  10 -5 and  |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------------- | --- | --- | --- | --- | ----- | ------------- |
der of this paper, we will adopt the simple but arbitrary
|     |     |     |     |     |     |     | chance is P(x) P(x)  |     | =   | 10 -I°. Thus, to say that I(x, y) is  |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | -------------------- | --- | --- | ------------------------------------- | --- | --- | --- |
threshold, and ignore pairs with small counts.
much less than 0, we need to say that P(x, y) is much less
Technically, the association ratio is different from mu-
than 10 -t°, a statement that is hard to make with much
tual information in two respects. First, joint probabilities
are supposed to be symmetric: P(x,y)  =  P(y, x),  and  confidence given the size of presently available corpora. In
|                |              |     |                             |     |     |     | fact, we cannot  |     | (easily)  | observe a  | probability less  |     | than  |
| -------------- | ------------ | --- | --------------------------- | --- | --- | --- | ---------------- | --- | --------- | ---------- | ----------------- | --- | ----- |
| thus,  mutual  | information  |     | is  also symmetric: I(x,y)  |     |     | =   |                  |     |           |            |                   |     |       |
1/N ~  10 -7, and therefore it is hard to know if I(x, y) is
I(y, x). However, the association ratio is not symmetric,
much less than chance or not, unless chance is very large.
sincef(x, y) encodes linear precedence. (Recall thatf(x, y)
(In fact, the pair a... doctors in Table 3, appears signifi-
denotes the number of times that word x appears before y
cantly less often than chance. But to justify this statement,
in the window of w words, not the number of times the two
we need to compensate for the window size (which shifts
words appear in either order.) Although we could fix this
|     |     |     |     |     |     |     | the score downward by 2.0, e.g. from 0.96 down to -  |     |     |     |     |     | 1.04),  |
| --- | --- | --- | --- | --- | --- | --- | ---------------------------------------------------- | --- | --- | --- | --- | --- | ------- |
problem by redefiningf(x, y) to be symmetric (by averag-
and we need to estimate the standard deviation, using a
ing the matrix with its transpose), we have decided not to
method such as Good (1953). 4
do so, since order information appears to be very interest-
ing. Notice the asymmetry in the pairs in Table 2 (com-
puted from 44 million words of 1988 AP text), illustrating a
|     |     |     |     |     |     |     |     | 5   | LEXICO-SYNTACTIC REGULARITIES  |     |     |     |     |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | ------------------------------ | --- | --- | --- | --- |
wide variety of biases ranging from sexism to syntax.
|                                           |     |     |     |     |                 |     | Although  | the  | psycholinguistic literature  |     |     | documents  | the  |
| ----------------------------------------- | --- | --- | --- | --- | --------------- | --- | --------- | ---- | ---------------------------- | --- | --- | ---------- | ---- |
| Second, one might expect f(x, y) <_ f(x)  |     |     |     |     | and f(x, y) <_  |     |           |      |                              |     |     |            |      |
f(y), but the way we have been counting, this needn't be  significance of noun/noun word associations such as doctor/
nurse in considerable detail, relatively little is said about
the case if x and y happen to appear several times in the
window. For example, given the sentence, "Library work-
ers were prohibited from saving books from this heap of
Table 3.  Some interesting Associations with "Doctor" in the
ruins," which appeared in an AP story on April 1, 1988,  1987 AP Corpus (N =  15 million)
| f(prohibited)  |     | =  1 and f(prohibited,  |     |     | from)  =  | 2. This  |     |     |     |     |     |     |     |
| -------------- | --- | ----------------------- | --- | --- | --------- | -------- | --- | --- | --- | --- | --- | --- | --- |
problem can be fixed by dividingf(x, y) by w -  1 (which  I(x, y)  f(x, y)  f(x)  x  f(y)  y
has the consequence of subtracting log2 (w -  1) =  2 from  11.3  12  111  honorary  621  doctor
our association ratio scores). This adjustment has the addi-  11.3  8  1105  doctors  44  dentists
|     |     |     |     |     |     |     | 10.7  | 30  | 1105  | doctors   |     | 241  | nurses    |
| --- | --- | --- | --- | --- | --- | --- | ----- | --- | ----- | --------- | --- | ---- | --------- |
|     |     |     |     |     |     |     | 9.4   | 8   | 1105  | doctors   |     | 154  | treating  |
|     |     |     |     |     |     |     |       |     |       | examined  |     |      | doctor    |
Table 2. Asymmetry in 1988 AP Corpus (N = 44 million)  9.0  6  275  621
|          |     |          |     |          |     |          | 8.9  | 11  | 1105  | doctors  |     | 317   | treat      |
| -------- | --- | -------- | --- | -------- | --- | -------- | ---- | --- | ----- | -------- | --- | ----- | ---------- |
| x        |     | y        |     | f(x, y)  |     | f(y, x)  | 8.7  | 25  | 621   | doctor   |     | 1407  | bills      |
|          |     |          |     |          |     |          | 8.7  | 6   | 621   | doctor   |     | 350   | visits     |
| doctors  |     | nurses   |     | 99       |     | 10       |      |     |       |          |     |       |            |
|          |     |          |     |          |     |          | 8.6  | 19  | 1105  | doctors  |     | 676   | hospitals  |
| man      |     | woman    |     | 256      |     | 56       |      |     |       |          |     |       |            |
|          |     |          |     |          |     |          | 8,4  | 6   | 241   | nurses   |     | 1105  | doctors    |
| doctors  |     | lawyers  |     | 29       |     | 19       |      |     |       |          |     |       |            |
| bread    |     | butter   |     | 15       |     | 1        |      |     |       |          |     |       |            |
Some Uninteresting Associations with "Doctor"
| save      |     | life   |     | 129   |     | 11  |       |     |         |         |     |        |          |
| --------- | --- | ------ | --- | ----- | --- | --- | ----- | --- | ------- | ------- | --- | ------ | -------- |
|           |     |        |     |       |     |     | 0.96  | 6   | 621     | doctor  |     | 73785  | with     |
| save      |     | money  |     | 187   |     | 11  |       |     |         |         |     |        |          |
|           |     |        |     |       |     |     | 0.95  | 41  | 284690  | a       |     | 1105   | doctors  |
| save      |     | from   |     | 176   |     | 18  |       |     |         |         |     |        |          |
| supposed  |     | to     |     | 1188  |     | 25  | 0.93  | 12  | 84716   | is      |     | 1105   | doctors  |
24  Computational Linguistics Volume 16, Number 1, March 1990

Kenneth Churcha nd Patrick Hanks  Word Association Norms, Mutual Information,a nd Lexicography
associations among verbs, function words, adjectives, and  associated;  the  last  three  are  not  so clear.  As  Sinclair
other non-nouns. In addition to identifying semantic rela-  suggests, the  approach is well suited for identifying the
tions of the doctor/nurse variety, we believe the association  phrasal verbs, at least in certain cases.
| ratio  can               | also  be used  | to        | search       | for  interesting  | lexico-  |     |                   |     |              |     |
| ------------------------ | -------------- | --------- | ------------ | ----------------- | -------- | --- | ----------------- | --- | ------------ | --- |
| syntactic relationships  |                | between   | verbs        | and  typical      | argu-    |     |                   |     |              |     |
|                          |                |           |              |                   |          |     | 6  PREPROCESSING  |     | WITH A PART  |     |
| ments/adjuncts.          | The            | proposed  | association  | ratio             | can  be  |     |                   |     |              |     |
viewed as a formalization of Sinclair's argument:  OF SPEECH TAGGER
How common are the  phrasal verbs with set?  Set  is  Phrasal verbs involving the preposition to raise an interest-
particularly  rich  in  making combinations  with  words  ing  problem because of the  possible confusion with  the
| like about,  | in,  up,  | out,  | on,  off,  | and  these words  | are  |                        |     |                                     |     |     |
| ------------ | --------- | ----- | ---------- | ----------------- | ---- | ---------------------- | --- | ----------------------------------- | --- | --- |
|              |           |       |            |                   |      | infinitive marker to.  |     | We have found that if we first tag  |     |     |
themselves very common. How likely is set offto occur?  every word in the corpus with a  part of speech using a
Both are frequent words set  occurs approximately 250  method such as Church (1988), and then measure associa-
times in a million words and off occurs approximately
tions between tagged words, we can identify interesting
556 times in a million words...  The  question we are  contrasts between verbs associated with a following prepo-
asking can be roughly rephrased as follows: how likely is  sition to~in and verbs associated with a following infinitive
| off to occur immediately after set?...  |     |     |     | This is 0.00025 x  |     |                |                                            |     |     |     |
| --------------------------------------- | --- | --- | --- | ------------------ | --- | -------------- | ------------------------------------------ | --- | --- | --- |
|                                         |     |     |     |                    |     | marker to~to.  | (Part of speech notation is borrowed from  |     |     |     |
0.00055  P(x)  P(y),  which gives us the tiny figure of  Francis and Kucera (1982); in =  preposition; to =  infini-
0.0000001375  ...  The assumption behind this calcula-  tive marker; vb =  bare verb; vbg =  verb +  ing; vbd =
tion is that the words are distributed at random in a text
|     |     |     |     |     |     | verb  +  ed; vbz  | =   | verb  +  s; vbn  | =  verb  +  | en.)  The  |
| --- | --- | --- | --- | --- | --- | ----------------- | --- | ---------------- | ----------- | ---------- |
at  chance, in our terminology.  It is obvious to a linguist  association ratio identifies quite a number of verbs associ-
that this is not so, and a rough measure of how much set  ated in an interesting way with to; restricting our attention
and offattract each other is to compare the probability
to pairs with a score of 3.0 or more, there are 768 verbs
with what actually happens  ...  Set  off occurs nearly  associated with the preposition to~in and 551  verbs with
70 times in the  7.3  million word corpus  P(x,  y)  =  the infinitive marker to/to. The ten verbs found to be most
| 70/(7.3  | x  106) >> P(x)  | P(y).  | That is enough to show  |     |     |     |     |     |     |     |
| -------- | ---------------- | ------ | ----------------------- | --- | --- | --- | --- | --- | --- | --- |
associated before to/in are:
its main patterning and it suggests that in currently-held
•  to~in: alluding/vbg, adhere/vb, amounted/vbn, relating/
corpora there will be found sufficient evidence for the
description  of a  substantial  collection  of phrases  ...  vbg, amounting/vbg, revert/vb, reverted/vbn, resorting/
vbg, relegated/vbn
(Sinclair 1987c, pp. 151-152).
|                                    |     |     |          |                |     | •  to~to:  obligated/vbn,  |     | trying/vbg,  | compelled/vbn,  | en-  |
| ---------------------------------- | --- | --- | -------- | -------------- | --- | -------------------------- | --- | ------------ | --------------- | ---- |
| Using Sinclair's estimates P(set)  |     |     | ~ 250 x  | 10 -6, P(off)  | ~-  |                            |     |              |                 |      |
556  x  10 -6, and P(set, off)  ~  70/(7.3  x  106), we would  ables/vbz,  supposed/vbn,  intends/vbz,  vowing/vbg,
tried/vbd, enabling/vbg, tends/vbz, tend/vb, intend/vb,
| estimate  | the  mutual  | information  |     | to  be  I(set; off)  | =   |     |     |     |     |     |
| --------- | ------------ | ------------ | --- | -------------------- | --- | --- | --- | --- | --- | --- |
tries/vbz
| log2P(set, off)/(P(set)  |                                              | P(off))  | ~   | 6.1.  In the  | 1988  AP  |     |     |     |     |     |
| ------------------------ | -------------------------------------------- | -------- | --- | ------------- | --------- | --- | --- | --- | --- | --- |
| corpus (N =              | 44,344,077), we estimate P(set) ~ 13,046/N,  |          |     |               |           |     |     |     |     |     |
Thus, we see there is considerable leverage to be gained by
P(off)  ~ 20,693/N, and P(set, off)  ~ 463/N. Given these  preprocessing the corpus and manipulating the inventory of
| estimates, we would compute the mutual information to be  |         |     |     |     |     | tokens.  |     |     |     |     |
| --------------------------------------------------------- | ------- | --- | --- | --- | --- | -------- | --- | --- | --- | --- |
| l(set; off)                                               | ~ 6.2.  |     |     |     |     |          |     |     |     |     |
In this example, at least, the values seem to be fairly
|     |     |     |     |     |     | 7   | PREPROCESSING  |     | WITH A PARSER  |     |
| --- | --- | --- | --- | --- | --- | --- | -------------- | --- | -------------- | --- |
comparable across corpora. In other examples, we will see
some differences due to sampling. Sinclair's corpus is a
Hindle (Church et al. 1989) has found it helpful to prepro-
| fairly balanced sample of (mainly British)  |     |     |     | text; the AP  |     |                  |       |                |                  |         |
| ------------------------------------------- | --- | --- | --- | ------------- | --- | ---------------- | ----- | -------------- | ---------------- | ------- |
|                                             |     |     |     |               |     | cess the  input  | with  | the  Fidditch  | parser  (Hindle  | 1983a,  |
corpus is an unbalanced sample of American journalese.
1983b)  to identify associations between verbs and argu-
This association between set and offis relatively strong;
|                                          |     |     |     |                       |     | ments, and  | postulate semantic classes for nouns on this  |     |     |     |
| ---------------------------------------- | --- | --- | --- | --------------------- | --- | ----------- | --------------------------------------------- | --- | --- | --- |
| the joint probability is more than 26 =  |     |     |     | 64 times larger than  |     |             |                                               |     |     |     |
basis. Hindle's method is able to find some very interesting
chance.  The other particles  that Sinclair  mentions have  associations, as Tables 5 and 6 demonstrate.
association ratios that can be seen in Table 4.
|                                                 |     |     |     |     |              | After running his parser over the  |     |     | 1988 AP corpus (44       |     |
| ----------------------------------------------- | --- | --- | --- | --- | ------------ | ---------------------------------- | --- | --- | ------------------------ | --- |
| The first three, set up, set off, and set out,  |     |     |     |     | are clearly  |                                    |     |     |                          |     |
|                                                 |     |     |     |     |              | million words), Hindle found N =   |     |     | 4,112,943 subject/verb/  |     |
object (SVO) triples. The mutual information between a
Table 4. Some Phrasal Verbs in 1988 AP Corpus  verb and  its object was computed from these 4  million
(N = 44 million)  triples by counting how often the verb and its object were
found in the same triple and dividing by chance. Thus, for
| x  y  | f(x)  |     | f(y)  | f(x, y)  | I(x; y)  |     |     |     |     |     |
| ----- | ----- | --- | ----- | -------- | -------- | --- | --- | --- | --- | --- |
example, disconnect/V and telephone/0 have a joint prob-
set  up  13,046  64,601  2713  7.3  ability of 7/N.  In this  case,  chance  is 84/N  x  481/N
set  off  13,046  20,693  463  6.2  because there are 84 SVO triples with the verb disconnect,
| set  out  | 13,046  |     | 47,956  | 301  | 4.4  |     |     |     |     |     |
| --------- | ------- | --- | ------- | ---- | ---- | --- | --- | --- | --- | --- |
and 481 SVO triples with the object telephone. The mutual
| set  on     | 13,046  |     | 258,170  | 162  | 1.1    |                                       |     |           |                       |             |
| ----------- | ------- | --- | -------- | ---- | ------ | ------------------------------------- | --- | --------- | --------------------- | ----------- |
|             |         |     |          |      |        | information is log z 7N/(84           |     | × 481) =  | 9.48. Similarly, the  |             |
| set  in     | 13,046  |     | 739,932  | 795  | 1.8    |                                       |     |           |                       |             |
|             |         |     |          |      |        | mutual information for drink/Vbeer/O  |     |           | is 9.9 =              | log 2 29N/  |
| set  about  | 13,046  |     | 82,319   | 16   | - 0.6  |                                       |     |           |                       |             |
(660 × 195). (drink/V and beer/O are found in 660 and
Computational Linguistics Volume 16, Number 1, March 1990  25

Kenneth Church and Patrick Hanks  Word Association Norms, Mutual Information, and Lexicography
Table 5. What Can You Drink?  readers, which introduced an element of selectivity and so
inevitably distortion (rare words and uses were collected
| Verb  | Object  | Mutual Info  | Joint Freq  |     |     |     |     |     |     |
| ----- | ------- | ------------ | ----------- | --- | --- | --- | --- | --- | --- |
but common uses of common words were not), or on small
| drink/V  | martinis/O  | 12.6  | 3   |     |     |     |     |     |     |
| -------- | ----------- | ----- | --- | --- | --- | --- | --- | --- | --- |
corpora of only a million words or so, which are reliably
| drink/V  | cup_water/O  | 11.6  | 3   |     |     |     |     |     |     |
| -------- | ------------ | ----- | --- | --- | --- | --- | --- | --- | --- |
informative for only the most common uses of the few most
| drink/V  | champagne/O  |     |     |     |     |     |     |     |     |
| -------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
10.9  3  frequent words of English. (A million-word corpus such as
| drink/V  | beverage/O  |       |     |     |     |     |     |     |     |
| -------- | ----------- | ----- | --- | --- | --- | --- | --- | --- | --- |
|          |             | 10.8  | 8   |     |     |     |     |     |     |
the Brown Corpus is reliable, roughly, for only some uses of
| drink/V  | cup_coffee/O  | 10.6  | 2   |     |     |     |     |     |     |
| -------- | ------------- | ----- | --- | --- | --- | --- | --- | --- | --- |
only some of the forms of around 4000 dictionary entries.
| drink/V  | cognacO/   | 10.6  | 2   |     |     |     |     |     |     |
| -------- | ---------- | ----- | --- | --- | --- | --- | --- | --- | --- |
drink/V  beer/O  9.9  29  But standard dictionaries typically contain twenty times
| drink/V  | eup/O  | 9.7  | 6   | this number of entries.)  |     |     |     |     |     |
| -------- | ------ | ---- | --- | ------------------------- | --- | --- | --- | --- | --- |
drink/V  coffee/O  The computational tools available for studying machine-
|          |          | 9.7  | 12  |     |     |     |     |     |     |
| -------- | -------- | ---- | --- | --- | --- | --- | --- | --- | --- |
| drink/V  | toast/O  |      |     |     |     |     |     |     |     |
9.6  4  readable corpora are at present still rather primitive. These
drink/V  alcohol/O  9.4  20  are  concordancing programs  (see  Figure  1),  which  are
drink/V  wine/O    9.3  10  basically KWIC (key word in context; Aho et al.  1988)
| drink/V  | fluid/O   | 9.0  | 5   |          |       |             |                 |                   |     |
| -------- | --------- | ---- | --- | -------- | ----- | ----------- | --------------- | ----------------- | --- |
|          |           |      |     | indexes  | with  | additional  | features  such  | as  the  ability  | to  |
| drink/V  | liquor/O  | 8.9  | 4   |          |       |             |                 |                   |     |
extend the context, sort leftward as well as rightward, and
| drink/V  | teaO  | 8.9  | 5   |     |     |     |     |     |     |
| -------- | ----- | ---- | --- | --- | --- | --- | --- | --- | --- |
so on. There is very little interactive software. In a typical
| drink/V  | milk/O  | 8.7  | 8   |     |     |     |     |     |     |
| -------- | ------- | ---- | --- | --- | --- | --- | --- | --- | --- |
drink/V  juice/O  situation in the lexicography of the 1980s, a lexicographer
|     |     | 8.3  | 4   |     |     |     |     |     |     |
| --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
drink/V  water/O  is giwen the concordances for a word, marks up the printout
|     |     | 7.2  | 43  |     |     |     |     |     |     |
| --- | --- | ---- | --- | --- | --- | --- | --- | --- | --- |
drink/V  quantityO  7.1  4  with colored pens to identify the salient senses, and then
writes syntactic descriptions and definitions.
|     |     |     |     | Although this  |     | technology is  | a  great  | improvement on  |     |
| --- | --- | --- | --- | -------------- | --- | -------------- | --------- | --------------- | --- |
195 SVO triples, respectively; they are found together in 29
using human readers to collect boxes of citation index cards
of these triples).
|     |     |     |     | (tlhe method  |     | Murray  used  | in  constructing  | The  | Oxford  |
| --- | --- | --- | --- | ------------- | --- | ------------- | ----------------- | ---- | ------- |
This application of Hindle's parser illustrates a second  English Dictionary a century ago), it works well if there are
| example of preprocessing the  |     | input  to highlight certain  |     |     |     |     |     |     |     |
| ----------------------------- | --- | ---------------------------- | --- | --- | --- | --- | --- | --- | --- |
no more than a few dozen concordance lines for a word, and
constraints of interest. For measuring syntactic constraints,
|     |     |     |     | only two or three  |     | main  | sense divisions.  | In analyzing a  |     |
| --- | --- | --- | --- | ------------------ | --- | ----- | ----------------- | --------------- | --- |
it may be useful to include some part of speech information  complex word such as take, save, or from, the lexicogra-
| and  to exclude much of the  |     | internal  structure  | of noun  |     |     |     |     |     |     |
| ---------------------------- | --- | -------------------- | -------- | --- | --- | --- | --- | --- | --- |
pher is trying to pick out significant patterns and subtle
phrases. For other purposes, it may be helpful to tag items
distinctions that are buried in literally thousands of concor-
| and/or  | phrases  with  semantic  | labels  such  | as  *person*,  |               |     |                                        |     |     |      |
| ------- | ------------------------ | ------------- | -------------- | ------------- | --- | -------------------------------------- | --- | --- | ---- |
|         |                          |               |                | dance lines:  |     | pages and pages of computer printout.  |     |     | The  |
*place*, *time*, *body part*, *bad*, and so on.
unaided human mind simply cannot discover all the signifi-
|     | 8  APPLICATIONS IN LEXICOGRAPHY  |     |     |                                                     |     |     |                        |     |     |
| --- | -------------------------------- | --- | --- | --------------------------------------------------- | --- | --- | ---------------------- | --- | --- |
|     |                                  |     |     | Is Su~Say, calling for ~x~ater economic reforms to  |     |     | save Oatha ~  poveay.  |     |     |
Large machine-readable corpora are only just now becom-
|     |     |     |     | mmi~:ion asseaed that " the Postal Se~wice could  |     |     | save enormous sums of money in conwacling out individual e  |     |     |
| --- | --- | --- | --- | ------------------------------------------------- | --- | --- | ----------------------------------------------------------- | --- | --- |
ing available to lexicographers. Up to now, lexicographers
|     |     |     |     |     | Then. sl0e said, the family hopes to  |     | save enough for a down payment on a boule.  |     |     |
| --- | --- | --- | --- | --- | ------------------------------------- | --- | ------------------------------------------- | --- | --- |
have been reliant either on citations collected by human
|     |     |     |     | e out-of-work steelworker, " because that doesn't  |                                             |     | save jobs, that costs jobs. "                               |     |     |
| --- | --- | --- | --- | -------------------------------------------------- | ------------------------------------------- | --- | ----------------------------------------------------------- | --- | --- |
|     |     |     |     |                                                    | ....  We suspend reality when we say we'll  |     | save money by spending $10,000 in wage~ for a public work~  |     |     |
Table 6.  What Can You Do to a Telephone?
|     |     |     |     | sclent~ts has won the first round in an effort to  |     |     | save one of Egypt's great m:Lsxtre.s, the decaying tomb of R  |     |     |
| --- | --- | --- | --- | -------------------------------------------------- | --- | --- | ------------------------------------------------------------- | --- | --- |
save the " pit ponies " doomed to be slaughtered.
Verb  Object  Mutual Info  Joint Freq  about three children in a mining town who plot to
|               |              |        |     |                                                       | GM executives say the slmtdow~ will  |     | save the automaker $500 million a year in operating e~ts a    |     |     |
| ------------- | ------------ | ------ | --- | ----------------------------------------------------- | ------------------------------------ | --- | ------------------------------------------------------------- | --- | --- |
| sit_by/V      | telephone/O  | 11.78  | 7   |                                                       |                                      |     |                                                               |     |     |
|               |              |        |     | rtr~ent as receiver, lilstracted officials to U3, to  |                                      |     | save the ¢¢m3pany rather than liquidate it and then declared  |     |     |
| disconnect/V  | telephone/O  | 9.48   | 7   |                                                       |                                      |     |                                                               |     |     |
answer/V  telephone/O  8.80  98  The package, which is to  save the counW/nearly $2 billion, also includes a program
hang_upV  telephone/O  7.87  3  newly enhanced image as the moderate who moved to  save the counw/.
tap/V  telephone/O  7.69  15  mffiina offer from chairman Victor Posner to help  save the financially troubled company, but said Pc~er stil
| pick_up/V  | telephone/O  |     |     |     |     |     |     |     |     |
| ---------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
5.63  11  after tellinga  delivery-room doctor not to try to  save the infant by imsertlnli a tube in its throat to belp i
| return/V  | telephone/O  |     |     |     |     |     |     |     |     |
| --------- | ------------ | --- | --- | --- | --- | --- | --- | --- | --- |
5.01  19  h bliffiday Tmr~day, cheered by those who fought to  save the majestic Beaux Arts arcl~tecmralm E~-telpiece.
be_by/V  telephone/O  4.93  2  save ate nation from commumsm.
at be ~sl formed an alliance with Moslem rebels to
| spot/V    | telephone/O  | 4.43  | 2   |     |     |                          |                                                                |     |     |
| --------- | ------------ | ----- | --- | --- | --- | ------------------------ | -------------------------------------------------------------- | --- | --- |
|           |              |       |     |     |     | • ' Basically we could   | save the operatingc osts of the Pershing,s  and ground-launch  |     |     |
| repeat/V  | telephone/O  | 4.39  | 3   |     |     |                          |                                                                |     |     |
|           |              |       |     |     |     | We worked for a year to  | save the ~te at enormous expense to us, " said Leveilee.       |     |     |
| place/V   | telephone/O  | 4.23  | 7   |     |     |                          |                                                                |     |     |
receive/V  telephone/O  4.22  28  their expet~ive mirrors, just like in wartime, to  save them fi~m diamken yankee brawlel~, " Ta~ said.
install/V  telephone/O  4.20  2  ald of many who risked their Own lives in order to  save those who were p~=aengers. "
be_on/V  telephone/O  We must increase tile amount Americans  save. "
|            |              | 4.05  | 15  |     |                                              |     |     |     |     |
| ---------- | ------------ | ----- | --- | --- | -------------------------------------------- | --- | --- | --- | --- |
| come_to/V  | telephone/O  |       |     |     |                                              |     |     |     |     |
|            |              | 3.63  | 6   |     | Figure 1 Short Sample of the Concordance to  |     |     |     |     |
use/V  telephone/O  3.59  29  "save" from the AP 1987 Corpus.
| operate/V  | telephone/O  | 3.16  | 4   |     |     |     |     |     |     |
| ---------- | ------------ | ----- | --- | --- | --- | --- | --- | --- | --- |
26  Computational Linguistics Volume 16, Number 1, March 1990

Kenneth Church and Patrick Hanks  Word Association Norms, Mutual Information, and Lexicography
cant patterns, let alone group them and rank them in order
British learners' dictionaries do make specific mention of
of importance.
from  in connection with save. These learners' dictionaries
The AP 1987 concordance to save is many pages long;  pay more attention to language structure and collocation
there are 666 lines for the base form alone, and many more
than do American collegiate dictionaries, and lexicogra-
for the inflected forms saved, saves, saving, and savings. In  phers trained in the British tradition are often fairly skilled
the discussion that follows, we shall, for the sake of simplic-  at  spotting  these generalizations.  However,  teasing out
ity, not analyze the inflected forms and we shall only look at
|     |     |     | such facts and distinguishing true  |     | intuitions from false  |     |
| --- | --- | --- | ----------------------------------- | --- | ---------------------- | --- |
the patterns to the right of save (see Table 7).
intuitions takes a lot of time and hard work, and there is a
It is hard to know what is important in such a concor-  high probability of inconsistencies and omissions.
dance and what is not. For example, although it is easy to
Which other verbs typically associate with from,  and
see from the concordance selection in Figure 1 that the
where does save rank in such a list? The association ratio
word "to" often comes before "save" and the word "the"  identified 1530 words that are associated with from; 911 of
often comes after "save," it is hard to say from examination
them were tagged as verbs. The first 100 verbs are:
of a concordance alone whether either or both of these
|     |     |     | refrain/vb,  | gleaned/vbn,  | stems/vbz,  | stemmed/vbd,  |
| --- | --- | --- | ------------ | ------------- | ----------- | ------------- |
co-occurrences have any significance.  stemming/vbg,  ranging/vbg,  stemmed/vbn,  ranged/
Two examples will illustrate how the association ratio  vbn, derived/vbn, ranged/vbd, extort/vb, graduated/
measure helps make the analysis both quicker and more
vbd, barred/vbn, benefiting/vbg, benefitted/vbn, bene-
accurate.  fited/vbn, excused/vbd, arising/vbg, range/vb, exempts/
|     |     |     | vbz,  suffers/vbz,  | exempting/vbg,  |     | benefited/vbd,  |
| --- | --- | --- | ------------------- | --------------- | --- | --------------- |
8.1  EXAMPLE 1: "SAVE ... FROM"
prevented/vbd (7.0), seeping/vbg, barred/vbd, prevents/
The association ratios in Table 7 show that association  vbz, suffering/vbg, excluded/vbn, marks/vbz, profiting/
norms apply to function words as well as content words. For
vbg, recovering/vbg, discharged/vbn, rebounding/vbg,
example, one of the words significantly associated with save  vary/vb,  exempted/vbn,  separate/vb,  banished/vbn,
is from.  Many dictionaries, for example Webster's Ninth  withdrawing/vbg, ferry/vb, prevented/vbn, profit/vb,
(Merriam Webster), make no
New  Collegiate Dictionary  bar/vb,  excused/vbn, bars/vbz,  benefit/vb, emerges/
explicit mention of from  in the entry for save,  although  vbz,  emerge/vb,  varies/vbz,  differ/vb, removed/vbn,
exempt/vb, expelled/vbn, withdraw/vb, stem/vb, sepa-
Table 7. Words Often Co-Occurring to the Right of"Save"  rated/vbn, judging/vbg, adapted/vbn, escaping/vbg, in-
herited/vbn, differed/vbd, emerged/vbd, withheld/vbd,
| I(x, y)  f(x, y)  | f(x)  x  | f(y)  y  |     |     |     |     |
| ----------------- | -------- | -------- | --- | --- | --- | --- |
leaked/vbn, strip/vb, resulting/vbg, discourage/vb, pre-
9.5  6  724  170  vent/vb, withdrew/vbd, prohibits/vbz, borrowing/vbg,
save  forests
9.4  6  724  save  180  $1.2  preventing/vbg, prohibit/vb,  resulted/vbd  (6.0),  pre-
8.8  37  724  save  1697  lives  clude/vb, divert/vb, distinguish/vb, pulled/vbn, fell/
| 8.7  6  | 724  save  | 301  enormous  |     |     |     |     |
| ------- | ---------- | -------------- | --- | --- | --- | --- |
vbn, varied/vbn, emerging/vbg, suffer/vb, prohibiting/
| 8.3  7   | 724  save  | 447  annually  |                    |               |              |             |
| -------- | ---------- | -------------- | ------------------ | ------------- | ------------ | ----------- |
|          |            |                | vbg,  extract/vb,  | subtract/vb,  | recover/vb,  | paralyzed/  |
| 7.7  20  | 724  save  | 2001  jobs     |                    |               |              |             |
vbn, stole/vbd, departing/vbg, escaped/vbn, prohibited/
| 7.6  64  | 724  save  | 6776  money  |                                          |     |     |               |
| -------- | ---------- | ------------ | ---------------------------------------- | --- | --- | ------------- |
|          |            |              | vbn, forbid/vb, evacuated/vbn, reap/vb,  |     |     | barring/vbg,  |
| 7.2  36  | 724        | 4875         |                                          |     |     |               |
save  life
removing/vbg, stolen/vbn, receives/vbz.
| 6.6  8  | 724  save  | 1668  dollars  |              |                                                |     |     |
| ------- | ---------- | -------------- | ------------ | ---------------------------------------------- | --- | --- |
|         |            |                | Save...from  | is a good example for illustrating the advan-  |     |     |
| 6.4  7  | 724  save  | 1719  costs    |              |                                                |     |     |
6.4  6  724  save  1481  thousands  tages of the association ratio. Save is ranked 319th in this
6.2  9  724  save  2590  face  list, indicating that the association is modest, strong enough
5.7  6  724  save  2311  son  to be important (21 times more likely than chance), but not
5.7  6  724  2387  so strong that it would pop out at us in a concordance, or
save  estimated
| 5.5  7  | 724  | 3141  |     |     |     |     |
| ------- | ---- | ----- | --- | --- | --- | --- |
save  your  that it would be one of the first things to come to mind.
| 5.5  24  | 724  | 10880  |     |     |     |     |
| -------- | ---- | ------ | --- | --- | --- | --- |
save  billion  If the dictionary is going to list save..,  from,  then, for
5.3  39  724  save  20846  million  consistency's sake, it ought to consider listing all of the
| 5.2  8  | 724  save  | 4398  us  |     |     |     |     |
| ------- | ---------- | --------- | --- | --- | --- | --- |
more important associations as well. Of the 27 bare verbs
| 5.1  6  | 724  save  | 3513  less  |     |     |     |     |
| ------- | ---------- | ----------- | --- | --- | --- | --- |
(tagged 'vb') in the list above, all but seven are listed in
| 5.0  7  | 724  save  | 4590  own  |     |     |     |     |
| ------- | ---------- | ---------- | --- | --- | --- | --- |
Collins Cobuild English Language Dictionary as occurring
| 4.6  7  | 724  save  | 5798  world  |     |     |     |     |
| ------- | ---------- | ------------ | --- | --- | --- | --- |
4.6  7  724  save  6028  my  with from.  However, this dictionary does not note that
4.6  15  724  13010  vary, ferry, strip, divert, forbid,  and reap occur with from.
save  them
If the Cobuild lexicographers had had access to the pro-
| 4.5  8  | 724  save  | 7434  country  |     |     |     |     |
| ------- | ---------- | -------------- | --- | --- | --- | --- |
4.4  15  724  save  14296  time  posed measure, they could possibly have obtained better
| 4.4  64  | 724  save  | 61262  from  | coverage at less cost.  |     |     |     |
| -------- | ---------- | ------------ | ----------------------- | --- | --- | --- |
| 4.3  23  | 724  save  | 23258  more  |                         |     |     |     |
4.2  25  724  save  27367  their  8.2  EXAMPLE2 : IDENTIFYING SEMANTIC CLASSES
| 4.1  8  | 724  save  | 9249  company  |                               |                                   |                    |         |
| ------- | ---------- | -------------- | ----------------------------- | --------------------------------- | ------------------ | ------- |
|         |            |                | Having established            | the  relative importance of save  |                    |         |
| 4.1  6  | 724  save  | 7114  month    |                               |                                   |                    | ...     |
|         |            |                | from,  and having noted that  |                                   | the two words are  | rarely  |
Computational Linguistics Volume 16, Number 1, March 1990  27

Kenneth Church and Patrick Hanks  Word Association Norms, Mutual Information, and Lexicography
adjacent, we would now like to speed up the labor-intensive  clear fi'om the association ratio table above that annually
and month 6 are commonly found with save. More detailed
| task  of categorizing  | the  | concordance  | lines.  | Ideally,  we  |     |     |     |     |     |     |
| ---------------------- | ---- | ------------ | ------- | ------------- | --- | --- | --- | --- | --- | --- |
would like to develop a  set of semi-automatic tools that  inspection shows that the time adverbials correlate interest-
would help a lexicographer produce something like Figure  ingly with just one group of save  objects, namely those
2, which provides an annotated summary of the 65 concor-  tagged  MONEY.  The AP wire is full of discussions of
dance lines for save ... from. 5 The save ...  from  pattern  saving $1.2 billion per month; computational lexicography
occurs in about 10% of the 666 concordance lines for save.  should measure and record such patterns if they are gen-
Traditionally, semantic categories have been only vaguely  eral, even when traditional dictionaries do not.
recognized, and to date little effort has been devoted to a  A,; another example illustrating how the association ratio
tables would have helped us analyze the save concordance
systematic classification of a large corpus. Lexicographers
have tended to use concordances impressionistically; seman-  lines, we found ourselves contemplating the semantic tag
tic theorists, AI-ers, and others have concentrated on a few  ENV(IRONMENT) to analyze lines such as:
interesting  examples, e.g.  bachelor,  and  have not  given  the trend to  save the forestsENV
much thought to how the results might be scaled up.
|     |     |     |     |     | it's our turn to  |     | save the lakeENV,  |     |     |     |
| --- | --- | --- | --- | --- | ----------------- | --- | ------------------ | --- | --- | --- |
With this concern in mind, it seems reasonable to ask
|                                          |     |     |                        |     | joined a fight to   |     | save their forestsENV,  |     |     |     |
| ---------------------------------------- | --- | --- | ---------------------- | --- | ------------------- | --- | ----------------------- | --- | --- | --- |
| how well these 65 lines for save...from  |     |     | fit in with all other  |     |                     |     |                         |     |     |     |
|                                          |     |     |                        |     | can we get busy to  |     | save the planetENV      |     | ?   |     |
uses of save A laborious concordance analysis was under-
taken to answer this question. When it was nearing comple-  If we  had  looked  at  the  association  ratio  tables  before
tion, we noticed that the tags that we were inventing to  labC.ing the  65  lines  for save  ...  from,  we might  have
|     |     |     |     |     | noticed the very large value for save..,  |     |     | forests, suggesting  |     |     |
| --- | --- | --- | --- | --- | ----------------------------------------- | --- | --- | -------------------- | --- | --- |
capture the generalizations could in most cases have been
suggested  by  looking  at  the  lexical  items  listed  in  the  that there may be an important pattern here. In fact, this
association ratio table for save. For example, we had failed  pattern probably subsumes most of the occurrences of the
|                                                                |     |     |     |     | ANIMAL"  |     | pattern  noticed  | in  Figure  | 2.  | Thus,  |
| -------------------------------------------------------------- | --- | --- | --- | --- | -------- | --- | ----------------- | ----------- | --- | ------ |
| to notice the significance of time adverbials in our analysis  |     |     |     |     | "save    |     |                   |             |     |        |
of save,  and no dictionary records this. Yet it should be  these tables do not provide semantic tags, but they provide
a powerful set of suggestions to the lexicographer for what
needs to be accounted for in choosing a set of semantic tags.
save X from Y (65 concordance lines)  It may be that everything said here about save and other
words is true only of 1987 American journalese. Intuitively,
1 save PERSON from Y (23 concordance lines)  however, many of the patterns discovered seem to be good
1.1 save PERSON from BAD (19 concordance lines)  candidates  for conventions of general  English.  A  future
step would be to examine other more balanced corpora and
| ( Robert DeNiro ) to  | save Indian tribes(PERSON from genocideDESTRUCTBAD  |     |     | at the hands of  |     |     |     |     |     |     |
| --------------------- | --------------------------------------------------- | --- | --- | ---------------- | --- | --- | --- | --- | --- | --- |
test how well the patterns hold up.
| " We wanted to            | save him(PERSON ~orn undue ~oubleBAD                 |     | and loss(BAD of money , "  |     |     |     |     |     |     |     |
| ------------------------- | ---------------------------------------------------- | --- | -------------------------- | --- | --- | --- | --- | --- | --- | --- |
| Murphy was sacrificed to  | save more powerful Democrats(PERSON from harm(BAD .  |     |                            |     |     |     |     |     |     |     |
" God sent this man to  save my five children(PERSON from being burned to death(DESTRUCT(BAD  and  9  CONCLUSIONS
| Pope John Paul I to "  | save us(PERSON fl~m sin(BAD . "  |     |     |     |     |     |     |     |     |     |
| ---------------------- | -------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
We began this paper with the psycholinguistic notion of
1.2 save PERSON from (BAD) LOC(AT1ON) (4 concordance lines)  word association norm, and extended that concept toward
| rescuers who helped  | save the toddler(PERSON from an abandoned weULOC will be feted with a parade  |     |     |     |     |     |     |     |     |     |
| -------------------- | ----------------------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
the information theoretic definition of mutual information.
while attempting to  save two drowning hoysPERSON  from a turbulent(BAD creeklLOC in OtdoLOC  This provided a precise statistical calculation that could be
applied to a very large corpus of text to produce a table of
2. save INST(ITUTION) from (ECON) BAD (27 concordance lines)
associations for tens of thousands of words. We were then
| member states to help  | save the EECINSTI from possible bankaxlptcyBCONBAD  |                         | this year.  |     |                                              |      |                 |            |                |          |
| ---------------------- | --------------------------------------------------- | ----------------------- | ----------- | --- | -------------------------------------------- | ---- | --------------- | ---------- | -------------- | -------- |
|                        |                                                     |                         |             |     | able  to  show that                          | the  | table  encoded  | a  number  |                | of very  |
| should be sought " to  | save the compenyCORP1NST                            | from bankmptfyBCONBAD.  |             |     |                                              |      |                 |            |                |          |
|                        |                                                     |                         |             |     | interesting patterns ranging from doctor..,  |      |                 |            | nurse to save  |          |
|                        | save the counffyNATIOlqlNST                         | flora disaster(BAD.     |             |     |                                              |      |                 |            |                |          |
law was necessary to
|                 |                               |                             |     |     | ....from.  We finally concluded by showing how the pat-  |     |     |     |     |     |
| --------------- | ----------------------------- | --------------------------- | --- | --- | -------------------------------------------------------- | --- | --- | --- | --- | --- |
| operation " to  | save the nation(NATION(INS'r  | from COmmUnL~nBADPOL1TICAL  |     | .   |                                                          |     |     |     |     |     |
terns in the association ratio table might help a lexicogra-
| were not needed to  | save the system from benkauptcyECONBAD.  |     |     |     |     |     |     |     |     |     |
| ------------------- | ---------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
pher organize a concordance.
| his efforts to  | save the woddINST  from the like~ of Lothax and the Spider Woman  |     |     |     |     |     |     |     |     |     |
| --------------- | ----------------------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
In point of fact, we actually developed these results in
|     |     |     |     |     | basically the reverse order.  |     | Concordance analysis is still  |     |     |     |
| --- | --- | --- | --- | --- | ----------------------------- | --- | ------------------------------ | --- | --- | --- |
3. save ANIMAL from DESTRUCT(ION) (5 concordance lines)
extremely labor-intensive and prone to errors of omission.
| give them the money to  | save the dogs(ANIMAL from being destroyed(DESTRUCT ,  |     |     |     |     |     |     |     |     |     |
| ----------------------- | ----------------------------------------------------- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
The ways that concordances are sorted don't adequately
| program intended to  | save the giant birds(ANIMAL ~om extinctionDESTRUCTI,  |     |     |     |                   |                          |     |              |     |       |
| -------------------- | ----------------------------------------------------- | --- | --- | --- | ----------------- | ------------------------ | --- | ------------ | --- | ----- |
|                      |                                                       |     |     |     | support  current  | lexicographic practice.  |     | Despite the  |     | fact  |
UNCLASSIFIED (10 concordance lines)  that  a  concordance  is  indexed  by  a  single  word,  often
walnut and ash tx~es to  save them from the axes and saws of a logging company.  lexicographers actually use a second word such as from  or
after the a~aek to  save the ship from a tembleBAD  fire, Navy reports concluded Thursday.  an equally common semantic concept such as a time adver-
cemficates that would  save shopper~pERSON  anywhere f~m $50MONEY  NUMBER  to $500MONEY  (/flu  bial to decide how to categorize concordance lines. In other
Figure 2 Some AP 1987 Concordance Lines to  words, they use two words to triangulate in on a word sense.
" Roughly Sorted into Categories.  This triangulation approach clusters concordance lines to-
"save...from,
gether into word senses based primarily on usage (distribu-
28  Computational Linguistics Volume 16, Number 1, March 1990

Kenneth Church and Patrick Hanks  Word Association Norms, Mutual Information, and Lexicography
tional evidence), as opposed to intuitive notions of meaning.  Hindle, D. 1983a "Deterministic Parsing of Syntactic Non-fluencies." In
Thus, the question of what is a word sense can be addressed  Proceedings of the 23rd Annual Meeting of the Association for Compu-
tational Linguistics.
| with  syntactic  | methods  |     | (symbol  pushing),  |     | and  need  not  |     |     |     |     |     |
| ---------------- | -------- | --- | ------------------- | --- | --------------- | --- | --- | --- | --- | --- |
Hindle, D. 1983b "User Manual for Fidditch, a Deterministic Parser."
| address semantics (interpretation),  |     |     |     | even though the inven-  |     |     |     |     |     |     |
| ------------------------------------ | --- | --- | --- | ----------------------- | --- | --- | --- | --- | --- | --- |
Naval Research Laboratory Technical Memorandum #7590-142.
tory of tags may appear to have semantic values.  Hornby, A. 1948 The Advanced Learner's Dictionary, Oxford University
| The triangulation approach requires "art." How does the  |     |     |     |     |     | Press, Oxford, U.K.  |     |     |     |     |
| -------------------------------------------------------- | --- | --- | --- | --- | --- | -------------------- | --- | --- | --- | --- |
lexicographer  decide  which  potential  cut  points  are  Jelinek, F. 1982. (personal communication)
|                |              |                         |                  |             |                 | Kahan, S.; Pavlidis, T.; and Baird, H.                      |     | 1987 "On the Recognition  |     | of     |
| -------------- | ------------ | ----------------------- | ---------------- | ----------- | --------------- | ----------------------------------------------------------- | --- | ------------------------- | --- | ------ |
| "interesting"  | and          | which                   | are  merely due  | to chance?  | The             |                                                             |     |                           |     |        |
|                |              |                         |                  |             |                 | Printed Characters of any Font or Size," IEEE Transactions  |     |                           |     | PAMI,  |
| proposed       | association  | ratio score provides a  |                  |             | practical  and  |                                                             |     |                           |     |        |
274-287.
objective measure that is often a fairly good approximation
Meyer, D.; Schvaneveldt, R.; and Ruddy, M. 1975 "Loci of Contextual
to the "art." Since the proposed measure is objective, it can  Effects on Visual Word-Recognition," in P. Rabbitt and S. Dornic
be applied in a systematic way over a large body of mate-  (eds.), Attention and Performance V, Academic Press, New York.
rial, steadily improving consistency and productivity.  Palermo, D. and Jenkins, J. 1964 "Word AssociationNorms." University
of Minnesota Press, Minneapolis, MN.
But on the other hand, the objective score can be mislead-
Sinclair, J.; Hanks, P.; Fox, G.; Moon, R.; and Stock, P. (eds.) 1987a
| ing. The score takes only distributional  |           |      |          | evidence into ac-  |                 |                          |                       |     |                      |     |
| ----------------------------------------- | --------- | ---- | -------- | ------------------ | --------------- | ------------------------ | --------------------- | --- | -------------------- | --- |
|                                           |           |      |          |                    |                 | Collins Cobuild English  | Language Dictionary.  |     | Collins, London and  |     |
| count.  For                               | example,  | the  | measure  | favors set         | ...  for  over  |                          |                       |     |                      |     |
Glasgow.
set  ...  down;  it  doesn't  know  that  the  former  is  less  Sinclair, J. 1987b "The Nature of the Evidence," in J. Sinclair (ed.),
interesting  because  its  semantics  are  compositional.  In  Looking Up: An Account of the COBUILD Project in Lexical Comput-
addition,  the  measure  is extremely  superficial;  it cannot  ing. Collins, London and Glasgow.
Smadja,  F. In press. "Microcoding the Lexicon with Co-Occurrence
cluster words into appropriate syntactic classes without an
|                       |     |       |               |        |              | Knowledge," in Zernik (ed.), Lexical Acquisition:  |     |     | Using On-Line Re-  |     |
| --------------------- | --- | ----- | ------------- | ------ | ------------ | -------------------------------------------------- | --- | --- | ------------------ | --- |
| explicit  preprocess  |     | such  | as  Church's  | parts  | program  or  |                                                    |     |     |                    |     |
sources to Build a Lexicon, MIT Press, Cambridge, MA.
Hindle's parser. Neither of these preprocesses, though, can
help highlight the "natural" similarity between nouns such
| as picture and photograph.  |     |     | Although one might imagine a  |     |     |     |     |     |     |     |
| --------------------------- | --- | --- | ----------------------------- | --- | --- | --- | --- | --- | --- | --- |
preprocess that would help in this particular case, there will
NOTES
| probably  | always  | be  a  class  | of  generalizations  |     | that  are  |     |     |     |     |     |
| --------- | ------- | ------------- | -------------------- | --- | ---------- | --- | --- | --- | --- | --- |
1.  This statistic has also been used by the IBM speech group (Jelinek
| obvious to an  | intelligent lexicographer,  |     |     | but  | lie hopelessly  |                         |                                   |     |     |            |
| -------------- | --------------------------- | --- | --- | ---- | --------------- | ----------------------- | --------------------------------- | --- | --- | ---------- |
|                |                             |     |     |      |                 | 1982) for constructing  | language models for applications  |     |     | in speech  |
beyond the objectivity of a computer.
recognition.
Despite these problems, the association ratio could be an  2.  Smadja (in press) discusses the separation  between collocates in a
| important tool to aid the lexicographer, rather like an index  |     |     |     |     |     | very similar way.  |     |     |     |     |
| -------------------------------------------------------------- | --- | --- | --- | --- | --- | ------------------ | --- | --- | --- | --- |
to the concordances. It can help us decide what to look for;  3.  This definition fw(x,y)  uses a rectangular window. It might be
interesting  to consider alternatives (e.g. a triangular window or a
it provides a quick summary of what company our words do
decaying exponential) that would weight words less and less as they
keep.
|     |     |     |     |     |     | are separated  by more and more words. Other windows are also  |                        |     |                   |     |
| --- | --- | --- | --- | --- | --- | -------------------------------------------------------------- | ---------------------- | --- | ----------------- | --- |
|     |     |     |     |     |     | possible. For example,                                         | Hindle (Church et al.  |     | 1989) has used a  |     |
syntactic parser to select words in certain constructions of interest.
REFERENCES
4.  Although the Good-Turing Method (Good 1953) is more than 35
Church, K. 1988 "A Stochastic Parts Program and Noun Phrase Parser  years old, it is still heavily cited. For example, Katz (1987) uses the
for Unrestricted Text," Second Conference on Applied Natural Lan-  method in order to estimate trigram probabilities in the IBM speech
guage Processing, Austin, TX.  recognizer. The Good-Turing  Method is helpful for trigrams that
Church, K.; Gale, W.; Hanks, P.; and Hindle, D. 1989 "Parsing, Word  have not been seen very often in the training corpus.
Associations  and Typical Predicate-Argument Relations," Interna-  5.  The last unclassified line. ... save shoppers anywhere from $50...
tional Workshop on Parsing Technologies, CMU.  raises interesting problems. Syntactic "chunking" shows that, in spite
Fano, R. 1961 Transmission  of Information:  A Statistical Theory of  of its co-occurrence of from with save, this line does not belong here.
Communications.  MIT Press, Cambridge, MA.  An intriguing  exercise, given the lookup table we are trying to
Firth, J. 1957 "A Synopsis of Linguistic Theory 1930-1955,"  in Studies  construct, is how to guard against false inferences such as that since
in Linguistic Analysis, Philological Society, Oxford; reprinted in Palmer,  shoppers is tagged PERSON,  $50 to $500 must here count as either
F. (ed.) 1968 Selected Papers of J. R. Firth, Longman, Harlow.  BAD or a LOCATION. Accidental coincidences of this kind do not
Francis, W. and Ku~era, H. 1982 Frequency Analysis of English Usage.  have a significant effect on the measure, however, although they do
Houghton Mifflin Company, Boston, MA.  serve as a reminder of the probabilistic nature of the findings.
Good, I. J. 1953 The Population Frequencies of Species and the Estima-  6.  The word time itself also occurs significantly in the table, but on closer
tion of Population Parameters. Biometrika, Vol. 40, 237-264.  examination it is clear that this use of time (e.g. to save time) counts
Hanks,  P.  1987 "Definitions  and Explanations," in J. Sinclair (ed.),  as something like a commodity or resource, not as part of a time
Looking Up: An Account of the COBUILD Project in Lexical Comput-  adjunct. Such are the pitfalls of lexicography (obvious when they are
ing. Collins, London and Glasgow.
pointed out).
Computational Linguistics Volume 16, Number 1, March 1990  29
