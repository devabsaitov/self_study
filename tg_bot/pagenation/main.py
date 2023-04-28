import os

from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from dotenv import load_dotenv

from tg_bot.pagenation.data import DATA

load_dotenv('.env')
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(BOT_TOKEN)
dp = Dispatcher(bot=bot, storage=MemoryStorage())

@dp.message_handler(commands="start")
async def start_handler(msg: types.Message):
    prev = InlineKeyboardButton(text = '⏮' , callback_data='prev_1')
    current = InlineKeyboardButton(text = f'1/{len(DATA)}', callback_data='current_1')
    next = InlineKeyboardButton(text = '⏭', callback_data='next_2')
    markup = InlineKeyboardMarkup(inline_keyboard=[[prev , current , next]])
    await msg.answer(text =DATA[0] , reply_markup=markup)

@dp.callback_query_handler()
async def edit_handler(callback : types.CallbackQuery):
    if callback.data.startswith('prev_'):
        page_num = int(callback.data.split('prev_')[-1])
    if callback.data.startswith('next_'):
        page_num = int(callback.data.split('next_')[-1])
    if callback.data.startswith('current_'):
        page_num = int(callback.data.split('current_')[-1])
    prev = InlineKeyboardButton(text='⏮', callback_data=f'prev_{len(DATA) if page_num == 1 else page_num - 1}')
    current = InlineKeyboardButton(text=f'{page_num}/{len(DATA)}', callback_data=f'current_{page_num}')
    next = InlineKeyboardButton(text='⏭', callback_data=f'next_{1 if page_num == len(DATA) else page_num + 1}')
    markup = InlineKeyboardMarkup(inline_keyboard=[[prev, current, next]])
    await bot.edit_message_text(text = DATA[page_num - 1] ,chat_id=callback.from_user.id, message_id=callback.message.message_id , reply_markup=markup)

@dp.message_handler(commands="video")
async def start_handler(msg: types.Message):
    await msg.answer_video(video=open('video.mp4' , 'rb'))




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
