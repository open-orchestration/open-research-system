> ## Documentation Index
> Fetch the complete documentation index at: [/llms.txt](https://modelcontextprotocol.io/llms.txt)
> Use this file to discover all available pages before exploring further.
[Skip to main content](https://modelcontextprotocol.io/specification/2025-06-18/architecture#content-area)
[Model Context Protocol home page![light logo](https://mintcdn.com/mcp/2BMHnlNW5OqOohXZ/logo/light.svg?fit=max&auto=format&n=2BMHnlNW5OqOohXZ&q=85&s=a5ac61ce77858fb1ddaf6de761c39499)![dark logo](https://mintcdn.com/mcp/2BMHnlNW5OqOohXZ/logo/dark.svg?fit=max&auto=format&n=2BMHnlNW5OqOohXZ&q=85&s=1227cb7feb8344f9f6288c6b5b0a6d80)](https://modelcontextprotocol.io/)
Version 2025-06-18
Search...
⌘KAsk Assistant
  * [Blog](https://blog.modelcontextprotocol.io)
  * [GitHub](https://github.com/modelcontextprotocol)


Search...
Navigation
Architecture
[Documentation](https://modelcontextprotocol.io/docs/getting-started/intro)[Extensions](https://modelcontextprotocol.io/extensions/overview)[Specification](https://modelcontextprotocol.io/specification/2025-06-18)[Registry](https://modelcontextprotocol.io/registry/about)[SEPs](https://modelcontextprotocol.io/seps)[Community](https://modelcontextprotocol.io/community/contributing)
  * [Specification](https://modelcontextprotocol.io/specification/2025-06-18)


  * [Key Changes](https://modelcontextprotocol.io/specification/2025-06-18/changelog)


  * [Architecture](https://modelcontextprotocol.io/specification/2025-06-18/architecture)


### Base Protocol
  * [Overview](https://modelcontextprotocol.io/specification/2025-06-18/basic)
  * [Lifecycle](https://modelcontextprotocol.io/specification/2025-06-18/basic/lifecycle)
  * [Transports](https://modelcontextprotocol.io/specification/2025-06-18/basic/transports)
  * [Authorization](https://modelcontextprotocol.io/specification/2025-06-18/basic/authorization)
  * Utilities


### Client Features
  * [Roots](https://modelcontextprotocol.io/specification/2025-06-18/client/roots)
  * [Sampling](https://modelcontextprotocol.io/specification/2025-06-18/client/sampling)
  * [Elicitation](https://modelcontextprotocol.io/specification/2025-06-18/client/elicitation)


### Server Features
  * [Overview](https://modelcontextprotocol.io/specification/2025-06-18/server)
  * [Prompts](https://modelcontextprotocol.io/specification/2025-06-18/server/prompts)
  * [Resources](https://modelcontextprotocol.io/specification/2025-06-18/server/resources)
  * [Tools](https://modelcontextprotocol.io/specification/2025-06-18/server/tools)
  * Utilities


  * [Schema Reference](https://modelcontextprotocol.io/specification/2025-06-18/schema)


## On this page
  * [Core Components](https://modelcontextprotocol.io/specification/2025-06-18/architecture#core-components)
    * [Host](https://modelcontextprotocol.io/specification/2025-06-18/architecture#host)
    * [Clients](https://modelcontextprotocol.io/specification/2025-06-18/architecture#clients)
    * [Servers](https://modelcontextprotocol.io/specification/2025-06-18/architecture#servers)
  * [Design Principles](https://modelcontextprotocol.io/specification/2025-06-18/architecture#design-principles)
  * [Capability Negotiation](https://modelcontextprotocol.io/specification/2025-06-18/architecture#capability-negotiation)


# Architecture
Copy page
Copy page
The Model Context Protocol (MCP) follows a client-host-server architecture where each host can run multiple client instances. This architecture enables users to integrate AI capabilities across applications while maintaining clear security boundaries and isolating concerns. Built on JSON-RPC, MCP provides a stateful session protocol focused on context exchange and sampling coordination between clients and servers.
## 
[​](https://modelcontextprotocol.io/specification/2025-06-18/architecture#core-components)
Core Components
### 
[​](https://modelcontextprotocol.io/specification/2025-06-18/architecture#host)
Host
The host process acts as the container and coordinator:
  * Creates and manages multiple client instances
  * Controls client connection permissions and lifecycle
  * Enforces security policies and consent requirements
  * Handles user authorization decisions
  * Coordinates AI/LLM integration and sampling
  * Manages context aggregation across clients


### 
[​](https://modelcontextprotocol.io/specification/2025-06-18/architecture#clients)
Clients
Each client is created by the host and maintains an isolated server connection:
  * Establishes one stateful session per server
  * Handles protocol negotiation and capability exchange
  * Routes protocol messages bidirectionally
  * Manages subscriptions and notifications
  * Maintains security boundaries between servers

A host application creates and manages multiple clients, with each client having a 1:1 relationship with a particular server.
### 
[​](https://modelcontextprotocol.io/specification/2025-06-18/architecture#servers)
Servers
Servers provide specialized context and capabilities:
  * Expose resources, tools and prompts via MCP primitives
  * Operate independently with focused responsibilities
  * Request sampling through client interfaces
  * Must respect security constraints
  * Can be local processes or remote services


## 
[​](https://modelcontextprotocol.io/specification/2025-06-18/architecture#design-principles)
Design Principles
MCP is built on several key design principles that inform its architecture and implementation:
  1. **Servers should be extremely easy to build**
     * Host applications handle complex orchestration responsibilities
     * Servers focus on specific, well-defined capabilities
     * Simple interfaces minimize implementation overhead
     * Clear separation enables maintainable code
  2. **Servers should be highly composable**
     * Each server provides focused functionality in isolation
     * Multiple servers can be combined seamlessly
     * Shared protocol enables interoperability
     * Modular design supports extensibility
  3. **Servers should not be able to read the whole conversation, nor “see into” other servers**
     * Servers receive only necessary contextual information
     * Full conversation history stays with the host
     * Each server connection maintains isolation
     * Cross-server interactions are controlled by the host
     * Host process enforces security boundaries
  4. **Features can be added to servers and clients progressively**
     * Core protocol provides minimal required functionality
     * Additional capabilities can be negotiated as needed
     * Servers and clients evolve independently
     * Protocol designed for future extensibility
     * Backwards compatibility is maintained


## 
[​](https://modelcontextprotocol.io/specification/2025-06-18/architecture#capability-negotiation)
Capability Negotiation
The Model Context Protocol uses a capability-based negotiation system where clients and servers explicitly declare their supported features during initialization. Capabilities determine which protocol features and primitives are available during a session.
  * Servers declare capabilities like resource subscriptions, tool support, and prompt templates
  * Clients declare capabilities like sampling support and notification handling
  * Both parties must respect declared capabilities throughout the session
  * Additional capabilities can be negotiated through extensions to the protocol

Each capability unlocks specific protocol features for use during the session. For example:
  * Implemented [server features](https://modelcontextprotocol.io/specification/2025-06-18/server) must be advertised in the server’s capabilities
  * Emitting resource subscription notifications requires the server to declare subscription support
  * Tool invocation requires the server to declare tool capabilities
  * [Sampling](https://modelcontextprotocol.io/specification/2025-06-18/client/sampling) requires the client to declare support in its capabilities

This capability negotiation ensures clients and servers have a clear understanding of supported functionality while maintaining protocol extensibility.
Was this page helpful?
YesNo
[Key Changes](https://modelcontextprotocol.io/specification/2025-06-18/changelog)[Overview](https://modelcontextprotocol.io/specification/2025-06-18/basic)
⌘I
[github](https://github.com/modelcontextprotocol)
Copyright © Model Context Protocol a Series of LF Projects, LLC.  
For web site terms of use, trademark policy and other project policies please see <https://lfprojects.org>.
Assistant
Responses are generated using AI and may contain mistakes.

