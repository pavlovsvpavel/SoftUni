import unittest


class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed


car = Car("a", "b", 1, 4)
car.make = "Audi"
print(car)


class CarTests(unittest.TestCase):
    def setUp(self) -> None:
        self.car = Car("Audi", "S3", 12.5, 60)

    def test_init(self):
        self.assertEqual("Audi", self.car.make)
        self.assertEqual("S3", self.car.model)
        self.assertEqual(12.5, self.car.fuel_consumption)
        self.assertEqual(60, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_empty_input_for_make(self):
        with self.assertRaises(Exception) as error:
            self.car = Car("", "S3", 12.5, 60)

        self.assertEqual("Make cannot be null or empty!", str(error.exception))

    def test_empty_input_for_model(self):
        with self.assertRaises(Exception) as error:
            self.car = Car("Audi", "", 12.5, 60)

        self.assertEqual("Model cannot be null or empty!", str(error.exception))

    def test_zero_or_negative_input_for_fuel_consumption(self):
        with self.assertRaises(Exception) as error:
            self.car = Car("Audi", "S3", 0, 60)

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(error.exception))

    def test_zero_or_negative_input_for_fuel_capacity(self):
        with self.assertRaises(Exception) as error:
            self.car = Car("Audi", "S3", 12.5, 0)

        self.assertEqual("Fuel capacity cannot be zero or negative!", str(error.exception))

    def test_negative_input_for_fuel_amount(self):
        with self.assertRaises(Exception) as error:
            self.car.fuel_amount = -1

        self.assertEqual("Fuel amount cannot be negative!", str(error.exception))

    def test_refuel_func_zero_or_negative_error(self):
        with self.assertRaises(Exception) as error:
            self.car.refuel(0)

        self.assertEqual("Fuel amount cannot be zero or negative!", str(error.exception))

    def test_successful_refuel(self):
        with self.subTest("Fuel is not added correctly to total fuel amount"):
            self.car.refuel(20)
            self.assertEqual(20, self.car.fuel_amount)

            self.car.refuel(20)
            self.assertEqual(40, self.car.fuel_amount)

        with self.subTest("Fuel can't be more than fuel capacity"):
            self.car.refuel(100)
            self.assertEqual(60, self.car.fuel_amount)

    def test_drive_func(self):
        with self.subTest():
            self.car.fuel_amount = 20
            self.car.drive(100)

            self.assertEqual(7.5, self.car.fuel_amount)

        with self.subTest():
            with self.assertRaises(Exception) as error:
                self.car.drive(333)

            self.assertEqual("You don't have enough fuel to drive!", str(error.exception))


if __name__ == "__main__":
    unittest.main()
