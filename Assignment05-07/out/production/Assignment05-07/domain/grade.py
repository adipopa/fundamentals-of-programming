class Grade:

    def __init__(self, assignment_id, student_id, grade=None):
        self.__assignment_id = assignment_id
        self.__student_id = student_id
        self.__grade = grade

    def __eq__(self, other):
        return self.__assignment_id == other.__assignment_id and self.__student_id == other.__student_id

    def get_assignment_id(self):
        return self.__assignment_id

    def get_student_id(self):
        return self.__student_id

    def get_grade(self):
        return self.__grade

    def __repr__(self):
        return str(self)
