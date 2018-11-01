"""
The main module that runs the program.
"""

from modules.testing import *
from modules.user_interface import *


def run_app():
    bank_transactions = []
    operations_queue = []

    generate_bank_transactions(bank_transactions)

    run_user_interface(bank_transactions, operations_queue)


run_tests()
run_app()
