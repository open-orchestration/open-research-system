# ADR Templates | Architectural Decision Records

Source: https://adr.github.io/adr-templates/

[](https://adr.github.io/) [Architectural Decision Records](https://adr.github.io/)
Homepage of the ADR GitHub organization
  * [ HOME ](https://adr.github.io/)
  * [ AD PRACTICES ](https://adr.github.io/ad-practices/)
  * [ ADR TEMPLATES ](https://adr.github.io/adr-templates/)
  * [ DECISION CAPTURING TOOLS ](https://adr.github.io/adr-tooling/)


[ ](https://github.com/adr)
[Home](https://adr.github.io/) ADR Templates
Post
Cancel
# ADR Templates
Posted Oct 24, 2024 Updated May 11, 2026
By _[adr.github.io](https://github.com/adr/adr.github.io) _
_2 min_ read
ADR Templates
Contents
ADR Templates
  * [Markdown Architectural Decision Records (MADR)](https://adr.github.io/adr-templates/#markdown-architectural-decision-records-madr)
  * [Nygard ADR](https://adr.github.io/adr-templates/#nygard-adr)
  * [Y-Statement](https://adr.github.io/adr-templates/#y-statement)
  * [Other ADR templates](https://adr.github.io/adr-templates/#other-adr-templates)


The following UML class diagram shows that many templates for ADR capturing exist, including (but not limited to) MADR, Nygardian ADRs, and Y-Statements:

```
---
  config:
    class:
      hideEmptyMembersBox: true
---
classDiagram
  direction TB
  class ADR {
    <<abstract>>
  }
  ADR <|-- MADR
  ADR <|-- NygardADR
  ADR <|-- Y-Statement
  ADR <|-- OtherADRTemplate

```

```
«abstract»
ADR
MADR
NygardADR
Y-Statement
OtherADRTemplate
```

##  Markdown Architectural Decision Records (MADR)[](https://adr.github.io/adr-templates/#markdown-architectural-decision-records-madr)
MADR is about architectural decisions that _matter_ ([`[ˈmæɾɚ]`](https://en.wiktionary.org/wiki/matter#Pronunciation)). Olaf Zimmermann’s [MADR Template Primer](https://www.ozimmer.ch/practices/2022/11/22/MADRTemplatePrimer.html) covers it in more depth. You can use MADR without installing software by populating the template in any text editor. Additionally, a [VS Code extension](https://marketplace.visualstudio.com/items?itemName=StevenChen.vscode-adr-manager) is available, though it may be outdated and lack support for the latest features. [Other tools](https://adr.github.io/adr-tooling/#madr-template) are also available.
MADR provides a [full](https://github.com/adr/madr/blob/4.0.0/template/adr-template.md?plain=1) and a [minimal](https://github.com/adr/madr/blob/4.0.0/template/adr-template-minimal.md?plain=1) template, both of which now come in an annotated and a bare format. The rationale for this decision is documented in the [template decisions](https://github.com/adr/madr/tree/4.0.0/template#decisions).
We think that the _considered options_ with their pros and cons are crucial to understand the reasons for choosing a particular design. Therefore, the [Markdown Architectural Decision Records (MADR)](https://adr.github.io/madr/) project in this organization includes such tradeoff analysis information. It also suggests metadata such as decision makers and confirmation in addition to decision status.
##  Nygard ADR[](https://adr.github.io/adr-templates/#nygard-adr)
An ADR consists of title, status, context, decision, and consequences according to “Documenting Architecture Decisions” by [@mtnygard](https://github.com/mtnygard).
The original [blog post from 2011](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions) suggests this structure, and a [Markdown rendering](https://github.com/joelparkerhenderson/architecture-decision-record/blob/main/locales/en/templates/decision-record-template-by-michael-nygard/index.md) is also available.
##  Y-Statement[](https://adr.github.io/adr-templates/#y-statement)
In short, the Y-statement is as follows:
> In the context of `<use case/user story>`, facing `<concern>` we decided for `<option>` to achieve `<quality>`, accepting `<downside>`.
The long form of it is as follows (extra section “because”):
> In the context of `<use case/user story>`, facing `<concern>`, we decided for `<option>` and neglected `<other options>`, to achieve `<system qualities/desired consequences>`, accepting `<downside/undesired consequences>`, because `<additional rationale>`.
cards42 has adopted the Y-statement template in its German [ADR card](https://cards42.org#adr); the English version is similar, but adds state information. Finally, you can find more explanations and examples on Medium: [Y-Statements - A Light Template for Architectural Decision Capturing](https://medium.com/@docsoc/y-statements-10eb07b5a177).
##  Other ADR templates[](https://adr.github.io/adr-templates/#other-adr-templates)
Numerous other ADR formats exist, many of which are also featured in [@joelparkerhenderson’s GitHub repository](https://github.com/joelparkerhenderson/architecture_decision_record).
The [template](http://www.iso-architecture.org/42010/templates/) for [ISO/IEC/IEEE 42010:2011](https://en.wikipedia.org/wiki/ISO/IEC_42010), the international standard for architecture descriptions of systems and software emgineering, suggests nine information items for ADRs its Appendix A. It also identifies areas to consider when identifying key decisions.
[adr](https://adr.github.io/categories/adr/)
This post is licensed under [ CC BY 4.0 ](https://creativecommons.org/licenses/by/4.0/) by the author.
Share [ ](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fadr.github.io%2Fadr-templates%2F) [ ](https://bsky.app/intent/compose?text=ADR%20Templates%20-%20Architectural%20Decision%20Records%20https%3A%2F%2Fadr.github.io%2Fadr-templates%2F) [ ](https://www.reddit.com/submit?url=https%3A%2F%2Fadr.github.io%2Fadr-templates%2F&title=ADR%20Templates%20-%20Architectural%20Decision%20Records)
## Recently Updated
  * [Decision Capturing Tools](https://adr.github.io/adr-tooling/)
  * [ADR Templates](https://adr.github.io/adr-templates/)
  * [AD Practices](https://adr.github.io/ad-practices/)


## Contents
### Further Reading
[ Oct 27, 2024Decision Capturing Tools The following lists are rather inclusive and sorted alphabetically. Please find out about the status and the maturity of the list entries for yourself by following the links. Tooling to create an... ](https://adr.github.io/adr-tooling/) [ Oct 26, 2024AD Practices The lists on this page point at ADR capturing practices and related advice but do not necessarily endorse all of them. Timing Architectural Decisions, a presentation given at the annual Swedish I... ](https://adr.github.io/ad-practices/)
-
[AD Practices](https://adr.github.io/ad-practices/)
© 2026 [adr.github.io](https://github.com/adr/adr.github.io). Some rights reserved.
Using the [Chirpy](https://github.com/cotes2020/jekyll-theme-chirpy) theme for [Jekyll](https://jekyllrb.com).
A new version of content is available.
Update 

