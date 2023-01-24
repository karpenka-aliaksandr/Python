import model
import view
import os

def add_student():
    name = input("введите фамилию, имя (через пробел): ").strip()
    model.add_student(name)

def add_lesson():
    lesson = input("введите предмет: ").strip()
    model.add_lesson(lesson)

def show_student(data):
    view.show_student(data)
    s = input()


def start():
    while True:
        #os.system("cls")
        view.show_menu()
        while True:
            menu_input = int(input())
            if 0<menu_input<6:
                break
            else:
                print("неправильный ввод")
        match menu_input:
            case 1:
                add_student()
            case 2:
                add_lesson()
            case 3:
                data = model.get_data()
                show_student(data)
            case 5:
                exit()

            