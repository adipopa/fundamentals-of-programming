from datetime import date

from domain.student import Student
from domain.assignment import Assignment
from domain.grade import Grade

from validation.student_validator import StudentValidator
from validation.assignment_validator import AssignmentValidator
from validation.grade_validator import GradeValidator

from repositories.student_repository import StudentRepository
from repositories.assignment_repository import AssignmentRepository
from repositories.grade_repository import GradeRepository

from controllers.student_controller import StudentController
from controllers.assignment_controller import AssignmentController
from controllers.grade_controller import GradeController

from ui.menu import MenuUI

'''
    1. We initialize the validators
        - Validator takes care of verifying the business entities
        - Helpers for validating the models in the program's domain
'''

student_validator = StudentValidator()
assignment_validator = AssignmentValidator()
grade_validator = GradeValidator()

'''
    2. We initialize the repositories
        - Repository holds the business entities
        - Acts like the program's database
        - Might include some data validation
        - Does not know about any other components
'''
student_repository = StudentRepository()
assignment_repository = AssignmentRepository()
grade_repository = GradeRepository()

'''
    Add a few items to the student repository
'''
student_repository.add(Student(None, 'P1', 916))
student_repository.add(Student(None, 'T2', 914))
student_repository.add(Student(None, 'K3', 915))
student_repository.add(Student(None, 'H4', 916))
student_repository.add(Student(None, 'E5', 916))
student_repository.add(Student(None, 'F6', 913))
student_repository.add(Student(None, 'I7', 914))
student_repository.add(Student(None, 'L8', 914))
student_repository.add(Student(None, 'U9', 915))
student_repository.add(Student(None, 'R10', 913))

'''
    Add a few items to the assignment repository
'''
assignment_repository.add(Assignment(None, 'B1', date(2018, 10, 29)))
assignment_repository.add(Assignment(None, 'O2', date(2018, 11, 6)))
assignment_repository.add(Assignment(None, 'P3', date(2018, 11, 13)))
assignment_repository.add(Assignment(None, 'Y4', date(2018, 11, 20)))
assignment_repository.add(Assignment(None, 'X5', date(2018, 11, 27)))
assignment_repository.add(Assignment(None, 'W6', date(2018, 11, 29)))
assignment_repository.add(Assignment(None, 'A7', date(2018, 12, 6)))
assignment_repository.add(Assignment(None, 'G8', date(2018, 12, 13)))
assignment_repository.add(Assignment(None, 'D9', date(2018, 12, 20)))
assignment_repository.add(Assignment(None, 'N10', date(2018, 12, 27)))

'''
    Add a few items to the grade repository
'''
grade_repository.add(Grade(2, 7, None))
grade_repository.add(Grade(9, 3, 9))
grade_repository.add(Grade(3, 8, None))
grade_repository.add(Grade(8, 2, None))
grade_repository.add(Grade(4, 9, None))
grade_repository.add(Grade(7, 3, None))
grade_repository.add(Grade(7, 6, None))
grade_repository.add(Grade(7, 6, 10))
grade_repository.add(Grade(5, 4, None))
grade_repository.add(Grade(6, 5, None))

'''
    3. We initialize the controllers
        - The controller implements the program's 'operations'
        - Knows only about the repository layer
        - 'Talks' to the repository and UI using parameter passing and expcetions
'''
student_controller = StudentController(student_validator, student_repository)
assignment_controller = AssignmentController(assignment_validator, assignment_repository)
grade_controller = GradeController(grade_validator, grade_repository, student_repository, assignment_repository)

'''
    4. Initialize the user interface
        - The UI implements all user interactions
        - Only knows about the controller layer
        - Calls functions from the controller to implement program features
        - Might include some data validation, as a fast-fail mechanism
'''
menu_ui = MenuUI(student_controller, assignment_controller, grade_controller)

'''
    5. Start the application's user interface
'''
menu_ui.run_main_menu()
