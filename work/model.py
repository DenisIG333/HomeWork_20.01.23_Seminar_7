db_list = []


def read_db(path: str) -> list:
    global db_list
    with open(path, 'r', encoding='UTF-8') as file:
        my_list = file.readlines()
        for line in my_list:
            id_dict = dict()
            line = line.strip().split(';')
            id_dict['lastname'] = line[0]
            id_dict['firstname'] = line[1]
            id_dict['phone'] = line[2]
            id_dict['comment'] = line[3]
            db_list.append(id_dict)


def save_db(path: str):

    with open(path, 'w', encoding='UTF-8') as data:
        for i in range(len(db_list)):
            for _ in db_list[i].values():
                value_list = db_list[i].values()
                new_value_list = ', '.join(value_list) + "\n"
            data.write(new_value_list.replace(",", ";").replace(" ", ""))

    print("Файл сохранен")
    data.close()