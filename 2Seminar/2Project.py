number = int(input("Введите число \n>>> "))

list = []
summ = 0
for i in range(1, number+1, 1):
    a = ((i + 1)/i)
    a = round(a**i, 2)

    if(a == int(a)):
        a = int(a)

    
    list.append(a)
    summ = summ + a

print(f'Для n={number} -> {list} \nСумма {summ}')