# 1)Создайте список из случайных чисел. Найдите максимальное количество его одинаковых элементов.
# В первой задаче 10 чисел в диапазоне от 2 до 5.



import random

max_count = 0
numbers = list()
for i in range(10):
    numbers.append(random.randint(2,5))
print(numbers)
i=0
while i<len(numbers)-max_count:
    count = 1
    for j in range(i+1,len(numbers)):
        if numbers[i] == numbers[j]:
            count += 1
    
    if count > max_count:
        max_count = count
    i+=1
print(max_count)

# другое решение через словарь
import random

a = 1
b = 6

array = [random.randint(a, b) for i in range(20)]
print(array)

d = {}

for i in array:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
    
print(d)

max = 0
for i in range(a, (b+1)):
    if(d[i] > max):
        max = d[i]

print(f"Максимальное повторение элемента {max} раз.")
# От Юрий Хван всем 10:15 PM


# от препода
# import random
#
# list_num = []
# max = 0
# for i in range(10):
#     a= random.randint(2,5)
#     list_num.append(a)
# print(list_num)
# print(set(list_num))
# for i in set(list_num):
#     if list_num.count(i)>max:
#         max = list_num.count(i)
# print(max)

# еще вариант
# import random

# number = int(input())
# maxRandom = int(input('input max random number'))
# maxAmount = 0

# list = []
# count = [0] * (maxRandom+1)

# for i in range(0, number):
#     list.append(random.randint(0, maxRandom))

# for i in list:
#     count[int(i)] += 1

# for i in count:
#     if i > maxAmount:
#         i = maxAmount

# print(list)
# print(max(count))

# вывод не доделан
# print('МАскимально количество раз появилась ' + str(count[maxAmount]) + ', ' + str(maxAmount+1) + ' раз')



