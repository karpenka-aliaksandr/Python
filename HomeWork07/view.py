import os


def view_data(data: dict, clear=False, sort_id=False, sort_name=False, only_name=False):
    if clear:
        os.system('cls')
    print('СПРАВОЧНИК:')
    lines=[]
    if data:
        for id, record in data.items():
            surname, name, phone, note = record.split()
            line = [id, surname, name, phone, note]
            lines.append(line)
        if sort_id:
            lines=sorted(lines, key = lambda line : line [0])
        if sort_name:
            lines=sorted(lines, key = lambda line : (line [1], line [2], line[0]))
        if only_name:
            temp_lines=[]
            for line in lines:
                t_line = ' '.join([line[1],line[2]])
                if t_line not in temp_lines:
                    temp_lines.append(t_line)
            lines=[]
            for line in temp_lines:
                lines.append(line.split())
        for line in lines:
            for elem in line:
                print(elem, end=' ')
            print()         
    else:
        print("В справочнике нет записей")
    print()


def view_menu(menu, clear=False):
    if clear:
        os.system('cls')
    print('МЕНЮ:')
    if menu:
        for punkt in menu.keys():
            print(f'{punkt}. {menu[punkt]}')
    else:
        print('В меню нет пунктов для вывода')
    print()


def view_sub_menu(sub_menu, clear=False):
    if clear:
        os.system('cls')
    if sub_menu:
        for element in sub_menu:
            print(element)


def view_data_menu(data, menu, clear=False, sort_id=False, sort_name=False, only_name=False):
    if clear:
        os.system('cls')
    view_data(data, sort_id=sort_id, sort_name=sort_name, only_name=only_name)
    view_menu(menu)
