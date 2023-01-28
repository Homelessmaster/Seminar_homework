def exit_program():
    print('Завершение программы')
    exit()




def delete_contact(db: list):
    delet_id = int(input('Введите id контакта которую хотите удалить \n>>> '))
    db.pop(delet_id-1)




def db_success(db: list):
    if db:
        print('Телефонная книга открыта')
        return True
    else:
        print('Телефонная книга пуста либо не открыта')
        return False 




def show_all(db: list):
    if db_success(db):       
        for i in range(len(db)):
            user_id = i + 1
            print(f'\t{user_id}', end='. ')
            for v in db[i].values():
                print(f'{v}', end=' ')
            print()




def create_contact():
    print('Создание нового контакта.')
    new_contact = dict()

    new_contact['lastname'] = input('   Введите фамилию \n>>> ')
    new_contact['firstname'] = input('   Введите имя \n>>> ')
    new_contact['phone'] = input('   Введите телефон \n>>> ')
    new_contact['comment'] = input('   Введите комментарий \n>>> ')
    return new_contact




def main_menu() -> int:
    print('Главное меню.')
    main_menu = ['Показать все контакты',
                 'Открыть файл',
                 'Сохранить файл',
                 'Создать контакт',
                 'Изменить контакт',
                 'Удалить контакт',
                 'Выход'
                ]
    for i in range(len(main_menu)):
        print(f'    {i+1}. {main_menu[i]}')

    user_input = int(input('Введите комнду \n>>> '))
    
    while(user_input > len(main_menu) or user_input <= 0):
        for i in range(len(main_menu)):
            print(f'    {i+1}. {main_menu[i]}')
        user_input = int(input('Введите комнду \n>>> '))

    return user_input




def change_contact(db: list):
    change_menu = ['Фамилию',     # меню изменений
                 'Имя',
                 'Номер',
                 'Коментарий',
                 'Всё',
                ]


    change_user_id = int(input('Введите id контакта которую хотите изменить \n>>> '))

    
    while(change_user_id > len(db) or change_user_id < 1):    # проверка на дурака (ошибка в выборе контакта)
        change_user_id = int(input('Введите id контакта которую хотите изменить \
                                    \nЕсли вы хотите выйти введите 0 \n>>> '))
        if(change_user_id == 0):
            break
    if(change_user_id == 0):
        print('ERROR')
        return

    change_contact = db[change_user_id-1] 


    print('Что вы хотите изменить?')   # вывод меню изменений
    for i in range(len(change_menu)):
        print(f'    {i+1}. {change_menu[i]}') 
    what_change = int(input('Введите номер того, что вы хотите изменить \n>>> '))


    if(what_change == 1):
        change_contact['lastname']  = input('   Введите фамилию \n>>> ')
    
    elif(what_change == 2):
        change_contact['firstname'] = input('   Введите имя \n>>> ')
    
    elif(what_change == 3):
        change_contact['phone']     = input('   Введите номер \n>>> ')
    
    elif(what_change == 4):
        change_contact['comment']   = input('   Введите комментарий \n>>> ')
    
    elif(what_change == 5):
        change_contact['lastname']  = input('   Введите фамилию \n>>> ')
        change_contact['firstname'] = input('   Введите имя \n>>> ')
        change_contact['phone']     = input('   Введите номер \n>>> ')
        change_contact['comment']   = input('   Введите комментарий \n>>> ')

        