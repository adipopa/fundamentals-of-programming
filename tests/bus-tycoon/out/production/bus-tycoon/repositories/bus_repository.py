from domain.bus import Bus


class BusRepository:

    def __init__(self):
        self.__buses = BusRepository.read_buses_from_file('buses.txt')

    def get_bus_by_id(self, bus_id):
        for bus in self.__buses:
            if bus.get_bus_id() == bus_id:
                return bus
        raise Exception("No bus found.")

    @staticmethod
    def read_buses_from_file(file_name):
        buses = []
        file = open(file_name, 'r')
        line = file.readline().strip()
        while len(line) > 0:
            arguments = line.split(',')
            buses.append(Bus(int(arguments[0]), int(arguments[1]), arguments[2], int(arguments[3])))
            line = file.readline().strip()
        file.close()
        return buses
