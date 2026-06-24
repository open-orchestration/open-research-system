---
id: d657c1d86
topic: 03-decision-frameworks
title: "Nygard's original five-section ADR template and the decision-log numbering/supersede convention"
status: draft
---

This finding grounds the **original ADR template by its originator, Michael Nygard**
(his 2011 post "Documenting Architecture Decisions") and the **decision-log
numbering / file-naming + supersede convention** operationalized by Nat Pryce's
`adr-tools`. It complements the existing finding decf6989c, which grounds the ADR/MADR
record *format* on adr.github.io and the MADR template — i.e. MADR's *expanded* schema.
That finding flagged two honest gaps: the original Nygard template "is not in the
corpus … only MADR's expanded schema is" and "neither source specifies a file-naming
or numbering scheme for the decision log." This finding closes both by going to the
originating primary (Nygard's own post) and to the canonical reference tool that
implements the numbering/supersede mechanics. The point is to ground the ancestor that
MADR descends from, and to make the Nygard-original-vs-MADR-expanded distinction explicit.

## Provenance note

Nygard's post is the *originating primary by the concept's author* — it is the blog
post that introduced and named the Architecture Decision Record, written by Nygard
himself, not an SEO/marketing aggregator relaying the idea [c692ba2f1]. For "Nygard's
original template" there is no more-primary source. The post is itself formatted as an
ADR [c692ba2f1]. `adr-tools` is the widely-used reference CLI by Nat Pryce; its README
is the canonical operationalization of the numbered-file + supersede mechanism, and its
own `adr init` first record links back to Nygard's article as the conceptual source
[c1601728e]. Where this finding mentions adr.github.io or the MADR template for
contrast, that is non-load-bearing and attributed to the existing finding decf6989c —
the load-bearing claims here rest only on [c692ba2f1] and [c1601728e].

## (a) Nygard's five sections and the status lifecycle

Nygard prescribes a deliberately small format — "a format with just a few parts, so
each document is easy to digest" — with five sections [c692ba2f1]:

- **Title** — a short noun phrase naming the document, e.g. "ADR 1: Deployment on
  Ruby on Rails 3.0.10" or "ADR 9: LDAP for Multitenant Integration" [c692ba2f1].
- **Context** — the forces at play (technological, political, social, and
  project-local). These forces are probably in tension and should be called out as
  such; the language here is value-neutral, simply describing facts [c692ba2f1].
- **Decision** — the response to those forces, stated in full sentences with active
  voice: "We will …" [c692ba2f1].
- **Status** — the decision's lifecycle state (detailed below) [c692ba2f1].
- **Consequences** — the resulting context after applying the decision. *All*
  consequences are listed, "not just the 'positive' ones" — a decision may have
  positive, negative, AND neutral consequences, all of which affect the team and
  project in the future [c692ba2f1].

Nygard also constrains the prose: the whole document should be one or two pages long,
written "as if it is a conversation with a future developer," in full sentences
organized into paragraphs [c692ba2f1].

The **status lifecycle** Nygard defines is: a decision may be "**proposed**" if the
project stakeholders haven't agreed with it yet, or "**accepted**" once it is agreed;
and "[i]f a later ADR changes or reverses a decision, it may be marked as
'**deprecated**' or '**superseded**' with a reference to its replacement" [c692ba2f1].
The superseded state thus carries an explicit pointer to the ADR that replaces it.

## (b) The "architecturally significant" scope criterion and the Alexandrian-pattern framing

Nygard scopes ADRs to "**architecturally significant**" decisions: "those that affect
the structure, non-functional characteristics, dependencies, interfaces, or
construction techniques" [c692ba2f1]. One ADR records one such significant decision for
a specific project — "something that has an effect on how the rest of the project will
run" [c692ba2f1].

He frames the artifact as "a short text file in a format similar to an **Alexandrian
pattern**" — though the decisions themselves are not necessarily patterns, "they share
the characteristic balancing of forces" [c692ba2f1]. Each record describes a set of
forces and a single decision in response to those forces, with the decision as the
central piece; the same force may therefore appear in multiple ADRs [c692ba2f1]. Nygard
extends the pattern-language analogy to consequences: "[t]he consequences of one ADR
are very likely to become the context for subsequent ADRs," mirroring "Alexander's idea
of a pattern language: the large-scale responses create spaces for the smaller scale to
fit into" [c692ba2f1].

## (c) The decision-log numbering / file-naming + supersede convention

Two grounded layers cover this, and they agree on the mechanism while differing on the
exact default directory.

**From Nygard's post itself** [c692ba2f1]: ADRs are kept in the project repository
under `doc/arch/adr-NNN.md`, written in a lightweight text formatting language "like
Markdown or Textile." The numbering rule is explicit: "ADRs will be numbered
sequentially and monotonically. **Numbers will not be reused.**" And on supersession:
"If a decision is reversed, we will keep the old one around, but mark it as superseded.
(It's still relevant to know that it *was* the decision, but is *no longer* the
decision.)" — i.e. the **keep-superseded, don't-delete** rule [c692ba2f1].

**From `adr-tools`** [c1601728e], which operationalizes this convention as a CLI:

- ADRs are stored as **Markdown files** in a project subdirectory; the **default
  directory is `doc/adr`**, though you can specify the directory when you initialise
  the log [c1601728e]. (Note the divergence from Nygard's `doc/arch/` example path
  [c692ba2f1]; both place a numbered Markdown file in a project subdirectory.)
- `adr init <dir>` creates the directory containing the **first ADR**, which "records
  that you are using ADRs to record architectural decisions and **links to Michael
  Nygard's article** on the subject" [c1601728e] — the tool itself attributes the
  concept to Nygard.
- `adr new <title>` creates "a new, **numbered** ADR file" and opens it in your editor
  [c1601728e].
- **Supersede** is `adr new -s 9 <title>`: this "create[s] a new ADR file that is
  flagged as superceding ADR 9, **and changes the status of ADR 9** to indicate that it
  is superceded by the new ADR" [c1601728e]. The supersede link is therefore
  **bidirectional** — the new record points back to ADR 9, and ADR 9's status is
  updated to point forward to its replacement — which is the executable form of
  Nygard's "superseded … with a reference to its replacement" [c692ba2f1] and his
  keep-the-old-one-around rule [c692ba2f1].

## (d) Nygard-original vs MADR-expanded

Nygard's template has exactly **five** sections — Title, Context, Decision, Status,
Consequences [c692ba2f1]. MADR (grounded in the existing finding decf6989c, on
adr.github.io + the MADR template, non-load-bearing here) is a descendant that *expands*
that base. Relative to Nygard's five, MADR adds fields Nygard's original does not have:
**Decision Drivers**, **Considered Options**, a structured **Decision Outcome** in the
"Chosen option … because {justification}" form, **Pros and Cons of the Options** (which
preserves the rejected alternatives), **Confirmation**, and **More Information**, plus
optional YAML frontmatter metadata (`status`, `date`, `decision-makers`, `consulted`,
`informed`) — per decf6989c. In short, Nygard records *the chosen decision and its
consequences*; MADR additionally records *the options that were weighed and the drivers
behind the choice*. Two correspondences are worth naming: MADR's `status` values
(proposed / rejected / accepted / deprecated / "superseded by ADR-0123", per decf6989c)
elaborate Nygard's proposed → accepted → deprecated/superseded lifecycle [c692ba2f1];
and MADR's "superseded by ADR-0123" notation is the same supersede-with-reference idea
Nygard states in prose [c692ba2f1] and `adr-tools` implements bidirectionally
[c1601728e].

## Gaps found

- **Exact zero-padded digit width is not stated in these two sources.** Nygard writes
  the file-name template as `adr-NNN.md` and mandates sequential, monotonic,
  non-reused numbering [c692ba2f1], but does not pin a fixed digit width or zero-padding
  rule. `adr-tools` says only "a new, **numbered** ADR file" without stating the literal
  digit count in its README [c1601728e]. The four-digit "ADR-0123" form appears only in
  the MADR `status` example (per the existing finding decf6989c), not in either source
  grounded here — so the precise zero-padded "NNNN" width remains ungrounded by
  [c692ba2f1]/[c1601728e]. Honest demotion: do not assert a four-digit padding from
  these two primaries.
- **Default directory differs between the two grounded sources.** Nygard's example
  path is `doc/arch/adr-NNN.md` [c692ba2f1]; `adr-tools` defaults to `doc/adr`
  [c1601728e]. Neither is "wrong"; the convention is "a numbered Markdown file in a
  configurable project subdirectory," and the specific default is tool/author-dependent.
- **The exact superseded-status wording that `adr-tools` writes is not quoted in its
  README.** The README states that ADR 9's status is changed "to indicate that it is
  superceded" [c1601728e] but does not give the literal status string it inserts; the
  precise text would require the tool's templates/source, not the README.
