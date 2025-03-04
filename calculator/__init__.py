from .calculation import Calculation
from .operations import add, subtract, multiply, divide

class Calculator:
    @staticmethod
    def add(a, b):
        return Calculation(a, b).add()

    @staticmethod
    def subtract(a, b):
        return Calculation(a, b).subtract()

    @staticmethod
    def multiply(a, b):
        return Calculation(a, b).multiply()

    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return Calculation(a, b).divide()