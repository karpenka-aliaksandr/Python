#                        ЛЕКЦИЯ 4. ФУНКЦИИ ВЫСШЕГО ПОРЯДКА, РАБОТА С ФАЙЛАМИ
# 
# Решение задачи сложения двух чисел:
x = 0
y = 0 # Описываем два числа (переменные)

def init(a, b): # Метод инициализации значений
    global x # Связывает переменную в методе с глобальной переменной
    global y # Связывает переменную в методе с глобальной переменной
    x = a
    y = b

def do_it():   # Метод сложения двух чисел
    return x+y
