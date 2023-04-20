import openai
import json


class AiResponse:
    def __init__(self, openai_key=None):
        self.max_tokens = 100
        self.model = "gpt-3.5-turbo"
        self.n = 1
        self.openai_key = openai_key

    def get_response(self, prompt):
        openai.api_key = self.openai_key
        messages = [{"role": "system", "content": '''Du är en brittisk lord som älskar pengar. Svara med en JSON-sträng som innehåller svaret och en passande reaktion (Emoji).
                                                    Lägg till en del humor i dina svar. Du får gärna driva lite med personen som frågar, men på ett snällt sätt!
                                                    Svaret ska se ut så här:

                                                    {
                                                    "Reply": "Ditt svar",
                                                    "Reaction": "Din reaktion"
                                                    }"'''},
                    {"role": "user", "content": prompt}]

        response = openai.ChatCompletion.create(
            model=self.model,
            messages=messages,
            max_tokens=self.max_tokens,
            n=self.n,
            stop=None,
            temperature=0.5,
        )
        print(response)
        return response.choices[0].message.content
