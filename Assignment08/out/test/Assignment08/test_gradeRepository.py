from unittest import TestCase

from domain.grade import Grade
from repositories.inmemory.grade_repository import GradeRepository


class TestGradeRepository(TestCase):

    def setUp(self):
        self.__grade_repository = GradeRepository()
        self.__grade = Grade(3, 7, None)

    def test_add(self):
        self.assertEqual(len(self.__grade_repository), 0)
        self.__grade_repository.add(self.__grade)
        self.assertEqual(len(self.__grade_repository), 1)
        grade2 = Grade(5, 8, None)
        self.__grade_repository.add(grade2)
        self.assertEqual(len(self.__grade_repository), 2)
        self.assertEqual(self.__grade_repository.get_all()[1], grade2)

    def test_update(self):
        self.__grade_repository.add(self.__grade)
        new_grade = Grade(1, 4, 9)
        self.__grade_repository.update(3, 7, new_grade)
        self.assertEqual(self.__grade_repository.get_all()[0], new_grade)

    def test_get_all(self):
        self.__grade_repository.add(self.__grade)
        self.assertEqual(self.__grade_repository.get_all(), [self.__grade])

    def test_delete(self):
        self.__grade_repository.add(self.__grade)
        self.__grade_repository.delete(3, 7)
        self.assertEqual(len(self.__grade_repository.get_all()), 0)

    def test_get_by_assignment(self):
        self.__grade_repository.add(self.__grade)
        self.assertEqual(self.__grade_repository.get_by_assignment(3)[0], self.__grade)

    def test_get_by_student(self):
        self.__grade_repository.add(self.__grade)
        self.assertEqual(self.__grade_repository.get_by_student(7)[0], self.__grade)

    def test_get_by_grade(self):
        self.__grade_repository.add(self.__grade)
        self.assertEqual(self.__grade_repository.get_by_grade(is_graded=False)[0], self.__grade)

    def test_find_grade_index(self):
        self.__grade_repository.add(self.__grade)
        grade_index = self.__grade_repository.find_grade_index(3, 7)
        self.assertEqual(grade_index, 0)
