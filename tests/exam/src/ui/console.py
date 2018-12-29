class Console:

    def __init__(self, student_controller):
        self.__student_controller = student_controller
        self.__commands = {
            'add': self.ui_add_student,
            'bonus': self.ui_give_bonus,
            'display': self.ui_display_students
        }

    def run_console(self):
        keep_alive = True
        while keep_alive:
            user_input = input(">> ").strip().split()
            command = user_input[0]
            parameters = user_input[1:]
            if command in self.__commands:
                try:
                    self.__commands[command](parameters)
                except ValueError as value_error:
                    print("Value ERROR: " + str(value_error))
                except Exception as exception:
                    print("ERROR: " + str(exception))
            elif command == 'exit':
                keep_alive = False
            else:
                print('Invalid command!')

    def ui_add_student(self, params):
        if len(params) < 4:
            raise Exception("Invalid parameters. Expected 4 arguments.")
        id = int(params[0])
        name = ' '.join(params[1:-2])
        attendance_count = int(params[-2])
        grade = int(params[-1])
        self.__student_controller.add_student(id, name, attendance_count, grade)

    def ui_give_bonus(self, params):
        if len(params) != 2:
            raise Exception("Invalid parameters. Expected 2 arguments.")
        p = int(params[0])
        b = int(params[1])
        self.__student_controller.give_bonus(p, b)

    def ui_display_students(self, params):
        if len(params) != 1:
            raise Exception("Invalid parameters. Expected 1 argument.")
        name = params[0]
        for student in self.__student_controller.retrieve_students_by_name(name):
            print(student)
