import discord

class DiscoBot():
    def __init__(self, key):
        self.key=key

    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')
    
    def CreateClient(self):
        intents = discord.Intents.default()
        intents.message_content = True
        client = DiscoBot(intents=intents)
        return client
    
    def RunClient(self):   
        self.createClient().run(self.key)


    

