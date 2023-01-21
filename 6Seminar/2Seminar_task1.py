#2 семинар 1 задание(cтарое)
number = float(input("Введите число \n>>> "))
number = str(number)
number = number.replace('.', '0')

result = 0

for i in range(0, len(number), 1):
    result = result + int(number[i]) 

print(result)



#новое

result2 = 0
sum = lambda x, y: int(x) + int(y)

for i in range(0, len(number) - 1, 2):
    result2 += sum(number[i], number[i+1])

print(result2)



