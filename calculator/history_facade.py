"""
Facade for handling calculation history using Pandas.
Provides a simplified interface for saving, loading, clearing, and deleting records.
"""

import os
import pandas as pd

HISTORY_FILE = "calculation_history.csv"

class HistoryFacade:
    def __init__(self):
        self.history = pd.DataFrame(columns=["Operation", "A", "B", "Result"])
    
    def add_record(self, operation: str, a: float, b: float, result: float):
        new_entry = pd.DataFrame([[operation, a, b, result]], columns=self.history.columns)
        if self.history.empty:
            self.history = new_entry
        else:
            self.history = pd.concat([self.history, new_entry], ignore_index=True)
    
    def save(self):
        self.history.to_csv(HISTORY_FILE, index=False)
    
    def load(self):
        if os.path.exists(HISTORY_FILE):
            self.history = pd.read_csv(HISTORY_FILE)
    
    def clear(self):
        self.history = pd.DataFrame(columns=["Operation", "A", "B", "Result"])
        if os.path.exists(HISTORY_FILE):
            os.remove(HISTORY_FILE)
    
    def delete_last(self):
        if not self.history.empty:
            self.history = self.history.iloc[:-1]
            self.save()
    
    def get_last_record(self):
        if self.history.empty:
            return None
        return self.history.iloc[-1]
