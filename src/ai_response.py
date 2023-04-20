import openai
import os


class AiResponse:
    def __init__(self):
        self.max_tokens = 100
        self.model = "text-davincii-002"
        self.n = 1
        self.openai_key = os.getenv("OPENAI_KEY")
        openai.api_key = self.openai_key

    def get_response(self, message):
        response = openai.Completion.create(
            engine=self.model,
            prompt=message.content.lower(),
            max_tokens=self.max_tokens,
            n=self.n,
            stop=None,
            temperature=0.5,
        )

        return response.choices[0].text.strip()
