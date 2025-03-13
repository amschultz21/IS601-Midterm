"""
Tests for verifying that conftest.py fixtures work as expected.
"""

import pytest
from calculator.calculator import Calculator
from calculator.commands import Command
from calculator.calculation import Calculation

def test_clear_calculator_history_fixture():
    """
    Verify that the autouse fixture clears the Calculator history.
    Since the fixture runs automatically before each test, Calculator.history should be empty.
    """
    # The clear_calculator_history fixture should run automatically, so the history is empty.
    assert Calculator.history.empty

def test_get_num_records_fixture(get_num_records):
    """
    Verify that the get_num_records fixture returns an integer,
    defaulting to 10 when no command-line option is provided.
    """
    # By default, --num_records should be 10.
    assert isinstance(get_num_records, int)
    assert get_num_records == 10

def test_generate_test_calculations_fixture(generate_test_calculations):
    """
    Verify that generate_test_calculations returns a list of Calculation instances.
    """
    # Check that the fixture returns a list.
    assert isinstance(generate_test_calculations, list)
    
    # If the list is non-empty, verify that each element is a Calculation instance.
    for item in generate_test_calculations:
        # Here, depending on your implementation, Calculation might be an instance of a Command,
        # so you can adjust the check accordingly.
        # For this example, we assume it's an instance of Calculation.
        assert isinstance(item, Calculation)
