from calculator.calculation import Calculation

def test_calculation_operations():
    calc_add = Calculation(4, 2, "add")
    assert calc_add.add() == 6

    calc_subtract = Calculation(4, 2, "subtract")
    assert calc_subtract.subtract() == 2

    calc_multiply = Calculation(4, 2, "multiply")
    assert calc_multiply.multiply() == 8

    calc_divide = Calculation(4, 2, "divide")
    assert calc_divide.divide() == 2

def test_calculation_divide_by_zero():
    calc = Calculation(10, 0, "divide")
    assert calc.divide() is None
