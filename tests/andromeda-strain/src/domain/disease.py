class Disease:

    def __init__(self, id, immunization_status, status):
        self.__id = id
        self.__immunization_status = immunization_status
        self.__status = status

    def get_id(self):
        return self.__id

    def get_immunization_status(self):
        return self.__immunization_status

    def get_status(self):
        return self.__status

    def set_immunization_status(self, immunization_status):
        self.__immunization_status = immunization_status

    def set_status(self, status):
        self.__status = status

    def __eq__(self, other):
        return self.__id == other.__id

    def __str__(self):
        return "ID: " + str(self.__id) + ", immunization status: " + \
               self.__immunization_status + ", status: " + self.__status
