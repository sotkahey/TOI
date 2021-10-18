list_1 = [] # список 1
list_2 = [] # список 2
print("Для выхода из цикла введите - quit")
while(True):
    word = input()
    if word == "quit":
        break
    else:
        list_1.append(word) # append - вставляет в конце списка значение аргумента
multiplicity = set(list_1) # делаем из списка множество
print("Список слов -",list_1)
print("Множество - ",multiplicity)
print("Количество слов в списке =",len(list_1))
print("Заполните следующий список из",len(list_1),"слов")
for i in range(len(list_1)):
    word = input()
    list_2.append(word)
print(list_2)
dictionary = {list_1[i]:list_2[i] for i in range(len(list_1))} # формируем словарь
print(dictionary)