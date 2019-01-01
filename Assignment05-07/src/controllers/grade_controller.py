from datetime import date

from domain.grade import Grade

from structures.collection import *

from utils.helper import Helper
intersection = Helper.intersection
average_grade_from_list = Helper.average_grade_from_list


class GradeController:
    """
    Grade controller class
    """

    def __init__(self, grade_validator, grade_repository, student_repository, assignment_repository):
        """
        Constructor for grade controller class
        grade_validator - The grade validator for validating a grade
        grade_repository - The grade repository for CRUD operations on grades
        student_repository - The student repository for CRUD operations on students
        assignment_repository - The assignment repository for CRUD operations on assignments
        """
        self.__grade_validator = grade_validator
        self.__grade_repository = grade_repository
        self.__student_repository = student_repository
        self.__assignment_repository = assignment_repository

    def give_assignment(self, assignment_id, student_id):
        """
        Method for giving an assignment (empty grade) to a student
        assignment_id - The assignment's ID (integer)
        student_id - The student's ID (integer)
        """
        grade = Grade(assignment_id, student_id, None)
        self.__grade_validator.validate(grade)
        self.__grade_repository.add(grade)

    def give_assignment_to_group(self, assignment_id, group):
        """
        Method for giving an assignment (empty grade) to a group of students
        assignment_id - The assignment's ID (integer)
        group - A group of students (integer)
        """
        for student in self.__student_repository.get_by_group(group):
            self.give_assignment(assignment_id, student.get_student_id())

    def grade_student(self, student_id, assignment_id, grade_value):
        """
        Method for grading a student (update an empty grade)
        student_id - The student's ID (integer)
        assignment_id - The assignment's ID (integer)
        grade_value - The grade's value (integer)
        """
        grade = Grade(assignment_id, student_id, grade_value)
        self.__grade_validator.validate(grade)
        self.__grade_repository.update(assignment_id, student_id, grade)

    def delete_grade(self, assignment_id, student_id):
        """
        Method for giving an assignment (empty grade)
        assignment_id - The assignment's ID (integer)
        student_id - The student's ID (integer)
        """
        self.__grade_repository.delete(assignment_id, student_id)

    def delete_grade_by_group(self, assignment_id, group):
        """
        Method for deleting an assignment (empty grade) for a group of students
        assignment_id - The assignment's ID (integer)
        group - A group of students (integer)
        """
        for student in self.__student_repository.get_by_group(group):
            self.delete_grade(assignment_id, student.get_student_id())

    def retrieve_grades(self):
        """
        Method for retrieving all students
        output: an array of students from the repository
        """
        return self.__grade_repository.get_all()

    def retrieve_ungraded_assignments_by_student(self, student_id):
        """
        Method for retrieving all the ungraded assignments for a given student
        output: an array of assignments from the repository
        """
        grades_by_student = self.__grade_repository.get_by_student(student_id)
        grades_by_grade = self.__grade_repository.get_by_grade(is_graded=False)
        ungraded_assignments = Collection()
        for grade in intersection(grades_by_student, grades_by_grade):
            ungraded_assignments.add(self.__assignment_repository.get(grade.get_assignment_id()))
        return ungraded_assignments

    def retrieve_students_by_assignment(self, assignment_id):
        """
        Method for retrieving all students by a given assignment
        output: an array of students from the repository
        """
        grades_by_assignment = self.__grade_repository.get_by_assignment(assignment_id)
        students_by_assignment = Collection()
        for grade in grades_by_assignment:
            students_by_assignment.add(self.__student_repository.get(grade.get_student_id()))
        return gnome_sort(students_by_assignment, sort_fn=lambda student_a, student_b: student_a.get_name() <= student_b.get_name())

    def retrieve_late_students(self):
        late_students = Collection()
        for student in self.__student_repository.get_all():
            ungraded_assignments = self.retrieve_ungraded_assignments_by_student(student.get_student_id())
            for assignment in ungraded_assignments:
                if assignment.get_deadline() < date.today():
                    late_students.add(student)
                    break
        return late_students

    def retrieve_best_students(self):
        best_students = self.__student_repository.get_all()
        return gnome_sort(best_students, sort_fn=lambda student_a, student_b: self.average_student_grade(student_a.get_student_id()) >= self.average_student_grade(student_b.get_student_id()))

    def retrieve_assignments_by_average_grade(self):
        assignments_by_average_grade = Collection()
        for assignment in self.__assignment_repository.get_all():
            grades_by_assignment = self.__grade_repository.get_by_assignment(assignment.get_assignment_id())
            grades_by_grade = self.__grade_repository.get_by_grade(is_graded=True)
            if len(intersection(grades_by_assignment, grades_by_grade)) != 0:
                assignments_by_average_grade.add(assignment)
        return gnome_sort(assignments_by_average_grade, sort_fn=lambda assignment_a, assignment_b: self.average_assignment_grade(assignment_a.get_assignment_id()) <= self.average_assignment_grade(assignment_b.get_assignment_id()))

    def average_student_grade(self, student_id):
        grades_by_student = self.__grade_repository.get_by_student(student_id)
        grades_by_grade = self.__grade_repository.get_by_grade(is_graded=True)
        grades = intersection(grades_by_student, grades_by_grade)
        return average_grade_from_list(grades)

    def average_assignment_grade(self, assignment_id):
        grades_by_assignment = self.__grade_repository.get_by_assignment(assignment_id)
        grades_by_grade = self.__grade_repository.get_by_grade(is_graded=True)
        grades = intersection(grades_by_assignment, grades_by_grade)
        return average_grade_from_list(grades)
