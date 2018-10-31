from math import sqrt, pow


def get_real_part(complex_number):
    """
    The function returns the real part of a given complex number.
    :param complex_number:
    :return:
    """
    return complex_number['real']


def set_real_part(complex_number, real):
    """
    The function sets the real part for a given complex number.
    :param complex_number:
    :param real:
    :return:
    """
    complex_number['real'] = real


def get_imaginary_part(complex_number):
    """
    The function returns the imaginary part of a given complex number.
    :param complex_number:
    :return:
    """
    return complex_number['imaginary']


def set_imaginary_part(complex_number, imaginary):
    """
    The function sets the real part for a given complex number.
    :param complex_number:
    :param imaginary:
    :return:
    """
    complex_number['imaginary'] = imaginary


def get_last_key(complex_numbers_dictionary):
    """
    The function returns the last key (index) of the complex_numbers_dictionary dictionary or 0 if the dictionary is empty.
    :param complex_numbers_dictionary:
    :return:
    """
    list_of_keys = list(complex_numbers_dictionary.keys())
    if len(list_of_keys) > 0:
        return list_of_keys[-1]
    return -1


def build_complex_number(input_value):
    """
    The function builds and returns a complex number object from the given input_value
    :param input_value:
    :return:
    """
    real_part = imaginary_part = 0

    if input_value.find(" + ") != -1:
        if input_value.find('i') != len(input_value) - 1:
            raise ValueError()
        real_part, imaginary_part = map(int, input_value.replace('i', '').split(" + "))
    elif input_value.find(" - ") != -1:
        if input_value.find('i') != len(input_value) - 1:
            raise ValueError()
        real_part, imaginary_part = map(int, input_value.replace('i', '').replace(" - ", ' -').split(' '))
    else:
        if input_value.find('i') != len(input_value) - 1:
            real_part = int(input_value)
        else:
            imaginary_part = int(input_value.replace('i', ''))

    complex_number = {}
    set_real_part(complex_number, real_part)
    set_imaginary_part(complex_number, imaginary_part)
    return complex_number


def add_number_to_dictionary(complex_numbers_dictionary, complex_number):
    """
    The function appends a complex number to the dictionary complex_numbers_dictionary
    :param complex_numbers_dictionary:
    :param complex_number:
    :return:
    """
    index = get_last_key(complex_numbers_dictionary) + 1
    complex_numbers_dictionary[index] = complex_number


def print_dictionary(complex_numbers_dictionary, start_index, end_index):
    """
    The function formats and prints all the complex numbers from the complex_numbers_dictionary dictionary to the console.
    :param complex_numbers_dictionary:
    :param start_index:
    :param end_index:
    :return:
    """
    for index in range(start_index, end_index):
        complex_number = complex_numbers_dictionary[index]
        value_to_print = "z" + str(index) + " = "

        real_part = get_real_part(complex_number)
        imaginary_part = get_imaginary_part(complex_number)

        if real_part != 0 and imaginary_part != 0:
            value_to_print += str(real_part) + (" + " if imaginary_part > 0 else " - ") + str(imaginary_part).replace('-', '') + 'i'
        elif real_part == 0 and imaginary_part != 0:
            value_to_print += str(imaginary_part) + "i"
        else:
            value_to_print += str(real_part)

        print(value_to_print)
    print()


def count_distinct_values(current_list):
    """
    The function return the number of distinct values from a list
    :param current_list:
    :return:
    """
    distinct_values = []
    for value in current_list:
        if value not in distinct_values:
            distinct_values.append(value)
    return len(distinct_values)


def at_most_3_distinct_values(complex_numbers_dictionary):
    """
    The function returns the longest sequence of complex_numbers_dictionary that contains at most 3 distinct values.
    :param complex_numbers_dictionary:
    :return:
    """
    max_sequence_length = 0
    start_index = 0

    length_of_dictionary = get_last_key(complex_numbers_dictionary) + 1

    if length_of_dictionary == 0:
        print("The sequence is empty because there are no complex numbers in the dictionary.\n")
        return

    for first_index in range(0, length_of_dictionary):
        sequence = []
        sequence_length = 0
        for second_index in range(first_index, length_of_dictionary):
            number_to_check = complex_numbers_dictionary[second_index]
            sequence.append(number_to_check)
            if count_distinct_values(sequence) <= 3:
                sequence_length += 1
            else:
                if sequence_length > max_sequence_length:
                    max_sequence_length = sequence_length
                    start_index = first_index
                break

        if sequence_length > max_sequence_length:
            max_sequence_length = sequence_length
            start_index = first_index

    print("The longest sequence that contains at most 3 distinct values is:")
    print_dictionary(complex_numbers_dictionary, start_index, start_index + max_sequence_length)


def modulus(complex_number):
    """
    The function returns the modulus of a complex number.
    :param complex_number:
    :return:
    """
    return sqrt(pow(get_real_part(complex_number), 2) + pow(get_imaginary_part(complex_number), 2))


def same_modulus(number_a, number_b):
    """
    The function checks if two numbers have different modulus.
    :param number_a:
    :param number_b:
    :return:
    """
    return modulus(number_a) == modulus(number_b)


def numbers_with_same_modulus(complex_numbers_dictionary):
    """
    The function returns the longest sequence of complex_numbers_dictionary that has numbers with same modulus.
    :param complex_numbers_dictionary:
    :return:
    """
    max_sequence_length = 0
    start_index = 0

    length_of_dictionary = get_last_key(complex_numbers_dictionary) + 1

    if length_of_dictionary == 0:
        print("The sequence is empty because there are no complex numbers in the dictionary.\n")
        return

    for first_index in range(0, length_of_dictionary):
        first_number_to_compare = complex_numbers_dictionary[first_index]
        sequence_length = 1
        for second_index in range(first_index + 1, length_of_dictionary):
            second_number_to_compare = complex_numbers_dictionary[second_index]
            if same_modulus(first_number_to_compare, second_number_to_compare):
                sequence_length += 1
            else:
                if sequence_length > max_sequence_length:
                    max_sequence_length = sequence_length
                    start_index = first_index
                break

        if sequence_length > max_sequence_length:
            max_sequence_length = sequence_length
            start_index = first_index

    print("The longest sequence that has numbers with same modulus:")
    print_dictionary(complex_numbers_dictionary, start_index, start_index + max_sequence_length)


def ui_read_dictionary(complex_numbers_dictionary):
    """
    The function reads an input from the console and adds the built complex number to
    the complex_numbers_dictionary dictionary.
    :param complex_numbers_dictionary:
    :return:
    """
    while True:
        option = input("Add a number to the dictionary by typing 'add' or go back to the main menu by typing 'back': ")
        if option == "add":
            while True:
                try:
                    input_value = input('Insert a complex number (z = a + bi form), z = ')
                    complex_number = build_complex_number(input_value)
                    add_number_to_dictionary(complex_numbers_dictionary, complex_number)
                    print("Number z = " + input_value + " successfully added.\n")
                    break
                except ValueError:
                    print("VALUE ERROR: Please retry using a valid complex number.\n")
                    break
        elif option == "back":
            print()
            break
        else:
            print("Invalid option, please choose from the given options above.\n")


def ui_longest_sequence_of(complex_numbers_dictionary):
    """
    The function displays a menu to let the user choose between the two properties that a sequence can have.
    :return:
    """
    print("a) ... contains at most 3 distinct values.")
    print("b) ... has numbers with same modulus.\n")
    while True:
        option = input("Choose option 'a' or 'b' or go back by typing 'back': ")
        if option == "a":
            at_most_3_distinct_values(complex_numbers_dictionary)
        elif option == "b":
            numbers_with_same_modulus(complex_numbers_dictionary)
        elif option == "back":
            break
        else:
            print("Invalid option, please choose from the given options above.\n")


def ui_print_dictionary(complex_numbers_dictionary):
    """
    The function calls the print_dictionary(complex_numbers_dictionary) function
    :return:
    """
    length_of_dictionary = get_last_key(complex_numbers_dictionary) + 1
    if length_of_dictionary == 0:
        print("There are no complex numbers in the dictionary.\n")
        return
    print("The dictionary of complex numbers:")
    print_dictionary(complex_numbers_dictionary, 0, length_of_dictionary)


def generate_initial_dictionary(complex_numbers_dictionary):
    """
    The function adds 10 initial values to the complex_numbers_dictionary dictionary.
    :return:
    """
    add_number_to_dictionary(complex_numbers_dictionary, build_complex_number("3i"))
    add_number_to_dictionary(complex_numbers_dictionary, build_complex_number("5 - 3i"))
    add_number_to_dictionary(complex_numbers_dictionary, build_complex_number("5 + 3i"))
    add_number_to_dictionary(complex_numbers_dictionary, build_complex_number("-5 + 3i"))
    add_number_to_dictionary(complex_numbers_dictionary, build_complex_number("7"))
    add_number_to_dictionary(complex_numbers_dictionary, build_complex_number("7"))
    add_number_to_dictionary(complex_numbers_dictionary, build_complex_number("4 - 3i"))
    add_number_to_dictionary(complex_numbers_dictionary, build_complex_number("4 - 3i"))
    add_number_to_dictionary(complex_numbers_dictionary, build_complex_number("1 + 1i"))
    add_number_to_dictionary(complex_numbers_dictionary, build_complex_number("3 + 5i"))


def run_menu():
    """
    The function starts the program and displays the main menu, giving the user the
    option to choose from a list of commands.
    :return:
    """
    print("Application started! Please choose from one of the options below by specifying the option's index.\n")
    print("1. Append list of complex numbers.")
    print("2. Display all complex numbers.")
    print("3. Display the longest sequence that...")
    print("0. Exit the application.\n")
    complex_numbers_dictionary = {}
    generate_initial_dictionary(complex_numbers_dictionary)
    while True:
        option = input("Choose one of the main options: ")
        available_options = {
            "1": ui_read_dictionary,
            "2": ui_print_dictionary,
            "3": ui_longest_sequence_of
        }
        if option in available_options:
            available_options[option](complex_numbers_dictionary)
        elif option == '0':
            return
        else:
            print("Invalid option, please choose from the given options above.\n")


run_menu()
