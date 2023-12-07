from unittest import TestCase, main
from project.student import Student


class TestStudent(TestCase):
    def setUp(self):
        self.student = Student("Ivan", None)
        self.student2 = Student("Ivan2", {"course 1": ['a', 'b']})

    def test_init(self):
        self.assertEqual("Ivan", self.student.name)
        self.assertEqual("Ivan2", self.student2.name)

        self.assertEqual({}, self.student.courses)
        self.assertEqual({"course 1": ['a', 'b']}, self.student2.courses)

    def test_enroll_if_new_course_in_courses(self):
        result = self.student2.enroll("course 1", ["n1", "n2"], "add notes")
        self.assertEqual({"course 1": ['a', 'b', "n1", "n2"]}, self.student2.courses)
        self.assertEqual("Course already added. Notes have been updated.", result)

        result = self.student2.enroll("course 1", ["n3", "n4"], "Y")
        self.assertEqual({"course 1": ['a', "b", "n1", "n2", "n3", "n4"]}, self.student2.courses)
        self.assertEqual("Course already added. Notes have been updated.", result)

    def test_enroll_if_course_not_in_courses_and_notes_is_Y_or_empty(self):
        result = self.student2.enroll("course 2", ["n5", "n6"], "Y")
        self.assertEqual({"course 1": ['a', 'b'], "course 2": ["n5", "n6"]}, self.student2.courses)
        self.assertEqual("Course and course notes have been added.", result)
        result = self.student2.enroll("course 3", ["n5", "n6"], "")
        self.assertEqual({"course 1": ['a', 'b'],"course 2": ["n5", "n6"], "course 3": ["n5", "n6"]}, self.student2.courses)
        self.assertEqual("Course and course notes have been added.", result)

    def test_enroll_if_course_not_in_courses_and_notes_is_empty(self):
        result = self.student2.enroll("course 4", "xcx", 'x')
        self.assertEqual({"course 1": ['a', 'b'], "course 4": []}, self.student2.courses)
        self.assertEqual("Course has been added.", result)

    def test_add_notes_when_course_is_in_courses(self):
        result = self.student2.add_notes("course 1", "notes test")
        self.assertEqual({"course 1": ['a', 'b', "notes test"]}, self.student2.courses)
        self.assertEqual("Notes have been updated", result)

    def test_add_notes_when_no_course_raise_error(self):
        with self.assertRaises(Exception) as ex:
            self.student2.add_notes("course xx", "notes test")
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course_when_course_in_courses(self):
        result = self.student2.leave_course("course 1")
        self.assertEqual({}, self.student2.courses)
        self.assertEqual("Course has been removed", result)

    def test_leave_course_when_course_not_in_courses_raise_error(self):
        with self.assertRaises(Exception) as ex:
            self.student2.leave_course("course 2")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == '__main__':
    main()
