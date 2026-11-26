
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "success"


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_overview():
    response = client.get("/api/overview")
    assert response.status_code == 200
    assert response.json()["total_items"] == 30490
    assert response.json()["reorder_items"] == 12472


def test_forecast():
    response = client.get("/api/forecast")
    assert response.status_code == 200


def test_inventory():
    response = client.get("/api/inventory")
    assert response.status_code == 200


def test_replenishment():
    response = client.get(
        "/api/replenishment",
        params={
            "limit": 10,
            "offset": 0,
            "category": "FOODS",
            "store": "CA_1",
            "status": "Reorder"
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert data["returned_records"] <= 10
    assert all(
        item["replenishment_status"] == "Reorder"
        for item in data["replenishment_data"]
    )


def test_business_insights():
    response = client.get("/api/business-insights")
    assert response.status_code == 200
