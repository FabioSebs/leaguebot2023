import openai
from decouple import config
from jodel.discord import DiscoBot
from deon.openai import ChatGPT

ai = ChatGPT(config("OAI_SECRET"))
print(ai.ask("how are you?"))
# mybot = DiscoBot(config("DISCO_SECRET"))
# mybot.RunClient()
