"""
Factory Method for creating Command objects.
"""

from calculator.commands import Command
from calculator.plugins.operations import operations  # This dict includes add, subtract, etc.

class CommandFactory:
    @staticmethod
    def create_command(a: float, b: float, operation_name: str) -> Command:
        if operation_name in operations:
            operation = operations[operation_name]
            return Command(a, b, operation)
        else:
            raise ValueError(f"Operation '{operation_name}' is not supported.")
