import pytest
from calculator.calculation import Calculation

def test_calculation_operations():
    assert Calculation(4, 2, "add").execute() == 6
    assert Calculation(4, 2, "subtract").execute() == 2
    assert Calculation(4, 2, "multiply").execute() == 8
    assert Calculation(4, 2, "divide").execute() == 2

def test_calculation_divide_by_zero():
    with pytest.raises(ZeroDivisionError, match="Division by zero is not allowed."):
        Calculation(10, 0, "divide").execute()