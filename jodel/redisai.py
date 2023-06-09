import redis

r = redis.Redis(host='redis', port=6379, decode_responses=True)

def SetRedis(name, champ, reply):
    r.setex(name+champ, 60*60*24, reply)

def GetRedis(name, champ):
    return r.get(name+champ)

