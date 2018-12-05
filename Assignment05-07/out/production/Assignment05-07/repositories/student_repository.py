from repositories.repository_exception import RepositoryException


class StudentRepository:

    def __init__(self):
        self.__students = []
        self.__count = 1

    def add(self, student):
        student.set_student_id(self.__count)
        self.__students.append(student)
        self.__count += 1

    def get(self, student_id):
        return self.__students[self.find_student_index(student_id)]

    def get_all(self):
        return self.__students

    def get_by_group(self, group):
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

