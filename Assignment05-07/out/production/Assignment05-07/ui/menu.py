from ui.menus.manage_lists import StudentsAndAssignmentsUI
from ui.menus.give_assignments import GiveAssignmentsUI
from ui.menus.grade_student import GradeStudentUI
from ui.menus.statistics import StatisticsUI

from validation.validation_exception import ValidationException
from repositories.repository_exception import RepositoryException
from controllers.controller_exception import ControllerException


class MenuUI:

    def __init__(self, student_controller, assignment_controller, grade_controller, history_controller):
        self.__student_controller = student_controller
        self.__assignment_controller = assignment_controller
        self.__grade_controller = grade_controller
        self.__history_controller = history_controller

        self.__students_and_assignments_ui = StudentsAndAssignmentsUI(
            student_controller, assignment_controller, grade_controller, history_controller
        )
        self.__give_assignments_ui = GiveAssignmentsUI(grade_controller, history_controller)
        self.__grade_student_ui = GradeStudentUI(grade_controller, history_controller)
        self.__statistics_ui = StatisticsUI(grade_controller)

        self.__options = {
            '1': self.__students_and_assignments_ui.students_and_assignments_menu,
            '2': self.__give_assignments_ui.give_assignments_menu,
            '3': self.__grade_student_ui.grade_student_menu,
            '4': self.__statistics_ui.statistics_menu,
            'u': self.ui_undo_action,
            'r': self.ui_redo_action
        }

    def run_main_menu(self):
        print("Application started! Please choose from one of the options below by specifying the option's index.")
        keep_alive = True
        while keep_alive:
            print("\n1. Manage the list of students and available assignments.")
            print("2. Give assignments to a student or a group of students.")
            print("3. Grade student for a given assignment.")
            print("4. Create statistics.")
            print("U. Undo action.")
            print("R. Redo action.")
            print("0. Exit the application.\n")
            user_option = input("Please select a submenu from 1-4, type 'U' or 'R' for history actions or 0 to exit the app: ").strip().lower()
            if user_option in self.__options:
                try:
                    self.__options[user_option]()
                except ValueError as value_error:
                    print("Value ERROR: " + str(value_error))
                except ValidationException as valid_error:
                    print(str(valid_error))
                except RepositoryException as repo_error:
                    print(str(repo_error))
                except ControllerException as controller_error:
                    print(str(controller_error))
            elif user_option == '0':
                keep_alive = True
            else:
                print("Invalid option!")

    def ui_undo_action(self):
        self.__history_controller.undo_action()

    def ui_redo_action(self):
        self.__history_controller.redo_action()
