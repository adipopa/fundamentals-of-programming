from utils.helper import Helper


class StudentsAndAssignmentsUI:

    def __init__(self, student_controller, assignment_controller):
        self.__student_controller = student_controller
        self.__assignment_controller = assignment_controller

    def students_and_assignments_menu(self):
        """
        The function displays a menu to let the user choose which list to manage.
        :return:
        """
        keep_alive = True
        while keep_alive:
            print("A. Manage the list of students.")
            print("B. Manage the list of assignments.\n")
            option = input("Choose option 'A' or 'B' or go back by typing 'back': ")
            if option == "A":
                self.manage_students_menu()
            elif option == "B":
                self.manage_assignments_menu()
            elif option == "back":
                keep_alive = False
            else:
                print("Invalid option.\n")

    def manage_students_menu(self):
        """
        The function displays a menu to let the user choose between the two properties that a sequence can have.
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
                self.__student_controller.create_student(name, group)
                print()
            elif user_option == 'b':
                student_id = int(input("Student ID: "))
                self.__student_controller.delete_student(student_id)
                print()
            elif user_option == 'c':
                student_id = int(input("Student ID: "))
                name = input("Student name: ")
                group = int(input("Student's group: "))
                self.__student_controller.update_student(student_id, name, group)
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
        The function displays a menu to let the user choose between the two properties that a sequence can have.
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
                self.__assignment_controller.create_assignment(description, deadline)
                print()
            elif user_option == 'b':
                assignment_id = int(input("Assignment ID: "))
                self.__assignment_controller.delete_assignment(assignment_id)
                print()
            elif user_option == 'c':
                assignment_id = int(input("Assignment ID: "))
                description = input("Assignment description: ")
                deadline = Helper.resolve_date(input("Assignment's deadline is on (DD/MM/YYYY format): "))
                self.__assignment_controller.update_assignment(assignment_id, description, deadline)
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
