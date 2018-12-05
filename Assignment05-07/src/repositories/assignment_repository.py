from repositories.repository_exception import RepositoryException


class AssignmentRepository:
    """
    Assignment repository class
    """

    def __init__(self):
        """
        Constructor for assignment repository class that sets up the array of assignments in the repo
        """
        self.__assignments = []
        self.__count = 1

    def add(self, assignment):
        """
        Method for adding an assignment to the repo -> auto increments the ID
        assignment - An instance of Assignment
        """
        assignment.set_assignment_id(self.__count)
        self.__assignments.append(assignment)
        self.__count += 1

    def get(self, assignment_id):
        """
        Method for retrieving an assignment based on it's ID
        assignment_id - The assignment's ID (integer)
        output: The assignment with the given ID
        """
        return self.__assignments[self.find_assignment_index(assignment_id)]

    def get_all(self):
        """
        Method for retrieving all the assignments
        output: An array of all the assignments in the repo
        """
        return self.__assignments

    def update(self, assignment_id, assignment):
        """
        Method for updating an assignment based on ID
        assignment_id - The assignment's ID (integer)
        assignment - An instance of Assignment
        """
        self.__assignments[self.find_assignment_index(assignment_id)] = assignment

    def delete(self, assignment_id):
        """
        Method for deleting an assignment based on ID
        assignment_id - The assignment's ID (integer)
        """
        del self.__assignments[self.find_assignment_index(assignment_id)]

    def find_assignment_index(self, assignment_id):
        """
        Method for finding the index of an assignment based on ID
        assignment_id - The assignment's ID (integer)
        output: The index of the assignment with the given ID
        """
        for index in range(len(self.__assignments)):
            if self.__assignments[index].get_assignment_id() == assignment_id:
                return index
        raise RepositoryException(["No assignment found with the given ID."])

    def __len__(self):
        return len(self.__assignments)

    def __str__(self):
        result = "Assignments in the list: \n"
        for assignment in self.__assignments:
            result += str(assignment) + "\n"
        return result

    def __repr__(self):
        return str(self)
