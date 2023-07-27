from unittest import TestCase, main
from project.bookstore import Bookstore


class TestBookStore(TestCase):
    def setUp(self) -> None:
        self.store = Bookstore(20)

    def test_successful_initialization(self):
        self.assertEqual(20, self.store.books_limit)
        self.assertEqual({}, self.store.availability_in_store_by_book_titles)
        self.assertEqual(0, self.store._Bookstore__total_sold_books)

    def test_books_limit_setter_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.store.books_limit = 0

        self.assertEqual("Books limit of 0 is not valid", str(ve.exception))

    def test_total_number_of_books_in_store(self):
        self.store.availability_in_store_by_book_titles = {
            "Book1": 3,
            "Book2": 7,
            "Book3": 10
        }

        result = self.store.__len__()

        self.assertEqual(20, result)

    def test_receive_books_when_not_enough_space_raises_exception(self):
        self.store.availability_in_store_by_book_titles = {
            "Book1": 3,
            "Book2": 7,
            "Book3": 10
        }

        with self.assertRaises(Exception) as ex:
            self.store.receive_book("Test", 1)

        expected = "Books limit is reached. Cannot receive more books!"

        self.assertEqual(expected, str(ex.exception))

    def test_receive_books_when_enough_space(self):
        self.store.availability_in_store_by_book_titles = {
            "Book1": 3,
            "Book2": 7,
        }

        result = self.store.receive_book("Book1", 5)
        expected = "8 copies of Book1 are available in the bookstore."

        self.assertEqual(expected, result)
        self.assertEqual(15, len(self.store))

        result_2 = self.store.receive_book("Test", 5)
        expected_2 = "5 copies of Test are available in the bookstore."

        self.assertEqual(expected_2, result_2)
        self.assertEqual(20, len(self.store))

    def test_sell_not_valid_book_raises_exception(self):
        self.store.availability_in_store_by_book_titles = {
            "Book1": 3,
            "Book2": 7,
        }

        with self.assertRaises(Exception) as ex:
            self.store.sell_book("Test", 10)

        self.assertEqual("Book Test doesn't exist!", str(ex.exception))

    def test_sell_not_valid_copies_of_book_raises_exception(self):
        self.store.availability_in_store_by_book_titles = {
            "Book1": 3,
            "Book2": 7,
        }

        with self.assertRaises(Exception) as ex:
            self.store.sell_book("Book1", 10)

        expected = "Book1 has not enough copies to sell. Left: 3"

        self.assertEqual({"Book1": 3, "Book2": 7},
                         self.store.availability_in_store_by_book_titles)

        self.assertEqual(expected, str(ex.exception))

    def test_sell_successfully(self):
        self.store.availability_in_store_by_book_titles = {
            "Book1": 3,
            "Book2": 7,
        }

        result = self.store.sell_book("Book1", 3)
        self.assertEqual(0, self.store.availability_in_store_by_book_titles["Book1"])
        self.assertEqual(3, self.store._Bookstore__total_sold_books)
        self.assertEqual("Sold 3 copies of Book1", result)

        self.assertEqual(7, len(self.store))

    def test__str__method(self):
        self.store.availability_in_store_by_book_titles = {
            "Book1": 10,
            "Book2": 10,
        }

        self.store.sell_book("Book1", 5)

        result = self.store.__str__()

        expected = "Total sold books: 5\n" \
                   "Current availability: 15\n" \
                   " - Book1: 5 copies\n" \
                   " - Book2: 10 copies"

        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
