# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

from decimal import Decimal

l = [1.1, 1.2, 3.1, 5, 10.01]
if len(l) == 0:
    print('Список пуст.')
    quit()
min_fract = Decimal('1')
max_fract = Decimal('0')
for i in range(len(l)):
    fract = Decimal(str(l[i]))-int(l[i])
    if fract > max_fract:
        max_fract = fract
    if 0 < fract < min_fract:
        min_fract = fract
print(max_fract - min_fract)


