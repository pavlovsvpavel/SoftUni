from unittest import TestCase, main
from project.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self) -> None:
        self.mammal = Mammal("Sisi", "Cat", "Meow")

    def test_successful_initialization(self):
        self.assertEqual("Sisi", self.mammal.name)
        self.assertEqual("Cat", self.mammal.type)
        self.assertEqual("Meow", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_make_sound_method(self):
        result = self.mammal.make_sound()

        self.assertEqual("Sisi makes Meow", result)

    def test_get_kingdom_method(self):
        result = self.mammal.get_kingdom()
        self.assertEqual("animals", result)

    def test_info_method(self):
        result = self.mammal.info()

        self.assertEqual("Sisi is of type Cat", result)


if __name__ == "__main__":
    main()
