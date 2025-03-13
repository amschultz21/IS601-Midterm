import pytest
from calculator.plugins.divide import operation

def test_divide_normal():
    """Test division with a valid divisor."""
    result = operation(10, 2)
    assert result == 5

def test_divide_by_zero():
    """Test division by zero raises ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError, match="Division by zero is not allowed."):
        operation(10, 0)
