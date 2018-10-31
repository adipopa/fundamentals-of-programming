def list_of_digits(n):
    """
    The function generates a list of unique digits from a given integer n.
    :param n:
    pre-condition: n >= 0, n - integer
    :return digits_list:
    post-condition: digits_list = [d0, d1, ..., dn-1], di where i=0,len(n), di - integer
    """
    digits_list = []
    while n > 0:
        digit = int(n % 10)
        if digit not in digits_list:
            digits_list.append(digit)
        n = int(n / 10)
    return digits_list


def read_number(index):
    """
    The function reads a line from the console and returns the integer value n if the input is valid.
    :param index:
    pre-condition: index = 1/2, index - integer
    :return n:
    post-condition: n >= 0, n - integer
    """
    while True:
        line = input("Please provide the first number n1: ") if index == 1 \
            else input("Please provide the second number n2: ")
        try:
            n = int(line)
            if n < 0:
                raise ValueError()
            return n
        except ValueError:
            print("VALUE ERROR: The input value must be a natural number.\n")


def check_property_p(n1, n2):
    """
    The function checks if the writings in base 10 for the integers n1 and n2 have the same digits.
    :param n1, n2:
    pre-condition: n1, n2 >= 0, n1, n2 - integers
    :return r:
    post-condition: r = True / False, r - boolean
    """
    return set(list_of_digits(n1)) == set(list_of_digits(n2))


def print_result(result):
    """
    The function prints to the console the result of the check for property p.
    :param result:
    pre-condition: result = True / False, result - boolean
    :return:
    """
    print("The writings in base 10 for the given numbers " + ("have" if result else "don't have") + " the same digits.")


def run():
    """
    The function starts the entire program.
    :return:
    """
    n1 = read_number(1)
    n2 = read_number(2)
    numbers_have_property_p = check_property_p(n1, n2)
    print_result(numbers_have_property_p)


def run_tests():
    """
    Testing if the function check_property_p(n1, n2) returns the expected value (TRUE or FALSE).
    :return:
    """
    assert check_property_p(2113, 323121) == True
    assert check_property_p(123123, 1234123) == False
    assert check_property_p(4, 4) == True
    assert check_property_p(3, 7) == False
    assert check_property_p(0, 0) == True
    assert check_property_p(1231204124124, 4123102131204214) == True
    assert check_property_p(1231782414124124124, 42341212842) == False


run_tests()
run()
