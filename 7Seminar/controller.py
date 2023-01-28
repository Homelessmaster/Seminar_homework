import model_read
import view
import model_save


#print(temp)



def input_handler(inp: int):
    match inp: 
        case 1:
            view.show_all(model_read.db_list)
        case 2:
            model_read.read_db('database')
            view.db_success(model_read.db_list)
        case 3:
            model_save.write('database', model_read.db_list)
        case 4:
            model_read.db_list.append(view.create_contact())
        case 5:
            view.change_contact(model_read.db_list)
        case 6:
            view.delete_contact(model_read.db_list)
        case 7: 
            view.exit_program()
            
def start():
    while True:
        user_inp = view.main_menu()
        input_handler(user_inp)

