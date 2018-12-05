from unittest import TestCase

from datetime import date
from domain.assignment import Assignment


class TestAssignment(TestCase):

    def setUp(self):
        self.__assignment = Assignment(1, "Phone Book", date(2018, 12, 20))

    def test_set_assignment_id(self):
        self.__assignment.set_assignment_id(3)
        self.assertEqual(self.__assignment.get_assignment_id(), 3)

    def test_get_assignment_id(self):
        self.assertEqual(self.__assignment.get_assignment_id(), 1)

    def test_get_description(self):
        self.assertEqual(self.__assignment.get_description(), "Phone Book")

    def test_get_deadline(self):
        self.assertEqual(self.__assignment.get_deadline(), date(2018, 12, 20))
