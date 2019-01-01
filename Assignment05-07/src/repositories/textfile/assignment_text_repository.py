from repositories.repository_exception import RepositoryException

from domain.assignment import Assignment

from structures.collection import *

from utils.helper import Helper


class AssignmentTextRepository:
    """
    Assignment repository class
    """

    def __init__(self, filename):
        """
        Constructor for assignment repository class that sets up the array of assignments in the repo
        """
        self.__assignments = Collection()
        self.__count = 1
        self.__filename = filename

        self.load_assignments()

    def add(self, assignment):
        """
        Method for adding an assignment to the repo -> auto increments the ID
        assignment - An instance of Assignment
        """
        if not assignment.get_assignment_id():
            assignment.set_assignment_id(self.__count)
            self.__count += 1
        self.__assignments.add(assignment)
        self.save_assignments()

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
        return gnome_sort(self.__assignments, sort_fn=lambda assignment_a, assignment_b: assignment_a.get_assignment_id() <= assignment_b.get_assignment_id())

    def update(self, assignment_id, assignment):
        """
        Method for updating an assignment based on ID
        assignment_id - The assignment's ID (integer)
        assignment - An instance of Assignment
        """
        self.__assignments[self.find_assignment_index(assignment_id)] = assignment
        self.save_assignments()

    def delete(self, assignment_id, should_decrement):
        """
        Method for deleting an assignment based on ID
        assignment_id - The assignment's ID (integer)
        """
        if should_decrement:
            self.__count -= 1
        del self.__assignments[self.find_assignment_index(assignment_id)]
        self.save_assignments()

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
            result += str(assignment) + '\n'
        return result

    def __repr__(self):
        return str(self)

    def load_assignments(self):
        try:
            file = open(self.__filename, 'r')
            line = file.readline().strip()
            while len(line) > 0:
                line = line.split(',')
                self.__assignments.add(Assignment(int(line[0]), line[1], Helper.resolve_date(line[2])))
                self.__count += 1
                line = file.readline().strip()
            file.close()
        except IOError as e:
            raise e

    def save_assignments(self):
        file = open(self.__filename, 'w')
        try:
            for assignment in self.__assignments:
                assignment_string = str(assignment.get_assignment_id()) + ',' + assignment.get_description() + ',' + \
                                    assignment.get_deadline().strftime('%d/%m/%Y') + '\n'
                file.write(assignment_string)
            file.close()
        except Exception as e:
            raise e
