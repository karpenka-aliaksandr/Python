import model_phones as mp
import model_menu as mm
import model_sub_menu as msm
import view as v

sort_id=False
sort_name=False 



def insert_record(data):
    v.view_data(data,clear=True,sort_id=sort_id,sort_name=sort_name)
    while True:
        id = -1
        s_id = input('Введите id(число) новой записи (или введите 0 для автоматического назначения id): ').strip()
        if s_id.isdigit():
            id = int(s_id)
        if id<0:
            print(f'{s_id} - недопустимо для id. Введите допустимый.')      
        elif id in data.keys():
            v.view_data(data,clear=True,sort_id=sort_id,sort_name=sort_name)
            print(f'{s_id} - Такой id уже существует. Введите уникальный.')
        else:
            break
    if id == 0:
        if data:
            id = max(data.keys())+1
        else:
            id = 1
        print(f'Автоматически назначен id = {id}')
    msm.clear()
    msm.add(f'Cоздание новой записи с id: {id}')
    v.view_sub_menu(msm.get())
    while True:
        s_name = input('Введите имя и фамилию через пробел: ').strip()
        if s_name:
            if len(s_name.split()) == 2:
                break
        v.view_data(data,clear=True,sort_id=sort_id,sort_name=sort_name)
        v.view_sub_menu(msm.get())
        print(f'{s_name} - не подходит')
    msm.add(f'Фамилия имя: {s_name}')
    v.view_data(data,clear=True,sort_id=sort_id,sort_name=sort_name)
    v.view_sub_menu(msm.get())
    while True:
        s_number = input('Введите номер телефона в формате +<код страны>(<код оператора>)<номер>: ')
        print(s_number)
        if s_number:
            if s_number.find('+') == 0:
                if s_number.find('(') > 1:

                    if len(s_number) - 1 > s_number.find(')') > s_number.find('(')+1:
                        break
        v.view_data(data,clear=True,sort_id=sort_id,sort_name=sort_name)
        v.view_sub_menu(msm.get())
        print(f'{s_number} - не подходит')
    msm.add(f'Телефон: {s_number}')
    v.view_data(data,clear=True,sort_id=sort_id,sort_name=sort_name)
    v.view_sub_menu(msm.get())
    while True:
        s_note = input('Введите примечание без пробелов: ').strip()
        if s_note:
            if ' '.find(s_note)==-1:
                break
        v.view_data(data,clear=True,sort_id=sort_id,sort_name=sort_name)
        v.view_sub_menu(msm.get())
        print(f'{s_note} - не подходит')
    mp.add_record(data,id,s_name,s_number,s_note)

def delete_record(data:dict):
    v.view_data(data,clear=True,sort_id=sort_id,sort_name=sort_name)
    while True:
        id=-2
        s_id = input('Введите id(число) записи, которую хотите удалить, -1 удалить все записи (или введите 0 для выхода из меню.): ').strip()
        if s_id.isdigit():
            id = int(s_id)
        if id in data.keys() or id == 0 or s_id == '-1':
            break
        else:
            v.view_data(data,clear=True,sort_id=sort_id,sort_name=sort_name)
            print(f'{s_id} - такого id нет или некорректный ввод. Введите существующий.')
    if s_id == '-1':
        mp.delete_all_record()
    elif id != 0:
        mp.delete_record(data,id)
    
def sort_record(data):
    global sort_id,sort_name
    v.view_data(data,clear=True,sort_id=sort_id,sort_name=sort_name)
    while True:
        s_id = input('Выберите: 1 - сортировать записи по id, 2 - сортировать по фимилии и имени, 0 - не сортировать: ')
        if s_id.isdigit():
            id = int(s_id)
        if 2 >= id >= 0:
            break
        else:
            v.view_data(data,clear=True,sort_id=sort_id,sort_name=sort_name)
            print(f'{s_id} - такого пункта нет. Введите существующий.')
    if id == 0:
        sort_id = False
        sort_name = False
    elif id == 1:
        sort_id = True
        sort_name = False
    else:
        sort_id = False
        sort_name = True
    
def view_only_names(data):
    v.view_data(data,clear=True,sort_id=sort_id,sort_name=sort_name,only_name=True)
    __ = input('Нажмите Enter для того, чтобы продолжить')





def choice(data,menu):
   
    punkt_id = 0
    while True:
        s_punkt_id = input('Введите номер меню: ')
        if s_punkt_id.isdigit():
            punkt_id = int(s_punkt_id)
        if punkt_id in menu:
            break
        else:
            v.view_data_menu(data,menu,clear=True)
            print(f'{s_punkt_id} - неправильный выбор')
    match menu[punkt_id]:
        case 'Добавить запись':
            insert_record(data)
        case 'Удалить запись':
            delete_record(data)
        case 'Сортировать записи':
            sort_record(data)
        case 'Вывести только имя и фамилию':
            view_only_names(data)
        case _:
            print('Выход из программы')
            exit()
    

def change():
    data = mp.get_all()
    mm.make_menu(data)
    menu=mm.get_menu()
    return data,menu


def start():
    data,menu = change()
    v.view_data_menu(data,menu,clear=True)
    while True:
        choice(data,menu)
        data,menu = change()
        v.view_data_menu(data,menu,clear=True,sort_id=sort_id,sort_name=sort_name)

    
    
    
        

