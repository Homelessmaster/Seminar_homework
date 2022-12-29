import random

def coefficient_creation(list_n):
    for i in range(3):
        list_n.append(random.randint(-100, 100))
        list_n[i] = str(list_n[i])
    return list_n


def creation_str_polynomial(polynomial_list):  
    polynomial_str = ''
    
    for i in range(len(polynomial_list)):
        polynomial_str = polynomial_str + polynomial_list[i]
    return polynomial_str


def change_list(polynomial_list, list_n):

    polynomial_list[0] = list_n[0]

    if(int(list_n[1]) < 0):
        polynomial_list[3] = ' - '
        b = list_n[1].split('-')
        polynomial_list[4] = b[1]

    elif(int(list_n[1]) >= 0):
        polynomial_list[4] = list_n[1]

    
    if(int(list_n[2]) < 0): 
        polynomial_list[6] = ' - '
        c = list_n[2].split('-')
        polynomial_list[7] = c[1]
        
    elif(int(list_n[2]) >= 0):
        polynomial_list[7] = list_n[2]

    
    


def degree(k, dictionary, polynomial):
    if(k - int(k) == 0):
        k = int(k)
        k = str(k)
        polynomial[2] = dictionary[k]

    elif(k - int(k) != 0):
        k = str(k)

        k = k.split('.')
        k.append('.')

        temp = k[1]
        k[1] = k[2]
        k[2] = temp

        for i in range(3):
            polynomial[2] = polynomial[2] + dictionary[k[i]]




polynomial_list = [ '', 'x', '',  ' + ' , '', 'x', ' + ', '', ' = ', '0']

list_n = []

dictionary = \
    {
        '1': '1a',
        '2': '2b',
        '3': '3c',
        '4': '4r',
        '5': '5w',
        '6': '6w',
        '7': '7w',
        '8': '8w',
        '9': '9w',
        '0': '0w',
        '.': '.w'
    }

k = float(input("Введите степень\n>>> "))
k = round(k, 1)

coefficient_creation(list_n)
change_list(polynomial_list, list_n)
degree(k, dictionary, polynomial_list)
creation_str_polynomial(polynomial_list)

with open('3Project.txt', 'w') as data:
    data.write(creation_str_polynomial(polynomial_list))