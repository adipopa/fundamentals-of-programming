class RepositoryException(Exception):
    """
    Exception class for repository errors
    """

    def __init__(self, message_list=None):
        """
        Constructor for repository exception class
        message_list - An array of strings representing the exception message
        """
        if message_list is None:
            message_list = ["Repository error!"]
        self.__message_list = message_list

    @property
    def messages(self):
        return self.__message_list

    def __str__(self):
        result = ""
        for message in self.messages:
            result += "Repository ERROR: " + message
        return result
