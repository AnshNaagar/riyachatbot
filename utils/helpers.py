bad_words = ["sex", "nude", "fuck", "xxx", "porn"]

def is_inappropriate(text):
    text = text.lower()
    return any(word in text for word in bad_words)
