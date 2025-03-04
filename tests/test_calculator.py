''' My Calculator Test'''

import pytest
from calculator import Calculator

def test_add():
    assert Calculator.add(5, 3) == 8

def test_subtract():
    assert Calculator.subtract(10, 4) == 6

def test_multiply():
    assert Calculator.multiply(6, 7) == 42

def test_divide():
    assert Calculator.divide(8, 2) == 4

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError, match="Division by zero is not allowed."):
        Calculator.divide(10, 0)