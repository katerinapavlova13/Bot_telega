# Здесь храним все перменные и методы для их чтения и установки (а-ля работа с классами)

total_candy = 150
max_candy = 28
min_candy = 1

def getCandies():
    global total_candy
    return total_candy

def checkWinner():
    if getCandies() <= 28:
        return True

def setCandies(count: int):
    global total_candy
    total_candy = count

