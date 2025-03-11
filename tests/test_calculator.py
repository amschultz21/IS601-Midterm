''' My Calculator Test'''

from calculator.calculator import Calculator
from calculator.commands import Command
from calculator.plugins.operations import add, divide

def test_execute_command():
    """Tests executing a command and storing it in history."""
    command = Command(5, 3, add)
    result = Calculator.execute_command(command)
    assert result == 8

    last_command = Calculator.get_last_command()
    assert last_command is not None
    assert last_command.a == 5
    assert last_command.b == 3
    assert last_command.operation.__name__ == add.__name__  # ✅ Ensure function name matches

def test_get_last_calculation():
    """Tests retrieving the last calculation from history."""
    command = Command(10, 2, divide)
    Calculator.execute_command(command)
    last_command = Calculator.get_last_command()

    assert last_command is not None
    assert last_command.a == 10
    assert last_command.b == 2
    assert last_command.operation.__name__ == divide.__name__  # ✅ Ensure function name matches
    assert last_command.execute() == 5
