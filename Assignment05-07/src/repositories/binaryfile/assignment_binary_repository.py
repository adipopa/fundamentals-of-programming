from repositories.repository_exception import RepositoryException

from structures.collection import *

import pickle


class AssignmentBinaryRepository:
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

        self.load_assignments_from_binary()

    def add(self, assignment):
        """
        Method for adding an assignment to the repo -> auto increments the ID
        assignment - An instance of Assignment
        """
        if not assignment.get_assignment_id():
            assignment.set_assignment_id(self.__count)
            self.__count += 1
        self.__assignments.add(assignment)
        self.save_assignments_to_binary()

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
        self.save_assignments_to_binary()

    def delete(self, assignment_id, should_decrement):
        """
        Method for deleting an assignment based on ID
        assignment_id - The assignment's ID (integer)
        """
        if should_decrement:
            self.__count -= 1
        del self.__assignments[self.find_assignment_index(assignment_id)]
        self.save_assignments_to_binary()

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

    def load_assignments_from_binary(self):
        try:
            file = open(self.__filename, 'rb')
            for assignment in pickle.load(file):
                self.__assignments.add(assignment)
            self.__count = self.__assignments[-1].get_assignment_id() + 1
        except EOFError:
            self.__assignments = Collection()
        except IOError as e:
            raise e

    def save_assignments_to_binary(self):
        file = open(self.__filename, 'wb')
        pickle.dump(self.__assignments, file)
        file.close()
