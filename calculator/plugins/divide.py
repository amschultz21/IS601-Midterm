"""
Plugin for division operation.
"""

def operation(a, b):
    """Returns the result of dividing a by b. Raises ZeroDivisionError if b is 0."""
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a / b
