from aiogram import types, Dispatcher
from telegram_bot.create_bot import bot
from telegram_bot.keyboards import kb_client
from telegram_bot.data_base import sqlite_db
from aiogram.types import ReplyKeyboardRemove


# @dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    try:
        await bot.send_message(message.from_user.id, 'В дальнейшем я буду вам помогать', reply_markup=kb_client)
        await message.delete()
    except Exception as e:
        await message.reply('Общение с ботом возможно только через ЛС')
        print(e)


# @dp.message_handler(commands=['Режим_работы'])
async def time_work_bot(message: types.Message):
    await bot.send_message(message.from_user.id, 'Когда мой создатель соизволит запустить меня(')


# @dp.message_handler(commands=['Для_чего_был_создан'])
async def dream_test(message: types.Message):
    await bot.send_message(message.from_user.id,
                           'Я первый тестовый образец моего создателя, захотевшего создать своего бота')


# @dp.message_handler(commands=['Меню'])
async def bot_menu_command(message: types.Message):
    await sqlite_db.sql_read(message)


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(time_work_bot, commands=['Режим_работы'])
    dp.register_message_handler(dream_test, commands=['Для_чего_был_создан'])
    dp.register_message_handler(bot_menu_command, commands=['Меню'])
