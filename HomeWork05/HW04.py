# 40. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Модуль сжатия:
# Для чисел:
# Входные данные:
# 111112222334445
# Выходные данные:
# 5142233415
# Также должно работать и для букв:
# Входные данные:
# AAAAAAFDDCCCCCCCAEEEEEEEEEEEEEEEEE
# Выходные данные:
# 6A1F2D7C1A17E
# (5 - количество единиц, далее сама единица, 4 - количество двоек, далее сама двойка и т.д)
# Модуль восстановления работет в обратную сторону - из строки выходных данных, получить строку входных данных.

# zip

sPathIn = 'TestRLE.txt'
sPathOut = 'TestRLE.rle'

fFileIn = open (sPathIn,'r')
fFileOut = open (sPathOut,'w')
sChar=''
iCharCount=1
bFlag = True
while bFlag:
    sCharRead = fFileIn.read(1)
    if sCharRead == '':
        bFlag = False
    if sCharRead == sChar and iCharCount < 9:
        iCharCount += 1
    else:
        if sChar != '':
            fFileOut.write(sChar+str(iCharCount))
        sChar = sCharRead
        iCharCount = 1
fFileIn.close
fFileOut.close


# unzip
sPathIn = 'TestRLE.rle'
sPathOut = 'TestRLE.out'

fFileIn = open (sPathIn,'r')
fFileOut = open (sPathOut,'w')
bFlag = True
while bFlag:
    sCharRead = fFileIn.read(2)
    if sCharRead == '':
        bFlag = False
    else:
        fFileOut.write(sCharRead[0]*int(sCharRead[1]))
fFileIn.close
fFileOut.close