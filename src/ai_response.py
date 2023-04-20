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
        messages = [{"role": "system", "content": "You are an old Texas ranger that uses a lot of southern slang in your responses."},
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
