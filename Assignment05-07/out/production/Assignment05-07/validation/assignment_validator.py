from datetime import date
from validation.validation_exception import ValidationException
from domain.assignment import Assignment


class AssignmentValidator:

    def validate(self, assignment):
        """
        Validate if provided Client instance is valid
        client - Instance of Client type
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
