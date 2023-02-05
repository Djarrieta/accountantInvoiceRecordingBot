def getOpenAiResponse(state, input):
    if state.openai is None:
        raise Exception("OpenAI not mounted")

    response = state.openai.Completion.create(
        model="text-davinci-003", prompt=input, temperature=0.7, max_tokens=200)

    if response["choices"] is None:
        raise Exception("OpenAI response is empty")

    return response["choices"][0]["text"]
