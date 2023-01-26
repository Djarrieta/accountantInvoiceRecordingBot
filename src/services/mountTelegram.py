def mountTelegram(state):
    if state.userData.telegramToken:
        state.telegram = telegram.Bot(state.userData.telegramToken)
