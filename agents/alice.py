from fastapi import FastAPI, Request
import httpx
import asyncio

app = FastAPI()

# Gateway configuration
GATEWAY_URL = "http://localhost:8000"
AGENT_ID = "alice"
AGENT_NAME = "Alice"
AGENT_ENDPOINT = "http://localhost:8001"  # Alice's own endpoint

@app.on_event("startup")
async def startup_event():
    """Register Alice with the A2A Gateway on startup"""
    agent_card = {
        "id": AGENT_ID,
        "name": AGENT_NAME,
        "capabilities": ["send_message", "receive_message"],
        "endpoint": AGENT_ENDPOINT,
        "description": "Alice - A messaging agent that can communicate with Bob"
    }
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(f"{GATEWAY_URL}/agents/register", json=agent_card)
            if response.status_code == 200:
                print(f"✅ Alice registered with Gateway at {GATEWAY_URL}")
            else:
                print(f"❌ Failed to register Alice: {response.text}")
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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
