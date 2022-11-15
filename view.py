# сюда все функции отправляющие сообщения

from aiogram import types

import model
from bot import bot

async def helloUser(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f'{message.from_user.first_name}, привет!\n'
                           f'Это игра в конфетки. Если хочешь сыграть, введи /rules '
                           f'и я расскажу тебе правила игры.')

async def goodbye(message: types.Message):
    await bot.send_message(message.from_user.id,
                        f'{message.from_user.first_name}, '
                        f'пока!')

async def regulations(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f'У нас есть {model.total_candy} конфет.\n '
                           'Мы по очереди берем конфеты.\n'
                           'За один ход можно взять не более чем 28 конфет.\n'
                           'Выйграет тот, кто заберет последние конфеты!\n'
                           'Чтобы начать введи /go.')

async def gogame(message: types.Message):
    await bot.send_message(message.from_user.id, 'Так и быть делай первый ход.')
