class Console:

    def __init__(self, bus_routes_controller):
        self.__bus_routes_controller = bus_routes_controller
        self.__commands = {
            'display-routes': self.ui_display_bus_routes,
            'travel': self.ui_show_travelled_length
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
                    print("Error: " + str(exception))
            elif command == 'exit':
                keep_alive = False
            else:
                print("Invalid command.")

    def ui_display_bus_routes(self, params):
        if len(params) != 0:
            raise Exception("Required 0 arguments.")
        bus_routes = self.__bus_routes_controller.retrieve_bus_routes()
        for route in bus_routes:
            print(route)

    def ui_show_travelled_length(self, params):
        if len(params) != 1:
            raise Exception("Required 1 argument.")
        bus_id = int(params[0])
        travel_details = self.__bus_routes_controller.compute_travelled_length(bus_id)
        print(travel_details['bus_details'])
        print("TOTAL TRAVELLED LENGTH: " + str(travel_details['travelled_length']))
