# Buckshot Roulette by Elijah Reed, v0.0

import random

# GAME DATA
shotgunRound = 0
ammoLeft = 8
lives = 0
blanks = 0

# PLAYER DATA
playerName = "TBD"
playerChoice = None
playerHealth = 4

# CPU DATA
dealerChoice = None
dealerHealth = 4

playerName = input("Dealer: Sign this release form with your name and press the ENTER key. This cannot be changed later.\n")
print(f"Dealer: You signed with {playerName}.\n")

print(f"Dealer: {playerName}, you'll learn the rules soon enough. No reason to waste my time.\n")

while playerHealth != 0 and dealerHealth != 0:
    ammoLeft = 8
    lives = random.randint(1,4)
    blanks = 8 - lives
    while ammoLeft != 0:
        print(f"{lives} live rounds, {blanks} blanks.")
        print(f"I load the rounds in the shotgun in a random order.")
        print("Now make your decision.")
        while playerChoice != "dealer" or shotgunRound == "live":
            playerChoice = input("Should you shoot yourself or the dealer?\nType YOURSELF or DEALER then press ENTER.\n").lower
            shotgunRound = random.randint(0,1)
            if shotgunRound == 0:
                shotgunRound = "blank"
            elif shotgunRound == 1:
                shotgunRound = "live"

            if playerChoice == "yourself" and shotgunRound == "blank":
                blanks -= 1
                print("*Click*\n")
                continue
            elif playerChoice == "yourself" and shotgunRound == "live":
                lives -= 1
                playerHealth -= 1
                print("*BANG*")
                print(f"{playerName} has {playerHealth} health remaining.")
                print(f"The Dealer has {dealerHealth} remaining.")
            elif playerChoice == "dealer" and shotgunRound == "blank":
                blanks -= 1
                print("*Click*\n")
                print("Dealer: My turn.")
            elif playerChoice == "dealer" and shotgunRound == "live":
                lives -= 1
                dealerHealth -= 1
                print("*BANG*")
                print(f"{playerName} has {playerHealth} health remaining.")
                print(f"The Dealer has {dealerHealth} remaining.\n")
                print("Dealer: My turn.")
            
