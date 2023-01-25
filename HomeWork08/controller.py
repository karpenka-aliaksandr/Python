import model
import view
import os
from statistics import mean

def add_student():
    while True:
        os.system("cls")
        students = model.get_students()
        view.show_students(students)
        while True:
            name = input("Добавление ученика. Введите фамилию и имя (пустое поле - выйти из меню): ").strip()
            if name:
                break
            return
            # os.system("cls")
            # view.show_students(students)
            # print(name,'- недопустимое значение. Введите повторно.')
        model.add_student(name)

def add_lesson():
    os.system("cls")
    courses = model.get_courses()
    view.show_courses(courses)
    course = input("Введите предмет: ").strip()
    model.add_cours(course)

def choise_student(students:dict):
    os.system("cls")
    view.show_students(students,show_ind=True)
    while True:
        ind = 0  
        name = input('Выберите студента (номер или фамилия и имя): ').strip()
        if name.isdigit():
            ind = int(name)
            list_names = [value for inx,value in enumerate(sorted(students.keys()),start = 1) if inx == ind]
            if list_names:
                name = list_names[0]
        if name in students.keys():
            break
        else:
            os.system("cls")
            view.show_students(students,show_ind=True)
            print('Неправильный ввод. Повторите.')
    return name

def choise_course(courses:dict,name):
    os.system("cls")
    if name:
        print(f'Ученик: {name}')
        print()
    view.show_courses (courses,show_ind=True)
    while True:     
        ind = 0  
        course = input('Выберите предмет (номер или наименование): ')
        if course.isdigit():
            ind = int(course)
            list_names = [value for inx,value in enumerate(sorted(courses.keys()),start = 1) if inx == ind]
            if list_names:
                course = list_names[0]
        if course in courses.keys():
            break
        else:
            os.system("cls")
            if name:
                print(f'Ученик: {name}')
                print()
            view.show_courses (courses,show_ind=True)
            print('Неправильный ввод. Повторите.')
    return course

def show_grades_student(name,course):
    os.system("cls")
    print(f'Ученик: {name}')
    print(f'Предмет: {course}')
    students= model.get_students()
    grades = students[name][course]
    print('Оценки: ',end='')
    if grades:
        print(', '.join(map(str,grades)))
        print(f'Средний балл: {round(mean(map(int,grades)),1)}')
    else:
        print('пока нет оценок.')
    print()

def show_all_grades(name):
    os.system("cls")
    students= model.get_students()
    print(f'Ученик: {name}')
    print()
    for course in students[name].keys():
        print(f'Предмет: {course}', end='  ')  
        grades = students[name][course]
        print('Оценки: ',end='')
        if grades:
            print(', '.join(map(str,grades)), end='. ')
            print(f'Средний балл: {round(mean(map(int,grades)),1)}')
        else:
            print('пока нет оценок.')
    print()



def ins_grades(name,course):
    while True:
        show_grades_student(name,course)
        while True:

            s_grade = input ('Введите оценку, которую хотите добавить (1-5) или 0 для выхода: ')
            if s_grade in ['0','1','2','3','4','5']:
                grade = int(s_grade)
                break
            else:
                show_grades_student(name,course)
                print('Неправильный ввод. Повторите.')
        if grade:
            model.add_grade(name,course,grade)
        else:
            break

def add_grades():
    students= model.get_students()
    name=choise_student(students)
    courses= model.get_courses()
    course = choise_course(courses,name)
    ins_grades(name,course)

def show_grades():
    students= model.get_students()
    name=choise_student(students)
    show_all_grades(name)
    __ = input('Нажмите Enter, чтобы продолжить.')

def mean_course():
    students= model.get_students()
    courses= model.get_courses()
    course = choise_course(courses,'')
    sum =0
    count = 0
    for student in students.values():
        for grade in student[course]:
            sum += int(grade)
            count += 1
    os.system("cls")
    print(f'Предмет: {course}')
    print (f'Средний балл по предмету: {round(sum/count,1)}')
    print()
    __=input('Нажмите Enter, чтобы продолжить')

def golden_students():
    os.system("cls")
    stud=[]
    students= model.get_students()
    courses= model.get_courses()
    for student in students.keys():
        is_golden = True
        for course in courses.keys():
            for grade in students[student][course]:
                if grade in [1,2,3]:
                    is_golden = False
        if is_golden:
            stud.append(student)
    if stud:
        print(f'На золотую медаль претендуют {len(stud)} ученик(-а,-ов):')
        for st in stud:
            print(st)
    else:
        print(f'На золотую медаль не претендует ни один ученик.')
    print()
    __=input('Нажмите Enter, чтобы продолжить')



def start():
    model.load()
    while True:
        os.system("cls")
        view.show_menu()
        while True:
            menu_input = 0
            s = input('Введите пункт меню: ')
            if s.isdigit():
                menu_input = int(s)
            if 0<menu_input<9:
                break
            else:
                os.system("cls")
                view.show_menu()
                print("Неправильный ввод. Повторите")
        match menu_input:
            case 1:
                add_student()
            case 2:
                add_lesson()
            case 3:
                add_grades()
            case 4:
                show_grades()
            case 5:
                mean_course()
            case 6:
                golden_students()
            case 7:
                model.save()
                __ = input('Данные сохранены. Нажмите Enter, чтобы продожить.')
            case 8:
                print('Выход из программы.')         
                exit()

            