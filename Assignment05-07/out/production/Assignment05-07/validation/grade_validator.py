from validation.validation_exception import ValidationException
from domain.grade import Grade


class GradeValidator:
    """
    Grade validator class
    """

    def validate(self, grade):
        """
        Validate if provided Grade instance is valid
        grade - Instance of Grade type
        Return List of validation errors. An empty list if instance is valid.
        """
        if not isinstance(grade, Grade):
            raise TypeError("Not a grade")
        _errors = []
        if grade.get_student_id() is None:
            _errors.append("Student ID invalid.")
        if grade.get_assignment_id() is None:
            _errors.append("Assignment ID invalid.")
        if len(_errors) != 0:
            raise ValidationException(_errors)
