from aiogram import types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
from config import bot, dp
import logging


@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    await message.answer(f"Салалекум {message.from_user.full_name}")
    # await message.reply(f"Привет босс {message.from_user.first_name}!")

@dp.message_handler(commands=['mem'])
async def command_mem(message: types.Message):
    photo = open('media/problem1.jpg', 'rb')
    photo_2 = open('media/igor2-15061915071907_5.jpg', 'rb')
    await bot.send_photo(message.from_user.id, photo)
    await bot.send_photo(message.from_user.id, photo_2)



@dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton("NEXT", callback_data="button_call_1")
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


@dp.callback_query_handler(lambda call: call.data == "button_call_1")
async def quiz_2(call: types.CallbackQuery):

    question = "Из какого зерна делается японский спирт саке?"
    answers = [
        "пшеницы",
        "кукурузы",
        "ячменя",
        "Рис",
        "проса",
        "овса",
    ]
    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        explanation="ИЗЗИ!",
        open_period=60,

    )





@dp.message_handler()
async def echo(message: types.Message):
    if message.text.isnumeric() == True:
        square = int(message.text)
        await message.answer(square**2)
    else:
        await bot.send_message(message.from_user.id, message.text)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
