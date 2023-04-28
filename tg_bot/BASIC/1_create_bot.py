# telegram bot create

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

BOT_TOKEN = '5838195691:AAFS8Flsva-HA6wn66Wu6tf-64RWtkclWDA'  # BotFather token olinadi
bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot=bot, storage=MemoryStorage())


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
