import telebot
from telebot import types
import random

sweetsGameOn: bool = False
iModeGame: int = 0  # 2-слыбый бот. 3-сильный бот.
bot = telebot.TeleBot("5988956202:AAGj8irBsJeWefJXeozx9R-5NUAWXic1Nak")
iN: int = 221
iGiveN: int = 0
iActivPlayer: int = 0

@bot.message_handler(commands=["start"])
def start(message):
    rem = types.ReplyKeyboardRemove()
    bot.send_message(
        message.chat.id, "Хотите сыграть в конфетки? нажмите:\n/sweets", reply_markup=rem)

@bot.message_handler(commands=["sweets"])
def sweets(message):
    global sweetsGameOn,iN
    sweetsGameOn = True
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, is_persistent=False)
    but1 = types.KeyboardButton("Правила")
    but2 = types.KeyboardButton("Играть")
    but3 = types.KeyboardButton("Выход")
    markup.add(but1, but2, but3)
    bot.send_message(message.chat.id, 'Выберите ниже:', reply_markup=markup)

@bot.message_handler(content_types="text")
def get_text_messages(message):  
    global sweetsGameOn
    global iModeGame, iN
    if sweetsGameOn: 
        if message.text == "Выход":
            rem = types.ReplyKeyboardRemove()
            sweetsGameOn = False
            bot.send_message(message.chat.id, "Вы вышли из игры.", reply_markup=rem)
        elif message.text == "Правила":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, is_persistent=False)
            but2 = types.KeyboardButton("Играть")
            but3 = types.KeyboardButton("Выход")
            markup.add(but2, but3)
            bot.send_message(message.chat.id,
                             "Вот правила.\nНа столе лежит 221 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.",
                             reply_markup=markup)
        elif message.text == "Играть" or message.text == "Начать игру сначала":
            iN=221
            markup = types.ReplyKeyboardMarkup(
                resize_keyboard=True, is_persistent=False)
            but0 = types.KeyboardButton("Правила")
            but1 = types.KeyboardButton('"Слабый" BOT')
            but2 = types.KeyboardButton('"Сильный" BOT')
            but3 = types.KeyboardButton("Выход")
            markup.add(but0,but1, but2, but3)
            bot.send_message(message.chat.id, "Выберите режим игры", reply_markup=markup)
        elif message.text == '"Слабый" BOT':
            bot.send_message( message.chat.id, 'Выбран режим игры со "слабым" ботом.')
            # message.text = None
            iModeGame = 2
            sweetGame(message)
        elif message.text == '"Сильный" BOT':
            bot.send_message(message.chat.id, 'Выбран режим игры с "сильным" ботом.')
            # message.text = None
            iModeGame = 3
            sweetGame(message)
    
def sweetGame(message):
    global iN, iActivPlayer,iGiveN
    iActivPlayer = random.randint(0, 1)  # 0 - игрок, 1 - ВОТ
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True,is_persistent = False)
    but2 = types.KeyboardButton("Начать игру сначала")
    but3 = types.KeyboardButton("Выход")
    markup.add(but2,but3)
    bot.send_message(message.chat.id, 'Случайно компьютер определил очередность ходов.')
    turns(message)
    return

def turns(message):
    global iN, iGiveN, iActivPlayer
    if iN > 0:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True,is_persistent = False)
        but2 = types.KeyboardButton("Начать игру сначала")
        but3 = types.KeyboardButton("Выход")
        markup.add(but2,but3)
        bot.send_message(message.chat.id, f'На столе {iN} конфет(-а,-ы)',reply_markup=markup)
        if iActivPlayer:
            botTurn(message)
        else:
            bot.send_message(message.chat.id, f'Cколько конфет Вы желаете взять 1-{maxN(iN)}? ')
            bot.register_next_step_handler(message,user_input)
    else:
        if not iActivPlayer:
            bot.send_message(
                message.chat.id, f'BOT выйграл. Поздравляем победителя.')
        else:
            bot.send_message(
                message.chat.id, f'Bы выйграли. Поздравляем победителя.')
        return

def user_input(message):
    global iGiveN, iN, iActivPlayer
    if message.text == "Начать игру сначала" or message.text == "Выход":
        get_text_messages(message)
        return
    if message.text.isdigit():
        iGiveN = int(message.text)
        if iGiveN >= 1 and iGiveN <= maxN(iN):
            iN -= iGiveN
            iActivPlayer = 1 - iActivPlayer
            turns(message)
            return
    bot.send_message(message.chat.id, f'Вы ввели неправильное количество конфет.')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True,is_persistent = False)
    but2 = types.KeyboardButton("Начать игру сначала")
    but3 = types.KeyboardButton("Выход")
    markup.add(but2,but3)
    bot.send_message(message.chat.id, f'На столе {iN} конфет(-а,-ы)',reply_markup=markup)
    bot.send_message(message.chat.id, f'Cколько конфет Вы желаете взять 1-{maxN(iN)}? ')
    bot.register_next_step_handler(message, user_input)


def maxN(iN):
    if iN >= 28:
        return 28
    else:
        return iN

def botTurn(message):
    global iModeGame, iN, iGiveN, iActivPlayer
    if iModeGame == 2:
        if iN > 57 or iN == 29:
            tookCandy = random.randint(1, maxN(iN))
        elif iN > 28:
            tookCandy = iN-29
        else:
            tookCandy = iN
    else:
        if iN > 28:
            tookCandy = (iN) % 29
            if tookCandy == 0:
                tookCandy = random.randint(1, maxN(iN))
        else:
            tookCandy = iN
    iGiveN = tookCandy
    bot.send_message(message.chat.id, f'Ход ВОТа')
    bot.send_message(message.chat.id, f'BOT взял {iGiveN} конфет.')
    iN -= iGiveN
    iActivPlayer = 1 - iActivPlayer
    turns(message)

bot.infinity_polling()
