import model
import view


#print(temp)



def input_handler(inp: int):
    match inp: 
        case 1:
            model.Read_DB(view.Classroom())
            view.DB_Success(model.class_list)
        case 2:
            view.Subject_List(model.class_list)
        case 3:
            model.Lesson(view.Subject(model.class_list), view.Call_Pupils(model.class_list, view.Subject(model.class_list)), view.Grade())
        case 4:
            view.Exit_Program()
            
def start():
    while True:
        user_inp = view.main_menu()
        input_handler(user_inp)