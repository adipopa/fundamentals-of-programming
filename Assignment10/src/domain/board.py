class Board:

    def __init__(self):
        self.__config = [[" " for column in range(8)] for row in range(8)]

    def get_config(self):
        return self.__config

    def set_config(self, config):
        self.__config = config

    def to_string(self):
        grid = "    1   2   3   4   5   6   7   8   "
        for row in range(8):
            grid += "\n" + chr(ord('A') + row) + " | "
            for column in range(8):
                position = self.__config[column][row]
                grid += str(position) + " | "
        return grid
