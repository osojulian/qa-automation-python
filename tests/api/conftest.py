import pytest
import requests

from api.booking_api import BookingApi


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


@pytest.fixture
def token(credentials):

    booking_api = BookingApi()

    post_token = booking_api.create_token(credentials)

    assert post_token.status_code == 200

    token = post_token.json()["token"]

    return token
