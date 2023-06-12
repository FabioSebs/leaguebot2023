import discord
from discord.ext import commands
from deon.openai import ChatGPT
import array as arr
from . import hashmap
from . import redisai
from . import cmd

class DiscoBot():
    def __init__(self, key, aikey):
        self.key=key
        self.AI=ChatGPT(aikey) 

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
    
    def CreateClient(self):
        intents = discord.Intents.default()
        intents.typing = False
        intents.message_content = True  
        
        bot = commands.Bot(command_prefix="!", intents=intents)
        
        @bot.event
        async def on_ready():
            print(f'Logged in as {bot.user.name}')

        @bot.event
        async def on_message(message):
            # CHECK PREFIX
            if message.author == bot.user or message.content[0] != '!':
                return
            
            #INFO COMMAND
            if await cmd.InfoComand(message.content, message):
                return

            #CHARACTER INFO
            if await cmd.ChampInfo(message.content, message, self.AI):
                return

            #MATCHUP INFO 
            if await cmd.ChampMatchup(message.content, message, self.AI):
                return
            
        bot.run(self.key)
           




    
