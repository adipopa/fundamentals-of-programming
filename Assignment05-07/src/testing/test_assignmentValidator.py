from unittest import TestCase

from datetime import date

from domain.assignment import Assignment

from validation.assignment_validator import AssignmentValidator
from validation.validation_exception import ValidationException


class TestAssignmentValidator(TestCase):

    def setUp(self):
        self.__assignment_validator = AssignmentValidator()

    def test_validate(self):
        assignment = Assignment(5, "Test", date(2018, 12, 17))
        self.assertTrue(self.__assignment_validator.validate, assignment)
        assignment2 = Assignment(7, "", date(2018, 12, 17))
        self.assertRaises(ValidationException, self.__assignment_validator.validate, assignment2)
