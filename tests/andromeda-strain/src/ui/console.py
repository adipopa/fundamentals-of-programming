class Console:

    def __init__(self, disease_controller):
        self.__disease_controller = disease_controller
        self.__commands = {
            'simulate': self.ui_simulate_day,
            'vaccinate': self.ui_vaccinate_person
        }

    def run_console(self):
        keep_alive = True
        while keep_alive:
            user_input = input(">> ").strip().split()
            command = user_input[0]
            params = user_input[1:]
            if command in self.__commands:
                try:
                    self.__commands[command](params)
                except ValueError as value_error:
                    print("Value ERROR: " + str(value_error))
                except Exception as exception:
                    print("ERROR: " + str(exception))
            elif user_input == 'exit':
                keep_alive = False
            else:
                print("Command not found.")

    def ui_simulate_day(self, params):
        if len(params) != 0:
            raise Exception("Invalid parameters. Required 0 arguments.")
        result_of_simulation = self.__disease_controller.simulate_day()
        print("Result of simulation: ")
        for person in result_of_simulation:
            print(person)

    def ui_vaccinate_person(self, params):
        if len(params) != 1:
            raise Exception("Invalid parameters. Required 1 argument.")
        id = int(params[0])
        self.__disease_controller.vaccinate_person(id)
