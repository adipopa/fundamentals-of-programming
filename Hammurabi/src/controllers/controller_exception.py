class ControllerError(Exception):

    def __init__(self, message=None):
        if message is None:
            message = "Unknown error."
        self.__message = message

    def __str__(self):
        return "Controller ERROR: " + self.__message + "\n"
