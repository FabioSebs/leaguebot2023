from . import hashmap
from . import redisai

def GetChampPrompt(name, champ):
    return f'Hey my name is {name} please say my name. Now tell me all you can about the champion in league of legends named {champ}'

def GetMatchupPrompt(champ1, champ2):
    return f'Tell me about the matchup between {champ1} and {champ2} in the game of league of legends.'

async def InfoComand(msg, msnger):
    if msg == "!info":
        await msnger.channel.send()
        return True
    return False
    
async def ChampInfo(msg, msnger, ai):
    champ = msg[1:].lower()
    author = f'{msnger.author}'[:-5]
    idx = hashmap.hashChamp(champ=champ)

    if champ not in hashmap.champList[idx]:
        return False
    
    if redisai.GetRedis(author, champ) == None:
        reply = ai.ask(GetChampPrompt(author, champ= champ))
        redisai.SetRedis(author, champ, reply.choices[0].text.replace('\n', ''))
        await msnger.channel.send(reply.choices[0].text.replace('\n', ''))
        return True

    else:
        await msnger.channel.send(redisai.GetRedis(author, champ))
        return True
    
async def ChampMatchup(msg, msnger, ai):
    fullmsg = msg[1:].lower()
    champs = fullmsg.split(":")

    if len(champs) != 2:
        return False
   
    reply = ai.ask(GetMatchupPrompt(champs[0], champs[1]))
    await msnger.channel.send(reply.choices[0].text.replace('\n', ''))
    return True

    