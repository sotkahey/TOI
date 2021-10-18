list_1 = []
list_2 = []


def mass_keys():
    str = []
    while (True):
        word = input()
        if word == "quit":
            break
        else:
            str.append(word)
    return str


def mass_values(str):
    str_2 = []
    for i in range(len(str)):
        word = input()
        str_2.append(word)
    return str_2


def last_lists(str_2, str):
    summ = {str[i]: str_2[i] for i in range(len(str))}
    return summ


print("Для выхода из цикла введите - quit")
list_1 = mass_keys()

multiplicity = set(list_1)  # set - множество
print("Список -", list_1)
print("Множество - ", multiplicity)
print("Количество символов в списке =", len(list_1))
print("Заполните следующий список из", len(list_1), "символов")

list_2 = mass_values(list_1)

print(list_2)
list = last_lists(list_2, list_1)
print(list)