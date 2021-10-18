import math
import random

class manipulation():
    def factorial(n):
        if n == 0:
            return 1
        return n * math.factorial(n - 1)

    def sum(self):
        print("number =")
        number = float(input())
        print("number_second = ")
        number_second = float(input())
        print(number + number_second)

    def deleniye(self):
        print("number =")
        number = float(input())
        print("number_second = ")
        number_second = float(input())
        print(number / number_second)

    def umnozheniye(self):
        print("number =")
        number = float(input())
        print("number_second = ")
        number_second = float(input())
        print(number * number_second)

    def vichetaniye(self):
        print("number =")
        number = float(input())
        print("number_second = ")
        number_second = float(input())
        print(number - number_second)

    def stepen(self):
        print("number =")
        number = float(input())
        print("number_second = ")
        number_second = float(input())
        print(number ** number_second)

    def module(self):
        print("number =")
        number = float(input())
        print(math.fabs(number))

    def acos(self):
        print("number =")
        number = float(input())
        print(math.acos(number))

    def rand(self):
        print("Рандомное число в диапазона от = ")
        number = int(input())
        print("До =")
        number_second = int(input())
        return print(random.randint(number, number_second))