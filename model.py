# Здесь храним все перменные и методы для их чтения и установки

total_candies = 150
max_candy = 28
min_candy = 1
take_user = 0
players = 0

def getCandies() -> int:
    global total_candies
    return total_candies

def setCandies(leftover: int):
    global total_candies
    total_candies = leftover

def checkWinner():
    if getCandies() <= 27:
        return True

def takeUser():
    global take_user
    return take_user

def setPlayer(player):
    global players
    players = player

def getPlayer() -> int:
    global total_candies
    return total_candies

def maxCandy():
    global max_candy
    return max_candy

def minCandy():
    global min_candy
    return min_candy
