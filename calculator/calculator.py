from typing import List, Optional
from .calculation import Calculation

class Calculator:
    """A simple calculator class that stores and performs calculations."""
    
    history: List[Calculation] = []  # Stores calculation history

    @staticmethod
    def add(a: float, b: float) -> float:
        """Returns the sum of a and b."""
        return a + b

    @staticmethod
    def subtract(a: float, b: float) -> float:
        """Returns the result of subtracting b from a."""
        return a - b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        """Returns the product of a and b."""
        return a * b

    @staticmethod
    def divide(a: float, b: float) -> float:
        """Returns the result of dividing a by b. Raises ZeroDivisionError if b is 0."""
        if b == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return a / b

    @classmethod
    def add_calculation(cls, calculation: Calculation) -> None:
        """Stores a calculation in the history."""
        cls.history.append(calculation)

    @classmethod
    def get_last_calculation(cls) -> Optional[Calculation]:
        """Retrieves the last calculation from history, or None if history is empty."""
        return cls.history[-1] if cls.history else None

    @classmethod
    def clear_history(cls) -> None:
        """Clears all stored calculations."""
        cls.history.clear()
