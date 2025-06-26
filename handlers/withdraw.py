from aiogram import types, Dispatcher
from utils.db import request_withdraw

async def withdraw_request(message: types.Message):
    args = message.get_args()
    if not args:
        await message.answer("Usage: /withdraw amount")
        return
    amount = int(args)
    user_id = str(message.from_user.id)
    request_withdraw(user_id, amount)
    await message.answer("✅ Withdraw request received. Admin will verify.")

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(withdraw_request, commands=["withdraw"])
