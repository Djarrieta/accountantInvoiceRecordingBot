import telebot
from services.getOpenAiResponse import getOpenAiResponse


def mountTelegram(state):
    if state.userData["telegramToken"] is None:
        raise Exception("Telegram token not found")

    state.telegram = telebot.TeleBot(state.userData["telegramToken"])

    @state.telegram.message_handler(content_types=["text"])
    def bot_text_messages(message):
        response = getOpenAiResponse(state, message.text)
        state.telegram.send_message(message.chat.id, response)

    state.telegram.infinity_polling()
