# Rock, Paper, Scissors by Elijah Reed, v0.1

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

if isCorrect == "yes":
    print(f"Now {playerName}, let's play Rock, Paper, Scissors!\n")
else:
    playerName = input("Type your name correctly this time.\n")