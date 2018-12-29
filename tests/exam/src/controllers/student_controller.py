from domain.student import Student


class StudentController:

    def __init__(self, student_validator, student_repository):
        self.__student_validator = student_validator
        self.__student_repository = student_repository

    def add_student(self, id, name, attendance_count, grade):
        student = Student(id, name, attendance_count, grade)
        self.__student_validator.validate(student)
        self.__student_repository.add(student)

    def give_bonus(self, p, b):
        for student in self.__student_repository.get_by_attendances(p):
            new_grade = student.get_grade() + b
            student.set_grade(new_grade if new_grade <= 10 else 10)
            self.__student_repository.update(student)

    def retrieve_students_by_name(self, name):
        return self.__student_repository.get_by_name(name)
