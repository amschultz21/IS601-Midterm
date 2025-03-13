"""
Plugin for multiplication operation.
"""

def operation(a, b):
    """Returns the product of a and b."""
    return a * b

from calculator.plugins.multiply import operation

def test_multiply():
    assert operation(3, 4) == 12

