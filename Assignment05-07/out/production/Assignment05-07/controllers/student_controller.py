from domain.student import Student


class StudentController:
    """
    Write specification here
    """
    def __init__(self, student_validator, student_repository):
        """
        Write specification here
        """
        self.__student_validator = student_validator
        self.__student_repository = student_repository

    def create_student(self, name, group):
        """
        Write specification here
        """
        student = Student(0, name, group)
        self.__student_validator.validate(student)
        self.__student_repository.add(student)

    def update_student(self, student_id, name, group):
        """
        Write specification here
        """
        student = Student(student_id, name, group)
        self.__student_validator.validate(student)
        self.__student_repository.update(student_id, student)

    def delete_student(self, student_id):
        """
        Write specification here
        """
        self.__student_repository.delete(student_id)

    def retrieve_students(self):
        """
        Write specification here
        """
        return self.__student_repository.get_all()

    def retrieve_students_by_group(self, group):
        """
        Write specification here
        """
        return self.__student_repository.get_by_group(group)
