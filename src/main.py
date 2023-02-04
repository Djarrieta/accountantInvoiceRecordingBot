from State import State
from services.getUserData import getUserData
from services.mountOpenAi import mountOpenAi
from services.mountTelegram import mountTelegram

state = State()

getUserData(state)
mountOpenAi(state)
mountTelegram(state)
