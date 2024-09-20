# Rock, Paper, Scissors by Elijah Reed, v0.5

# MODULE IMPORTS
import random

# DATA STRUCTURES -- PLAYER
playerName = "Test Player"
playerChoice = None
playerScore =  0

# DATA STRUCTURES -- CPU
cpuScore = 0
cpuChoice = None

# PLAYER NAME INPUT
playerName = input("Please enter your name and press the ENTER key.\n")
print(f"Your name is {playerName}")
isCorrect = input("Is that correct? Type yes or no then press the ENTER key.\n").lower()

# .lower() can turn ALL input into lowercase
# .upper() can turn ALL input into uppercase

if isCorrect == "yes":
    print(f"Now {playerName}, let's play Rock, Paper, Scissors!\n")
else:
    playerName = input("Type your name correctly this time.\n")

# THE RULES using MUTLI-LINE STRINGS
print(f"""
Welcome {playerName} to the Rock, Paper, Scissors Robot!
We're going to play Rock, Paper, Scissors!

Here's how it works: Your opponent is the CPU. First to 5 wins gets the victory.
You will choose from Rock, Paper, or Scissors.
The CPU will also choose at random.
      
- ROCK BEATS SCISSORS
- SCISSORS BEATS PAPER
- PAPER BEATS ROCK

""")

# MULTI-LINE STRINGS CAN BE USED AS BIG COMMENTS
"""
According to my calculations,
Everything in between these quotes will be ignored.
I'm such a genius
"""

while playerScore < 5 and cpuScore < 5:
    print(f"{playerName}, you have {playerScore} wins.\nThe CPU has {cpuScore} wins.")
    playerChoice = input("Time to Choose. Rock, Paper, or Scissors?\n").lower()
    if playerChoice != "rock" and playerChoice != "paper" and playerChoice != "scissors":
        playerChoice = input("Try again. Rock, Paper, or Scissors?\n").lower()
        if playerChoice != "rock" and playerChoice != "paper" and playerChoice != "scissors":
            print("Ladies and Gentlemen, let's give a warm round of applause for the person who thinks they are above the rules.")
            exit()
        print(f"You have picked {playerChoice}.")
    else:
         print(f"You have picked {playerChoice}.")

    # let CPU select choice at random
    cpuChoice = random.randint(0, 2) # randomly selects 0, 1, or 2.
    if cpuChoice == 0:
        cpuChoice = "rock"
    elif cpuChoice == 1:
        cpuChoice = "paper"
    elif cpuChoice == 2:
        cpuChoice = "scissors"
    else:
        print("CPU decided to go on break. Restart and try Again")
        exit()
    print(f"The CPU picked {cpuChoice}.\n")

    # compare player choice to CPU choice
    # print the results to the screen
    # award point to winner and output results
