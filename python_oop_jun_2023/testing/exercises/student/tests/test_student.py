from unittest import TestCase, main

from project.student import Student


class TestStudent(TestCase):
    def setUp(self) -> None:
        self.student = Student("Ivan")
        self.student_with_courses = Student("Gosho", {"Python_DB": ["cool"]})

    def test_correct_initialization(self):
        self.assertEqual("Ivan", self.student.name)
        self.assertEqual({}, self.student.courses)
        self.assertEqual({"Python_DB": ["cool"]}, self.student_with_courses.courses)

    def test_enroll_existing_course_and_add_notes(self):
        result = self.student_with_courses.enroll("Python_DB", ["first_note"])
        expected = "Course already added. Notes have been updated."
        self.assertEqual(result, expected)

        self.assertEqual(["cool", "first_note"], self.student_with_courses.courses["Python_DB"])

    def test_enroll_non_existing_course_and_add_notes_without_third_parameter(self):
        result = self.student.enroll("Java", ["first_note"])
        expected = "Course and course notes have been added."

        self.assertEqual(expected, result)
        self.assertEqual(["first_note"], self.student.courses["Java"])

    def test_enroll_non_existing_course_and_add_notes_with_third_parameter(self):
        result = self.student.enroll("Java", ["first_note"], "Y")
        expected = "Course and course notes have been added."

        self.assertEqual(expected, result)
        self.assertEqual(["first_note"], self.student.courses["Java"])

    def test_enroll_non_existing_course_without_adding_notes(self):
        result = self.student.enroll("C#", ["first_note"], "N")
        expected = "Course has been added."

        self.assertEqual(expected, result)
        self.assertEqual([], self.student.courses["C#"])

    def test_add_notes_to_existent_course(self):
        result = self.student_with_courses.add_notes("Python_DB", "second_note")
        expected = "Notes have been updated"

        self.assertEqual(expected, result)
        self.assertEqual(["cool", "second_note"], self.student_with_courses.courses["Python_DB"])

    def test_add_notes_to_non_existing_course(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("Java", "note")

        expected = "Cannot add notes. Course not found."
        self.assertEqual(expected, str(ex.exception))

    def test_leave_existent_course(self):
        result = self.student_with_courses.leave_course("Python_DB")
        expected = "Course has been removed"

        self.assertEqual(expected, result)
        self.assertEqual({}, self.student_with_courses.courses)

    def test_leave_non_existing_course_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("Java")

        expected = "Cannot remove course. Course not found."
        self.assertEqual(expected, str(ex.exception))


if __name__ == "__main__":
    main()
