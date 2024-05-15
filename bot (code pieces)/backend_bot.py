import telebot
from telebot import types

bot = telebot.TeleBot('6492500738:AAFLerBpsh1PEP2jL3WcvJSk-eiS8-YIBUg')


@bot.message_handler(commands=['start'])
def start(message):
    temp = f"Привет, {message.from_user.first_name}!"
    markup = types.ReplyKeyboardMarkup()
    btn_del = types.KeyboardButton('del')
    btn_edit = types.KeyboardButton('edit')
    btn_redirect = types.KeyboardButton('Goto site')
    markup.row(btn_del)
    markup.row(btn_edit, btn_redirect)
    bot.send_message(message.chat.id, temp, reply_markup=markup)
    bot.register_next_step_handler(message, on_click)

def on_click(message):
    if message.text == 'del':
        bot.send_message(message.chat.id, 'Delete')
    elif message.text == 'edit':
        bot.send_message(message.chat.id, 'edit')


@bot.message_handler(commands=['b'])
def bnt_panel(message):
    temp = f"Привет, {message.from_user.first_name}!"
    markup = types.InlineKeyboardMarkup()
    btn_del = types.InlineKeyboardButton('del', callback_data='delete')
    btn_edit = types.InlineKeyboardButton('edit', callback_data='edit')
    btn_redirect = types.InlineKeyboardButton('Goto site', url='google.com')
    markup.row(btn_del)
    markup.row(btn_edit, btn_redirect)
    bot.send_message(message.chat.id, temp, reply_markup=markup)



@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id)
    elif callback.data == 'edit':
        bot.edit_message_text('edited', callback.message.chat.id, callback.message.message_id)





@bot.message_handler() # Обязательно внизу
def error(message):
    temp = "Я не знаю такой команды"
    bot.send_message(message.chat.id, temp)


bot.infinity_polling()