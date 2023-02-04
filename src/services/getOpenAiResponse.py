def getOpenAiResponse(state, input):
    if state.openai is None:
        raise Exception("OpenAI not mounted")

    response = state.openai.Completion.create(
        model="text-davinci-003", prompt=input, temperature=0.7, max_tokens=20)

    return response["choices"][0]["text"]
