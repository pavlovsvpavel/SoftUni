from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self) -> None:
        self.vehicle = Vehicle(20.5, 225)

    def test_for_correct_class_attributes(self):
        self.assertEqual(1.25, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_successful_initialization(self):
        self.assertEqual(20.5, self.vehicle.fuel)
        self.assertEqual(20.5, self.vehicle.capacity)
        self.assertEqual(225, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_driving_with_less_fuel_than_needed_raises_error(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_driving_with_enough_fuel(self):
        self.vehicle.drive(10)

        self.assertEqual(8, self.vehicle.fuel)

    def test_refueling_with_more_than_max_capacity_raises_error(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(1)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refueling_with_less_than_max_capacity(self):
        self.vehicle.drive(10)
        self.vehicle.refuel(5)

        self.assertEqual(13, self.vehicle.fuel)

    def test__str__method(self):
        self.vehicle.drive(10)

        result = self.vehicle.__str__()

        expected = "The vehicle has 225 " \
                   "horse power with 8.0 fuel left " \
                   "and 1.25 fuel consumption"

        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
