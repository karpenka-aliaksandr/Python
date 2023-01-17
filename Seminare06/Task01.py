#41)Напишите программу на Python для поиска пересечения двух
# заданных массивов с помощью Lambda, filter.

def intersection(a:list,b:list) -> list:
    return [a for a in a if a in b]

a = [1, 2, 3, 5, 7, 8, 9, 10]
b = [1, 2, 4, 8, 9]
print(intersection(a,b))


# a1 = [1, 2, 3, 5, 7, 8, 9, 10]
# a2 = [1, 2, 4, 8, 9]
#
# res = list(filter(lambda x: x in a1,a2))
# print(res)

