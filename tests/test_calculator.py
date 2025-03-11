''' My Calculator Test'''

import pytest
from calculator.calculator import Calculator
from calculator.commands import Command
from calculator.operations import add, subtract, multiply, divide

def test_add():
    """Tests addition using the add function."""
    assert add(5, 3) == 8

def test_subtract():
    """Tests subtraction using the subtract function."""
    assert subtract(10, 4) == 6

def test_multiply():
    """Tests multiplication using the multiply function."""
    assert multiply(6, 7) == 42

def test_divide():
    """Tests division using the divide function."""
    assert divide(8, 2) == 4

def test_divide_by_zero():
    """Ensures that division by zero raises a ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError, match="division by zero"):
        divide(10, 0)

def test_execute_command():
    """Tests executing a command and storing it in history."""
    command = Command(5, 3, add)
    result = Calculator.execute_command(command)
    assert result == 8
    assert Calculator.get_last_command() == command

def test_get_last_calculation():
    """Tests retrieving the last calculation from history."""
    command = Command(10, 2, divide)
    Calculator.execute_command(command)
    assert Calculator.get_last_command().execute() == 5

def test_clear_history():
    """Tests clearing the calculator history."""
    command = Command(4, 2, multiply)
    Calculator.execute_command(command)
    assert len(Calculator.history) == 1
    Calculator.clear_history()
    assert len(Calculator.history) == 0
