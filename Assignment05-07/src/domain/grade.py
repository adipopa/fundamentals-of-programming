class Grade:
    """
    Grade domain class
    """

    def __init__(self, assignment_id, student_id, grade=None):
        """
        Constructor for grade domain class
        assignment_id - The assignment's ID (integer)
        student_id - The student's ID (integer)
        grade - The grade's value (integer)
        """
        self.__assignment_id = assignment_id
        self.__student_id = student_id
        self.__grade = grade

    def __eq__(self, other):
        return self.__assignment_id == other.__assignment_id and self.__student_id == other.__student_id

    def __hash__(self):
        return hash((self.__assignment_id, self.__student_id))

    def get_assignment_id(self):
        return self.__assignment_id

    def get_student_id(self):
        return self.__student_id

    def get_grade(self):
        return self.__grade

    def __repr__(self):
        return str(self)
