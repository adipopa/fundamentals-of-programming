class GiveAssignmentsUI:

    def __init__(self, grade_controller):
        self.__grade_controller = grade_controller

    def give_assignments_menu(self):
        """
        The function displays a menu to let the user choose which list to manage.
        :return:
        """
        keep_alive = True
        while keep_alive:
            print("a. Give assignment to a student.")
            print("b. Give assignment to a group of students.\n")
            option = input("Choose option 'a' or 'b' or go back by typing 'back': ")
            if option == "a":
                assignment_id = int(input("Assignment ID: "))
                student_id = int(input("Student ID: "))
                self.__grade_controller.give_assignment(assignment_id, student_id)
                print()
            elif option == "b":
                assignment_id = int(input("Assignment ID: "))
                group = int(input("Group of students: "))
                self.__grade_controller.give_assignment_to_group(assignment_id, group)
                print()
            elif option == "back":
                keep_alive = False
            else:
                print("Invalid option.\n")
