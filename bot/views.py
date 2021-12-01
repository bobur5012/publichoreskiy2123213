import telebot
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User
from .buttons import *
from .text import *

bot = TeleBot("2078494870:AAHzAvPN3cHCSul8V__6JvqmhtT4w8SN_c0")


@csrf_exempt
def index(request):
    if request.method == 'GET':
        return HttpResponse("<a href='http://t.me/dkarimoff96'>Created by</>")
    if request.method == 'POST':
        bot.process_new_updates([
            telebot.types.Update.de_json(
                request.body.decode("utf-8")
            )
        ])
        return HttpResponse(status=200)


@bot.message_handler(commands=["start"])
def start(message):
    text = f'Assalomu alaykum {message.from_user.first_name}. Men Evos yetkazib berish xizmati botiman!\n Привет Doniyor! Я бот службы доставки Evos!\n Hi Doniyor! I am Evos delivery service bot!'
    bot.send_message(message.chat.id, text)
    text1 = "Muloqot tilini tanlang\n Выберите язык\n Select Language"
    markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
    btn = types.KeyboardButton("O'zbekcha")
    btn1 = types.KeyboardButton("Русский")
    btn2 = types.KeyboardButton("English")
    markup.add(btn, btn1, btn2)
    bot.send_message(message.chat.id, text1, reply_markup=markup)

    bot_user = User.objects.create(
        user_id=message.from_user.id,
        first_name=message.from_user.first_name,
        user_name=message.from_user.username,
        last_name=message.from_user.last_name,
        step=1
    )
    bot_user.save()




@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot_user = User.objects.get(user_id=message.chat.id)
    if message.text == "O'zbekcha":

        markup = city_btn(city)
        bot.send_message(message.chat.id, "Shaharni tanlang", reply_markup=markup)
        bot_user = User.objects.get(user_id=message.chat.id)
        if bot_user.step == 1:
            bot_user.lang = message.text
            bot_user.step += 1
            bot_user.save()

    if message.text in city1:
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        btn = types.KeyboardButton("Share my contacts", request_contact=True)
        markup.add(btn)
        bot.send_message(message.chat.id, "Ro'yxatga olish uchun telefon raqamingizni kiriting! \n Masalan +998xx xxx xx xx", reply_markup=markup)
        bot_user = User.objects.get(user_id=message.chat.id)
        if bot_user.step == 2:
            bot_user.city = message.text
            bot_user.step += 1
            bot_user.save()

    elif message.text == 'Orqaga':
        print(len(bot_user.latitude))
        if len(bot_user.latitude)>0 and len(bot_user.longitude)>0:
            btn = types.KeyboardButton("Menu")
            markup = base_btn()
            markup.add(btn)
            bot.send_message(message.chat.id, "birini tanlang", reply_markup=markup)
        else:
            markup = base_btn()
            bot.send_message(message.chat.id, "birini tanlang", reply_markup=markup)

    elif message.text == "Buyurtma qilish":
        bot_user = User.objects.get(user_id=message.chat.id)
        bot_user.step = 5
        bot_user.save()
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        btn = types.KeyboardButton("Share my location", request_location=True)
        btn2 = types.KeyboardButton("Orqaga")
        markup.add(btn, btn2)
        bot.send_message(message.chat.id, "Eltib berish uchun geo-joylashuvni jo'nating yoki manzilni tanlang", reply_markup=markup)

    elif message.text == "Buyurtmalarim":
        bot.send_message(message.chat.id, "Siz hali hanuz birorta ham buyurtma bermagansiz.")
    elif message.text == "Izoh":
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        btn = types.KeyboardButton("Orqaga")
        markup.add(btn)
        bot.send_message(message.chat.id, "Fikr va mulohazalaringizni yuboring", reply_markup=markup)
    elif message.text == "EVOS Oilasi":
        bot_user = User.objects.get(user_id=message.chat.id)
        bot_user.step = 6
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        btn = types.KeyboardButton("Orqaga")
        bot_user.step += 1
        bot_user.save()
        markup.add(btn)
        bot.send_message(message.chat.id, "Ismingizni kiriting", reply_markup=markup)

    elif message.text == "Sozlamlar":
        markup = types.InlineKeyboardMarkup(row_width=3)
        btn = types.InlineKeyboardButton("Muloqot tili", callback_data='1')
        btn2 = types.InlineKeyboardButton("Shahar", callback_data="2")
        btn3 = types.InlineKeyboardButton("Telefon", callback_data='3')
        markup.add(btn, btn2, btn3)
        bot.send_message(message.chat.id, "Muloqot tili: 🇺🇿 O'zbekcha \n Shahar: Farg'ona \n Telefon: +998908356595 \n Quyidagilardan birini tanlang",
                         reply_markup=markup)

    elif bot_user.step == 8:
        bot_user.birth_date = message.text
        bot_user.step += 1
        bot_user.save()
        bot.send_message(message.chat.id, "Tabriklaymiz! \n Siz EVOS oilasiga a`zo bo`ldingiz!")

        markup = base_btn()

        bot.send_message(message.chat.id, "birini tanlang", reply_markup=markup)
    elif message.text == "Menu":
        bot_user.step = 10
        img_url = "https://cityrating.uz/wp-content/uploads/2018/10/evos1.jpg"

        markup = types.InlineKeyboardMarkup(row_width=2)
        btn = types.InlineKeyboardButton("Barcha menular", url="https://telegra.ph/EVOS-MENU-04-05-5")
        btn2 = types.InlineKeyboardButton("Set", url="https://telegra.ph/EVOS-MENU-04-05-5")
        btn3 = types.InlineKeyboardButton("Lavash", url="https://telegra.ph/EVOS-MENU-04-05-5")
        btn4 = types.InlineKeyboardButton("Boshqa", url="https://telegra.ph/EVOS-MENU-04-05-5")
        btn5 = types.InlineKeyboardButton("Shaurma", url="https://telegra.ph/EVOS-MENU-04-05-5")
        btn6 = types.InlineKeyboardButton("Donar", url="https://telegra.ph/EVOS-MENU-04-05-5")
        btn7 = types.InlineKeyboardButton("Burger", url="https://telegra.ph/EVOS-MENU-04-05-5")
        btn8 = types.InlineKeyboardButton("Hot-dog", url="https://telegra.ph/EVOS-MENU-04-05-5")
        btn9 = types.InlineKeyboardButton("Desertlar", url="https://telegra.ph/EVOS-MENU-04-05-5")
        btn10 = types.InlineKeyboardButton("Ichimliklar", url="https://telegra.ph/EVOS-MENU-04-05-5")
        btn11 = types.InlineKeyboardButton("Gazaklar", url="https://telegra.ph/EVOS-MENU-04-05-5")
        markup.add(btn, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11)
        bot.send_photo(message.chat.id, photo=img_url,
                       caption='Kategoriyalardan birini tanlang!',
                       reply_markup=markup)
    else:
        bot_user = User.objects.get(user_id=message.chat.id)
        if bot_user.step == 7:
            bot_user.first_name = message.text
            bot_user.step += 1
            bot_user.save()
            bot.send_message(message.chat.id, "Tug'ilgan kuningizni kiriting.\n Masalan 2000-12-20")


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == "1":
        markup = types.InlineKeyboardMarkup(row_width=3)
        btn = types.InlineKeyboardButton("O`zbekcha", callback_data='uz')
        btn2 = types.InlineKeyboardButton("Русский", callback_data="ru")
        btn3 = types.InlineKeyboardButton("English", callback_data='en')
        markup.add(btn, btn2, btn3)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Quyidagilardan birini tanlang", reply_markup=markup)
    elif call.data == "uz":
        bot_user = User.objects.get(user_id=call.message.chat.id)
        bot_user.lang = "O`zbekcha"
        bot_user.save()
        bot.send_message(call.message.chat.id, "TIl o`zgardi")

    elif call.data == "ru":
        bot_user = User.objects.get(user_id=call.message.chat.id)
        bot_user.lang = call.message.json['reply_markup']['inline_keyboard'][0][1]['text']
        bot_user.save()
        bot.send_message(call.message.chat.id, "Язык изменён")
    elif call.data == "en":
        bot_user = User.objects.get(user_id=call.message.chat.id)
        bot_user.lang = call.message.json['reply_markup']['inline_keyboard'][0][2]['text']
        bot_user.save()
        bot.send_message(call.message.chat.id, "Language has changed")
    elif call.data == "2":
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn = types.InlineKeyboardButton("TOSHKENT", callback_data="T")
        btn1 = types.InlineKeyboardButton("FERGANA", callback_data="F")
        btn2 = types.InlineKeyboardButton("QIRGULI", callback_data="Qir")
        btn3 = types.InlineKeyboardButton("QASHADARYO", callback_data="Qash")
        btn4 = types.InlineKeyboardButton("ANDIJON", callback_data="A")
        btn5 = types.InlineKeyboardButton("QO`QON", callback_data="Qo")
        btn6 = types.InlineKeyboardButton("NAMANGAN", callback_data="N")
        btn7 = types.InlineKeyboardButton("SAMARQAND", callback_data="S")
        markup.add(btn, btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Quyidagilardan birini tanlang", reply_markup=markup)
    elif call.data == "3":
        markup = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
        btn = types.KeyboardButton("Share my contacts", request_contact=True)
        btn2 = types.KeyboardButton("Orqaga")
        markup.add(btn, btn2)
        bot.send_message(call.chat.id, "TIl o`zgardi", reply_markup=markup)


@bot.message_handler(content_types='contact')
def contact(message):

    markup = types.InlineKeyboardMarkup(row_width=1)
    btn = types.InlineKeyboardButton("Qoidalarni o`qish", url='http://google.com')
    markup.add(btn)
    img_url = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQcG1-QmRv39obLo-jVCQz5qM4NghvTx_MbNQ&usqp=CAU"
    bot.send_photo(message.chat.id, photo=img_url, caption='Davom ettirishdan oldin qoidalar bilan tanishib chiqing!',
                   reply_markup=markup)
    markup = base_btn()
    bot.send_message(message.chat.id, "Ro`yhatdan muvaffaqiyatli o`tdingiz", reply_markup=markup)
    bot_user = User.objects.get(user_id=message.chat.id)
    if bot_user.step == 3:
        bot_user.phone_number = message.contact.phone_number
        bot_user.step += 1
        bot_user.save()

@bot.message_handler(content_types="location")
def location(message):

    bot_user = User.objects.get(user_id=message.chat.id)
    if bot_user.step == 5:
        bot_user.longitude = message.location.longitude
        bot_user.latitude = message.location.latitude
        bot_user.step += 1
        bot_user.save()
        btn = types.KeyboardButton("Menu")
        markup = base_btn()
        markup.add(btn)
        bot.send_message(message.chat.id, "birini tanlang", reply_markup=markup)
