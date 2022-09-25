import asyncio
import aioschedule
from aiogram import types, Dispatcher
from config import bot


async def get_chat_id(message: types.Message):
    global chat_id
    chat_id = message.from_user.id
    await bot.send_message(chat_id=chat_id, text="ok!")


async def weekends():
    await bot.send_message(chat_id=chat_id, text="Скоро выходные!")
    video = open('media/moi-plani-na-vixodnie-prikol_(videomega.ru).mp4', 'rb')
    await bot.send_video(chat_id=chat_id, video=video)






async def schedule():

    aioschedule.every().friday.at("18:33").do(weekends)

    while True:
        await aioschedule.run_pending()
        await asyncio.sleep(2)


def register_handlers_notification(dp: Dispatcher):
    dp.register_message_handler(get_chat_id,
                                lambda word: 'выходные' in word.text)