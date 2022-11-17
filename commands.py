from aiogram import types
import view

async def start(message: types.Message):
    await view.helloUser(message)

async def finish(message: types.Message):
    await view.goodbye(message)

async def rules(message:types.Message):
    await view.regulations(message)

async def go(message:types.Message):
    await view.goGame(message)



