import discord
from discord.ext import commands


class DiscoBot():
    def __init__(self, key):
        self.key=key

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
    
    def CreateClient(self):
        intents = discord.Intents.default()
        intents.typing = False
        intents.message_content = True  # Add this line to include the message_content intent
        
        bot = commands.Bot(command_prefix="!", intents=intents)
        
        @bot.event
        async def on_ready():
            print(f'Logged in as {bot.user.name}')

        @bot.command()
        async def hello(ctx):
            print("triggered")
            await ctx.send(f'Hello, {ctx.author.name}!')
        
        bot.run(self.key)
    



    

