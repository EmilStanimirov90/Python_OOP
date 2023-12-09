from project.second_hand_car import SecondHandCar

from unittest import TestCase, main


class TestSecondHandCar(TestCase):

    def setUp(self):
        self.car1 = SecondHandCar("model", "type", 10000, 1000.50)
        self.car2 = SecondHandCar("model2", "type2", 20000, 2000.50)
        self.car3 = SecondHandCar("model2", "type2", 202000, 20200.50)

    def test_init(self):
        self.assertEqual("model", self.car1.model)
        self.assertEqual("type", self.car1.car_type)
        self.assertEqual(10000, self.car1.mileage)
        self.assertEqual(1000.50, self.car1.price)
        self.assertEqual([], self.car1.repairs)

    def test_setter_price(self):
        with self.assertRaises(ValueError) as ve:
            self.car1.price = 1
        self.assertEqual('Price should be greater than 1.0!', str(ve.exception))
        with self.assertRaises(ValueError) as ve:
            self.car1.price = 0
        self.assertEqual('Price should be greater than 1.0!', str(ve.exception))

    def test_setter_mileage(self):
        with self.assertRaises(ValueError) as ve:
            self.car1.mileage = 100
        self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!', str(ve.exception))

    def test_promo_price_wrong_raise_error(self):
        with self.assertRaises(ValueError) as v:
            self.car1.set_promotional_price(1001)
        self.assertEqual('You are supposed to decrease the price!', str(v.exception))

    def test_promo_price_correct(self):
        result = self.car1.set_promotional_price(500)
        self.assertEqual(500, self.car1.price)
        self.assertEqual('The promotional price has been successfully set.', result)

    def test_repair_raise_error(self):
        r = self.car1.need_repair(2000, 'engine')
        self.assertEqual('Repair is impossible!', r)

    def test_repair_correct(self):
        r = self.car1.need_repair(200, 'engine')
        self.assertEqual(1200.5, self.car1.price)
        self.assertEqual(["engine"], self.car1.repairs)
        self.assertEqual('Price has been increased due to repair charges.', r)

    def test_gt(self):
        self.assertTrue(self.car3 > self.car2)
        self.assertFalse(self.car2 > self.car3)

    def test_gt_diff_types(self):
        self.assertEqual("Cars cannot be compared. Type mismatch!", self.car1 > self.car3)

    def test_str(self):
        self.assertEqual(f"""Model model | Type type | Milage 10000km
Current price: 1000.50 | Number of Repairs: 0""", self.car1.__str__())

if __name__ == "__main__":
    main()
