from domain.assignment import Assignment


class AssignmentController:
    """
    Assignment controller class
    """

    def __init__(self, assignment_validator, assignment_repository):
        """
        Constructor for assignment controller class
        assignment_validator - The assignment validator for validating an assignment
        assignment_repository - The assignment repository for CRUD operations on assignments
        """
        self.__assignment_validator = assignment_validator
        self.__assignment_repository = assignment_repository

    def create_assignment(self, description, deadline):
        """
        Method for creating an assignment
        description - The assignment's description (string)
        deadline - The assignment's deadline (consisting of a date)
        """
        assignment = Assignment(None, description, deadline)
        self.__assignment_validator.validate(assignment)
        self.__assignment_repository.add(assignment)

    def update_assignment(self, assignment_id, description, deadline):
        """
        Method for updating an assignment
        assignment_id - The assignment's ID (integer)
        description - The assignment's description (string)
        deadline - The assignment's deadline (consisting of a date)
        """
        assignment = Assignment(assignment_id, description, deadline)
        self.__assignment_validator.validate(assignment)
        self.__assignment_repository.update(assignment_id, assignment)

    def delete_assignment(self, assignment_id):
        """
        Method for deleting an assignment
        assignment_id - The assignment's ID (integer)
        """
        self.__assignment_repository.delete(assignment_id)

    def retrieve_assignments(self):
        """
        Method for retrieving all assignments
        output: an array of assignments from the repository
        """
        return self.__assignment_repository.get_all()
