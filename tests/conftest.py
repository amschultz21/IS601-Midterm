import pytest
from calculator.calculator import Calculator

@pytest.fixture(autouse=True)
def clear_calculator_history():
    """Fixture to ensure calculator history is cleared before each test."""
    Calculator.clear_history()
