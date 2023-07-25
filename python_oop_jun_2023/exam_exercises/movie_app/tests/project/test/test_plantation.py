from unittest import TestCase, main
from project.plantation import Plantation


class TestPlantation(TestCase):
    def setUp(self) -> None:
        self.plantation = Plantation(4)

    def test_correct_initialization(self):
        self.assertEqual(4, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)

    def test_size_for_negative_number(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.size = -1

        self.assertEqual("Size must be positive number!", str(ve.exception))

    def test_hire_worker_worker_already_hired_raises_error(self):
        self.plantation.hire_worker("Ivan")

        with self.assertRaises(ValueError) as ve:
            self.plantation.hire_worker("Ivan")

        self.assertEqual("Worker already hired!", str(ve.exception))

    def test_hire_worker_worker_not_hired_add_to_workers_list(self):
        result = self.plantation.hire_worker("Ivan")
        self.assertEqual("Ivan successfully hired.", result)

        self.assertEqual(["Ivan"], self.plantation.workers)

    def test__len__method(self):
        self.plantation.plants = {
            "Ivan": ["Rose", "Hibiscus"],
            "Gosho": ["Apple tree", "Strawberry"]
        }

        result = self.plantation.__len__()

        self.assertEqual(4, result)

    def test_planting_method_worker_is_not_hired_raises_error(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("Pesho", "Crocus")

        self.assertEqual("Worker with name Pesho is not hired!", str(ve.exception))

    def test_planting_method_plantation_is_full_raises_error(self):
        self.plantation.hire_worker("Ivan")
        self.plantation.plants = {
            "Ivan": ["Rose", "Hibiscus"],
            "Gosho": ["Apple tree", "Strawberry"]
        }

        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("Ivan", "some plant")

        self.assertEqual("The plantation is full!", str(ve.exception))

    def test_successful_planting_method_first_plant(self):
        self.plantation.hire_worker("Pesho")
        result = self.plantation.planting("Pesho", "first plant")

        self.assertEqual("Pesho planted it's first first plant.", result)

    def test_successful_planting_method_existing_worker(self):
        self.plantation.hire_worker("Pesho")
        self.plantation.planting("Pesho", "first plant")

        result = self.plantation.planting("Pesho", "next plant")
        expected = "Pesho planted next plant."

        self.assertEqual(expected, result)

    def test__str__method(self):
        self.plantation.hire_worker("Ivan")
        self.plantation.hire_worker("Gosho")
        self.plantation.planting("Ivan", "Rose")
        self.plantation.planting("Ivan", "Tree")
        self.plantation.planting("Gosho", "Hibiscus")
        self.plantation.planting("Gosho", "Strawberry")

        result = self.plantation.__str__()

        expected = "Plantation size: 4\n" \
                   "Ivan, Gosho\n" \
                   "Ivan planted: Rose, Tree\n" \
                   "Gosho planted: Hibiscus, Strawberry"

        self.assertEqual(expected, result)

    def test__repr__method(self):
        self.plantation.hire_worker("Ivan")
        self.plantation.hire_worker("Gosho")

        result = self.plantation.__repr__()

        expected = "Size: 4\n" \
                   "Workers: Ivan, Gosho"

        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
