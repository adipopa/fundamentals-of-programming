from repositories.repository_exception import RepositoryException


class GradeRepository:

    def __init__(self):
        self.__grades = []

    def add(self, grade):
        if not any(grd == grade for grd in self.__grades):
            self.__grades.append(grade)

    def update(self, assignment_id, student_id, grade):
        grade_index = self.find_grade_index(assignment_id, student_id)
        self.__grades[grade_index] = grade

    def get_ungraded_by_student(self, student_id):
        return [grade for grade in self.__grades if grade.get_student_id() == student_id and grade.get_grade() is None]

    def get_by_assignment(self, assignment_id):
        return [grade for grade in self.__grades if grade.get_assignment_id() == assignment_id]

    def find_grade_index(self, assignment_id, student_id):
        for index in range(len(self.__grades)):
            grade = self.__grades[index]
            if grade.get_assignment_id() == assignment_id and grade.get_student_id() == student_id:
                return index
        raise RepositoryException(["No assignment found with the given ID for this student."])

    def __len__(self):
        return len(self.__grades)
