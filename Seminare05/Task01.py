# 35. В файле находится N натуральных чисел, записанных через пробел. 
# Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.


f = open ('numbers.txt','r')
data = list(map(int,f.read().split()))
f.close
# data = [3,5,6,7,8]
for i in range(1, len(data)):
    if data[i]-1 != data[i-1]:
        print(data[i]-1)

