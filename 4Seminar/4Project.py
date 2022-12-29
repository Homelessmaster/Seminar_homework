import time

n_max = int(input('Введите максимальное число: '))
n_min = int(input('Введите минимальное число: '))


while(n_max == n_min):
    print(n_max)
    n_max = int(input('Введите максимальное число: '))
    n_min = int(input('Введите минимальное число: '))

k = 10000000
if(n_min <= 100):
    k = 10000
elif(n_min >= 100):
    k = 10000000
elif(n_min >= 1000):
    k = 10000000000

time = time.time()

time = (time - int(time))
time = round((time * k) - time, 1)

n = int(time)

while( n > n_max or n < n_min):
    if(n > n_max):
        n2 = n + n - 100
        while(n2 <= 0):
            n2 = n2 + 100
        n = n - n2
        
    elif(n < n_min):
        n2 = n / n - 10
        n = n - n2



        

print(int(n))
