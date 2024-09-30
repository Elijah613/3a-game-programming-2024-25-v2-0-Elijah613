# Rock, Paper, Scissors by Elijah Reed, v0.7

# MODULE IMPORTS
import random, time

# DATA STRUCTURES -- PLAYER
playerChoice = None
playerScore =  0
numDraws = 0

# DATA STRUCTURES -- CPU
cpuScore = 0
cpuChoice = None

# MAIN GAME LOOP
loopCount = 0
loopsReq = int(input("How many loops do you want?\nEnter an integer, no commas, and press the ENTER key.\n"))
rpsTimeStart = time.time() # returns the number of seconds since Jan. 01, 1970 @ 12:00AM

while loopCount < loopsReq:

    playerChoice = random.randint(0, 2)
    if playerChoice == 0:
        playerChoice = "rock"
    elif playerChoice == 1:
        playerChoice = "paper"
    elif playerChoice == 2:
        playerChoice = "scissors"
    else:
        print("CPU decided to go on break. Restart and try Again")
        exit()

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
    # print(f"The CPU threw {cpuChoice}.\n")

    # compare player choice to CPU choice
    if playerChoice == "rock" and cpuChoice == "paper":
        print(f"The CPU threw {cpuChoice} and you threw {playerChoice}.")
        print("You lost this round, you suck!")
        cpuScore += 1
        # CPU Wins
    elif playerChoice == "rock" and cpuChoice == "scissors":
        print(f"The CPU threw {cpuChoice} and you threw {playerChoice}.")
        print("You win this round, what a genius everybody.")
        playerScore += 1
        # Player Wins
    
    elif playerChoice == "paper" and cpuChoice == "rock":
        print(f"The CPU threw {cpuChoice} and you threw {playerChoice}.")
        print("You win this round, what a genius everybody..")
        playerScore += 1
        # Player Wins
    elif playerChoice == "paper" and cpuChoice == "paper":
        print(f"The CPU threw {cpuChoice} and you threw {playerChoice}.")
        print("You tied with the CPU, run it back.")
        numDraws += 1
        # Draw
    elif playerChoice == "paper" and cpuChoice == "scissors":
        print(f"The CPU threw {cpuChoice} and you threw {playerChoice}.")
        print("You lost this round, you suck!")
        cpuScore += 1
        # CPU Wins
    elif playerChoice == "scissors" and cpuChoice == "rock":
        print(f"The CPU threw {cpuChoice} and you threw {playerChoice}.")
        print("You lost this round, you suck!")
        cpuScore += 1
        # CPU Wins
    elif playerChoice == "scissors" and cpuChoice == "paper":
        print(f"The CPU threw {cpuChoice} and you threw {playerChoice}.")
        print("You win this round, what a genius everybody.")
        playerScore += 1
        # Player Wins
    elif playerChoice == "scissors" and cpuChoice == "scissors":
        print(f"The CPU threw {cpuChoice} and you threw {playerChoice}.")
        print("You tied with the CPU, run it back.")
        numDraws += 1
        # Draw
    else:
        print("The game broke :/\n Restart and Try Again.")
        exit()
    loopCount += 1

print(f"\nYour final score is {playerScore} and the CPU's final score is {cpuScore} and there was {numDraws} draws.")
if playerScore > cpuScore:
    print(f"You actually won, I can't believe it.\n")
elif cpuScore > playerScore:
    print("HAHA LOSER, YOU SUCK, YOU LOST!\n")
else:
    print("The game broke :/\n Restart and Try Again.")
    exit()


rpsTimeStop = time.time()
rpsTime = rpsTimeStop - rpsTimeStart
print(f"# of Loops: {loopCount}")
print(f"Execution Time {rpsTime:.2F} seconds.\n") # :.2F cuts the value down to 2 decimal places.