from unittest import TestCase

from domain.bus import Bus


class TestBus(TestCase):

    def setUp(self):
        self.__bus = Bus(1, 21, 'electric', 9)

    def test_get_bus_id(self):
        self.assertEqual(self.__bus.get_bus_id(), 1)

    def test_get_route_code(self):
        self.assertEqual(self.__bus.get_route_code(), 21)

    def test_get_times_used_on_route(self):
        self.assertEqual(self.__bus.get_times_used_on_route(), 9)
