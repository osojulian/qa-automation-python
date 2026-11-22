from api.booking_api import BookingApi

def test_get():

    booking_api = BookingApi()

    response = booking_api.get_bookings()

    assert response.status_code == 200
