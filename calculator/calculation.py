class Calculation:
    """Represents a mathematical calculation with two numbers and an operation type."""

    def __init__(self, a, b, operation):
        """
        Initializes a Calculation object.

        :param a: First operand
        :param b: Second operand
        :param operation: Type of operation ('add', 'subtract', 'multiply', 'divide')
        """
        self.a = a
        self.b = b
        self.operation = operation

    def execute(self):
        """Performs the calculation based on the operation type."""
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
