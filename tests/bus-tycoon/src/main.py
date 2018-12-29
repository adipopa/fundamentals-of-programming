from repositories.bus_repository import BusRepository
from repositories.route_repository import RouteRepository
from controllers.bus_routes_controller import BusRoutesController
from ui.console import Console

"""
1. We initiate the repositories that read and keep the program data.
"""

bus_repository = BusRepository()
route_repository = RouteRepository()

"""
2. We initialize the controller which contains all the program logic and serves as the main service for the application.
    - the controller takes as arguments the repositories defined above
"""

bus_routes_controller = BusRoutesController(bus_repository, route_repository)

"""
3. Finally, initialize the console, given the controller as argument and run the main method.
"""

console = Console(bus_routes_controller)

console.run_console()
