from unittest import TestCase

from domain.grade import Grade

from validation.grade_validator import GradeValidator
from validation.validation_exception import ValidationException


class TestGradeValidator(TestCase):

    def setUp(self):
        self.__grade_validator = GradeValidator()

    def test_validate(self):
        grade = Grade(4, 7, None)
        self.assertTrue(self.__grade_validator.validate, grade)
        grade2 = Grade(6, None, 8)
        self.assertRaises(ValidationException, self.__grade_validator.validate, grade2)
