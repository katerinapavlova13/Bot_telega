#здесь главный файл для запуска

from aiogram.utils import executor

import heandlers
from bot import dp

async def on_startup(_):
    print('Бот запущен')

heandlers.registred_handlers(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

