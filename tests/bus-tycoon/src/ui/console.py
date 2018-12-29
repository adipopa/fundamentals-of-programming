class Console:

    def __init__(self, bus_routes_controller):
        self.__bus_routes_controller = bus_routes_controller
        self.__commands = {
            'display-buses': self.ui_display_buses,
            'display-routes': self.ui_display_bus_routes,
            'travelled': self.ui_show_travelled_length
        }

    def run_console(self):
        print("Bus tycoon application started! List of commands:")
        print(" - display-buses <route_code>")
        print(" - display-routes")
        print(" - travelled <bus_id>\n")
        keep_alive = True
        while keep_alive:
            user_input = input(">> ").strip().split()
            if len(user_input) == 0:
                print("No command given.")
                continue
            command = user_input[0]
            parameters = user_input[1:]
            if command in self.__commands:
                try:
                    self.__commands[command](parameters)
                except ValueError as value_error:
                    print("Value ERROR: " + str(value_error))
                except Exception as exception:
                    print("Error: " + str(exception))
            elif command == 'exit':
                keep_alive = False
            else:
                print("Invalid command.")

    def ui_display_buses(self, parameters):
        if len(parameters) != 1:
            raise Exception("Required 1 argument.")
        route_code = int(parameters[0])
        buses = self.__bus_routes_controller.retrieve_buses_by_route(route_code)
        for bus in buses:
            print(bus)
        print()

    def ui_display_bus_routes(self, parameters):
        if len(parameters) != 0:
            raise Exception("Required 0 arguments.")
        bus_routes = self.__bus_routes_controller.retrieve_bus_routes()
        for route in bus_routes:
            print(route)
        print()

    def ui_show_travelled_length(self, parameters):
        if len(parameters) != 1:
            raise Exception("Required 1 argument.")
        bus_id = int(parameters[0])
        travel_details = self.__bus_routes_controller.compute_travelled_length(bus_id)
        print(travel_details['bus_details'])
        print("TOTAL TRAVELLED LENGTH: " + str(travel_details['travelled_length']) + '\n')
