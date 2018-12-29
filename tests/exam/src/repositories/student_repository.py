from domain.student import Student


class StudentRepository:

    def __init__(self):
        self.__students = StudentRepository.read_students_from_file('students.txt')

    def add(self, student):
        """
        Method for adding a student to the repo -> auto increments the ID
        student - An instance of Student
        """
        if student in self.__students:
            raise Exception("Student with the given ID already exists.")
        self.__students.append(student)

    def update(self, student):
        self.__students[self.find_student_index(student)] = student

    def get_by_attendances(self, attendances):
        return [student for student in self.__students if student.get_attendance_count() >= attendances]

    def get_by_name(self, name):
        students_by_name = [student for student in self.__students if name.lower() in student.get_name().lower()]
        return sorted(students_by_name, key=lambda student: student.get_name())

    def find_student_index(self, student):
        for student_index in range(len(self.__students)):
            if self.__students[student_index].get_id() == student.get_id():
                return student_index
        raise Exception("No student found with the given ID.")

    @staticmethod
    def read_students_from_file(file_name):
        students = []
        try:
            file = open(file_name, "r")
            line = file.readline().strip()
            while len(line) > 0:
                arguments = line.split(",")
                students.append(Student(int(arguments[0]), arguments[1], int(arguments[2]), int(arguments[3])))
                line = file.readline().strip()
            file.close()
        except IOError as io_error:
            raise io_error
        return students
