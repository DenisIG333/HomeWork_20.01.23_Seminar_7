import model
import view


def dictonary(number: int):
    return model.db_list[number]

def db_list_ifo():
    return len(model.db_list)


def input_handler(inp: int):
    match inp:
        case 1:
            view.show_all(model.db_list)
        case 2:
            model.read_db('database.txt')
            view.db_success(model.db_list)
        case 3:
            model.save_db('database.txt')
        case 4:
            model.db_list.append(view.create_contact())
        case 5:
            view.show_all(model.db_list)
            model.db_list[view.number] = view.change_contact()
        case 6:
            view.search_contact(model.db_list)
        case 7:
            view.show_all(model.db_list)
            view.delete_contact(model.db_list)
        case 8:
            view.exit_program()
        case _ :
            print("Введи от 1 до 8")


def start():
    while True:
        user_inp = view.main_menu()
        input_handler(user_inp)