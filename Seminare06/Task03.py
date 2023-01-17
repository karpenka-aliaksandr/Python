# 43)Имеется список id сотрудников из 10 элементов, каждый id - случайное число от 1 до 100 (сделать с помощью list_comprehension)
# Имеется список имен сотрудников из 10 элементов (вручную)

# Сопоставьте каждому имени сотрудника его id по порядку, и выведите получившийся список кортежей.
# Отсортировать список по возрастанию id.

# Выведете имена сотрудников, получившие нечетное id.

# Решить с помощью zip,filter,lambda

import random
def hr_base(names:list,ids:list):
    out = list(zip(ids,names))
    out = sorted(out,key=lambda x: x[0])
    print(out)
    out = list(map(lambda x: x[1],filter(lambda x: x[0]%2==1,out)))
    return out

names ="""Иванов
Смирнов
Кузнецов
Попов
Васильев
Петров
Соколов
Михайлов
Кабанов
Носков"""
ids = random.sample(population=range(1,101),k=10)
print(hr_base(names.split(),ids))



# import random
# id = random.sample(range(0,100), 10)
# print(id)
#
# name = ["s1","s2","s3","s4","s5","s6","s7","s8","s9","s10",]
#
# res = list(zip(id,name))
# print(res)
#
# res = sorted(res)
# print(res)
#
# odd_list = list(filter(lambda x: x[0]%2==1,res))
# print(odd_list)
# names_list = list(map(lambda x:x[1],odd_list))
# print(names_list)
