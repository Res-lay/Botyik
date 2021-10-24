# -*- coding: utf-8 -*-
import random
from telebot import *    


token = '2017299699:AAFVBg7vBhFaabAZQPGG8CBS76_ZWkcboss'
bot = telebot.TeleBot(token)

first = ["Сегодня — идеальный день для новых начинаний.","Оптимальный день для того, чтобы решиться на смелый поступок!","Будьте осторожны, сегодня звёзды могут повлиять на ваше финансовое состояние.","Лучшее время для того, чтобы начать новые отношения или разобраться со старыми.","Плодотворный день для того, чтобы разобраться с накопившимися делами."]
second = ["Но помните, что даже в этом случае нужно не забывать про","Если поедете за город, заранее подумайте про","Те, кто сегодня нацелен выполнить множество дел, должны помнить про","Если у вас упадок сил, обратите внимание на","Помните, что мысли материальны, а значит вам в течение дня нужно постоянно думать про"]
second_add = ["отношения с друзьями и близкими.","работу и деловые вопросы, которые могут так некстати помешать планам.","себя и своё здоровье, иначе к вечеру возможен полный раздрай.","бытовые вопросы — особенно те, которые вы не доделали вчера.","отдых, чтобы не превратить себя в загнанную лошадь в конце месяца."]
third = ["Злые языки могут говорить вам обратное, но сегодня их слушать не нужно.", "Знайте, что успех благоволит только настойчивым, поэтому посвятите этот день воспитанию духа.", "Даже если вы не сможете уменьшить влияние ретроградного Меркурия, то хотя бы доведите дела до конца.","Не нужно бояться одиноких встреч — сегодня то самое время, когда они значат многое.","Если встретите незнакомца на пути — проявите участие, и тогда эта встреча посулит вам приятные хлопоты."]
emoji = ['⛎','🌌', '✨', '💫', '🔯']

@bot.message_handler(commands=['start'])
# Приветствие
def privet(message):
    hello_word = f'Приветик 😆 \nХочешь узнать гороскоп на сегодня?💖'
    bot.send_message(message.chat.id, hello_word,
                     reply_markup=keyboard())


@bot.message_handler(content_types=['text'])
# Реакция на все запросы пользователя
def reaction(message):
    chat_id = message.chat.id
    if message.text == 'Да❤':
        bot.send_message(chat_id, f'Тогда поехали!🥰 \n Лови свежий гороскоп🤤😱', reply_markup=keyboardzodiak())
    elif message.text == 'Нет😢':
        bot.send_message(chat_id, 'Тогда пока😥')
        bot.send_sticker(chat_id, 'CAACAgIAAxkBAAEDIcFhcxc1x_Md0Sc93aBjYbqqVSLnYAACkwwAAuT2OUlA873wZJq2GSEE')
    elif (message.text == 'Овен♈') or (message.text == 'Телец♉') or (message.text == 'Близнецы♊') or (
            message.text == 'Рак♋') or (message.text == 'Лев♌') or (message.text == 'Дева♍') or (
            message.text == 'Весы♎') or (message.text == 'Скорпион♏') or (message.text == 'Стрелец♐') or (
            message.text == 'Козерог♑') or (message.text == 'Водолей♒') or (message.text == 'Рыбы♓'):
        msg = random.choice(emoji) + ' ' + random.choice(first) + ' ' + random.choice(second) + ' ' + random.choice(second_add) + ' ' + random.choice(third) + ' ' + random.choice(emoji)
        bot.send_message(chat_id, msg, reply_markup=keyboardzodiak())


# Клавиатра при приветсвии
def keyboard():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    btn1 = types.KeyboardButton('Да❤')
    btn2 = types.KeyboardButton('Нет😢')
    markup.add(btn1, btn2)
    return markup


# Клавиатура знаков зодиака
def keyboardzodiak():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    btn1 = types.KeyboardButton('Овен♈')
    btn2 = types.KeyboardButton('Телец♉')
    btn3 = types.KeyboardButton('Близнецы♊')
    btn4 = types.KeyboardButton('Рак♋')
    btn5 = types.KeyboardButton('Лев♌')
    btn6 = types.KeyboardButton('Дева♍')
    btn7 = types.KeyboardButton('Весы♎')
    btn8 = types.KeyboardButton('Скорпион♏')
    btn9 = types.KeyboardButton('Стрелец♐')
    btn10 = types.KeyboardButton('Козерог♑')
    btn11 = types.KeyboardButton('Водолей♒')
    btn12 = types.KeyboardButton('Рыбы♓')
    markup.add(btn1, btn2, btn3)
    markup.add(btn4, btn5, btn6)
    markup.add(btn7, btn8, btn9)
    markup.add(btn10, btn11, btn12)
    return markup


bot.polling(none_stop=True)