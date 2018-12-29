class BusRoutesController:

    def __init__(self, bus_repository, routes_repository):
        self.__bus_repository = bus_repository
        self.__routes_repository = routes_repository

    def retrieve_bus_routes(self):
        return self.__routes_repository.get_all_routes()

    def compute_travelled_length(self, bus_id):
        bus = self.__bus_repository.get_bus_by_id(bus_id)
        route = self.__routes_repository.get_route_by_code(bus.get_route_code())
        travelled_length = bus.get_times_used_on_route() * route.get_length_in_kilometers()
        return {
            'bus_details': bus,
            'travelled_length': travelled_length
        }
