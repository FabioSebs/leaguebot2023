import discord
from discord.ext import commands
from deon.openai import ChatGPT
import json
import array as arr

PROMPT = "tell me all you know about the champion in league of legends named "
INDEX = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "j": 9, "k": 10, "l": 11, "m": 12, "n": 13, "o": 14, "p": 15, "q": 16, "r": 17, "s": 18, "t": 19, "u": 20, "v": 21, "w": 22, "x": 23, "y": 24, "z": 25}

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
            
            champ = message.content[1:].lower()
            champList = champHashMap()
            idx = hashChamp(champ)
            if champ not in champList[idx]:
                await message.channel.send("I am not qualified to answer this question. You either spelled the name of a champ wrong or are retarded.")
                return
            
            reply = self.AI.ask(PROMPT+champ)
            await message.channel.send(reply.choices[0].text.replace('\n', ''))
            
        bot.run(self.key)
           

def champHashMap():
    champs = getJSON()
    sorted_champs = sorted(champs)
    hashmap = [[] for _ in range(26)]
    for champ in sorted_champs:
        idx = hashChamp(champ)
        hashmap[idx].append(champ)
    return hashmap

def hashChamp(champ):
    # returns the index where the champ should go in the 2d array
    return INDEX[champ[0]]


def getJSON():
    with open('leaguechamps.json') as file:
        data = json.load(file)
    return [x['user'].lower() for x in data]

      
    



    
