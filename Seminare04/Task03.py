# 29. Задайте два числа. Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

a = int(input('Введите число: '))
b = int(input('Введите еще число: '))
i = a
if b>i:
    i = b
j = i    
while i % a != 0 or i % b != 0: 
    i += j
print(i)