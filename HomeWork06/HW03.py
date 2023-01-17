# Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def ab(a,b):
    if b==0:
        return 1
    if b==1: 
        return a
    if b>1:
        return a*ab(a,b-1)
    if b==-1:
        return 1/a
    if b<-1:
        return (1/a)*ab(a,b+1)


a=2
b=3
print(ab(a,b))