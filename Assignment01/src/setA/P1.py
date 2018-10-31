from math import sqrt


def is_prime(n):
    """
    The function checks if the integer value n is a prime number.
    :param n:
    pre-condition: n >= 0, n - integer
    :return r:
    post-condition: r = True / False, r - boolean
    """
    if n < 2:
        return False

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    d = 3
    while d <= sqrt(n):
        if n % d == 0:
            return False
        d = d + 2

    return True


def read_number():
    """
    The function reads a line from the console and returns the integer value n if the input is valid.
    :return n:
    post-condition: n >= 0, n - integer
    """
    while True:
        line = input("Please provide the number n: ")
        try:
            n = int(line)
            if n < 0:
                raise ValueError()
            return n
        except ValueError:
            print("VALUE ERROR: The input value must be a natural number.\n")


def generate_prime_number(n):
    """
    The function increments the integer value n to find the first prime number larger than the initial value.
    :param n:
    pre-condition: n >= 0, n - integer
    :return n:
    post-condition: n >= 0, n - integer
    """
    while True:
        n += 1
        if is_prime(n):
            return n


def print_prime(n):
    """
    The function prints to the console the first prime number larger than n.
    :param n:
    pre-condition: n >= 0, n - integer
    :return:
    """
    print("The first prime number larger than n is: " + str(n))


def run_tests():
    """
    Testing if the function generate_prime_number(n) returns the expected value (an INTEGER).
    :return:
    """
    assert generate_prime_number(2) == 3
    assert generate_prime_number(24) == 29
    assert generate_prime_number(47) == 53
    assert generate_prime_number(1) == 2
    assert generate_prime_number(0) == 2
    assert generate_prime_number(2147483629) == 2147483647


def run():
    """
    The function starts the entire program.
    :return:
    """
    n = read_number()
    prime = generate_prime_number(n)
    print_prime(prime)


run_tests()
run()
