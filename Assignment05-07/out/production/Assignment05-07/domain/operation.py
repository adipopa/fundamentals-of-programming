class Operation:
    """
    Operation domain class
    """

    def __init__(self, undo, redo):
        """
        Constructor for grade domain class
        index - The index that tracks where the user is currently in the undo / redo stack.
        operation - the last operation performed
        """
        self.__undo = undo
        self.__redo = redo
