import os
from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from dotenv import load_dotenv

load_dotenv('.env')
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot=bot, storage=MemoryStorage())

data = dict()
@dp.message_handler(commands="start")
async def start_handler(msg: types.Message):
    print(msg.chat.id)
    await msg.answer(text = f"{msg.from_user.id} -> {msg.from_user.first_name}" )

@dp.message_handler(lambda msg : len(msg.text.split()) == 3)
async def share(msg : types.Message):
    _ , to_id , message = msg.text.split()
    ikm = InlineKeyboardMarkup()
    ikb = InlineKeyboardButton(text = "read" , callback_data="1")
    ikm.add(ikb)
    a = await msg.bot.send_message( -1001841135002,text =f"Secret msg -> {to_id} \n ********" , reply_markup=ikm)
    data.update({a.message_id : (int(to_id) , msg.from_user.id , message)})

@dp.callback_query_handler()
async def secret_callback_handler(callback: types.CallbackQuery , state : FSMContext):
    msg = data.get(callback.message.message_id)
    if callback.from_user.id in data.get(callback.message.message_id):
        if callback.from_user.id != data.get(callback.message.message_id)[0]:
            await callback.answer(text=msg[-1], show_alert=True)
        else:
            del data[callback.message.message_id]
            await callback.message.delete()
            await callback.answer(text = msg[-1] , show_alert=True)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
