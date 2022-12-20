# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

k = int(input('Введите целое положительное число: '))
list_fib = []
for i in range(k+1):
    if i == 0:
        list_fib.append(0)
    elif i==1:
        list_fib.append(1)
        list_fib.insert(0,1)
    else:
        list_fib.append(list_fib[-1]+list_fib[-2])
        list_fib.insert(0,list_fib[1]-list_fib[0])
print(list_fib)