from domain.situation import Situation

from validators.game_validator import GameValidator
from controllers.game_controller import GameController

from ui.console import Console

situation = Situation()
game_validator = GameValidator()

game_controller = GameController(situation, game_validator)

console = Console(game_controller)

console.start_game()
