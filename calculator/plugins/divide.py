"""
Plugin for division operation.
"""

def operation(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a / b
