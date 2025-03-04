"""
Test cases for the Calculation class.
"""

import pytest
from calculator.calculation import Calculation

def test_calculation_operations():
    """
    Tests different arithmetic operations using the Calculation class.
    """
    assert Calculation(4, 2, "add").execute() == 6
    assert Calculation(4, 2, "subtract").execute() == 2
    assert Calculation(4, 2, "multiply").execute() == 8
    assert Calculation(4, 2, "divide").execute() == 2

def test_calculation_divide_by_zero():
    """
    Ensures that division by zero raises a ZeroDivisionError.
    """
    with pytest.raises(ZeroDivisionError, match="Division by zero is not allowed."):
        Calculation(10, 0, "divide").execute()
