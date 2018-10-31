from interface import *


def run_menu():
    print("Welcome John to your bank account management app!")
    print("Please use one of the available commands (type 'help' to display them).\n")
    bank_transactions = []
    generate_bank_transactions(bank_transactions)
    while True:
        user_input = input("bank-account:~ john$ ").split()
        options = {
            'add': ui_add_transaction,
            'insert': ui_insert_transaction,
            'remove': ui_remove_transactions,
            'replace': ui_replace_transaction,
            'list': ui_list_transactions,
            'sum': ui_sum_transactions,
            'max': ui_max_transaction,
            'filter': ui_filter_transactions
        }
        command = user_input[0]
        if command in options:
            options[command](bank_transactions, user_input[1:])
        elif command == 'help':
            ui_show_commands()
        elif command == 'exit':
            return
        else:
            print("Command not found! Please use one of the available commands (type 'help' to display them).\n")


run_menu()
