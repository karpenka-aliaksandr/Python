# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
print('Программа задает список из n чисел последовательности (1+1/n)^n и выводит на экран их сумму.')
# Пример:
# - Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44}

N = int(input('Введите натуральное N: '))
sequence = {}
sum_sequence = 0
for n in range(1, N+1):
    sequence[n] = round((1+1/n)**n, 2)
    sum_sequence += sequence[n]
print(sequence)
print('sum = ', sum_sequence)
