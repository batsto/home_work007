import check
import logger


def view(data):
    print(data)


def get_value(x):
    x = input()
    if check.examination_value(x) == True:
        return x
    else:
        return 'Вы ввели не число'

def get_action(x):
    x = input()
    if check.examination_action(x) == True:
        return x
    else: 
        return 'Вы ввели не математическое действие'

def menu():
    print("Это простой калькулятор на Python")
    print("Выберите действие которое хотите сделать:\n"
              "Сложить: +\n"
              "Вычесть: -\n"
              "Умножить: *\n"
              "Поделить: /\n"
              "Выйти: q\n")