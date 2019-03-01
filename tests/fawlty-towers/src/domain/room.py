class Room:

    def __init__(self, number, type):
        self.__number = number
        self.__type = type

    def get_number(self):
        return self.__number

    def get_type(self):
        return self.__type

    def __str__(self):
        return "Room " + str(self.__number) + ", type: " + self.__type
