"""
This module implements the Command Pattern for calculator operations.
"""

from typing import Callable

class Command:
    """Base class for calculator commands."""
    def __init__(self, a: float, b: float, operation: Callable[[float, float], float]):
        """
        Initializes a command with operands and an operation.
        
        :param a: First operand
        :param b: Second operand
        :param operation: Function that performs the calculation
        """
        self.a = a
        self.b = b
        self.operation = operation

    def execute(self) -> float:
        """Executes the stored operation."""
        return self.operation(self.a, self.b)
