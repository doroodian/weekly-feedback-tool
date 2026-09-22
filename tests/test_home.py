from fastapi.testclient import TestClient

from weekly_feedback_tool.main import app

client = TestClient(app)


def test_home_returns_ok() -> None:
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
