# Buckshot Roulette by Elijah Reed, v0.0

import random

# GAME DATA
shotgunShell = None
ammoLeft = 0
lives = 0
blanks = 0

# PLAYER DATA
playerName = "TBD"
playerChoice = None
playerHealth = 0

# CPU DATA
dealerChoice = None
dealerHealth = 0

playerName = input("Dealer: Sign this release form with your name and press the ENTER key. This cannot be changed later.\n")
print(f"Dealer: You signed with {playerName}.\n")

print(f"Dealer: {playerName}, you'll learn the rules soon enough. No reason to waste my time.")

while playerHealth != 0 and dealerHealth != 0:
    pass