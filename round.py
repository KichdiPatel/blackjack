import random
import time


cards = [['A','2','3','4','5','6','7','8','9','10','J','Q','K'],    # 0 = Diamonds
         ['A','2','3','4','5','6','7','8','9','10','J','Q','K'],    # 1 = Hearts
         ['A','2','3','4','5','6','7','8','9','10','J','Q','K'],    # 2 = Clubs
         ['A','2','3','4','5','6','7','8','9','10','J','Q','K']]    # 3 = Spades

reset = [['A','2','3','4','5','6','7','8','9','10','J','Q','K'],    # 0 = Diamonds
         ['A','2','3','4','5','6','7','8','9','10','J','Q','K'],    # 1 = Hearts
         ['A','2','3','4','5','6','7','8','9','10','J','Q','K'],    # 2 = Clubs
         ['A','2','3','4','5','6','7','8','9','10','J','Q','K']]    # 3 = Spades

suits = ["D","H","C","S"]

BALANCE = 200

CURRENT_BET = 0

def newPage():
    for i in range(70):
        print()

def getCard():
    suit = random.choice(range(4))
    num = random.choice(range(len(cards[suit])))
    while(len(cards[suit]) == 0):
        suit = random.choice(range(4))
    card = cards[suit].pop(num)
    
    return card + suits[suit] 

def getHandVal(arr):
    total = 0
    a_count = 0

    for c in arr:
        if(c[0:2] == '10'):
            val = c[0:2]
        else:
            val = c[0]
        if(val != 'A'):
            if(val == 'J' or val == 'Q' or val == 'K'):
                total += 10
            else:
                total += int(val)
        else:
            a_count += 1

    for i in range(a_count):
        acesLeft = a_count - i -1 
        if(total + 11 <= 21-acesLeft):
            total += 11
        else:
            total += 1
    
    return total    
        
def printBoard(dealerCards, playerCards, hidden):
    newPage()

    print("YOUR BALANCE:", BALANCE)
    
    print("CURRENT BET:", CURRENT_BET)
    
    print()

    if(hidden):
        print("Dealer Cards: " + dealerCards[0] + " XX")
    else:
        dealerCardString = ""
        for c in dealerCards:
            dealerCardString += c + " "
        print("Dealer Cards: " + dealerCardString + " = " + str(getHandVal(dealerCards)))

    print()

    playerCardString = ""
    for card in playerCards:
        playerCardString += card + " "
    print("Your Cards: " + playerCardString + " = " + str(getHandVal(playerCards)))

def round():
    dealerCards = [getCard(), getCard()]

    playerCards = [getCard(), getCard()]

    printBoard(dealerCards, playerCards, True)

    # PLAYER'S MOVE
    playerLost = False
    playerWon = False
    if(getHandVal(playerCards) == 21):
        playerWon = True
    
    while(playerWon == False and playerLost == False):
        move = input("Hit[h] or Stay[s]? ")
        if(move.lower() == 'h'):
            playerCards.append(getCard())
            printBoard(dealerCards, playerCards, True)
            playerHandVal = getHandVal(playerCards)
            if(playerHandVal > 21):
                print("------------YOU LOST - BUST------------")
                playerLost = True
                break
            elif(playerHandVal == 21):
                playerWon = True
                break
        else:
            break

    # DEALER'S MOVE
    printBoard(dealerCards, playerCards, False)
    time.sleep(2)
    playerVal = getHandVal(playerCards)
    
    dealerWon = True
    if(playerWon):
        dealerWon = False
    

    while(playerLost == False and playerWon == False):
        dealerVal = getHandVal(dealerCards)
        if(dealerVal > 21):
            dealerWon = False
            break
        elif(dealerVal >= playerVal):
            break
        else:
            dealerCards.append(getCard())
            printBoard(dealerCards, playerCards, False)
            time.sleep(2)

    if(dealerWon):
        print("------------YOU LOST - DEALER WON------------")
    else:
        print("************YOU WON - DEALER LOST************")
    
    return not dealerWon

def game(BALANCE, CURRENT_BET):
    BALANCE -= int(CURRENT_BET)
    playerWin = round()

    if(playerWin):
        BALANCE += (int(CURRENT_BET) * 2)

    return BALANCE

#####MAIN######
resetCounter = 0
while(BALANCE != 0):
    print("******************STARTING NEW ROUND******************")
    # time.sleep(2)
    print("YOUR BALANCE: ", BALANCE)
    CURRENT_BET = input("What is your bet? ")

    BALANCE = game(BALANCE, CURRENT_BET)
    resetCounter += 1
    time.sleep(4)

    if(resetCounter >= 4 or len(cards[0]) == 0 or len(cards[1]) == 0 or len(cards[2]) == 0 or len(cards[3]) == 0):
        newPage()
        print("SHUFFLING DECK")
        time.sleep(2)
        cards = reset
        resetCounter = 0
    
    
    CURRENT_BET = 0
    newPage()

print("YOU LOST ALL YOUR MONEY")

