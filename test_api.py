
from fastapi.testclient import TestClient

from api import app

client = TestClient(app)


def test_home_endpoint():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json()["message"] == "Project Atlas API çalışıyor!"


def test_calculate_weekly_hours_success():
    response = client.post(
        "/calculate-weekly-hours",
        json={
            "hours_per_day": 5,
            "days_per_week": 7,
        },
    )

    assert response.status_code == 200
    assert response.json()["total_hours"] == 35

def test_calculate_weekly_hours_response_model():
    response = client.post(
        "/calculate-weekly-hours",
        json={
            "hours_per_day": 5,
            "days_per_week": 7,
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert set(data.keys()) == {
        "hours_per_day",
        "days_per_week",
        "total_hours",
    }
    assert data["hours_per_day"] == 5
    assert data["days_per_week"] == 7
    assert data["total_hours"] == 35


def test_calculate_weekly_hours_zero():
    response = client.post(
        "/calculate-weekly-hours",
        json={
            "hours_per_day": 0,
            "days_per_week": 5,
        },
    )

    assert response.status_code == 200
    assert response.json()["total_hours"] == 0


def test_calculate_weekly_hours_invalid_days():
    response = client.post(
        "/calculate-weekly-hours",
        json={
            "hours_per_day": 5,
            "days_per_week": 8,
        },
    )

    assert response.status_code == 422


def test_calculate_weekly_hours_negative_hours():
    response = client.post(
        "/calculate-weekly-hours",
        json={
            "hours_per_day": -5,
            "days_per_week": 5,
        },
    )

    assert response.status_code == 422


def test_calculate_weekly_hours_missing_field():
    response = client.post(
        "/calculate-weekly-hours",
        json={
            "hours_per_day": 5,
        },
    )

    assert response.status_code == 422

    data = response.json()

    assert "detail" in data
    assert isinstance(data["detail"], list)
    assert any(
        error["loc"][-1] == "days_per_week"
        for error in data["detail"]
    )



def test_calculate_weekly_hours_string_instead_of_number():
    response = client.post(
        "/calculate-weekly-hours",
        json={
            "hours_per_day": "abc",
            "days_per_week": 5,
        },
    )

    assert response.status_code == 422


def test_calculate_weekly_hours_days_above_limit():
    response = client.post(
        "/calculate-weekly-hours",
        json={
            "hours_per_day": 5,
            "days_per_week": 8,
        },
    )

    assert response.status_code == 422


def test_calculate_weekly_hours_decimal_hours():
    response = client.post(
        "/calculate-weekly-hours",
        json={
            "hours_per_day": 5.5,
            "days_per_week": 5,
        },
    )

    assert response.status_code == 200
    assert response.json()["total_hours"] == 27.5

def test_calculate_weekly_hours_numeric_string():
    response = client.post(
        "/calculate-weekly-hours",
        json={
            "hours_per_day": "5",
            "days_per_week": 5,
        },
    )

    assert response.status_code == 422

def test_calculate_weekly_hours_decimal_days_rejected():
    response = client.post(
        "/calculate-weekly-hours",
        json={
            "hours_per_day": 5,
            "days_per_week": 5.5,
        },
    )

    assert response.status_code == 422

