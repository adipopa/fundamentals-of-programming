from repositories.repository_exception import RepositoryException


class AssignmentRepository:

    def __init__(self):
        self.__assignments = []
        self.__count = 1

    def add(self, assignment):
        assignment.set_assignment_id(self.__count)
        self.__assignments.append(assignment)
        self.__count += 1

    def get(self, assignment_id):
        return self.__assignments[self.find_assignment_index(assignment_id)]

    def get_all(self):
        return self.__assignments

    def update(self, assignment_id, assignment):
        self.__assignments[self.find_assignment_index(assignment_id)] = assignment

    def delete(self, assignment_id):
        del self.__assignments[self.find_assignment_index(assignment_id)]

    def find_assignment_index(self, assignment_id):
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
