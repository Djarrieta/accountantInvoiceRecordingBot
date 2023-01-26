
import os
from dotenv import load_dotenv


def getUserData(state):
    load_dotenv()
    state.userData["telegramToken"] = os.getenv("TELEGRAM_TOKEN")
    state.userData["openaiToken"] = os.getenv("OPENAI_TOKEN")
    state.userData["chatId"] = os.getenv("CHAT_ID")
