from aiogram.types import ReplyKeyboardMarkup, KeyboardButton  # , ReplyKeyboardRemove

b1 = KeyboardButton('/Режим_работы')
b2 = KeyboardButton('/Для_чего_был_создан')
# b3 = KeyboardButton('/что-то')
b4 = KeyboardButton('Скинуть свой номер', request_contact=True)
b5 = KeyboardButton('Скинуть геолокацию', request_location=True)
# b6 = KeyboardButton('Скинуть профиль', request_user=True)
kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_client.add(b2).insert(b1).row(b4, b5)
