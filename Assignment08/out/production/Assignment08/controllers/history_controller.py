from controllers.controller_exception import ControllerException


class HistoryController:

    def __init__(self, grade_repository, student_repository, assignment_repository):
        self.__operations = []
        self.__pointer = -1

        self.__grade_repository = grade_repository
        self.__student_repository = student_repository
        self.__assignment_repository = assignment_repository

    def upsert_operations(self, operation):
        if self.can_redo():
            self.__operations = self.__operations[:self.__pointer + 1]
        self.__operations.append(operation)
        self.__pointer += 1

    def undo_action(self):
        if self.can_undo():
            operation = self.__operations[self.__pointer]['undo']
            self.__pointer -= 1
            undo_action = operation['action']
            undo_params = operation['params']
            undo_action(*undo_params)
        else:
            raise ControllerException(['There is no action left to undo.'])

    def redo_action(self):
        if self.can_redo():
            self.__pointer += 1
            operation = self.__operations[self.__pointer]['redo']
            redo_action = operation['action']
            redo_params = operation['params']
            redo_action(*redo_params)
        else:
            raise ControllerException(['There is no action to redo.'])

    def can_undo(self):
        return self.__pointer > -1

    def can_redo(self):
        return self.__pointer < len(self.__operations) - 1
