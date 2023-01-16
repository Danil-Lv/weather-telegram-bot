from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
b1 = KeyboardButton(text='Get weather')
kb.add(b1)
