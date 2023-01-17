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


def checkBot(quantity, bank, userCandy, cheat):
    
    if(bank > cheat):
        quantity = bank - cheat
        return quantity
    
    quantity = 29 - userCandy 

    if(bank - quantity < 0):
        quantity = bank

    return quantity


def name(user):
    user = str(input(f"{user}, введите свой ник \n>>> "))
    return user


CandyBank = 500
CandyUser1 = 0
CandyBot = 0
NameUser1 = 'user1'
NameBot = 'Alex'
Botcheat = CandyBank - CandyBank % 29  





NameUser1 = name(NameUser1)

print(f"Имя бота {NameBot}")
print(f"Банк конфет {CandyBank}")
print("Вы можете взять не менее 1 конфеты и не более 28")
print("Игра начинается!")



while True:
    while(CandyBank > 0):

        CandyBot = checkBot(CandyBot, CandyBank, CandyUser1, Botcheat)

        if(CandyBank - CandyBot == 0):
            print(f"Победил {NameBot}!")
            break

        CandyBank = CandyBank - CandyBot
        print(f"{NameBot} сделал ход.\nОсталось конфет: {CandyBank}")


        CandyUser1 = check(CandyUser1, NameUser1, CandyBank)

        if(CandyBank - CandyUser1 == 0):
            print(f"Победил {NameUser1}!")
            break

        CandyBank = CandyBank - CandyUser1
        print(f"Осталось конфет: {CandyBank}")
    

