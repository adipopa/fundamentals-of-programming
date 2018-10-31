from utils import *


def add_transaction_to_list(bank_transactions, transaction, show_confirmation_message=True):
    bank_transactions.append(transaction)
    if show_confirmation_message:
        print_value = "-bank-account: Added " + format_transaction_type(get_type(transaction)) + " transaction to day " + str(get_day(transaction)) + " of " + \
                      str(get_value(transaction)) + " RON with the '" + get_description(transaction) + "' description.\n"
        print(print_value)


def add_transaction(bank_transactions, value, type, description):
    day = get_current_day()
    transaction = build_transaction(day, value, type, description)
    add_transaction_to_list(bank_transactions, transaction)


def insert_transaction(bank_transactions, day, value, type, description):
    transaction = build_transaction(day, value, type, description)
    add_transaction_to_list(bank_transactions, transaction)


def remove_transactions_by_day(bank_transactions, day):
    transactions_by_day = filter_transactions_by_day(bank_transactions, day)
    bank_transactions[:] = transactions_by_day
    print("-bank-account: Removed all transactions from day " + str(day) + ".\n")


def remove_transactions_by_day_interval(bank_transactions, start_day, end_day):
    if start_day > end_day:
        print("-bank-account: Logical error, the <start_day> should be smaller or equal than the <end_day>.\n")
        return
    transactions_by_day_interval = filter_transactions_by_day_interval(bank_transactions, start_day, end_day)
    bank_transactions[:] = transactions_by_day_interval
    print("-bank-account: Removed all transactions between day " + str(start_day) + " and day " + str(end_day) + ".\n")


def remove_transactions_by_type(bank_transactions, type):
    transactions_by_type = filter_transactions_by_type(bank_transactions, type)
    bank_transactions[:] = transactions_by_type
    print("-bank-account: Removed all " + format_transaction_type(type) + " transactions.\n")


def replace_transaction(bank_transactions, day, type, description, value):
    transaction_index = find_transaction(bank_transactions, day, type, description)
    if transaction_index != -1:
        set_value(bank_transactions[transaction_index], value)
    print("-bank-account: Replaced the amount for the " + format_transaction_type(type) + " transaction having the '" +
          description + "' description from day " + str(day) + " with " + str(value) + " RON.\n")


def list_transactions(bank_transactions):
    if len(bank_transactions) == 0:
        print("-bank-account: It seems like you have zero transactions this month.\n")
        return
    print("-bank-account: List of this month's transactions:")
    for transaction in bank_transactions:
        print(build_list_message(transaction))
    print()


def list_transactions_by_type(bank_transactions, type):
    transactions_by_type = find_transactions_by_type(bank_transactions, type)
    if len(transactions_by_type) == 0:
        print("-bank-account: It seems like you have zero " + format_transaction_type(type) + " transactions this month.\n")
        return
    print("-bank-account: List of this month's " + format_transaction_type(type) + " transactions:")
    for transaction in transactions_by_type:
        print(build_list_message(transaction))
    print()


def list_transactions_by_value(bank_transactions, operand, value):
    transactions_by_value = find_transactions_by_value(bank_transactions, operand, value)
    if len(transactions_by_value) == 0:
        print("-bank-account: It seems like you have zero transactions with value " + operand + " " + str(value) + " this month.\n")
        return
    print("-bank-account: List of this month's transactions with value " + operand + " " + str(value) + ":")
    for transaction in transactions_by_value:
        print(build_list_message(transaction))
    print()


def calculate_balance_on_day(bank_transactions, day):
    balance = 0
    for transaction in bank_transactions:
        if get_day(transaction) <= day:
            if get_type(transaction) == 'in':
                balance += get_value(transaction)
            else:
                balance -= get_value(transaction)
    print("-bank-account: Your account's balance on day " + str(day) + ": " + str(balance) + "RON.\n")


def generate_bank_transactions(bank_transactions):
    add_transaction_to_list(bank_transactions, build_transaction(3, 450, 'in', 'sale'), False)
    add_transaction_to_list(bank_transactions, build_transaction(4, 80, 'out', 'shirt'), False)
    add_transaction_to_list(bank_transactions, build_transaction(7, 250, 'out', 'sneakers'), False)
    add_transaction_to_list(bank_transactions, build_transaction(8, 24, 'out', 'food'), False)
    add_transaction_to_list(bank_transactions, build_transaction(8, 17, 'out', 'groceries'), False)
    add_transaction_to_list(bank_transactions, build_transaction(14, 2300, 'in', 'salary'), False)
    add_transaction_to_list(bank_transactions, build_transaction(15, 1250, 'out', 'phone'), False)
    add_transaction_to_list(bank_transactions, build_transaction(17, 300, 'out', 'gas'), False)
    add_transaction_to_list(bank_transactions, build_transaction(23, 5000, 'in', 'credit'), False)
    add_transaction_to_list(bank_transactions, build_transaction(27, 2400, 'out', 'fridge'), False)
