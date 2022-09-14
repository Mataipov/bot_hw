from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot, dp




async def quiz_2(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_2 = InlineKeyboardButton("Викторина третья", callback_data="button_call_2")
    markup.add(button_call_2)

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
        reply_markup=markup

    )
async def quiz_3(call: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    button_call_3 = InlineKeyboardButton("Викторина первая", callback_data="button_call_3")
    markup.add(button_call_3)
    question = " Из чего в основном состоят кометы?"
    answers = [
        'ядовитая жидкость',
        'лед и пыль',
        'ржавый металл',
        'расплавленный камень',
    ]

    await bot.send_poll(
        chat_id=call.message.chat.id,
        question=question,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=1,
        explanation="ИЗЗИ!",
        open_period=60,
        reply_markup=markup
    )

async def quiz_1(call: types.CallbackQuery):
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
            chat_id=call.message.chat.id,
            question=question,
            options=answers,
            is_anonymous=False,
            type='quiz',
            correct_option_id=1,
            explanation="Если ты не знаешь, то ты не любитель культуры Японии!",
            open_period=60,
            reply_markup=markup
        )


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text="button_call_1")
    dp.register_callback_query_handler(quiz_3,
                                       lambda call: call.data == "button_call_2")
    dp.register_callback_query_handler(quiz_1,
                                       lambda call: call.data == "button_call_3")