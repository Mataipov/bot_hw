from aiogram.utils import executor
from config import dp
import logging
from handlers import clients, callback, extra, admins, fsm_admin_menu

clients.register_handlers_client(dp)
callback.register_handlers_callback(dp)
fsm_admin_menu.register_handlers_fsm_menu(dp)

extra.register_handlers_extra(dp)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)

