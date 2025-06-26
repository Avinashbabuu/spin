from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.utils import executor
import asyncio
import config
from handlers import start, spin, balance, refer, withdraw

bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot)

start.register_handlers(dp)
spin.register_handlers(dp)
balance.register_handlers(dp)
refer.register_handlers(dp)
withdraw.register_handlers(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
