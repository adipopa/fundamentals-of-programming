"""
Module for handling user actions and printing values to the console.
"""

from modules.validation import *
from modules.business import *


def ui_add_transaction(bank_transactions, operations_queue, params):
    try:
        if len(params) != 3:
            raise IndexError
        try:
            value = resolve_value(params[0])
            type = resolve_type(params[1])
            description = params[2]
            add_transaction(bank_transactions, operations_queue, value, type, description)
            print("-bank-account: Added " + format_transaction_type(type) + " transaction for today of " +
                  str(value) + " RON with the '" + description + "' description.\n")
        except TypeError as type_error:
            print(str(type_error))
    except IndexError:
        print("-bank-account: Invalid syntax, please use: add <value> <type> <description>. For more information type 'help'.\n")


def ui_insert_transaction(bank_transactions, operations_queue, params):
    try:
        if len(params) != 4:
            raise IndexError
        try:
            day = resolve_day(params[0])
            value = resolve_value(params[1])
            type = resolve_type(params[2])
            description = params[3]
            insert_transaction(bank_transactions, operations_queue, day, value, type, description)
            print("-bank-account: Inserted " + format_transaction_type(type) + " transaction to day " + str(day) + " of " +
                  str(value) + " RON with the '" + description + "' description.\n")
        except TypeError as type_error:
            print(str(type_error))
    except IndexError:
        print("-bank-account: Invalid syntax, please use: insert <day> <value> <type> <description>. For more information type 'help'.\n")


def ui_remove_transactions(bank_transactions, operations_queue, params):
    try:
        if len(params) == 1:
            try:
                day = resolve_day(int(params[0]))
                remove_transactions_by_day(bank_transactions, operations_queue, day)
                print("-bank-account: Removed all transactions from day " + str(day) + ".\n")
            except ValueError:
                try:
                    type = resolve_type(params[0])
                    remove_transactions_by_type(bank_transactions, operations_queue, type)
                    print("-bank-account: Removed all " + format_transaction_type(type) + " transactions.\n")
                except TypeError as type_error:
                    print(str(type_error))
            except TypeError as type_error:
                print(str(type_error))
        elif len(params) == 3:
            try:
                start_day = resolve_day(params[0])
                if params[1] != 'to':
                    print("-bank-account: Invalid syntax, please use: remove <start day> to <end day>. For more information type 'help'.\n")
                    return
                end_day = resolve_day(params[2])
                if start_day > end_day:
                    print("-bank-account: Logical error, the <start_day> should be smaller or equal than the <end_day>.\n")
                    return
                remove_transactions_by_day_interval(bank_transactions, operations_queue, start_day, end_day)
                print("-bank-account: Removed all transactions between day " + str(start_day) + " and day " + str(end_day) + ".\n")
            except TypeError as type_error:
                print(str(type_error))
        else:
            raise IndexError
    except IndexError:
        print("-bank-account: Invalid syntax, please use: remove <day> / remove <start day> to <end day> / remove <type>. For more information type 'help'.\n")


def ui_replace_transaction(bank_transactions, operations_queue, params):
    try:
        if len(params) != 5:
            raise IndexError
        try:
            day = resolve_day(params[0])
            type = resolve_type(params[1])
            description = params[2]
            if params[3] != 'with':
                print("-bank-account: Invalid syntax, please use: replace <day> <type> <description> with <value>. For more information type 'help'.\n")
                return
            value = resolve_value(params[4])
            replace_transaction(bank_transactions, operations_queue, day, type, description, value)
            print("-bank-account: Replaced the amount for the " + format_transaction_type(type) + " transaction having the '" +
                  description + "' description from day " + str(day) + " with " + str(value) + " RON.\n")
        except TypeError as type_error:
            print(str(type_error))
    except IndexError:
        print("-bank-account: Invalid syntax, please use: replace <day> <type> <description> with <value>. For more information type 'help'.\n")


def ui_list_transactions(bank_transactions, params):
    try:
        operands = ['<', '=', '>']
        if len(params) == 0:
            transactions = get_transactions(bank_transactions)
            if len(transactions) == 0:
                print("-bank-account: It seems like you have zero transactions this month.\n")
                return
            print("-bank-account: List of this month's transactions:")
            ui_print_transactions(transactions)
        elif len(params) == 1:
            try:
                if params[0] in operands:
                    print("-bank-account: Invalid syntax, please use: list [ < | = | > ] <value>. For more information type 'help'.\n")
                    return
                if params[0] == 'balance':
                    print("-bank-account: Invalid syntax, please use: list balance <day>. For more information type 'help'.\n")
                    return
                type = resolve_type(params[0])
                transactions_by_type = get_transactions_by_type(bank_transactions, type)
                if len(transactions_by_type) == 0:
                    print("-bank-account: It seems like you have zero " + format_transaction_type(type) + " transactions this month.\n")
                    return
                print("-bank-account: List of this month's " + format_transaction_type(type) + " transactions:")
                ui_print_transactions(transactions_by_type)
            except TypeError as type_error:
                print(str(type_error))
        elif len(params) == 2:
            if params[0] in operands:
                try:
                    operand = params[0]
                    value = resolve_value(params[1])
                    transactions_by_value = get_transactions_by_value(bank_transactions, operand, value)
                    if len(transactions_by_value) == 0:
                        print("-bank-account: It seems like you have zero transactions with value " + operand + " " + str(value) + " this month.\n")
                        return
                    print("-bank-account: List of this month's transactions with value " + operand + " " + str(value) + ":")
                    ui_print_transactions(transactions_by_value)
                except TypeError as type_error:
                    print(str(type_error))
            elif params[0] == 'balance':
                try:
                    day = resolve_day(params[1])
                    balance = calculate_balance_on_day(bank_transactions, day)
                    print("-bank-account: Your account's balance on day " + str(day) + ": " + str(balance) + " RON.\n")
                except TypeError as type_error:
                    print(str(type_error))
            else:
                print("-bank-account: Invalid syntax, please use: list / list <type> / list [ < | = | > ] <value> / list balance <day>. For more information "
                      "type 'help'.\n")
                return
        else:
            raise IndexError
    except IndexError:
        print("-bank-account: Invalid syntax, please use: list / list <type> / list [ < | = | > ] <value> / list balance <day>. For more information "
              "type 'help'.\n")


def ui_sum_transactions(bank_transactions, params):
    try:
        if len(params) != 1:
            raise IndexError
        try:
            type = resolve_type(params[0])
            transactions_sum = sum_transactions(bank_transactions, type)
            print("-bank-account: The sum of all the " + format_transaction_type(type) + " transactions: " + str(transactions_sum) + " RON.\n")
        except TypeError as type_error:
            print(str(type_error))
    except IndexError:
        print("-bank-account: Invalid syntax, please use: sum <type>. For more information type 'help'.\n")


def ui_max_transaction(bank_transactions, params):
    try:
        if len(params) != 2:
            raise IndexError
        try:
            type = resolve_type(params[0])
            day = resolve_day(params[1])
            max_transaction = maximum_transaction(bank_transactions, type, day)
            if get_value(max_transaction) == 0:
                print("-bank-account: It seems like there are no " + format_transaction_type(type) + " transactions on day " + str(day) + ".\n")
                return
            print("-bank-account: The maximum " + format_transaction_type(type) + " transaction on day " + str(day) +
                  " is:\n" + build_transaction_message(max_transaction) + "\n")
        except TypeError as type_error:
            print(str(type_error))
    except IndexError:
        print("-bank-account: Invalid syntax, please use: max <type> <day>. For more information type 'help'.\n")


def ui_filter_transactions(bank_transactions, operations_queue, params):
    try:
        if len(params) == 1:
            try:
                type = resolve_type(params[0])
                filter_transactions(bank_transactions, operations_queue, type, None)
                print("-bank-account: Kept only the " + format_transaction_type(type) + " transactions.\n")
            except TypeError as type_error:
                print(str(type_error))
        elif len(params) == 2:
            try:
                type = resolve_type(params[0])
                value = resolve_value(params[1])
                filter_transactions(bank_transactions, operations_queue, type, value)
                print("-bank-account: Kept only the " + format_transaction_type(type) + " transactions having" +
                      " an amount of money smaller than " + str(value) + " RON.\n")
            except TypeError as type_error:
                print(str(type_error))
        else:
            raise IndexError
    except IndexError:
        print("-bank-account: Invalid syntax, please use: filter <type> / filter <type> <day>. For more information type 'help'.\n")


def ui_undo_last_operation(bank_transactions, operations_queue, params):
    try:
        if len(params) != 0:
            raise IndexError
        if len(operations_queue) == 0:
            print("There are zero operations left to undo.\n")
            return
        undo_last_operation(bank_transactions, operations_queue)
        print("-bank-account: Reversed the last bank account operation.\n")
    except IndexError:
        print("-bank-account: Invalid syntax, please use: undo. For more information type 'help'.\n")


def ui_show_commands():
    print("BANK ACCOUNT management, version 1.2 (python).")
    print("These commands are defined internally.  Type 'help' to see this list.\n")
    print(" add <value> <type> <description> - adds to the current day an <type> transaction of <value> RON with the <description> description.")
    print(" insert <day> <value> <type> <description> - inserts to day <day> an <type> transaction of <value> RON with the <description> description.\n")
    print(" remove <day> - removes all transactions from day <day>.")
    print(" remove <start day> to <end day> - removes all transactions between day <start day> and day <end day>.")
    print(" remove <type> - removes all the <type> transactions from the current month.")
    print(" replace <day> <type> <description> with <value> - replaces the amount for the <type> transaction having the <description> "
          "description from day <day> with <value> RON.\n")
    print(" list - displays the entire list of transactions.")
    print(" list <type> - displays all the <type> transactions.")
    print(" list [ < | = | > ] <value> - displays all transactions having an amount of money [ < | = | > ] than <value>.")
    print(" list balance <day> - computes the account’s balance on day <day>. This is the sum of all 'in' transactions, from which we "
          "subtract 'out' transactions occurring before or on day <day>.\n")
    print(" sum <type> - displays the total amount from <type> transactions.")
    print(" max <type> <day> - displays the maximum <type> transaction on day <day>.\n")
    print(" filter <type> - keeps only <type> transactions.")
    print(" filter <type> <value> - keeps only <type> transactions having an amount of money smaller than <value> RON.\n")
    print(" undo - reverses the last operation that has modified program data.\n")


def ui_print_transactions(bank_transactions):
    for transaction in get_sorted_transactions(bank_transactions):
        print(build_transaction_message(transaction))
    print()


def run_user_interface(bank_transactions, operations_queue):
    print("Welcome John to your bank account management app!")
    print("Please use one of the available commands (type 'help' to display them).\n")
    while True:
        user_input = input("bank-account:~ john$ ").split()
        modify_transactions_options = {
            'add': ui_add_transaction,
            'insert': ui_insert_transaction,
            'remove': ui_remove_transactions,
            'replace': ui_replace_transaction,
            'filter': ui_filter_transactions,
            'undo': ui_undo_last_operation
        }
        display_only_options = {
            'list': ui_list_transactions,
            'sum': ui_sum_transactions,
            'max': ui_max_transaction
        }
        command = user_input[0]
        if command in modify_transactions_options:
            modify_transactions_options[command](bank_transactions, operations_queue, user_input[1:])
        elif command in display_only_options:
            display_only_options[command](bank_transactions, user_input[1:])
        elif command == 'help':
            ui_show_commands()
        elif command == 'exit':
            return
        else:
            print("Command not found! Please use one of the available commands (type 'help' to display them).\n")