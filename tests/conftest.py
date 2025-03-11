"""
Pytest configuration file that provides fixtures for testing.
This file ensures that the Calculator history is cleared before each test
and allows generating a specified number of test records.
"""

import random
import pytest
from calculator.calculator import Calculator
from calculator.calculation import Calculation

@pytest.fixture(autouse=True)
def clear_calculator_history():
    """Fixture to ensure calculator history is cleared before each test."""
    Calculator.clear_history()

def pytest_addoption(parser):
    """
    Adds a custom command-line option to pytest: --num_records=N
    Allows users to specify the number of test records to generate.
    """
    parser.addoption(
        "--num_records",
        action="store",
        default=10,
        type=int,
        help="Number of records to generate"
    )

@pytest.fixture(scope="session")
def get_num_records(request):
    """
    Returns the number of records specified by the --num_records argument.
    Defaults to 10 if not specified.
    """
    return request.config.getoption("--num_records")

@pytest.fixture(scope="function")
def generate_test_calculations(num_records_value):
    """
    Generates a list of Calculation instances based on the --num_records argument.
    """
    operations = [
        Calculator.add,
        Calculator.subtract,
        Calculator.multiply,
        Calculator.divide
    ]

    test_data = []

    for _ in range(num_records_value):
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        operation_func = random.choice(operations)

        if operation_func is Calculator.divide and b == 0:
            b = 1  # Avoid division by zero

        test_data.append(Calculation(a, b, operation_func))

    return test_data
