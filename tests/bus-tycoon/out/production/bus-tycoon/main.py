from repositories.bus_repository import BusRepository
from repositories.route_repository import RouteRepository
from controllers.bus_routes_controller import BusRoutesController
from ui.console import Console

bus_repository = BusRepository()
route_repository = RouteRepository()

bus_routes_controller = BusRoutesController(bus_repository, route_repository)

console = Console(bus_routes_controller)

console.run_console()