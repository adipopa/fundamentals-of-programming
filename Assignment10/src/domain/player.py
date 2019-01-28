from domain.board import Board


class Player:

    def __init__(self):
        self.__strategy_board = Board()
        self.__targeting_board = Board()

        self.__planes_coordinates = []

    def get_strategy_board(self):
        return self.__strategy_board

    def set_strategy_board(self, strategy_board=None):
        if strategy_board is None:
            strategy_board = Board()
        self.__strategy_board = strategy_board

    def get_targeting_board(self):
        return self.__targeting_board

    def set_targeting_board(self, targeting_board=None):
        if targeting_board is None:
            targeting_board = Board()
        self.__targeting_board = targeting_board

    def get_plane_coordinates(self, start_x, start_y):
        for plane_coordinates in self.__planes_coordinates:
            plane_x = plane_coordinates[0][0]
            plane_y = plane_coordinates[0][1]
            if plane_x == start_x and plane_y == start_y:
                return plane_coordinates

    def add_plane_coordinates(self, plane_coordinates):
        self.__planes_coordinates.append(plane_coordinates)

    def get_planes_coordinates(self):
        return self.__planes_coordinates
