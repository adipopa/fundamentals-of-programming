from copy import deepcopy

import random

from controllers.controller_exception import ControllerException


class GameController:

    def __init__(self, player, computer, difficulty):
        self.__player = player
        self.__computer = computer
        self.__difficulty = difficulty

        self.__turn = 1
        self.__directions = {
            'up': (0, -1),
            'down': (0, 1),
            'left': (-1, 0),
            'right': (1, 0)
        }

    @property
    def current_player(self):
        return self.__player if self.__turn == 1 else self.__computer

    @property
    def next_player(self):
        return self.__player if self.__turn == 2 else self.__computer

    def draw_plane(self, start_position, direction):
        board_to_draw = self.current_player.get_strategy_board()
        config = deepcopy(board_to_draw.get_config())

        start_position_details = list(start_position)

        if len(start_position_details) != 2:
            raise ControllerException("Start position invalid, you can use for example: 'B4'.")

        position_y, position_x = map(str, start_position_details)

        x = int(position_x) - 1
        y = ord(position_y) - ord('A')

        direction_x = self.__directions[direction][0]
        direction_y = self.__directions[direction][1]

        if x < 0 or x > 7 or y < 0 or y > 7:
            raise ControllerException("The starting position must be between the boundaries of the 8x8 playing board.")

        plane_coordinates = []

        config = GameController.map_plane(config, x, y, direction_x, direction_y, direction, plane_coordinates)

        board_to_draw.set_config(config)

        self.current_player.set_strategy_board(board_to_draw)
        self.current_player.add_plane_coordinates(plane_coordinates)

    def ai_draw_planes(self):
        planes_drawn = False
        while not planes_drawn:
            self.reset_player_board()
            try:
                for plane_index in range(2):
                    plane_x = random.randint(1, 8)
                    plane_y = chr(ord('A') + random.randint(0, 7))
                    start_position = [plane_y, plane_x]
                    direction = random.sample(list(self.__directions), 1)[0]
                    self.draw_plane(start_position, direction)
                planes_drawn = True
            except ControllerException:
                continue
        self.next_turn()

    def strike_board(self, strike_position):
        targeting_board = self.current_player.get_targeting_board()
        board_to_strike = self.next_player.get_strategy_board()

        position_y, position_x = map(str, strike_position)

        x = int(position_x) - 1
        y = ord(position_y) - ord('A')

        if x < 0 or x > 7 or y < 0 or y > 7:
            raise ControllerException("The striking position must be between the boundaries of the 8x8 playing board.")

        strike_config = board_to_strike.get_config()
        targeting_config = targeting_board.get_config()

        strike_details = strike_config[x][y]

        if strike_details == 'O' or strike_details == 'X' or strike_details == 'D':
            raise ControllerException("This position has already been hit.")

        if strike_details == ' ':
            targeting_config[x][y] = strike_config[x][y] = 'O'
        elif strike_details == 'T' or strike_details == 'W':
            targeting_config[x][y] = strike_config[x][y] = 'X'
        elif strike_details == 'H':
            targeting_config[x][y] = strike_config[x][y] = 'D'
            if self.__difficulty == "medium":
                plane_coordinates = self.next_player.get_plane_coordinates(start_x=x, start_y=y)
                for coordinate in plane_coordinates[1:]:
                    x = coordinate[0]
                    y = coordinate[1]
                    targeting_config[x][y] = strike_config[x][y] = 'X'

    def ai_strike_board(self):
        board_struck = False
        while not board_struck:
            try:
                targeting_board = self.current_player.get_targeting_board()
                board_hits = self.get_board_hits(targeting_board)
                if len(board_hits) == 0:
                    plane_x = random.randint(1, 8)
                    plane_y = chr(ord('A') + random.randint(0, 7))
                else:
                    random_hit = random.sample(board_hits, 1)[0]
                    direction = random.sample(list(self.__directions), 1)[0]
                    plane_x = 1 + random_hit[0] + self.__directions[direction][0]
                    plane_y = chr(ord('A') + random_hit[1] + self.__directions[direction][1])
                strike_position = [plane_y, plane_x]
                self.strike_board(strike_position)
                print('AI struck position: ' + plane_y + str(plane_x))
                board_struck = True
            except ControllerException:
                continue
        self.next_turn()

    def get_board_hits(self, targeting_board):
        board_config = targeting_board.get_config()
        board_hits = []
        for y in range(len(board_config)):
            line = board_config[y]
            for x in range(len(line)):
                if board_config[x][y] == 'X' and self.in_alive_plane(x, y, board_config):
                    board_hits.append([x, y])
        return board_hits

    def in_alive_plane(self, x, y, board_config):
        for plane_coordinates in self.next_player.get_planes_coordinates():
            start_x = plane_coordinates[0][0]
            start_y = plane_coordinates[0][1]
            if board_config[start_x][start_y] == 'D':
                if [x, y] in plane_coordinates:
                    return False
        return True

    def next_turn(self):
        self.__turn = 1 if self.__turn == 2 else 2

    @staticmethod
    def map_plane(config, x, y, offset_x, offset_y, direction, plane_coordinates):
        position_error = ControllerException("There's not enough space to draw a plane given this start position and direction.")
        overlap_error = ControllerException("The planes cannot overlap, please provide another start position and direction.")

        if config[x][y] != " ":
            raise overlap_error

        config[x][y] = "H"
        plane_coordinates.append([x, y])

        for tail_position in range(3):
            x += offset_x
            y += offset_y
            if x < 0 or x > 7 or y < 0 or y > 7:
                raise position_error
            if config[x][y] != " ":
                raise overlap_error
            config[x][y] = "T"
            plane_coordinates.append([x, y])
            if tail_position == 0:
                for wing_position in range(1, 3):
                    if direction == "up" or direction == "down":
                        if x - wing_position < 0 or x + wing_position > 7:
                            raise position_error
                        if config[x - wing_position][y] != " " or config[x + wing_position][y] != " ":
                            raise overlap_error
                        config[x - wing_position][y] = config[x + wing_position][y] = "W"
                        plane_coordinates.append([x - wing_position, y])
                        plane_coordinates.append([x + wing_position, y])
                    else:
                        if y - wing_position < 0 or y + wing_position > 7:
                            raise position_error
                        if config[x][y - wing_position] != " " or config[x][y + wing_position] != " ":
                            raise overlap_error
                        config[x][y - wing_position] = config[x][y + wing_position] = "W"
                        plane_coordinates.append([x, y - wing_position])
                        plane_coordinates.append([x, y + wing_position])
            if tail_position == 2:
                if direction == "up" or direction == "down":
                    if config[x - 1][y] != " " or config[x + 1][y] != " ":
                        raise overlap_error
                    config[x - 1][y] = config[x + 1][y] = "W"
                    plane_coordinates.append([x - 1, y])
                    plane_coordinates.append([x + 1, y])
                else:
                    if config[x][y - 1] != " " or config[x][y + 1] != " ":
                        raise overlap_error
                    config[x][y - 1] = config[x][y + 1] = "W"
                    plane_coordinates.append([x, y - 1])
                    plane_coordinates.append([x, y + 1])

        return config

    def retrieve_player_board(self, show_target=False):
        board = self.current_player.get_strategy_board().to_string()
        if show_target:
            board_lines = board.splitlines()
            for line_index in range(len(board_lines)):
                targeting_board_line = self.current_player.get_targeting_board().to_string().splitlines()[line_index]
                board_lines[line_index] += "    " + targeting_board_line
            board = '\n'.join(board_lines)
        return board

    def get_player_planes_count(self):
        board_config = self.current_player.get_strategy_board().get_config()
        return self.alive_planes_count(board_config)

    def get_opponent_planes_count(self):
        board_config = self.next_player.get_strategy_board().get_config()
        return self.alive_planes_count(board_config)

    @staticmethod
    def alive_planes_count(board_config):
        alive_planes_count = 0
        for line in board_config:
            for position in line:
                if position == 'H':
                    alive_planes_count += 1
        return alive_planes_count

    def reset_player_board(self):
        self.current_player.set_strategy_board()
        self.current_player.set_targeting_board()
