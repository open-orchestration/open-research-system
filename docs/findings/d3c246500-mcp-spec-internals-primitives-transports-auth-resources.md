---
id: d3c246500
topic: 17-specs-standards
title: "MCP 2025-06-18 spec internals: primitives, transports, OAuth authorization, and Resources as an append-only corpus store"
status: draft
---

This finding grounds the **internals** of the Model Context Protocol (MCP)
specification, version `2025-06-18`, directly on its four official spec pages at
modelcontextprotocol.io: Architecture [c6a01ecb9], Transports [ce4efcb5b],
Authorization [cd2811bcf], and Resources [cfd67269f]. It complements
`d75f0cdee` (interop primitives: MCP, CSL-JSON, MADR), which establishes at a
high level that MCP exposes three server primitives and that the engine should
model read access as Resources, search/extraction as Tools, and query scaffolds
as Prompts. This finding does not re-state that point — it supplies the
spec-level mechanics that point assumes: the exact primitive set and how
capabilities are negotiated, the two standard transports and their tradeoffs,
the OAuth 2.1 authorization model with its named RFCs, and — load-bearing for
the append-only corpus question — the precise URI, listing, subscription, and
notification semantics of Resources.

## (a) Host/client/server model, JSON-RPC, the three server primitives, capability negotiation

MCP follows a **client-host-server** architecture: a host process is the
container and coordinator that creates and manages multiple client instances,
controls connection permissions and lifecycle, enforces security policies and
consent, and coordinates LLM integration and sampling [c6a01ecb9]. Each
**client** is created by the host and maintains an isolated connection with a
**1:1 relationship to a single server**, establishing one stateful session per
server, handling protocol/capability negotiation, and managing subscriptions and
notifications [c6a01ecb9]. **Servers** expose resources, tools, and prompts via
MCP primitives, operate independently with focused responsibilities, and may be
local processes or remote services [c6a01ecb9]. MCP is built on **JSON-RPC** and
is a **stateful session protocol** focused on context exchange and sampling
coordination [c6a01ecb9].

A core design principle constrains information flow: servers **should not be
able to read the whole conversation, nor "see into" other servers** — full
conversation history stays with the host and each server connection is isolated
[c6a01ecb9]. Two other principles: servers should be extremely easy to build
(the host carries orchestration), and highly composable (multiple focused
servers combine over the shared protocol) [c6a01ecb9].

The three primitives **servers** expose are **resources** (data sources
providing contextual information), **tools** (callable functions an AI
application can invoke to perform actions), and **prompts** (reusable templated
messages that structure interactions with language models) [c6a01ecb9]. (The
detailed message shapes for tools and prompts live on separate spec pages not
fully grounded here — see Gaps.)

MCP uses **capability-based negotiation**: clients and servers explicitly
declare supported features during initialization, and capabilities determine
which protocol features and primitives are available for the session
[c6a01ecb9]. Servers declare capabilities like resource subscriptions, tool
support, and prompt templates; clients declare capabilities like sampling
support and notification handling; both parties **must** respect declared
capabilities throughout the session [c6a01ecb9]. Concretely, emitting resource
subscription notifications requires the server to have declared subscription
support, and tool invocation requires the server to have declared tool
capabilities [c6a01ecb9].

## (b) The two standard transports: stdio vs Streamable HTTP

MCP uses JSON-RPC to encode messages, which **MUST** be UTF-8 encoded, and
defines **two standard transport mechanisms** [ce4efcb5b]:

**stdio.** The client launches the MCP server as a **subprocess**; the server
reads JSON-RPC messages from `stdin` and writes them to `stdout`. Messages are
**delimited by newlines and MUST NOT contain embedded newlines** [ce4efcb5b].
The server **MUST NOT** write anything to `stdout` that is not a valid MCP
message, and the client **MUST NOT** write anything to the server's `stdin` that
is not a valid MCP message; the server **MAY** use `stderr` for logging
[ce4efcb5b]. Clients **SHOULD** support stdio whenever possible [ce4efcb5b].
This is the natural fit for a local, co-located server: no network surface, no
session/auth machinery, credentials supplied via environment (see (c)).

**Streamable HTTP.** The server runs as an independent process handling multiple
client connections over HTTP POST and GET, and **MAY** optionally use
**Server-Sent Events (SSE)** to stream multiple server messages [ce4efcb5b].
The server **MUST** provide a single **MCP endpoint** path supporting both POST
and GET (e.g. `https://example.com/mcp`) [ce4efcb5b]. Every client JSON-RPC
message **MUST** be a new HTTP POST to that endpoint, with an `Accept` header
listing both `application/json` and `text/event-stream` [ce4efcb5b]. For a
JSON-RPC response or notification the server **MUST** return **202 Accepted**
with no body when it accepts the input; for a JSON-RPC request the server
**MUST** return either `Content-Type: text/event-stream` (initiating an SSE
stream) or `Content-Type: application/json` (a single JSON object), and the
client **MUST** support both [ce4efcb5b]. This Streamable HTTP transport
**replaces the deprecated HTTP+SSE transport** from protocol version
`2024-11-05` [ce4efcb5b].

Streamable HTTP carries machinery stdio does not need:
- **Session management** — a server **MAY** assign a session ID at
  initialization by including it in an `Mcp-Session-Id` header on the
  `InitializeResult` response; that ID **SHOULD** be globally unique and
  cryptographically secure and **MUST** contain only visible ASCII (0x21–0x7E);
  once issued, clients **MUST** include `Mcp-Session-Id` on subsequent requests
  [ce4efcb5b].
- **Resumability/redelivery** — servers **MAY** attach a per-stream `id` to SSE
  events; on reconnect a client **SHOULD** issue an HTTP GET with `Last-Event-ID`
  so the server can replay messages on that disconnected stream only, never on a
  different stream [ce4efcb5b].
- **Protocol version header** — if using HTTP the client **MUST** send
  `MCP-Protocol-Version: <version>` (e.g. `2025-06-18`) on all subsequent
  requests; absent the header the server **SHOULD** assume `2025-03-26`, and an
  invalid/unsupported version **MUST** get a `400 Bad Request` [ce4efcb5b].

**Security notes (Streamable HTTP).** Servers **MUST** validate the `Origin`
header on all incoming connections to prevent **DNS-rebinding attacks**; when
running locally, servers **SHOULD** bind only to **localhost (127.0.0.1)**
rather than all interfaces (0.0.0.0); and servers **SHOULD** implement proper
authentication [ce4efcb5b]. Without these protections a remote website could
use DNS rebinding to reach a local MCP server [ce4efcb5b].

**Tradeoff summary.** stdio is the low-ceremony, local, single-client,
no-auth path (clients SHOULD prefer it when possible); Streamable HTTP is the
networked, multi-client, optionally-streaming path that adds sessions,
resumability, version negotiation, and the DNS-rebinding/localhost-binding
hardening — and it is the transport to which the OAuth model in (c) applies
[ce4efcb5b].

## (c) Authorization: OAuth 2.1, HTTP-only and optional

Authorization operates **at the transport level** and is defined **only for
HTTP-based transports** [cd2811bcf]. It is **OPTIONAL**: HTTP-transport
implementations **SHOULD** conform to the spec, while **STDIO transports SHOULD
NOT** follow it and instead **retrieve credentials from the environment**
[cd2811bcf]. This cleanly partitions the engine's two deployment modes — a local
stdio server takes secrets from env; a remote HTTP server uses the OAuth flow
below.

**Roles.** A protected **MCP server acts as an OAuth 2.1 resource server** that
accepts and responds to requests bearing access tokens; the **MCP client acts as
an OAuth 2.1 client** making requests on behalf of a resource owner; the
**authorization server** issues access tokens and may be co-hosted with the
resource server or separate [cd2811bcf].

The model is a **selected subset** of four established specs [cd2811bcf]:
- **OAuth 2.1** (IETF draft `draft-ietf-oauth-v2-1-13`) — authorization servers
  **MUST** implement OAuth 2.1 for both confidential and public clients
  [cd2811bcf].
- **OAuth 2.0 Protected Resource Metadata — RFC 9728** — MCP servers **MUST**
  implement it to advertise their authorization server(s); the returned metadata
  document **MUST** include an `authorization_servers` field with at least one
  entry [cd2811bcf].
- **OAuth 2.0 Authorization Server Metadata — RFC 8414** — the AS metadata
  discovery spec on which the flow relies [cd2811bcf].
- **OAuth 2.0 Dynamic Client Registration — RFC 7591** — authorization servers
  and MCP clients **SHOULD** support it [cd2811bcf].

**PKCE.** MCP clients **MUST** implement **PKCE** (OAuth 2.1 §7.5.2) to prevent
authorization-code interception/injection [cd2811bcf].

**Token audience binding (RFC 8707).** MCP servers **MUST** validate that access
tokens were issued specifically for them as the intended audience (RFC 8707 §2),
and **MUST** reject tokens not naming them in the audience; invalid/expired
tokens **MUST** get HTTP 401 [cd2811bcf]. Clients **MUST** include the
`resource` parameter (RFC 8707 Resource Indicators) in authorization and token
requests to name the target resource, and **MUST NOT** send the MCP server any
token other than one issued by that server's authorization server [cd2811bcf].
Error codes: 401 (auth required / token invalid), 403 (invalid scopes /
insufficient permissions), 400 (malformed request) [cd2811bcf].

**Confused-deputy / token-passthrough cautions.** Because an MCP server can act
as an intermediary to third-party APIs, attackers can exploit it as a
**confused deputy**; proxy servers using static client IDs **MUST** obtain user
consent for each dynamically registered client before forwarding to third-party
authorization servers [cd2811bcf]. When an MCP server calls an upstream API it
acts as a separate OAuth client there, and it **MUST NOT pass through** the
token it received from the MCP client — token passthrough is explicitly
forbidden [cd2811bcf]. Authorization-server endpoints **MUST** be served over
HTTPS [cd2811bcf].

## (d) Resources in detail

Each resource is uniquely identified by a **URI (RFC 3986)** [cfd67269f].
Resources are **application-driven**: the host decides how to incorporate
context (explicit user selection, search/filter, or automatic inclusion by
heuristics or model selection), and the protocol mandates no specific
interaction model [cfd67269f].

**Capability.** Servers supporting resources **MUST** declare the `resources`
capability, which exposes two **optional** sub-features [cfd67269f]:
- **`subscribe`** — whether the client can subscribe to be notified of changes
  to *individual* resources.
- **`listChanged`** — whether the server emits notifications when the *list* of
  available resources changes.

A server may support **neither, either, or both** [cfd67269f].

**Protocol messages.**
- **`resources/list`** (paginated, `cursor`/`nextCursor`) returns a `resources`
  array of objects each carrying `uri`, `name`, optional `title`, `description`,
  `mimeType`, and `size` [cfd67269f].
- **`resources/read`** takes a `uri` and returns a `contents` array; each entry
  carries the `uri`, `mimeType`, and either `text` (text content) or binary data
  [cfd67269f].
- **Resource templates** — `resources/templates/list` (paginated) returns
  `resourceTemplates`, each with a `uriTemplate` (**URI Templates, RFC 6570**,
  e.g. `file:///{path}`), enabling parameterized resources [cfd67269f].

**Notifications.**
- **`notifications/resources/list_changed`** — sent by servers that declared
  `listChanged` when the *set of available resources* changes [cfd67269f].
- A client subscribes with **`resources/subscribe`** (params: `uri`); the server
  then sends **`notifications/resources/updated`** (params: `uri`) when *that
  subscribed resource's content* changes [cfd67269f].

**URI schemes.** The protocol defines standard schemes but the list is **not
exhaustive — implementations are free to use additional, custom schemes**
[cfd67269f]. `https://` is for resources the client can fetch directly from the
web on its own; for other cases servers **SHOULD** prefer another or a custom
scheme [cfd67269f]. `file://` identifies filesystem-like resources that need not
map to an actual physical file; `git://` is also listed [cfd67269f].

## (e) Applied: modeling the engine's append-only corpus/findings store as Resources

The engine's premise is an append-only corpus/findings store ("the agent
forgets, the repo remembers"). The spec's Resources primitive supports modeling
this directly; the following is **this finding's synthesis built on the spec's
named mechanics**, not a usage the spec prescribes:

- **Each finding/source as a resource under a custom URI scheme.** Because the
  scheme list is explicitly non-exhaustive and custom schemes are permitted
  [cfd67269f], the engine can expose every finding as `finding://<id>` and every
  source as `corpus://<id>` — each a `uri` per RFC 3986 [cfd67269f], with
  `name`/`title`/`description`/`mimeType` populated from the item's metadata.
- **Discovery via paginated `resources/list`; retrieval via `resources/read`.**
  The whole corpus is enumerable through `resources/list` (cursor pagination
  handles growth), and a finding's body is fetched via `resources/read`
  returning text `contents` [cfd67269f]. **Resource templates** (RFC 6570) let
  the engine advertise a parameterized shape such as `finding://{id}` rather
  than listing every finding statically [cfd67269f].
- **Append maps onto `notifications/resources/list_changed`.** Promoting a new
  finding grows the available-resource set — exactly the event
  `notifications/resources/list_changed` signals (server having declared the
  `listChanged` capability) [cfd67269f]. This matches the append-only model:
  the common write is "a new resource appeared," not "an existing one mutated."
- **The rare in-place change maps onto `subscribe` + `notifications/resources/updated`.**
  When a finding's content does change in place (e.g. its status flips to
  *superseded*), a client that issued `resources/subscribe` on that
  `finding://<id>` receives `notifications/resources/updated` for that URI
  [cfd67269f]. Declaring both `subscribe` and `listChanged` (the spec allows
  both [cfd67269f]) covers append (list grew) and edit (subscribed item updated)
  with distinct, spec-named signals.

The fit is good precisely because append-only stores are list-growth-dominated,
and `list_changed` is the spec's signal for "the available set changed" while
`updated` is reserved for the rarer per-resource content change [cfd67269f].

## Gaps found

- **Tools and Prompts message shapes not fully grounded here.** The exact
  request/response schemas for `tools/*` and `prompts/*` live on separate
  `2025-06-18` server-feature pages not among these four sources; `d75f0cdee`
  grounds the tool contract at a high level but the prompts message shape and
  full tool result schema remain a candidate gap.
- **Security Best Practices and Lifecycle pages referenced but not ingested.**
  The Authorization page defers the confused-deputy/token-passthrough detail to
  a separate `security_best_practices` page, and the transport version-negotiation
  detail to the `lifecycle` page; both are cited but not grounded here.
- **CSL-JSON schema remains a separate gap.** The engine's citation interchange
  format (CSL-JSON) is independent of MCP and is grounded only at a high level in
  `d75f0cdee`; a dedicated CSL-JSON schema grounding is still open.
- **Version pinned at `2025-06-18`.** All claims are tied to this revision (which
  itself replaced the `2024-11-05` HTTP+SSE transport and changes the default
  assumed version to `2025-03-26` absent a header [ce4efcb5b]); newer spec
  revisions may alter primitive shapes, transport mechanics, or the auth model.
