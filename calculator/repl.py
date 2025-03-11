"""
This module implements a REPL (Read-Eval-Print Loop) for the Calculator with dynamic command loading and multiprocessing.
"""

import os
import importlib
import pkgutil
import multiprocessing
from dotenv import load_dotenv
from calculator.calculator import Calculator
from calculator.commands import Command

load_dotenv()
environment = os.getenv("ENVIRONMENT", "development")

print(f"🛠 Running in {environment} mode")

def load_plugins():
    """Dynamically loads available plugins from the `calculator.plugins` package."""
    plugins = {}
    package = "calculator.plugins"

    for _, module_name, _ in pkgutil.iter_modules([package.replace(".", "/")]):
        module = importlib.import_module(f"{package}.{module_name}")
        if hasattr(module, "operation"):
            plugins[module_name] = module.operation

    return plugins

operations = load_plugins()

def display_menu():
    """Displays the available commands."""
    print("\n📌 Available Commands:")
    for command in operations.keys():
        print(f" - {command}")
    print(" - menu (Show this menu)")
    print(" - exit (Quit the calculator)\n")

def execute_command_multiprocess(a, b, operation_func):
    """Executes a command in a separate process for parallelism."""
    with multiprocessing.Pool(processes=1) as pool:
        result = pool.apply(operation_func, (a, b))
    return result

def repl():
    """Runs an interactive REPL for the calculator."""
    print("🎉 Welcome to the Interactive Calculator!")
    display_menu()

    while True:
        user_input = input("\nEnter a command (or type 'menu' to see available commands): ").strip().lower()

        if user_input == "exit":
            print("👋 Goodbye!")
            break

        if user_input == "menu":
            display_menu()
            continue

        if user_input not in operations:
            print("⚠️ Invalid command. Type 'menu' to see available commands.")
            continue

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            command = Command(a, b, operations[user_input])

            result = execute_command_multiprocess(a, b, operations[user_input])
            Calculator.history.append(command)
            print(f"✅ Result: {result}\n")

        except ValueError:
            print("❌ Invalid input. Please enter numeric values.")
        except ZeroDivisionError:
            print("❌ Error: Division by zero is not allowed.")

if __name__ == "__main__":
    repl()
