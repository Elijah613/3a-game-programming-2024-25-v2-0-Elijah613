# Twenty One by Elijah Reed, v0.1

import random

# PLAYER DATA
playerTotal = 0
playerScore = 0
playerChoice = None

# CPU DATA
cpuTotal = 0
cpuScore = 0
cpuChoice = None

# Allow player to input their name.
playerName = input("Hello player, please type your name and press the ENTER key.\n")
print(f"You typed {playerName}. Is that right?\n")
isCorrect = input("Is that right? Type yes or no then press the ENTER key.\n").lower()

if isCorrect == "yes":
    print(f"Now {playerName}, let's play TWENTY ONE.\n")
else:
    playerName = input("Type your name correctly this time.\n")

# Explain the rules.
print("""
Welcome to TWENTY ONE. This is a card game all based on your luck, however we ran out of cards.
Here's how to play:

The goal is to get the closest to 21. Don't go over 21 or the win will be given to the CPU. You will recieve two cards at the start of each round.
If you want to get another card, say "HIT". Then you will get another card onto your total number.
If you are satisfied with your total, say "STAY". Your turn will be over and the CPU will make its decisions.

After both you and the CPU are done with your turns, the totals and winner will be displayed.
""")

# Give the player 2 cards (two random ints).
playerCard1 = random.randint(1,10)
playerCard2 = random.randint(1,10)

playerCard3 = random.randint(1,10)
playerCard4 = random.randint(1,10)
playerCard5 = random.randint(1,10)
playerCard6 = random.randint(1,10)
playerCard7 = random.randint(1,10)
playerCard8 = random.randint(1,10)
playerCard9 = random.randint(1,10)
playerCard10 = random.randint(1,10)

playerTotal = playerCard1 + playerCard2
print(f"You got a {playerCard1} and a {playerCard2} to start with.")

# Give the CPU two cards.
cpuCard1 = random.randint(1,10)
cpuCard2 = random.randint(1,10)

cpuCard3 = random.randint(1,10)
cpuCard4 = random.randint(1,10)
cpuCard5 = random.randint(1,10)
cpuCard6 = random.randint(1,10)
cpuCard7 = random.randint(1,10)
cpuCard8 = random.randint(1,10)
cpuCard9 = random.randint(1,10)
cpuCard10 = random.randint(1,10)

cpuTotal = cpuCard1 + cpuCard2

# Allow player the choice to HIT or STAY.
while playerScore < 5 and cpuScore < 5:
    while playerChoice != "stay":
        playerChoice = input("Now what will it be, HIT or STAY\n").lower()
        if playerChoice == "hit":
            playerTotal + playerCard3
            print(f"You got a {playerCard3}.")
            print(f"Your new total is {playerTotal}.")
            if playerTotal > 21:
                print("You Bust! CPU wins this round")
                playerTotal = 0 
                cpuScore += 1
        playerChoice = input("Again, HIT or STAY\n").lower()
        if playerChoice == "hit":
            playerTotal + playerCard4
            print(f"You got a {playerCard4}.")
            print(f"Your new total is {playerTotal}.")
            if playerTotal > 21:
                print("You Bust! CPU wins this round")
                playerTotal = 0 
                cpuScore += 1
        playerChoice = input("Again, HIT or STAY\n").lower()
        if playerChoice == "hit":
            playerTotal + playerCard5
            print(f"You got a {playerCard5}.")
            print(f"Your new total is {playerTotal}.")
            if playerTotal > 21:
                print("You Bust! CPU wins this round")
                playerTotal = 0 
                cpuScore += 1
        playerChoice = input("Again, HIT or STAY\n").lower()
        if playerChoice == "hit":
            playerTotal + playerCard6
            print(f"You got a {playerCard6}.")
            print(f"Your new total is {playerTotal}.")
            if playerTotal > 21:
                print("You Bust! CPU wins this round")
                playerTotal = 0 
                cpuScore += 1
        if playerChoice == "hit":
            playerTotal + playerCard7
            print(f"You got a {playerCard7}.")
            print(f"Your new total is {playerTotal}.")
            if playerTotal > 21:
                print("You Bust! CPU wins this round")
                playerTotal = 0 
                cpuScore += 1
        if playerChoice == "hit":
            playerTotal + playerCard8
            print(f"You got a {playerCard8}.")
            print(f"Your new total is {playerTotal}.")
            if playerTotal > 21:
                print("You Bust! CPU wins this round")
                playerTotal = 0 
                cpuScore += 1
        if playerChoice == "hit":
            playerTotal + playerCard9
            print(f"You got a {playerCard9}.")
            print(f"Your new total is {playerTotal}.")
            if playerTotal > 21:
                print("You Bust! CPU wins this round")
                playerTotal = 0 
                cpuScore += 1
        if playerChoice == "hit":
            playerTotal + playerCard10
            print(f"You got a {playerCard10}.")
            print(f"Your new total is {playerTotal}.")
            if playerTotal > 21:
                print("You Bust! CPU wins this round")
                playerTotal = 0 
                cpuScore += 1

        elif playerChoice == "stay":
            print("Your turn is over\n")

    while cpuChoice != "stay":
        cpuChoice = random.randint(0,1)
        pass



# For HIT -- Give the player another card and add it to their total.
# For STAY -- Pass the turn to the CPU.
# Allow CPU to HIT or STAY.
# Once both stay, output results and winner.