from repositories.repository_exception import RepositoryException

import pickle


class GradeBinaryRepository:
    """
    Grade repository class
    """

    def __init__(self, filename):
        """
        Constructor for grade repository class that sets up the array of grades in the repo
        """
        self.__grades = []
        self.__filename = filename

        self.load_grades_from_binary()

    def add(self, grade):
        """
        Method for adding a grade to the repo
        grade - An instance of Grade
        """
        if not any(old_grade == grade for old_grade in self.__grades):
            self.__grades.append(grade)
        self.save_grades_to_binary()

    def update(self, assignment_id, student_id, grade):
        grade_index = self.find_grade_index(assignment_id, student_id)
        self.__grades[grade_index] = grade
        self.save_grades_to_binary()

    def delete(self, assignment_id, student_id):
        """
        Method for deleting a grade based on assignment and student IDs
        assignment_id - The assignment's ID (integer)
        student_id - The student's ID (integer)
        """
        del self.__grades[self.find_grade_index(assignment_id, student_id)]
        self.save_grades_to_binary()

    def get_all(self):
        """
        Method for retrieving all the grades
        output: An array of all the grades in the repo
        """
        return sorted(self.__grades, key=lambda grade: (grade.get_assignment_id(), grade.get_student_id()))

    def get_by_assignment(self, assignment_id):
        return [grade for grade in self.__grades if grade.get_assignment_id() == assignment_id]

    def get_by_student(self, student_id):
        return [grade for grade in self.__grades if grade.get_student_id() == student_id]

    def get_by_grade(self, is_graded):
        return [grade for grade in self.__grades if (grade.get_grade() is not None if is_graded else grade.get_grade() is None)]

    def find_grade_index(self, assignment_id, student_id):
        for index in range(len(self.__grades)):
            grade = self.__grades[index]
            if grade.get_assignment_id() == assignment_id and grade.get_student_id() == student_id:
                return index
        raise RepositoryException(["No assignment found with the given ID for this student."])

    def __len__(self):
        return len(self.__grades)

    def load_grades_from_binary(self):
        try:
            file = open(self.__filename, 'rb')
            self.__grades = pickle.load(file)
        except EOFError:
            self.__grades = []
        except IOError as e:
            raise e

    def save_grades_to_binary(self):
        file = open(self.__filename, 'wb')
        pickle.dump(self.__grades, file)
        file.close()
