# Задайте натуральное число N. Напишите программу, 
# которая составит список простых множителей числа N.

n = int(input('Введите натуральное число: '))
prost_mn = []
prost = 2
while prost <= n:
    while n % prost == 0:
        prost_mn.append(prost)
        n /= prost
    while True:
        count = 0
        prost += 1
        for i in range(1,prost+1):
            if prost % i == 0:
                count += 1
        if count == 2:
            break 
print(f'Простые множители числа равны: {prost_mn}')