path = "day1\day1_input.txt"

def parseData(dataToAnalyse):
    calibrationValues = []
    
    with open(dataToAnalyse, 'r') as file:
        data = file.readlines()

        for line in data:
            firstNumber = 0
            lastNumber = 0
            while firstNumber == 0:
                for char in line:
                    if char.isdigit():
                        firstNumber = int(char)
            while lastNumber == 0:
                for char in reversed(line):
                    if char.isdigit():
                        lastNumber = int(char)
            calibrationValues.append((lastNumber * 10) + firstNumber)
    return(calibrationValues)

def addNumbers(numbers):
    runningTotal = 0
    for number in numbers:
        runningTotal += number
    return runningTotal

dataset = parseData(path)
sum = addNumbers(dataset)
print(sum)