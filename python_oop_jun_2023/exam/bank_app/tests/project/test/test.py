from unittest import TestCase, main
from project.second_hand_car import SecondHandCar


class TestSecondHandCar(TestCase):
    def setUp(self) -> None:
        self.car = SecondHandCar("Audi", "RS3", 10000, 101101.00)

    def test_correct_initialization(self):
        self.assertEqual("Audi", self.car.model)
        self.assertEqual("RS3", self.car.car_type)
        self.assertEqual(10000, self.car.mileage)
        self.assertEqual(101101.00, self.car.price)
        self.assertEqual([], self.car.repairs)

    def test_invalid_price_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.car.price = 1.0

        expected = 'Price should be greater than 1.0!'
        self.assertEqual(expected, str(ve.exception))

    def test_invalid_mileage_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.car.mileage = 100

        expected = 'Please, second-hand cars only! Mileage must be greater than 100!'
        self.assertEqual(expected, str(ve.exception))

    def test_set_promo_price_greater_than_actual_price_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(102000)

        expected = 'You are supposed to decrease the price!'
        self.assertEqual(expected, str(ve.exception))

    def test_set_promo_price_equal_to_actual_price_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.car.set_promotional_price(101101)

        expected = 'You are supposed to decrease the price!'
        self.assertEqual(expected, str(ve.exception))

    def test_successfully_promo_price_return_message(self):
        result = self.car.set_promotional_price(100000)
        expected = 'The promotional price has been successfully set.'

        self.assertEqual(expected, result)
        self.assertEqual(100000, self.car.price)

    def test_repair_price_is_higher_than_half_of_car_price_return_message(self):
        result = self.car.need_repair(100000, "Engine")

        expected = 'Repair is impossible!'
        self.assertEqual(expected, result)

    def test_successful_repair_return_message(self):
        result = self.car.need_repair(50000, "Transmission")
        expected = 'Price has been increased due to repair charges.'

        self.assertEqual(expected, result)
        self.assertEqual(["Transmission"], self.car.repairs)
        self.assertEqual(151101, self.car.price)

    def test__gt__method_with_incorrect_car_type_return_message(self):
        other = SecondHandCar("BMW", "M3", 1000, 50000.00)

        result = self.car.__gt__(other)
        expected = 'Cars cannot be compared. Type mismatch!'

        self.assertEqual(expected, result)

    def test__gt__method_with_same_car_type_return_message(self):
        other = SecondHandCar("Audi", "RS3", 20000, 50000.00)

        result = self.car.__gt__(other)

        self.assertTrue(result)

    def test__str__method(self):
        self.car.need_repair(50000, "Transmission")
        result = self.car.__str__()

        expected = f"""Model Audi | Type RS3 | Milage 10000km
Current price: 151101.00 | Number of Repairs: 1"""

        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
