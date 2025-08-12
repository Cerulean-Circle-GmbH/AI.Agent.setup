import express from "express";
import cors from "cors";
import crypto from "node:crypto";

const app = express();
app.use(cors());
app.use(express.json());

/** @typedef {{ id:string, name:string, capabilities:string[], endpoint:string, auth?:{type:'bearer', token:string} }} AgentCard */

const agents = /** @type {Record<string, AgentCard>} */ ({});
const tasks = /** @type {Record<string, any>} */ ({});

// Health
app.get("/healthz", (_, res) => res.json({ ok: true }));

// List agents
app.get("/agents", (_, res) => res.json(Object.values(agents)));

// Register or update an Agent Card
app.post("/agents/register", (req, res) => {
  const card = req.body;
  if (!card?.id || !card?.endpoint) {
    return res.status(400).json({ error: "invalid agent card" });
  }
  agents[card.id] = card;
  res.json({ ok: true });
});

// Submit a task
app.post("/tasks", async (req, res) => {
  const { to, intent, inputs, from } = req.body || {};
  if (!to || !intent) return res.status(400).json({ error: "missing to/intent" });

  const task_id = "t-" + crypto.randomBytes(6).toString("hex");
  tasks[task_id] = { status: "queued", logs: [], result: null, to, intent, inputs, from };

  const agent = agents[to];
  if (!agent) return res.status(404).json({ error: "unknown agent" });

  try {
    const r = await fetch(`${agent.endpoint}/task`, {
      method: "POST",
      headers: {
        "content-type": "application/json",
        ...(agent.auth?.type === "bearer" ? { authorization: `Bearer ${agent.auth.token}` } : {}),
      },
      body: JSON.stringify({ task_id, from, intent, inputs }),
    });
    if (!r.ok) throw new Error(await r.text());
    tasks[task_id].status = "running";
    res.json({ task_id });
  } catch (e) {
    tasks[task_id].status = "failed";
    tasks[task_id].error = String(e);
    res.status(500).json({ error: String(e) });
  }
});

// Get task status/result
app.get("/tasks/:task_id", (req, res) => {
  const t = tasks[req.params.task_id];
  if (!t) return res.status(404).json({ error: "unknown task" });
  res.json(t);
});

// Background agent posts result
app.post("/tasks/:task_id/result", (req, res) => {
  const t = tasks[req.params.task_id];
  if (!t) return res.status(404).json({ error: "unknown task" });
  Object.assign(t, { status: "completed", ...req.body });
  res.json({ ok: true });
});

const PORT = process.env.PORT || 8080;
app.listen(PORT, () => console.log(`A2A Gateway listening on :${PORT}`));
