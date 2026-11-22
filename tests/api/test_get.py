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
