# 11. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
    
#     *Пример:*
    
#     - Для N = 5: 1, -3, 9, -27, 81

N = int(input('Введите число N: '))
numbers = list()
numbers.append(1)
for i in range(1,N):
    numbers.append(-numbers[i-1]*3)
print(numbers)




# метод преподавателя
# n = int(input())
# num = 1
# print(num, end = " ")
# for i in range(1,n):
#     num*=-3
#     print(num, end = " ")

