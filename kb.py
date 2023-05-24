from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton

from configurebot import cfg

mainmenunewsupport = KeyboardButton(cfg['button_new_question'])
mainmenuabout = KeyboardButton(cfg['button_about_us'])
mainmenuauthor = KeyboardButton(cfg['button_author'])
mainmenu = ReplyKeyboardMarkup(resize_keyboard=True).row(mainmenunewsupport, mainmenuabout, mainmenuauthor)