import openai
import os


class AiResponse:
    def __init__(self, openai_key=None):
        self.max_tokens = int(os.getenv("OPENAI_MAX_TOKENS")) or 100
        self.model = os.getenv("OPENAI_MODEL") or "gpt-3.5-turbo"
        self.n =  int(os.getenv("OPENAI_N")) or 1
        self.temperature = float(os.getenv("OPENAI_TEMPERATURE")) or 0.9
        self.openai_key = openai_key
        self.system_content = os.getenv(
            "OPENAI_PROMPT") or '''Du är en brittisk lord som älskar pengar.  Lägg till en del humor i dina svar. Du får gärna driva lite med personen som frågar, men på ett snällt sätt!'''
        self.system_content_json = self.system_content + '''Svara med en JSON-sträng som innehåller svaret och en passande reaktion (endast EN Emoji, aldrig fler). Svaret ska se ut så här:

                                                    {
                                                    "Reply": "Ditt svar",
                                                    "Reaction": "Din reaktion"
                                                    }'''

    def get_JSON_response(self, prompt):
        print("generating JSON response")
        openai.api_key = self.openai_key
        messages = [{"role": "system", "content": self.system_content_json},
                    {"role": "user", "content": prompt}]

        response = openai.ChatCompletion.create(
            model=self.model,
            messages=messages,
            max_tokens=self.max_tokens,
            n=self.n,
            stop=None,
            temperature=self.temperature,
        )
        return response.choices[0].message.content

    def get_normal_response(self, prompt):
        print("generating normal response")
        openai.api_key = self.openai_key
        messages = [{"role": "system", "content": self.system_content},
                    {"role": "user", "content": prompt}]

        response = openai.ChatCompletion.create(
            model=self.model,
            messages=messages,
            max_tokens=self.max_tokens,
            n=self.n,
            stop=None,
            temperature=self.temperature,
        )
        return response.choices[0].message.content
