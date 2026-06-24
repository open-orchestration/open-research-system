> ## Documentation Index
> Fetch the complete documentation index at: [/llms.txt](https://modelcontextprotocol.io/llms.txt)
> Use this file to discover all available pages before exploring further.
[Skip to main content](https://modelcontextprotocol.io/specification/2025-06-18/server/tools#content-area)
[Model Context Protocol home page![light logo](https://mintcdn.com/mcp/2BMHnlNW5OqOohXZ/logo/light.svg?fit=max&auto=format&n=2BMHnlNW5OqOohXZ&q=85&s=a5ac61ce77858fb1ddaf6de761c39499)![dark logo](https://mintcdn.com/mcp/2BMHnlNW5OqOohXZ/logo/dark.svg?fit=max&auto=format&n=2BMHnlNW5OqOohXZ&q=85&s=1227cb7feb8344f9f6288c6b5b0a6d80)](https://modelcontextprotocol.io/)
Version 2025-06-18
Search...
⌘KAsk Assistant
  * [Blog](https://blog.modelcontextprotocol.io)
  * [GitHub](https://github.com/modelcontextprotocol)


Search...
Navigation
Server Features
Tools
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
  * [User Interaction Model](https://modelcontextprotocol.io/specification/2025-06-18/server/tools#user-interaction-model)
  * [Capabilities](https://modelcontextprotocol.io/specification/2025-06-18/server/tools#capabilities)
  * [Protocol Messages](https://modelcontextprotocol.io/specification/2025-06-18/server/tools#protocol-messages)
    * [Listing Tools](https://modelcontextprotocol.io/specification/2025-06-18/server/tools#listing-tools)
    * [Calling Tools](https://modelcontextprotocol.io/specification/2025-06-18/server/tools#calling-tools)
    * [List Changed Notification](https://modelcontextprotocol.io/specification/2025-06-18/server/tools#list-changed-notification)
  * [Message Flow](https://modelcontextprotocol.io/specification/2025-06-18/server/tools#message-flow)
  * [Data Types](https://modelcontextprotocol.io/specification/2025-06-18/server/tools#data-types)
    * [Tool](https://modelcontextprotocol.io/specification/2025-06-18/server/tools#tool)
    * [Tool Result](https://modelcontextprotocol.io/specification/2025-06-18/server/tools#tool-result)
    * [Text Content](https://modelcontextprotocol.io/specification/2025-06-18/server/tools#text-content)
    * [Image Content](https://modelcontextprotocol.io/specification/2025-06-18/server/tools#image-content)
    * [Audio Content](https://modelcontextprotocol.io/specification/2025-06-18/server/tools#audio-content)
    * [Resource Links](https://modelcontextprotocol.io/specification/2025-06-18/server/tools#resource-links)
    * [Embedded Resources](https://modelcontextprotocol.io/specification/2025-06-18/server/tools#embedded-resources)
    * [Structured Content](https://modelcontextprotocol.io/specification/2025-06-18/server/tools#structured-content)
    * [Output Schema](https://modelcontextprotocol.io/specification/2025-06-18/server/tools#output-schema)
  * [Error Handling](https://modelcontextprotocol.io/specification/2025-06-18/server/tools#error-handling)
  * [Security Considerations](https://modelcontextprotocol.io/specification/2025-06-18/server/tools#security-considerations)


Server Features
# Tools
Copy page
Copy page
The Model Context Protocol (MCP) allows servers to expose tools that can be invoked by language models. Tools enable models to interact with external systems, such as querying databases, calling APIs, or performing computations. Each tool is uniquely identified by a name and includes metadata describing its schema.
## 
[​](https://modelcontextprotocol.io/specification/2025-06-18/server/tools#user-interaction-model)
User Interaction Model
Tools in MCP are designed to be **model-controlled** , meaning that the language model can discover and invoke tools automatically based on its contextual understanding and the user’s prompts. However, implementations are free to expose tools through any interface pattern that suits their needs—the protocol itself does not mandate any specific user interaction model.
For trust & safety and security, there **SHOULD** always be a human in the loop with the ability to deny tool invocations.Applications **SHOULD** :
  * Provide UI that makes clear which tools are being exposed to the AI model
  * Insert clear visual indicators when tools are invoked
  * Present confirmation prompts to the user for operations, to ensure a human is in the loop


## 
[​](https://modelcontextprotocol.io/specification/2025-06-18/server/tools#capabilities)
Capabilities
Servers that support tools **MUST** declare the `tools` capability:

```
{
  "capabilities": {
    "tools": {
      "listChanged": true
    }
  }
}

```

`listChanged` indicates whether the server will emit notifications when the list of available tools changes.
## 
[​](https://modelcontextprotocol.io/specification/2025-06-18/server/tools#protocol-messages)
Protocol Messages
### 
[​](https://modelcontextprotocol.io/specification/2025-06-18/server/tools#listing-tools)
Listing Tools
To discover available tools, clients send a `tools/list` request. This operation supports [pagination](https://modelcontextprotocol.io/specification/2025-06-18/server/utilities/pagination). **Request:**

```
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/list",
  "params": {
    "cursor": "optional-cursor-value"
  }
}

```

**Response:**

```
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "tools": [
      {
        "name": "get_weather",
        "title": "Weather Information Provider",
        "description": "Get current weather information for a location",
        "inputSchema": {
          "type": "object",
          "properties": {
            "location": {
              "type": "string",
              "description": "City name or zip code"
            }
          },
          "required": ["location"]
        }
      }
    ],
    "nextCursor": "next-page-cursor"
  }
}

```

### 
[​](https://modelcontextprotocol.io/specification/2025-06-18/server/tools#calling-tools)
Calling Tools
To invoke a tool, clients send a `tools/call` request: **Request:**

```
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "tools/call",
  "params": {
    "name": "get_weather",
    "arguments": {
      "location": "New York"
    }
  }
}

```

**Response:**

```
{
  "jsonrpc": "2.0",
  "id": 2,
  "result": {
    "content": [
      {
        "type": "text",
        "text": "Current weather in New York:\nTemperature: 72°F\nConditions: Partly cloudy"
      }
    ],
    "isError": false
  }
}

```

### 
[​](https://modelcontextprotocol.io/specification/2025-06-18/server/tools#list-changed-notification)
List Changed Notification
When the list of available tools changes, servers that declared the `listChanged` capability **SHOULD** send a notification:

```
{
  "jsonrpc": "2.0",
  "method": "notifications/tools/list_changed"
}

```

## 
[​](https://modelcontextprotocol.io/specification/2025-06-18/server/tools#message-flow)
Message Flow
## 
[​](https://modelcontextprotocol.io/specification/2025-06-18/server/tools#data-types)
Data Types
### 
[​](https://modelcontextprotocol.io/specification/2025-06-18/server/tools#tool)
Tool
A tool definition includes:
  * `name`: Unique identifier for the tool
  * `title`: Optional human-readable name of the tool for display purposes.
  * `description`: Human-readable description of functionality
  * `inputSchema`: JSON Schema defining expected parameters
  * `outputSchema`: Optional JSON Schema defining expected output structure
  * `annotations`: optional properties describing tool behavior


For trust & safety and security, clients **MUST** consider tool annotations to be untrusted unless they come from trusted servers.
### 
[​](https://modelcontextprotocol.io/specification/2025-06-18/server/tools#tool-result)
Tool Result
Tool results may contain [**structured**](https://modelcontextprotocol.io/specification/2025-06-18/server/tools#structured-content) or **unstructured** content. **Unstructured** content is returned in the `content` field of a result, and can contain multiple content items of different types:
All content types (text, image, audio, resource links, and embedded resources) support optional [annotations](https://modelcontextprotocol.io/specification/2025-06-18/server/resources#annotations) that provide metadata about audience, priority, and modification times. This is the same annotation format used by resources and prompts.
#### 
[​](https://modelcontextprotocol.io/specification/2025-06-18/server/tools#text-content)
Text Content

```
{
  "type": "text",
  "text": "Tool result text"
}

```

#### 
[​](https://modelcontextprotocol.io/specification/2025-06-18/server/tools#image-content)
Image Content

```
{
  "type": "image",
  "data": "base64-encoded-data",
  "mimeType": "image/png"
  "annotations": {
    "audience": ["user"],
    "priority": 0.9
  }

}

```

This example demonstrates the use of an optional Annotation.
#### 
[​](https://modelcontextprotocol.io/specification/2025-06-18/server/tools#audio-content)
Audio Content

```
{
  "type": "audio",
  "data": "base64-encoded-audio-data",
  "mimeType": "audio/wav"
}

```

#### 
[​](https://modelcontextprotocol.io/specification/2025-06-18/server/tools#resource-links)
Resource Links
A tool **MAY** return links to [Resources](https://modelcontextprotocol.io/specification/2025-06-18/server/resources), to provide additional context or data. In this case, the tool will return a URI that can be subscribed to or fetched by the client:

```
{
  "type": "resource_link",
  "uri": "file:///project/src/main.rs",
  "name": "main.rs",
  "description": "Primary application entry point",
  "mimeType": "text/x-rust",
  "annotations": {
    "audience": ["assistant"],
    "priority": 0.9
  }
}

```

Resource links support the same [Resource annotations](https://modelcontextprotocol.io/specification/2025-06-18/server/resources#annotations) as regular resources to help clients understand how to use them.
Resource links returned by tools are not guaranteed to appear in the results of a `resources/list` request.
#### 
[​](https://modelcontextprotocol.io/specification/2025-06-18/server/tools#embedded-resources)
Embedded Resources
[Resources](https://modelcontextprotocol.io/specification/2025-06-18/server/resources) **MAY** be embedded to provide additional context or data using a suitable [URI scheme](https://modelcontextprotocol.io/specification/2025-06-18/server/resources#common-uri-schemes). Servers that use embedded resources **SHOULD** implement the `resources` capability:

```
{
  "type": "resource",
  "resource": {
    "uri": "file:///project/src/main.rs",
    "mimeType": "text/x-rust",
    "text": "fn main() {\n    println!(\"Hello world!\");\n}",
    "annotations": {
      "audience": ["user", "assistant"],
      "priority": 0.7,
      "lastModified": "2025-05-03T14:30:00Z"
    }
  }
}

```

Embedded resources support the same [Resource annotations](https://modelcontextprotocol.io/specification/2025-06-18/server/resources#annotations) as regular resources to help clients understand how to use them.
#### 
[​](https://modelcontextprotocol.io/specification/2025-06-18/server/tools#structured-content)
Structured Content
**Structured** content is returned as a JSON object in the `structuredContent` field of a result. For backwards compatibility, a tool that returns structured content SHOULD also return the serialized JSON in a TextContent block.
#### 
[​](https://modelcontextprotocol.io/specification/2025-06-18/server/tools#output-schema)
Output Schema
Tools may also provide an output schema for validation of structured results. If an output schema is provided:
  * Servers **MUST** provide structured results that conform to this schema.
  * Clients **SHOULD** validate structured results against this schema.

Example tool with output schema:

```
{
  "name": "get_weather_data",
  "title": "Weather Data Retriever",
  "description": "Get current weather data for a location",
  "inputSchema": {
    "type": "object",
    "properties": {
      "location": {
        "type": "string",
        "description": "City name or zip code"
      }
    },
    "required": ["location"]
  },
  "outputSchema": {
    "type": "object",
    "properties": {
      "temperature": {
        "type": "number",
        "description": "Temperature in celsius"
      },
      "conditions": {
        "type": "string",
        "description": "Weather conditions description"
      },
      "humidity": {
        "type": "number",
        "description": "Humidity percentage"
      }
    },
    "required": ["temperature", "conditions", "humidity"]
  }
}

```

Example valid response for this tool:

```
{
  "jsonrpc": "2.0",
  "id": 5,
  "result": {
    "content": [
      {
        "type": "text",
        "text": "{\"temperature\": 22.5, \"conditions\": \"Partly cloudy\", \"humidity\": 65}"
      }
    ],
    "structuredContent": {
      "temperature": 22.5,
      "conditions": "Partly cloudy",
      "humidity": 65
    }
  }
}

```

Providing an output schema helps clients and LLMs understand and properly handle structured tool outputs by:
  * Enabling strict schema validation of responses
  * Providing type information for better integration with programming languages
  * Guiding clients and LLMs to properly parse and utilize the returned data
  * Supporting better documentation and developer experience


## 
[​](https://modelcontextprotocol.io/specification/2025-06-18/server/tools#error-handling)
Error Handling
Tools use two error reporting mechanisms:
  1. **Protocol Errors** : Standard JSON-RPC errors for issues like:
     * Unknown tools
     * Invalid arguments
     * Server errors
  2. **Tool Execution Errors** : Reported in tool results with `isError: true`:
     * API failures
     * Invalid input data
     * Business logic errors

Example protocol error:

```
{
  "jsonrpc": "2.0",
  "id": 3,
  "error": {
    "code": -32602,
    "message": "Unknown tool: invalid_tool_name"
  }
}

```

Example tool execution error:

```
{
  "jsonrpc": "2.0",
  "id": 4,
  "result": {
    "content": [
      {
        "type": "text",
        "text": "Failed to fetch weather data: API rate limit exceeded"
      }
    ],
    "isError": true
  }
}

```

## 
[​](https://modelcontextprotocol.io/specification/2025-06-18/server/tools#security-considerations)
Security Considerations
  1. Servers **MUST** :
     * Validate all tool inputs
     * Implement proper access controls
     * Rate limit tool invocations
     * Sanitize tool outputs
  2. Clients **SHOULD** :
     * Prompt for user confirmation on sensitive operations
     * Show tool inputs to the user before calling the server, to avoid malicious or accidental data exfiltration
     * Validate tool results before passing to LLM
     * Implement timeouts for tool calls
     * Log tool usage for audit purposes


Was this page helpful?
YesNo
[Resources](https://modelcontextprotocol.io/specification/2025-06-18/server/resources)[Completion](https://modelcontextprotocol.io/specification/2025-06-18/server/utilities/completion)
⌘I
[github](https://github.com/modelcontextprotocol)
Assistant
Responses are generated using AI and may contain mistakes.

