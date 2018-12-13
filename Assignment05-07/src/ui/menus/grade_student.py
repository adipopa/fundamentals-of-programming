class GradeStudentUI:

    def __init__(self, grade_controller, history_controller):
        self.__grade_controller = grade_controller
        self.__history_controller = history_controller

    def grade_student_menu(self):
        """
        The function displays a menu to let the user choose a student and an assignment of that student to be graded.
        :return:
        """
        keep_alive = True
        while keep_alive:
            user_option = input("Please enter a student's ID or go back by typing 'back': ")
            try:
                student_id = int(user_option)
            except ValueError:
                if user_option == 'back':
                    keep_alive = False
                else:
                    print("Invalid option!\n")
            else:
                ungraded_assignments = self.__grade_controller.retrieve_ungraded_assignments_by_student(student_id)
                if len(ungraded_assignments) != 0:
                    for assignment in ungraded_assignments:
                        print(assignment)
                    assignment_id = int(input("\nAssignment ID: "))
                    grade = int(input("Grade: "))
                    self.__grade_controller.grade_student(student_id, assignment_id, grade)
                    self.__history_controller.upsert_operations({
                        'undo': {
                            'action': self.__grade_controller.grade_student,
                            'params': [student_id, assignment_id, None]
                        },
                        'redo': {
                            'action': self.__grade_controller.grade_student,
                            'params': [student_id, assignment_id, grade]
                        }
                    })
                    print()
                else:
                    print("There are no ungraded assignments assigned to this student.\n")
