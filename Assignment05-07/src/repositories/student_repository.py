from repositories.repository_exception import RepositoryException


class StudentRepository:
    """
    Student repository class
    """

    def __init__(self):
        """
        Constructor for student repository class that sets up the array of students in the repo
        """
        self.__students = []
        self.__count = 1

    def add(self, student):
        """
        Method for adding a student to the repo -> auto increments the ID
        student - An instance of Student
        """
        student.set_student_id(self.__count)
        self.__students.append(student)
        self.__count += 1

    def get(self, student_id):
        """
        Method for retrieving a student based on it's ID
        student_id - The student's ID (integer)
        output: The student with the given ID
        """
        return self.__students[self.find_student_index(student_id)]

    def get_all(self):
        """
        Method for retrieving all the students
        output: An array of all the students in the repo
        """
        return self.__students

    def get_by_group(self, group):
        """
        Method for retrieving all the students from a given group
        group - The group of students (integer)
        output: An array of assignments part of a given group
        """
        return [student for student in self.__students if student.get_group() == group]

    def update(self, student_id, student):
        self.__students[self.find_student_index(student_id)] = student

    def delete(self, student_id):
        del self.__students[self.find_student_index(student_id)]

    def find_student_index(self, student_id):
        for index in range(len(self.__students)):
            if self.__students[index].get_student_id() == student_id:
                return index
        raise RepositoryException(["No student found with the given ID."])

    def __len__(self):
        return len(self.__students)

    def __str__(self):
        result = "Students in the list: \n"
        for student in self.__students:
            result += str(student) + "\n"
        return result

    def __repr__(self):
        return str(self)

