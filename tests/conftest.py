"""
Pytest configuration file that provides fixtures for testing.
This file ensures that the Calculator history is cleared before each test.
"""

import pytest
from calculator.calculator import Calculator

@pytest.fixture(autouse=True)
def clear_calculator_history():
    """Fixture to ensure calculator history is cleared before each test."""
    Calculator.clear_history()
