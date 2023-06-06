import openai
from decouple import config
from jodel.discord import DiscoBot

mybot = DiscoBot(config("DISCO_TOKEN"), config("OAI_SECRET"))
mybot.CreateClient()
