class ControllerException(Exception):
    """
    Exception class for controller errors
    """
    def __init__(self, message_list=None):
        """
        Constructor for controller exception class
        message_list - An array of strings representing the exception message
        """
        if message_list is None:
            message_list = ["Controller error!"]
        self.__message_list = message_list

    @property
    def messages(self):
        return self.__message_list

    def __str__(self):
        result = ""
        for message in self.messages:
            result += "Controller ERROR: " + message
        return result
