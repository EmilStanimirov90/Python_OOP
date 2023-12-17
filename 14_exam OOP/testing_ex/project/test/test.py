from unittest import TestCase, main
from collections import deque

from project.railway_station import RailwayStation


class TestRailwayStation(TestCase):
    def setUp(self):
        self.rs1 = RailwayStation("Plovdiv")

    def test_init(self):
        self.assertEqual("Plovdiv", self.rs1.name)
        self.assertEqual(deque([]), self.rs1.arrival_trains)
        self.assertEqual(deque([]), self.rs1.departure_trains)

    def test_setter_name(self):
        with self.assertRaises(ValueError) as ve:
            self.rs1.name = "a"
        self.assertEqual("Name should be more than 3 symbols!", str(ve.exception))

    def test_new_arrival_on_board(self):
        self.rs1.new_arrival_on_board('x')
        self.assertEqual(deque(["x"]), self.rs1.arrival_trains)

    def test_different_train_has_arrived_than_expected(self):
        self.rs1.new_arrival_on_board('x')
        self.assertEqual("There are other trains to arrive before y.", self.rs1.train_has_arrived("y"))

    def test_correct_train_has_arrived(self):
        self.rs1.new_arrival_on_board('x')
        self.assertEqual(deque(["x"]), self.rs1.arrival_trains)
        self.rs1.new_arrival_on_board('y')

        self.assertEqual(deque(["x", "y"]), self.rs1.arrival_trains)
        self.assertEqual("x is on the platform and will leave in 5 minutes.", self.rs1.train_has_arrived('x'))
        self.assertEqual(deque(["y"]), self.rs1.arrival_trains)

        self.assertEqual("y is on the platform and will leave in 5 minutes.", self.rs1.train_has_arrived('y'))
        self.assertEqual(deque([]), self.rs1.arrival_trains)
        self.assertEqual(deque(["x", "y"]), self.rs1.departure_trains)

    def test_train_has_left_True(self):
        self.rs1.departure_trains = deque(["x", "y"])
        self.assertTrue(self.rs1.train_has_left("x"))
        self.assertEqual(deque(["y"]), self.rs1.departure_trains)
        self.assertFalse(self.rs1.train_has_left("x"))

    def test_train_has_left_False(self):
        pass


if __name__ == "__main__":
    main()
