class Calculation:
    def __init__(self, a, b, operation):
        """Initialize Calculation with two numbers and an operation."""
        self.a = a
        self.b = b
        self.operation = operation

    def execute(self):
        """Executes the calculation based on the operation type."""
        if self.operation == "add":
            return self.a + self.b
        elif self.operation == "subtract":
            return self.a - self.b
        elif self.operation == "multiply":
            return self.a * self.b
        elif self.operation == "divide":
            if self.b == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            return self.a / self.b
        else:
            raise ValueError("Invalid operation")