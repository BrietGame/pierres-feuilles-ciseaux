from enum import Enum
import random

class Items(Enum):
    PIERRE = 1
    FEUILLE = 2
    CISEAUX = 3

def getItems():
    return Items

def getItem(item):
    return Items[item].name

def getList():
    return list(Items);

def getRandomItem():
    return random.choice(getList())