from datetime import date, timedelta


def read_date_of_birth():
    """
    The function reads a line from the console and returns the date of birth value.
    :return date_of_birth < current date, date_of_birth - date:
    """
    print("Please use the DD/MM/YYYY format when inserting the date.\n")
    while True:
        try:
            date_entry = input("Please enter the date of birth: ")
            day, month, year = map(int, date_entry.split('/'))
            if date(year, month, day) <= date.today():
                return date(year, month, day)
            else:
                print("LOGIC ERROR: The date of birth cannot be greater than the current date.\n")
        except ValueError:
            print("VALUE ERROR: The input date must be valid and must respect the DD/MM/YYYY format.\n")


def calculate_age_in_days(date_of_birth):
    """
    The function takes the date_of_birth value and calculates the age in number of days.
    :param date_of_birth:
    pre-condition: date_of_birth < current date, date_of_birth - date
    :return age_in_days:
    post-condition: age_in_days >= 0, age_in_days - integer
    """
    return (date.today() - date_of_birth).days


def print_age_in_days(age_in_days):
    """
    The function prints to the console the age value in number of days.
    :param age_in_days:
    pre-condition: age_in_days >= 0, age_in_days - integer
    :return:
    """
    print("The age is equal to " + str(age_in_days) + " days.")


def run_tests():
    """
    Testing if the function calculate_age_in_days(date_of_birth) returns the expected value (an INTEGER).
    Tests were written on October 10, 2018, which means that some values have to be greater or equal
    than the expected value.
    :return:
    """
    assert calculate_age_in_days(date(1999, 8, 5)) >= 7006
    assert calculate_age_in_days(date(2017, 1, 1)) >= 647
    assert calculate_age_in_days(date.today() - timedelta(days=253)) == 253
    assert calculate_age_in_days(date.today()) == 0


def run():
    """
    The function starts the entire program.
    :return:
    """
    date_of_birth = read_date_of_birth()
    age_in_days = calculate_age_in_days(date_of_birth)
    print_age_in_days(age_in_days)


run_tests()
run()
