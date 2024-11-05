# Twenty One by Elijah Reed, v0.2

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


# Give the CPU two cards.
playerCard1 = random.randint(1,10)
playerCard2 = random.randint(1,10)
playerRandomCard = 0
playerTotal = playerCard1 + playerCard2
print(f"You got a {playerCard1} and a {playerCard2} to start with.")   

# Allow player the choice to HIT or STAY.
while playerScore < 5 and cpuScore < 5:
    while playerChoice != "stay" and playerTotal <= 21:
        playerChoice = input("Now what will it be, HIT or STAY\n").lower()
        if playerChoice == "hit":
            playerRandomCard = random.randint(1,10)
            playerTotal = playerTotal + playerRandomCard
            print(f"You got a {playerRandomCard}")
            print(f"Your new total is {playerTotal}")

        elif playerChoice == "stay":
            print("Your turn is over. Time for the CPU's turn.\n")
    
    if playerTotal > 21:
        print("You Bust! The CPU wins this round.\n")
        cpuScore += 1
        playerTotal = 0
        cpuTotal = 0
        continue

    cpuCard1 = random.randint(1,10)
    cpuCard2 = random.randint(1,10)
    cpuRandomCard = 0
    cpuTotal = cpuCard1 + cpuCard2
    cpuShowing = cpuCard2

    while cpuChoice != "stay" and cpuTotal < 21:
        cpuChoice = random.randint(0,1)

        if cpuChoice == 0:
            cpuChoice = "hit"
        elif cpuChoice == 1:
            cpuChoice = "stay"

        if cpuChoice == "hit":
            cpuRandomCard = random.randint(1,10)
            cpuTotal = cpuTotal + cpuRandomCard
            cpuShowing = cpuShowing + cpuRandomCard
            print(f"The CPU got a {cpuRandomCard}.")
            print(f"The CPU is showing {cpuShowing}.\n")

        elif cpuChoice == "stay":
            print("The CPU chose to stay.")
             

    if cpuTotal > 21:
        print(f"The CPU bust with a total of {cpuTotal}")
        if playerTotal <= 21 and cpuTotal <= 21:
            print("\nBoth of you have stayed.")
            print(f"You had {playerTotal} and the CPU had {cpuTotal}.")

            if playerTotal > cpuTotal:
                playerScore += 1
                print("You won this round.")
            elif playerTotal < cpuTotal:
                cpuScore += 1
                print("You lost this round.")

    playerTotal = 0
    cpuTotal = 0


# For HIT -- Give the player another card and add it to their total.
# For STAY -- Pass the turn to the CPU.
# Allow CPU to HIT or STAY.
# Once both stay, output results and winner.