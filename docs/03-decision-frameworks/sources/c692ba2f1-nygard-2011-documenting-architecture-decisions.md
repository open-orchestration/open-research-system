[ ![Cognitect Blog](https://cognitect.com/assets/images/cognitect-nubank-logo.svg) ](https://cognitect.com/)
[Technologies](https://cognitect.com/technologies.html) [Blog](https://cognitect.com/blog/) [Cognicast](https://cognitect.com/cognicast) [Contact](https://cognitect.com/contact.html) [Archive](https://cognitect.com/archive.html)
[All Topics](https://cognitect.com/blog/index.html) -  [How We Work](https://cognitect.com/blog/how-we-work.html) -  [Events](https://cognitect.com/blog/events.html) -  [Customer Stories](https://cognitect.com/blog/customer-stories.html) -  [Technology](https://cognitect.com/blog/technology.html) -  [Testing](https://cognitect.com/blog/testing.html) -  [The New Normal](https://cognitect.com/blog/the-new-normal.html) -  [Open Source](https://cognitect.com/blog/open-source.html) -  -  [RSS Feed](https://cognitect.com/feed.xml)
[ ![](https://cognitect.com/assets/Authors/MichaelNygard.jpg) ](https://cognitect.com/authors/MichaelNygard.html)
Documenting Architecture Decisions
[Michael Nygard](https://cognitect.com/authors/MichaelNygard.html) - November 15, 2011 
[agility](https://cognitect.com/blog/tags?tag=agility) [architecture](https://cognitect.com/blog/tags?tag=architecture)
# Context
Architecture for agile projects has to be described and defined differently. Not all decisions will be made at once, nor will all of them be done when the project begins.
Agile methods are not opposed to documentation, only to valueless documentation. Documents that assist the team itself can have value, but only if they are kept up to date. Large documents are never kept up to date. Small, modular documents have at least a chance at being updated.
Nobody ever reads large documents, either. Most developers have been on at least one project where the specification document was larger (in bytes) than the total source code size. Those documents are too large to open, read, or update. Bite sized pieces are easier for for all stakeholders to consume.
One of the hardest things to track during the life of a project is the motivation behind certain decisions. A new person coming on to a project may be perplexed, baffled, delighted, or infuriated by some past decision. Without understanding the rationale or consequences, this person has only two choices:
  1. **Blindly accept the decision.**
This response may be OK, if the decision is still valid. It may not be good, however, if the context has changed and the decision should really be revisited. If the project accumulates too many decisions accepted without understanding, then the development team becomes afraid to change anything and the project collapses under its own weight.
  2. **Blindly change it.**
Again, this may be OK if the decision needs to be reversed. On the other hand, changing the decision without understanding its motivation or consequences could mean damaging the project's overall value without realizing it. (E.g., the decision supported a non-functional requirement that hasn't been tested yet.)


It's better to avoid either blind acceptance or blind reversal.
# Decision
We will keep a collection of records for "architecturally significant" decisions: those that affect the structure, non-functional characteristics, dependencies, interfaces, or construction techniques.
An architecture decision record is a short text file in a format similar to an Alexandrian pattern. (Though the decisions themselves are not necessarily patterns, they share the characteristic balancing of forces.) Each record describes a set of forces and a single decision in response to those forces. Note that the decision is the central piece here, so specific forces may appear in multiple ADRs.
We will keep ADRs in the project repository under doc/arch/adr-NNN.md
We should use a lightweight text formatting language like Markdown or Textile.
ADRs will be numbered sequentially and monotonically. Numbers will not be reused.
If a decision is reversed, we will keep the old one around, but mark it as superseded. (It's still relevant to know that it _was_ the decision, but is _no longer_ the decision.)
We will use a format with just a few parts, so each document is easy to digest. The format has just a few parts.
**Title** These documents have names that are short noun phrases. For example, "ADR 1: Deployment on Ruby on Rails 3.0.10" or "ADR 9: LDAP for Multitenant Integration"
**Context** This section describes the forces at play, including technological, political, social, and project local. These forces are probably in tension, and should be called out as such. The language in this section is value-neutral. It is simply describing facts.
**Decision** This section describes our response to these forces. It is stated in full sentences, with active voice. "We will …"
**Status** A decision may be "proposed" if the project stakeholders haven't agreed with it yet, or "accepted" once it is agreed. If a later ADR changes or reverses a decision, it may be marked as "deprecated" or "superseded" with a reference to its replacement.
**Consequences** This section describes the resulting context, after applying the decision. All consequences should be listed here, not just the "positive" ones. A particular decision may have positive, negative, and neutral consequences, but all of them affect the team and project in the future.
The whole document should be one or two pages long. We will write each ADR as if it is a conversation with a future developer. This requires good writing style, with full sentences organized into paragraphs. Bullets are acceptable only for visual style, not as an excuse for writing sentence fragments. (Bullets kill people, even PowerPoint bullets.)
# Status
Accepted.
# Consequences
One ADR describes one significant decision for a specific project. It should be something that has an effect on how the rest of the project will run.
The consequences of one ADR are very likely to become the context for subsequent ADRs. This is also similar to Alexander's idea of a pattern language: the large-scale responses create spaces for the smaller scale to fit into.
Developers and project stakeholders can see the ADRs, even as the team composition changes over time.
The motivation behind previous decisions is visible for everyone, present and future. Nobody is left scratching their heads to understand, "What were they thinking?" and the time to change old decisions will be clear from changes in the project's context.
* * *
# Experience Report
You may have noticed that this post is formatted like an ADR itself. We've been using this format on a few of our projects since early August. That's not a very long time in the global sense, but early feedback from both clients and developers has been quite positive. In that time, we've had six to ten developers rotate through projects using ADRs. All of them have stated that they appreciate the degree of context they received by reading them.
ADRs have been especially useful for capturing longer-term intentions. We have several clients who are stabilizing their current systems, but looking toward a larger rearchitecture in the not-too-distant future. By writing these intentions down, we don't inadvertently make those future changes harder.
One potential objection is that keeping these in version control with the code makes them less accessible for project managers, client stakeholders, and others who don't live in version control like the development team does. In practice, our projects almost all live in GitHub private repositories, so we can exchange links to the latest version in master. Since GitHub does markdown processing automatically, it looks just as friendly as any wiki page would.
So far, ADRs are proving to be a useful tool, so we'll keep using them.
# More Reading
Thanks to Philipe Kruchten for discussing the [importance of architecture decisions](http://www.computer.org/portal/web/csdl/doi/10.1109/MS.2009.52). I'm told there is more about them in [Documenting Software Architectures](http://www.sei.cmu.edu/library/abstracts/books/0321552687.cfm) which is near the top of my reading queue.
  
  

[ ![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png) ](http://creativecommons.org/publicdomain/zero/1.0/)   
To the extent possible under law, [ Cognitect, a Nu Holdings, Ltd. company.](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions) has waived all copyright and related or neighboring rights to "Documenting Architecture Decisions". This work is published from:  United States. 
random
recent
[ My Clojure Workflow, Reloaded— ](https://cognitect.com/blog/2013/06/04/clojure-workflow-reloaded) [ Secret Service and Personalized Cracking— ](https://cognitect.com/blog/2005/4/4/secret-service-and-personalized-cracking) [ A Major Datomic Update— ](https://cognitect.com/blog/2016/11/28/a-major-datomic-update) [ Relevance Agile Bibliography— ](https://cognitect.com/blog/2009/7/7/relevance-agile-bibliography) [ Where to Find Cognitects- February Edition— ](https://cognitect.com/blog/2014/01/31/where-to-find-cognitects-february-edition)
[ —Sponsoring Open Source Developers ](https://cognitect.com/blog/2020/12/15/sponsoring-open-source-developers) [ —Cognitect dev-tools ](https://cognitect.com/blog/2020/08/20/Cognitect-dev-tools) [ —Cognitect Joins Nubank ](https://cognitect.com/blog/2020/07/23/Cognitect-Joins-Nubank) [ —Cognitect and PICI ](https://cognitect.com/blog/2020/06/30/cognitect-and-pici) [ —Supporting Open Source Developers ](https://cognitect.com/blog/supporting-open-source-developers)
[Get In Touch](https://cognitect.com/contact.html)
  * ## [Alessandra Sierra](https://cognitect.com/authors/AlessandraSierra.html)
  * ## [Alex Miller](https://cognitect.com/authors/AlexMiller.html)
  * ## [Carin Meier](https://cognitect.com/authors/CarinMeier.html)
  * ## [David Chelimsky](https://cognitect.com/authors/DavidChelimsky.html)
  * ## [David Nolen](https://cognitect.com/authors/DavidNolen.html)
  * ## [Ghadi Shayban](https://cognitect.com/authors/GhadiShayban.html)
  * ## [Jeb Beich](https://cognitect.com/authors/JebBeich.html)
  * ## [Justin Gehtland](https://cognitect.com/authors/JustinGehtland.html)
  * ## [Lynn Grogan](https://cognitect.com/authors/LynnGrogan.html)
  * ## [Marc Phillips](https://cognitect.com/authors/MarcPhillips.html)
  * ## [Michael Nygard](https://cognitect.com/authors/MichaelNygard.html)
  * ## [Naoko Higashide](https://cognitect.com/authors/NaokoHigashide.html)
  * ## [Paul de Grandis](https://cognitect.com/authors/PauldeGrandis.html)
  * ## [Rich Hickey](https://cognitect.com/authors/RichHickey.html)
  * ## [Russ Olsen](https://cognitect.com/authors/RussOlsen.html)
  * ## [Stuart Halloway](https://cognitect.com/authors/StuartHalloway.html)
  * ## [Tim Baldridge](https://cognitect.com/authors/TimBaldridge.html)
  * ## [Aaron Bedra](https://cognitect.com/authors/AaronBedra.html)
  * ## [Chris Redinger](https://cognitect.com/authors/ChrisRedinger.html)
  * ## [Craig Andera](https://cognitect.com/authors/CraigAndera.html)
  * ## [Don Mullen](https://cognitect.com/authors/DonMullen.html)
  * ## [Glenn Vanderburg](https://cognitect.com/authors/GlennVanderburg.html)
  * ## [Jared Pace](https://cognitect.com/authors/JaredPace.html)
  * ## [Jason Rudolph](https://cognitect.com/authors/JasonRudolph.html)
  * ## [Jon Distad](https://cognitect.com/authors/JonDistad.html)
  * ## [Larry Karnowski](https://cognitect.com/authors/LarryKarnowski.html)
  * ## [Michael Parenteau](https://cognitect.com/authors/MichaelParenteau.html)
  * ## [Muness Alrubaie](https://cognitect.com/authors/MunessAlrubaie.html)
  * ## [Rob Sanheim](https://cognitect.com/authors/RobSanheim.html)
  * ## [Sam Umbach](https://cognitect.com/authors/SamUmbach.html)
  * ## [Kim Foster](https://cognitect.com/authors/KimFoster.html)
  * ## [Jaret Binford](https://cognitect.com/authors/JaretBinford.html)
  * ## [Joe Smith](https://cognitect.com/authors/JoeSmith.html)
  * ## [Clinton Dreisbach](https://cognitect.com/authors/ClintonDreisbach.html)
  * ## [Tim Ewald](https://cognitect.com/authors/TimEwald.html)
  * ## [Robert Randolph](https://cognitect.com/authors/RobertRandolph.html)
  * ## [Alex Redington](https://cognitect.com/authors/AlexRedington.html)
  * ## [Joe Lane](https://cognitect.com/authors/JoeLane.html)
  * ## [Christian Romney](https://cognitect.com/authors/ChristianRomney.html)


  * Nu International
    * [About Nu ](https://international.nubank.com.br/about)
    * [Careers ](https://international.nubank.com.br/careers)
    * [Newsroom ](https://international.nubank.com.br/newsroom)
    * [Investor Relations ](https://www.investidores.nu/en/)
  * Nu Impact
    * [Enviromental ](https://international.nubank.com.br/impact/environmental)
    * [Social ](https://international.nubank.com.br/impact/social)
    * [Governance ](https://international.nubank.com.br/impact/governance/)
  * Global Presence
    * [Brazil ](https://nubank.com.br)
    * [Mexico ](https://nu.com.mx)
    * [Colombia ](https://nu.com.co)
    * [Argentina ](https://nu.com.ar)
  * Blogs
    * [Building Nubank ](https://building.nubank.com.br/)
    * [Brazil ](https://blog.nubank.com.br/)
    * [Mexico ](https://blog.nu.com.mx/)
    * [Colombia ](https://blog.nu.com.co/)


Copyright 2025, Cognitect, a Nu Holdings, Ltd. company | [privacy-policy](https://cognitect.com/privacy-policy.html) | [ Github](https://github.com/cognitect)

