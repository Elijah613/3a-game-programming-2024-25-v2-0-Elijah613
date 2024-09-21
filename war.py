# War by Elijah Reed, v0.2

import random

cardsInDeck = 52

# PLAYER DATA
playerScore = 0
playerCard = 0

# CPU DATA
cpuScore = 0
cpuCard = 0

# NAME INPUT
playerName = input("Hello player, please type your name and press the ENTER key.\n")
print(f"You typed {playerName}.\n")
isCorrect = input("Is that right? Type yes or no then press the ENTER key.\n").lower()

if isCorrect == "yes":
    print(f"Good, now {playerName}, time to battle.\n")
else:
    playerName = input("Type your name correctly this time.\n")

# RULE EXPLANATION
print("""
Welcome to WAR. This is a luck-based card game, but in the terminal.
Here's how it works:
      
    Both you and the CPU will draw a card, whoever has the higher value will win the round and gain 2 points.
    However, if both cards are equal, there will be another draw and whoever wins that round will recieve 4 points.
      
    The game will continue until all 52 cards are used. Whoever has the highest point score wins the whole game.
""")

while cardsInDeck != 0:

    nextRound = input("Ready for the draw?\n").lower()
    if nextRound == "yes":
        playerCard = random.randint(1,10)
        cpuCard = random.randint(1,10)
        print(f"Your card is a {playerCard}.")
        print(f"The CPU's card was a {cpuCard}.\n")

        if playerCard > cpuCard:
            print("You win!")
            playerScore += 2
            cardsInDeck -= 2
        elif playerCard < cpuCard:
            print("You lose!")
            cpuScore += 2
            cardsInDeck -= 2
        elif playerCard == cpuCard:
            print("Oh, a draw? Time for WAR!\n")

            playerCard = random.randint(1,10)
            cpuCard = random.randint(1,10)
            print(f"Your top card is a {playerCard}.")
            print(f"The top CPU's card was a {cpuCard}.")

            if playerCard > cpuCard:
                print("You win!")
                playerScore += 4
                cardsInDeck -= 4
            elif playerCard < cpuCard:
                print("You lose!")
                cpuScore += 4
                cardsInDeck -= 4
        print(f"\nYour score is {playerScore}.")
        print(f"The CPU's score is {cpuScore}.")
        print(f"There are {cardsInDeck} cards left in the deck.\n")
    elif nextRound == "no":
        print("You forfeit the game. So long, loser.\n")
        exit()

print("The deck has run out. Let's get the scores.")
print(f"Your final score was {playerScore} and the CPU's final score was {cpuScore}.")
if playerScore > cpuScore:
    print("You have won the game..... somehow.\n")
elif playerScore < cpuScore:
    print("HAHA, YOU SUCK.\n")
elif playerScore == cpuScore:
    print("There was no winner, tough luck.")

exit()
