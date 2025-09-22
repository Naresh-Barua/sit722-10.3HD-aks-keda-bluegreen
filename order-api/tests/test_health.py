from fastapi.testclient import TestClient
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from app.main import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert "status" in r.json()
