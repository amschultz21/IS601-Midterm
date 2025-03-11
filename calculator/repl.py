"""
This module implements a REPL (Read-Eval-Print Loop) for the Calculator.
"""

from calculator.calculator import Calculator
from calculator.commands import Command
from calculator.operations import add, subtract, multiply, divide

def repl():
    """Runs an interactive REPL for the calculator."""
    print("Welcome to the Interactive Calculator!")
    print("Available commands: add, subtract, multiply, divide")
    print("Type 'exit' to quit.\n")

    operations = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide
    }

    while True:
        user_input = input("Enter command (add, subtract, multiply, divide) or 'exit': ").strip().lower()

        if user_input == "exit":
            print("Goodbye!")
            break

        if user_input not in operations:
            print("Invalid command. Try again.")
            continue

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            command = Command(a, b, operations[user_input])  # Create command object
            result = Calculator.execute_command(command)
            print(f"Result: {result}\n")
        except ValueError:
            print("Invalid input. Please enter numeric values.")
        except ZeroDivisionError:
            print("Error: Division by zero is not allowed.")

if __name__ == "__main__":
    repl()  # ✅ Ensure the REPL starts when running the module
