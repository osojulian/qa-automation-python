import requests


class BookingApi:

    URL = "https://restful-booker.herokuapp.com"

    def get_bookings(self):

        r = requests.get(f"{self.URL}/booking")

        return r

    def get_booking_id(self, booking_id):

        r = requests.get(f"{self.URL}/booking/{booking_id}")

        return r

    def post_booking(self, payload):

        r = requests.post(f"{self.URL}/booking", json=payload)

        return r

    def create_token(self, payload):

        r = requests.post(f"{self.URL}/auth", json=payload)

        return r

    def put_booking(self, token, booking_id, update_booking):

        headers = {"Cookie": f"token={token}"}

        r = requests.put(
            f"{self.URL}/booking/{booking_id}", headers=headers, json=update_booking
        )

        return r
