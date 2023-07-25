import unittest
from project.movie import Movie


class MovieTests(unittest.TestCase):

    def test_for_valid_initialization(self):
        m = Movie("Mission Impossible", 2023, 7.5)
        self.assertEqual("Mission Impossible", m.name)
        self.assertEqual(2023, m.year)
        self.assertEqual(7.5, m.rating)
        self.assertEqual([], m.actors)

    def test_for_invalid_name_with_empty_string_raises_error(self):
        with self.assertRaises(ValueError) as ve:
            Movie("", 2023, 7.5)

        self.assertEqual("Name cannot be an empty string!", str(ve.exception))

    def test_for_invalid_year_lower_than_1887_raises_error(self):
        with self.assertRaises(ValueError) as ve:
            Movie("Mission Impossible", 1000, 7.5)

        self.assertEqual("Year is not valid!", str(ve.exception))

    def test_for_adding_actor_in_actors_list(self):
        m = Movie("Mission Impossible", 2023, 7.5)
        m.add_actor("Ivan")
        m.add_actor("Georgi")
        self.assertEqual(["Ivan", "Georgi"], m.actors)
        result = m.add_actor("Georgi")
        self.assertEqual("Georgi is already added in the list of actors!", result)

    def test__gt__by_movie_rating_self_is_winner(self):
        m = Movie("Mission Impossible", 2023, 7.5)
        m2 = Movie("Creed 2", 2022, 7.0)
        result = str(m > m2)

        self.assertTrue(m.rating > m2.rating)
        self.assertEqual('"Mission Impossible" is better than "Creed 2"', result)

    def test__gt__by_movie_rating_other_is_winner(self):
        m = Movie("Mission Impossible", 2023, 7.5)
        m3 = Movie("The Matrix", 2000, 9.9)
        result = str(m > m3)

        self.assertTrue(m.rating <= m3.rating)
        self.assertEqual('"The Matrix" is better than "Mission Impossible"', result)

    def test__repr__(self):
        m = Movie("Mission Impossible", 2023, 7.5)
        m.add_actor("Ivan")

        self.assertEqual("Name: Mission Impossible\n"
                         "Year of Release: 2023\n"
                         "Rating: 7.50\n"
                         "Cast: Ivan", str(m))


if __name__ == "__main__":
    unittest.main()
