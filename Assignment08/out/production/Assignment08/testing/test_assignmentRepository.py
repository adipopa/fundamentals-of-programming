from unittest import TestCase

from datetime import date

from domain.assignment import Assignment
from repositories.inmemory.assignment_repository import AssignmentRepository


class TestAssignmentRepository(TestCase):

    def setUp(self):
        self.__assignment_repository = AssignmentRepository()
        self.__assignment = Assignment(None, "Test", date(2018, 12, 17))

    def test_add(self):
        self.assertEqual(len(self.__assignment_repository), 0)
        self.__assignment_repository.add(self.__assignment)
        self.assertEqual(len(self.__assignment_repository), 1)
        assignment2 = Assignment(None, "Test2", date(2018, 11, 19))
        self.__assignment_repository.add(assignment2)
        self.assertEqual(len(self.__assignment_repository), 2)
        self.assertEqual(self.__assignment_repository.get_all()[1], assignment2)

    def test_get(self):
        self.__assignment_repository.add(self.__assignment)
        self.assertEqual(self.__assignment_repository.get(1), self.__assignment)

    def test_get_all(self):
        self.__assignment_repository.add(self.__assignment)
        self.assertEqual(self.__assignment_repository.get_all(), [self.__assignment])

    def test_update(self):
        self.__assignment_repository.add(self.__assignment)
        new_assignment = Assignment(1, "Updated", date(2018, 12, 17))
        self.__assignment_repository.update(1, new_assignment)
        self.assertEqual(self.__assignment_repository.get_all()[0], new_assignment)

    def test_delete(self):
        self.__assignment_repository.add(self.__assignment)
        self.__assignment_repository.delete(1)
        self.assertEqual(len(self.__assignment_repository.get_all()), 0)

    def test_find_assignment_index(self):
        self.__assignment_repository.add(self.__assignment)
        assignment_index = self.__assignment_repository.find_assignment_index(1)
        self.assertEqual(assignment_index, 0)
