from aiogram import types, Dispatcher
from utils.db import get_user_balance, update_user_balance
import random

async def spin_game(message: types.Message):
    user_id = str(message.from_user.id)
    reward = random.choice([0, 10, 20, 50, 0])
    balance = update_user_balance(user_id, reward)
    await message.answer(f"🎰 You won ₹{reward}!\nNew Balance: ₹{balance}")

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(spin_game, commands=["spin"])
