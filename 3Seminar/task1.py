#Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
#стоящих на позиции с нечетным индексом.
#Пример:
#[2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

import random

summ = 0
list = []

for i in range(5):
    list.append(random.randint(-5, 5))

for i in range(len(list)):
    if(i%2 != 0):
        summ = summ + list[i]

print(list)
print(f'Ответ: {summ}')

