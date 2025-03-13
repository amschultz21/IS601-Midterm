import pytest
from calculator.plugins.operations import operations, add, subtract, multiply, divide

def test_default_operations_keys():
    """Test that the default operations are present in the operations dictionary."""
    expected_keys = {"add", "subtract", "multiply", "divide"}
    assert expected_keys.issubset(set(operations.keys()))

def test_default_add():
    """Test that the add operation returns the correct result."""
    assert add(2, 3) == 5

def test_default_subtract():
    """Test that the subtract operation returns the correct result."""
    assert subtract(5, 3) == 2

def test_default_multiply():
    """Test that the multiply operation returns the correct result."""
    assert multiply(3, 4) == 12

def test_default_divide():
    """Test that the divide operation returns the correct result."""
    assert divide(10, 2) == 5

def test_divide_by_zero():
    """Test that divide operation raises ZeroDivisionError when dividing by zero."""
    with pytest.raises(ZeroDivisionError, match="Division by zero is not allowed."):
        divide(10, 0)
