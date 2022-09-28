from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot, dp
from parser.novels import parser
import random




async def command_start(message: types.Message):
    await message.answer(f"Салалекум {message.from_user.full_name}")



async def pin(message: types.Message):
    if not message.reply_to_message:
        await message.reply("Команда должна быть ответом на сообщение!")
    else:
        await bot.pin_chat_message(message.chat.id,
                                   message.reply_to_message.message_id)







async def command_mem(message: types.Message):
    photos = [
        'media/problem1.jpg',
        'media/igor2-15061915071907_5.jpg'
    ]
    photo = open(random.choice(photos), 'rb')

    await bot.send_photo(message.from_user.id, photo)




async def command_help(message: types.Message):
    await message.answer(f"Разбирайся сам!")



async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("Викторина вторая", callback_data="button_call_1")
    markup.add(button_call_1)

    question = "Какой национальный цветок Японии?"
    answers = [
        "Хризантемы",
        "Сакура",
        "Пионы",
        "Ирисы",
        "Камелии",
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type = 'quiz',
        correct_option_id=1,
        explanation="Если ты не знаешь, то ты не любитель культуры Японии!",
        open_period=60,
        reply_markup=markup
    )
async def novels_parser(message: types.Message):
    novels = parser()
    for novel in novels:
        await bot.send_message(
            message.from_user.id,
            f"{novel['link']}\n\n"
            f"{novel['title']}\n"
            f"{novel['author']}\n\n"

        )


def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(pin, commands=['pin'], commands_prefix='!/')
    dp.register_message_handler(command_mem, commands=['mem'])
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(command_help, commands=['help'])
    dp.register_message_handler(novels_parser, commands=['novels'])
