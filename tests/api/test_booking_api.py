from api.booking_api import BookingApi

def test_get():

    booking_api = BookingApi()

    response = booking_api.get_bookings()

    assert response.status_code == 200

def test_get_booking_by_id():

    booking_api = BookingApi()

    bookings_response = booking_api.get_bookings()

    bookings = bookings_response.json()

    booking_id = bookings[0]['bookingid']

    response = booking_api.get_booking_id(booking_id)

    assert response.status_code == 200

    assert isinstance(response.json()['firstname'], str)

def test_post():

    payload = {
    "firstname": "Andrew",
    "lastname": "Krag",
    "totalprice": 345,
    "depositpaid": True,
    "bookingdates": {
        "checkin": "2020-01-01",
        "checkout": "2022-01-01"
    },
    "additionalneeds": "Breakfast"
}

    booking_api = BookingApi()

    response = booking_api.post_booking(payload)

    assert response.status_code == 200

    assert payload["firstname"] == response.json()['booking']['firstname']

