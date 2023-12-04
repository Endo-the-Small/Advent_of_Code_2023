# import the data in a readable format
def parseData(data):
    dataset = []
    with open(data, 'r') as file:
        for line in file:
            dataset.append(line.strip())
    return dataset

# create a set of coordinates based on the strings
def createCoordinates(dataset):
    coordinateList = []

    replacements = {'one':'1',
                    'two':'2',
                    'three':'3',
                    'four':'4',
                    'five':'5',
                    'six':'6',
                    'seven':'7',
                    'eight':'8',
                    'nine':'9'}
    
    #find first number in sequence
    def firstNumber(string):
        i = 0
        while i <= len(string):
            if string[i].isdigit():
                return int(string[i])
            else:
                for word, number in replacements.items():
                    if string[i:].startswith(word):
                        return int(number)
            i += 1

    #find last number in sequence
    def lastNumber(string):
        i = len(string)
        while i >= 0:
            if string[i-1].isdigit():
                return int(string[i-1])
            else:
                for word, number in replacements.items():
                    if string[:i].endswith(word):
                        return int(number)
            i -= 1

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


path = "day1\day1_input.txt"
dataset = parseData(path)
coordinates = createCoordinates(dataset)
result = sumCoordinates(coordinates)
print(f"The answer is {result}")