from unittest import TestCase

from repositories.bus_repository import BusRepository
from repositories.route_repository import RouteRepository

from controllers.bus_routes_controller import BusRoutesController


class TestBusRoutesController(TestCase):

    def setUp(self):
        bus_repository = BusRepository()
        route_repository = RouteRepository()

        self.__bus_routes_controller = BusRoutesController(bus_repository, route_repository)

    def test_retrieve_buses_by_route(self):
        buses_by_route = self.__bus_routes_controller.retrieve_buses_by_route(21)
        self.assertEqual(len(buses_by_route), 2)
        self.assertEqual(buses_by_route[0].get_bus_id(), 2)
        self.assertEqual(buses_by_route[1].get_bus_id(), 3)

    def test_retrieve_bus_routes(self):
        routes = self.__bus_routes_controller.retrieve_bus_routes()
        self.assertEqual(len(routes), 3)
        self.assertEqual(routes[0].get_route_code(), 5)
        self.assertEqual(routes[1].get_route_code(), 21)
        self.assertEqual(routes[2].get_route_code(), 24)

    def test_compute_travelled_length(self):
        travel_details = self.__bus_routes_controller.compute_travelled_length(3)
        bus = travel_details['bus_details']
        travelled_length = travel_details['travelled_length']
        self.assertEqual(bus.get_bus_id(), 3)
        self.assertEqual(bus.get_route_code(), 21)
        self.assertEqual(bus.get_times_used_on_route(), 7)
        self.assertEqual(travelled_length, 84)
