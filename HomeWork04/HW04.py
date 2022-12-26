# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.

# Пример:
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint
koef_max = 100
k = int(input('Введите натуральную степень k: '))
path = 'mn.txt'
file = open(path,'w')
for i in range(k,-1,-1):
    koef = randint(0,koef_max)
    if i == k:
        while not koef:
            koef = randint(0,koef_max)
    if i != k and koef > 0:
            file.write('+')
    if koef != 0:
        if koef != 1 or i == 0:
            file.write(str(koef))
            if i > 0:
                file.write('*')
        if i>0:
            file.write('x')
        if i>1:
            file.write('^'+str(i))
file.write('=0')
file.close



