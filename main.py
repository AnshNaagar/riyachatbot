from aiogram import Bot, Dispatcher, executor, types
from config import BOT_TOKEN
from handlers import commands, chat, broadcast
from utils import db

bot = Bot(token=BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot)

# Register handlers
commands.register(dp)
chat.register(dp)
broadcast.register(dp)

async def on_startup(dispatcher):
    db.init_db()
    print("🤖 Bot is running...")

if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup)
