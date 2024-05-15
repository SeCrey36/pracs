import telebot
import sqlite3
from telebot import types


bot = telebot.TeleBot('6492500738:AAFLerBpsh1PEP2jL3WcvJSk-eiS8-YIBUg')


@bot.message_handler(commands=['start'])
def start(message):
    conn = sqlite3.connect('db.sql')
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_incriment primary key, name varchar(50), pass varchar(50))')
    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(message.chat.id, 'Hello, lets register u. Input name')
    bot.register_next_step_handler(message, reg)


def reg(message):
    name = message.text.strip()
    bot.send_message(message.chat.id, 'Input pass')
    password = message.text.strip()

    conn = sqlite3.connect('db.sql')
    cur = conn.cursor()

    cur.execute(f"INSERT INTO users (name, pass) VALUES ('{name}', '{password}')")
    conn.commit()
    cur.close()
    conn.close()

    temp = 'Registered!'
    markup = types.InlineKeyboardMarkup()
    btn_show_users = types.InlineKeyboardButton('show all users', callback_data='all_users')
    markup.row(btn_show_users)
    bot.send_message(message.chat.id, temp, reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    conn = sqlite3.connect('db.sql')
    cur = conn.cursor()

    cur.execute(f"SELECT * FROM users")
    users = cur.fetchall()
    info = ''
    for i in users:
        info += f'Name: {i[1]}, pass: {i[2]}\n'
    cur.close()
    conn.close()

    bot.send_message(call.message.chat.id, info)




bot.infinity_polling()