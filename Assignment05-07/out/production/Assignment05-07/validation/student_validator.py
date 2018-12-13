from validation.validation_exception import ValidationException
from domain.student import Student


class StudentValidator:
    """
    Student validator class
    """

    def validate(self, student):
        """
        Validate if provided Student instance is valid
        student - Instance of Student type
        Return List of validation errors. An empty list if instance is valid.
        """
        if not isinstance(student, Student):
            raise TypeError("Not a student")
        _errors = []
        if len(student.get_name()) == 0:
            _errors.append("Name invalid.")
        if student.get_group() <= 0:
            _errors.append("Group invalid.")
        if len(_errors) != 0:
            raise ValidationException(_errors)
