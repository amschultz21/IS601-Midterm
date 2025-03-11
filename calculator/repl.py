"""
This module implements a REPL (Read-Eval-Print Loop) for the Calculator with Pandas-based history management.
"""

import os
import importlib
import pkgutil
import multiprocessing
import logging
import pandas as pd
from dotenv import load_dotenv
from calculator.calculator import Calculator
from calculator.commands import Command

load_dotenv()
environment = os.getenv("ENVIRONMENT", "development")

logging.basicConfig(
    filename="calculator.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info(f"🛠 Running in {environment} mode")

def load_plugins():
    """Dynamically loads available plugins from the `calculator.plugins` package."""
    plugins = {}
    package = "calculator.plugins"

    for _, module_name, _ in pkgutil.iter_modules([package.replace(".", "/")]):
        module = importlib.import_module(f"{package}.{module_name}")
        if hasattr(module, "operation"):
            plugins[module_name] = module.operation

    logging.info(f"Loaded plugins: {list(plugins.keys())}")
    return plugins

operations = load_plugins()
Calculator.load_history()

def display_menu():
    """Displays available commands."""
    print("\n📌 Available Commands:")
    for command in operations.keys():
        print(f" - {command}")
    print(" - history (View calculation history)")
    print(" - save (Save history to file)")
    print(" - clear (Clear all history)")
    print(" - delete_last (Delete the last calculation)")
    print(" - menu (Show this menu)")
    print(" - exit (Quit the calculator)\n")

def execute_command_multiprocess(a, b, operation_func):
    """Executes a command in a separate process."""
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
            Calculator.save_history()
            logging.info("User exited the calculator.")
            print("👋 Goodbye!")
            break

        if user_input == "menu":
            display_menu()
            continue

        if user_input == "history":
            print("\n📜 Calculation History:")
            if Calculator.history.empty:
                print("No calculations found.")
            else:
                print(Calculator.history)
            continue

        if user_input == "save":
            Calculator.save_history()
            print("✅ History saved.")
            continue

        if user_input == "clear":
            Calculator.clear_history()
            print("✅ History cleared.")
            continue

        if user_input == "delete_last":
            Calculator.delete_last_record()
            print("✅ Last calculation deleted.")
            continue

        if user_input not in operations:
            logging.warning(f"Invalid command attempted: {user_input}")
            print("⚠️ Invalid command. Type 'menu' to see available commands.")
            continue

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            command = Command(a, b, operations[user_input])

            result = execute_command_multiprocess(a, b, operations[user_input])
            Calculator.execute_command(command)
            print(f"✅ Result: {result}\n")

        except ValueError:
            logging.error("Invalid input: Non-numeric value entered")
            print("❌ Invalid input. Please enter numeric values.")
        except ZeroDivisionError:
            logging.error("Attempted division by zero")
            print("❌ Error: Division by zero is not allowed.")

if __name__ == "__main__":
    repl()
