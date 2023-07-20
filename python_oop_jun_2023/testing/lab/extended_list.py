import unittest


class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


class IntegerListTests(unittest.TestCase):
    def setUp(self) -> None:
        self.i = IntegerList(2, 4, 6, 8, 10, "asd", True, 2.2)

    def test_init(self):
        result = self.i.get_data()
        self.assertEqual([2, 4, 6, 8, 10], result)

    def test_get_data_func(self):
        self.assertEqual([2, 4, 6, 8, 10], self.i.get_data())

    def test_add_func_error(self):
        with self.assertRaises(ValueError) as error:
            self.i.add(2.3)

        self.assertEqual("Element is not Integer", str(error.exception))

    def test_successful_adding_an_integer(self):
        result = self.i.add(100)

        self.assertEqual([2, 4, 6, 8, 10, 100], result)

    def test_remove_index_func_error(self):
        with self.assertRaises(IndexError) as error:
            self.i.remove_index(5)

        self.assertEqual("Index is out of range", str(error.exception))

    def test_successful_removing_an_integer(self):
        result = self.i.remove_index(1)

        self.assertEqual(4, result)

    def test_get_func_error(self):
        with self.assertRaises(IndexError) as error:
            self.i.get(10)

        self.assertEqual("Index is out of range", str(error.exception))

    def test_insert_func_error(self):
        with self.subTest():
            with self.assertRaises(IndexError) as error:
                self.i.insert(10, 20)

            self.assertEqual("Index is out of range", str(error.exception))

        with self.subTest():
            with self.assertRaises(ValueError) as error:
                self.i.insert(4, 5.5)

            self.assertEqual("Element is not Integer", str(error.exception))

    def test_insert_with_valid_attributes(self):
        self.i.insert(0, 500)

        self.assertEqual([500, 2, 4, 6, 8, 10], self.i.get_data())

    def test_get_biggest_func(self):
        result = self.i.get_biggest()

        self.assertEqual(10, result)

    def test_get_index_func(self):
        result = self.i.get_index(2)

        self.assertEqual(0, result)


if __name__ == "__main__":
    unittest.main()
