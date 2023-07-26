from unittest import TestCase, main
from project.shopping_cart import ShoppingCart


class TestShoppingCart(TestCase):
    def setUp(self) -> None:
        self.cart = ShoppingCart("Lidl", 50.5)

    def test_successful_initialization(self):
        self.assertEqual("Lidl", self.cart.shop_name)
        self.assertEqual(50.5, self.cart.budget)
        self.assertEqual({}, self.cart.products)

    def test_shop_name_setter_raises_value_error(self):
        with self.subTest():
            with self.assertRaises(ValueError) as ve:
                self.cart.shop_name = "lidl4"

            expected = "Shop must contain only letters and must start with capital letter!"
            self.assertEqual(expected, str(ve.exception))

    def test_add_to_card_price_is_over_100_raises_value_error(self):
        self.cart.products["tomatoes"] = 101

        with self.assertRaises(ValueError) as ve:
            self.cart.add_to_cart("tomatoes", 101)

        self.assertEqual("Product tomatoes cost too much!", str(ve.exception))

    def test_add_to_cart_is_successful(self):
        result_1 = self.cart.add_to_cart("bread", 1.5)
        result_2 = self.cart.add_to_cart("tomatoes", 5.5)

        self.assertEqual({"bread": 1.5, "tomatoes": 5.5}, self.cart.products)
        self.assertEqual("bread product was successfully added to the cart!", result_1)
        self.assertEqual("tomatoes product was successfully added to the cart!", result_2)

    def test_remove_from_cart_nonexistent_product_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.remove_from_cart("bread")

        expected = "No product with name bread in the cart!"

        self.assertEqual(expected, str(ve.exception))

    def test_remove_from_cart_is_successful(self):
        self.cart.add_to_cart("bread", 1.5)
        self.cart.add_to_cart("tomatoes", 5.5)

        result = self.cart.remove_from_cart("bread")

        expected = "Product bread was successfully removed from the cart!"

        self.assertEqual(expected, result)
        self.assertEqual({"tomatoes": 5.5}, self.cart.products)

    def test_new_shop_name(self):
        other = ShoppingCart("Billa", 50.5)
        result = self.cart.__add__(other)

        self.assertEqual("LidlBilla", result.shop_name)

    def test_new_budget(self):
        other = ShoppingCart("Billa", 50.5)
        result = self.cart.__add__(other)

        self.assertEqual(101, result.budget)

    def test_new_shopping_cart_products(self):
        new_cart = ShoppingCart("LidlBilla", 101)
        self.cart.add_to_cart("bread", 1.5)
        new_cart.add_to_cart("bananas", 6.5)

        result = self.cart.__add__(new_cart)

        self.assertEqual({"bread": 1.5, "bananas": 6.5}, result.products)

    def test_buy_products_with_less_budget_raises_value_error(self):
        self.cart.add_to_cart("black angus", 60)
        self.cart.add_to_cart("tomatoes", 5.50)

        with self.assertRaises(ValueError) as ve:
            self.cart.buy_products()

        expected = "Not enough money to buy the products! Over budget with 15.00lv!"

        self.assertEqual(expected, str(ve.exception))

    def test_successful_buy(self):
        self.cart.add_to_cart("bread", 1.50)
        self.cart.add_to_cart("tomatoes", 5.50)
        result = self.cart.buy_products()

        expected = "Products were successfully bought! Total cost: 7.00lv."

        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
