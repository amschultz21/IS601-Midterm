"""
Calculator module that manages arithmetic operations and calculation history using Pandas.
"""

import pandas as pd
import os
from calculator.commands import Command

HISTORY_FILE = "calculation_history.csv"

class Calculator:
    """A calculator that stores executed commands using Pandas."""
    
    history = pd.DataFrame(columns=["Operation", "A", "B", "Result"])

    @staticmethod
    def execute_command(command: Command) -> float:
        """Executes a command and stores it in history."""
        result = command.execute()
        Calculator.add_to_history(command.operation.__name__, command.a, command.b, result)
        return result

    @classmethod
    def add_to_history(cls, operation: str, a: float, b: float, result: float):
        """Adds a calculation to the Pandas DataFrame."""
        new_entry = pd.DataFrame([[operation, a, b, result]], columns=cls.history.columns)
        cls.history = pd.concat([cls.history, new_entry], ignore_index=True)

    @classmethod
    def save_history(cls):
        """Saves the history to a CSV file."""
        cls.history.to_csv(HISTORY_FILE, index=False)

    @classmethod
    def load_history(cls):
        """Loads the calculation history from a CSV file if it exists."""
        if os.path.exists(HISTORY_FILE):
            cls.history = pd.read_csv(HISTORY_FILE)

    @classmethod
    def clear_history(cls):
        """Clears all history records."""
        cls.history = pd.DataFrame(columns=["Operation", "A", "B", "Result"])
        if os.path.exists(HISTORY_FILE):
            os.remove(HISTORY_FILE)

    @classmethod
    def delete_last_record(cls):
        """Deletes the last calculation from history."""
        if not cls.history.empty:
            cls.history = cls.history.iloc[:-1]
            cls.save_history()
