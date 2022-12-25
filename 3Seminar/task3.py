#Задайте список из вещественных чисел. Напишите программу, 
#которая найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
#Пример:
#[1.1, 1.2, 3.1, 5, 10.01] => 0.19

import random


#создание списка и его заполнение
list = []

for i in range(5):
    list.append(round(random.uniform(0, 10), 2))     

for i in range(len(list)):
    if(list[i] == int(list[i])):
        list[i] = int(list[i])

print(list)


#поиск максимального и минимального значения
for i in range(len(list)):
    list[i] = round(list[i]%1, 2)

max = list[0]
min = list[0]

i = 1
while(min == 0):     
    min = list[i]       
    i = i + 1

for i in list:      
    if(i>max):
        max = i
    if(i<min and i != 0):
        min = i

print(max, min)

#вывод
print(round(max - min, 2))


