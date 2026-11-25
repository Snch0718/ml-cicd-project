
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_homepage():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {
        "message": "ML API is running!"
    }


def test_health():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_valid_prediction():
    response = client.post(
        "/predict",
        json={
            "sepal_length": 5.1,
            "sepal_width": 3.5,
            "petal_length": 1.4,
            "petal_width": 0.2
        }
    )

    assert response.status_code == 200

    result = response.json()

    assert "prediction" in result
    assert "confidence" in result
    assert 0 <= result["confidence"] <= 1


def test_invalid_prediction():
    response = client.post(
        "/predict",
        json={
            "sepal_length": -5.1,
            "sepal_width": 3.5,
            "petal_length": 1.4,
            "petal_width": 0.2
        }
    )

    assert response.status_code == 422
