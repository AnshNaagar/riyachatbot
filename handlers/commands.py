from aiogram import types, Dispatcher
from utils import db

async def start_cmd(message: types.Message):
    db.add_user(message.from_user.id)
    await message.reply("👋 Hello! I am your AI bot. Use /chatbot to enable AI mode.")

async def chatbot_cmd(message: types.Message):
    user_id = message.from_user.id
    current = db.toggle_chatbot(user_id)
    await message.reply(f"✅ Chatbot mode is now {current}")

async def lang_cmd(message: types.Message):
    parts = message.text.split(maxsplit=1)
    if len(parts) < 2:
        return await message.reply("⚙️ Usage: /lang <language>")
    lang = parts[1].lower()
    db.set_language(message.from_user.id, lang)
    await message.reply(f"🌐 Language updated to {lang}")

def register(dp: Dispatcher):
    dp.register_message_handler(start_cmd, commands=["start"])
    dp.register_message_handler(chatbot_cmd, commands=["chatbot"])
    dp.register_message_handler(lang_cmd, commands=["lang"])
