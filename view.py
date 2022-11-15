# сюда все функции отправляющие сообщения
from aiogram import types
import random
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
                           f'У нас есть {model.total_candies} конфет.\n '
                           'Мы по очереди берем конфеты.\n'
                           'За один ход можно взять не более чем 28 конфет.\n'
                           'Выйграет тот, кто заберет последние конфеты!\n'
                           'Чтобы начать введи /go.')

async def goGame(message: types.Message):
    await bot.send_message(message.from_user.id, 'Так и быть делай первый ход.')

async def moveUser(message: types.Message):
    teke_user = int(message.text)
    if int(teke_user) > model.max_candy:
        await bot.send_message(message.from_user.id, 'Эй, ты взял слишком много, не больше 28!!!')
    elif int(teke_user) < model.min_candy:
        await bot.send_message(message.from_user.id, 'Ничего не брать тоже нельзя!')
    else:
        total_count = model.getCandies()
        leftover = total_count - teke_user
        model.setCandies(leftover)
        model.getCandies()
        await bot.send_message(message.from_user.id,
                               f'{message.from_user.first_name} ты взял(а) {teke_user} конфет, осталось {leftover}.')
        if model.checkWinner() == True:
            await bot.send_message(message.from_user.id,
                                   'Я выйграл! Приятно иметь с тобой дело!=)')
        await moveBot()


async def moveBot(message: types.Message):
    candies = model.getCandies()
    take = random.randint(1, 28)
    leftover = candies - take
    model.setCandies(leftover)
    model.getCandies()
    await bot.send_message(message.from_user.id,
                           f'Я взял {take} конфет, осталось {leftover}.')
    if model.checkWinner() == True:
        await bot.send_message(message.from_user.id,
                               f'{message.from_user.first_name}, ты выйграл(а)! Мои поздравления!')
    else:
        await bot.send_message(message.from_user.id,
                               f'{message.from_user.first_name}, теперь твой ход.')
    await moveUser(player)
