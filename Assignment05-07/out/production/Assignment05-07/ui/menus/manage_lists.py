from utils.helper import Helper


class StudentsAndAssignmentsUI:

    def __init__(self, student_controller, assignment_controller, grade_controller, history_controller):
        self.__student_controller = student_controller
        self.__assignment_controller = assignment_controller
        self.__grade_controller = grade_controller
        self.__history_controller = history_controller

    def students_and_assignments_menu(self):
        """
        The function displays a menu to let the user choose which list to manage.
        :return:
        """
        print("A. Manage the list of students.")
        print("B. Manage the list of assignments.")
        print("C. Display all the assignments of all students with their given grade if available.\n")
        keep_alive = True
        while keep_alive:
            user_option = input("Choose option 'A', 'B' or 'C' or go back by typing 'back': ").strip().lower()
            if user_option == 'a':
                self.manage_students_menu()
            elif user_option == 'b':
                self.manage_assignments_menu()
            elif user_option == 'c':
                self.display_grades()
            elif user_option == 'back':
                keep_alive = False
            else:
                print("Invalid option!\n")

    def manage_students_menu(self):
        """
        The function displays a menu to let the user choose how to manage the students list.
        :return:
        """
        print("a. Add a student to the list.")
        print("b. Remove a student from the list.")
        print("c. Update a student in the list.")
        print("d. Display the students in the list.\n")
        keep_alive = True
        while keep_alive:
            user_option = input("Choose from one of the available options or go back by typing 'back': ")
            if user_option == 'a':
                name = input("Student name: ")
                group = int(input("Student's group: "))
                student_id = self.__student_controller.create_student(name, group)
                self.__history_controller.upsert_operations({
                    'undo': {
                        'action': self.__student_controller.delete_student,
                        'params': [student_id, True]
                    },
                    'redo': {
                        'action': self.__student_controller.create_student,
                        'params': [name, group]
                    }
                })
                print()
            elif user_option == 'b':
                student_id = int(input("Student ID: "))
                deleted_student = self.__student_controller.get_student(student_id)
                self.__student_controller.delete_student(student_id)
                self.__history_controller.upsert_operations({
                    'undo': {
                        'action': self.__student_controller.create_student,
                        'params': [deleted_student.get_name(), deleted_student.get_group(), deleted_student.get_student_id()]
                    },
                    'redo': {
                        'action': self.__student_controller.delete_student,
                        'params': [student_id]
                    }
                })
                print()
            elif user_option == 'c':
                student_id = int(input("Student ID: "))
                name = input("Student name: ")
                group = int(input("Student's group: "))
                old_student = self.__student_controller.get_student(student_id)
                self.__student_controller.update_student(student_id, name, group)
                self.__history_controller.upsert_operations({
                    'undo': {
                        'action': self.__student_controller.update_student,
                        'params': [student_id, old_student.get_name(), old_student.get_group()]
                    },
                    'redo': {
                        'action': self.__student_controller.update_student,
                        'params': [student_id, name, group]
                    }
                })
                print()
            elif user_option == 'd':
                print("Students in the list: \n")
                for student in self.__student_controller.retrieve_students():
                    print(str(student))
                print()
            elif user_option == 'back':
                keep_alive = False
            else:
                print("Invalid option, please choose from the given options above.\n")

    def manage_assignments_menu(self):
        """
        The function displays a menu to let the user choose how to manage the assignments list.
        :return:
        """
        print("a. Add an assignment to the list.")
        print("b. Remove an assignment from the list.")
        print("c. Update an assignment in the list.")
        print("d. Display the assignments in the list.\n")
        keep_alive = True
        while keep_alive:
            user_option = input("Choose from one of the available options or go back by typing 'back': ")
            if user_option == 'a':
                description = input("Assignment description: ")
                deadline = Helper.resolve_date(input("Assignment's deadline is on (DD/MM/YYYY format): "))
                assignment_id = self.__assignment_controller.create_assignment(description, deadline)
                self.__history_controller.upsert_operations({
                    'undo': {
                        'action': self.__assignment_controller.delete_assignment,
                        'params': [assignment_id, True]
                    },
                    'redo': {
                        'action': self.__assignment_controller.create_assignment,
                        'params': [description, deadline]
                    }
                })
                print()
            elif user_option == 'b':
                assignment_id = int(input("Assignment ID: "))
                deleted_assignment = self.__assignment_controller.get_assignment(assignment_id)
                self.__assignment_controller.delete_assignment(assignment_id)
                self.__history_controller.upsert_operations({
                    'undo': {
                        'action': self.__assignment_controller.create_assignment,
                        'params': [deleted_assignment.get_description(), deleted_assignment.get_deadline(), deleted_assignment.get_assignment_id()]
                    },
                    'redo': {
                        'action': self.__assignment_controller.delete_assignment,
                        'params': [assignment_id]
                    }
                })
                print()
            elif user_option == 'c':
                assignment_id = int(input("Assignment ID: "))
                description = input("Assignment description: ")
                deadline = Helper.resolve_date(input("Assignment's deadline is on (DD/MM/YYYY format): "))
                old_assignment = self.__assignment_controller.get_assignment(assignment_id)
                self.__assignment_controller.update_assignment(assignment_id, description, deadline)
                self.__history_controller.upsert_operations({
                    'undo': {
                        'action': self.__assignment_controller.update_assignment,
                        'params': [assignment_id, old_assignment.get_description(), old_assignment.get_deadline()]
                    },
                    'redo': {
                        'action': self.__assignment_controller.update_assignment,
                        'params': [assignment_id, description, deadline]
                    }
                })
                print()
            elif user_option == 'd':
                print("Assignments in the list: \n")
                for assignment in self.__assignment_controller.retrieve_assignments():
                    print(str(assignment))
                print()
            elif user_option == 'back':
                keep_alive = False
            else:
                print("Invalid option, please choose from the given options above.\n")

    def display_grades(self):
        for grade in self.__grade_controller.retrieve_grades():
            print(grade)
        print()
