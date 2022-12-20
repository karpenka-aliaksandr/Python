# 21. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.

# *Пример:*

# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1


spisok = ["qwe", "asd", "zxc", "qwe", "ertqwe"] 
find = "qwe"
pos = -1
vhogdenie = 0
for i in range(len(spisok)):
    if spisok[i] == find:
        vhogdenie += 1
    if vhogdenie == 2:
        pos = i
        break
print(pos)           


# list_str =  []
# sub_str = "123"
# count = 0
# for i in range(len(list_str)):
#     print(i)
#     if list_str[i]==sub_str:
#         count+=1
#         if count == 2:
#             print(i)
#             break
# if count<2:
#     print(-1)
