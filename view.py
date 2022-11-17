import asyncio
from aiogram import types
import random
import model
from bot import bot

async def helloUser(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f'{message.from_user.first_name}, привет! 👋\n'
                           f'Это игра в конфеты. 🍬 \n'
                           f'Если хочешь сыграть, нажми /rules '
                           f'и я расскажу тебе правила игры. 😉')

async def goodbye(message: types.Message):
    await bot.send_message(message.from_user.id,
                        f'{message.from_user.first_name}, '
                        f'пока! 👋')

async def regulations(message: types.Message):
    await bot.send_message(message.from_user.id,
                           f'У нас есть {model.getCandies()} конфет🍬.\n'
                           'Мы по очереди берем конфеты.\n'
                           f'За один ход можно взять не более чем {model.maxCandy()} конфет.\n'
                           'Выйграет тот, кто заберет последние конфеты!\n')
    await asyncio.sleep(5)
    await bot.send_message(message.from_user.id,
                           'Подкинем монетку, чтобы узнать кто будет брать конфеты первый.'
                           ' Нажми /go и монета сделает выбор.')

async def goGame(message: types.Message):
    model.total_candies = 150
    count = random.randint(0, 1)
    if count:
        await bot.send_message(message.from_user.id,
                           'Так и быть делай первый ход.😑')
        await moveUser(message)
    else:
        await bot.send_message(message.from_user.id,
                               'Я хожу первый. 😎')
        await moveBot(message)

async def moveUser(message: types.Message):
    user = message.text
    model.setPlayer(user)
    if (message.text).isdigit():
        if int(user) > model.maxCandy():
            await bot.send_message(message.from_user.id,
                                   f'Эй, ты взял(a) слишком много, не больше {model.maxCandy()}! 😡')
        elif int(user) < model.minCandy():
            await bot.send_message(message.from_user.id,
                                   'Ничего не брать тоже нельзя! 🤨')
        else:
            total_count = model.getCandies()
            take_user = int(message.text)
            leftover = total_count - take_user
            await bot.send_message(message.from_user.id,
                                   f'{message.from_user.first_name}, ты взял(а) {take_user} конфет,'
                                   f' осталось {leftover}.')
            if model.checkWinner(leftover):
                await asyncio.sleep(1)
                await bot.send_message(message.from_user.id,
                                       'Я выйграл! 🥳\n'
                                       'Приятно иметь с тобой дело!😉')
                await bot.send_message(message.from_user.id,
                                       '🍬🍬🍬🍬🍬🍬GAME OVER🍬🍬🍬🍬🍬🍬')
                await asyncio.sleep(2)
                await bot.send_message(message.from_user.id,
                                       'Если хочешь сыграть снова нажми /go 😏\n'
                                       'либо /finish и мы попрощаемся.😩')
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
                           'Хмм...дай подумать.🤔')
    await asyncio.sleep(3)
    await bot.send_message(message.from_user.id,
                               f'Я взял {take} конфет, осталось {leftover}.')
    if model.checkWinner(leftover):
        await asyncio.sleep(1)
        await bot.send_message(message.from_user.id,
                               f'{message.from_user.first_name}, '
                               f'ты выйграл(а)!😭\n'
                               f'Я конечно рад за тебя, но не от всей души...\n'
                               f'Может быть реванш?🥺')
        await bot.send_message(message.from_user.id,
                               '🍬🍬🍬🍬🍬🍬GAME OVER🍬🍬🍬🍬🍬🍬')
        await asyncio.sleep(2)
        await bot.send_message(message.from_user.id,
                               'Если хочешь сыграть снова нажми /go 😏\n'
                               'либо /finish и мы попрощаемся.😞')
        return

    model.setCandies(leftover)
    await nextMove(message)


async def nextMove(message: types.Message):
    await bot.send_message(message.from_user.id, f'{message.from_user.first_name}, '
                                                 'надеюсь ты хорошо подумал(а)? 🧠\n'
                                                 'Теперь твой ход.')