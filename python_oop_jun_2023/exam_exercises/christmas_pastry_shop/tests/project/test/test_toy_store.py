from unittest import TestCase, main

from project.toy_store import ToyStore


class TestToyStore(TestCase):
    def setUp(self) -> None:
        self.store = ToyStore()

    def test_successful_initialization(self):
        expected = {
            "A": None,
            "B": None,
            "C": None,
            "D": None,
            "E": None,
            "F": None,
            "G": None,
        }
        self.assertEqual(expected, self.store.toy_shelf)

    def test_add_toy_to_nonexistent_shelf_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.store.add_toy("W", "Bear")

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_add_existing_toy_to_shelf_raises_exception(self):
        self.store.toy_shelf["A"] = "Bear"

        with self.assertRaises(Exception) as ex:
            self.store.add_toy("A", "Bear")

        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_add_toy_to_already_taken_shelf_raises_exception(self):
        self.store.toy_shelf["A"] = "Bear"

        with self.assertRaises(Exception) as ex:
            self.store.add_toy("A", "Dog")

        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_successful_add_toy_to_shelf(self):
        result = self.store.add_toy("C", "Cat")

        self.assertEqual("Cat", self.store.toy_shelf["C"])
        self.assertEqual(f"Toy:Cat placed successfully!", result)

    def test_remove_toy_from_nonexistent_shelf_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("W", "Train")

        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_remove_nonexistent_toy_from_shelf_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("D", "Car")

        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_successful_toy_removal_from_shelf(self):
        self.store.toy_shelf["D"] = "Train"

        result = self.store.remove_toy("D", "Train")
        expected = None
        expected_message = f"Remove toy:Train successfully!"

        self.assertEqual(expected, self.store.toy_shelf["D"])
        self.assertEqual(expected_message, result)


if __name__ == "__main__":
    main()
