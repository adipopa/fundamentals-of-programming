"""
Module that handles all the major business related actions.
"""

from copy import deepcopy
from modules.utils import *


def add_transaction_to_list(bank_transactions, transaction):
    bank_transactions.append(transaction)


def append_operations_queue(bank_transactions, operations_queue):
    if len(operations_queue) != 0:
        if bank_transactions == operations_queue[-1]:
            return
    operations_queue.append(deepcopy(bank_transactions))


def add_transaction(bank_transactions, operations_queue, value, type, description):
    append_operations_queue(bank_transactions, operations_queue)
    day = get_current_day()
    transaction = build_transaction(day, value, type, description)
    add_transaction_to_list(bank_transactions, transaction)


def insert_transaction(bank_transactions, operations_queue, day, value, type, description):
    append_operations_queue(bank_transactions, operations_queue)
    transaction = build_transaction(day, value, type, description)
    add_transaction_to_list(bank_transactions, transaction)


def remove_transactions_by_day(bank_transactions, operations_queue, day):
    append_operations_queue(bank_transactions, operations_queue)
    transactions_by_day = filter_out_transactions_by_day(bank_transactions, day)
    bank_transactions[:] = transactions_by_day


def remove_transactions_by_day_interval(bank_transactions, operations_queue, start_day, end_day):
    append_operations_queue(bank_transactions, operations_queue)
    transactions_by_day_interval = filter_out_transactions_by_day_interval(bank_transactions, start_day, end_day)
    bank_transactions[:] = transactions_by_day_interval


def remove_transactions_by_type(bank_transactions, operations_queue, type):
    append_operations_queue(bank_transactions, operations_queue)
    transactions_by_type = filter_out_transactions_by_type(bank_transactions, type)
    bank_transactions[:] = transactions_by_type


def replace_transaction(bank_transactions, operations_queue, day, type, description, value):
    append_operations_queue(bank_transactions, operations_queue)
    transaction_index = find_transaction(bank_transactions, day, type, description)
    if transaction_index != -1:
        set_value(bank_transactions[transaction_index], value)


def get_transactions(bank_transactions):
    return bank_transactions


def get_transactions_by_type(bank_transactions, type):
    return filter_transactions_by_type(bank_transactions, type)


def get_transactions_by_value(bank_transactions, operand, value):
    return filter_transactions_by_value(bank_transactions, operand, value)


def calculate_balance_on_day(bank_transactions, day):
    balance = 0
    for transaction in bank_transactions:
        if get_day(transaction) <= day:
            if get_type(transaction) == 'in':
                balance += get_value(transaction)
            else:
                balance -= get_value(transaction)
    return balance


def sum_transactions(bank_transactions, type):
    transactions_sum = 0
    for transaction in bank_transactions:
        if get_type(transaction) == type:
            transactions_sum += get_value(transaction)
    return transactions_sum


def maximum_transaction(bank_transactions, type, day):
    max_transaction = build_transaction(None, 0, None, None)
    for transaction in bank_transactions:
        if get_type(transaction) == type and get_day(transaction) == day:
            if get_value(transaction) > get_value(max_transaction):
                max_transaction = transaction
    return max_transaction


def filter_transactions(bank_transactions, operations_queue, type, value):
    append_operations_queue(bank_transactions, operations_queue)
    filtered_transactions = filter_transactions_by_type(bank_transactions, type)
    if value is not None:
        filtered_transactions = filter_transactions_by_value(filtered_transactions, '<', value)
    bank_transactions[:] = filtered_transactions


def undo_last_operation(bank_transactions, operations_queue):
    bank_transactions[:] = operations_queue[-1]
    del operations_queue[-1]


def generate_bank_transactions(bank_transactions):
    add_transaction_to_list(bank_transactions, build_transaction(3, 450, 'in', 'sale'))
    add_transaction_to_list(bank_transactions, build_transaction(4, 80, 'out', 'shirt'))
    add_transaction_to_list(bank_transactions, build_transaction(8, 24, 'out', 'food'))
    add_transaction_to_list(bank_transactions, build_transaction(8, 17, 'out', 'groceries'))
    add_transaction_to_list(bank_transactions, build_transaction(14, 2300, 'in', 'salary'))
    add_transaction_to_list(bank_transactions, build_transaction(14, 250, 'in', 'sneakers'))
    add_transaction_to_list(bank_transactions, build_transaction(15, 1250, 'out', 'phone'))
    add_transaction_to_list(bank_transactions, build_transaction(17, 300, 'out', 'gas'))
    add_transaction_to_list(bank_transactions, build_transaction(23, 5000, 'in', 'credit'))
    add_transaction_to_list(bank_transactions, build_transaction(27, 2400, 'out', 'fridge'))
