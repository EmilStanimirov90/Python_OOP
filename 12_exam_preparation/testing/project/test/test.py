from project.trip import Trip
from unittest import TestCase, main


class TestTrip(TestCase):

    def setUp(self):
        self.t1f = Trip(10000.1, 1, False)
        self.t2f = Trip(10000.0, 2, False)
        self.t3t = Trip(10000.0, 2, True)

    def test_init(self):
        self.assertEqual(1000.1, self.t1f.budget)
        self.assertEqual(2, self.t2f.travelers)
        self.assertTrue(self.t3t.is_family)
        self.assertEqual({}, self.t3t.booked_destinations_paid_amounts)

    def test_setter_travelers(self):
        with self.assertRaises(ValueError) as ve:
            self.t1f.travelers = 0
        self.assertEqual('At least one traveler is required!', str(ve.exception))

    def test_setter_family(self):
        self.t1f.is_family = True
        self.assertFalse(self.t1f.is_family)
        self.assertFalse(self.t2f.is_family)
        self.assertTrue(self.t3t.is_family)

    def test_book_trip_not_in_offers(self):
        self.assertEqual('This destination is not in our offers, please choose a new one!',
                         self.t3t.book_a_trip("x"))


    def test_book_trip_not_enough_budget(self):
        self.assertEqual('Your budget is not enough!', self.t3t.book_a_trip("New Zealand"))

    def test_book_trip_success_no_discount(self):
        self.assertEqual(f'Successfully booked destination Bulgaria! Your budget left is 9000.00',self.t2f.book_a_trip("Bulgaria"))
        self.assertEqual(9000, self.t2f.budget)
        self.assertEqual({"Bulgaria": 1000}, self.t2f.booked_destinations_paid_amounts)

    def test_book_trip_success_with_discount(self):
        self.assertEqual(f'Successfully booked destination Bulgaria! Your budget left is 9100.00',
                         self.t3t.book_a_trip("Bulgaria"))
        self.assertEqual(9100, self.t3t.budget)
        self.assertEqual({"Bulgaria": 900}, self.t3t.booked_destinations_paid_amounts)

    def test_booking_empty(self):
        self.assertEqual('No bookings yet. Budget: 10000.00', self.t2f.booking_status())

    def test_booking_sorted(self):

        self.t3t.budget = 100000
        self.t3t.book_a_trip("Bulgaria")
        self.t3t.book_a_trip("Australia")
        expected_result = """Booked Destination: Australia
Paid Amount: 10260.00
Booked Destination: Bulgaria
Paid Amount: 900.00
Number of Travelers: 2
Budget Left: 88840.00"""
        self.assertEqual(expected_result, self.t3t.booking_status())



if __name__ == "__main__":
    main()
