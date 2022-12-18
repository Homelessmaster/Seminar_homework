number = float(input("Введите число \n>>> "))

number = str(number)

number = number.replace('.', '0')

result = 0

for i in range(0, len(number), 1):
    result = result + int(number[i]) 

print(result)

