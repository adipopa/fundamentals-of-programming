class BusRoutesController:
    """
    This is the BusRoutesController class, the main controller of the app that contains all the logic
    required to fulfill the app's features.
    """

    def __init__(self, bus_repository, route_repository):
        """
        Constructor of BusRoutesController class.
        :param bus_repository:
        :param route_repository:
        """
        self.__bus_repository = bus_repository
        self.__route_repository = route_repository

    def retrieve_buses_by_route(self, route_code):
        """
        The method retrieves all the buses (with their details) for a given route_code and returns them.
        :param route_code:
        :return:
        """
        return self.__bus_repository.get_buses_by_route(route_code)

    def retrieve_bus_routes(self):
        """
        The method retrieves all the bus routes (with their details) and returns them.
        :return:
        """
        return self.__route_repository.get_all_routes()

    def compute_travelled_length(self, bus_id):
        """
        The method computes the total travelled length performed by a bus, given a bus_id and returns a object composed
        of: 'bus_details', which contains the details of the bus and 'travelled_length', which contains the total
        travelled length performed by that bus.
        :param bus_id:
        :return:
        """
        bus = self.__bus_repository.get_bus_by_id(bus_id)
        route = self.__route_repository.get_route_by_code(bus.get_route_code())
        travelled_length = bus.get_times_used_on_route() * route.get_length_in_kilometers()
        return {
            'bus_details': bus,
            'travelled_length': travelled_length
        }
