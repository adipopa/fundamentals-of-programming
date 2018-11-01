"""
Module that handles the model and state of a transaction.
"""


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
