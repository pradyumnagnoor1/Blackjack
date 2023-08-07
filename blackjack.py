from ascii import cardAscii
from art import *
import random
import sys

# get card value
def cardValue(card):

    rank = card.split()[0]

    if rank in ['J', 'Q', 'K']:
        return 10

    elif rank == 'A':
        return 11

    else:
        return int(rank)



# calculate hand value
def handValue(hand):

    value = sum(cardValue(card) for card in hand)

    if 'A' in hand and value > 21:
        value -= 10

    return value


# draw card
def drawCard():
    Suits = ["\u2663", "\u2665", "\u2666", "\u2660"]

    Ranks = ['A', '2', '3', '4', '5',
         '6', '7', '8', '9', '10',
         'J', 'Q', 'K']

    deck = []

    for suit in Suits:
        for rank in Ranks:
            deck.append(f"{rank} {suit}")

    return random.choice(deck)


#format to print ascii cards and point counter
def fmtName(hand1):
    for card in hand1:
        rank, suit = card.split()
        asciiCard = cardAscii(rank, suit)
        print(asciiCard, end='')

    print(f"{handValue(hand1)} points")


#Score comparison between player and dealer
def compareScores(dealerScore, playerScore):

    if playerScore == 21 and dealerScore != 21:
        tprint("BLACKJACK! YOU WIN!!", font="small")

    elif dealerScore == 21 and playerScore != 21:
        tprint("Dealer Blackjack, you lose", font="small")

    elif dealerScore > 21:
        tprint("Dealer bust! You win!", font="small")

    elif playerScore > 21:
        tprint("Bust. Dealer wins.", font="small")

    elif dealerScore > playerScore:
        tprint("Dealer wins", font="small")

    elif playerScore > dealerScore:
        tprint("You win!!", font="small")

    elif playerScore == dealerScore:
        tprint("Push!", font="small")

    return ""

#blackjack game

def main():
    print()
    print("Welcome to Blackjack!")
    playerHand = []
    dealerHand = []

    for _ in range(2):
        playerHand.append(drawCard())

    dealerHand.append(drawCard())



    print("Your hand: ")
    fmtName(playerHand)
    print()
    print(f"Dealer hand: ")
    fmtName(dealerHand)
    print()
    while handValue(playerHand) < 21:
        playerScore = handValue(playerHand)
        action = input("Hit or Stand? (type in 'h' or 's'): ").lower()

        if action == 'h':
            print()
            playerHand.append(drawCard())
            playerScore = handValue(playerHand)
            if playerScore > 21:
                print("Final scores")
                fmtName(playerHand)
                fmtName(dealerHand)
                sys.exit("Bust. Dealer wins.")
            else:
                print(f"Your hand: ")
                fmtName(playerHand)
                print()
                print(f"Dealer hand: ")
                fmtName(dealerHand)
                print()

        elif action == 's':
            break

    playerScore = handValue(playerHand)



    while handValue(dealerHand) < 17:
        dealerHand.append(drawCard())

    dealerScore = handValue(dealerHand)

    print()
    print("Final scores")
    fmtName(playerHand)
    fmtName(dealerHand)

    result = compareScores(dealerScore, playerScore)
    print()
    print()
    print(result)
    print()

    while True:
        playAgain = input("Play again? (type in 'y' or 'n'): ")

        if playAgain == 'y':
            main()
        else:
            sys.exit()





main()
