from unittest import TestCase

from domain.grade import Grade


class TestGrade(TestCase):

    def setUp(self):
        self.__grade = Grade(3, 7, 9)

    def test_get_assignment_id(self):
        self.assertEqual(self.__grade.get_assignment_id(), 3)

    def test_get_student_id(self):
        self.assertEqual(self.__grade.get_student_id(), 7)

    def test_get_grade(self):
        self.assertEqual(self.__grade.get_grade(), 9)
