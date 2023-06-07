import discord
from discord.ext import commands
from deon.openai import ChatGPT
import json

PROMPT = "tell me all you know about the champion in league of legends named "

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

            if message.author == bot.user or message.content[0] != '!':
                return
            
            if message.content == '!info':
                await message.channel.send('I am a LeagueBot powered by ChatGPT and created by Fabrzy! The best player in the server, please use me if you need to know any champion information')
                return
            
            
            
            # TODO: HASH MAP / INDEX THE CHAMPS
            champ = message.content[1:].lower()
            usersList = getJSON()
            if champ not in usersList:
                await message.channel.send("I am not qualified to answer this question. You either spelled the name of a champ wrong or are retarded.")
                return
            
            reply = self.AI.ask(PROMPT+champ)
            await message.channel.send(reply.choices[0].text.replace('\n', ''))
            
        bot.run(self.key)
           

def getJSON():
    with open('leaguechamps.json') as file:
        data = json.load(file)
    return [x['user'].lower() for x in data]

      
    



    
