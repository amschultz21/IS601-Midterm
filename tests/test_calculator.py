''' My Calculator Test'''

import pytest
from calculator import Calculator

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
