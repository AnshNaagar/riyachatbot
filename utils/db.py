import sqlite3
from config import DB_PATH

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users(
        user_id INTEGER PRIMARY KEY,
        chatbot INTEGER DEFAULT 0,
        language TEXT DEFAULT 'english'
    )""")
    conn.commit()
    conn.close()

def add_user(user_id):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("INSERT OR IGNORE INTO users (user_id) VALUES (?)", (user_id,))
    conn.commit()
    conn.close()

def toggle_chatbot(user_id):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT chatbot FROM users WHERE user_id=?", (user_id,))
    state = cur.fetchone()[0]
    new_state = 0 if state == 1 else 1
    cur.execute("UPDATE users SET chatbot=? WHERE user_id=?", (new_state, user_id))
    conn.commit()
    conn.close()
    return "ON" if new_state == 1 else "OFF"

def is_chatbot_on(user_id):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT chatbot FROM users WHERE user_id=?", (user_id,))
    state = cur.fetchone()
    conn.close()
    return state and state[0] == 1

def set_language(user_id, lang):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("UPDATE users SET language=? WHERE user_id=?", (lang, user_id))
    conn.commit()
    conn.close()

def get_language(user_id):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT language FROM users WHERE user_id=?", (user_id,))
    lang = cur.fetchone()
    conn.close()
    return lang[0] if lang else "english"

def get_all_users():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute("SELECT user_id FROM users")
    users = cur.fetchall()
    conn.close()
    return users
