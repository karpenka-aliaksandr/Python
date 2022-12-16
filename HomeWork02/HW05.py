# Реализуйте алгоритм перемешивания списка.
import random

print('Программа создает список с элементами от 1 до N и реализует алгоритм его перемешиваия.')
N = int(input('Введите число N: '))
spisok = list(range(1, N+1))
print('Начальный список   : ', spisok)


# index_temp = random.randint(0,N-1)
# temp = spisok[index_temp]
# for i in range(len(spisok)):
#     index_temp1 = random.randint(0,N-1)
#     spisok[index_temp] = spisok[index_temp1]
#     index_temp = index_temp1
# spisok[index_temp] = temp
# print('Cписок перемешанный: ', spisok)

# немного улучшенный, гарантировано перемещение каждого числа.
sorted = [0]*len(spisok)
index_temp = random.randint(0, N-1)
sorted[index_temp] = 1
temp = spisok[index_temp]
for i in range(len(spisok)-1):
    index_temp1 = random.randint(0, N-1)
    while sorted[index_temp1]:
        index_temp1 += 1
        if index_temp1 == N:
            index_temp1 = 0
    spisok[index_temp] = spisok[index_temp1]
    sorted[index_temp1] = 1
    index_temp = index_temp1
spisok[index_temp] = temp
print('Cписок перемешанный: ', spisok)
