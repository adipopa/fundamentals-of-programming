from repositories.hotel_repository import HotelRepository
from controllers.hotel_controller import HotelController
from ui.console import Console

hotel_repository = HotelRepository(rooms_filename="rooms.txt", reservations_filename="reservations.txt")

hotel_controller = HotelController(hotel_repository)

console = Console(hotel_controller)

console.show_menu()
