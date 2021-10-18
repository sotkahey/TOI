def main():
    amount=0
    text = input("Введите текст")
    for i in range(0,len(text)):  # len - вычисляет длину строки
        if text[i] == 'c':
            amount = amount + 1
    print()
    print("Символ 'c' встречается",amount,"раз")
    for i in range(0,len(text)-1):
        if i == 2:
            continue
        print(text[i],end ='')  # end = '' - для вывода в строку
main()