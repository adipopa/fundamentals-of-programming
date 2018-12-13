class StatisticsUI:

    def __init__(self, grade_controller):
        self.__grade_controller = grade_controller

    def statistics_menu(self):
        """
        The function displays a menu to let the user choose which statistics to be displayed.
        :return:
        """
        keep_alive = True
        print("a. All students who received a given assignment.")
        print("b. All students who are late in handing in at least one assignment.")
        print("c. Students with the best school situation.")
        print("d. All assignments for which there is at least one grade.\n")
        while keep_alive:
            user_option = input("Choose from the options above or go back by typing 'back': ")
            if user_option == 'a':
                assignment_id = int(input("Assignment ID: "))
                for student in self.__grade_controller.retrieve_students_by_assignment(assignment_id):
                    print(student)
                print()
            elif user_option == 'b':
                for student in self.__grade_controller.retrieve_late_students():
                    print(student)
                print()
            elif user_option == 'c':
                for student in self.__grade_controller.retrieve_best_students():
                    print(student)
                print()
            elif user_option == 'd':
                for student in self.__grade_controller.retrieve_assignments_by_average_grade():
                    print(student)
                print()
            elif user_option == 'back':
                keep_alive = False
            else:
                print("Invalid option!\n")
