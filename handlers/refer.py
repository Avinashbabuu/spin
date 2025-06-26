from aiogram import types, Dispatcher
from utils.db import add_user, reward_referrer

async def handle_refer(message: types.Message):
    ref_id = message.get_args()
    user_id = str(message.from_user.id)
    add_user(user_id, ref_id)
    await message.answer("🎉 You joined via referral!\nUse /spin to start playing.")
    if ref_id:
        reward_referrer(ref_id)

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(handle_refer, commands=["refer"])
