class StatisticsUI:

    def __init__(self, grade_controller):
        self.__grade_controller = grade_controller

    def statistics_menu(self):
        """
        The function displays a menu to let the user choose which list to manage.
        :return:
        """
        keep_alive = True
        print("a. All students who received a given assignment.")
        print("b. All students who are late in handing in at least one assignment.")
        print("c. Students with the best school situation.")
        print("d. All assignments for which there is at least one grade.\n")
        while keep_alive:
            option = input("Choose from the options above or go back by typing 'back': ")
            if option == "a":
                assignment_id = int(input("Assignment ID: "))
                for students in self.__grade_controller.retrieve_students_by_assignment(assignment_id):
                    print(students)
                print()
            elif option == "b":
                pass
            elif option == "c":
                pass
            elif option == "d":
                pass
            elif option == "back":
                keep_alive = False
            else:
                print("Invalid option.\n")
