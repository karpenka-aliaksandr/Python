# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
print('Программа задаёт список из N элементов, заполненных числами из промежутка [-N, N]. ')
# Найдите произведение элементов на указанных позициях.
print('Находит произведение элементов на указанных позициях.')
# Позиции хранятся в файле file.txt в одной строке одно число.
print('Позиции хранятся в файле file.txt в одной строке одно число.')

N = int(input('Введите натуральное N: '))
list_numbers = list(range(-N, N+1))
print(list_numbers)
product = 1
fl = open('file.txt')
print('Произведение элементов списка с индексами: ', end='')
for line in fl:
    print(int(line), end=' ')
    product *= list_numbers[int(line)]
fl.close
print('равно', product)
