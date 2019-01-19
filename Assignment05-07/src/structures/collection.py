class Collection:

    def __init__(self):
        self.__data = []

    def add(self, item):
        self.__data.append(item)

    def __setitem__(self, key, value):
        self.__data[key] = value

    def __delitem__(self, key):
        del self.__data[key]

    def __getitem__(self, key):
        return self.__data[key]

    def __next__(self):
        """
        Returns the next element of the iteration
        """
        if self.__iterPosition >= len(self.__data):
            raise StopIteration()
        result = self.__data[self.__iterPosition]
        self.__iterPosition = self.__iterPosition + 1
        return result

    def __iter__(self):
        """
        Return an iterator
        """
        self.__iterPosition = 0
        return self

    def __len__(self):
        return len(self.__data)


def gnome_sort(items, sort_function):
    # we start from index 0
    index = 0
    # repeat the following steps until the index reaches the end of the array (i.e-'len(items)-1')
    while index < len(items):
        # if we are at the start of the array then go to the right element (from items[0] to items[1])
        if index == 0:
            index = index + 1
        # else, using the sort_function function provided by the upper level, compare the previous array element with
        # the current array element, if the function returns TRUE then go one step to the right
        elif sort_function(items[index - 1], items[index]):
            index = index + 1
        # otherwise, swap these two elements and go one step backwards
        else:
            items[index], items[index - 1] = items[index - 1], items[index]
            index = index - 1
    # if the end of the array is reached then stop and return the now sorted array
    return items[:]


def filter_items(items, filter_function):
    return [item for item in items if filter_function(item)]
