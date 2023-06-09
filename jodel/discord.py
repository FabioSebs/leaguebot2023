import discord
from discord.ext import commands
from deon.openai import ChatGPT
import array as arr
from . import hashmap
from . import redisai

def GetPrompt(name, champ):
    return f'Hey my name is {name} please say my name. Now tell me all you can about the champion in league of legends named {champ}'

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
            # INFINITE LOOP CHECK
            reply = ''

            if message.author == bot.user or message.content[0] != '!':
                return
            
            if message.content == '!info':
                await message.channel.send('I am a LeagueBot powered by ChatGPT and created by Fabrzy! The best player in the server, please use me if you need to know any champion information')
                return
        
            champ = message.content[1:].lower()
            author = f'{message.author}'[:-5]
            idx = hashmap.hashChamp(champ)

            if champ not in hashmap.champList[idx]:
                await message.channel.send("I am not qualified to answer this question. You either spelled the name of a champ wrong or are retarded.")
                return
            
            if redisai.GetRedis(author, champ) == None:
                reply = self.AI.ask(GetPrompt(author, champ= champ))
                redisai.SetRedis(author, champ, reply.choices[0].text.replace('\n', ''))
                await message.channel.send(reply.choices[0].text.replace('\n', ''))
            
            else:
                print(redisai.GetRedis(author, champ))
                await message.channel.send(redisai.GetRedis(author, champ))
            
        bot.run(self.key)
           




    
