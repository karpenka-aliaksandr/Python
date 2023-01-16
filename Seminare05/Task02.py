# Дан список чисел. Создайте список, в который попадают числа, описываемые возрастающую последовательность. 
# Порядок элементов менять нельзя.
    
#     *Пример:* 
    
#     [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

def posled(data):
    result = []
    flag = False
    length=len(data)
    for i in range(length-1):
        for j in range(i+1,length):
            if data[j]>data[i]:
                flag = True
                begin = i
                next = j
                break
        if flag:
            break
    if flag: 
        result.append(data[begin])
        result.append(data[next])
        for i in range(next+1,length):
            if data[i]>result[-1]:
                result.append(data[i])
        return result
    else:
        return -1

data = [7, 5, 2, 3, 4, 6, 1, 7]
data_posled = posled(data)
print(data_posled)


