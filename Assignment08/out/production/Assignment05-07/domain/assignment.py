class Assignment:
    """
    Assignment domain class
    """

    def __init__(self, assignment_id, description, deadline):
        """
        Constructor for assignment domain class
        assignment_id - The assignment's ID (integer)
        description - The assignment's description (string)
        deadline - The assignment's deadline (consisting of a date)
        """
        self.__assignment_id = assignment_id
        self.__description = description
        self.__deadline = deadline

    def set_assignment_id(self, assignment_id):
        self.__assignment_id = assignment_id

    def get_assignment_id(self):
        return self.__assignment_id

    def get_description(self):
        return self.__description

    def get_deadline(self):
        return self.__deadline

    def __str__(self):
        return 'ID: ' + str(self.__assignment_id) + ', description: ' + self.__description + ', deadline: ' + self.__deadline.strftime('%d, %b %Y')

    def __repr__(self):
        return str(self)
