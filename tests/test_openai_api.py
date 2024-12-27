# tests/test_openai_api.py

# Unit tests for OpenAI API routes
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_generate_endpoint():
    payload = {
        "prompt": "What are the symptoms of diabetes?",
        "model": "gpt-4o"
    }
    response = client.post("/openai/generate", json=payload)
    assert response.status_code == 200
    assert "result" in response.json()
