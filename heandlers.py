# Здесь хранятся хендлеры

from aiogram import Dispatcher

import commands
import view

def registred_handlers(dp: Dispatcher):
    dp.register_message_handler(commands.start, commands=['start'])
    dp.register_message_handler(commands.finish, commands=['finish'])
    dp.register_message_handler(commands.rules, commands=['rules'])
    dp.register_message_handler(commands.go, commands=['go'])

    dp.register_message_handler(view.moveUser)
    dp.register_message_handler(view.moveBot)
