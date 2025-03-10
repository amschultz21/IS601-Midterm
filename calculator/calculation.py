"""
This module defines the Calculation class that executes arithmetic operations.
"""

from typing import Callable

class Calculation:
    """Represents a mathematical calculation with two numbers and an operation function."""

    def __init__(self, a: float, b: float, operation: Callable[[float, float], float]):
        """
        Initializes a Calculation instance.

        :param a: First operand
        :param b: Second operand
        :param operation: Function that performs the calculation
        """
        self.a = a
        self.b = b
        self.operation = operation

    def execute(self) -> float:
        """Executes the stored operation function."""
        return self.operation(self.a, self.b)  
