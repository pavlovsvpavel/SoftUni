import unittest


class Cat:

    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')

        self.sleepy = False


class CatTests(unittest.TestCase):
    def test_cat_size_increase(self):
        cat = Cat("Sisi")
        expected_result = cat.size + 1
        cat.eat()
        result = cat.size
        self.assertEqual(expected_result, result)

    def test_fed_is_true_after_eat(self):
        cat = Cat("Sisi")
        cat.eat()
        self.assertTrue(cat.fed)

    def test_already_fed_after_eat_error(self):
        cat = Cat("Sisi")
        cat.eat()
        with self.assertRaises(Exception) as error:
            cat.eat()

        self.assertEqual('Already fed.', str(error.exception))

    def test_cannot_sleep_if_not_fed_error(self):
        cat = Cat("Sisi")
        with self.assertRaises(Exception) as error:
            cat.sleep()
        self.assertEqual('Cannot sleep while hungry', str(error.exception))

    def test_cat_is_sleepy_after_sleeping(self):
        cat = Cat("Sisi")
        cat.eat()
        cat.sleep()

        self.assertFalse(cat.sleepy)


if __name__ == "__main__":
    unittest.main()
