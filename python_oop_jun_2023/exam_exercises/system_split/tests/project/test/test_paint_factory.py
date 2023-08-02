from unittest import TestCase, main

from project.factory.paint_factory import PaintFactory


class TestPaintFactory(TestCase):
    def setUp(self) -> None:
        self.factory = PaintFactory("Test", 5)

    def test_correct_initialization(self):
        self.assertEqual("Test", self.factory.name)
        self.assertEqual(5, self.factory.capacity)
        self.assertEqual({}, self.factory.ingredients)
        self.assertEqual(["white", "yellow", "blue", "green", "red"], self.factory.valid_ingredients)

    def test_can_add_method(self):
        value = 3
        self.factory.ingredients = {"blue": 1}
        self.factory.ingredients = {"white": 1}

        self.assertTrue(self.factory.can_add(value))

    def test_not_enough_capacity_to_add_valid_product_type_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.factory.add_ingredient("white", 10)

        expected = "Not enough space in factory"
        self.assertEqual(expected, str(ve.exception))

    def test_add_invalid_product_type_raises_type_error(self):
        with self.assertRaises(TypeError) as te:
            self.factory.add_ingredient("black", 10)

        expected = "Ingredient of type black not allowed in PaintFactory"
        self.assertEqual(expected, str(te.exception))

    def test_add_valid_product_type_with_enough_capacity(self):
        self.factory.add_ingredient("blue", 1)
        self.assertEqual({"blue": 1}, self.factory.ingredients)

        self.factory.add_ingredient("blue", 2)
        self.assertEqual({"blue": 3}, self.factory.ingredients)

    def test_remove_valid_product_type_with_lower_than_zero_quantity_raises_value_error(self):
        self.factory.ingredients = {"blue": 1}
        with self.assertRaises(ValueError) as ve:
            self.factory.remove_ingredient("blue", 2)

        expected = "Ingredients quantity cannot be less than zero"
        self.assertEqual(expected, str(ve.exception))

    def test_remove_non_existent_product_type_raises_key_error(self):
        with self.assertRaises(KeyError) as ke:
            self.factory.remove_ingredient("blue", 2)

        expected = f"'No such ingredient in the factory'"
        self.assertEqual(expected, str(ke.exception))

    def test__repr__method(self):
        self.factory.add_ingredient("blue", 1)
        self.factory.add_ingredient("white", 2)

        result = self.factory.__repr__()
        expected = ("Factory name: Test with capacity 5.\n"
                    "blue: 1\n"
                    "white: 2\n")

        self.assertEqual(expected, result)

    def test_products_getter(self):
        self.factory.ingredients = {"white": 4}
        result = self.factory.products

        self.assertEqual({"white": 4}, result)


if __name__ == "__main__":
    main()
