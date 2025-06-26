from aiogram import types, Dispatcher
from utils.db import get_user_balance

async def check_balance(message: types.Message):
    user_id = str(message.from_user.id)
    balance = get_user_balance(user_id)
    await message.answer(f"💰 Your balance: ₹{balance}")

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(check_balance, commands=["balance"])
