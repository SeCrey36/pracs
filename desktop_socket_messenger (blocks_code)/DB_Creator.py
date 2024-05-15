import sqlite3
import os

def createdb():
    cu.execute('PRAGMA foreign_keys = 1')
    con.commit()

    cu.execute('''CREATE TABLE IF NOT EXISTS users(
    userid INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, 
    mail TEXT NOT NULL UNIQUE,
    nickname TEXT NOT NULL,
    online INTEGER NOT NULL,
    last_online TEXT,
    pass_hash TEXT NOT NULL,
    role TEXT NOT NULL
    )''')
    con.commit()

    cu.execute('''CREATE TABLE IF NOT EXISTS chats(
    chatid INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, 
    type INTEGER NOT NULL,
    namechat TEXT,
    date_create TEXT NOT NULL,
    photo_link TEXT,
    admin_chat TEXT
    )''')
    con.commit()

    cu.execute('''CREATE TABLE IF NOT EXISTS messages(
    messid INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE, 
    send_time TEXT NOT NULL,
    read INTEGER NOT NULL,
    deleted INTEGER NOT NULL,
    sender_id INTEGER NOT NULL,
    chat_id INTEGER NOT NULL,
    foreign key (sender_id) references users (userid),
    foreign key (chat_id) references chats (chatid)
    )''')
    con.commit()

    cu.execute('''CREATE TABLE IF NOT EXISTS users_have_chats(
    user_id INTEGER NOT NULL, 
    chat_id INTEGER NOT NULL,
    foreign key (user_id) references users (userid),
    foreign key (chat_id) references chats (chatid)
    )''')
    con.commit()


def inputdb():
    for i in range(10):
        mail = str(i) + 'user@gmail.com'
        nickname = 'nick' + str(i)
        online = 0
        last_online = '10.10.20'
        pass_hash = 'hqwbhjbf98247981247nmdf'
        role = 'user'

        sqlite_insert_temp = """INSERT INTO users(mail, nickname, online, last_online, pass_hash, role) 
        VALUES (?, ?, ?, ?, ?, ?)"""

        data_temp = (mail, nickname, online, last_online, pass_hash, role)
        cu.execute(sqlite_insert_temp, data_temp)
        con.commit()

def printdate():
    cu.execute("SELECT * FROM users")
    rows = cu.fetchall()
    for row in rows:
        print(row)

def dropdb():
    os.remove('mess.db')

try:
    con = sqlite3.connect('mess.db')
    cu = con.cursor()
    print('Connection!')
except:
    print('ERR while create connection')
### FUNCTIONS CALL ###


### FUNCTIONS CALL ###
con.close()

#dropdb()