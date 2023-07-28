from unittest import TestCase, main
from project.team import Team


class TestTeam(TestCase):
    def setUp(self) -> None:
        self.team = Team("Test")

    def test_successful_initialization(self):
        self.assertEqual("Test", self.team.name)
        self.assertEqual({}, self.team.members)

    def test_name_setter_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.team.name = "Test1"

        self.assertEqual("Team Name can contain only letters!", str(ve.exception))

    def test_add_unique_members_method(self):
        self.team.members = {"Ivan": 20, "Gosho": 25}

        result = self.team.add_member(Ivan=20, Pesho=30, Maria=40)

        expected = "Successfully added: Pesho, Maria"
        self.assertEqual(expected, result)

        self.assertEqual({"Ivan": 20, "Gosho": 25, "Pesho": 30, "Maria": 40}, self.team.members)

    def test_remove_existing_member(self):
        self.team.members = {"Ivan": 20, "Gosho": 25, "Pesho": 30}

        result = self.team.remove_member("Ivan")

        self.assertEqual("Member Ivan removed", result)
        self.assertEqual({"Gosho": 25, "Pesho": 30}, self.team.members)

    def test_remove_nonexistent_member_return_message(self):
        self.team.members = {"Ivan": 20, "Gosho": 25, "Pesho": 30}

        result = self.team.remove_member("Sisi")

        self.assertEqual("Member with name Sisi does not exist", result)

        self.assertEqual({"Ivan": 20, "Gosho": 25, "Pesho": 30}, self.team.members)

    def test_team_length_greater_than_other_team(self):
        self.team.members = {"Ivan": 20, "Gosho": 25, "Pesho": 30, "Mario": 35}

        other = Team("Other")
        other.members = {"Maria": 20, "Ivana": 25, "Dara": 30}

        result = self.team.__gt__(other)

        self.assertEqual(True, result)
        self.assertTrue(len(self.team.members) > len(other.members))

    def test_team_length_less_than_or_equal_other_team(self):
        self.team.members = {"Ivan": 20, "Gosho": 25}

        other = Team("Other")
        other.members = {"Maria": 20, "Ivana": 25, "Dara": 30}

        result = self.team.__gt__(other)

        self.assertEqual(False, result)
        self.assertTrue(len(self.team.members) <= len(other.members))

    def test__len__method(self):
        self.team.members = {"Ivan": 20, "Gosho": 25, "Pesho": 30, "Mario": 35}

        result = self.team.__len__()

        self.assertEqual(4, result)

    def test__add__method(self):
        other = Team("Other")

        self.team.members = {"Ivan": 20, "Gosho": 25}
        other.members = {"Maria": 20, "Ivana": 25, "Mario": 40}

        result = self.team.__add__(other)
        self.assertEqual("TestOther", result.name)

        expected = {"Ivan": 20, "Gosho": 25, "Maria": 20, "Ivana": 25, "Mario": 40}
        self.assertEqual(expected, result.members)

    def test__str__method(self):
        self.team.members = {
            "Ivan": 20,
            "Gosho": 25,
            "Maria": 20,
            "Ivana": 40,
            "Pesho": 50
        }

        result = self.team.__str__()

        expected = "Team name: Test\n" \
                   "Member: Pesho - 50-years old\n" \
                   "Member: Ivana - 40-years old\n" \
                   "Member: Gosho - 25-years old\n" \
                   "Member: Ivan - 20-years old\n" \
                   "Member: Maria - 20-years old"

        self.assertEqual(expected, str(result))


if __name__ == "__main__":
    main()
