import pytest
from fastapi.testclient import TestClient
from agents.bob import app

client = TestClient(app)

def test_agent_card():
    response = client.get("/agent-card")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == "agent-b"
    assert "echo" in data["capabilities"]
    assert "reverse" in data["capabilities"]
    assert "description" in data

def test_task_echo():
    task = {"id": "t1", "type": "echo", "payload": {"message": "hello"}}
    response = client.post("/tasks", json=task)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "completed"
    assert data["artifact"] == "hello"


def test_task_reverse():
    task = {"id": "t2", "type": "reverse", "payload": {"message": "hello"}}
    response = client.post("/tasks", json=task)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "completed"
    assert data["artifact"] == "olleh"


def test_task_unknown_type():
    task = {"id": "t3", "type": "unknown", "payload": {"message": "hello"}}
    response = client.post("/tasks", json=task)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "error"
    assert "Unknown task type" in data["message"]
