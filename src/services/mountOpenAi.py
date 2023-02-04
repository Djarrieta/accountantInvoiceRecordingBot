import openai


def mountOpenAi(state):
    if state.userData["openaiToken"] is None:
        raise Exception("OpenAI token not found")

    openai.api_key = state.userData["openaiToken"]
    state.openai = openai
