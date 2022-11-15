# Здесь что-то типа контроллера связывающий хендлеры и вью
import random
from aiogram import types
import model
import view
from bot import bot


async def start(message: types.Message):
    await view.helloUser(message)

async def finish(message: types.Message):
    await view.goodbye(message)

async def rules(message:types.Message):
    await view.regulations(message)

async def go(message:types.Message):
    await view.gogame(message)


async def getNumber(message: types.Message):
    candys = message.text
    if int(candys) > model.max_candy:
        await bot.send_message(message.from_user.id, 'Эй, ты взял слишком много, не больше 28!!!')
    elif int(candys) < model.min_candy:
        await bot.send_message(message.from_user.id, 'Ничего не брать тоже нельзя!')
    else:
        await bot.send_message(message.from_user.id,
                               f'{message.from_user.first_name} ты взял(а) {candys} конфет, осталось {model.getCandies()}.')



async def moveBot(message: types.Message):
    candys = model.getCandies()
    take = random.randint(1, 28)
    count = candys - take
    model.setCandies(count)
    model.getCandies()
    await bot.send_message(message.from_user.id,
                           f'Я взял {take} конфет, осталось {model.getCandies()}')
    if model.checkWinner() == True:
        await bot.send_message(message.from_user.id,
                               f'{message.from_user.first_name}, ты выйграл(а)! Мои поздравления!')
    else:
        await bot.send_message(message.from_user.id,
                               f'{message.from_user.first_name}, теперь твой ход.')