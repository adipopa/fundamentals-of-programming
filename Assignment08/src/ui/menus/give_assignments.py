class GiveAssignmentsUI:

    def __init__(self, grade_controller, history_controller):
        self.__grade_controller = grade_controller
        self.__history_controller = history_controller

    def give_assignments_menu(self):
        """
        The function displays a menu to let the user choose which list to manage.
        :return:
        """
        keep_alive = True
        while keep_alive:
            print("a. Give assignment to a student.")
            print("b. Give assignment to a group of students.\n")
            user_option = input("Choose option 'a' or 'b' or go back by typing 'back': ")
            if user_option == 'a':
                assignment_id = int(input("Assignment ID: "))
                student_id = int(input("Student ID: "))
                self.__grade_controller.give_assignment(assignment_id, student_id)
                self.__history_controller.upsert_operations({
                    'undo': {
                        'action': self.__grade_controller.delete_grade,
                        'params': [assignment_id, student_id]
                    },
                    'redo': {
                        'action': self.__grade_controller.give_assignment,
                        'params': [assignment_id, student_id]
                    }
                })
                print()
            elif user_option == 'b':
                assignment_id = int(input("Assignment ID: "))
                group = int(input("Group of students: "))
                self.__grade_controller.give_assignment_to_group(assignment_id, group)
                self.__history_controller.upsert_operations({
                    'undo': {
                        'action': self.__grade_controller.delete_grade_by_group,
                        'params': [assignment_id, group]
                    },
                    'redo': {
                        'action': self.__grade_controller.give_assignment_to_group,
                        'params': [assignment_id, group]
                    }
                })
                print()
            elif user_option == 'back':
                keep_alive = False
            else:
                print("Invalid option!\n")
