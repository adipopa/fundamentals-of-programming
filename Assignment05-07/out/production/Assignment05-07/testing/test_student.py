from unittest import TestCase

from domain.student import Student


class TestStudent(TestCase):

    def setUp(self):
        self.__student = Student(1, "Popa Adrian", 916)

    def test_set_student_id(self):
        self.__student.set_student_id(7)
        self.assertEqual(self.__student.get_student_id(), 7)

    def test_get_student_id(self):
        self.assertEqual(self.__student.get_student_id(), 1)

    def test_get_name(self):
        self.assertEqual(self.__student.get_name(), "Popa Adrian")

    def test_get_group(self):
        self.assertEqual(self.__student.get_group(), 916)
