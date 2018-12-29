from domain.disease import Disease


class DiseaseRepository:

    def __init__(self):
        self.__persons = DiseaseRepository.read_persons_from_file('persons.txt')

    def update(self, person):
        self.__persons[self.find_person_index(person.get_id())] = person

    def get_all_persons(self):
        return self.__persons

    def get_person_by_id(self, id):
        return self.__persons[self.find_person_index(id)]

    def get_ill_persons_count(self):
        ill_persons = [person for person in self.__persons if person.get_status() == 'ill']
        return len(ill_persons)

    def find_person_index(self, id):
        for person_index in range(len(self.__persons)):
            if self.__persons[person_index].get_id() == id:
                return person_index
        raise Exception("No person found with the given ID.")

    @staticmethod
    def read_persons_from_file(file_name):
        persons = []
        try:
            file = open(file_name, 'r')
            line = file.readline().strip()
            while len(line) > 0:
                fields = line.split(',')
                persons.append(Disease(int(fields[0]), fields[1], fields[2]))
                line = file.readline().strip()
            file.close()
        except IOError as io_error:
            raise io_error
        return persons
