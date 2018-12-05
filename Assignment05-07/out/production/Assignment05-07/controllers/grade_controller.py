from domain.grade import Grade


class GradeController:

    def __init__(self, grade_validator, grade_repository, student_repository, assignment_repository):
        """
        Write specification here
        """
        self.__grade_validator = grade_validator
        self.__grade_repository = grade_repository
        self.__student_repository = student_repository
        self.__assignment_repository = assignment_repository

    def give_assignment(self, assignment_id, student_id):
        """
        Write specification here
        """
        grade = Grade(assignment_id, student_id, None)
        self.__grade_validator.validate(grade)
        self.__grade_repository.add(grade)

    def give_assignment_to_group(self, assignment_id, group):
        """
        Write specification here
        """
        for student in self.__student_repository.get_by_group(group):
            self.give_assignment(assignment_id, student.get_student_id())

    def retrieve_ungraded_assignments_by_student(self, student_id):
        """
        Write specification here
        """
        ungraded_assignments = []
        for grade in self.__grade_repository.get_ungraded_by_student(student_id):
            ungraded_assignments.append(self.__assignment_repository.get(grade.get_assignment_id()))
        return ungraded_assignments

    def retrieve_students_by_assignment(self, assignment_id):
        students = []
        for grade in self.__grade_repository.get_by_assignment(assignment_id):
            students.append(self.__student_repository.get(grade.get_student_id()))
        return sorted(students, key=lambda student: student.get_name())

    def grade_student(self, student_id, assignment_id, grade_value):
        """
        Write specification here
        """
        grade = Grade(assignment_id, student_id, grade_value)
        self.__grade_validator.validate(grade)
        self.__grade_repository.update(assignment_id, student_id, grade)
