
# import the data in a readable format
def parseData(data):
    dataset = []
    with open(data, 'r') as file:
        for line in file:
            dataset.append(line.strip())
    return dataset


# replace words for numbers, from left to right
# this didn't work and was getting messy! so I started again with attempt 2
# rather that replacing text I decided to try searching text in a different way
def textToInt(dataToClean):
    cleanedCoordinates = []
    replacements = {'one':'1',
                    'two':'2',
                    'three':'3',
                    'four':'4',
                    'five':'5',
                    'six':'6',
                    'seven':'7',
                    'eight':'8',
                    'nine':'9'}
    def numberWang(string):
        newString = ''
        i = 0
        while i < len(string):
            replaced = False
            for number, wang in replacements.items():
                if string[i:].startswith(number):
                    newString += wang
                    i += len(number)
                    replaced = True
                    break
            if not replaced:
                newString += string[i]
                i += 1
            else:
                newString += string[i:]
                i = len(string)
        return newString
    def WangerNum(string):
        newString = ''
        i = len(string)
        while i >= 0:
            replaced = False
            for number, wang in replacements.items():
                if string[:i].endswith(number):
                    newString = wang +newString
                    i -= len(number)
                    replaced = True
                    break
            if not replaced and i > 0:
                newString = string[i-1] + newString
                i -= 1

            else:
                newString = string[:i] + newString
                i = -1
        return newString
    
    for i in dataToClean:
        newValue = numberWang(i)
        newerValue = WangerNum(newValue)
        cleanedCoordinates.append(newerValue)
    return cleanedCoordinates

# create a set of coordinates based on the strings
def createCoordinates(dataset):
    coordinateList = []

    #find first number in sequence
    def firstNumber(string):
        for char in string:
            if char.isdigit():
                return int(char)

    #find last number in sequence
    def lastNumber(string):
        for char in reversed(string):
            if char.isdigit():
                return int(char)

    #create new dataset with first and second number
    def makeCoordinate(firstNumber, lastNumber):
        coordinate = firstNumber * 10 + lastNumber
        return coordinate
    
    for line in dataset:
        firstNumberValue = firstNumber(line)
        lastNumberValue = lastNumber(line)
        coordinatesValue = makeCoordinate(firstNumberValue,lastNumberValue)
        coordinateList.append(coordinatesValue)
    
    return coordinateList

#calculate sum of coordinates
def sumCoordinates(coordinates):
    runningTotal = 0
    for entry in coordinates:
        runningTotal += entry
    return runningTotal


path = "day1\day1_part2_input.txt"
dataset = parseData(path)
newstrings = textToInt(dataset)
print(newstrings)
coordinates = createCoordinates(newstrings)
print(coordinates)
result = sumCoordinates(coordinates)
print(f"The answer is {result}")

