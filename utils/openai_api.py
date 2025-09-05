import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def get_reply(user_input, lang="english"):
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"Reply in {lang}: {user_input}",
            max_tokens=150
        )
        return response.choices[0].text.strip()
    except:
        return "⚠️ Error: Unable to fetch reply right now."
