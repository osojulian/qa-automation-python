import requests

class BookingApi:

    URL = 'https://restful-booker.herokuapp.com/booking'

    def get_bookings(self):

        r = requests.get(self.URL)

        return r

    def get_booking_id(self, booking_id):

        r = requests.get(f'{self.URL}/{booking_id}')

        return r

    def post_booking(self, payload):

        r = requests.post(self.URL, json=payload)

        return r
