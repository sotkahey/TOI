from math_two import manipulation


run = True
print(
    "/ - деление \n* - умножение \n+ - сложение \n- - разность\nm - модуль\narccos - arccos \n^ - возведение в степень \n! - факториал \nrand - рандомное число \nquit - выход")

while (run):
    str = input()

    if str == "/":
        manipulation.deleniye(self=(''))

    elif str == "quit":
        run = False

    elif str == "*":
        manipulation.umnozheniye(self=(''))

    elif str == "-":
        manipulation.vichetaniye(self=(''))

    elif str == "+":
        manipulation.sum(self=(''))

    elif str == "^":
        manipulation.stepen(self=(''))

    elif str == "m":
        manipulation.module(self=(''))

    elif str == "arccos":
        manipulation.acos(self=(''))

    elif str == "!":
        print("numb =")
        numb = float(input())
        print(manipulation.factorial(numb))

    elif str == "rand":
        manipulation.rand(self=(''))

    else:
        print("Команда отсутствует")