class GradeStudentUI:

    def __init__(self, grade_controller):
        self.__grade_controller = grade_controller

    def grade_student_menu(self):
        """
        The function displays a menu to let the user choose which list to manage.
        :return:
        """
        keep_alive = True
        while keep_alive:
            option = input("Please enter a student's ID or go back by typing 'back': ")
            try:
                student_id = int(option)
            except ValueError:
                if option == "back":
                    keep_alive = False
                else:
                    print("Invalid option.\n")
            else:
                ungraded_assignments = self.__grade_controller.retrieve_ungraded_assignments_by_student(student_id)
                if len(ungraded_assignments) != 0:
                    for assignment in ungraded_assignments:
                        print(assignment)
                    assignment_id = int(input("\nAssignment ID: "))
                    grade = int(input("Grade: "))
                    self.__grade_controller.grade_student(student_id, assignment_id, grade)
                    print()
                else:
                    print("There are no ungraded assignments assigned to this student.\n")
