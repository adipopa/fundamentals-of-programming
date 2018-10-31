def get_day(transaction):
    return transaction['day']


def set_day(transaction, day):
    transaction['day'] = day


def get_value(transaction):
    return transaction['value']


def set_value(transaction, value):
    transaction['value'] = value


def get_type(transaction):
    return transaction['type']


def set_type(transaction, type):
    transaction['type'] = type


def get_description(transaction):
    return transaction['description']


def set_description(transaction, description):
    transaction['description'] = description


def build_transaction(day, value, type, description):
    transaction = {}
    set_day(transaction, day)
    set_value(transaction, value)
    set_type(transaction, type)
    set_description(transaction, description)
    return transaction


def find_transaction(bank_transactions, day, type, description):
    for index in range(len(bank_transactions)):
        transaction = bank_transactions[index]
        if get_day(transaction) == day and get_type(transaction) == type and get_description(transaction) == description:
            return index
    return -1
