"""
This module defines the Calculator class, which manages arithmetic operations using the Command Pattern.
"""

from typing import List, Optional
from .calculation import Calculation
from .commands import Command
from .operations import add, subtract, multiply, divide

class Calculator:
    """A calculator that stores executed commands."""
    
    history: List[Command] = []  # Stores command history

    @staticmethod
    def execute_command(command: Command) -> float:
        """Executes a command and stores it in history."""
        result = command.execute()
        Calculator.history.append(command)
        return result

    @classmethod
    def get_last_command(cls) -> Optional[Command]:
        """Retrieves the last executed command."""
        return cls.history[-1] if cls.history else None

    @classmethod
    def clear_history(cls) -> None:
        """Clears all stored commands."""
        cls.history.clear()
