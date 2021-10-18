def main():
    numb = int(input('Введите число'))
    numbborder = int(input('Введите пограничное число'))
    if numb < numbborder:
        print('Число меньше погрничного числа')
    if numb > numbborder:
        if numb > numbborder * 3:
            print('Число больше более чем в 3 раза чем пограничное число')
        else:
            print('Число больше пограничного числа')
    if numb == numbborder:
        print('Числа равны')
main()