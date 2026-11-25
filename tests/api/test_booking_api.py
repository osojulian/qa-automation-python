from api.booking_api import BookingApi


def test_get_all_bookings():

    booking_api = BookingApi()

    response = booking_api.get_bookings()

    assert response.status_code == 200

    assert isinstance(response.json(), list)


def test_get_booking_by_id():

    booking_api = BookingApi()

    bookings_response = booking_api.get_bookings()

    bookings = bookings_response.json()

    booking_id = bookings[0]["bookingid"]

    response = booking_api.get_booking_id(booking_id)

    assert response.status_code == 200

    assert isinstance(response.json()["firstname"], str)


def test_create_booking():

    payload = {
        "firstname": "Andrew",
        "lastname": "Krag",
        "totalprice": 345,
        "depositpaid": True,
        "bookingdates": {"checkin": "2020-01-01", "checkout": "2022-01-01"},
        "additionalneeds": "Breakfast",
    }

    booking_api = BookingApi()

    response = booking_api.post_booking(payload)

    assert response.status_code == 200

    assert response.json()["booking"]["firstname"] == payload["firstname"]

    booking_id = response.json()["bookingid"]

    booking_by_id = booking_api.get_booking_id(booking_id)

    assert booking_by_id.status_code == 200

    assert booking_by_id.json()["firstname"] == payload["firstname"]


def test_update_booking():

    booking_payload = {
        "firstname": "Andrew",
        "lastname": "Krag",
        "totalprice": 345,
        "depositpaid": True,
        "bookingdates": {"checkin": "2020-01-01", "checkout": "2022-01-01"},
        "additionalneeds": "Breakfast",
    }

    credentials = {"username": "admin", "password": "password123"}

    update_payload = {
        "firstname": "James",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {"checkin": "2018-01-01", "checkout": "2019-01-01"},
        "additionalneeds": "Breakfast",
    }

    booking_api = BookingApi()

    create_booking = booking_api.post_booking(booking_payload)

    assert create_booking.status_code == 200

    booking_id = create_booking.json()["bookingid"]

    post_token = booking_api.create_token(credentials)

    assert post_token.status_code == 200

    token = post_token.json()["token"]

    response = booking_api.put_booking(token, booking_id, update_payload)

    assert response.status_code == 200

    response_put = response.json()

    assert response_put['firstname'] == update_payload['firstname']

    response_id = booking_api.get_booking_id(booking_id)

    assert response_id.status_code == 200

    assert response_id.json() == update_payload
