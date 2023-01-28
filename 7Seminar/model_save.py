
def write(path: str, db: list):

    #cleaning
    contact_list = []

    for dict in db:
        contact_list.append(dict['lastname']  + ';' \
                        + dict['firstname'] + ';' \
                        + dict['phone']     + ';' \
                        + dict['comment']   + ';')


    
    #saving
    with open(f'7Seminar\{path}', 'w', encoding='UTF-8') as file:  
        for contact in contact_list:
            file.writelines(f'{contact} \n')





