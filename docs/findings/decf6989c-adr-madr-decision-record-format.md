---
id: decf6989c
topic: 03-decision-frameworks
title: "The ADR/MADR decision-record format: what an ADR is, the MADR field schema, and the Nygard lineage"
status: draft
---

# The ADR/MADR decision-record format: what an ADR is, the MADR field schema, and the Nygard lineage

Scoring methods such as Analysis of Competing Hypotheses and weighted multi-criteria
scoring *produce* a decision; they say nothing about how to *record* it so a later
reader can reconstruct the reasons, trade-offs, and consequences. That recording
discipline is a separate artifact with its own vocabulary and template: the
Architectural Decision Record (ADR) and its concrete Markdown form, MADR. This
finding grounds the *format* — what an ADR is, what fields the official MADR
template prescribes and what each is for, and where the format came from — using
the ADR community's own site [cd5366499] and the MADR project's own template
[c6da6f093]. It complements, and deliberately does not repeat, the sibling finding
on ACH and weighted scoring [d1b3c3b4c], which covers the *methods* that arrive at
a choice rather than the *record* that documents it.

## What is an ADR, and what is a decision log?

The ADR community site defines a layered vocabulary [cd5366499]. An **Architectural
Decision (AD)** is "a justified design choice that addresses a functional or
non-functional requirement that is architecturally significant" [cd5366499]. An
**Architecturally Significant Requirement (ASR)** is "a requirement that has a
measurable effect on the architecture and quality of a software and/or hardware
system" [cd5366499]. An **Architectural Decision Record (ADR)** "captures a single
AD and its rationale"; put simply, an ADR "can help you understand the reasons for
a chosen architectural decision, along with its trade-offs and consequences"
[cd5366499]. Crucially, the unit is *one decision plus its rationale* — not a
catalogue of options scored against each other, but the record of a choice and why
it was made.

The site names the collection-level artifact directly: "The collection of ADRs
created and maintained in a project constitute its *decision log*" [cd5366499]. All
of this sits "within the topic of Architectural Knowledge Management (AKM)," and
the site notes the practice generalizes beyond architecture — "ADR usage can be
extended to design and other decisions ('any decision record')" [cd5366499]. That
last clause is the bridge to MADR, whose name (per the template) is "Markdown Any
Decision Records" [c6da6f093] — the same record format applied to any decision, not
only architectural ones.

## What exact fields does the MADR template prescribe, and what is each for?

The official MADR template specifies a precise field schema [c6da6f093]. Optional
**YAML frontmatter metadata** comes first, with four elements: `status` (proposed,
rejected, accepted, deprecated, or "superseded by ADR-0123"), `date` ("when the
decision was last updated"), `decision-makers` ("list everyone involved in the
decision"), `consulted` ("everyone whose opinions are sought (typically
subject-matter experts); and with whom there is a two-way communication"), and
`informed` ("everyone who is kept up-to-date on progress; and with whom there is a
one-way communication") [c6da6f093]. These metadata elements are explicitly marked
optional — "Feel free to remove any of them" [c6da6f093].

The body sections, in the template's order, are [c6da6f093]:

- **Title** — "short title, representative of solved problem and found solution"
  [c6da6f093].
- **Context and Problem Statement** — describe the context and problem "in free
  form using two to three sentences or in the form of an illustrative story," with
  the scope of the decision made explicit [c6da6f093].
- **Decision Drivers** (optional) — a list of drivers, each "for instance, a
  desired software quality, faced concern, constraint or force" [c6da6f093].
- **Considered Options** — a list of option titles [c6da6f093].
- **Decision Outcome** — names the chosen option in the form 'Chosen option:
  "{title}", because {justification}', where the justification may be e.g. "only
  option, which meets k.o. criterion decision driver | which resolves force {force}
  | … | comes out best (see below)" [c6da6f093].
- **Consequences** (optional, nested under Decision Outcome) — a list where each
  entry is tagged "Good, because {positive consequence…}" or "Bad, because
  {negative consequence…}" [c6da6f093].
- **Confirmation** (optional, nested under Decision Outcome) — "Describe how the
  implementation / compliance of the ADR can/will be confirmed," e.g. via "any
  automated or manual fitness function" or "a design/code review or a test with a
  library such as ArchUnit." The template notes that although classified optional,
  Confirmation "is included in many ADRs" [c6da6f093].
- **Pros and Cons of the Options** (optional) — a per-option subsection, each
  listing arguments tagged "Good, because…", "Neutral, because…" (used "if the
  given argument weights neither for good nor bad"), or "Bad, because…"
  [c6da6f093].
- **More Information** (optional) — additional evidence/confidence for the outcome,
  the team agreement, when/how the decision should be realized and "if/when it
  should be re-visited," plus links to other decisions and resources [c6da6f093].

The schema makes the format's intent legible: it records the chosen option **and**
the rejected ones, the drivers that mattered, the explicit justification, and the
good/bad consequences — i.e. rationale and trade-offs, not just the verdict.

## Where did the format come from — the Nygard lineage

The ADR community site supplies the provenance. Under "Background Information" it
states that "[Documenting Architecture Decisions] is the blog post from 2011 by
Michael Nygard that popularized the concept" [cd5366499]. (The site cites Nygard's
post; this finding is grounded on the adr.github.io page, not on Nygard's post
directly — so the attribution is "the ADR community site credits Nygard's 2011 post
with popularizing the concept" [cd5366499].) The site also locates the format in a
broader research lineage: the work in the adr organization "is based on the
guidelines and principles in *Sustainable Architectural Decisions* by Zdun et al.,
for instance the Y-statement format suggested in that article" [cd5366499], and it
points to a WICSA 2015 paper comparing "seven templates" and to a history of
architecture decision recording "since the late 1990[s]" [cd5366499].

The site also states the *motivation* the GitHub adr organization pursues:
"Motivate the need for and benefits of AD capturing and establish a common
vocabulary"; "Strengthen the tooling around ADRs, in support of agile practices as
well as iterative and incremental engineering processes"; and "Provide pointers to
public knowledge in the context of AKM and ADRs" [cd5366499]. So the format exists
to make decisions and their rationale durable and shared — a common vocabulary plus
tooling — rather than to compute which option wins.

## How the record captures rationale and consequences, not just the choice

The defining property of the format, across both sources, is that it preserves
*why* and *what-it-costs*, not merely *what*. The community site says an ADR
captures "a single AD and its rationale" and helps a reader understand "the reasons
for a chosen architectural decision, along with its trade-offs and consequences"
[cd5366499]. The MADR template operationalizes exactly that: the **Decision
Outcome** field forces a written "because {justification}" rather than a bare
choice; the **Consequences** field forces both Good and Bad entries; the **Pros and
Cons of the Options** field preserves the rejected alternatives with their own
arguments; and the **Confirmation** field records how compliance with the decision
will later be checked [c6da6f093]. This is the precise contrast with the scoring
methods in the sibling finding: ACH's matrix and a weighted-criteria total are
machinery for *reaching* a defensible choice [d1b3c3b4c], whereas the ADR/MADR
format is machinery for *recording* a choice — including the discarded options and
the consequences accepted — so the decision log remains auditable over time
[cd5366499][c6da6f093].

## Application — how this engine should record contested judgments

- **Record each resolved judgment as one ADR-style record, append-only.** Keep the
  collection as a decision log [cd5366499]; one record per decision plus its
  rationale, never overwriting prior records — supersession is expressed via the
  `status` field ("superseded by …") rather than deletion [c6da6f093].
- **Always write the justification and both-signed consequences.** Use the MADR
  Decision Outcome ("because …") and Consequences (Good/Bad) fields so the record
  carries trade-offs, not just the verdict [c6da6f093][cd5366499].
- **Preserve the rejected options.** Populate Considered Options and Pros and Cons
  of the Options so a reviewer sees what was weighed, not only what won [c6da6f093].
- **Feed scoring output into the record, don't conflate them.** Where the engine
  uses ACH or weighted scoring to *reach* a judgment [d1b3c3b4c], capture that
  judgment in the ADR/MADR fields; the matrix/score is evidence cited inside More
  Information or Decision Drivers, while the ADR is the durable record [c6da6f093].
- **Capture confirmation.** Use the Confirmation field to state how the engine (or
  a reviewer) will later check the decision still holds [c6da6f093].

## Honest gaps

- **Numbering/sequence conventions are not in these two sources.** The `status`
  example references "ADR-0123" [c6da6f093], implying sequential numbering, but
  neither source specifies a file-naming or numbering scheme for the decision log;
  that would need the ADR templates/tooling pages [cd5366499].
- **The Nygard template itself is not in the corpus.** The community site credits
  Nygard's 2011 post and Mark Richards' series "starting from Nygard's template"
  [cd5366499], but the original Nygard four-field template (context/decision/status/
  consequences) is not grounded here — only MADR's expanded schema is [c6da6f093].
- **No empirical evidence on whether the format improves decisions.** These sources
  define and motivate the format; they do not measure whether maintaining a
  decision log improves decision quality or recall — an open question distinct from
  the (separately documented) evidence debate over ACH in [d1b3c3b4c].
- **Relationship between ADR and the Y-statement/Zdun lineage** is referenced but
  not detailed [cd5366499]; how MADR's fields map onto the Y-statement format is
  unresolved in this corpus.
