"""
Module that contains all the necessary utility functions used inside the program.
"""

from datetime import datetime
from modules.model import *


def get_current_day():
    return int(datetime.today().day)


def format_transaction_type(type):
    return 'incoming' if type == 'in' else 'outgoing'


def build_transaction_message(transaction):
    return format_transaction_type(get_type(transaction)).capitalize() + " transaction of " + str(get_value(transaction)) + " RON on day " + \
        str(get_day(transaction)) + ", description: '" + get_description(transaction) + "'."


def get_sorted_transactions(bank_transactions):
    return sorted(bank_transactions, key=lambda transaction: transaction['day'])


def find_transaction(bank_transactions, day, type, description):
    for index in range(len(bank_transactions)):
        transaction = bank_transactions[index]
        if get_day(transaction) == day and get_type(transaction) == type and get_description(transaction) == description:
            return index
    return -1


def filter_out_transactions_by_type(bank_transactions, type):
    return [transaction for transaction in bank_transactions if get_type(transaction) != type]


def filter_out_transactions_by_day(bank_transactions, day):
    return [transaction for transaction in bank_transactions if get_day(transaction) != day]


def filter_out_transactions_by_day_interval(bank_transactions, start_day, end_day):
    return [transaction for transaction in bank_transactions if get_day(transaction) < start_day or get_day(transaction) > end_day]


def filter_transactions_by_type(bank_transactions, type):
    return [transaction for transaction in bank_transactions if get_type(transaction) == type]


def filter_transactions_by_value(bank_transactions, operand, value):
    if operand == '<':
        return [transaction for transaction in bank_transactions if get_value(transaction) < value]
    elif operand == '=':
        return [transaction for transaction in bank_transactions if get_value(transaction) == value]
    elif operand == '>':
        return [transaction for transaction in bank_transactions if get_value(transaction) > value]
