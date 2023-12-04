
# read through the data and create a structure to store the games

def parseData(path):
    gameArray = {}
    with open(path, 'r') as file:
        for line in file:
            gameID = int(line.replace("Game ","").split(":")[0])
            rolls = line.split(':')[1].split(";")
            game = []
            for roll in rolls:
                r = {'red':0, 'blue':0, 'green':0}
                i = roll.replace(' ','').split(',')
                for record in i:
                    for colour in r:
                        if colour in record:
                            numberOfCubes = record.replace(colour,'')
                            r[colour] = int(numberOfCubes)
                game.append(r)
            gameArray[gameID] = game
        return gameArray

# find the max cubes displayed per game

def maxCubes(gameArray):
    maxCubeResult = {}
    gameID = 1
    while gameID <= len(gameArray):
        r = {'red':0, 'blue':0, 'green':0}
        for roll in gameArray[gameID]:
            for colour in r:
                if colour in roll:
                    r[colour] = max(r[colour],roll[colour])
        maxCubeResult[gameID] = r
        gameID += 1
    return maxCubeResult

# check if each game is possible

def checkPossibility(maxCubesResult, actualCubes):
    possibilityMatrix = {}
    for gameID, maxCubes in maxCubesResult.items():
        possible = True
        while possible == True:
            for colour, number in actualCubes.items():
                if colour in maxCubes and maxCubes[colour] > number:
                    possible = False
            possibilityMatrix[gameID] = possible
            possible = False
    return possibilityMatrix

def sumOfPossible(games):
    runningTotal = 0
    for game, possible in games.items():
        if possible == True:
            runningTotal += game
    return runningTotal

def cubePower(allGames):
    gamePower = {}
    for gameID, cubes in allGames.items():
        gamePower[gameID] = cubes['red'] * cubes['green'] * cubes['blue']
    return gamePower

def sumCubePower(cubePower):
    megaAwesomeCubePower = 0
    for gameID, power in cubePower.items():
        megaAwesomeCubePower += power
    return megaAwesomeCubePower

path = "day2\day2_input.txt"
gameArray = parseData(path)
maxCubesResult = maxCubes(gameArray)
actualCubes = {'red': 12, 'blue': 14, 'green': 13}
possibilityMatrix = checkPossibility(maxCubesResult, actualCubes)
firstResult = sumOfPossible(possibilityMatrix)
print(f"The answer to the first problem is {firstResult}")
powerOfCubes = cubePower(maxCubesResult)
secondResult = sumCubePower(powerOfCubes)
print(f"The answer to the second problem is {secondResult}")