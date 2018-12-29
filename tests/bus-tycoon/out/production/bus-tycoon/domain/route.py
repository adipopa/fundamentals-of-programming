class Route:

    def __init__(self, route_code, length_in_kilometers):
        self.__route_code = route_code
        self.__length_in_kilometers = length_in_kilometers

    def get_route_code(self):
        return self.__route_code

    def get_length_in_kilometers(self):
        return self.__length_in_kilometers

    def __str__(self):
        return "Route code: " + str(self.__route_code) + ", length in kilometers: " + str(self.__length_in_kilometers)
