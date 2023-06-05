import openai

class ChatGPT:
    def __init__(self, key):
        self.key = key

    def ask(self, prompt):
        openai.api_key = self.key
        response = openai.Completion.create(
            model="text-davinci-003", 
            prompt=prompt, 
            temperature=0, 
            max_tokens=300
        )
        return response

