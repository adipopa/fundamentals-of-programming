def resolve_day(day_argument):
    error_message = "-bank-account: add: Argument <day> must be an integer with value between 1 and 31.\n"
    try:
        day = int(day_argument)
        if day < 1 or day > 31:
            raise TypeError(error_message)
        return day
    except ValueError:
        raise TypeError(error_message)


def resolve_value(value_argument):
    error_message = "-bank-account: add: Argument <value> must be a positive integer.\n"
    try:
        value = int(value_argument)
        if value <= 0:
            raise TypeError(error_message)
        return value
    except ValueError:
        raise TypeError(error_message)


def resolve_type(type_argument):
    if type_argument != 'in' and type_argument != 'out':
        raise TypeError("-bank-account: add: Argument <type> must be either 'in' or 'out'.\n")
    return type_argument