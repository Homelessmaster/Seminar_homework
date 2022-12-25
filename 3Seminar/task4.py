#Напишите программу, которая будет преобразовывать десятичное число в двоичное.
#Пример:
#45 -> 101101
#3 -> 11
#2 -> 10

#преобразование десятичного числа в двоичное(перевернутое)
def conversion(number, list):
    
    while True:
        
        if((number%2 == 0 or number%2 == 1) and number > 3):
            list.append(number%2)
        
        if(number == 3):
            list.append(1)
            list.append(1)
            break

        elif(number == 2):
            list.append(0)
            list.append(1)
            break  

        number = number//2

    return list

#переворот двоичного числа
def list_reverse(list):

    index_count = len(list)//2

    j = 0

    for i in range(index_count):
        tmp = list[i]
        list[i] = list[j-1]
        list[j-1] = tmp
        j = j - 1

#Преобразование списка в текст
def convert_list_to_string(list):
    result_str = ''
    for i in range(len(list)):
        result_str = result_str + str(list[i])

    return result_str



while True:
    
    number = int(input("Введите число\n>>> "))
    list = []
    

    conversion(number, list)
    list_reverse(list)


    print(list)
    print(convert_list_to_string(list))

    print('')
    exit = input("Продолжить? y/n \n>>> ")
    if(exit == 'n'):
        break

        


    
    

