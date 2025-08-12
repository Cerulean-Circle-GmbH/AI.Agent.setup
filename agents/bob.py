from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from typing import List, Dict
import httpx
import asyncio

app = FastAPI()

# Gateway configuration
GATEWAY_URL = "http://localhost:8000"
AGENT_ID = "bob"
AGENT_NAME = "Bob"
AGENT_ENDPOINT = "http://localhost:8002"  # Bob's own endpoint

@app.on_event("startup")
async def startup_event():
    """Register Bob with the A2A Gateway on startup"""
    agent_card = {
        "id": AGENT_ID,
        "name": AGENT_NAME,
        "capabilities": ["send_message", "receive_message", "echo", "reverse"],
        "endpoint": AGENT_ENDPOINT,
        "description": "Bob - A messaging agent that can communicate with Alice and perform tasks"
    }
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(f"{GATEWAY_URL}/agents/register", json=agent_card)
            if response.status_code == 200:
                print(f"✅ Bob registered with Gateway at {GATEWAY_URL}")
            else:
                print(f"❌ Failed to register Bob: {response.text}")
    except Exception as e:
        print(f"❌ Could not connect to Gateway: {e}")

@app.post("/send")
async def send_message(request: Request):
    """Send a message through the Gateway"""
    msg = await request.json()
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(f"{GATEWAY_URL}/messages", json=msg)
            if response.status_code == 200:
                return {"status": "sent"}
            else:
                return {"status": "error", "message": response.text}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.get("/messages")
def get_messages(receiver: str):
    """Get messages from the Gateway"""
    try:
        import requests
        response = requests.get(f"{GATEWAY_URL}/messages?receiver={receiver}")
        if response.status_code == 200:
            return response.json()
        else:
            return {"messages": [], "error": response.text}
    except Exception as e:
        return {"messages": [], "error": str(e)}

@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "agent": AGENT_NAME}

# Keep existing endpoints for test compatibility
@app.get("/agent-card")
def agent_card():
    return JSONResponse({
        "id": "agent-b",
        "name": "Agent B",
        "capabilities": ["echo", "reverse"],
        "description": "Performs echo and reverse tasks."
    })

from pydantic import BaseModel

class Task(BaseModel):
    id: str
    type: str
    payload: dict

@app.post("/tasks")
async def handle_task(task: Task):
    if task.type == "echo":
        result = task.payload.get("message", "")
        return {"status": "completed", "artifact": result}
    elif task.type == "reverse":
        result = task.payload.get("message", "")[::-1]
        return {"status": "completed", "artifact": result}
    else:
        return {"status": "error", "message": "Unknown task type"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)
