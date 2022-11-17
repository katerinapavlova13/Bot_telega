from aiogram.utils import executor
import heandlers
from bot import dp

heandlers.registred_handlers(dp)
executor.start_polling(dp, skip_updates=True)

