# Вычислить число pi c заданной точностью d

# Пример:
# - при d = 0.001, π = 3.141   10^{-1} ≤ d ≤10^{-10}

#Ряд Грегори
d=float(input('Введите требуемую точность вычисления числа Пи: '))
n=0
s1=0
s2=0
while True:
    n += 1
    s1=s2 + 4 / (2*n-1)
    n += 1
    s2=s1 - 4 / (2*n-1)
    print(s1,s2)
    if s1-s2 < d:
        break
print((int((s1+s2)/2/d))*d)