import config
import database_creator
import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart, Command

bot_token = config.bot_token
bot = Bot(token=bot_token)
dp = Dispatcher()
database_creator.create_db()


@dp.message(CommandStart())
async def start(message: types.Message):
    if 1 == 1: #проверка на существующую регистрацию
        quests = ('')
    reply_keyboard = types.ReplyKeyboardMarkup(keyboard=[
    [types.KeyboardButton(text='Очереди'),
     types.KeyboardButton(text='Управление очередями'),],
    [types.KeyboardButton(text='Помощь')]],
    resize_keyboard=True, input_field_placeholder='Выберите кнопку')

    await message.answer(text=f'Привет, {message.from_user.first_name}!', reply_markup=reply_keyboard)



@dp.message(Command('help'))
async def help_bot(message: types.Message):
    await message.answer(text='Помощь')


@dp.message()
async def echo_mes(message: types.Message):
    await message.answer(text='Я не понимаю тебя :(')


async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
