class Student:
    """
    Student domain class
    """

    def __init__(self, student_id, name, group):
        self.__student_id = student_id
        self.__name = name
        self.__group = group

    def set_student_id(self, student_id):
        self.__student_id = student_id

    def get_student_id(self):
        return self.__student_id

    def get_name(self):
        return self.__name

    def get_group(self):
        return self.__group

    def __str__(self):
        return 'ID: ' + str(self.__student_id) + ', name: ' + self.__name + ', group: ' + str(self.__group)

    def __repr__(self):
        return str(self)
