import sqlite3


def create_db():
    with sqlite3.connect('users_data.db') as connection:
        # Устанавливаем соединение с базой данных
        cursor = connection.cursor()

        # Создаем таблицу Users
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        age INTEGER,
        sex INTEGER,
        find_sex INTEGER,
        about TEXT,
        steam TEXT NOT NULL,
        photo BLOB,
        seen_ids TEXT
        )
        ''')

        # Сохраняем изменения и закрываем соединение
        connection.commit()