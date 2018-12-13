from unittest import TestCase

from domain.student import Student

from validation.student_validator import StudentValidator
from validation.validation_exception import ValidationException


class TestStudentValidator(TestCase):

    def setUp(self):
        self.__student_validator = StudentValidator()

    def test_validate(self):
        student = Student(4, "Adrian Popa", 916)
        self.assertTrue(self.__student_validator.validate, student)
        student2 = Student(6, "", 917)
        self.assertRaises(ValidationException, self.__student_validator.validate, student2)
