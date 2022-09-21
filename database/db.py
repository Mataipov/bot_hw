import random
import sqlite3
from config import bot


def sql_create():
    global db, cursor
    db = sqlite3.connect("bot.sqlite3")
    cursor = db.cursor()

    if db:
        print("База данных подключена!")

    db.execute("CREATE TABLE IF NOT EXISTS menu "
               "(username TEXT, "
               "photo TEXT, "
               "name_dish TEXT PRIMARY KEY, "
               "description_dish TEXT, "
               "price TEXT)")

    db.commit()


async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.execute("INSERT INTO menu VALUES (?, ?, ?, ?, ?)",
                       tuple(data.values()))
    db.commit()


async def sql_command_random(message):
    result = cursor.execute("SELECT * FROM menu").fetchall()
    random_user = random.choice(result)
    await bot.send_photo(message.from_user.id, random_user[1],
                         caption=f"Название блюда: {random_user[2]}\n"
                                 f"Описание блюда: {random_user[3]}\n"
                                 f"Цена блюда: {random_user[4]}\n\n"
                                 f"{random_user[0]}")


async def sql_command_all():
    user_list = cursor.execute("SELECT * FROM menu").fetchall()
    return user_list


async def sql_command_delete(name_dish):
    cursor.execute("DELETE FROM menu WHERE name_dish == ?", (name_dish,))
    db.commit()