k = int(input("Введите число:\n>>>"))

fib_list = []

n = 1
n2 = 0
j = 1
k_copy = k
for i in range(k_copy):
    
    for j in range(k_copy):
        tmp = n
        n = n2 - n
        n2 = tmp
        j = j + 1
    fib_list.append(n2)
    n = 1
    n2 = 0
    j = 1
    k_copy = k_copy - 1

n = 1
n2 = 0
j = 1  
for i in range(k+1):
    fib_list.append(n2)
    tmp = n
    n = n2 + n
    n2 = tmp
    


print(fib_list)