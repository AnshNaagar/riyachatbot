from aiogram import types, Dispatcher
from config import OWNER_ID
from utils import db

async def broadcast_cmd(message: types.Message):
    if message.from_user.id != OWNER_ID:
        return await message.reply("😅 Ye command sirf owner ke liye hai.")
    
    text = message.text.split(maxsplit=1)
    if len(text) < 2:
        return await message.reply("⚙️ Usage: /broadcast <message>")
    
    users = db.get_all_users()
    sent = 0
    for user in users:
        try:
            await message.bot.send_message(user[0], text[1])
            sent += 1
        except:
            pass
    await message.reply(f"✅ Broadcast sent to {sent} users.")

def register(dp: Dispatcher):
    dp.register_message_handler(broadcast_cmd, commands=["broadcast"])
