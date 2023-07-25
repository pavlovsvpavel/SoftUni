from unittest import TestCase, main
from project.tennis_player import TennisPlayer


class TestTennisPlayer(TestCase):
    def setUp(self) -> None:
        self.player = TennisPlayer("Grigor", 35, 69)

    def test_successful_initialization(self):
        self.assertEqual("Grigor", self.player.name)
        self.assertEqual(35, self.player.age)
        self.assertEqual(69, self.player.points)
        self.assertEqual([], self.player.wins)

    def test_name_less_than_two_symbols_raises_error(self):
        with self.assertRaises(ValueError) as ve:
            self.player.name = "PP"

        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))

    def test_age_less_than_18_years_raises_error(self):
        with self.assertRaises(ValueError) as ve:
            self.player.age = 17

        self.assertEqual("Players must be at least 18 years of age!", str(ve.exception))

    def test_add_nonexistent_tournament(self):
        self.player.add_new_win("Wimbledon")

        self.assertEqual(["Wimbledon"], self.player.wins)

    def test_add_existing_tournament(self):
        self.player.add_new_win("Australian Open")
        self.player.add_new_win("Wimbledon")

        result = self.player.add_new_win("Australian Open")
        expected = "Australian Open has been already added to the list of wins!"

        self.assertEqual(expected, result)

    def test__lt__method_player_with_less_points_than_other(self):
        other = TennisPlayer("Sharapova", 38, 85)

        result = self.player.__lt__(other)
        expected = 'Sharapova is a top seeded player and he/she is better than Grigor'

        self.assertEqual(expected, result)

    def test__lt__method_player_with_more_points_than_other(self):
        other = TennisPlayer("Nadal", 38, 65)

        result = self.player.__lt__(other)
        expected = 'Grigor is a better player than Nadal'

        self.assertEqual(expected, result)

    def test__str__method(self):
        self.player.add_new_win("Australian Open")
        self.player.add_new_win("Wimbledon")

        result = self.player.__str__()

        expected = "Tennis Player: Grigor\n" \
                   "Age: 35\n" \
                   "Points: 69.0\n" \
                   "Tournaments won: Australian Open, Wimbledon"

        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
