from aiogram import types, Dispatcher
from utils.db import add_user
import config

async def cmd_start(message: types.Message):
    user_id = str(message.from_user.id)
    add_user(user_id)
    await message.answer(f"Welcome to Spinner Bot!\nUse /spin to play.")

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands=["start"])
