from .calculation import Calculation

class Calculator:
    @staticmethod
    def add(a, b):
        return Calculation(a, b, "add").execute()

    @staticmethod
    def subtract(a, b):
        return Calculation(a, b, "subtract").execute()

    @staticmethod
    def multiply(a, b):
        return Calculation(a, b, "multiply").execute()

    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return Calculation(a, b, "divide").execute()