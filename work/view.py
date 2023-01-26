import controller
import model


number = 0
isSaveChangeContact = True

def main_menu() -> int:
    print('Главное меню.')
    menu_list = ['Показать все контакты',
                 'Открыть файл',
                 'Сохранить файл',
                 'Создать контакт',
                 'Изменить контакт',
                 'Найти контакт',
                 'Удалить контакт',
                 'Выход'
                 ]
    for i in range(len(menu_list)):
        print(f'\t{i + 1}. {menu_list[i]}')
    user_input = int(input('Введи команду >: '))
    # TODO: сделать валидацию
    return user_input


def show_all(db: list):
    if db_success(db):
        for i in range(len(db)):
            user_id = i + 1
            print(f'\t{user_id}', end='. ')
            for v in db[i].values():
                print(f'{v}', end=' ')
            print()


def db_success(db: list):
    if db:
        print('Телефонная книга открыта')
        return True
    else:
        print('Телефонная книга пуста или не открыта')
        return False


def exit_program():
    print('Завершение программы.')
    exit()


def create_contact():
    print('Создание нового контакта.')
    new_contact = dict()

    new_contact['lastname'] = input('\tВведите фамилию >: ')
    new_contact['firstname'] = input('\tВведите имя >: ')
    new_contact['phone'] = input('\tВведите телефон >: ')
    new_contact['comment'] = input('\tВведите комментарий >: ')
    print()
    print('Новый контакт создан.')


def change_contact():
    global number
    print("Изменение контакта.")

    change_contact = dict()

    while True:
        try:
            num = int(input('Введи порядковый номер контакта >: '))
            if num > 0 and num <= controller.db_list_ifo():
                number = num - 1
                change_contact['lastname'] = input('\tВведите фамилию >: ')
                change_contact['firstname'] = input('\tВведите имя >: ')
                change_contact['phone'] = input('\tВведите телефон >: ')
                change_contact['comment'] = input('\tВведите комментарий >: ')
                print(f"контакт под номером {number + 1} изменен")

                save_input = input("Сохранить изменения? Введите да/нет ")
                if save_input == "да":
                    return change_contact

                else:
                    print("изменения не сохранены")
                    return controller.dictonary(number)
            else:
                print(f'Вводите только числа от 1 до {controller.db_list_ifo()}')

        except ValueError:
            print(f'Вводите только числа от 1 до {controller.db_list_ifo()}')



def search_contact(db: list):
    num = input('Введи текст для поиска >: ')
    print()
    count = 0
    for i in range(len(db)):
        for v in db[i].values():
            if v == num:
                print("Совпадения найдены:")
                valuesList = list(db[i].values())
                print(', '.join(valuesList))
                print()
                count += 1
    if count <= 0:
        print("Точных совпадений не найдено")
        print()

def delete_contact(db: list):
    while True:
        try:
            num = int(input('Для удаления введи порядковый номер контакта >: '))
            if num > 0 and num <= controller.db_list_ifo():
                db.pop(num - 1)
                print(f"Контакт под номером {num} удален")
                print()
                break
            else:
                print(f'Вводите только числа от 1 до {controller.db_list_ifo()}')

        except ValueError:
            print(f'Вводите только числа от 1 до {controller.db_list_ifo()}')


