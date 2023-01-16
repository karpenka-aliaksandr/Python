# 39(1). Создайте программу для игры с конфетами человек против человека. Реализовать игру игрока против игрока в терминале. 
# Игроки ходят друг за другом, вписывая желаемое количество конфет. Первый ход определяется жеребьёвкой. 
# В конце вывести игрока, который победил

# Условие задачи: На столе лежит 221 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 

# В качестве дополнительного усложнения можно:
#         a) Добавьте игру против бота ( где бот берет рандомное количество конфет от 1 до 28)

#         b) Подумайте как наделить бота ""интеллектом"" (есть алгоритм, позволяющий выяснить какое количесвто конфет необходимо 
#         брать, чтобы гарантированно победить, соответственно внедрить этот алгоритм боту )


import random

def maxN(iN):
    if iN>=28:
        return 28
    else:
        return iN

def botMove(iModeGame,iN):
    if iModeGame == 2:
        if iN>57 or iN==29:
            tookCandy = random.randint(1,maxN(iN))
        elif iN>28:
            tookCandy = iN-29
        else:
            tookCandy = iN
    else: 
        if iN>28:
            tookCandy = (iN) % 29
            if tookCandy == 0:
                tookCandy = random.randint(1,maxN(iN))
        else:
            tookCandy = iN
    print(f'BOT взял {tookCandy} конфет.')
    return tookCandy
   
print()
print()
print('Игра. Есть N конфет, два игрока по очереди берут от 1 до 28 конфет. Выигрывает игрок, взявший последнюю конфету.')
lNames=[]
print()

print('Выберите режим игры: ')
print('1. Игрок против игрока.')
print('2. Игрок против "слабого" бота.')
print('3. Игрок против "сильного" бота.')
while True:
    sModeGame = input()
    if sModeGame.isdigit():
        iModeGame=int(sModeGame)
        if iModeGame>=1 and iModeGame<=3:
            break
    print('Вы выбрали неправильный режим. ')
if iModeGame == 1:
    lNames.append(input('Введите имя первого игрока: '))
    lNames.append(input('Введите имя второго игрока: '))
else:
    lNames.append(input('Введите имя игрока: '))
    lNames.append('BOT')
while True:
    iN=int(input('Введите начальное количество конфет в диапазоне 221 - 555: '))
    if iN>=221 and iN<=555:
        break
    else:
        print('Вы ввели неправильное количество конфет.')  



iActivPlayer = random.randint(0,1) 
print('Случайно компьютер определил очередность ходов.')
while iN>0:
    print(f'Ход игрока {lNames[iActivPlayer]}. ',end = '')
    if lNames[iActivPlayer] == 'BOT':
        iGiveN = botMove(iModeGame,iN)
    else:
        while True:
            sGiveN = (input(f'{lNames[iActivPlayer]}, cколько конфет Вы желаете взять 1-{maxN(iN)}? '))
            if sGiveN.isdigit():
                iGiveN=int(sGiveN)
                if iGiveN>=1 and iGiveN<=maxN(iN):
                    break
            else:
                print('Вы ввели неправильное количество конфет.')
    iN-=iGiveN
    print(f'В игре осталось {iN} конфет(-а,-ы)')
    if iN==0:
        print(f'{lNames[iActivPlayer]} выйграл(-а). Поздравляем победителя.')
    else:
        iActivPlayer = 1- iActivPlayer
    



