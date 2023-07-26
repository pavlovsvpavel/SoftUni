from unittest import TestCase, main

from project.truck_driver import TruckDriver


class TestTruckDriver(TestCase):
    def setUp(self) -> None:
        self.driver = TruckDriver("Ivan", 10.5)

    def test_successful_initialization(self):
        self.assertEqual("Ivan", self.driver.name)
        self.assertEqual(10.5, self.driver.money_per_mile)
        self.assertEqual({}, self.driver.available_cargos)
        self.assertEqual(0, self.driver.earned_money)
        self.assertEqual(0, self.driver.miles)

    def test_earned_money_less_than_zero_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.driver.earned_money = -1

        self.assertEqual("Ivan went bankrupt.", str(ve.exception))

    def test_add_existing_cargo_raises_exception(self):
        self.driver.add_cargo_offer("New York", 200)

        with self.assertRaises(Exception) as ex:
            self.driver.add_cargo_offer("New York", 200)

        self.assertEqual("Cargo offer is already added.", str(ex.exception))

    def test_add_unique_cargo_return_message(self):
        result = self.driver.add_cargo_offer("New York", 200)

        expected = "Cargo for 200 to New York was added as an offer."

        self.assertEqual({"New York": 200}, self.driver.available_cargos)

        self.assertEqual(expected, result)

    def test_for_cargo_offer_raises_value_error(self):
        result = self.driver.drive_best_cargo_offer()

        self.assertEqual("There are no offers available.", result)

    def test_find_best_cargo_offer(self):
        self.driver.add_cargo_offer("New York", 200)
        self.driver.add_cargo_offer("Washington", 300)

        self.assertEqual({"New York": 200, "Washington": 300}, self.driver.available_cargos)

        result = self.driver.drive_best_cargo_offer()
        expected = "Ivan is driving 300 to Washington."

        self.assertEqual(expected, result)

    def test_earned_money_increase(self):
        self.driver.add_cargo_offer("New York", 200)
        self.driver.add_cargo_offer("Washington", 250)
        self.driver.drive_best_cargo_offer()

        self.assertEqual(2605, self.driver.earned_money)

    def test_miles_increase(self):
        self.driver.add_cargo_offer("New York", 200)
        self.driver.add_cargo_offer("Washington", 250)
        self.driver.drive_best_cargo_offer()

        self.assertEqual(250, self.driver.miles)

    def test_eat_method_reduce_earned_money(self):
        self.driver.add_cargo_offer("New York", 200)
        self.driver.add_cargo_offer("Washington", 250)
        self.driver.drive_best_cargo_offer()

        self.assertEqual(2605, self.driver.earned_money)

    def test_sleep_method_reduce_earned_money(self):
        self.driver.add_cargo_offer("New York", 200)
        self.driver.add_cargo_offer("Washington", 1000)
        self.driver.drive_best_cargo_offer()

        self.assertEqual(10375, self.driver.earned_money)

    def test_pump_gas_method_reduce_earned_money(self):
        self.driver.add_cargo_offer("New York", 200)
        self.driver.add_cargo_offer("Washington", 1500)
        self.driver.drive_best_cargo_offer()

        self.assertEqual(15085, self.driver.earned_money)

    def test_truck_repair_method_reduce_earned_money(self):
        self.driver.add_cargo_offer("New York", 200)
        self.driver.add_cargo_offer("Washington", 10000)
        self.driver.drive_best_cargo_offer()

        self.assertEqual(93250, self.driver.earned_money)

    def test__repr__(self):
        self.driver.add_cargo_offer("New York", 200)
        self.driver.drive_best_cargo_offer()

        result = self.driver.__repr__()
        expected = "Ivan has 200 miles behind his back."

        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
