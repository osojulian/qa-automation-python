import requests

class BookingApi:

    URL = 'https://restful-booker.herokuapp.com/booking'

    def get_bookings(self):

        r = requests.get(self.URL)

        return r
