from validators.student_validator import StudentValidator
from repositories.student_repository import StudentRepository
from controllers.student_controller import StudentController
from ui.console import Console

student_validator = StudentValidator()
student_repository = StudentRepository()

student_controller = StudentController(student_validator, student_repository)

console = Console(student_controller)

console.run_console()
