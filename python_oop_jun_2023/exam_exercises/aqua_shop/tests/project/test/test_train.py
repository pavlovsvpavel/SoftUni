from unittest import TestCase, main

from project.train.train import Train


class TestTrain(TestCase):
    def setUp(self) -> None:
        self.train = Train("Test", 2)

    def test_class_attributes(self):
        self.assertEqual("Train is full", Train.TRAIN_FULL)
        self.assertEqual("Passenger {} Exists", Train.PASSENGER_EXISTS)
        self.assertEqual("Passenger Not Found", Train.PASSENGER_NOT_FOUND)
        self.assertEqual("Added passenger {}", Train.PASSENGER_ADD)
        self.assertEqual("Removed {}", Train.PASSENGER_REMOVED)
        self.assertEqual(0, Train.ZERO_CAPACITY)

    def test_correct_initialization(self):
        self.assertEqual("Test", self.train.name)
        self.assertEqual(2, self.train.capacity)
        self.assertEqual([], self.train.passengers)

    def test_add_passenger_in_full_train_raises_value_error(self):
        self.train.passengers = ["Ivan", "Maria"]
        with self.assertRaises(ValueError) as ve:
            self.train.add("Pesho")

        self.assertEqual(Train.TRAIN_FULL, str(ve.exception))

    def test_add_existent_passenger_raises_value_error(self):
        self.train.passengers = ["Ivan"]
        with self.assertRaises(ValueError) as ve:
            self.train.add("Ivan")

        self.assertEqual(Train.PASSENGER_EXISTS.format("Ivan"), str(ve.exception))

    def test_add_passenger_successfully(self):
        result = self.train.add("Ivan")

        self.assertEqual(Train.PASSENGER_ADD.format("Ivan"), result.format("Ivan"))
        self.assertEqual(["Ivan"], self.train.passengers)

    def test_remove_non_existent_passenger_raises_value_error(self):
        self.train.passengers = ["Ivan"]

        with self.assertRaises(ValueError) as ve:
            self.train.remove("Maria")

        self.assertEqual(Train.PASSENGER_NOT_FOUND, str(ve.exception))
        self.assertEqual(["Ivan"], self.train.passengers)

    def test_remove_existent_passenger(self):
        self.train.passengers = ["Ivan"]
        result = self.train.remove("Ivan")

        self.assertEqual(Train.PASSENGER_REMOVED.format("Ivan"), result)
        self.assertEqual([], self.train.passengers)


if __name__ == "__main__":
    main()
