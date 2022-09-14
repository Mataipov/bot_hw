from aiogram import types, Dispatcher
from config import bot, dp, ADMINS
import random




async def echo(message: types.Message):
    if message.text.isnumeric() == True:
        square = int(message.text)
        await message.answer(square**2)
    else:
        await bot.send_message(message.from_user.id, message.text)

    if message.from_user.id not in ADMINS:
        await message.reply("Ты не мой босс!!!")
    elif message.text == 'game':
        ran = ['⚽️', '🏀','🎲', '🎯','🎳', '🎰']
        em = random.choice(ran)
        await bot.send_dice(message.chat.id, emoji=em)







def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo, content_types=['text', 'photo'])