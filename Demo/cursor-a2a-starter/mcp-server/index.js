import { Server } from "@modelcontextprotocol/sdk/server/index.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

const GATEWAY = process.env.GATEWAY || "http://localhost:8080";

const server = new Server(
  { name: "a2a-mcp", version: "0.1.0" },
  { capabilities: { tools: {} } }
);

server.tool("a2a_send_task", {
  description: "Send a TaskRequest to a background agent via A2A Gateway",
  inputSchema: z.object({
    agent_id: z.string(),
    intent: z.string(),
    inputs: z.record(z.any()),
    from: z.string().default("active.cursor")
  }).passthrough()
}, async (args) => {
  const r = await fetch(`${GATEWAY}/tasks`, {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify({
      to: args.agent_id,
      intent: args.intent,
      inputs: args.inputs,
      from: args.from
    })
  });
  const body = await r.json();
  if (!r.ok) throw new Error(body.error || "task submit failed");
  return { content: [{ type: "text", text: JSON.stringify(body) }] };
});

server.tool("a2a_get_result", {
  description: "Get TaskResult by task_id from A2A Gateway",
  inputSchema: z.object({ task_id: z.string() })
}, async ({ task_id }) => {
  const r = await fetch(`${GATEWAY}/tasks/${task_id}`);
  const body = await r.json();
  if (!r.ok) throw new Error(body.error || "status fetch failed");
  return { content: [{ type: "text", text: JSON.stringify(body) }] };
});

const transport = new StdioServerTransport();
await server.connect(transport);
console.error("a2a-mcp server ready");
