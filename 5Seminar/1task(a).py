import random

def check(quantity, name, bank):

    quantity = int(input(f"{name}, введите количество конфет, которую забираете \n>>> "))

    while True:
        if(quantity < 1 or quantity > 28):
            print("Так нельзя) Введите дозволеннное количество конфет (не меньше 1, не больше 28")
            quantity = int(input(f"{name}, введите количество конфет, которую забираете \n>>> "))  

        if(bank - quantity < 0):
            print("Так нельзя)")
            quantity = int(input(f"{name}, введите количество конфет, которую забираете \n>>> ")) 

        else:
            break     
    return quantity


def checkBot(quantity, bank):

    quantity = random.randint(1, 29)

    while True:
        if(bank - quantity < 0):
            quantity = random.randint(1, bank)
        else:
            break     
    return quantity


def name(user):
    user = str(input(f"{user}, введите свой ник \n>>> "))
    return user


CandyBank = 500
CandyUser1 = 0
CandyUser2 = 0
NameUser1 = 'user1'
NameBot = 'Alex'



NameUser1 = name(NameUser1)

print(f"Имя бота {NameBot}")
print(f"Банк конфет {CandyBank}")
print("Вы можете взять не менее 1 конфеты и не более 28")
print("Игра начинается!")

while(CandyBank > 0):

    CandyUser1 = check(CandyUser1, NameUser1, CandyBank)

    if(CandyBank - CandyUser1 == 0):
        print(f"Попедил {NameUser1}!")
        break

    CandyBank = CandyBank - CandyUser1
    print(f"Осталось конфет: {CandyBank}")


    CandyUser2 = checkBot(CandyUser2, CandyBank)

    if(CandyBank - CandyUser2 == 0):
        print(f"Попедил {NameBot}!")
        break

    CandyBank = CandyBank - CandyUser2
    print(f"{NameBot} сделал ход.\nОсталось конфет: {CandyBank}")