from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import bot, ADMINS


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
                                                f"скинь фотку...")
    else:
        await message.answer("Пиши в личку!!!")


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['id'] = message.from_user.id
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
    await state.finish()
    await message.answer("Все свободен!")


def register_handlers_fsm_menu(dp: Dispatcher):
    dp.register_message_handler(fsm_start, commands=['menu'])
    dp.register_message_handler(load_photo, state=FSMAdmin.photo,
                                content_types=['photo'])
    dp.register_message_handler(load_name_dish, state=FSMAdmin.name_dish)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_price, state=FSMAdmin.price)