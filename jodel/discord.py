import discord
from discord.ext import commands
from deon.openai import ChatGPT

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

        @bot.command()
        async def hello(ctx):
            print("triggered")
            await ctx.send(f'Hello, {ctx.author.name}!')

        @bot.event
        async def on_message(message):
            # INFINITE LOOP CHECK
            if message.author == bot.user:
                return
            
            champ = message.content[1:]
            reply = self.AI.ask(PROMPT+champ)
            await message.channel.send(reply.choices.text.replace('\n', ''))

        bot.run(self.key)
    



    
