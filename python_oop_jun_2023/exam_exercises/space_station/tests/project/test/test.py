from unittest import TestCase, main
from project.library import Library


class TestLibrary(TestCase):
    def setUp(self) -> None:
        self.library = Library("Test")

    def test_correct_initialization(self):
        self.assertEqual("Test", self.library.name)
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

    def test_invalid_name_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.library.name = ""

        expected = "Name cannot be empty string!"
        self.assertEqual(expected, str(ve.exception))

    def test_add_book_to_non_existing_author(self):
        self.library.add_book("Author", "Title")

        result = self.library.books_by_authors["Author"]

        self.assertEqual(["Title"], result)

    def test_add_existing_reader_return_message(self):
        self.library.add_reader("Gosho")
        result = self.library.add_reader("Gosho")

        expected = "Gosho is already registered in the Test library."
        self.assertEqual(expected, result)

    def test_add_non_existing_reader(self):
        self.library.add_reader("Gosho")

        self.assertEqual([], self.library.readers["Gosho"])

    def test_rent_book_reader_not_in_readers_return_message(self):
        result = self.library.rent_book("Ivan", "Author1", "Title1")

        expected = "Ivan is not registered in the Test Library."
        self.assertEqual(expected, result)

    def test_rent_book_author_not_in_authors_return_message(self):
        self.library.add_reader("Ivan")
        result = self.library.rent_book("Ivan", "Author1", "Title1")

        expected = "Test Library does not have any Author1's books."
        self.assertEqual(expected, result)

    def test_rent_book_title_not_in_titles_return_message(self):
        self.library.add_reader("Ivan")
        self.library.add_book("Author1", "Title")

        result = self.library.rent_book("Ivan", "Author1", "Title1")
        expected = """Test Library does not have Author1's "Title1"."""
        self.assertEqual(expected, result)

    def test_rent_book_with_valid_data(self):
        self.library.add_reader("Ivan")
        self.library.add_book("Author", "Title")
        self.library.rent_book("Ivan", "Author", "Title")

        self.assertEqual([{"Author": "Title"}], self.library.readers["Ivan"])
        self.assertEqual([], self.library.books_by_authors["Author"])


if __name__ == "__main__":
    main()
