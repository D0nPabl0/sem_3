'''Задача 30: Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество
элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: a
n = a1 + (n-1) * d.
Каждое число вводится с новой строки.
Ввод: 1 2 5
Вывод: 1 3 5 7 9'''

a1 = 1
d = 2
n = 5
for i in range(n):
    print(a1 + i * d, end=' ')