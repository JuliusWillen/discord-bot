from ai_response import AiResponse

AI = AiResponse("")

while True:
    prompt = input("Prompt: ")
    print(AI.get_response(prompt))
