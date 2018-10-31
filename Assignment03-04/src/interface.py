from business import *
from validation import *


def ui_add_transaction(bank_transactions, params):
    try:
        if len(params) != 3:
            raise IndexError
        try:
            value = resolve_value(params[0])
            type = resolve_type(params[1])
            description = params[2]
            add_transaction(bank_transactions, value, type, description)
        except TypeError as te:
            print(str(te))
    except IndexError:
        print("-bank-account: Invalid syntax, please use: add <value> <type> <description>. For more information type 'help'.\n")


def ui_insert_transaction(bank_transactions, params):
    try:
        if len(params) != 4:
            raise IndexError
        try:
            day = resolve_day(params[0])
            value = resolve_value(params[1])
            type = resolve_type(params[2])
            description = params[3]
            insert_transaction(bank_transactions, day, value, type, description)
        except TypeError as te:
            print(str(te))
    except IndexError:
        print("-bank-account: Invalid syntax, please use: insert <day> <value> <type> <description>. For more information type 'help'.\n")


def ui_remove_transactions(bank_transactions, params):
    try:
        if len(params) == 1:
            try:
                day = resolve_day(int(params[0]))
                remove_transactions_by_day(bank_transactions, day)
            except ValueError:
                try:
                    type = resolve_type(params[0])
                    remove_transactions_by_type(bank_transactions, type)
                except TypeError as te:
                    print(str(te))
            except TypeError as te:
                print(str(te))
        elif len(params) == 3:
            try:
                start_day = resolve_day(params[0])
                if params[1] != 'to':
                    print("-bank-account: Invalid syntax, please use: remove <start day> to <end day>. For more information type 'help'.\n")
                    return
                end_day = resolve_day(params[2])
                remove_transactions_by_day_interval(bank_transactions, start_day, end_day)
            except TypeError as te:
                print(str(te))
        else:
            raise IndexError
    except IndexError:
        print("-bank-account: Invalid syntax, please use: remove <day> / remove <start day> to <end day> / remove <type>. For more information type 'help'.\n")


def ui_replace_transaction(bank_transactions, params):
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
            replace_transaction(bank_transactions, day, type, description, value)
        except TypeError as te:
            print(str(te))
    except IndexError:
        print("-bank-account: Invalid syntax, please use: replace <day> <type> <description> with <value>. For more information type 'help'.\n")


def ui_list_transactions(bank_transactions, params):
    try:
        if len(params) == 0:
            list_transactions(bank_transactions)
        elif len(params) == 1:
            try:
                type = resolve_type(params[0])
                list_transactions_by_type(bank_transactions, type)
            except TypeError as te:
                print(str(te))
        elif len(params) == 2:
            operands = ['<', '=', '>']
            if params[0] in operands:
                try:
                    operand = params[0]
                    value = resolve_value(params[1])
                    list_transactions_by_value(bank_transactions, operand, value)
                except TypeError as te:
                    print(str(te))
            elif params[0] == 'balance':
                try:
                    day = resolve_day(params[1])
                    calculate_balance_on_day(bank_transactions, day)
                except TypeError as te:
                    print(str(te))
            else:
                print("-bank-account: Invalid syntax, please use: list / list <type> / list [ < | = | > ] / list balance <day>. For more information type 'help'.\n")
                return
        else:
            raise IndexError
    except IndexError:
        print("-bank-account: Invalid syntax, please use: list / list <type> / list [ < | = | > ] / list balance <day>. For more information type 'help'.\n")


def ui_sum_transactions(bank_transactions, params):
    try:
        if len(params) != 1:
            raise IndexError
        try:
            day = resolve_day(params[0])
            type = resolve_type(params[1])
            description = params[2]
            if params[3] != 'with':
                print("-bank-account: Invalid syntax, please use: replace <day> <type> <description> with <value>. For more information type 'help'.\n")
                return
            value = resolve_value(params[4])
            replace_transaction(bank_transactions, day, type, description, value)
        except TypeError as te:
            print(str(te))
    except IndexError:
        print("-bank-account: Invalid syntax, please use: sum <type>. For more information type 'help'.\n")


def ui_show_commands():
    print("BANK ACCOUNT management, version 1.0.1 (python).")
    print("These commands are defined internally.  Type 'help' to see this list.\n")
    print(" add <value> <type> <description> - adds to the current day an <type> transaction of <value> RON with the <description> description.")
    print(" insert <day> <value> <type> <description> - insert to day <day> an <type> transaction of <value> RON with the <description> description.\n")
    print(" remove <day> - remove all transactions from day <day>.")
    print(" remove <start day> to <end day> - removes all transactions between day <start day> and day <end day>.")
    print(" remove <type> - remove all the <type> transactions from the current month.")
    print(" replace <day> <type> <description> with <value> - replace the amount for the <type> transaction having the <description> "
          "description from day <day> with <value> RON.\n")
    print(" list - write the entire list of transactions.")
    print(" list <type> - write all the <type> transactions.")
    print(" list [ < | = | > ] <value> - writes all transactions having an amount of money [ < | = | > ] than <value>.")
    print(" list balance <day> - computes the account’s balance on day <day>. This is the sum of all 'in' transactions, from which we "
          "subtract 'out' transactions occurring before or on day <day>.\n")
    print(" sum <type> - write the total amount from <type> transactions.")
    print(" max <type> <day> - write the maximum <type> transaction on day <day>.\n")
    print(" filter <type> - keep only <type> transactions.")
    print(" filter <type> <value> - keep only <type> transactions having an amount of money smaller than <value> RON.\n")
    print(" undo - reverses the last operation that has modified program data.\n")
