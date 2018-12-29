from domain.route import Route


class RouteRepository:

    def __init__(self):
        self.__routes = RouteRepository.read_routes_from_file('routes.txt')

    def get_all_routes(self):
        return self.__routes

    def get_route_by_code(self, route_code):
        for route in self.__routes:
            if route.get_route_code() == route_code:
                return route
        raise Exception("No route found.")

    @staticmethod
    def read_routes_from_file(file_name):
        routes = []
        file = open(file_name, 'r')
        line = file.readline().strip()
        while len(line) > 0:
            arguments = line.split(',')
            routes.append(Route(int(arguments[0]), int(arguments[1])))
            line = file.readline().strip()
        file.close()
        return routes
