from repositories.repository_exception import RepositoryException

from structures.collection import *

import pickle


class StudentBinaryRepository:
    """
    Student repository class
    """

    def __init__(self, filename):
        """
        Constructor for student repository class that sets up the array of students in the repo
        """
        self.__students = Collection()
        self.__count = 1
        self.__filename = filename

        self.load_students_from_binary()

    def add(self, student):
        """
        Method for adding a student to the repo -> auto increments the ID
        student - An instance of Student
        """
        if not student.get_student_id():
            student.set_student_id(self.__count)
            self.__count += 1
        self.__students.add(student)
        self.save_students_to_binary()

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
        return gnome_sort(self.__students, sort_function=lambda student_a, student_b: student_a.get_student_id() <= student_b.get_student_id())

    def get_by_group(self, group):
        """
        Method for retrieving all the students from a given group
        group - The group of students (integer)
        output: An array of students part of a given group
        """
        return filter_items(self.__students, filter_function=lambda student: student.get_group() == group)

    def update(self, student_id, student):
        self.__students[self.find_student_index(student_id)] = student
        self.save_students_to_binary()

    def delete(self, student_id, should_decrement):
        if should_decrement:
            self.__count -= 1
        del self.__students[self.find_student_index(student_id)]
        self.save_students_to_binary()

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
            result += str(student) + '\n'
        return result

    def __repr__(self):
        return str(self)

    def load_students_from_binary(self):
        try:
            file = open(self.__filename, 'rb')
            for student in pickle.load(file):
                self.__students.add(student)
            self.__count = self.__students[-1].get_student_id() + 1
        except EOFError:
            self.__students = Collection()
        except IOError as e:
            raise e

    def save_students_to_binary(self):
        file = open(self.__filename, 'wb')
        pickle.dump(self.__students, file)
        file.close()
