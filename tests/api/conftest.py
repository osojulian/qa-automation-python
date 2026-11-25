import pytest


@pytest.fixture
def payload():
    return {
        "firstname": "Andrew",
        "lastname": "Krag",
        "totalprice": 345,
        "depositpaid": True,
        "bookingdates": {"checkin": "2020-01-01", "checkout": "2022-01-01"},
        "additionalneeds": "Breakfast",
    }


@pytest.fixture
def credentials():
    return {"username": "admin", "password": "password123"}
