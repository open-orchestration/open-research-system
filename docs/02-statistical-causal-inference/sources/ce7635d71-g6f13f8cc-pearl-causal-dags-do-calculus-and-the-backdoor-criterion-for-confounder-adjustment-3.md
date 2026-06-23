[ Andrew Heiss ](https://www.andrewheiss.com/)
  * [ About](https://www.andrewheiss.com/)
  * [ CV](https://www.andrewheiss.com/cv/)
  * [ Blog](https://www.andrewheiss.com/blog/)
  * [ Research](https://www.andrewheiss.com/research/)
  * [ Teaching](https://www.andrewheiss.com/teaching/)
  * [ Talks](https://www.andrewheiss.com/talks/)
  * [ Now](https://www.andrewheiss.com/now/)
  * [ Uses](https://www.andrewheiss.com/uses/)
  * [ AI](https://www.andrewheiss.com/ai/)


  * [ ](https://www.andrewheiss.com/atom.xml)
  *   * [ ](https://bsky.app/profile/andrew.heiss.phd)
  * [ ](https://fediscience.org/users/andrew/)
  * [ ](https://github.com/andrewheiss)
  * [ ](https://www.youtube.com/andrewheiss)
  * [ ](https://www.heissatopia.com/)
  * [ ](https://www.linkedin.com/in/andrewheiss)


# Do-calculus adventures! Exploring the three rules of do-calculus in plain language and deriving the backdoor adjustment formula by hand
Code
Use R to explore the three rules of _do_ -calculus in plain language and derive the backdoor adjustment formula by hand 
[r](https://www.andrewheiss.com/rss.html#category=r)
[tidyverse](https://www.andrewheiss.com/rss.html#category=tidyverse)
[DAGs](https://www.andrewheiss.com/rss.html#category=DAGs)
[causal inference](https://www.andrewheiss.com/rss.html#category=causal%20inference)
[do calculus](https://www.andrewheiss.com/rss.html#category=do%20calculus)
Author
[Andrew Heiss](https://www.andrewheiss.com/) [ ![](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/)](https://orcid.org/0000-0002-3948-3914)
Published
Tuesday, September 7, 2021
Doi
[10.59350/fqkhz-kq526](https://doi.org/10.59350/fqkhz-kq526)
## Contents
  * [Exploring the rules of _do_ -calculus](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#exploring-the-rules-of-do-calculus)
    * [Rule 1: Ignoring observations](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#rule-1-ignoring-observations)
    * [Rule 2: Treating interventions as observations](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#rule-2-treating-interventions-as-observations)
    * [Rule 3: Ignoring interventions](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#rule-3-ignoring-interventions)
    * [Summary](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#summary)
  * [Deriving the backdoor adjustment formula from _do_ -calculus rules](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#deriving-the-backdoor-adjustment-formula-from-do-calculus-rules)
    * [Marginalizing across zzz](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#marginalizing-across-z)
    * [Applying Rule 2](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#applying-rule-2)
    * [Applying Rule 3](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#applying-rule-3)
    * [Final equation](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#final-equation)
  * [References](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#references)


I’ve been teaching [a course on program evaluation](https://evalf21.classes.andrewheiss.com/) since Fall 2019, and while part of the class is focused on logic models and the more managerial aspects of evaluation, the bulk of the class is focused on causal inference. Ever since reading [Judea Pearl’s _The Book of Why_](http://bayes.cs.ucla.edu/WHY/) in 2019, I’ve thrown myself into the world of DAGs, econometrics, and general causal inference, and I’ve been both teaching it and using it in research ever since. I’ve even [published a book chapter on it](https://www.andrewheiss.com/research/chapters/heiss-causal-inference-2021/). Fun stuff.
This post assumes you have a general knowledge of DAGs and backdoor confounding. Read [this post](https://www.andrewheiss.com/blog/2020/02/25/closing-backdoors-dags/) or [this chapter](https://www.andrewheiss.com/research/chapters/heiss-causal-inference-2021/) if you haven’t heard about those things yet.
DAGs are a powerful tool for causal inference because they let you map out all your assumptions of the data generating process for some treatment and some outcome. Importantly, these causal graphs help you determine what statistical approaches you need to use to isolate or identify the causal arrow between treatment and outcome. One of the more common (and intuitive) methods for idenfifying causal effects with DAGs is to close back doors, or adjust for nodes in a DAG that open up unwanted causal associtions between treatment and control. By properly closing backdoors, you can estimate a causal quantity using observational data. There’s even a special formula called the backdoor adjustment formula that takes an equation with a do⁡(⋅)\operatorname{do}(\cdot)do(⋅) operator (a [special mathematical function](https://stats.stackexchange.com/questions/211008/dox-operator-meaning) representing a direct experimental intervention in a graph) and allows you to estimate the effect with _do_ -free quantities:
P(y∣do⁡(x))=∑zP(y∣x,z)×P(z) P(y \mid \operatorname{do}(x)) = \sum_z P(y \mid x, z) \times P(z) P(y∣do(x))=z∑​P(y∣x,z)×P(z)
When I teach this stuff, I show that formula on a slide, tell students they don’t need to worry about it too much, and then show how actually do it using regression, inverse probability weighting, and matching ([with this guide](https://evalf21.classes.andrewheiss.com/example/matching-ipw/)). For my MPA and MPP students, the math isn’t as important as the actual application of these principles, so that’s what I focus on.
However—confession time—that math is also a bit of a magic black box for me too. I’ve read it in books and assume that it’s correct, but I never really fully understood why.
Compounding my confusion is the fact that the foundation of Judea Pearl-style DAG-based causal inference is the idea of _do_ -calculus ([Pearl 2012](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#ref-Pearl:2012)): a set of three mathematical rules that can be applied to a causal graph to identify causal relationships. Part of my confusion stems from the fact that most textbooks and courses (including mine!) explain that you can identify causal relationships in DAGs using backdoor adjustment, frontdoor adjustment, or the fancy application of _do_ -calculus rules. When framed like this, it seems like backdoor and frontdoor adjustment are separate things from _do_ -calculus, and that _do_ -calculus is something you do when backdoor and frontdoor adjustments don’t work.
But that’s not the case! In 2020, [I asked Twitter](https://twitter.com/@andrewheiss) if backdoor and frontdoor adjustment were connected to _do_ -calculus, and surprisingly [Judea Pearl himself answered](https://twitter.com/yudapearl/status/1252462516468240390) that they are!
![](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/pearl-tweet.png)
They’re both specific consequences of the application of the rules of _do_ -calculus—they just have special names because they’re easy to see in a graph.
But how? How do people apply these strange rules of _do_ -calculus to derive these magical backdoor and frontdoor adjustment formulas? The question has haunted me since April 2020.
But in the past couple days, I’ve stumbled across a couple excellent resources ([this course](https://www.bradyneal.com/causal-inference-course) and [these videos](https://www.youtube.com/playlist?list=PLoazKTcS0Rzb6bb9L508cyJ1z-U9iWkA0) + [this blog post](https://stephenmalina.com/post/2020-03-09-front-door-do-calc-derivation/)) that explained _do_ -calculus really well, so I figured I’d finally tackle this question and figure out how exactly _do_ -calculus is used to derive the backdoor adjustment formula. I won’t show the derivation of the frontdoor formula—smarter people than me have done that ([here](https://stephenmalina.com/post/2020-03-09-front-door-do-calc-derivation/) and [Section 6.2.1 here](https://www.bradyneal.com/Introduction_to_Causal_Inference-Dec17_2020-Neal.pdf), for instance), but I can do the backdoor one now!
First, I’ll explain and illustrate how each of the three rules of _do_ -calculus as plain-language-y as possible, and then I’ll apply those rules to show how the backdoor adjustment formula is created.
I use the **ggdag** and **dagitty** packages in R for all this, so you can follow along too. Here we go!

```
library[](https://rdrr.io/r/base/library.html)(tidyverse[](https://tidyverse.tidyverse.org/))  # For ggplot2 and friends
library[](https://rdrr.io/r/base/library.html)(patchwork[](https://patchwork.data-imaginist.com/))  # For combining plots
library[](https://rdrr.io/r/base/library.html)(ggdag[](https://github.com/r-causal/ggdag))      # For making DAGs with ggplot
library[](https://rdrr.io/r/base/library.html)(dagitty[](https://www.dagitty.net/))    # For dealing with DAG math
library[](https://rdrr.io/r/base/library.html)(latex2exp[](https://www.stefanom.io/latex2exp/))  # Easily convert LaTeX into arcane plotmath expressions
library[](https://rdrr.io/r/base/library.html)(ggtext[](https://wilkelab.org/ggtext/))     # Use markdown in ggplot labels

# Create a cleaner serifed theme to use throughout
theme_do_calc <- function() {
  theme_dag[](https://r-causal.github.io/ggdag/reference/theme_dag_blank.html)(base_family = "Linux Libertine O") +
    theme[](https://ggplot2.tidyverse.org/reference/theme.html)(plot.title = element_text[](https://ggplot2.tidyverse.org/reference/element.html)(size = rel[](https://ggplot2.tidyverse.org/reference/element.html)(1.5)),
        plot.subtitle = element_markdown[](https://wilkelab.org/ggtext/reference/element_markdown.html)())
}

# Make all geom_dag_text() layers use these settings automatically
update_geom_defaults[](https://ggplot2.tidyverse.org/reference/update_defaults.html)(ggdag:::GeomDagText, list[](https://rdrr.io/r/base/list.html)(family = "Linux Libertine O", 
                                               fontface = "bold",
                                               color = "black"))
```

## Exploring the rules of _do_ -calculus[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#exploring-the-rules-of-do-calculus)
The three rules of _do_ -calculus have always been confusing to me since they are typically written as pure math equations and not in plain understandable language. For instance, [here’s Judea Pearl’s canonical primer on _do_ -calculus](https://ftp.cs.ucla.edu/pub/stat_ser/r402.pdf)—a short PDF with lots of math and proofs ([Pearl 2012](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#ref-Pearl:2012)). In basically everything I’ve read about _do_ -calculus, there’s inevitably a listing of these three very mathy rules, written for people much smarter than me:
![](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/do-calculus-math.png)
From left to right: Lattimore and Rohde ([2019](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#ref-LattimoreRohde:2019)), [The Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/entries/causal-models/do-calculus.html), Pearl ([2012](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#ref-Pearl:2012)), Neal ([2020](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#ref-Neal:2020))
However, beneath this scary math, each rule has specific intuition and purpose behind it—I just didn’t understand the plain-language reasons for each rule until reading [this really neat blog post](https://stephenmalina.com/post/2020-03-09-front-door-do-calc-derivation/). Here’s what each rule actually does:
  * **Rule 1** : Decide if we can ignore an observation
  * **Rule 2** : Decide if we can treat an intervention as an observation
  * **Rule 3** : Decide if we can ignore an intervention


Whoa! That’s exceptionally logical. Each rule is designed to help simplify and reduce nodes in a DAG by either ignoring them (Rules 1 and 3) or making it so interventions like do⁡(⋅)\operatorname{do}(\cdot)do(⋅) can be treated like observations instead (Rule 2).
Let’s explore each of these rules in detail. In all these situations, we’re assuming that there’s a DAG with 4 nodes: W, X, Y, and Z. Y is always the outcome; X is always the main treatment. In each rule, our goal is to get rid of Z by applying the rule. When talking about interventions in a graph, there’s a special notation with overlines and underlines:
  * An overline like GX‾G_{\overline{X}}GX​ means that you delete all the arrows _going into_ X
  * An underline like GX‾G_{\underline{X}}GX​​ means that you delete all the arrows _coming out of_ X


I imagine this line like a wall:
  * If the wall is on top of X like X‾\overline{X}X, you can’t draw any arrows going into it, so you delete anything going in
  * If the wall is on the bottom of X like X‾\underline{X}X​, you can’t draw any arrows going out of it, so you delete anything going out


### Rule 1: Ignoring observations[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#rule-1-ignoring-observations)
According to Rule 1, we can ignore any observational node if it doesn’t influence the outcome through any path, or if it is d-separated from the outcome. Here’s the formal definition:
P(y∣z,do⁡(x),w)=P(y∣do⁡(x),w) if (Y⊥Z∣W,X)GX‾ P(y \mid z, \operatorname{do}(x), w) = P(y \mid \operatorname{do}(x), w) \qquad \text{ if } (Y \perp Z \mid W, X)_{G_{\overline{X}}} P(y∣z,do(x),w)=P(y∣do(x),w) if (Y⊥Z∣W,X)GX​​
There are a lot of moving parts here, but remember, the focus in this equation is zzz. Our goal here is to remove or ignore zzz. Notice how zzz exists on the left-hand side of the equation and how it is gone on the right-hand side. As long as we meet the cryptic conditions of (Y⊥Z∣W,X)GX‾(Y \perp Z \mid W, X)_{G_{\overline{X}}}(Y⊥Z∣W,X)GX​​, we can get rid of it. But what the heck does that even mean?
Here, GX‾G_{\overline{X}}GX​ means “the original causal graph with all arrows into X removed”, while the Y⊥Z∣W,XY \perp Z \mid W, XY⊥Z∣W,X part means “Y is independent of Z, given W and X” in the new modified graph. If the Y and Z nodes are d-separated from each other after we account for both W and X, we can get rid of Z and ignore it.
Let’s look at this graphically to help make better sense of this. We’ll use the `dagify()[](https://r-causal.github.io/ggdag/reference/dagify.html)` function from **ggdag** to build a couple DAGs: one complete one (GGG) and one with all the arrows into X deleted (GX‾G_{\overline{X}}GX​). X causes both X and Y, while W confounds X, Y, and Z.

```
rule1_g <- dagify[](https://r-causal.github.io/ggdag/reference/dagify.html)(
  Y ~ X + W,
  X ~ W,
  Z ~ X + W,
  coords = list[](https://rdrr.io/r/base/list.html)(x = c[](https://rdrr.io/r/base/c.html)(X = 1, Y = 2, Z = 1.25, W = 1.5),
                y = c[](https://rdrr.io/r/base/c.html)(X = 1, Y = 1, Z = 2, W = 2))
)

rule1_g_x_over <- dagify[](https://r-causal.github.io/ggdag/reference/dagify.html)(
  Y ~ X + W,
  Z ~ X + W,
  coords = list[](https://rdrr.io/r/base/list.html)(x = c[](https://rdrr.io/r/base/c.html)(X = 1, Y = 2, Z = 1.25, W = 1.5),
                y = c[](https://rdrr.io/r/base/c.html)(X = 1, Y = 1, Z = 2, W = 2))
) 
```


```
plot_rule1_g <- ggplot[](https://ggplot2.tidyverse.org/reference/ggplot.html)(rule1_g, aes[](https://ggplot2.tidyverse.org/reference/aes.html)(x = x, y = y, 
                                    xend = xend, yend = yend)) +
  geom_dag_edges[](https://r-causal.github.io/ggdag/reference/geom_dag_edges.html)() +
  geom_dag_point[](https://r-causal.github.io/ggdag/reference/node_point.html)(color = "grey80", size = 10) +
  geom_dag_text[](https://r-causal.github.io/ggdag/reference/geom_dag_text.html)() +
  labs[](https://ggplot2.tidyverse.org/reference/labs.html)(title = TeX[](https://www.stefanom.io/latex2exp/reference/TeX.html)("$G$"),
       subtitle = "Original DAG") +
  theme_do_calc()

plot_rule1_g_x_over <- ggplot[](https://ggplot2.tidyverse.org/reference/ggplot.html)(rule1_g_x_over, aes[](https://ggplot2.tidyverse.org/reference/aes.html)(x = x, y = y, 
                                                  xend = xend, yend = yend)) +
  geom_dag_edges[](https://r-causal.github.io/ggdag/reference/geom_dag_edges.html)() +
  geom_dag_point[](https://r-causal.github.io/ggdag/reference/node_point.html)(color = "grey80", size = 10) +
  geom_dag_text[](https://r-causal.github.io/ggdag/reference/geom_dag_text.html)() +
  labs[](https://ggplot2.tidyverse.org/reference/labs.html)(title = TeX[](https://www.stefanom.io/latex2exp/reference/TeX.html)("$G_{\\bar{X}}$"),
       subtitle = "DAG with arrows *into* X deleted") +
  theme_do_calc()

plot_rule1_g | plot_rule1_g_x_over
```

![](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/index_files/figure-html/plot-rule1-1.png)
If we want to calculate the causal effect of X on Y, do we need to worry about Z here, or can we ignore it? Let’s apply Rule 1. If we look at the modified GX‾G_{\overline{X}}GX​, Y and Z are completely d-separated if we account for both W and X—there’s no direct arrow between them, and there’s no active path connecting them through W or X, since we’re accounting for (or condition on) those nodes. Y and Z are thus d-separated and Y⊥Z∣W,XY \perp Z \mid W, XY⊥Z∣W,X. We can confirm this with the `impliedConditionalIndependencies()[](https://rdrr.io/pkg/dagitty/man/impliedConditionalIndependencies.html)` function from the **dagitty** package:

```
impliedConditionalIndependencies[](https://rdrr.io/pkg/dagitty/man/impliedConditionalIndependencies.html)(rule1_g_x_over)
## W _||_ X
## Y _||_ Z | W, X
```

And there it is! The second independency there is Y⊥Z∣W,XY \perp Z \mid W, XY⊥Z∣W,X. That means that we can apply Rule 1 and ignore Z, meaning that
P(y∣z,do⁡(x),w)=P(y∣do⁡(x),w) P(y \mid z, \operatorname{do}(x), w) = P(y \mid \operatorname{do}(x), w) P(y∣z,do(x),w)=P(y∣do(x),w)
This makes sense but is a little too complicated for me, since we’re working with four different nodes. We can simplify this and pretend that do⁡(x)\operatorname{do}(x)do(x) is nothing and that X doesn’t exist. That leaves us with just three nodes—W, Y, and Z—and this DAG:

```
rule1_g_simple <- dagify[](https://r-causal.github.io/ggdag/reference/dagify.html)(
  Y ~ W,
  Z ~ W,
  coords = list[](https://rdrr.io/r/base/list.html)(x = c[](https://rdrr.io/r/base/c.html)(Y = 2, Z = 1, W = 1.5),
                y = c[](https://rdrr.io/r/base/c.html)(Y = 1, Z = 1, W = 2))
)

plot_rule1_g_simple <- ggplot[](https://ggplot2.tidyverse.org/reference/ggplot.html)(rule1_g_simple, aes[](https://ggplot2.tidyverse.org/reference/aes.html)(x = x, y = y, 
                                                  xend = xend, yend = yend)) +
  geom_dag_edges[](https://r-causal.github.io/ggdag/reference/geom_dag_edges.html)() +
  geom_dag_point[](https://r-causal.github.io/ggdag/reference/node_point.html)(color = "grey80", size = 10) +
  geom_dag_text[](https://r-causal.github.io/ggdag/reference/geom_dag_text.html)() +
  labs[](https://ggplot2.tidyverse.org/reference/labs.html)(title = TeX[](https://www.stefanom.io/latex2exp/reference/TeX.html)("$G$"),
       subtitle = "Simplified DAG without X") +
  theme_do_calc()
plot_rule1_g_simple
```

![](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/index_files/figure-html/plot-rule1-simple-1.png)
The simplified X-free version of Rule 1 looks like this:
P(y∣z,w)=P(y∣w) if (Y⊥Z∣W)G P(y \mid z, w) = P(y \mid w) \qquad \text{ if } (Y \perp Z \mid W)_{G} P(y∣z,w)=P(y∣w) if (Y⊥Z∣W)G​
In other words, we can ignore Z and remove it from the P(y∣z,w)P(y \mid z, w)P(y∣z,w) equation if Y and Z are d-separated (or independent of each other) after accounting for W. Once we account for W, there’s no possible connection between Y and Z, so they really are d-separated. We can again confirm this with code:

```
impliedConditionalIndependencies[](https://rdrr.io/pkg/dagitty/man/impliedConditionalIndependencies.html)(rule1_g_simple)
## Y _||_ Z | W
```

There we go. Because Y⊥Z∣WY \perp Z \mid WY⊥Z∣W we can safely ignore Z.
### Rule 2: Treating interventions as observations[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#rule-2-treating-interventions-as-observations)
Rule 1 is neat, but it has nothing to do with causal interventions or the do⁡(⋅)\operatorname{do}(\cdot)do(⋅) operator. It feels more like a housekeeping rule—it’s a way of simplifying and removing unnecessary nodes that don’t have to do with the main treatment → outcome relationship.
With Rule 2, we start messing with interventions. In an experiment like a randomized controlled trial, a researcher has the ability to assign treatment and either do⁡(x)\operatorname{do}(x)do(x) or not do⁡(x)\operatorname{do}(x)do(x). With observational data, though, it’s not possible to do⁡(x)\operatorname{do}(x)do(x) directly. It would be fantastic if we could take an intervention like do⁡(x)\operatorname{do}(x)do(x) and treat it like regular non-interventional observational data. Rule 2 lets us do this.
According to Rule 2, interventions (or do(x)do(x)do(x)) can be treated as observations (or xxx) when the causal effect of a variable on the outcome (X→YX \rightarrow YX→Y) only influences the outcome through directed paths. The official math for this is this complicated thing:
P(y∣do⁡(z),do⁡(x),w)=P(y∣z,do⁡(x),w) if (Y⊥Z∣W,X)GX‾,Z‾ P(y \mid \operatorname{do}(z), \operatorname{do}(x), w) = P(y \mid z, \operatorname{do}(x), w) \qquad \text{ if } (Y \perp Z \mid W, X)_{G_{\overline{X}, \underline{Z}}} P(y∣do(z),do(x),w)=P(y∣z,do(x),w) if (Y⊥Z∣W,X)GX,Z​​​
For me, this is super confusing, since there are two different do⁡(⋅)\operatorname{do}(\cdot)do(⋅) operators here and when I think of causal graphs, I think of single interventions. Like we did with Rule 1, we can simplify this and pretend that there’s no intervention do⁡(x)\operatorname{do}(x)do(x) (we’ll do the full rule in a minute, don’t worry). Again, this is legal because each of these rules are focused on messing with the Z variable: ignoring it or treating it as an observation. That leaves us with this slightly simpler (though still cryptic) equation:
P(y∣do⁡(z),w)=P(y∣z,w) if (Y⊥Z∣W)GZ‾ P(y \mid \operatorname{do}(z), w) = P(y \mid z, w) \qquad \text{ if } (Y \perp Z \mid W)_{G_{\underline{Z}}} P(y∣do(z),w)=P(y∣z,w) if (Y⊥Z∣W)GZ​​​
Notice how the left-hand side has the interventional do⁡(z)\operatorname{do}(z)do(z), while the right-hand side has the observed zzz. As long as we meet the condition (Y⊥Z∣W)GZ‾(Y \perp Z \mid W)_{G_{\underline{Z}}}(Y⊥Z∣W)GZ​​​, we can transform do⁡(z)\operatorname{do}(z)do(z) into zzz and work only with observational data. Once again, though, what does this (Y⊥Z∣W)GZ‾(Y \perp Z \mid W)_{G_{\underline{Z}}}(Y⊥Z∣W)GZ​​​ condition even mean?
Here, GZ‾G_{\underline{Z}}GZ​​ means “the original causal graph with all arrows out of Z removed”, while the Y⊥Z∣WY \perp Z \mid WY⊥Z∣W part means “Y is independent of Z, given W” in the new modified graph. Similar to Rule 1, if the Y and Z nodes are d-separated from each other after we account for W, we can legally treat do⁡(z)\operatorname{do}(z)do(z) like zzz.
As we did with Rule 1, we’ll build a couple basic DAGs: a complete one (GGG) and one with all the arrows _out of_ Z deleted (GZ‾G_{\underline{Z}}GZ​​).

```
rule2_g_simple <- dagify[](https://r-causal.github.io/ggdag/reference/dagify.html)(
  Y ~ Z + W,
  Z ~ W,
  coords = list[](https://rdrr.io/r/base/list.html)(x = c[](https://rdrr.io/r/base/c.html)(Y = 2, Z = 1, W = 1.5),
                y = c[](https://rdrr.io/r/base/c.html)(Y = 1, Z = 1, W = 2))
)

rule2_g_simple_z_under <- dagify[](https://r-causal.github.io/ggdag/reference/dagify.html)(
  Y ~ W,
  Z ~ W,
  coords = list[](https://rdrr.io/r/base/list.html)(x = c[](https://rdrr.io/r/base/c.html)(Y = 2, Z = 1, W = 1.5),
                y = c[](https://rdrr.io/r/base/c.html)(Y = 1, Z = 1, W = 2))
) 
```


```
plot_rule2_g_simple <- ggplot[](https://ggplot2.tidyverse.org/reference/ggplot.html)(rule2_g_simple, 
                              aes[](https://ggplot2.tidyverse.org/reference/aes.html)(x = x, y = y, 
                                  xend = xend, yend = yend)) +
  geom_dag_edges[](https://r-causal.github.io/ggdag/reference/geom_dag_edges.html)() +
  geom_dag_point[](https://r-causal.github.io/ggdag/reference/node_point.html)(color = "grey80", size = 10) +
  geom_dag_text[](https://r-causal.github.io/ggdag/reference/geom_dag_text.html)() +
  labs[](https://ggplot2.tidyverse.org/reference/labs.html)(title = TeX[](https://www.stefanom.io/latex2exp/reference/TeX.html)("$G$"),
       subtitle = "Original DAG") +
  theme_do_calc()

plot_rule2_g_simple_z_under <- ggplot[](https://ggplot2.tidyverse.org/reference/ggplot.html)(rule2_g_simple_z_under, 
                                      aes[](https://ggplot2.tidyverse.org/reference/aes.html)(x = x, y = y, 
                                          xend = xend, yend = yend)) +
  geom_dag_edges[](https://r-causal.github.io/ggdag/reference/geom_dag_edges.html)() +
  geom_dag_point[](https://r-causal.github.io/ggdag/reference/node_point.html)(color = "grey80", size = 10) +
  geom_dag_text[](https://r-causal.github.io/ggdag/reference/geom_dag_text.html)() +
  labs[](https://ggplot2.tidyverse.org/reference/labs.html)(title = TeX[](https://www.stefanom.io/latex2exp/reference/TeX.html)("$G_{\\underline{Z}}$"),
       subtitle = "DAG with arrows *out of* Z deleted") +
  theme_do_calc()

plot_rule2_g_simple | plot_rule2_g_simple_z_under
```

![](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/index_files/figure-html/plot-rule2-simple-1.png)
So, can we treat Z here like an observational node instead of a interventional do⁡(⋅)\operatorname{do}(\cdot)do(⋅) node? Let’s apply Rule 2. If we look at the modified GZ‾G_{\underline{Z}}GZ​​ graph, Z and Y are completely d-separated if we account for W—there’s no direct arrow between them, and there’s no active path connecting them through W since we’re conditioning on W. We can thus say that Y⊥Z∣WY \perp Z \mid WY⊥Z∣W. We can confirm this with code too:

```
impliedConditionalIndependencies[](https://rdrr.io/pkg/dagitty/man/impliedConditionalIndependencies.html)(rule2_g_simple_z_under)
## Y _||_ Z | W
```

Woohoo! Because Y⊥Z∣WY \perp Z \mid WY⊥Z∣W in that modified GZ‾G_{\underline{Z}}GZ​​ graph, we can legally convert the interventional do⁡(z)\operatorname{do}(z)do(z) to just a regular old observational zzz:
P(y∣do⁡(z),w)=P(y∣z,w) P(y \mid \operatorname{do}(z), w) = P(y \mid z, w) P(y∣do(z),w)=P(y∣z,w)
So far we’ve applied Rule 2 to a simplified DAG with three nodes, but what does it look like if we’re using the full four-node graph that is used in the formal definition of Rule 2?
P(y∣do⁡(z),do⁡(x),w)=P(y∣z,do⁡(x),w) if (Y⊥Z∣W,X)GX‾,Z‾ P(y \mid \operatorname{do}(z), \operatorname{do}(x), w) = P(y \mid z, \operatorname{do}(x), w) \qquad \text{ if } (Y \perp Z \mid W, X)_{G_{\overline{X}, \underline{Z}}} P(y∣do(z),do(x),w)=P(y∣z,do(x),w) if (Y⊥Z∣W,X)GX,Z​​​
Here’s one graphical representation of a graph with the four nodes W, X, Y, and Z (but it’s definitely not the only possible graph! These _do_ -calculus rules don’t assume any specific relationships between the nodes). Here, Y is caused by both X and Z, and we’ll pretend that they’re both interventions (so do⁡(x)\operatorname{do}(x)do(x) and do⁡(z)\operatorname{do}(z)do(z)). X is causally linked to Z, and W confounds all three: X, Y, and Z. Graph GGG shows the complete DAG; Graph GX‾,Z‾G_{\overline{X}, \underline{Z}}GX,Z​​ shows a modified DAG with all arrows _into_ X deleted (X‾\overline{X}X) and all arrows _out of_ Z deleted (Z‾\underline{Z}Z​).

```
rule2_g <- dagify[](https://r-causal.github.io/ggdag/reference/dagify.html)(
  Y ~ X + W + Z,
  X ~ W,
  Z ~ X + W,
  coords = list[](https://rdrr.io/r/base/list.html)(x = c[](https://rdrr.io/r/base/c.html)(X = 1, Y = 2, Z = 1.25, W = 1.5),
                y = c[](https://rdrr.io/r/base/c.html)(X = 1, Y = 1, Z = 2, W = 2))
)

rule2_g_modified <- dagify[](https://r-causal.github.io/ggdag/reference/dagify.html)(
  Y ~ X + W,
  Z ~ X + W,
  coords = list[](https://rdrr.io/r/base/list.html)(x = c[](https://rdrr.io/r/base/c.html)(X = 1, Y = 2, Z = 1.25, W = 1.5),
                y = c[](https://rdrr.io/r/base/c.html)(X = 1, Y = 1, Z = 2, W = 2))
) 
```


```
plot_rule2_g <- ggplot[](https://ggplot2.tidyverse.org/reference/ggplot.html)(rule2_g, aes[](https://ggplot2.tidyverse.org/reference/aes.html)(x = x, y = y, 
                                    xend = xend, yend = yend)) +
  geom_dag_edges[](https://r-causal.github.io/ggdag/reference/geom_dag_edges.html)() +
  geom_dag_point[](https://r-causal.github.io/ggdag/reference/node_point.html)(color = "grey80", size = 10) +
  geom_dag_text[](https://r-causal.github.io/ggdag/reference/geom_dag_text.html)() +
  labs[](https://ggplot2.tidyverse.org/reference/labs.html)(title = TeX[](https://www.stefanom.io/latex2exp/reference/TeX.html)("$G$"),
       subtitle = "Original DAG") +
  theme_do_calc()

plot_rule2_modified <- ggplot[](https://ggplot2.tidyverse.org/reference/ggplot.html)(rule2_g_modified, 
                              aes[](https://ggplot2.tidyverse.org/reference/aes.html)(x = x, y = y, 
                                  xend = xend, yend = yend)) +
  geom_dag_edges[](https://r-causal.github.io/ggdag/reference/geom_dag_edges.html)() +
  geom_dag_point[](https://r-causal.github.io/ggdag/reference/node_point.html)(color = "grey80", size = 10) +
  geom_dag_text[](https://r-causal.github.io/ggdag/reference/geom_dag_text.html)() +
  labs[](https://ggplot2.tidyverse.org/reference/labs.html)(title = TeX[](https://www.stefanom.io/latex2exp/reference/TeX.html)("$G_{\\bar{X}, \\underline{Z}}$"),
       subtitle = "DAG with arrows *into* X and *out of* Z deleted") +
  theme_do_calc()

plot_rule2_g | plot_rule2_modified
```

![](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/index_files/figure-html/plot-rule2-1.png)
Okay. Our goal here is to check if we can treat do⁡(z)\operatorname{do}(z)do(z) like a regular observational zzz. We can legally do this if Y and Z are d-separated in that modified graph, after accounting for both W and X, or Y⊥Z∣W,XY \perp Z \mid W, XY⊥Z∣W,X. And that is indeed the case! There’s no direct arrow connecting Y and Z in the modified graph, and once we condition on (or account for) W and X, no pathways between Y and Z are active—Y and Z are independent and d-separated. We can confirm this with code:

```
impliedConditionalIndependencies[](https://rdrr.io/pkg/dagitty/man/impliedConditionalIndependencies.html)(rule2_g_modified)
## W _||_ X
## Y _||_ Z | W, X
```

The second independency there is that Y⊥Z∣W,XY \perp Z \mid W, XY⊥Z∣W,X, which is exactly what we want to see. We can thus legally transform do⁡(z)\operatorname{do}(z)do(z) to zzz:
P(y∣do⁡(z),do⁡(x),w)=P(y∣z,do⁡(x),w) P(y \mid \operatorname{do}(z), \operatorname{do}(x), w) = P(y \mid z, \operatorname{do}(x), w) P(y∣do(z),do(x),w)=P(y∣z,do(x),w)
What’s really neat is that Rule 2 is a generalized version of the backdoor criterion. More on that below after we explore Rule 3.
### Rule 3: Ignoring interventions[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#rule-3-ignoring-interventions)
Rule 3 is the trickiest of the three, conceptually. It tells us when we can completely remove a do⁡(⋅)\operatorname{do}(\cdot)do(⋅) expression rather than converting it to an observed quantity. Here it is in all its mathy glory:
P(y∣do⁡(z),do⁡(x),w)=P(y∣do⁡(x),w) if (Y⊥Z∣W,X)GX‾,Z(W)‾ P(y \mid \operatorname{do}(z), \operatorname{do}(x), w) = P(y \mid \operatorname{do}(x), w) \qquad \text{ if } (Y \perp Z \mid W, X)_{G_{\overline{X}, \overline{Z(W)}}} P(y∣do(z),do(x),w)=P(y∣do(x),w) if (Y⊥Z∣W,X)GX,Z(W)​​​
In simpler language, this means that we can ignore an intervention (or a do⁡(⋅)\operatorname{do}(\cdot)do(⋅) expression) if it doesn’t influence the outcome through any uncontrolled path—we can remove do⁡(z)\operatorname{do}(z)do(z) if there is no causal association (or no unblocked causal paths) flowing from Z to Y.
This rule is tricky, though, because it depends on where the Z node (i.e. the intervention we want to get rid of) appears in the graph. Note the notation for the modified graph here. With the other rules, we used things like GX‾G_{\overline{X}}GX​ or GZ‾G_{\underline{Z}}GZ​​ to remove arrows into and out of specific nodes in the modified graph. Here, though, we have the strange GZ(W)‾G_{\overline{Z(W)}}GZ(W)​​. This Z(W) is weird! It means “any Z node that isn’t an ancestor of W”. We thus only delete arrows going into a Z node in the modified graph if that Z node doesn’t precede W.
Here’s one version of what that could look like graphically:

```
rule3_g <- dagify[](https://r-causal.github.io/ggdag/reference/dagify.html)(
  Y ~ X + W,
  W ~ Z,
  Z ~ X,
  coords = list[](https://rdrr.io/r/base/list.html)(x = c[](https://rdrr.io/r/base/c.html)(X = 1, Y = 2, Z = 1.25, W = 1.5),
                y = c[](https://rdrr.io/r/base/c.html)(X = 1, Y = 1, Z = 2, W = 1.75))
)
```


```
plot_rule3_g <- ggplot[](https://ggplot2.tidyverse.org/reference/ggplot.html)(rule3_g, 
                       aes[](https://ggplot2.tidyverse.org/reference/aes.html)(x = x, y = y, 
                           xend = xend, yend = yend)) +
  geom_dag_edges[](https://r-causal.github.io/ggdag/reference/geom_dag_edges.html)() +
  geom_dag_point[](https://r-causal.github.io/ggdag/reference/node_point.html)(color = "grey80", size = 10) +
  geom_dag_text[](https://r-causal.github.io/ggdag/reference/geom_dag_text.html)() +
  labs[](https://ggplot2.tidyverse.org/reference/labs.html)(title = TeX[](https://www.stefanom.io/latex2exp/reference/TeX.html)("$G$"),
       subtitle = "Original DAG") +
  theme_do_calc()

plot_rule3_g_modified <- ggplot[](https://ggplot2.tidyverse.org/reference/ggplot.html)(rule3_g, 
                                aes[](https://ggplot2.tidyverse.org/reference/aes.html)(x = x, y = y, 
                                    xend = xend, yend = yend)) +
  geom_dag_edges[](https://r-causal.github.io/ggdag/reference/geom_dag_edges.html)() +
  geom_dag_point[](https://r-causal.github.io/ggdag/reference/node_point.html)(color = "grey80", size = 10) +
  geom_dag_text[](https://r-causal.github.io/ggdag/reference/geom_dag_text.html)() +
  labs[](https://ggplot2.tidyverse.org/reference/labs.html)(title = TeX[](https://www.stefanom.io/latex2exp/reference/TeX.html)("$G_{\\bar{X}, \\bar{Z(W)}}$"),
       subtitle = "DAG with arrows *into* Z deleted as long as Z isn't an<br>ancestor of W + all arrows *into* X deleted") +
  theme_do_calc()

plot_rule3_g | plot_rule3_g_modified
```

![](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/index_files/figure-html/plot-rule3-1.png)
Notice how these two graphs are identical. Because we only delete arrows going into Z if Z is not an ancestor of W, in this case G=GX‾,Z(W)‾G = G_{\overline{X}, \overline{Z(W)}}G=GX,Z(W)​​.
Remember that our original goal is to get rid of do⁡(z)\operatorname{do}(z)do(z), which we can legally do if Y and Z are d-separated and independent in our modified graph, or if Y⊥Z∣W,XY \perp Z \mid W, XY⊥Z∣W,X. That is once again indeed the case here: there’s no direct arrow between Y and Z, and if we condition on W and X, there’s no way to pass association between Y and Z, meaning that Y and Z are d-separated. Let’s confirm it with code:

```
impliedConditionalIndependencies[](https://rdrr.io/pkg/dagitty/man/impliedConditionalIndependencies.html)(rule3_g)
## W _||_ X | Z
## Y _||_ Z | W, X
```

That second independency is our Y⊥Z∣W,XY \perp Z \mid W, XY⊥Z∣W,X, so we can safely eliminate do⁡(z)\operatorname{do}(z)do(z) from the equation. We can ignore it because it doesn’t influence the outcome YYY through any possible path. Goodbye do⁡(z)\operatorname{do}(z)do(z)!:
P(y∣do⁡(z),do⁡(x),w)=P(y∣do⁡(x),w) P(y \mid \operatorname{do}(z), \operatorname{do}(x), w) = P(y \mid \operatorname{do}(x), w) P(y∣do(z),do(x),w)=P(y∣do(x),w)
In this case, the alternative graph GX‾,Z(W)‾G_{\overline{X}, \overline{Z(W)}}GX,Z(W)​​ was the same as the original graph because of the location of Z—Z was an ancestor of W, so we didn’t delete any arrows. If Z is _not_ an ancestor, though, we get to actually modify the graph. For instance, consider this DAG:

```
rule3_g_alt <- dagify[](https://r-causal.github.io/ggdag/reference/dagify.html)(
  Y ~ X + W,
  Z ~ W,
  X ~ Z,
  coords = list[](https://rdrr.io/r/base/list.html)(x = c[](https://rdrr.io/r/base/c.html)(X = 1, Y = 2, Z = 1.25, W = 1.5),
                y = c[](https://rdrr.io/r/base/c.html)(X = 1, Y = 1, Z = 2, W = 1.75))
)

rule3_g_alt_modified <- dagify[](https://r-causal.github.io/ggdag/reference/dagify.html)(
  Y ~ X + W,
  Z ~ 0,
  X ~ 0,
  coords = list[](https://rdrr.io/r/base/list.html)(x = c[](https://rdrr.io/r/base/c.html)(X = 1, Y = 2, Z = 1.25, W = 1.5),
                y = c[](https://rdrr.io/r/base/c.html)(X = 1, Y = 1, Z = 2, W = 1.75))
) 
```


```
plot_rule3_g_alt <- ggplot[](https://ggplot2.tidyverse.org/reference/ggplot.html)(rule3_g_alt, 
                           aes[](https://ggplot2.tidyverse.org/reference/aes.html)(x = x, y = y, 
                               xend = xend, yend = yend)) +
  geom_dag_edges[](https://r-causal.github.io/ggdag/reference/geom_dag_edges.html)() +
  geom_dag_point[](https://r-causal.github.io/ggdag/reference/node_point.html)(color = "grey80", size = 10) +
  geom_dag_text[](https://r-causal.github.io/ggdag/reference/geom_dag_text.html)() +
  labs[](https://ggplot2.tidyverse.org/reference/labs.html)(title = TeX[](https://www.stefanom.io/latex2exp/reference/TeX.html)("$G$"),
       subtitle = "Original DAG") +
  theme_do_calc()

plot_rule3_g_alt_modified <- ggplot[](https://ggplot2.tidyverse.org/reference/ggplot.html)(rule3_g_alt_modified, 
                                    aes[](https://ggplot2.tidyverse.org/reference/aes.html)(x = x, y = y, 
                                        xend = xend, yend = yend)) +
  geom_dag_edges[](https://r-causal.github.io/ggdag/reference/geom_dag_edges.html)() +
  geom_dag_point[](https://r-causal.github.io/ggdag/reference/node_point.html)(color = "grey80", size = 10) +
  geom_dag_text[](https://r-causal.github.io/ggdag/reference/geom_dag_text.html)() +
  labs[](https://ggplot2.tidyverse.org/reference/labs.html)(title = TeX[](https://www.stefanom.io/latex2exp/reference/TeX.html)("$G_{\\bar{X}, \\bar{Z(W)}}$"),
       subtitle = "DAG with arrows *into* Z deleted as long as Z isn't an<br>ancestor of W + all arrows *into* X deleted") +
  theme_do_calc()

plot_rule3_g_alt | plot_rule3_g_alt_modified
## Warning: Removed 1 rows containing missing values (`geom_dag_point()`).
## Warning: Removed 1 rows containing missing values (`geom_dag_text()`).
```

![](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/index_files/figure-html/plot-rule3-alt-1.png)
Phew. In this case, our DAG surgery for making the modified graph GX‾,Z(W)‾G_{\overline{X}, \overline{Z(W)}}GX,Z(W)​​ actually ended up completely d-separating Z from all nodes. Because Z isn’t an ancestor of W (but is instead a descendant), we get to delete arrows going into it, and we get to delete arrows going into X as well. We can remove do⁡(z)\operatorname{do}(z)do(z) from the equation as long as Y⊥Z∣W,XY \perp Z \mid W, XY⊥Z∣W,X in this modified graph. That is most definitely the case here. And once again, code confirms it (ignore the 0s here—they’re only there so that the DAG plots correctly):

```
impliedConditionalIndependencies[](https://rdrr.io/pkg/dagitty/man/impliedConditionalIndependencies.html)(rule3_g_alt_modified)
## 0 _||_ W
## 0 _||_ Y | X
## W _||_ X
## W _||_ Z
## X _||_ Z | 0
## Y _||_ Z | 0
## Y _||_ Z | X
```

And once again, we can legally get rid of do⁡(z)\operatorname{do}(z)do(z):
P(y∣do⁡(z),do⁡(x),w)=P(y∣do⁡(x),w) P(y \mid \operatorname{do}(z), \operatorname{do}(x), w) = P(y \mid \operatorname{do}(x), w) P(y∣do(z),do(x),w)=P(y∣do(x),w)
### Summary[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#summary)
Phew. Let’s look back at the three main rules and add their corresponding mathy versions, which should make more sense now:
  * **Rule 1** : Decide if we can ignore an observation
P(y∣z,do⁡(x),w)=P(y∣do⁡(x),w) if (Y⊥Z∣W,X)GX‾ P(y \mid z, \operatorname{do}(x), w) = P(y \mid \operatorname{do}(x), w) \qquad \text{ if } (Y \perp Z \mid W, X)_{G_{\overline{X}}} P(y∣z,do(x),w)=P(y∣do(x),w) if (Y⊥Z∣W,X)GX​​
  * **Rule 2** : Decide if we can treat an intervention as an observation
P(y∣do⁡(z),do⁡(x),w)=P(y∣z,do⁡(x),w) if (Y⊥Z∣W,X)GX‾,Z‾ P(y \mid \operatorname{do}(z), \operatorname{do}(x), w) = P(y \mid z, \operatorname{do}(x), w) \qquad \text{ if } (Y \perp Z \mid W, X)_{G_{\overline{X}, \underline{Z}}} P(y∣do(z),do(x),w)=P(y∣z,do(x),w) if (Y⊥Z∣W,X)GX,Z​​​
  * **Rule 3** : Decide if we can ignore an intervention
P(y∣do⁡(z),do⁡(x),w)=P(y∣do⁡(x),w) if (Y⊥Z∣W,X)GX‾,Z(W)‾ P(y \mid \operatorname{do}(z), \operatorname{do}(x), w) = P(y \mid \operatorname{do}(x), w) \qquad \text{ if } (Y \perp Z \mid W, X)_{G_{\overline{X}, \overline{Z(W)}}} P(y∣do(z),do(x),w)=P(y∣do(x),w) if (Y⊥Z∣W,X)GX,Z(W)​​​


## Deriving the backdoor adjustment formula from _do_ -calculus rules[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#deriving-the-backdoor-adjustment-formula-from-do-calculus-rules)
That was a lot of math, but hopefully each of these _do_ -calculus rules make sense in isolation now. Now that I finally understand what each of these are doing, we can apply these rules to see where the pre-derived / canned backdoor adjustment formula comes from. Somehow by applying these rules, we can transform the left-hand side of this formula into the _do_ -free right-hand side:
P(y∣do⁡(x))=∑zP(y∣x,z)×P(z) P(y \mid \operatorname{do}(x)) = \sum_z P(y \mid x, z) \times P(z) P(y∣do(x))=z∑​P(y∣x,z)×P(z)
Let’s go through the derivation of the backdoor adjustment formula step-by-step to see how it works. We’ll use this super simple DAG that shows the causal effect of treatment X on outcome Y, confounded by Z:

```
backdoor_g <- dagify[](https://r-causal.github.io/ggdag/reference/dagify.html)(
  Y ~ X + Z,
  X ~ Z,
  coords = list[](https://rdrr.io/r/base/list.html)(x = c[](https://rdrr.io/r/base/c.html)(Y = 2, X = 1, Z = 1.5),
                y = c[](https://rdrr.io/r/base/c.html)(Y = 1, X = 1, Z = 2))
)

plot_backdoor_g <- ggplot[](https://ggplot2.tidyverse.org/reference/ggplot.html)(backdoor_g, aes[](https://ggplot2.tidyverse.org/reference/aes.html)(x = x, y = y, 
                                          xend = xend, yend = yend)) +
  geom_dag_edges[](https://r-causal.github.io/ggdag/reference/geom_dag_edges.html)() +
  geom_dag_point[](https://r-causal.github.io/ggdag/reference/node_point.html)(color = "grey80", size = 10) +
  geom_dag_text[](https://r-causal.github.io/ggdag/reference/geom_dag_text.html)() +
  labs[](https://ggplot2.tidyverse.org/reference/labs.html)(title = TeX[](https://www.stefanom.io/latex2exp/reference/TeX.html)("$G$"),
       subtitle = "Basic backdoor confounding") +
  theme_do_calc()
plot_backdoor_g
```

![](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/index_files/figure-html/basic-backdoor-dag-1.png)
### Marginalizing across zzz [](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#marginalizing-across-z)
We’re interested in the causal effect of X on Y, or P(y∣do⁡(x))P(y \mid \operatorname{do}(x))P(y∣do(x)). If this were an experiment like a randomized controlled trial, we’d be able to delete all arrows going into X, which would remove all confounding from Z and allow us to measure the exact causal effect of X on Y. However, with observational data, we can’t delete arrows like that. But, we can condition the X → Y relationship on Z, given that it influences both X and Y.
We thus need to calculate the joint probability of P(y∣do⁡(x))P(y \mid \operatorname{do}(x))P(y∣do(x)) across all values of Z. Using the rules of [probability marginalization](https://en.wikipedia.org/wiki/Marginal_distribution) and [the chain rule for joint probabilities](https://en.wikipedia.org/wiki/Chain_rule_\(probability\)), we can write this joint probability like so:
P(y∣do⁡(x))=∑zP(y∣do⁡(x),z)×P(z∣do⁡(x)) P(y \mid \operatorname{do}(x)) = \sum_z P(y \mid \operatorname{do}(x), z) \times P(z \mid \operatorname{do}(x)) P(y∣do(x))=z∑​P(y∣do(x),z)×P(z∣do(x))
The right-hand side of that equation is what we want to be able to estimate using only observational data, but right now it has two do⁡(⋅)\operatorname{do}(\cdot)do(⋅) operators in it, marked in red and purple:
∑zP(y∣do⁡(x),z)×P(z∣do⁡(x)) \sum_z P(y \mid {\color{#FF4136} \operatorname{do}(x)}, z) \times P(z \mid {\color{#B10DC9} \operatorname{do}(x)}) z∑​P(y∣do(x),z)×P(z∣do(x))
We need to get rid of those.
### Applying Rule 2[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#applying-rule-2)
First let’s get rid of the red do⁡(x)\color{#FF4136} \operatorname{do}(x)do(x) that’s in P(y∣do⁡(x),z)P(y \mid {\color{#FF4136} \operatorname{do}(x)}, z)P(y∣do(x),z). This chunk of the equation involves all three variables: treatment, outcome, and confounder. Accordingly, we don’t really want to ignore any of these variables by using something like Rule 1 or Rule 3. Instead, we can try to treat that do⁡(x)\color{#FF4136} \operatorname{do}(x)do(x) as an observational x\color{#FF4136} xx using Rule 2.
According to Rule 2, we can treat an interventional do⁡(⋅)\operatorname{do}(\cdot)do(⋅) operator as observational if we meet specific criteria in a modified graph where we remove all arrows out of X:
P(y∣do⁡(x),z)=P(y∣x,z) if (Y⊥X∣Z)GX‾ P(y \mid {\color{#FF4136} \operatorname{do}(x)}, z) = P(y \mid {\color{#FF4136} x}, z) \qquad \text{ if } (Y \perp X \mid Z)_{G_{\underline{X}}} P(y∣do(x),z)=P(y∣x,z) if (Y⊥X∣Z)GX​​​
Here’s the modified GX‾G_{\underline{X}}GX​​ graph:

```
backdoor_g_underline_x <- dagify[](https://r-causal.github.io/ggdag/reference/dagify.html)(
  Y ~ Z,
  X ~ Z,
  coords = list[](https://rdrr.io/r/base/list.html)(x = c[](https://rdrr.io/r/base/c.html)(Y = 2, X = 1, Z = 1.5),
                y = c[](https://rdrr.io/r/base/c.html)(Y = 1, X = 1, Z = 2))
)

plot_backdoor_g_underline_x <- ggplot[](https://ggplot2.tidyverse.org/reference/ggplot.html)(backdoor_g_underline_x, 
                                      aes[](https://ggplot2.tidyverse.org/reference/aes.html)(x = x, y = y, 
                                          xend = xend, yend = yend)) +
  geom_dag_edges[](https://r-causal.github.io/ggdag/reference/geom_dag_edges.html)() +
  geom_dag_point[](https://r-causal.github.io/ggdag/reference/node_point.html)(color = "grey80", size = 10) +
  geom_dag_text[](https://r-causal.github.io/ggdag/reference/geom_dag_text.html)() +
  labs[](https://ggplot2.tidyverse.org/reference/labs.html)(title = TeX[](https://www.stefanom.io/latex2exp/reference/TeX.html)("$G_{\\underline{X}}$"),
       subtitle = "DAG with arrows *out of* X deleted") +
  theme_do_calc()

plot_backdoor_g | plot_backdoor_g_underline_x
```

![](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/index_files/figure-html/backdoor-rule2-1.png)
Following Rule 2, we can treat do⁡(x)\color{#FF4136} \operatorname{do}(x)do(x) like a regular observational x\color{#FF4136} xx as long as X and Y are d-separated in this modified GX‾G_{\underline{X}}GX​​ graph when conditioning on Z. And that is indeed the case: there’s no direct arrow between X and Y, and by conditioning on Z, there’s no active pathway between X and Y through Z. Let’s see if code backs us up:

```
impliedConditionalIndependencies[](https://rdrr.io/pkg/dagitty/man/impliedConditionalIndependencies.html)(backdoor_g_underline_x)
## X _||_ Y | Z
```

Perfect! Because Y⊥X∣ZY \perp X \mid ZY⊥X∣Z, we can treat do⁡(x)\color{#FF4136} \operatorname{do}(x)do(x) like x\color{#FF4136} xx.
### Applying Rule 3[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#applying-rule-3)
After applying Rule 2 to the first chunk of the equation, we’re still left with the purple do⁡(x)\color{#B10DC9} \operatorname{do}(x)do(x) in the second chunk:
∑zP(y∣x,z)×P(z∣do⁡(x)) \sum_z P(y \mid {\color{#FF4136} x}, z) \times P(z \mid {\color{#B10DC9} \operatorname{do}(x)}) z∑​P(y∣x,z)×P(z∣do(x))
This second chunk doesn’t have the outcome yyy in it and instead refers only to the treatment and confounder. Since it’s not connected with the outcome, it would be neat if we could get rid of that do⁡(x)\color{#B10DC9} \operatorname{do}(x)do(x) altogether. That’s what Rule 3 is for—ignoring interventions.
According to Rule 3, we can remove a do⁡(⋅)\operatorname{do}(\cdot)do(⋅) operator as long as it doesn’t influence the outcome through any uncontrolled or unconditioned path in a modified graph. Because we’re dealing with a smaller number of variables here, the math for Rule 3 is a lot simpler:
P(z∣do⁡(x))=P(z∣nothing!) if (X⊥Z)GX‾ P(z \mid {\color{#B10DC9} \operatorname{do}(x)}) = P(z \mid {\color{#B10DC9} \text{nothing!}}) \qquad \text{ if } (X \perp Z)_{G_{\overline{X}}} P(z∣do(x))=P(z∣nothing!) if (X⊥Z)GX​​
Here’s the simplified GX‾G_{\overline{X}}GX​ graph:

```
backdoor_g_overline_x <- dagify[](https://r-causal.github.io/ggdag/reference/dagify.html)(
  Y ~ X + Z,
  coords = list[](https://rdrr.io/r/base/list.html)(x = c[](https://rdrr.io/r/base/c.html)(Y = 2, X = 1, Z = 1.5),
                y = c[](https://rdrr.io/r/base/c.html)(Y = 1, X = 1, Z = 2))
)

plot_backdoor_g_overline_x <- ggplot[](https://ggplot2.tidyverse.org/reference/ggplot.html)(backdoor_g_overline_x, 
                                     aes[](https://ggplot2.tidyverse.org/reference/aes.html)(x = x, y = y, 
                                         xend = xend, yend = yend)) +
  geom_dag_edges[](https://r-causal.github.io/ggdag/reference/geom_dag_edges.html)() +
  geom_dag_point[](https://r-causal.github.io/ggdag/reference/node_point.html)(color = "grey80", size = 10) +
  geom_dag_text[](https://r-causal.github.io/ggdag/reference/geom_dag_text.html)() +
  labs[](https://ggplot2.tidyverse.org/reference/labs.html)(title = TeX[](https://www.stefanom.io/latex2exp/reference/TeX.html)("$G_{\\bar{X}}$"),
       subtitle = "DAG with arrows *into* X deleted") +
  theme_do_calc()

plot_backdoor_g | plot_backdoor_g_overline_x
```

![](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/index_files/figure-html/backdoor-rule3-1.png)
As long as X and Z are d-separated and independent, we can remove that do⁡(x)\color{#B10DC9} \operatorname{do}(x)do(x) completely. According to this graph, there’s no direct arrow connecting them, and there’s no active pathway through Y, since Y is a collider in this case and doesn’t pass on causal association. As always, let’s verify with code:

```
impliedConditionalIndependencies[](https://rdrr.io/pkg/dagitty/man/impliedConditionalIndependencies.html)(backdoor_g_overline_x)
## X _||_ Z
```

Huzzah! X⊥ZX \perp ZX⊥Z, which means we can nuke the do⁡(x)\color{#B10DC9} \operatorname{do}(x)do(x).
### Final equation[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#final-equation)
After marginalizing across zzz, applying Rule 2, and applying Rule 3, we’re left with the following formula for backdoor adjustment:
P(y∣do⁡(x))=∑zP(y∣x,z)×P(z) P(y \mid \operatorname{do}(x)) = \sum_z P(y \mid x, z) \times P(z) P(y∣do(x))=z∑​P(y∣x,z)×P(z)
That’s exactly the same formula as the general backdoor adjustment formula—we successfully derived it using _do_ -calculus rules!
Most importantly, there are no do⁡(⋅)\operatorname{do}(\cdot)do(⋅) operators anywhere in this equation, making this estimand completely _do_ -free and estimable using non-interventional observational data! As long as we close the backdoor confounding by adjusting for Z (however you want, like through inverse probability weighting, matching, fancy machine learning stuff, or whatever else—see [this chapter](https://www.andrewheiss.com/research/chapters/heiss-causal-inference-2021/), or [this blog post](https://www.andrewheiss.com/blog/2020/02/25/closing-backdoors-dags/), or [this guide](https://evalf21.classes.andrewheiss.com/example/matching-ipw/) for examples of how to do this), we can estimate the causal effect of X on Y (or P(y∣do⁡(x))P(y \mid \operatorname{do}(x))P(y∣do(x))) with only observational data.
Here’s the derivation all at once:
[Marginalization across z+chain rule for conditional probabilities]P(y∣do⁡(x))=∑zP(y∣do⁡(x),z)×P(z∣do⁡(x))[Use Rule 2 to treat do⁡(x) as x]=∑zP(y∣x,z)×P(z∣do⁡(x))[Use Rule 3 to nuke do⁡(x)]=∑zP(y∣x,z)×P(z∣nothing!)[Final backdoor adjustment formula!]=∑zP(y∣x,z)×P(z) \begin{aligned} & [\text{Marginalization across } z + \text{chain rule for conditional probabilities}] \\\ P(y \mid \operatorname{do}(x)) =& \sum_z P(y \mid {\color{#FF4136} \operatorname{do}(x)}, z) \times P(z \mid {\color{#B10DC9} \operatorname{do}(x)}) \\\ & [\text{Use Rule 2 to treat } {\color{#FF4136} \operatorname{do}(x)} \text{ as } {\color{#FF4136} x}] \\\ =& \sum_z P(y \mid {\color{#FF4136} x}, z) \times P(z \mid {\color{#B10DC9} \operatorname{do}(x)}) \\\ & [\text{Use Rule 3 to nuke } {\color{#B10DC9} \operatorname{do}(x)}] \\\ =& \sum_z P(y \mid {\color{#FF4136} x}, z) \times P(z \mid {\color{#B10DC9} \text{nothing!}}) \\\ & [\text{Final backdoor adjustment formula!}] \\\ =& \sum_z P(y \mid x, z) \times P(z) \end{aligned} P(y∣do(x))====​[Marginalization across z+chain rule for conditional probabilities]z∑​P(y∣do(x),z)×P(z∣do(x))[Use Rule 2 to treat do(x) as x]z∑​P(y∣x,z)×P(z∣do(x))[Use Rule 3 to nuke do(x)]z∑​P(y∣x,z)×P(z∣nothing!)[Final backdoor adjustment formula!]z∑​P(y∣x,z)×P(z)​
That’s so so cool!
The frontdoor adjustment formula can be derived in a similar process—see [the end of this post for an example](https://stephenmalina.com/post/2020-03-09-front-door-do-calc-derivation/#fn:1) (with that, you apply Rules 2 and 3 repeatedly until all the do⁡(⋅)\operatorname{do}(\cdot)do(⋅) operators disappear)
And in cases where there’s no pre-derived backdoor or frontdoor adjustment formula, you can still apply these three _do_ -calculus rules to attempt to identify the relationship between X and Y. Not all DAGs are fully estimable, but if they are estimable, the rules of _do_ -calculus can be applied to derive the estimate. Fancier tools like [Causal Fusion](https://causalfusion.net/) help with this and automate the process.
## References[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#references-1)
Lattimore, Finnian, and David Rohde. 2019. “Replacing the Do-Calculus with Bayes Rule,” December. <https://arxiv.org/abs/1906.07125>. 
Neal, Brady. 2020. _Introduction to Causal Inference from a Machine Learning Perspective_. <https://www.bradyneal.com/causal-inference-course>. 
Pearl, Judea. 2012. “The _Do_ -Calculus Revisited.” In _Proceedings of the Twenty-Eighth Conference on Uncertainty in Artificial Intelligence_ , 3–11. UAI’12. Arlington, Virginia: AUAI Press. <https://dl.acm.org/doi/10.5555/3020652.3020654>. 
## Citation[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#citation)
BibTeX citation:

```
@online{heiss2021,
  author = {Heiss, Andrew},
  title = {Do-Calculus Adventures! {Exploring} the Three Rules of
    Do-Calculus in Plain Language and Deriving the Backdoor Adjustment
    Formula by Hand},
  date = {2021-09-07},
  url = {https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/},
  doi = {10.59350/fqkhz-kq526},
  langid = {en}
}
__
```

For attribution, please cite this work as:
Heiss, Andrew. 2021. “Do-Calculus Adventures! Exploring the Three Rules of Do-Calculus in Plain Language and Deriving the Backdoor Adjustment Formula by Hand.” September 7, 2021. <https://doi.org/10.59350/fqkhz-kq526>. 
##### Source Code

```
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-1)---
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-2)title: "Do-calculus adventures! Exploring the three rules of do-calculus in plain language and deriving the backdoor adjustment formula by hand"
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-3)date: 2021-09-07
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-4)description: "Use R to explore the three rules of <em>do</em>-calculus in plain language and derive the backdoor adjustment formula by hand"
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-5)image: do-calculus-math.png
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-6)categories:
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-7)  - r
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-8)  - tidyverse
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-9)  - DAGs
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-10)  - causal inference
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-11)  - do calculus
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-12)html-math-method: katex
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-13)doi: 10.59350/fqkhz-kq526
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-14)citation: true
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-15)---
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-16)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-17)```{r knitr-options, include=FALSE}
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-18)knitr::opts_chunk$set(fig.align = "center", fig.retina = 3, collapse = TRUE)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-19)```
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-20)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-21)I've been teaching [a course on program evaluation](https://evalf21.classes.andrewheiss.com/) since Fall 2019, and while part of the class is focused on logic models and the more managerial aspects of evaluation, the bulk of the class is focused on causal inference. Ever since reading [Judea Pearl's *The Book of Why*](http://bayes.cs.ucla.edu/WHY/) in 2019, I've thrown myself into the world of DAGs, econometrics, and general causal inference, and I've been both teaching it and using it in research ever since. I've even [published a book chapter on it](https://www.andrewheiss.com/research/chapters/heiss-causal-inference-2021/). Fun stuff.
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-22)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-23)This post assumes you have a general knowledge of DAGs and backdoor confounding. Read [this post](https://www.andrewheiss.com/blog/2020/02/25/closing-backdoors-dags/) or [this chapter](https://www.andrewheiss.com/research/chapters/heiss-causal-inference-2021/) if you haven't heard about those things yet.
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-24)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-25)DAGs are a powerful tool for causal inference because they let you map out all your assumptions of the data generating process for some treatment and some outcome. Importantly, these causal graphs help you determine what statistical approaches you need to use to isolate or identify the causal arrow between treatment and outcome. One of the more common (and intuitive) methods for idenfifying causal effects with DAGs is to close back doors, or adjust for nodes in a DAG that open up unwanted causal associtions between treatment and control. By properly closing backdoors, you can estimate a causal quantity using observational data. There's even a special formula called the backdoor adjustment formula that takes an equation with a $\operatorname{do}(\cdot)$ operator (a [special mathematical function](https://stats.stackexchange.com/questions/211008/dox-operator-meaning) representing a direct experimental intervention in a graph) and allows you to estimate the effect with *do*-free quantities:
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-26)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-27)$$
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-28)P(y \mid \operatorname{do}(x)) = \sum_z P(y \mid x, z) \times P(z)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-29)$$
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-30)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-31)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-32)When I teach this stuff, I show that formula on a slide, tell students they don't need to worry about it too much, and then show how actually do it using regression, inverse probability weighting, and matching ([with this guide](https://evalf21.classes.andrewheiss.com/example/matching-ipw/)). For my MPA and MPP students, the math isn't as important as the actual application of these principles, so that's what I focus on.
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-33)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-34)However—confession time—that math is also a bit of a magic black box for me too. I've read it in books and assume that it's correct, but I never really fully understood why.
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-35)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-36)Compounding my confusion is the fact that the foundation of Judea Pearl-style DAG-based causal inference is the idea of *do*-calculus [@Pearl:2012]: a set of three mathematical rules that can be applied to a causal graph to identify causal relationships. Part of my confusion stems from the fact that most textbooks and courses (including mine!) explain that you can identify causal relationships in DAGs using backdoor adjustment, frontdoor adjustment, or the fancy application of *do*-calculus rules. When framed like this, it seems like backdoor and frontdoor adjustment are separate things from *do*-calculus, and that *do*-calculus is something you do when backdoor and frontdoor adjustments don't work.
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-37)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-38)But that's not the case! In 2020, [I asked Twitter](https://twitter.com/@andrewheiss) if backdoor and frontdoor adjustment were connected to *do*-calculus, and surprisingly [Judea Pearl himself answered](https://twitter.com/yudapearl/status/1252462516468240390) that they are! 
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-39)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-40)```{r echo=FALSE, out.width="70%", fig.align="center"}
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-41)knitr::include_graphics("pearl-tweet.png")
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-42)```
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-43)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-44)They're both specific consequences of the application of the rules of *do*-calculus—they just have special names because they're easy to see in a graph. 
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-45)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-46)But how? How do people apply these strange rules of *do*-calculus to derive these magical backdoor and frontdoor adjustment formulas? The question has haunted me since April 2020.
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-47)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-48)But in the past couple days, I've stumbled across a couple excellent resources ([this course](https://www.bradyneal.com/causal-inference-course) and [these videos](https://www.youtube.com/playlist?list=PLoazKTcS0Rzb6bb9L508cyJ1z-U9iWkA0) + [this blog post](https://stephenmalina.com/post/2020-03-09-front-door-do-calc-derivation/)) that explained *do*-calculus really well, so I figured I'd finally tackle this question and figure out how exactly *do*-calculus is used to derive the backdoor adjustment formula. I won't show the derivation of the frontdoor formula—smarter people than me have done that ([here](https://stephenmalina.com/post/2020-03-09-front-door-do-calc-derivation/) and [Section 6.2.1 here](https://www.bradyneal.com/Introduction_to_Causal_Inference-Dec17_2020-Neal.pdf), for instance), but I can do the backdoor one now!
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-49)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-50)First, I'll explain and illustrate how each of the three rules of *do*-calculus as plain-language-y as possible, and then I'll apply those rules to show how the backdoor adjustment formula is created. 
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-51)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-52)I use the **ggdag** and **dagitty** packages in R for all this, so you can follow along too. Here we go!
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-53)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-54)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-55)```{r setup, warning=FALSE, message=FALSE}
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-56)library(tidyverse)  # For ggplot2 and friends
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-57)library(patchwork)  # For combining plots
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-58)library(ggdag)      # For making DAGs with ggplot
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-59)library(dagitty)    # For dealing with DAG math
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-60)library(latex2exp)  # Easily convert LaTeX into arcane plotmath expressions
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-61)library(ggtext)     # Use markdown in ggplot labels
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-62)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-63)# Create a cleaner serifed theme to use throughout
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-64)theme_do_calc <- function() {
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-65)  theme_dag(base_family = "Linux Libertine O") +
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-66)    theme(plot.title = element_text(size = rel(1.5)),
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-67)        plot.subtitle = element_markdown())
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-68)}
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-69)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-70)# Make all geom_dag_text() layers use these settings automatically
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-71)update_geom_defaults(ggdag:::GeomDagText, list(family = "Linux Libertine O", 
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-72)                                               fontface = "bold",
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-73)                                               color = "black"))
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-74)```
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-75)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-76)## Exploring the rules of *do*-calculus
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-77)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-78)The three rules of *do*-calculus have always been confusing to me since they are typically written as pure math equations and not in plain understandable language. For instance, [here's Judea Pearl's canonical primer on *do*-calculus](https://ftp.cs.ucla.edu/pub/stat_ser/r402.pdf)—a short PDF with lots of math and proofs [@Pearl:2012]. In basically everything I've read about *do*-calculus, there's inevitably a listing of these three very mathy rules, written for people much smarter than me:
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-79)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-80)```{r echo=FALSE, out.width="100%", fig.align="center"}
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-81)#| fig-cap: "From left to right: @LattimoreRohde:2019, [The Stanford Encyclopedia of Philosophy](https://plato.stanford.edu/entries/causal-models/do-calculus.html), @Pearl:2012, @Neal:2020"
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-82)knitr::include_graphics("do-calculus-math.png")
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-83)```
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-84)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-85)However, beneath this scary math, each rule has specific intuition and purpose behind it—I just didn't understand the plain-language reasons for each rule until reading [this really neat blog post](https://stephenmalina.com/post/2020-03-09-front-door-do-calc-derivation/). Here's what each rule actually does:
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-86)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-87)- **Rule 1**: Decide if we can ignore an observation
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-88)- **Rule 2**: Decide if we can treat an intervention as an observation
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-89)- **Rule 3**: Decide if we can ignore an intervention
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-90)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-91)Whoa! That's exceptionally logical. Each rule is designed to help simplify and reduce nodes in a DAG by either ignoring them (Rules 1 and 3) or making it so interventions like $\operatorname{do}(\cdot)$ can be treated like observations instead (Rule 2).
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-92)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-93)Let's explore each of these rules in detail. In all these situations, we're assuming that there's a DAG with 4 nodes: W, X, Y, and Z. Y is always the outcome; X is always the main treatment. In each rule, our goal is to get rid of Z by applying the rule. When talking about interventions in a graph, there's a special notation with overlines and underlines:
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-94)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-95)- An overline like $G_{\overline{X}}$ means that you delete all the arrows *going into* X
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-96)- An underline like $G_{\underline{X}}$ means that you delete all the arrows *coming out of* X
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-97)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-98)I imagine this line like a wall:
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-99)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-100)- If the wall is on top of X like $\overline{X}$, you can't draw any arrows going into it, so you delete anything going in
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-101)- If the wall is on the bottom of X like $\underline{X}$, you can't draw any arrows going out of it, so you delete anything going out
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-102)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-103)### Rule 1: Ignoring observations
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-104)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-105)According to Rule 1, we can ignore any observational node if it doesn't influence the outcome through any path, or if it is d-separated from the outcome. Here's the formal definition:
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-106)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-107)$$
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-108)P(y \mid z, \operatorname{do}(x), w) = P(y \mid \operatorname{do}(x), w) \qquad \text{ if } (Y \perp Z \mid W, X)_{G_{\overline{X}}}
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-109)$$
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-110)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-111)There are a lot of moving parts here, but remember, the focus in this equation is $z$. Our goal here is to remove or ignore $z$. Notice how $z$ exists on the left-hand side of the equation and how it is gone on the right-hand side. As long as we meet the cryptic conditions of $(Y \perp Z \mid W, X)_{G_{\overline{X}}}$, we can get rid of it. But what the heck does that even mean? 
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-112)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-113)Here, $G_{\overline{X}}$ means "the original causal graph with all arrows into X removed", while the $Y \perp Z \mid W, X$ part means "Y is independent of Z, given W and X" in the new modified graph. If the Y and Z nodes are d-separated from each other after we account for both W and X, we can get rid of Z and ignore it.
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-114)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-115)Let's look at this graphically to help make better sense of this. We'll use the `dagify()` function from **ggdag** to build a couple DAGs: one complete one ($G$) and one with all the arrows into X deleted ($G_{\overline{X}}$). X causes both X and Y, while W confounds X, Y, and Z. 
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-116)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-117)```{r build-rule1}
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-118)rule1_g <- dagify(
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-119)  Y ~ X + W,
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-120)  X ~ W,
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-121)  Z ~ X + W,
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-122)  coords = list(x = c(X = 1, Y = 2, Z = 1.25, W = 1.5),
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-123)                y = c(X = 1, Y = 1, Z = 2, W = 2))
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-124))
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-125)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-126)rule1_g_x_over <- dagify(
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-127)  Y ~ X + W,
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-128)  Z ~ X + W,
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-129)  coords = list(x = c(X = 1, Y = 2, Z = 1.25, W = 1.5),
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-130)                y = c(X = 1, Y = 1, Z = 2, W = 2))
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-131)) 
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-132)```
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-133)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-134)```{r plot-rule1, fig.width=8, fig.height=3, out.width="100%"}
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-135)#| column: page-inset-right
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-136)plot_rule1_g <- ggplot(rule1_g, aes(x = x, y = y, 
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-137)                                    xend = xend, yend = yend)) +
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-138)  geom_dag_edges() +
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-139)  geom_dag_point(color = "grey80", size = 10) +
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-140)  geom_dag_text() +
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-141)  labs(title = TeX("$G$"),
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-142)       subtitle = "Original DAG") +
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-143)  theme_do_calc()
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-144)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-145)plot_rule1_g_x_over <- ggplot(rule1_g_x_over, aes(x = x, y = y, 
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-146)                                                  xend = xend, yend = yend)) +
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-147)  geom_dag_edges() +
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-148)  geom_dag_point(color = "grey80", size = 10) +
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-149)  geom_dag_text() +
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-150)  labs(title = TeX("$G_{\\bar{X}}$"),
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-151)       subtitle = "DAG with arrows *into* X deleted") +
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-152)  theme_do_calc()
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-153)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-154)plot_rule1_g | plot_rule1_g_x_over
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-155)```
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-156)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-157)If we want to calculate the causal effect of X on Y, do we need to worry about Z here, or can we ignore it? Let's apply Rule 1. If we look at the modified $G_{\overline{X}}$, Y and Z are completely d-separated if we account for both W and X—there's no direct arrow between them, and there's no active path connecting them through W or X, since we're accounting for (or condition on) those nodes. Y and Z are thus d-separated and $Y \perp Z \mid W, X$. We can confirm this with the `impliedConditionalIndependencies()` function from the **dagitty** package:
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-158)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-159)```{r independencies-rule1}
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-160)impliedConditionalIndependencies(rule1_g_x_over)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-161)```
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-162)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-163)And there it is! The second independency there is $Y \perp Z \mid W, X$. That means that we can apply Rule 1 and ignore Z, meaning that
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-164)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-165)$$
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-166)P(y \mid z, \operatorname{do}(x), w) = P(y \mid \operatorname{do}(x), w)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-167)$$
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-168)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-169)This makes sense but is a little too complicated for me, since we're working with four different nodes. We can simplify this and pretend that $\operatorname{do}(x)$ is nothing and that X doesn't exist. That leaves us with just three nodes—W, Y, and Z—and this DAG:
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-170)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-171)```{r plot-rule1-simple, fig.width=4, fig.height=3, out.width="60%"}
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-172)rule1_g_simple <- dagify(
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-173)  Y ~ W,
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-174)  Z ~ W,
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-175)  coords = list(x = c(Y = 2, Z = 1, W = 1.5),
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-176)                y = c(Y = 1, Z = 1, W = 2))
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-177))
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-178)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-179)plot_rule1_g_simple <- ggplot(rule1_g_simple, aes(x = x, y = y, 
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-180)                                                  xend = xend, yend = yend)) +
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-181)  geom_dag_edges() +
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-182)  geom_dag_point(color = "grey80", size = 10) +
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-183)  geom_dag_text() +
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-184)  labs(title = TeX("$G$"),
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-185)       subtitle = "Simplified DAG without X") +
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-186)  theme_do_calc()
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-187)plot_rule1_g_simple
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-188)```
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-189)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-190)The simplified X-free version of Rule 1 looks like this:
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-191)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-192)$$
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-193)P(y \mid z, w) = P(y \mid w) \qquad \text{ if } (Y \perp Z \mid W)_{G}
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-194)$$
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-195)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-196)In other words, we can ignore Z and remove it from the $P(y \mid z, w)$ equation if Y and Z are d-separated (or independent of each other) after accounting for W. Once we account for W, there's no possible connection between Y and Z, so they really are d-separated. We can again confirm this with code:
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-197)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-198)```{r independencies-rule1-simple}
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-199)impliedConditionalIndependencies(rule1_g_simple)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-200)```
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-201)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-202)There we go. Because $Y \perp Z \mid W$ we can safely ignore Z.
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-203)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-204)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-205)### Rule 2: Treating interventions as observations
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-206)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-207)Rule 1 is neat, but it has nothing to do with causal interventions or the $\operatorname{do}(\cdot)$ operator. It feels more like a housekeeping rule—it's a way of simplifying and removing unnecessary nodes that don't have to do with the main treatment → outcome relationship. 
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-208)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-209)With Rule 2, we start messing with interventions. In an experiment like a randomized controlled trial, a researcher has the ability to assign treatment and either $\operatorname{do}(x)$ or not $\operatorname{do}(x)$. With observational data, though, it's not possible to $\operatorname{do}(x)$ directly. It would be fantastic if we could take an intervention like $\operatorname{do}(x)$ and treat it like regular non-interventional observational data. Rule 2 lets us do this.
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-210)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-211)According to Rule 2, interventions (or $do(x)$) can be treated as observations (or $x$) when the causal effect of a variable on the outcome ($X \rightarrow Y$) only influences the outcome through directed paths. The official math for this is this complicated thing:
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-212)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-213)$$
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-214)P(y \mid \operatorname{do}(z), \operatorname{do}(x), w) = P(y \mid z, \operatorname{do}(x), w) \qquad \text{ if } (Y \perp Z \mid W, X)_{G_{\overline{X}, \underline{Z}}}
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-215)$$
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-216)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-217)For me, this is super confusing, since there are two different $\operatorname{do}(\cdot)$ operators here and when I think of causal graphs, I think of single interventions. Like we did with Rule 1, we can simplify this and pretend that there's no intervention $\operatorname{do}(x)$ (we'll do the full rule in a minute, don't worry). Again, this is legal because each of these rules are focused on messing with the Z variable: ignoring it or treating it as an observation. That leaves us with this slightly simpler (though still cryptic) equation:
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-218)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-219)$$
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-220)P(y \mid \operatorname{do}(z), w) = P(y \mid z, w) \qquad \text{ if } (Y \perp Z \mid W)_{G_{\underline{Z}}}
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-221)$$
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-222)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-223)Notice how the left-hand side has the interventional $\operatorname{do}(z)$, while the right-hand side has the observed $z$. As long as we meet the condition $(Y \perp Z \mid W)_{G_{\underline{Z}}}$, we can transform $\operatorname{do}(z)$ into $z$ and work only with observational data. Once again, though, what does this $(Y \perp Z \mid W)_{G_{\underline{Z}}}$ condition even mean?
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-224)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-225)Here, $G_{\underline{Z}}$ means "the original causal graph with all arrows out of Z removed", while the $Y \perp Z \mid W$ part means "Y is independent of Z, given W" in the new modified graph. Similar to Rule 1, if the Y and Z nodes are d-separated from each other after we account for W, we can legally treat $\operatorname{do}(z)$ like $z$.
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-226)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-227)As we did with Rule 1, we'll build a couple basic DAGs: a complete one ($G$) and one with all the arrows *out of* Z deleted ($G_{\underline{Z}}$).
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-228)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-229)```{r build-rule2-simple}
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-230)rule2_g_simple <- dagify(
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-231)  Y ~ Z + W,
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-232)  Z ~ W,
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-233)  coords = list(x = c(Y = 2, Z = 1, W = 1.5),
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-234)                y = c(Y = 1, Z = 1, W = 2))
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-235))
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-236)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-237)rule2_g_simple_z_under <- dagify(
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-238)  Y ~ W,
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-239)  Z ~ W,
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-240)  coords = list(x = c(Y = 2, Z = 1, W = 1.5),
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-241)                y = c(Y = 1, Z = 1, W = 2))
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-242)) 
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-243)```
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-244)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-245)```{r plot-rule2-simple, fig.width=8, fig.height=3, out.width="100%"}
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-246)#| column: page-inset-right
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-247)plot_rule2_g_simple <- ggplot(rule2_g_simple, 
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-248)                              aes(x = x, y = y, 
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-249)                                  xend = xend, yend = yend)) +
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-250)  geom_dag_edges() +
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-251)  geom_dag_point(color = "grey80", size = 10) +
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-252)  geom_dag_text() +
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-253)  labs(title = TeX("$G$"),
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-254)       subtitle = "Original DAG") +
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-255)  theme_do_calc()
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-256)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-257)plot_rule2_g_simple_z_under <- ggplot(rule2_g_simple_z_under, 
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-258)                                      aes(x = x, y = y, 
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-259)                                          xend = xend, yend = yend)) +
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-260)  geom_dag_edges() +
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-261)  geom_dag_point(color = "grey80", size = 10) +
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-262)  geom_dag_text() +
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-263)  labs(title = TeX("$G_{\\underline{Z}}$"),
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-264)       subtitle = "DAG with arrows *out of* Z deleted") +
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-265)  theme_do_calc()
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-266)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-267)plot_rule2_g_simple | plot_rule2_g_simple_z_under
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-268)```
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-269)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-270)So, can we treat Z here like an observational node instead of a interventional $\operatorname{do}(\cdot)$ node? Let's apply Rule 2. If we look at the modified $G_{\underline{Z}}$ graph, Z and Y are completely d-separated if we account for W—there's no direct arrow between them, and there's no active path connecting them through W since we're conditioning on W. We can thus say that $Y \perp Z \mid W$. We can confirm this with code too:
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-271)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-272)```{r independencies-rule2-simple}
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-273)impliedConditionalIndependencies(rule2_g_simple_z_under)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-274)```
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-275)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-276)Woohoo! Because $Y \perp Z \mid W$ in that modified $G_{\underline{Z}}$ graph, we can legally convert the interventional $\operatorname{do}(z)$ to just a regular old observational $z$:
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-277)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-278)$$
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-279)P(y \mid \operatorname{do}(z), w) = P(y \mid z, w)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-280)$$
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-281)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-282)So far we've applied Rule 2 to a simplified DAG with three nodes, but what does it look like if we're using the full four-node graph that is used in the formal definition of Rule 2?
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-283)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-284)$$
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-285)P(y \mid \operatorname{do}(z), \operatorname{do}(x), w) = P(y \mid z, \operatorname{do}(x), w) \qquad \text{ if } (Y \perp Z \mid W, X)_{G_{\overline{X}, \underline{Z}}}
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-286)$$
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-287)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-288)Here's one graphical representation of a graph with the four nodes W, X, Y, and Z (but it's definitely not the only possible graph! These *do*-calculus rules don't assume any specific relationships between the nodes). Here, Y is caused by both X and Z, and we'll pretend that they're both interventions (so $\operatorname{do}(x)$ and $\operatorname{do}(z)$). X is causally linked to Z, and W confounds all three: X, Y, and Z. Graph $G$ shows the complete DAG; Graph $G_{\overline{X}, \underline{Z}}$ shows a modified DAG with all arrows *into* X deleted ($\overline{X}$) and all arrows *out of* Z deleted ($\underline{Z}$).
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-289)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-290)```{r build-rule2}
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-291)rule2_g <- dagify(
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-292)  Y ~ X + W + Z,
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-293)  X ~ W,
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-294)  Z ~ X + W,
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-295)  coords = list(x = c(X = 1, Y = 2, Z = 1.25, W = 1.5),
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-296)                y = c(X = 1, Y = 1, Z = 2, W = 2))
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-297))
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-298)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-299)rule2_g_modified <- dagify(
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-300)  Y ~ X + W,
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-301)  Z ~ X + W,
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-302)  coords = list(x = c(X = 1, Y = 2, Z = 1.25, W = 1.5),
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-303)                y = c(X = 1, Y = 1, Z = 2, W = 2))
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-304)) 
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-305)```
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-306)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-307)```{r plot-rule2, fig.width=8, fig.height=3, out.width="100%"}
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-308)#| column: page-inset-right
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-309)plot_rule2_g <- ggplot(rule2_g, aes(x = x, y = y, 
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-310)                                    xend = xend, yend = yend)) +
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-311)  geom_dag_edges() +
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-312)  geom_dag_point(color = "grey80", size = 10) +
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-313)  geom_dag_text() +
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-314)  labs(title = TeX("$G$"),
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-315)       subtitle = "Original DAG") +
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-316)  theme_do_calc()
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-317)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-318)plot_rule2_modified <- ggplot(rule2_g_modified, 
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-319)                              aes(x = x, y = y, 
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-320)                                  xend = xend, yend = yend)) +
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-321)  geom_dag_edges() +
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-322)  geom_dag_point(color = "grey80", size = 10) +
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-323)  geom_dag_text() +
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-324)  labs(title = TeX("$G_{\\bar{X}, \\underline{Z}}$"),
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-325)       subtitle = "DAG with arrows *into* X and *out of* Z deleted") +
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-326)  theme_do_calc()
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-327)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-328)plot_rule2_g | plot_rule2_modified
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-329)```
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-330)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-331)Okay. Our goal here is to check if we can treat $\operatorname{do}(z)$ like a regular observational $z$. We can legally do this if Y and Z are d-separated in that modified graph, after accounting for both W and X, or $Y \perp Z \mid W, X$. And that is indeed the case! There's no direct arrow connecting Y and Z in the modified graph, and once we condition on (or account for) W and X, no pathways between Y and Z are active—Y and Z are independent and d-separated. We can confirm this with code:
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-332)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-333)```{r independencies-rule2}
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-334)impliedConditionalIndependencies(rule2_g_modified)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-335)```
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-336)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-337)The second independency there is that $Y \perp Z \mid W, X$, which is exactly what we want to see. We can thus legally transform $\operatorname{do}(z)$ to $z$:
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-338)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-339)$$
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-340)P(y \mid \operatorname{do}(z), \operatorname{do}(x), w) = P(y \mid z, \operatorname{do}(x), w)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-341)$$
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-342)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-343)What's really neat is that Rule 2 is a generalized version of the backdoor criterion. More on that below after we explore Rule 3.
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-344)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-345)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-346)### Rule 3: Ignoring interventions
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-347)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-348)Rule 3 is the trickiest of the three, conceptually. It tells us when we can completely remove a $\operatorname{do}(\cdot)$ expression rather than converting it to an observed quantity. Here it is in all its mathy glory:
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-349)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-350)$$
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-351)P(y \mid \operatorname{do}(z), \operatorname{do}(x), w) = P(y \mid \operatorname{do}(x), w) \qquad \text{ if } (Y \perp Z \mid W, X)_{G_{\overline{X}, \overline{Z(W)}}}
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-352)$$
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-353)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-354)In simpler language, this means that we can ignore an intervention (or a $\operatorname{do}(\cdot)$ expression) if it doesn't influence the outcome through any uncontrolled path—we can remove $\operatorname{do}(z)$ if there is no causal association (or no unblocked causal paths) flowing from Z to Y.
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-355)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-356)This rule is tricky, though, because it depends on where the Z node (i.e. the intervention we want to get rid of) appears in the graph. Note the notation for the modified graph here. With the other rules, we used things like $G_{\overline{X}}$ or $G_{\underline{Z}}$ to remove arrows into and out of specific nodes in the modified graph. Here, though, we have the strange $G_{\overline{Z(W)}}$. This Z(W) is weird! It means "any Z node that isn't an ancestor of W". We thus only delete arrows going into a Z node in the modified graph if that Z node doesn't precede W.
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-357)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-358)Here's one version of what that could look like graphically:
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-359)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-360)```{r build-rule3}
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-361)rule3_g <- dagify(
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-362)  Y ~ X + W,
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-363)  W ~ Z,
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-364)  Z ~ X,
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-365)  coords = list(x = c(X = 1, Y = 2, Z = 1.25, W = 1.5),
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-366)                y = c(X = 1, Y = 1, Z = 2, W = 1.75))
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-367))
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-368)```
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-369)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-370)```{r plot-rule3, fig.width=8, fig.height=3, out.width="100%"}
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-371)#| column: page-inset-right
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-372)plot_rule3_g <- ggplot(rule3_g, 
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-373)                       aes(x = x, y = y, 
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-374)                           xend = xend, yend = yend)) +
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-375)  geom_dag_edges() +
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-376)  geom_dag_point(color = "grey80", size = 10) +
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-377)  geom_dag_text() +
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-378)  labs(title = TeX("$G$"),
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-379)       subtitle = "Original DAG") +
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-380)  theme_do_calc()
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-381)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-382)plot_rule3_g_modified <- ggplot(rule3_g, 
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-383)                                aes(x = x, y = y, 
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-384)                                    xend = xend, yend = yend)) +
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-385)  geom_dag_edges() +
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-386)  geom_dag_point(color = "grey80", size = 10) +
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-387)  geom_dag_text() +
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-388)  labs(title = TeX("$G_{\\bar{X}, \\bar{Z(W)}}$"),
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-389)       subtitle = "DAG with arrows *into* Z deleted as long as Z isn't an<br>ancestor of W + all arrows *into* X deleted") +
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-390)  theme_do_calc()
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-391)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-392)plot_rule3_g | plot_rule3_g_modified
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-393)```
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-394)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-395)Notice how these two graphs are identical. Because we only delete arrows going into Z if Z is not an ancestor of W, in this case $G = G_{\overline{X}, \overline{Z(W)}}$. 
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-396)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-397)Remember that our original goal is to get rid of $\operatorname{do}(z)$, which we can legally do if Y and Z are d-separated and independent in our modified graph, or if $Y \perp Z \mid W, X$. That is once again indeed the case here: there's no direct arrow between Y and Z, and if we condition on W and X, there's no way to pass association between Y and Z, meaning that Y and Z are d-separated. Let's confirm it with code:
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-398)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-399)```{r independencies-rule3}
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-400)impliedConditionalIndependencies(rule3_g)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-401)```
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-402)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-403)That second independency is our $Y \perp Z \mid W, X$, so we can safely eliminate $\operatorname{do}(z)$ from the equation. We can ignore it because it doesn't influence the outcome $Y$ through any possible path. Goodbye $\operatorname{do}(z)$!:
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-404)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-405)$$
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-406)P(y \mid \operatorname{do}(z), \operatorname{do}(x), w) = P(y \mid \operatorname{do}(x), w)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-407)$$
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-408)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-409)In this case, the alternative graph $G_{\overline{X}, \overline{Z(W)}}$ was the same as the original graph because of the location of Z—Z was an ancestor of W, so we didn't delete any arrows. If Z is *not* an ancestor, though, we get to actually modify the graph. For instance, consider this DAG:
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-410)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-411)```{r build-rule3-alt}
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-412)rule3_g_alt <- dagify(
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-413)  Y ~ X + W,
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-414)  Z ~ W,
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-415)  X ~ Z,
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-416)  coords = list(x = c(X = 1, Y = 2, Z = 1.25, W = 1.5),
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-417)                y = c(X = 1, Y = 1, Z = 2, W = 1.75))
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-418))
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-419)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-420)rule3_g_alt_modified <- dagify(
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-421)  Y ~ X + W,
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-422)  Z ~ 0,
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-423)  X ~ 0,
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-424)  coords = list(x = c(X = 1, Y = 2, Z = 1.25, W = 1.5),
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-425)                y = c(X = 1, Y = 1, Z = 2, W = 1.75))
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-426)) 
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-427)```
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-428)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-429)```{r plot-rule3-alt, fig.width=8, fig.height=3, out.width="100%"}
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-430)#| column: page-inset-right
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-431)plot_rule3_g_alt <- ggplot(rule3_g_alt, 
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-432)                           aes(x = x, y = y, 
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-433)                               xend = xend, yend = yend)) +
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-434)  geom_dag_edges() +
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-435)  geom_dag_point(color = "grey80", size = 10) +
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-436)  geom_dag_text() +
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-437)  labs(title = TeX("$G$"),
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-438)       subtitle = "Original DAG") +
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-439)  theme_do_calc()
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-440)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-441)plot_rule3_g_alt_modified <- ggplot(rule3_g_alt_modified, 
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-442)                                    aes(x = x, y = y, 
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-443)                                        xend = xend, yend = yend)) +
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-444)  geom_dag_edges() +
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-445)  geom_dag_point(color = "grey80", size = 10) +
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-446)  geom_dag_text() +
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-447)  labs(title = TeX("$G_{\\bar{X}, \\bar{Z(W)}}$"),
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-448)       subtitle = "DAG with arrows *into* Z deleted as long as Z isn't an<br>ancestor of W + all arrows *into* X deleted") +
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-449)  theme_do_calc()
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-450)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-451)plot_rule3_g_alt | plot_rule3_g_alt_modified
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-452)```
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-453)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-454)Phew. In this case, our DAG surgery for making the modified graph $G_{\overline{X}, \overline{Z(W)}}$ actually ended up completely d-separating Z from all nodes. Because Z isn't an ancestor of W (but is instead a descendant), we get to delete arrows going into it, and we get to delete arrows going into X as well. We can remove $\operatorname{do}(z)$ from the equation as long as $Y \perp Z \mid W, X$ in this modified graph. That is most definitely the case here. And once again, code confirms it (ignore the 0s here—they're only there so that the DAG plots correctly):
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-455)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-456)```{r independencies-rule3-alt}
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-457)impliedConditionalIndependencies(rule3_g_alt_modified)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-458)```
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-459)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-460)And once again, we can legally get rid of $\operatorname{do}(z)$:
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-461)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-462)$$
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-463)P(y \mid \operatorname{do}(z), \operatorname{do}(x), w) = P(y \mid \operatorname{do}(x), w)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-464)$$
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-465)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-466)### Summary
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-467)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-468)Phew. Let's look back at the three main rules and add their corresponding mathy versions, which should make more sense now:
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-469)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-470)- **Rule 1**: Decide if we can ignore an observation
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-471)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-472)  $$
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-473)  P(y \mid z, \operatorname{do}(x), w) = P(y \mid \operatorname{do}(x), w) \qquad \text{ if } (Y \perp Z \mid W, X)_{G_{\overline{X}}}
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-474)  $$
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-475)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-476)- **Rule 2**: Decide if we can treat an intervention as an observation
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-477)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-478)  $$
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-479)  P(y \mid \operatorname{do}(z), \operatorname{do}(x), w) = P(y \mid z, \operatorname{do}(x), w) \qquad \text{ if } (Y \perp Z \mid W, X)_{G_{\overline{X}, \underline{Z}}}
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-480)  $$
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-481)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-482)- **Rule 3**: Decide if we can ignore an intervention
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-483)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-484)  $$
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-485)  P(y \mid \operatorname{do}(z), \operatorname{do}(x), w) = P(y \mid \operatorname{do}(x), w) \qquad \text{ if } (Y \perp Z \mid W, X)_{G_{\overline{X}, \overline{Z(W)}}}
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-486)  $$
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-487)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-488)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-489)## Deriving the backdoor adjustment formula from *do*-calculus rules
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-490)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-491)That was a lot of math, but hopefully each of these *do*-calculus rules make sense in isolation now. Now that I finally understand what each of these are doing, we can apply these rules to see where the pre-derived / canned backdoor adjustment formula comes from. Somehow by applying these rules, we can transform the left-hand side of this formula into the *do*-free right-hand side:
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-492)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-493)$$
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-494)P(y \mid \operatorname{do}(x)) = \sum_z P(y \mid x, z) \times P(z)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-495)$$
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-496)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-497)Let's go through the derivation of the backdoor adjustment formula step-by-step to see how it works. We'll use this super simple DAG that shows the causal effect of treatment X on outcome Y, confounded by Z:
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-498)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-499)```{r basic-backdoor-dag, fig.width=4, fig.height=3, out.width="60%"}
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-500)backdoor_g <- dagify(
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-501)  Y ~ X + Z,
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-502)  X ~ Z,
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-503)  coords = list(x = c(Y = 2, X = 1, Z = 1.5),
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-504)                y = c(Y = 1, X = 1, Z = 2))
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-505))
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-506)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-507)plot_backdoor_g <- ggplot(backdoor_g, aes(x = x, y = y, 
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-508)                                          xend = xend, yend = yend)) +
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-509)  geom_dag_edges() +
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-510)  geom_dag_point(color = "grey80", size = 10) +
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-511)  geom_dag_text() +
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-512)  labs(title = TeX("$G$"),
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-513)       subtitle = "Basic backdoor confounding") +
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-514)  theme_do_calc()
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-515)plot_backdoor_g
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-516)```
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-517)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-518)### Marginalizing across $z$
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-519)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-520)We're interested in the causal effect of X on Y, or $P(y \mid \operatorname{do}(x))$. If this were an experiment like a randomized controlled trial, we'd be able to delete all arrows going into X, which would remove all confounding from Z and allow us to measure the exact causal effect of X on Y. However, with observational data, we can't delete arrows like that. But, we can condition the X → Y relationship on Z, given that it influences both X and Y.
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-521)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-522)We thus need to calculate the joint probability of $P(y \mid \operatorname{do}(x))$ across all values of Z. Using the rules of [probability marginalization](https://en.wikipedia.org/wiki/Marginal_distribution) and [the chain rule for joint probabilities](https://en.wikipedia.org/wiki/Chain_rule_(probability)), we can write this joint probability like so:
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-523)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-524)$$
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-525)P(y \mid \operatorname{do}(x)) = \sum_z P(y \mid \operatorname{do}(x), z) \times P(z \mid \operatorname{do}(x))
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-526)$$
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-527)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-528)The right-hand side of that equation is what we want to be able to estimate using only observational data, but right now it has two $\operatorname{do}(\cdot)$ operators in it, marked in <span style="color:#FF4136;">red</span> and <span style="color:#B10DC9;">purple</span>:
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-529)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-530)$$
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-531)\sum_z P(y \mid {\color{#FF4136} \operatorname{do}(x)}, z) \times P(z \mid {\color{#B10DC9} \operatorname{do}(x)})
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-532)$$
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-533)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-534)We need to get rid of those.
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-535)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-536)### Applying Rule 2
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-537)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-538)First let's get rid of the <span style="color:#FF4136;">red</span> $\color{#FF4136} \operatorname{do}(x)$ that's in $P(y \mid {\color{#FF4136} \operatorname{do}(x)}, z)$. This chunk of the equation involves all three variables: treatment, outcome, and confounder. Accordingly, we don't really want to ignore any of these variables by using something like Rule 1 or Rule 3. Instead, we can try to treat that $\color{#FF4136} \operatorname{do}(x)$ as an observational $\color{#FF4136} x$ using Rule 2.
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-539)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-540)According to Rule 2, we can treat an interventional $\operatorname{do}(\cdot)$ operator as observational if we meet specific criteria in a modified graph where we remove all arrows out of X:
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-541)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-542)$$
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-543)P(y \mid {\color{#FF4136} \operatorname{do}(x)}, z) = P(y \mid {\color{#FF4136} x}, z) \qquad \text{ if } (Y \perp X \mid Z)_{G_{\underline{X}}}
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-544)$$
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-545)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-546)Here's the modified $G_{\underline{X}}$ graph:
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-547)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-548)```{r backdoor-rule2, fig.width=8, fig.height=3, out.width="100%"}
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-549)#| column: page-inset-right
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-550)backdoor_g_underline_x <- dagify(
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-551)  Y ~ Z,
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-552)  X ~ Z,
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-553)  coords = list(x = c(Y = 2, X = 1, Z = 1.5),
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-554)                y = c(Y = 1, X = 1, Z = 2))
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-555))
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-556)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-557)plot_backdoor_g_underline_x <- ggplot(backdoor_g_underline_x, 
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-558)                                      aes(x = x, y = y, 
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-559)                                          xend = xend, yend = yend)) +
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-560)  geom_dag_edges() +
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-561)  geom_dag_point(color = "grey80", size = 10) +
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-562)  geom_dag_text() +
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-563)  labs(title = TeX("$G_{\\underline{X}}$"),
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-564)       subtitle = "DAG with arrows *out of* X deleted") +
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-565)  theme_do_calc()
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-566)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-567)plot_backdoor_g | plot_backdoor_g_underline_x
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-568)```
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-569)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-570)Following Rule 2, we can treat $\color{#FF4136} \operatorname{do}(x)$ like a regular observational $\color{#FF4136} x$ as long as X and Y are d-separated in this modified $G_{\underline{X}}$ graph when conditioning on Z. And that is indeed the case: there's no direct arrow between X and Y, and by conditioning on Z, there's no active pathway between X and Y through Z. Let's see if code backs us up:
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-571)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-574)```{r}
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-575)impliedConditionalIndependencies(backdoor_g_underline_x)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-576)```
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-577)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-578)Perfect! Because $Y \perp X \mid Z$, we can treat $\color{#FF4136} \operatorname{do}(x)$ like $\color{#FF4136} x$.
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-579)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-580)### Applying Rule 3
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-581)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-582)After applying Rule 2 to the first chunk of the equation, we're still left with the <span style="color:#B10DC9;">purple</span> $\color{#B10DC9} \operatorname{do}(x)$ in the second chunk:
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-583)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-584)$$
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-585)\sum_z P(y \mid {\color{#FF4136} x}, z) \times P(z \mid {\color{#B10DC9} \operatorname{do}(x)})
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-586)$$
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-587)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-588)This second chunk doesn't have the outcome $y$ in it and instead refers only to the treatment and confounder. Since it's not connected with the outcome, it would be neat if we could get rid of that $\color{#B10DC9} \operatorname{do}(x)$ altogether. That's what Rule 3 is for—ignoring interventions.
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-589)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-590)According to Rule 3, we can remove a $\operatorname{do}(\cdot)$ operator as long as it doesn't influence the outcome through any uncontrolled or unconditioned path in a modified graph. Because we're dealing with a smaller number of variables here, the math for Rule 3 is a lot simpler:
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-591)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-592)$$
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-593)P(z \mid {\color{#B10DC9} \operatorname{do}(x)}) = P(z \mid {\color{#B10DC9} \text{nothing!}}) \qquad \text{ if } (X \perp Z)_{G_{\overline{X}}}
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-594)$$
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-595)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-596)Here's the simplified $G_{\overline{X}}$ graph:
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-597)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-598)```{r backdoor-rule3, fig.width=8, fig.height=3, out.width="100%"}
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-599)#| column: page-inset-right
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-600)backdoor_g_overline_x <- dagify(
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-601)  Y ~ X + Z,
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-602)  coords = list(x = c(Y = 2, X = 1, Z = 1.5),
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-603)                y = c(Y = 1, X = 1, Z = 2))
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-604))
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-605)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-606)plot_backdoor_g_overline_x <- ggplot(backdoor_g_overline_x, 
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-607)                                     aes(x = x, y = y, 
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-608)                                         xend = xend, yend = yend)) +
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-609)  geom_dag_edges() +
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-610)  geom_dag_point(color = "grey80", size = 10) +
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-611)  geom_dag_text() +
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-612)  labs(title = TeX("$G_{\\bar{X}}$"),
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-613)       subtitle = "DAG with arrows *into* X deleted") +
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-614)  theme_do_calc()
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-615)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-616)plot_backdoor_g | plot_backdoor_g_overline_x
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-617)```
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-618)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-619)As long as X and Z are d-separated and independent, we can remove that $\color{#B10DC9} \operatorname{do}(x)$ completely. According to this graph, there's no direct arrow connecting them, and there's no active pathway through Y, since Y is a collider in this case and doesn't pass on causal association. As always, let's verify with code:
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-620)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-623)```{r}
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-624)impliedConditionalIndependencies(backdoor_g_overline_x)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-625)```
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-626)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-627)Huzzah! $X \perp Z$, which means we can nuke the $\color{#B10DC9} \operatorname{do}(x)$.
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-628)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-629)### Final equation
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-630)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-631)After marginalizing across $z$, applying Rule 2, and applying Rule 3, we're left with the following formula for backdoor adjustment:
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-632)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-633)$$
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-634)P(y \mid \operatorname{do}(x)) = \sum_z P(y \mid x, z) \times P(z)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-635)$$
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-636)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-637)That's exactly the same formula as the general backdoor adjustment formula—we successfully derived it using *do*-calculus rules!
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-638)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-639)Most importantly, there are no $\operatorname{do}(\cdot)$ operators anywhere in this equation, making this estimand completely *do*-free and estimable using non-interventional observational data! As long as we close the backdoor confounding by adjusting for Z (however you want, like through inverse probability weighting, matching, fancy machine learning stuff, or whatever else—see [this chapter](https://www.andrewheiss.com/research/chapters/heiss-causal-inference-2021/), or [this blog post](https://www.andrewheiss.com/blog/2020/02/25/closing-backdoors-dags/), or [this guide](https://evalf21.classes.andrewheiss.com/example/matching-ipw/) for examples of how to do this), we can estimate the causal effect of X on Y (or $P(y \mid \operatorname{do}(x))$) with only observational data.
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-640)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-641)Here's the derivation all at once:
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-642)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-643)$$
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-644)\begin{aligned}
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-645)& [\text{Marginalization across } z + \text{chain rule for conditional probabilities}] \\
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-646)P(y \mid \operatorname{do}(x)) =& \sum_z P(y \mid {\color{#FF4136} \operatorname{do}(x)}, z) \times P(z \mid {\color{#B10DC9} \operatorname{do}(x)}) \\
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-647)& [\text{Use Rule 2 to treat } {\color{#FF4136} \operatorname{do}(x)} \text{ as } {\color{#FF4136} x}] \\
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-648)=& \sum_z P(y \mid {\color{#FF4136} x}, z) \times P(z \mid {\color{#B10DC9} \operatorname{do}(x)}) \\
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-649)& [\text{Use Rule 3 to nuke } {\color{#B10DC9} \operatorname{do}(x)}] \\
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-650)=& \sum_z P(y \mid {\color{#FF4136} x}, z) \times P(z \mid {\color{#B10DC9} \text{nothing!}}) \\
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-651)& [\text{Final backdoor adjustment formula!}] \\
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-652)=& \sum_z P(y \mid x, z) \times P(z)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-653)\end{aligned}
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-654)$$
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-655)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-656)That's so so cool!
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-657)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-658)The frontdoor adjustment formula can be derived in a similar process—see [the end of this post for an example](https://stephenmalina.com/post/2020-03-09-front-door-do-calc-derivation/#fn:1) (with that, you apply Rules 2 and 3 repeatedly until all the $\operatorname{do}(\cdot)$ operators disappear)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-659)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-660)And in cases where there's no pre-derived backdoor or frontdoor adjustment formula, you can still apply these three *do*-calculus rules to attempt to identify the relationship between X and Y. Not all DAGs are fully estimable, but if they are estimable, the rules of *do*-calculus can be applied to derive the estimate. Fancier tools like [Causal Fusion](https://causalfusion.net/) help with this and automate the process.
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-661)
[](https://www.andrewheiss.com/blog/2021/09/07/do-calculus-backdoors/#cb24-662)## References

```

2007–2025 Andrew Heiss All content licensed under  
[ Creative Commons CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)
**ORCID** [0000-0002-3948-3914](https://orcid.org/0000-0002-3948-3914) [PGP public key](https://www.andrewheiss.com/pgp_ath.asc.txt) Fingerprint:  
4AA2 FA83 A8B2 05A4 E30F  
610D 1382 6216 9178 36AB
Made with and [Quarto](https://quarto.org/) [View the source at GitHub](https://github.com/andrewheiss/ath-quarto)

