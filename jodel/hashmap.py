import json

INDEX = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4, "f": 5, "g": 6, "h": 7, "i": 8, "j": 9, "k": 10, "l": 11, "m": 12, "n": 13, "o": 14, "p": 15, "q": 16, "r": 17, "s": 18, "t": 19, "u": 20, "v": 21, "w": 22, "x": 23, "y": 24, "z": 25}

# OPENING JSON FILE AND MAKING AN ARRAY
def getJSON():
    with open('leaguechamps.json') as file:
        data = json.load(file)
    return [x['user'].lower() for x in data]


# DATA STRUCTURE GENERATOR FUNCTION FOR CHAMP HASH MAP
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

champList = champHashMap()


    