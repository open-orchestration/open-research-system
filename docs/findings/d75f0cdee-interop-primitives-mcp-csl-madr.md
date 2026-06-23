---
status: draft
topic: 17-specs-standards
id: d75f0cdee
---

# Interoperability primitives for a research engine: what MCP, CSL-JSON, and MADR actually specify

The interoperability layer of a research engine has three distinct seams: how it
**exposes its capabilities to AI clients** (MCP), how it **emits machine-readable
citations** (CSL-JSON / BibTeX), and how it **records its own design decisions**
(MADR/ADR). This finding anchors precise structural claims to each standard's
official specification, so the engine's adapters can be built against the actual
contracts rather than against folklore.

## 1. MCP defines a two-layer protocol with three server-exposed primitives

The Model Context Protocol separates a **data layer** from a **transport layer**:
the data layer is a [JSON-RPC 2.0](https://www.jsonrpc.org/)-based exchange
protocol carrying lifecycle management and the core primitives, while the
transport layer defines the communication channels (connection establishment,
message framing, authorization) — and the same JSON-RPC 2.0 message format is
used across all transport mechanisms [c847773b8]. MCP is a **stateful** protocol
whose lifecycle exists to negotiate the capabilities both client and server
support [c847773b8].

MCP defines three core primitives that *servers* expose:
**Tools** (executable functions an AI application can invoke to perform actions),
**Resources** (data sources providing contextual information), and
**Prompts** (reusable templates that structure interactions with language
models) [c847773b8]. Each primitive type has associated methods for discovery
(`*/list`), retrieval (`*/get`), and — for tools — execution (`tools/call`);
clients use the `*/list` methods to discover available primitives dynamically
[c847773b8].

The tool contract is concrete. A `tools/list` request takes no parameters and
returns a `tools` array; each tool object carries a `name` (unique identifier
within the server's namespace), a `title` (human-readable display name), a
`description`, and an `inputSchema` — a JSON Schema defining the expected input
parameters for type validation [c847773b8]. A `tools/call` request passes
`name` (matching the discovered tool exactly) and `arguments` (conforming to that
`inputSchema`); the response returns a `content` array of typed content objects
(e.g. `{"type": "text", ...}`), supporting multi-format results [c847773b8].
The specification's own navigation organizes the protocol into Base Protocol,
Server Features, and Client Features sections under version `2025-03-26`
[c3b99c089]. A mirror of the docs lists the same concept set — Sampling,
Transport, Tools, Architecture, Prompts, Resources [c91d7e937].

**Implication for the engine:** exposing the corpus and findings over MCP means
modeling read access as **Resources**, search/extraction as **Tools** (each with
an `inputSchema`), and any reusable query scaffolds as **Prompts** — and the
client discovers all of them via the `*/list` methods rather than out-of-band
configuration.

## 2. CSL-JSON is the most structurally programmable citation interchange format

CSL-JSON is the input format consumed by Citation Style Language processors: a
JSON document that is strictly an **array of items**, which any CSL-compliant
engine can render into a formatted citation under a chosen style [c5a6a2462].
Each item object carries an `id` (the equivalent of a BibTeX citation key), a
`type` drawn from a fixed list (e.g. `article-journal`), and a set of variables
such as `title`, `author`, `container-title`, `volume`, `issue`, `page`,
`issued`, and `DOI` [c5a6a2462].

Two structural details matter for an emitter. **Names** are objects with `family`
and `given` (plus optional `suffix`, `non-dropping-particle`,
`dropping-particle`); institutional authors use a single-string `literal` form to
stop the processor from splitting them into a personal name [c5a6a2462].
**Dates** are not free text — `issued` is an object whose `date-parts` is a
nested array (e.g. `{"date-parts": [[2023, 5, 14]]}`) [c5a6a2462]. The GROBID-tools
write-up describes CSL-JSON as winning for interchange because it is plain JSON
with first-class language support, its variables are typed (string, number, name,
date) and consistently named, and it is the format Zotero and many tools use
internally, so round-tripping rarely loses information [c5a6a2462].

A promotional converter blog (twineconvert) describes a feature comparison: it
characterizes BibTeX and RIS as ~40-year-old formats with roughly 30 standard
fields/tags each, against CSL-JSON's ~12 years and 80+ CSL fields, and notes that
across conversions the core fields (title, authors, year, journal, DOI) survive
cleanly while format-specific metadata is lost [cc13e4eb2]. This is a vendor
description, not a standards body, so it is treated as illustrative rather than
authoritative.

The lossy-interchange point is corroborated by Zotero's own knowledge base, which
states that export formats differ in compatibility, that Zotero RDF is the least
lossy (preserving collections, attachment files, and notes), and that RIS or MODS
preserve notes but not attachments or collections [cda819b22]. Zotero publishes
its type/field mappings to CSL and to formats including RIS, MODS, BibTeX,
BibLaTeX, and Dublin Core RDF [cda819b22].

**Implication for the engine:** emit **CSL-JSON as the canonical citation format**
— its typed, named variables and array-of-items shape are directly consumable by
the same JSON tooling the engine already uses, and any required BibTeX/RIS output
should be treated as a downstream, lossy projection rather than a parallel source
of truth.

## 3. MADR specifies a lean, file-based template for recording decisions

An Architectural Decision (AD) is a justified design choice addressing a
requirement of architectural significance; it is captured in an Architectural
Decision Record (ADR) documenting one AD and its rationale, and MADR is a
streamlined Markdown template for recording such decisions in a structured manner
[c83e68685]. The official MADR full template defines a YAML front-matter block
with optional `status` (proposed | rejected | accepted | deprecated | superseded),
`date`, `decision-makers`, `consulted`, and `informed`, followed by a short title
and a mandatory **Context and Problem Statement** section, with **Decision
Drivers** as an optional element [c83e68685].

MADR is deliberately unopinionated about repository layout: it does **not** enforce
any directory organization, and for large projects it documents categorization by
subdirectory (e.g. `decisions/backend/0001-use-quarkus.md`,
`decisions/ui/0001-use-vuejs.md`) as one community option — with the explicit
consequence that ADR numbers are then unique only locally within a category, not
globally [c83e68685].

**Implication for the engine:** the decision log can adopt MADR as-is — numbered
Markdown files with the status/date/context structure — giving each automated or
human decision a versionable, lint-able record without inventing a bespoke schema.

## Convergent vs. contested

- **Convergent (spec-anchored):** All three standards are file-/message-oriented
  and machine-parseable. MCP fixes the JSON-RPC primitive contracts
  [c847773b8]; CSL-JSON fixes the item/variable schema [c5a6a2462]; MADR fixes a
  Markdown record skeleton [c83e68685]. Each is directly implementable as an
  adapter.
- **Contested / vendor-described, not load-bearing:** the relative "field
  richness" ranking of BibTeX vs RIS vs CSL-JSON comes from a converter vendor's
  marketing post [cc13e4eb2] and is reported only as illustration; the
  authoritative interchange-loss claim rests on Zotero's KB [cda819b22].

## Provenance note

MCP claims are anchored to the official `modelcontextprotocol.io` specification
and learn/architecture docs [c3b99c089][c847773b8] plus a docs mirror
[c91d7e937]; MADR claims to the official `adr.github.io/madr` template
[c83e68685]; the lossy-interchange claim to Zotero's documentation [cda819b22].
CSL-JSON structural claims come from a descriptive engineering write-up
[c5a6a2462] but state only what the published CSL schema defines. The single
promotional source [cc13e4eb2] carries no load-bearing claim.
