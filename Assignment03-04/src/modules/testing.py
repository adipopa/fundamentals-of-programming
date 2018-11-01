"""
Module that tests if the results from running the program are the expected ones.
"""

from modules.validation import *
from modules.business import *


def test_build_transaction():
    transaction = build_transaction(24, 200, 'in', 'built')
    assert get_day(transaction) == 24
    assert get_value(transaction) == 200
    assert get_type(transaction) == 'in'
    assert get_description(transaction) == 'built'


def test_resolve_day(day, should_pass):
    try:
        resolve_day(day)
        assert should_pass
    except TypeError:
        assert not should_pass


def test_resolve_type(type, should_pass):
    try:
        resolve_type(type)
        assert should_pass
    except TypeError:
        assert not should_pass


def test_resolve_value(value, should_pass):
    try:
        resolve_value(value)
        assert should_pass
    except TypeError:
        assert not should_pass


def test_validation():
    test_resolve_day('21', True)
    test_resolve_day('0', False)
    test_resolve_day('-7', False)
    test_resolve_day('34', False)
    test_resolve_day('in', False)
    test_resolve_day(None, False)

    test_resolve_type('in', True)
    test_resolve_type('out', True)
    test_resolve_type('both', False)
    test_resolve_type('13', False)
    test_resolve_type(None, False)

    test_resolve_value('500', True)
    test_resolve_value('0', False)
    test_resolve_value('-375', False)
    test_resolve_value('out', False)
    test_resolve_value(None, False)


def test_add_transaction(bank_transactions, operations_queue):
    add_transaction(bank_transactions, operations_queue, 400, 'in', 'first')
    transaction = bank_transactions[10]
    assert get_day(transaction) == get_current_day()
    assert get_value(transaction) == 400
    assert get_type(transaction) == 'in'
    assert get_description(transaction) == 'first'


def test_insert_transaction(bank_transactions, operations_queue):
    insert_transaction(bank_transactions, operations_queue, 14, 130, 'out', 'second')
    transaction = bank_transactions[11]
    assert get_day(transaction) == 14
    assert get_value(transaction) == 130
    assert get_type(transaction) == 'out'
    assert get_description(transaction) == 'second'

    insert_transaction(bank_transactions, operations_queue, 17, 25, 'out', 'third')
    transaction = bank_transactions[12]
    assert get_day(transaction) == 17
    assert get_value(transaction) == 25
    assert get_type(transaction) == 'out'
    assert get_description(transaction) == 'third'


def test_remove_transactions_by_day(bank_transactions, operations_queue):
    remove_transactions_by_day(bank_transactions, operations_queue, 8)
    assert filter_out_transactions_by_day(bank_transactions, 8) == bank_transactions


def test_remove_transactions_by_day_interval(bank_transactions, operations_queue):
    remove_transactions_by_day_interval(bank_transactions, operations_queue, 16, 19)
    assert filter_out_transactions_by_day_interval(bank_transactions, 16, 19) == bank_transactions


def test_remove_transactions_by_type(bank_transactions, operations_queue):
    remove_transactions_by_type(bank_transactions, operations_queue, 'out')
    assert filter_out_transactions_by_type(bank_transactions, 'out') == bank_transactions


def test_replace_transaction(bank_transactions, operations_queue):
    replace_transaction(bank_transactions, operations_queue, 23, 'in', 'credit', 3500)
    transaction_index = find_transaction(bank_transactions, 23, 'in', 'credit')
    assert get_value(bank_transactions[transaction_index]) == 3500


def test_calculate_balance_on_day(bank_transactions):
    balance = calculate_balance_on_day(bank_transactions, 17)
    assert balance == 3400


def test_maximum_transaction(bank_transactions):
    max_transaction = maximum_transaction(bank_transactions, 'in', 14)
    assert max_transaction == bank_transactions[1]


def test_filter_transactions(bank_transactions, operations_queue):
    filter_transactions(bank_transactions, operations_queue, 'in', None)
    assert filter_transactions_by_type(bank_transactions, 'in') == bank_transactions

    filter_transactions(bank_transactions, operations_queue, 'in', 600)
    transactions_by_type = filter_transactions_by_type(bank_transactions, 'in')
    assert filter_transactions_by_value(transactions_by_type, '<', 600) == bank_transactions


def test_undo_last_operation(bank_transactions, operations_queue):
    for undo_index in range(7, -1, -1):
        last_operation = operations_queue[undo_index]
        undo_last_operation(bank_transactions, operations_queue)
        assert bank_transactions == last_operation
    assert len(operations_queue) == 0


def run_tests():
    bank_transactions = []
    operations_queue = []

    generate_bank_transactions(bank_transactions)

    test_build_transaction()
    test_validation()
    test_add_transaction(bank_transactions, operations_queue)
    test_insert_transaction(bank_transactions, operations_queue)
    test_remove_transactions_by_day(bank_transactions, operations_queue)
    test_remove_transactions_by_day_interval(bank_transactions, operations_queue)
    test_remove_transactions_by_type(bank_transactions, operations_queue)
    test_replace_transaction(bank_transactions, operations_queue)
    test_calculate_balance_on_day(bank_transactions)
    test_maximum_transaction(bank_transactions)
    test_filter_transactions(bank_transactions, operations_queue)
    test_undo_last_operation(bank_transactions, operations_queue)
