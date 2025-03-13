import pytest
from calculator.plugins.subtract import operation

def test_subtract_positive_numbers():
    """Test subtraction with positive numbers."""
    result = operation(10, 5)
    assert result == 5

def test_subtract_negative_result():
    """Test subtraction that results in a negative number."""
    result = operation(5, 10)
    assert result == -5

def test_subtract_with_zero():
    """Test subtraction when one of the operands is zero."""
    result1 = operation(0, 5)
    result2 = operation(5, 0)
    assert result1 == -5
    assert result2 == 5

def test_subtract_floats():
    """Test subtraction with floating point numbers."""
    result = operation(10.5, 2.5)
    assert result == 8.0
