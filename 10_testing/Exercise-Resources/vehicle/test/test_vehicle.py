from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(55.5, 100.5)

    def test_correct_init(self):
        self.assertEqual(55.5, self.vehicle.fuel)
        self.assertEqual(55.5, self.vehicle.capacity)
        self.assertEqual(100.5, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_attributes_types(self):
        self.assertTrue(isinstance(self.vehicle.fuel, float))
        self.assertTrue(isinstance(self.vehicle.capacity, float))
        self.assertTrue(isinstance(self.vehicle.horse_power, float))
        self.assertTrue(isinstance(self.vehicle.fuel_consumption, float))
        self.assertTrue(isinstance(self.vehicle.DEFAULT_FUEL_CONSUMPTION, float))

    def test_drive_success(self):
        self.vehicle.drive(20)
        self.assertEqual(30.5, self.vehicle.fuel)

    def test_drive_fail(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(60)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_refuel_not_full_tank(self):
        self.vehicle.drive(4)
        self.vehicle.refuel(4)
        self.assertEqual(54.5, self.vehicle.fuel)

    def test_refuel_filled_to_brim(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(500)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_str(self):
        self.assertEqual(f"The vehicle has {100.5} "
                         f"horse power with {55.5} fuel left and {1.25} fuel consumption", str(self.vehicle))


if __name__ == "__main__":
    main()
