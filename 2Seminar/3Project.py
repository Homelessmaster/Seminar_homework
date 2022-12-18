import random

list = []

for i in range(random.randint(5, 10)):
    number = random.randint(-100, 100)
    list.append(number)

print(list)

for i in range(10):
    j = random.randint(0, len(list)-1)
    j1 = random.randint(0, len(list)-1)
    temp = list[j]
    list[j] = list[j1]
    list[j1] = temp

print(list)
