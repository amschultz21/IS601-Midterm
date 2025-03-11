''' My Calculator Test'''

import pytest
from calculator.calculation import Calculation
from calculator.calculator import Calculator
from calculator.operations import add, subtract, multiply, divide

def test_imports():
    """Tests that all imports from calculator/__init__.py work correctly."""
    assert callable(add)
    assert callable(subtract)
    assert callable(multiply)
    assert callable(divide)
    assert isinstance(Calculator, type)  # Ensure Calculator is a class
    assert isinstance(Calculation, type)  # Ensure Calculation is a class

def test_add():
    """Tests addition in the Calculator."""
    assert Calculator.add(5, 3) == 8

def test_subtract():
    """Tests subtraction in the Calculator."""
    assert Calculator.subtract(10, 4) == 6

def test_multiply():
    """Tests multiplication in the Calculator."""
    assert Calculator.multiply(6, 7) == 42

def test_divide():
    """Tests division in the Calculator."""
    assert Calculator.divide(8, 2) == 4

def test_divide_by_zero():
    """Ensures that division by zero raises a ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError, match="Division by zero is not allowed."):
        Calculator.divide(10, 0)

def test_add_calculation():
    """Tests storing a calculation in history."""
    calculation = Calculation(5, 3, Calculator.add)
    Calculator.add_calculation(calculation)
    assert Calculator.get_last_calculation() == calculation

def test_get_last_calculation():
    """Tests retrieving the last calculation from history."""
    calculation = Calculation(10, 2, Calculator.divide)
    Calculator.add_calculation(calculation)
    assert Calculator.get_last_calculation().execute() == 5

def test_clear_history():
    """Tests clearing the calculator history."""
    calculation = Calculation(4, 2, Calculator.multiply)
    Calculator.add_calculation(calculation)
    assert len(Calculator.history) == 1
    Calculator.clear_history()
    assert len(Calculator.history) == 0

def test_operations():
    """Tests the operations module directly."""
    assert add(5, 3) == 8
    assert subtract(10, 4) == 6
    assert multiply(6, 7) == 42
    assert divide(8, 2) == 4

def test_operations_divide_by_zero():
    """Ensures the divide function raises ZeroDivisionError when dividing by zero."""
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
