from validation.student_validator import StudentValidator
from validation.assignment_validator import AssignmentValidator
from validation.grade_validator import GradeValidator

from repositories.student_repository import StudentRepository
from repositories.assignment_repository import AssignmentRepository
from repositories.grade_repository import GradeRepository

from controllers.student_controller import StudentController
from controllers.assignment_controller import AssignmentController
from controllers.grade_controller import GradeController
from controllers.history_controller import HistoryController

from utils.generator import Generator

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
    3. Call the generator methods for each of the student, assignment and grade repositories
'''

generator = Generator(student_repository, assignment_repository, grade_repository)

generator.generate_students(100)
generator.generate_assignments(100)
generator.generate_grades(100)

'''
    4. We initialize the controllers
        - The controller implements the program's 'operations'
        - Knows only about the repository layer
        - 'Talks' to the repository and UI using parameter passing and exceptions
'''
student_controller = StudentController(student_validator, student_repository)
assignment_controller = AssignmentController(assignment_validator, assignment_repository)
grade_controller = GradeController(grade_validator, grade_repository, student_repository, assignment_repository)
history_controller = HistoryController(student_controller, assignment_controller, grade_controller)

'''
    5. Initialize the user interface
        - The UI implements all user interactions
        - Only knows about the controller layer
        - Calls functions from the controller to implement program features
        - Might include some data validation, as a fast-fail mechanism
'''
menu_ui = MenuUI(student_controller, assignment_controller, grade_controller, history_controller)

'''
    6. Start the application's user interface
'''
menu_ui.run_main_menu()
