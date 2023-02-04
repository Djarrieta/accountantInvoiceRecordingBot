from State import State
from services.getOpenAiResponse import getOpenAiResponse
from services.getUserData import getUserData
from services.mountOpenAi import mountOpenAi
# only one state object is created for the entire application
state = State()

getUserData(state)
mountOpenAi(state)

response = getOpenAiResponse(state, "How to use OpenAI?")

print(response)
