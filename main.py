import asyncio
from aiogram.utils import executor
from config import dp
import logging
from handlers import clients, callback, extra, admins, fsm_admin_menu, notifications, inlline
from database.db import sql_create


async def on_startup(_):
    asyncio.create_task(notifications.schedule())
    sql_create()

clients.register_handlers_client(dp)
callback.register_handlers_callback(dp)
fsm_admin_menu.register_handlers_fsm_menu(dp)
inlline.register_handlers_inline(dp)
notifications.register_handlers_notification(dp)

extra.register_handlers_extra(dp)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup))

