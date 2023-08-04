from unittest import TestCase, main
from project.student_report_card import StudentReportCard


class TestStudentReportCard(TestCase):
    def setUp(self) -> None:
        self.card = StudentReportCard("Test", 10)

    def test_correct_initialization(self):
        self.assertEqual("Test", self.card.student_name)
        self.assertEqual(10, self.card.school_year)
        self.assertEqual({}, self.card.grades_by_subject)

    def test_successful_year(self):
        self.card.school_year = 1

        self.assertEqual(1, self.card.school_year)

    def test_successful_year_1(self):
        self.card.school_year = 12

        self.assertEqual(12, self.card.school_year)

    def test_incorrect_student_name_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.card.student_name = ""

        expected = "Student Name cannot be an empty string!"
        self.assertEqual(expected, str(ve.exception))

    def test_incorrect_student_school_year_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.card.school_year = 13

        expected = "School Year must be between 1 and 12!"
        self.assertEqual(expected, str(ve.exception))

    def test_add_grade_to_non_existent_subject(self):
        self.card.grades_by_subject = {"Math": [5.50, 6.00]}

        self.card.add_grade("Biology", 4.50)

        self.assertEqual({"Math": [5.50, 6.00], "Biology": [4.50]}, self.card.grades_by_subject)

    def test_add_grade_to_existent_subject(self):
        self.card.grades_by_subject = {"Math": [5.50, 2.00]}
        self.card.add_grade("Math", 3.00)

        self.assertEqual({"Math": [5.50, 2.00, 3.00]}, self.card.grades_by_subject)

    def test_average_grade_by_subject_return_message(self):
        self.card.grades_by_subject = {"Math": [5.50, 6.00], "Programming": [6.00, 4.00]}

        result = self.card.average_grade_by_subject()
        expected = "Math: 5.75\n" \
                   "Programming: 5.00"

        self.assertEqual(expected, result)

    def test_average_grade_for_all_subjects_return_message(self):
        self.card.grades_by_subject = {"Math": [5.50, 6.00], "Programming": [6.00, 4.00]}

        result = self.card.average_grade_for_all_subjects()
        expected = "Average Grade: 5.38"

        self.assertEqual(expected, result)

    def test__repr__method(self):
        self.card.grades_by_subject = {"Math": [5.50, 6.00], "Programming": [6.00, 4.00]}

        result = self.card.__repr__()
        expected = f"Name: Test\n" \
                   f"Year: 10\n" \
                   f"----------\n" \
                   f"Math: 5.75\n" \
                   f"Programming: 5.00\n" \
                   f"----------\n" \
                   f"Average Grade: 5.38"

        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
