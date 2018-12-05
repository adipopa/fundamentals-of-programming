class ValidationException(Exception):
    """
    Exception class for validator errors
    """

    def __init__(self, message_list=None):
        """
        Constructor for validation exception class
        message_list - An array of strings representing the exception message
        """
        if message_list is None:
            message_list = ["Validation error!"]
        self.__message_list = message_list

    @property
    def messages(self):
        return self.__message_list

    def __str__(self):
        result = ""
        for message in self.messages:
            result += "Validation ERROR: " + message + "\n"
        return result
