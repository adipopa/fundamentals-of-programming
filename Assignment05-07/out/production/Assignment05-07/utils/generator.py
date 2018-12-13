from domain.student import Student
from domain.assignment import Assignment
from domain.grade import Grade

from datetime import date
import calendar

import random


class Generator:
    """
    Generator class for generating the initial data in the repositories
    """

    def __init__(self, student_repository, assignment_repository, grade_repository):
        self.__student_repository = student_repository
        self.__assignment_repository = assignment_repository
        self.__grade_repository = grade_repository

        self.__first_names = ['James', 'John', 'Robert', 'Michael', 'William', 'David', 'Richard', 'Joseph', 'Thomas', 'Charles', 'Mary', 'Patricia', 'Jennifer', 'Linda', 'Elizabeth', 'Barbara', 'Susan', 'Jessica', 'Sarah', 'Margaret']
        self.__last_names = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown', 'David', 'Miller', 'Wilson', 'Moore', 'Taylor', 'Anderson', 'Thomas', 'Jackson', 'White', 'Harris']
        self.__words = ['time', 'person', 'year', 'way', 'day', 'brown', 'move', 'airplane', 'jump', 'game', 'instant', 'home', 'camp', 'take', 'blue', 'mountain', 'sea', 'sun', 'work', 'clock']

    def generate_students(self, amount):
        for value in range(amount):
            name = Generator.get_random_object(self.__first_names) + ' ' + Generator.get_random_object(self.__last_names)
            group = Generator.get_random_number(900, 920)
            self.__student_repository.add(Student(None, name, group))

    def generate_assignments(self, amount):
        for value in range(amount):
            description = ''
            for _ in range(3):
                description += Generator.get_random_object(self.__words) + ' '
            year = Generator.get_random_number(2018, 2020)
            month = Generator.get_random_number(1, 12)
            day = Generator.get_random_number(1, calendar.monthrange(year, month)[1])
            self.__assignment_repository.add(Assignment(None, description[:-1].capitalize(), date(year, month, day)))

    def generate_grades(self, amount):
        for value in range(amount):
            assignment_id = Generator.get_random_number(1, 100)
            student_id = Generator.get_random_number(1, 100)
            grade = Generator.get_random_number(2, 10)
            self.__grade_repository.add(Grade(assignment_id, student_id, grade if grade >= 6 else None))

    @staticmethod
    def get_random_object(list_of_objects):
        random_index = random.randint(0, len(list_of_objects) - 1)
        return list_of_objects[random_index]

    @staticmethod
    def get_random_number(start_index, end_index):
        return random.randint(start_index, end_index)
