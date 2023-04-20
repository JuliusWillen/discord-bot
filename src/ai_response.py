import openai
import os


class AiResponse:
    def __init__(self, openai_key=None):
        self.max_tokens = 100
        self.model = "text-davinci-003"
        self.n = 1
        self.openai_key = openai_key

    def get_response(self, prompt):
        openai.api_key = self.openai_key
        response = openai.Completion.create(
            engine=self.model,
            prompt=prompt,
            max_tokens=self.max_tokens,
            n=self.n,
            stop=None,
            temperature=0.5,
        )

        return response.choices[0].text.strip()
