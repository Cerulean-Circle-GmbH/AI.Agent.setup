# Cursor A2A Starter

This is a minimal reference implementation to enable **agent-to-agent**-style communication
inside **Cursor** using a small **Gateway**, a **Background Agent shim**, and an **MCP server**
the **active chat** can call.

## Structure
- `gateway/` — routes TaskRequests to background agents and stores TaskResults
- `bg-agent/` — example background agent that registers an Agent Card and executes tasks
- `mcp-server/` — exposes two MCP tools: `a2a_send_task`, `a2a_get_result`

## Requirements
- Node.js 18+
- npm

## Quick start

```bash
# 1) Install deps for all packages
npm -w gateway i
npm -w bg-agent i
npm -w mcp-server i

# 2) Start the gateway
npm -w gateway run start

# 3) In another terminal, start the background agent
npm -w bg-agent run start

# 4) (In Cursor) add MCP server config similar to:
#   Settings → MCP → Add new server
#   command: node
#   args: mcp-server/index.js
#   env:   GATEWAY=http://localhost:8080
#
# Then from the active chat, call tools:
#   a2a_send_task { "agent_id":"bg.refactorer", "intent":"edit_code",
#                   "inputs":{"path":"src/payments","goal":"extract PaymentService"} }
#   → returns { "task_id":"..." }
#   a2a_get_result { "task_id":"..." }
```

> Replace the TODO in `bg-agent/index.js` with your Cursor Background Agent job launcher.
