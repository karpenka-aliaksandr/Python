#Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
# print(max(int(input()),int(input()),int(input())))

# a = int(input())
# maxx = a
# for i in range(4):
#     a = int(input())
#     if a>maxx:
#         maxx = a
# print(maxx)

import array
 
def Max(ar):
    max = ar[0]
    for i in range(1,len(ar)):
        if ar[i]>max:
            max = ar[i] 
    return max

arr = []
for i in range(5):
    arr.append(int(input(f"Введите число {i+1}: ")))

max = Max(arr)
print(max)