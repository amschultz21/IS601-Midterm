import pytest
from calculator.plugins.multiply import operation

def test_multiply_positive_numbers():
    """Test multiplication with two positive numbers."""
    assert operation(3, 4) == 12

def test_multiply_negative_numbers():
    """Test multiplication with a negative number."""
    assert operation(-3, 4) == -12

def test_multiply_by_zero():
    """Test multiplication with zero."""
    assert operation(0, 5) == 0
    assert operation(5, 0) == 0

def test_multiply_floats():
    """Test multiplication with floating point numbers."""
    assert operation(2.5, 4) == 10.0
