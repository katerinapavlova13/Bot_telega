# сюда все функции отправляющие сообщения
import asyncio
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
    await bot.send_message(message.from_user.id,
                           'Так и быть делай первый ход.')

async def moveUser(message: types.Message):
    user = message.text
    model.setPlayer(user)
    if (message.text).isdigit():
        if int(user) > model.maxCandy():
            await bot.send_message(message.from_user.id,
                                   f'Эй, ты взял слишком много, не больше {model.maxCandy()}!!!')
        elif int(user) < model.minCandy():
            await bot.send_message(message.from_user.id,
                                   'Ничего не брать тоже нельзя!')
        else:
            total_count = model.getCandies()
            take_user = int(message.text)
            leftover = total_count - take_user
            await bot.send_message(message.from_user.id,
                                   f'{message.from_user.first_name} ты взял(а) {take_user} конфет,'
                                   f' осталось {leftover}.')
            if model.checkWinner() == True:
                await bot.send_message(message.from_user.id,
                                       'Я выйграл! Приятно иметь с тобой дело!=)')
                return
            model.setCandies(leftover)
            await moveBot(message)

async def moveBot(message: types.Message):
    candies = model.getCandies()
    if candies < 29:
        take = candies
    else:
        take = random.randint(1, 28)
    leftover = candies - take
    await bot.send_message(message.from_user.id,
                               f'Я взял {take} конфет, осталось {leftover}.')
    if model.checkWinner() == True:
        await bot.send_message(message.from_user.id,
                               f'{message.from_user.first_name}, '
                               f'ты выйграл(а)! Мои поздравления!')
        return
    model.setCandies(leftover)
    await asyncio.sleep(1)
    await nextMove(message)


async def nextMove(message: types.Message):
    await bot.send_message(message.from_user.id, f'{message.from_user.first_name}, '
                                                 f'теперь твой ход')
