
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


path = "day1\day1_input.txt"
dataset = parseData(path)
coordinates = createCoordinates(dataset)
result = sumCoordinates(coordinates)
print(f"The answer is {result}")