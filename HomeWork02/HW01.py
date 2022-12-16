# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
print('Программа принимает на вход вещественное число и показывает сумму его цифр.')
# Пример:

# - 6782 -> 23
# - 0,56 -> 11

sum_digits = 0
num_string = input('Введите вещественное число: ')
num_string_without_separator = num_string.replace('.','').replace(',','')
for i in num_string_without_separator:
    sum_digits = sum_digits + int(i)
print('Сумма цифр числа ',num_string, ' равна ', sum_digits)
