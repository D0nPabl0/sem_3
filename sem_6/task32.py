'''Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
(т.е. не меньше заданного минимума и не больше заданного максимума)
Ввод: [1, 3, 7, 10, 5, 8, 4, 8]
Вывод: [2, 3, 5, 7]'''

list_1 = [1, 3, 7, 10, 5, 8, 4, 8]
list_2 = []
max = 10
min = 6
# for i in range(len(lst_1)):
#     if list_1[i] >= min and list_1[i] <= max:
#         list_2.append(i)
# print(list_2)
# или
for i in range(len(list_1)):
    if min <= list_1[i] <= max:
        print(i, end=' ')