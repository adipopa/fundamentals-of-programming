from domain.assignment import Assignment


class AssignmentController:
    """
    Write specification here
    """
    def __init__(self, assignment_validator, assignment_repository):
        """
        Write specification here
        """
        self.__assignment_validator = assignment_validator
        self.__assignment_repository = assignment_repository

    def create_assignment(self, description, deadline):
        """
        Write specification here
        """
        assignment = Assignment(None, description, deadline)
        self.__assignment_validator.validate(assignment)
        self.__assignment_repository.add(assignment)

    def update_assignment(self, assignment_id, description, deadline):
        """
        Write specification here
        """
        assignment = Assignment(assignment_id, description, deadline)
        self.__assignment_validator.validate(assignment)
        self.__assignment_repository.update(assignment_id, assignment)

    def delete_assignment(self, assignment_id):
        """
        Write specification here
        """
        self.__assignment_repository.delete(assignment_id)

    def retrieve_assignments(self):
        """
        Write specification here
        """
        return self.__assignment_repository.get_all()
