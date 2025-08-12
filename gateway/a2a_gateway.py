from fastapi import FastAPI, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, List, Optional
import uuid
import json
import os
from datetime import datetime

app = FastAPI(title="A2A Gateway")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Data models
class AgentCard(BaseModel):
    id: str
    name: str
    capabilities: List[str]
    endpoint: str
    description: Optional[str] = None

class Task(BaseModel):
    to: str
    intent: str
    inputs: Dict
    from_agent: str = "user"

class TaskResult(BaseModel):
    status: str
    artifacts: Optional[List[Dict]] = None
    logs: Optional[List[str]] = None
    error: Optional[str] = None

# In-memory storage
agents: Dict[str, AgentCard] = {}
tasks: Dict[str, Dict] = {}
messages: List[Dict] = []

# File-based message logger (append-only JSON Lines)
LOG_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
LOG_PATH = os.path.join(LOG_DIR, "messages.log")

def ensure_log_dir():
    try:
        os.makedirs(LOG_DIR, exist_ok=True)
    except Exception:
        pass

def log_message_event(message: Dict):
    ensure_log_dir()
    enriched = {
        **message,
        "_logged_at": datetime.utcnow().isoformat() + "Z",
    }
    try:
        with open(LOG_PATH, "a") as log_file:
            log_file.write(json.dumps(enriched, ensure_ascii=False) + "\n")
    except Exception:
        # Logging should never break message flow
        pass

@app.get("/health")
def health_check():
    return {"status": "healthy", "agents": len(agents), "tasks": len(tasks)}

@app.get("/agents")
def list_agents():
    return list(agents.values())

@app.post("/agents/register")
def register_agent(agent: AgentCard):
    agents[agent.id] = agent
    return {"ok": True, "agent_id": agent.id}

@app.post("/tasks")
async def submit_task(task: Task):
    task_id = f"t-{uuid.uuid4().hex[:12]}"
    
    if task.to not in agents:
        raise HTTPException(status_code=404, detail="Unknown agent")
    
    # Store task
    tasks[task_id] = {
        "id": task_id,
        "to": task.to,
        "intent": task.intent,
        "inputs": task.inputs,
        "from_agent": task.from_agent,
        "status": "queued",
        "logs": [],
        "result": None
    }
    
    return {"task_id": task_id}

@app.get("/tasks/{task_id}")
def get_task(task_id: str):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    return tasks[task_id]

@app.post("/tasks/{task_id}/result")
def submit_task_result(task_id: str, result: TaskResult):
    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")
    
    tasks[task_id].update(result.dict())
    return {"ok": True}

# Message endpoints for Alice and Bob
@app.post("/messages")
async def send_message(message: Dict, request: Request):
    # Enrich with meta: who sent the HTTP request (remote addr)
    client_host = request.client.host if request and request.client else None
    enriched = {**message, "_remote_addr": client_host}
    messages.append(enriched)
    log_message_event(enriched)
    return {"status": "sent"}

@app.get("/messages")
def get_messages(receiver: str):
    return {"messages": [m for m in messages if m["receiver"] == receiver]}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
