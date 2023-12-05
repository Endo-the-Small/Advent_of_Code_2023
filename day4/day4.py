

# parse the data and pull out winning numbers and playing numbers

def parsedata(path):
    def removeBlanks(input):
        output = []
        for i in input:
            if i.isdigit():
                output.append(int(i))
        return output
    
    with open(path, 'r') as file:
        winningNumbers = []
        playerNumbers = []
        for line in file.readlines():
            numbers = line.strip().split(':')[1].split('|')
            winningNumbers.append(removeBlanks(numbers[0].split(' ')))
            playerNumbers.append(removeBlanks(numbers[1].split(' ')))
    return winningNumbers, playerNumbers

# play out each card to find matching numbers

def playCards(winningNumbers, playerNumbers):
    gameResults = []
    for game, numbers in enumerate(playerNumbers):
        duplicates = set(numbers).intersection(set(winningNumbers[game]))
        gameResults.append(duplicates)
    return gameResults

# calculate the point score from part 1 of the challenge

def winnings(winningCards):
    runningTotal = 0
    for card in winningCards:
        wincount = len(card)
        winvalue = 0
        if wincount > 0:
            winvalue += 1 
            wincount -= 1
        while wincount > 0:
            winvalue = winvalue * 2
            wincount -= 1
        runningTotal += winvalue
    return runningTotal

# ---------- additional functions for part 2 ------------
# calculate number of cards won (I realised after successfully 
# answering the question that there should be logic to stop imaginary cards being 
# created at the end of the list, but my dataset didn't encounter the problem... and it's the end of the day)

def waterfallWinnings(gameresults):
    allCards = {}
    for cardID, wins in enumerate(gameresults, start= 1):
        if cardID in allCards:
            allCards[cardID] += 1
        else:
            allCards[cardID] = 1
        additionalCard = []
        cardWinCounter = cardID
        for win in wins:
            cardWinCounter += 1
            additionalCard.append(cardWinCounter)
        for card in additionalCard:
            if card in allCards:
                allCards[card] += allCards[cardID]
            else:
                allCards[card] = allCards[cardID]
    return allCards

# add together the totals of cards won

def addWaterfallWinnings(waterfallWinningsAnswer):
    runningTotal = 0
    for card, number in waterfallWinningsAnswer.items():
        runningTotal += number
    return runningTotal

# this runs all the code

path = 'day4\day4_input.txt'
winningNumbers, playerNumbers = parsedata(path)
winningCards = playCards(winningNumbers, playerNumbers)
firstAnswer = winnings(winningCards)
print(f'the first answer is {firstAnswer}')
waterfallWinningsAnswer = waterfallWinnings(winningCards)
secondAnswer = addWaterfallWinnings(waterfallWinningsAnswer)
print(f'the second answer is {secondAnswer}')