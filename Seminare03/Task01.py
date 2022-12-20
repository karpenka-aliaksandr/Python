# 19. Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.
import datetime


def Random_num(max_random_num):
    random = datetime.datetime.now().microsecond
    print(random)
    return random % max_random_num


max_random = int(input('Введите максимум для генерации случайного числа: '))
print(Random_num(max_random+1))




# import datetime
# n = int(input())
# rand = datetime.datetime.now().microsecond%(n+1)
# print(rand)
