def Exit_Program():
    print('Завершение программы')
    exit()


def Classroom():
    cuser_input_n = input("Введите номер класса \n>>> ")
    user_input_l  = input("Введите букву класса \n>>> ").upper()
    classroom = cuser_input_n + user_input_l

    return(classroom)

def main_menu() -> int:
    print('Главное меню.')
    main_menu = ['Открыть классный журнал',
                 'Посмотреть классный журнал',
                 'Провести урок',  #Вызвать к доске #Поставить оценку 
                 'Выход'
                ]
    for i in range(len(main_menu)):
        print(f'    {i+1}. {main_menu[i]}')

    user_input = int(input('Введите комнду \n>>> '))
    
    while(user_input > len(main_menu) or user_input <= 0): # валидация
        for i in range(len(main_menu)):
            print(f'    {i+1}. {main_menu[i]}')
        user_input = int(input('Введите комнду \n>>> '))

    return user_input   


def DB_Success(db: list):
    if db:
        print('Классный журнал открыт')
        return True
    else:
        print('Классный журнал пуст либо не открыт')
        return False 

def Subject_List(db: list):
    if DB_Success(db):       
        for i in range(len(db)):
            user_id = i + 1
            print(f'\t{user_id}', end='. ')
            for v in db[i].values():
                print(f'{db[i].keys()}: {v}', end=' ')
            print()    

def Subject(db: list):
    print('Список предметов.')
    #создание списка предметов
    subject_list = []
    for i in range(len(db)):
        for k in db[i].keys():
            subject_list.append(k)

    #вывод списка предметов
    for i in range(len(subject_list)):
        print(f'    {i+1}. {subject_list[i]}')

    user_input = int(input('Выберите предмет(цифра) \n>>> '))

    while(user_input > len(subject_list) or user_input <= 0): # валидация
        for i in range(len(subject_list)):
            print(f'    {i+1}. {subject_list[i]}')
        user_input = int(input('Выберите предмет(цифра) \n>>> '))

    return user_input-1

def Call_Pupils(db: list, subject: int):

    subject = db[subject]
    list = []

    for v in subject.values():
        values = v
    for k in values.keys():
        list.append(k)
    print('Кого хотите вызвать?')
    for i in range(len(list)):
        print(f'{i+1}. {list[i]}')
    pupils_number = int(input('Введите номер ученика \n>>> '))

    pupils = list[pupils_number-1]

    return pupils

def Grade():
    grade = int(input('Каую поставите оценку?\n>>> '))

    return grade