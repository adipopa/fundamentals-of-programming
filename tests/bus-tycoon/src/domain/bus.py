class Bus:

    def __init__(self, bus_id, route_code, model, times_used_on_route):
        self.__bus_id = bus_id
        self.__route_code = route_code
        self.__model = model
        self.__times_used_on_route = times_used_on_route

    def get_bus_id(self):
        return self.__bus_id

    def get_route_code(self):
        return self.__route_code

    def get_times_used_on_route(self):
        return self.__times_used_on_route

    def __str__(self):
        return "Bus ID: " + str(self.__bus_id) + ", route code: " + str(self.__route_code) + \
               ", model: " + self.__model + ", times used on this route: " + str(self.__times_used_on_route)
