import express from "express";
import cors from "cors";

const GATEWAY = process.env.GATEWAY || "http://localhost:8080";
const PORT = process.env.PORT || 8091;
const AGENT_ID = process.env.AGENT_ID || "bg.refactorer";

const app = express();
app.use(cors());
app.use(express.json());

async function register() {
  const r = await fetch(`${GATEWAY}/agents/register`, {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify({
      id: AGENT_ID,
      name: "Refactorer",
      capabilities: ["edit_code", "run_tests"],
      endpoint: `http://localhost:${PORT}`
    })
  });
  if (!r.ok) {
    console.error("Agent registration failed:", await r.text());
  } else {
    console.log("Registered Agent Card:", AGENT_ID);
  }
}

// Receive TaskRequest
app.post("/task", async (req, res) => {
  const { task_id, intent, inputs } = req.body || {};
  console.log("Received task", task_id, intent, inputs);

  // TODO: integrate with real Cursor Background Agent workflow here.
  // Simulate work:
  await new Promise(r => setTimeout(r, 1000));
  const artifacts = [
    { type: "diff", uri: "git://repo/commit/abc123", summary: "Extracted PaymentService" }
  ];
  const logs = ["Started refactor", "Updated imports", "All tests passed"];

  // Report back
  const rr = await fetch(`${GATEWAY}/tasks/${task_id}/result`, {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify({ artifacts, logs })
  });
  if (!rr.ok) {
    console.error("Posting result failed:", await rr.text());
  }

  res.json({ ok: true });
});

app.listen(PORT, async () => {
  console.log(`BG Agent listening on :${PORT}`);
  await register();
});
