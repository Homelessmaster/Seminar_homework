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

def name(user):
    user = str(input(f"{user}, введите свой ник \n>>> "))
    return user


CandyBank = 10
CandyUser1 = 0
CandyUser2 = 0
NameUser1 = 'user1'
NameUser2 = 'user2'


NameUser1 = name(NameUser1)
NameUser2 = name(NameUser2)

while(CandyBank > 0):

    CandyUser1 = check(CandyUser1, NameUser1, CandyBank)

    if(CandyBank - CandyUser1 == 0):
        print(f"Попедил {NameUser1}!")

    CandyBank = CandyBank - CandyUser1
    print(f"Осталось конфет: {CandyBank}")


    CandyUser2 = check(CandyUser2, NameUser2, CandyBank)

    if(CandyBank - CandyUser2 == 0):
        print(f"Попедил {NameUser2}!")

    CandyBank = CandyBank - CandyUser2
    print(f"Осталось конфет: {CandyBank}")