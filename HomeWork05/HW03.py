# 39(2). Создайте программу для игры в ""Крестики-нолики"". Игра реализуется в терминале, игроки ходят поочередно, 
# необходимо вывести карту(как удобнее, можно например в виде списка, внутри которого будут 3 списка по 3 элемента, 
# каждый из которого обозначает соответсвующие клетки от 1 до 9), сделать проверку не занята ли клетка, на которую 
# мы хотим поставить крестик или нолик, и проверку на победу( стоят ли крестики или нолик в ряд по диагонали, вертикали, горизонтали)

import random
from os import system, name  
 
def clear():  
    if name == 'nt':  
        _ = system('cls')  
    else:  
        _ = system('clear')  

def end(i):
    if (i+1) % 3 == 0:
        return '\n'
    else:
        return ''
        
def printPole(lPole):
    clear()  
    for i in range(9):
        if lPole[i] == 0:
            print('_ ',end = end(i))
        elif lPole[i] == 1:
            print('X ', end = end(i))
        else:
            print('0 ', end = end(i))

def isHorizontal(lPole):
    bFlag = False
    for i in range(3):
        if lPole[i*3] != 0 and lPole[i*3] == lPole[i*3+1] and lPole[i*3+1] == lPole[i*3+2]:
            bFlag = True
    return  bFlag
def isVertical(lPole):
    bFlag = False
    for i in range(3):
        if lPole[i] != 0 and lPole[i] == lPole[i+3] and lPole[i+3] == lPole[i+6]:
            bFlag = True
    return  bFlag
def isDiagonal(lPole):
    bFlag = False
    if lPole[4] != 0 and (lPole[0] == lPole[4] and lPole[4] == lPole[8] or lPole[2] == lPole[4] and lPole[4] == lPole[6]):
        bFlag = True
    return  bFlag

def isWinner(lPole):
    bFlag = False
    if isHorizontal(lPole) or isVertical(lPole) or isDiagonal(lPole):
        bFlag = True
    return  bFlag


lPole = [0,0,0,0,0,0,0,0,0]

print('Игра "Крестики-нолики"')
lNames=[]
print()
lNames.append(input('Введите имя первого игрока: '))
lNames.append(input('Введите имя второго игрока: '))
iActivPlayer = random.randint(0,1) 
iLabel=1
print('Случайно компьютер определил очередность ходов.')
bFlagWin=True
while bFlagWin:
    print()
    printPole(lPole)
    print()
    print(f'Ход игрока {lNames[iActivPlayer]}. ')
    while True:
        sMove = (input(f'{lNames[iActivPlayer]}, в какую ячейку хотите походить 1-9? '))
        if sMove.isdigit():
            iMove=int(sMove)
            if iMove>=1 and iMove<=9 and lPole[iMove-1] == 0:
                break
            else:
                print('Вы ввели неправильное число или поле занято.')
    lPole[iMove-1] = iLabel
    print()
    printPole(lPole)
    print()

    if isWinner(lPole):
        bFlagWin=False
        print(f'{lNames[iActivPlayer]} выйграл(-а). Поздравляем победителя.')
        print()
    if not 0 in lPole:
        print('Игроки сыграли вничью')  
        print()
        bFlagWin=False  
    iActivPlayer = 1 - iActivPlayer
    iLabel = 3 - iLabel

  
    















