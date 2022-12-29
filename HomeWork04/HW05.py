# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

def Step(elem: str):
    if 'x' in elem:
        find = elem.find('^')
        if find >= 0:
            return int(elem[find+1:])
        else:
            return 1
    return 0

def Koef(elem: str):
    if 'x' in elem:
        find = elem.find('*')
        if find >= 0:
            return int(elem[:find])
        else:
            return 1
    return int(elem)


def Iter():
    if step>0:
        if koef>1:
            file_out.write(str(koef)+'*')
        file_out.write('x')
        if step>1:
            file_out.write('^'+str(step))
    else:
        if koef>0:
            file_out.write(str(koef))
    if count1 < len(mn1) or count2 < len(mn2):
        file_out.write('+')
    
def Iter1():
    if step>0:
        if koef > 1:
            file_out.write(str(koef)+'*')
        file_out.write('x')
        if step > 1:
            file_out.write('^'+str(step))
    else:
        if koef > 0:
            file_out.write(str(koef))
    if len(keys) > 0:
        file_out.write('+')

path_in1 = 'mn1.txt'
path_in2 = 'mn2.txt'
path_out = 'sum_mn.txt'

file_in1 = open(path_in1, 'r')
mn1 = list(file_in1.read().replace('=','+').split(sep='+'))
mn1.remove('0')
file_in1.close

file_in2 = open(path_in2, 'r')
mn2 = list(file_in2.read().replace('=','+').split(sep='+'))
mn2.remove('0')
file_in2.close

file_out = open(path_out, 'w')
# count1 = 0
# count2 = 0
# while count1 < len(mn1) and count2 < len(mn2):
#     if Step(mn1[count1]) == Step(mn2[count2]):
#         step = Step(mn1[count1])
#         koef = Koef(mn1[count1]) + Koef(mn2[count2])
#         count1 += 1
#         count2 += 1     
#     elif Step(mn1[count1]) > Step(mn2[count2]):
#         step = Step(mn1[count1])
#         koef = Koef(mn1[count1])
#         count1 += 1
#     else:
#         step = Step(mn2[count2])
#         koef = Koef(mn2[count2])
#         count2 += 1
#     Iter()
# while count1 < len(mn1):
#      step = Step(mn1[count1])
#      koef = Koef(mn1[count1])
#      count1 += 1
#      Iter()
# while count2 < len(mn2):
#     step = Step(mn2[count2])
#     koef = Koef(mn2[count2])
#     count2 += 1
#     Iter()


# Второе решение
dictionary = {}
for item in mn1:
    dictionary[Step(item)]=Koef(item)
for item in mn2:
    if Step(item) in dictionary.keys():
        dictionary[Step(item)]+=Koef(item)
    else:
        dictionary[Step(item)]=Koef(item)
keys = list(dictionary.keys())
while len(keys) > 0:
    step = max(keys)
    keys.remove(step)
    koef=int(dictionary.pop(step))
    Iter1()
file_out.write('=0')
file_out.close
