# Вариант 1
# f = open('num.txt','r')
# numb = [(int(i),int(i)**2) for i in (list(f.read().split())) if int(i)%2 == 0]
# print(numb)
# f.close



# Вариант 2
def select(f,col):
    return [f(x) for x in col]


def where(f,col):
    return [x for x in col if f(x)]




f = open('num.txt','r')
data = list(f.read().split())
f.close
data = select(int,data)
data = where(lambda x: x%2 == 0, data)
data = select(lambda x: (x, x**2),data)
print(data)