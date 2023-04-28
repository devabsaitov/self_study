# telegram bot create
from aiogram.types import KeyboardButton , ReplyKeyboardMarkup
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

BOT_TOKEN = '5838195691:AAFS8Flsva-HA6wn66Wu6tf-64RWtkclWDA'  # BotFather token olinadi
bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot=bot, storage=MemoryStorage())

markup = ReplyKeyboardMarkup(row_width=2 , resize_keyboard=True , one_time_keyboard=True)
# markup.add('button 1','button 2','button 3', 'button 4')
markup.add(KeyboardButton('Contact ' , request_contact=True) , KeyboardButton('Location' , request_location=True))


@dp.message_handler(lambda message : str(message.text).isnumeric() )
async def keyboard_show_handler(message: types.Message):
    await message.answer(text = 'Keyboard button show ' , reply_markup=markup)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)