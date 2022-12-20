# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
from decimal import Decimal
print('Программа принимает на вход вещественное число и показывает сумму его цифр.')
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# решение 1
# sum_digits = 0
# num_string = input('Введите вещественное число: ')
# num_string_without_separator = num_string.replace('.', '').replace(',', '')
# for i in num_string_without_separator:
#     sum_digits = sum_digits + int(i)
# print('Сумма цифр числа ', num_string, ' равна ', sum_digits)

# решение 2
sum_digits = 0
num_dec = Decimal(input('Введите вещественное число: '))
if num_dec < 0:
    num_dec *= -1
while num_dec % 1 > 0: 
    num_dec *=10
while num_dec > 0:
    sum_digits = sum_digits + int(num_dec % 10)
    num_dec //= 10
print(sum_digits)


