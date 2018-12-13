from domain.student import Student


class StudentController:
    """
    Student controller class
    """

    def __init__(self, student_validator, student_repository):
        """
        Constructor for student controller class
        student_validator - The student validator for validating a student
        student_repository - The student repository for CRUD operations on students
        """
        self.__student_validator = student_validator
        self.__student_repository = student_repository

    def create_student(self, name, group, student_id=None):
        """
        Method for creating a student
        name - The student's name (string)
        group - The student's group (integer)
        """
        student = Student(student_id, name, group)
        self.__student_validator.validate(student)
        self.__student_repository.add(student)
        return self.__student_repository.get_all()[-1].get_student_id()

    def update_student(self, student_id, name, group):
        """
        Method for updating a student
        student_id - The student's ID (integer)
        name - The student's name (string)
        group - The student's group (integer)
        """
        student = Student(student_id, name, group)
        self.__student_validator.validate(student)
        self.__student_repository.update(student_id, student)

    def delete_student(self, student_id, should_decrement=False):
        """
        Method for deleting a student
        student_id - The student's ID (integer)
        """
        self.__student_repository.delete(student_id, should_decrement)

    def get_student(self, student_id):
        return self.__student_repository.get(student_id)

    def retrieve_students(self):
        """
        Method for retrieving all students
        output: an array of students from the repository
        """
        return self.__student_repository.get_all()

    def retrieve_students_by_group(self, group):
        """
        Method for retrieving all students by a given group
        output: an array of students from the repository
        """
        return self.__student_repository.get_by_group(group)
