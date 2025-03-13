"""
Plugin for subtraction operation.
"""

def operation(a, b):
    """Returns the result of subtracting b from a."""
    return a - b

from calculator.plugins.subtract import operation

def test_subtract():
    assert operation(10, 4) == 6
