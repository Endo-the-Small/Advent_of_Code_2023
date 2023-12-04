

# parse through the data to capture the details

def parseData(path):
    with open(path, 'r') as file:
        # create a blueprint using x, y coordinates
        x = 0
        y = 0
        blueprint = {}
        parts = {}
        partNumber = 1
        for line in file:
            cleanLine = line.strip()
            # run through each character and assign it to an x, y reference
            for index, char in enumerate(cleanLine):
                if x > index:
                    continue
                elif char =='.':
                    blueprint[(x, y)] = False
                    x += 1
                elif char =='*':
                    blueprint[(x, y)] = 'gear'
                    x += 1
                elif char.isdigit():
                    partValue = 0
                    partXY = []
                    # this is logic to capture numbers one two and three digits long
                    if index + 2 < len(cleanLine) and cleanLine[index + 2].isdigit():
                            partValue = int(cleanLine[index:index + 3])
                            partXY = [(x, y),(x + 1, y),(x + 2, y)]
                            blueprint[(x, y)] = (partNumber, partValue)
                            blueprint[(x + 1, y)] = (partNumber, partValue)
                            blueprint[(x + 2, y)] = (partNumber, partValue)
                            x += 3
                    elif index + 1 < len(cleanLine) and cleanLine[index + 1].isdigit():
                            partValue = int(cleanLine[index:index + 2])
                            partXY = [(x, y),(x + 1, y)]
                            blueprint[(x, y)] = (partNumber, partValue)
                            blueprint[(x + 1, y)] = (partNumber, partValue)
                            x += 2
                    else:
                        partValue = int(char)
                        partXY = [(x, y)]
                        blueprint[(x, y)] = (partNumber, partValue)
                        x += 1
                    parts[(partNumber, partValue)] = partXY
                    partNumber += 1
                else:
                    blueprint[(x, y)] = True
                    x += 1
                
            y += 1
            x = 0
        return blueprint, parts

# sort through the parts and work out which should be counted

def validateParts(blueprint, parts):
    correctParts = []
    for part, coordinates in parts.items():
        for x, y in coordinates:
            xCheck = -1
            yCheck = -1
            while yCheck <= 1 and part not in correctParts:
                while xCheck <= 1 and part not in correctParts:
                    coordToCheck = (x + xCheck, y + yCheck)
                    if coordToCheck in blueprint and (blueprint[coordToCheck] == True or blueprint[coordToCheck] == 'gear'):
                            correctParts.append(part)
                    xCheck += 1
                yCheck += 1
                xCheck = -1
    return correctParts

# sum the correct parts
def sumParts(correctParts):
    runningTotal = 0
    for part, value in correctParts:
        runningTotal += value
    return runningTotal

#find the number connected to gears

def gearRatio(blueprint):
    gearDetails = {}
    for coordinate, value in blueprint.items():
        if value == 'gear':
            gearDetails[coordinate] = []
            xCheck = -1
            yCheck = -1
            while yCheck <= 1:
                while xCheck <= 1:
                    coordToCheck = (coordinate[0] + xCheck, coordinate[1] + yCheck)
                    if coordToCheck in blueprint and (type(blueprint[coordToCheck]) != bool and blueprint[coordToCheck] != 'gear'):
                        if blueprint[coordToCheck] not in gearDetails[coordinate]:
                            gearDetails[coordinate].append(blueprint[coordToCheck])
                    xCheck += 1
                yCheck += 1
                xCheck = -1
    return gearDetails

#calculate gear ratios ofr  gears with 2 connections

def calculateRatios(gearDetails):
    runningTotal = 0
    for gear, value in gearDetails.items():
        if len(value) == 2:
            runningTotal += value[0][1] * value[1][1]
    return runningTotal

path = 'day3\day3_input.txt'
blueprint, parts = parseData(path)
correctParts = validateParts(blueprint, parts)
firstAnswer = sumParts(correctParts)
print(f'The first answer is {firstAnswer}')
gearDetails = gearRatio(blueprint)
secondAnswer = calculateRatios(gearDetails)
print(f'The second answer is {secondAnswer}')