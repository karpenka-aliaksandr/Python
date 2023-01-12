#  Дан список заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут только уникальные элементы исходного.
#     Примечание. Списки создайте вручную, например так:
# my_list_1 = [2, 2, 5, 12, 8, 2, 12]

# В этом случае ответ будет:
# [5, 8]
my_list_1 = [2, 2, 5, 12, 8, 2, 12]
for elem in my_list_1:
    if my_list_1.count(elem)>1:
        while elem in my_list_1:
            my_list_1.remove(elem)
print(my_list_1)



# my_list_1 = [2, 2, 5, 12, 8, 2, 12]
# my_list_set = set(my_list_1)
# print(my_list_set)
# for elem in my_list_set:
#     my_list_1.remove(elem)
# print(my_list_1)
# my_list_set1=set(my_list_1)
# my_set = my_list_set - my_list_set1
# print (my_set)