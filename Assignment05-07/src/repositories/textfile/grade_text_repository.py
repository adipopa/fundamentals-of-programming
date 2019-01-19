from repositories.repository_exception import RepositoryException

from domain.grade import Grade

from structures.collection import *


class GradeTextRepository:
    """
    Grade repository class
    """

    def __init__(self, filename):
        """
        Constructor for grade repository class that sets up the array of grades in the repo
        """
        self.__grades = Collection()
        self.__filename = filename
        self.load_grades()

    def add(self, grade):
        """
        Method for adding a grade to the repo
        grade - An instance of Grade
        """
        if not any(old_grade == grade for old_grade in self.__grades):
            self.__grades.add(grade)
        self.save_grades()

    def update(self, assignment_id, student_id, grade):
        grade_index = self.find_grade_index(assignment_id, student_id)
        self.__grades[grade_index] = grade
        self.save_grades()

    def delete(self, assignment_id, student_id):
        """
        Method for deleting a grade based on assignment and student IDs
        assignment_id - The assignment's ID (integer)
        student_id - The student's ID (integer)
        """
        del self.__grades[self.find_grade_index(assignment_id, student_id)]
        self.save_grades()

    def get_all(self):
        """
        Method for retrieving all the grades
        output: An array of all the grades in the repo
        """
        sorted_by_id = gnome_sort(self.__grades, sort_function=lambda grade_a, grade_b: grade_a.get_student_id() <= grade_b.get_student_id())
        return gnome_sort(sorted_by_id, sort_function=lambda grade_a, grade_b: grade_a.get_assignment_id() <= grade_b.get_assignment_id())

    def get_by_assignment(self, assignment_id):
        return filter_items(self.__grades, filter_function=lambda grade: grade.get_assignment_id() == assignment_id)

    def get_by_student(self, student_id):
        return filter_items(self.__grades, filter_function=lambda grade: grade.get_student_id() == student_id)

    def get_by_grade(self, is_graded):
        return filter_items(self.__grades, filter_function=lambda grade: (grade.get_grade() is not None if is_graded else grade.get_grade() is None))

    def find_grade_index(self, assignment_id, student_id):
        for index in range(len(self.__grades)):
            grade = self.__grades[index]
            if grade.get_assignment_id() == assignment_id and grade.get_student_id() == student_id:
                return index
        raise RepositoryException(["No assignment found with the given ID for this student."])

    def __len__(self):
        return len(self.__grades)

    def load_grades(self):
        try:
            file = open(self.__filename, 'r')
            line = file.readline().strip()
            while len(line) > 0:
                line = line.split(',')
                self.__grades.add(Grade(int(line[0]), int(line[1]), None if line[2] == 'None' else int(line[2])))
                line = file.readline().strip()
            file.close()
        except IOError as e:
            raise e

    def save_grades(self):
        file = open(self.__filename, 'w')
        try:
            for grade in self.__grades:
                grade_string = str(grade.get_assignment_id()) + ',' + str(grade.get_student_id()) + ',' + \
                               str(grade.get_grade()) + '\n'
                file.write(grade_string)
            file.close()
        except Exception as e:
            raise e
