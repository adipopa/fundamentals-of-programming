from unittest import TestCase

from domain.student import Student
from repositories.student_repository import StudentRepository


class TestStudentRepository(TestCase):

    def setUp(self):
        self.__student_repository = StudentRepository()
        self.__student = Student(None, "Test", 916)

    def test_add(self):
        self.assertEqual(len(self.__student_repository), 0)
        self.__student_repository.add(self.__student)
        self.assertEqual(len(self.__student_repository), 1)
        student2 = Student(None, "Test2", 712)
        self.__student_repository.add(student2)
        self.assertEqual(len(self.__student_repository), 2)
        self.assertEqual(self.__student_repository.get_all()[1], student2)

    def test_get(self):
        self.__student_repository.add(self.__student)
        self.assertEqual(self.__student_repository.get(1), self.__student)

    def test_get_all(self):
        self.__student_repository.add(self.__student)
        self.assertEqual(self.__student_repository.get_all(), [self.__student])

    def test_update(self):
        self.__student_repository.add(self.__student)
        new_student = Student(1, "Updated", 847)
        self.__student_repository.update(1, new_student)
        self.assertEqual(self.__student_repository.get_all()[0], new_student)

    def test_delete(self):
        self.__student_repository.add(self.__student)
        self.__student_repository.delete(1)
        self.assertEqual(len(self.__student_repository.get_all()), 0)

    def test_find_student_index(self):
        self.__student_repository.add(self.__student)
        student_index = self.__student_repository.find_student_index(1)
        self.assertEqual(student_index, 0)
