import pytest
import requests
import time

# Gateway configuration
GATEWAY_URL = "http://localhost:8000"

def test_alice_sends_message_to_bob():
    """Test that Alice can send a message to Bob through the Gateway"""
    message = {"sender": "Alice", "receiver": "Bob", "content": "Hello Bob!"}
    
    # Send message through Gateway
    response = requests.post(f"{GATEWAY_URL}/messages", json=message)
    assert response.status_code == 200
    assert response.json()["status"] == "sent"

    # Bob retrieves messages from Gateway
    response = requests.get(f"{GATEWAY_URL}/messages?receiver=Bob")
    assert response.status_code == 200
    messages = response.json()["messages"]
    assert any(m["sender"] == "Alice" and m["content"] == "Hello Bob!" for m in messages)

def test_bob_sends_message_to_alice():
    """Test that Bob can send a message to Alice through the Gateway"""
    message = {"sender": "Bob", "receiver": "Alice", "content": "Hi Alice!"}
    
    # Send message through Gateway
    response = requests.post(f"{GATEWAY_URL}/messages", json=message)
    assert response.status_code == 200
    assert response.json()["status"] == "sent"

    # Alice retrieves messages from Gateway
    response = requests.get(f"{GATEWAY_URL}/messages?receiver=Alice")
    assert response.status_code == 200
    messages = response.json()["messages"]
    assert any(m["sender"] == "Bob" and m["content"] == "Hi Alice!" for m in messages)

def test_gateway_health():
    """Test that the Gateway is running and healthy"""
    response = requests.get(f"{GATEWAY_URL}/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert "agents" in data
    assert "tasks" in data
