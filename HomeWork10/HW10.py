# 1. Прикрутить бота к задачам с предыдущего семинара:
#     1. **Создать калькулятор для работы с рациональными и комплексными числами, организовать меню**


import telebot

from telebot import types
bot = telebot.TeleBot("5988956202:AAGj8irBsJeWefJXeozx9R-5NUAWXic1Nak")
typeNums = 0
calcOn = False


@bot.message_handler(commands=["start"])
def start(message):
    rem = types.ReplyKeyboardRemove()
    bot.send_message(message.chat.id, "Хотите запустить калькулятор? Нажмите:\n/calc", reply_markup=rem)
@bot.message_handler(commands=["calc"])
def calc(message):
    global calcOn
    calcOn = True
    mrk = types.ReplyKeyboardMarkup(resize_keyboard=True)
    key1 = types.KeyboardButton('Рациональные')
    key2 = types.KeyboardButton('Комплексные')
    key3 = types.KeyboardButton('Выход')
    mrk.add(key1, key2, key3)
    bot.send_message(message.chat.id, f'Калькулятор \nСделайте выбор, с какими числами работать', reply_markup=mrk)

@bot.message_handler(content_types=['text'])
def buttons(message):
    global typeNums
    global calcOn
    if calcOn:
        rem = types.ReplyKeyboardRemove()
        mrk = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key3 = types.KeyboardButton('Выход')
        mrk.add(key3)
        if message.text == 'Рациональные':
            bot.send_message(message.chat.id, f'Выбран режим рациональных чисел', reply_markup=mrk)
            bot.send_message(message.chat.id, f'Введите выражение разделяя пробелом по примеру <float + float>')
            typeNums = 0
            bot.register_next_step_handler(message, controller)
        elif message.text == 'Комплексные':
            bot.send_message(message.chat.id, f'Выбран режим комплексных чисел', reply_markup=mrk)
            bot.send_message(message.chat.id, f'Введите выражение разделяя пробелом по примеру <complex / complex>')
            typeNums = 1
            bot.register_next_step_handler(message, controller)
        elif message.text == 'Выход':
            calcOn = False
            bot.send_message(message.chat.id, f'Вы вышли из программы.\nДля повторного входа нажмите: /calc', reply_markup=rem)

def controller(message):
    if message.text == "Выход":
        buttons(message)
        return
    line = message.text.strip().split()
    allOk = True
    znak = ''
    if len(line) == 3:
        znak = line[1]
        if typeNums == 0:
            try:
                a = float(line[0])
                b = float(line[2])
            except ValueError:
                allOk = False
        else:
            try:
                a = complex(line[0])
                b = complex(line[2])
            except ValueError:
                allOk = False
    if not allOk:
        mrk = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key3 = types.KeyboardButton('Выход')
        mrk.add(key3)
        bot.send_message(message.chat.id, f'Введены неправильные числа или выражение.\n Повторите',reply_markup=mrk)
        bot.register_next_step_handler(message, controller)
        return
    if znak == '+':
        res = summ_nums(a, b)
    elif znak == '-':
        res = sub_nums(a, b)
    elif znak == '*':
        res = mult_nums(a, b)
    elif znak == '/':
        res = div_nums(a, b)
    elif typeNums == 1 and (znak == '//' or znak == '%'):
        bot.send_message(message.chat.id, f'Для комплексных чисел данное действие не применимо.\n Повторите')
        bot.register_next_step_handler(message, controller)
        return
    elif znak == '//':
        res = div_int(a, b)
    elif znak == '%':
        res = div_rem(a, b)
    else: 
        bot.send_message(message.chat.id, f'Неправильно введен знак.\n Повторите')
        bot.register_next_step_handler(message, controller)
        return
    bot.send_message(message.chat.id, str(res))
    calc(message)

    
def summ_nums(a, b):
    return a + b


def sub_nums(a, b):
    return a - b


def mult_nums(a, b):
    return a * b


def div_nums(a, b):
    return a / b


def div_int(a, b):
    return a // b


def div_rem(a, b):
    return a % b


bot.infinity_polling()