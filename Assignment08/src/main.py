from validation.student_validator import StudentValidator
from validation.assignment_validator import AssignmentValidator
from validation.grade_validator import GradeValidator

from repositories.inmemory.student_repository import StudentRepository
from repositories.inmemory.assignment_repository import AssignmentRepository
from repositories.inmemory.grade_repository import GradeRepository

from repositories.textfile.student_text_repository import StudentTextRepository
from repositories.textfile.assignment_text_repository import AssignmentTextRepository
from repositories.textfile.grade_text_repository import GradeTextRepository

from repositories.binaryfile.student_binary_repository import StudentBinaryRepository
from repositories.binaryfile.assignment_binary_repository import AssignmentBinaryRepository
from repositories.binaryfile.grade_binary_repository import GradeBinaryRepository

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
    2. We initialize the repositories based on settings.properties file (in-memory / text-files / binary-files)
        - Repository holds the business entities
        - Acts like the program's database
        - Might include some data validation
        - Does not know about any other components
'''

student_repository = None
assignment_repository = None
grade_repository = None

try:
    settings_file = open('settings.properties', 'r')
    repository = settings_file.readline().strip().split('=')[1]
    if repository == 'inmemory':
        student_repository = StudentRepository()
        assignment_repository = AssignmentRepository()
        grade_repository = GradeRepository()
        generator = Generator(student_repository, assignment_repository, grade_repository)
        generator.generate_students(100)
        generator.generate_assignments(100)
        generator.generate_grades(100)
    elif repository == 'textfiles' or repository == 'binaryfiles':
        students_filename = settings_file.readline().strip().replace('"', '').split('=')[1]
        assignments_filename = settings_file.readline().strip().replace('"', '').split('=')[1]
        grades_filename = settings_file.readline().strip().replace('"', '').split('=')[1]
        if repository == 'textfiles':
            student_repository = StudentTextRepository(students_filename)
            assignment_repository = AssignmentTextRepository(assignments_filename)
            grade_repository = GradeTextRepository(grades_filename)
        else:
            student_repository = StudentBinaryRepository(students_filename)
            assignment_repository = AssignmentBinaryRepository(assignments_filename)
            grade_repository = GradeBinaryRepository(grades_filename)
    else:
        raise IOError("Invalid repository in settings.properties")
    settings_file.close()
except IOError as e:
    raise e

'''
    3. We initialize the controllers
        - The controller implements the program's 'operations'
        - Knows only about the repository layer
        - 'Talks' to the repository and UI using parameter passing and exceptions
'''
student_controller = StudentController(student_validator, student_repository)
assignment_controller = AssignmentController(assignment_validator, assignment_repository)
grade_controller = GradeController(grade_validator, grade_repository, student_repository, assignment_repository)
history_controller = HistoryController(student_controller, assignment_controller, grade_controller)

'''
    4. Initialize the user interface
        - The UI implements all user interactions
        - Only knows about the controller layer
        - Calls functions from the controller to implement program features
        - Might include some data validation, as a fast-fail mechanism
'''
menu_ui = MenuUI(student_controller, assignment_controller, grade_controller, history_controller)

'''
    5. Start the application's user interface
'''
menu_ui.run_main_menu()
