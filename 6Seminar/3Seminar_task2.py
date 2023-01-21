#Напишите программу, которая найдёт произведение пар чисел списка. 
#Парой считаем первый и последний элемент, второй и предпоследний и т.д.
#Пример:
#[2, 3, 4, 5, 6] => [12, 15, 16];
#[2, 3, 5, 6] => [12, 15]

import random

list = []
list_result = []

for i in range(5):
    list.append(random.randint(-10, 10))

index_count = len(list)//2

if(len(list) % 2 != 0):
    index_count = index_count + 1

j = 0
for i in range(index_count):
    list_result.append(list[i] * list[j-1])
    j = j - 1

print(list)
print(list_result)




#новое

data = [random.randint(-10, 10) for item in range(5)]

index_count = len(data)//2

if(len(data) % 2 != 0):
    index_count = index_count + 1

print(data)
print([data[i] * data[-i - 1] for i in range(index_count)])