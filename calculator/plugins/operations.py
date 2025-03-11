"""
Dynamically loads operation functions from plugin files.
"""

import importlib
import pkgutil

# Default mathematical operations
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")
    return a / b

# Store default operations with their correct names.
operations = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide
}

# Dynamically discover and load available plugins
package = "calculator.plugins"

for _, module_name, _ in pkgutil.iter_modules([package.replace(".", "/")]):
    if module_name not in ["operations"]:  # Avoid recursive import
        module = importlib.import_module(f"{package}.{module_name}")
        if hasattr(module, "operation"):
            op_func = module.operation
            # If the module name is one of our standard operations,
            # override the function's __name__ with the module name.
            if module_name in operations:
                op_func.__name__ = module_name
            operations[module_name] = op_func

# Expose add, subtract, multiply, and divide directly.
add = operations["add"]
subtract = operations["subtract"]
multiply = operations["multiply"]
divide = operations["divide"]
