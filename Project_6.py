import math
import random

def plus(number,second_number):
    print("number =")
    number = float(input())
    print("second_number = ")
    second_number = float(input())
    return print(number + second_number)
def minus(number,second_number):
    print("number =")
    number = float(input())
    print("second number = ")
    secondnumber = float(input())
    return print(number - secondnumber)
def deleniye(number,second_number):
    print("number =")
    number = float(input())
    print("second number = ")
    secondnumber = float(input())
    return print(number / secondnumber)
def umnojeniye(number,second_number):
    print("number =")
    number = float(input())
    print("second number = ")
    secondnumber = float(input())
    return print(number * secondnumber)
def stepen(number,second_number):
    print("number =")
    number = float(input())
    print("second number = ")
    secondnumber = float(input())
    return print(number ** secondnumber)
def module(number):
    print("number =")
    number = float(input())
    return print(math.fabs(number))
def arccos(number):
    print("number =")
    number = float(input())
    return print(math.acos(number))
def factorial(n):
    if n == 0:
        return 1
    return n*factorial(n-1)
def rand(number,second_number):
    print("Рандомное число в диапазона от: ")
    number = int(input())
    print("До :")
    secondnumber = int(input())
    return print(random.randint(number, secondnumber))

point = True
print("/ деление \n* умножение \n+ сложение \n- разность\nm модуль\narccos - arccos \n^  возведение в степень \n! факториал \nrand рандомное число \nquit выход")

while(point):
    number=0;second_number=0;str=0;
    command = input()

    if command == "/":
        deleniye(number,second_number)

    elif command == "quit":
        point = False

    elif command == "*":
        umnojeniye(number,second_number)

    elif command == "-":
        minus(number,second_number)

    elif command == "+":
        plus(number,second_number)

    elif command == "^":
        stepen(number,second_number)

    elif command == "m":
        module(number)

    elif command == "arccos":
        arccos(number)

    elif command == "!":
        print("number =")
        number = float(input())
        print(factorial(number))

    elif command == "rand":
        rand(number,second_number)

    else:
        print("Команда отсутствует")