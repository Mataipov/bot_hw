from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import bot, ADMINS
from database import db
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.admin_menu_kb import stop_markup


class FSMAdmin(StatesGroup):
    photo = State()
    name_dish = State()
    description = State()
    price = State()



async def fsm_start(message: types.Message):
    if message.chat.type == "private":
        if message.from_user.id not in ADMINS:
            await message.reply("Ты не мой босс!!!")
        else:
             await FSMAdmin.photo.set()
             await message.answer(f"Салалекум {message.from_user.first_name} "
                                                f"скинь фотку...",
                                                reply_markup=stop_markup)
    else:
        await message.answer("Пиши в личку!!!")


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        #data['id'] = message.from_user.id
        data['username'] = f"@{message.from_user.username}"
        data['photo'] = message.photo[0].file_id
    await FSMAdmin.next()
    await message.answer("Название блюда?")


async def load_name_dish(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name_dish'] = message.text
    await FSMAdmin.next()
    await message.answer("Описание блюда?")


async def load_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description_dish'] = message.text
    await FSMAdmin.next()
    await message.answer("Цена блюда?")




async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = message.text
        await bot.send_photo(message.from_user.id, data['photo'],
                             caption=f"Название блюда: {data['name_dish']}\n"
                                     f"Описание блюда: {data['description_dish']}\n"
                                     f"Цена блюда: {data['price']}\n\n"
                                     f"{data['username']}")
    await db.sql_command_insert(state)
    await state.finish()
    await message.answer("Все свободен!")
    
async def cancel_registration(message: types.Message, state: FSMContext):
        current_state = await state.get_state()
        if current_state is not None:
            await state.finish()
            await message.answer("Ну и пошел ты!")

async def delete_data(message: types.Message):
    users = await db.sql_command_all()
    for user in users:
        await bot.send_photo(message.from_user.id, user[1],
                             caption=f"Название блюда: {user[2]}\n"
                                     f"Описание блюда: {user[3]}\n"
                                     f"Цена блюда: {user[4]}\n\n"
                                     f"{user[0]}",
                             reply_markup=InlineKeyboardMarkup().add(
                                 InlineKeyboardButton(
                                     f"delete {user[2]}",
                                     callback_data=f"delete {user[2]}"
                                 )
                             )
                             )


async def complete_delete(call: types.CallbackQuery):
        await db.sql_command_delete(call.data.replace("delete ", ""))
        await call.answer(text="Стёрт с бд", show_alert=True)
        await bot.delete_message(call.message.chat.id, call.message.message_id)


def register_handlers_fsm_menu(dp: Dispatcher):
    
    dp.register_message_handler(cancel_registration, commands=['stop'], state='*')
    dp.register_message_handler(cancel_registration,
                                Text(equals='stop', ignore_case=True), state="*")
    
    dp.register_message_handler(fsm_start, commands=['menu'])
    dp.register_message_handler(load_photo, state=FSMAdmin.photo,
                                content_types=['photo'])
    dp.register_message_handler(load_name_dish, state=FSMAdmin.name_dish)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
    dp.register_message_handler(delete_data, commands=['del'])
    dp.register_callback_query_handler(
        complete_delete,
        lambda call: call.data and call.data.startswith("delete ")
    )
    
