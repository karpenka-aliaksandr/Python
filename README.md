# Python

## Особенности:

- Интерпретируемый.
- Неявная типизация.
- Нет ограничения на длину хранимых данных.

## 1. Основы синтаксиса

    1. Очистка экрана
    
    import os
    os.system('cls||clear')

    2. Команды разнесены по строкам. Без точки с запятой в конце.

    3. Динамическая типизация. Не требуется заранее объявлять переменные.
    
    Типы данных: int, float, boolean, str
    list и др.
    Есть особое значение None.
    
    Для вывода типа - функция type()

    Строка записывается в одинарных или двойных кавычках.
    Чтобы закоментировать строку или её часть используется символ "#"
    Перевод строки "/n"
   
    4. Варианты вывода.
    
    print(a, b, c) #вывод переменных в одну строку
    print(a, ' - ', b, ' - ', c)
    print('{} - {} - {}'.format(a, b, c))
    print('{1} - {2} - {0}'.format(a, b, c))
    print(f'{a} - {b} - {c}')                   # Сергей Камянецкий назвал это интерполяцией

    5. Тип list.

    Список – пронумерованная, изменяемая коллекция объектов "произвольных" типов
    list = [1, 3, 2, 34]

    numbers = [1, 2, 3, 4, 5]
    print(numbers) # [1, 2, 3, 4, 5]

    numbers = list(range(1, 6))
    print(numbers) # [1, 2, 3, 4, 5]

    numbers[0] = 10
    print(numbers) # [10, 2, 3, 4, 5]

    for i in numbers:                   # i-копия значения элемента 
        i *= 2
        print(i) # [20, 4, 6, 8, 10]
    print(numbers) # [10, 2, 3, 4, 5] 


    colors = ['red', 'green', 'blue']
    
    for e in colors:
        print(e)            # red green blue

    for e in colors:
        print(e*2)          # redred greengreen blueblue

    colors.append('gray')   # добавить в конец
    print(colors == ['red', 'green', 'blue', 'gray']) # True
    colors.remove('red') #или del colors[0] # удалить элемент



    6. Ввод данных input().

    a = input('Введите число: ')
    a - строка

    a = int(input('Введите число: '))
    a - целое число

    a = float(input('Введите число: '))
    a - вещественное число
    
    7. Операции: 

    + - сложение
    - - вычитание
    / - деление (вещественное)
    * - умножение
    // - деление целочисленное
    ** - возведение в степень
    % - остаток от деления

    округление - round(n, <число знаков>)

    сокращенные операции присваивания: а += 5 (замена а = а + 5), *=, -= и т.д. 

    8. Логические операции

    >, >=, <, <=, ==, !=
    not, and, or - не путать с &, |, ^ (побитовые)
    is, is not, in, not in

    9. Управляющие конструкции if-else

    if condition :
        # operator 1
        # operator 2
        # ...
        # operator n
    else:
        # operator n + 1
        # operator n + 2
        # ...
        # operator n + m

    if условие:
        блок 1
    else
        блок 2

    10. Управляющие конструкции if-elif-else
   
    if condition1:
        # operator
    elif condition2:
        # operator
    elif condition3:
        # operator
    else:
        # operator 
    
    11. Управляющие конструкции: while

    while condition:
        # operator 1
        # operator 2
        # . . .
        # operator n

    12. Управляющие конструкции: while-else

    while condition:
        # operator 1
        # operator 2
        # . . .
        # operator n
    else:
        # operator n + 1
        # operator n + 2
        # . . .
        # operator n + m
    
    13. Управляющие конструкции: for
   
    for i in enumeration:
        # operator 1
        # operator 2
        # . . .
        # operator n

    r = range(5)            # range(0, 5)
    r = range(2, 5)         # range(2, 5)
    r = range(-5, 0)        # range(-5, 0)
    r = range(1, 10, 2)     # range(1, 10, 2)
    r = range(100, 0, -20)  # range(100, 0, -20)

    r = range(100, 0, -20)  # range(100, 0, -20)
    for i in r:
        print(i)
    # 100 80 60 40 20
    for i in range(5):
        print(i)
    # 0 1 2 3 4
        
    14. Строки
    text = 'съешь ещё этих мягких французских булок'
    print(len(text))                    # 39
    print('ещё' in text)                # True
    print(text.isdigit())               # False
    print(text.islower())               # True
    print(text.replace('ещё','ЕЩЁ'))    # 'съешь ЕШЁ этих мягких французских булок'
    for c in text:
        print(c)

    text = 'съешь ещё этих мягких французских булок'
    print(text[0])                          # c
    print(text[1])                          # ъ
    print(text[len(text)-1])                # к
    print(text[-5])                         # б
    print(text[:])                          # print(text)
    print(text[:2])                         # съ
    print(text[len(text)-2:])               # ок
    print(text[2:9])                        # ешь ещё
    print(text[6:-18])                      # ещё этих мягких
    print(text[0:len(text):6])              # сеикакл # с шагом 6
    print(text[::6])                        # сеикакл
    text = text[2:9] + text[-5] + text[:2]  #
    
    15. функции

    Это фрагмент программы, используемый многократно

    def function_name(x):
        # body line 1
        # . . .
        # body line n
        # optional return

    