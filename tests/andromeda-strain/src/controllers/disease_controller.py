class DiseaseController:

    def __init__(self, disease_repository):
        self.__disease_repository = disease_repository
        self.__day_number = 1

    def simulate_day(self):
        if self.__day_number == 3:
            for person in self.__disease_repository.get_all_persons():
                person.set_status('healthy')
                self.__disease_repository.update(person)

        ill_persons_count = self.__disease_repository.get_ill_persons_count()
        for person in self.__disease_repository.get_all_persons():
            if ill_persons_count <= 0:
                break
            if person.get_status() == 'healthy' and person.get_immunization_status() == 'non-vaccinated':
                person.set_status('ill')
                self.__disease_repository.update(person)
                ill_persons_count -= 1
        self.__day_number += 1

        return self.__disease_repository.get_all_persons()

    def vaccinate_person(self, id):
        person = self.__disease_repository.get_person_by_id(id)
        if person.get_status() == 'healthy':
            person.set_immunization_status('vaccinated')
            self.__disease_repository.update(person)
