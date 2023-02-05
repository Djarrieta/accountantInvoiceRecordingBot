import telebot
from telebot import types

from services.getOpenAiResponse import getOpenAiResponse


def mountTelegram(state):
    if state.userData["telegramToken"] is None:
        raise Exception("Telegram token not found")

    state.telegram = telebot.TeleBot(state.userData["telegramToken"])

    markup = types.ReplyKeyboardMarkup(row_width=1)
    markup.add(types.KeyboardButton('ChatId'))
    markup.add(types.KeyboardButton('MaxLength'))

    state.telegram.send_message(
        state.userData["chatId"], "Ask whatever you want", reply_markup=markup)

    @state.telegram.message_handler(content_types=["text"])
    def bot_text_messages(message):
        if message.text == "ChatId":
            state.telegram.send_message(message.chat.id, message.chat.id)
        else:
            response = getOpenAiResponse(state, message.text)
            state.telegram.send_message(message.chat.id, response)

    state.telegram.infinity_polling()
