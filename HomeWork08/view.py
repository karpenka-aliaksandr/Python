def show_menu():
    print("Меню:")
    print("1. Добавление нового ученика (отобразить учеников)")
    print("2. Добавление предмета")
    print("3. Добавить оценки ученику по предмету (вывод среднего балла по предмету)")
    print("4. Вывод листа оценок конкретного ученика (со средним баллом) ")
    print("5. Вывод среднего балла по школе по предмету")
    print("6. Вывод учеников, претендующих на золотую медаль")
    print("7. Сохранить данные")
    print("8. Выход из программы без сохранения данных")
    print()

def show_students(students:dict,show_ind = False):
    print('Ученики:')
    for ind,name in enumerate(sorted(students.keys()),start=1):
        if show_ind: 
            print(ind, end=' ')
        print(name)
    print()

def show_courses(courses:dict,show_ind = False):
    print('Предметы:')
    for ind,name in enumerate(sorted(courses.keys()),start=1):
        if show_ind: 
            print(ind, end=' ')
        print(name)
    print()