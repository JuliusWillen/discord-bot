from ai_response import AiResponse

AI = AiResponse("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")

while True:
    prompt = input("Prompt: ")
    print(AI.get_response(prompt))
