from unittest import TestCase, main
from project.student import Student


class StudentTest(TestCase):
    def setUp(self) -> None:
        self.student = Student("Lili")
        self.student_with_courses = Student("Ruja", {"porn": ["milf"]})

    def test_correct_initializing_without_courses(self):
        self.assertEqual("Lili", self.student.name)
        self.assertEqual({}, self.student.courses)

    def test_correct_initializing_with_course(self):
        self.assertEqual({"porn": ["milf"]}, self.student_with_courses.courses)

    def test_enroll_if_cours_exist_in_courses_correct_setup(self):
        result = self.student_with_courses.enroll("porn", ["doggy", "teen"])
        self.assertEqual(["milf", "doggy", "teen"], self.student_with_courses.courses["porn"])
        self.assertEqual("Course already added. Notes have been updated.", result)

    def test_enroll_with_non_existing_course_expect_correct_adding_without_third_param(self):
        result = self.student.enroll("drive", ["gear", "engine"])
        self.assertEqual({"drive": ["gear", "engine"]}, self.student.courses)
        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_with_non_existing_course_expect_correct_adding_with_third_param_Y(self):
        result = self.student.enroll("drive", ["gear", "engine"], "Y")
        self.assertEqual({"drive": ["gear", "engine"]}, self.student.courses)
        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_with_non_existing_course_without_adding_notes_excpect_correct_add(self):
        result = self.student.enroll("drive", ["gear", "engine"], "n")
        self.assertEqual({"drive": []}, self.student.courses)
        self.assertEqual("Course has been added.", result)

    def test_add_notes_in_existing_course_expect_correct_adding(self):
        result = self.student_with_courses.add_notes("porn", "doggy")
        self.assertEqual(["milf", "doggy"], self.student_with_courses.courses["porn"])
        self.assertEqual("Notes have been updated", result)

    def test_add_notes_to_non_existing_course_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("drive", "gear")
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course_with_exists_course_expect_correct_remove(self):
        result = self.student_with_courses.leave_course("porn")
        self.assertEqual({}, self.student_with_courses.courses)
        self.assertEqual("Course has been removed", result)

    def test_leave_course_with_non_existing_course_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("drive")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == "__main__":
    main()
