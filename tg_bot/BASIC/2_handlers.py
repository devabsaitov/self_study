# telegram bot handlers
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

BOT_TOKEN = '5838195691:AAFS8Flsva-HA6wn66Wu6tf-64RWtkclWDA'
bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot=bot, storage=MemoryStorage())

@dp.message_handler(commands='document')
async def start_handler(message : types.Message):
    # await message.reply(text = message.text)
    # await message.reply_photo(photo= open('img.png' , 'rb'), caption="Assalom O'zbekiston")
    # await message.answer_photo(photo= open('img.png' , 'rb'), caption="Assalom O'zbekiston")
    # await message.reply_contact(phone_number='+998901234567', first_name='Botirjon' , last_name='Botirov')
    # await message.answer_contact(phone_number='+998901234567', first_name='Botirjon' , last_name='Botirov',)
    # await message.reply_document(document=open('test.xlsx' , 'rb'))
    # await message.reply_video(video=open('video.MP4' , 'rb'))
    await message.reply_location(latitude=12 , longitude=45)




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)