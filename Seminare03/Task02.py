# 20. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

spisok = ['qwe','qweqw',3.2,'weqwe']
flag = False
for item in spisok:
    if isinstance(item,int):
        flag = True
    if isinstance(item,float):
        flag = True
print(flag)



# a = ["st","qwe","12","tyy"]
# for i in a:
#     if i.isdigit():
#         print(a.index(i))
