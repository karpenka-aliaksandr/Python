# Задайте последовательность чисел. Напишите программу, 
# которая выведет список неповторяющихся элементов исходной последовательности.


from random import randint
n_list = list(randint(1,4) for i in range(randint(5,10+1)))
print(n_list)
n_mn = []
for i in n_list:
    if not i in n_mn:
        n_mn.append(i)
print(n_mn)    
