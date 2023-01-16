# 38. Напишите программу, удаляющую из текста все слова, содержащие "абв".


data = 'аф фыв ыва ываабв, ывадлойц. Оывало абвываф, длоываабв.'

# Способ 1.

# data_slova= data.split()
# data_slova_without = ''
# for slovo in data_slova:
#     if not 'абв' in slovo:
#         data_slova_without += slovo + ' '
# print(data_slova_without)

# Способ 2.

data=' '.join(list(filter(lambda slovo: not 'абв' in slovo, data.split())))
print(data)