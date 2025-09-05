from aiogram import types, Dispatcher
from utils import db, openai_api, helpers
import random

friendly_replies = [
    "😅 ye kya keh rhe ho, mujhe pasand nhi jo tum karna chahte ho...",
    "arre yaar, esa mat likho 😅",
    "uff, mujhe thoda awkward lag raha hai ye padh ke 🤔",
    "😶 mujhe acha nahi laga tumhara msg"
]

async def chat_handler(message: types.Message):
    user_id = message.from_user.id
    if not db.is_chatbot_on(user_id):
        return  

    text = message.text
    if helpers.is_inappropriate(text):
        await message.reply(random.choice(friendly_replies))
        return
    
    lang = db.get_language(user_id)
    reply = openai_api.get_reply(text, lang)
    await message.reply(reply)

def register(dp: Dispatcher):
    dp.register_message_handler(chat_handler, content_types=types.ContentTypes.TEXT)
