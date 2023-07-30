from unittest import TestCase, main
from project.pet_shop import PetShop


class TestPetShop(TestCase):
    def setUp(self) -> None:
        self.shop = PetShop("Test")

    def test_correct_initialization(self):
        self.assertEqual("Test", self.shop.name)
        self.assertEqual({}, self.shop.food)
        self.assertEqual([], self.shop.pets)

    def test_negative_food_quantity_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.shop.add_food("Catfood", -1)

        self.assertEqual('Quantity cannot be equal to or less than 0', str(ve.exception))

    def test_add_non_existent_return_message(self):
        result = self.shop.add_food("Catfood", 10.5)
        expected = "Successfully added 10.50 grams of Catfood."

        self.assertEqual(expected, result)
        self.assertEqual({"Catfood": 10.5}, self.shop.food)

    def test_add_quantity_to_valid_food_return_message(self):
        self.shop.food = {"Catfood": 10.5}
        result = self.shop.add_food("Catfood", 10.5)
        expected = "Successfully added 10.50 grams of Catfood."

        self.assertEqual(expected, result)
        self.assertEqual({"Catfood": 21.0}, self.shop.food)

    def test_non_existent_pet_name_return_message(self):
        result = self.shop.add_pet("Sisi")
        expected = "Successfully added Sisi."

        self.assertEqual(expected, result)
        self.assertEqual(["Sisi"], self.shop.pets)

    def test_existing_pet_name_raises_exception(self):
        self.shop.add_pet("Sisi")

        with self.assertRaises(Exception) as ex:
            self.shop.add_pet("Sisi")

        expected = "Cannot add a pet with the same name"
        self.assertEqual(expected, str(ex.exception))

    def test_feed_non_existent_pet_name_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.shop.feed_pet("Catfood", "Sisi")

        expected = "Please insert a valid pet name"
        self.assertEqual(expected, str(ex.exception))

    def test_feed_pet_with_non_valid_food_name_return_message(self):
        self.shop.pets = ["Sisi"]

        result = self.shop.feed_pet("Catfood", "Sisi")
        expected = 'You do not have Catfood'

        self.assertEqual(expected, result)

    def test_food_with_quantity_less_than_100_return_message(self):
        self.shop.pets = ["Sisi"]
        self.shop.food = {"Catfood": 10}

        result = self.shop.feed_pet("Catfood", "Sisi")
        expected = "Adding food..."

        self.assertEqual(expected, result)
        self.assertEqual({"Catfood": 1010.00}, self.shop.food)

    def test_decreasing_food_quantity_after_feeding_return_message(self):
        self.shop.pets = ["Sisi"]
        self.shop.food = {"Catfood": 1000}

        result = self.shop.feed_pet("Catfood", "Sisi")
        expected = "Sisi was successfully fed"

        self.assertEqual(expected, result)
        self.assertEqual({"Catfood": 900}, self.shop.food)

    def test__repr__method(self):
        self.shop.pets = ["Sisi", "Max"]

        result = self.shop.__repr__()
        expected = f'Shop Test:\n' \
                   f'Pets: Sisi, Max'

        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
