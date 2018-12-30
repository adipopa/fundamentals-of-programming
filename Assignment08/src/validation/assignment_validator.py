from datetime import date
from validation.validation_exception import ValidationException
from domain.assignment import Assignment


class AssignmentValidator:
    """
    Assignment validator class
    """

    def validate(self, assignment):
        """
        Validate if provided Assignment instance is valid
        assignment - Instance of Assignment type
        Return List of validation errors. An empty list if instance is valid.
        """
        if not isinstance(assignment, Assignment):
            raise TypeError("Not an assignment")
        _errors = []
        if len(assignment.get_description()) == 0:
            _errors.append("Description invalid.")
        if not isinstance(assignment.get_deadline(), date) or assignment.get_deadline() < date.today():
            _errors.append("Deadline invalid.")
        if len(_errors) != 0:
            raise ValidationException(_errors)
