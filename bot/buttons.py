from telebot import *
from .text import *

def city_btn(m):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    for i in range(len(m)):
        btn = types.KeyboardButton(m[i][0])
        btn1 = types.KeyboardButton(m[i][1])
        markup.add(btn, btn1)
    return markup


def base_btn():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn = types.KeyboardButton("Buyurtma qilish")
    btn1 = types.KeyboardButton("Buyurtmalarim")
    btn2 = types.KeyboardButton("EVOS Oilasi")
    btn3 = types.KeyboardButton("Izoh")
    btn4 = types.KeyboardButton("Sozlamlar")

    markup.add(btn)
    markup.add(btn1, btn2)
    markup.add(btn3, btn4)
    return markup
















