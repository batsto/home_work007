
import logger
import ui
import number


def start_calc():
    ui.menu()
    action = ui.get_action()
    x = ui.get_value()
    y = ui.get_value()
    if action == '+':
        return number.addition(x, y)
    elif action == '-':
        return number.subtraction(x, y)
    elif action == '*':
        return number.multiplication(x, y)
    elif action == '/':
        return number.division(x, y)

