class Student:

    def __init__(self, id, name, attendance_count, grade):
        self.__id = id
        self.__name = name
        self.__attendance_count = attendance_count
        self.__grade = grade

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_attendance_count(self):
        return self.__attendance_count

    def get_grade(self):
        return self.__grade

    def set_grade(self, grade):
        self.__grade = grade

    def __eq__(self, other):
        return self.__id == other.__id

    def __str__(self):
        return "ID: " + str(self.__id) + ", name: " + self.__name + ", attended " + \
               str(self.__attendance_count) + " lab(s) and has the grade: " + str(self.__grade)
