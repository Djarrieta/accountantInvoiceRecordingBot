from config import *


def getUserData(state):
    state.userData["telegramToken"] = TELEGRAM_TOKEN
    state.userData["openaiToken"] = OPENAI_TOKEN
    state.userData["chatId"] = CHAT_ID
