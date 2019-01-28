from domain.player import Player

from controllers.game_controller import GameController

from ux.console import Console
from ux.gui import GUI

player = Player()
computer = Player()

try:
    settings_file = open("settings.properties", "r")

    interface_option = settings_file.readline().strip()
    if len(interface_option) == 0:
        raise IOError("Interface option not given, check settings.properties file.")
    interface = interface_option.split("=")[1]

    difficulty_option = settings_file.readline().strip()
    if len(difficulty_option) == 0:
        raise IOError("Difficulty option not given, check settings.properties file.")
    difficulty = difficulty_option.split("=")[1]

    if difficulty != "medium" and difficulty != "hard":
        raise IOError("The difficulty option in settings.properties must be either 'medium' or 'hard'.")

    game_controller = GameController(player, computer, difficulty)

    if interface == "console":
        console = Console(game_controller)
        console.start_game()
    elif interface == "gui":
        gui = GUI(game_controller)
        gui.start_game()
    else:
        raise IOError("The interface option in settings.properties must be either 'console' or 'gui'.")
    settings_file.close()
except IOError as io_error:
    raise io_error
