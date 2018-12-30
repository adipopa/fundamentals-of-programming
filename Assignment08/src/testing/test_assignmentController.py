from unittest import TestCase

from datetime import date

from validation.assignment_validator import AssignmentValidator
from repositories.inmemory.assignment_repository import AssignmentRepository
from controllers.assignment_controller import AssignmentController


class TestAssignmentController(TestCase):

    def setUp(self):
        self.__assignment_controller = AssignmentController(AssignmentValidator(), AssignmentRepository())

    def test_create_assignment(self):
        description = "Phone Book"
        deadline = date(2019, 2, 19)
        self.assertEqual(len(self.__assignment_controller.retrieve_assignments()), 0)
        self.__assignment_controller.create_assignment(description, deadline)
        self.assertEqual(len(self.__assignment_controller.retrieve_assignments()), 1)

    def test_update_assignment(self):
        pass

    def test_delete_assignment(self):
        pass

    def test_get_assignment(self):
        pass

    def test_retrieve_assignments(self):
        pass
