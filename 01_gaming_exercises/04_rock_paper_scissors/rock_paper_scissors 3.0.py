# Rock, Paper, Scissors by Elijah Reed, v0.14

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
def playerName() -> str: # Function Signature -- name of function, (arguements if any)
    """"Gets the name from the player and returns it."""
    # The line above is a DOCSTRING
    playerName = input("Please enter your name and press the ENTER key.\n")
    print(f"Your name is {playerName}")
    isCorrect = input("Is that correct? Type yes or no then press the ENTER key.\n").lower()
    if isCorrect == "yes":
        print(f"Now {playerName}, let's play Rock, Paper, Scissors!\n")
    else:
        playerName = input("Type your name correctly this time.\n")
    return playerName

# CALLING THE FUBCTION
playerName = playerName()

# THE RULES using MUTLI-LINE STRINGS
def rules() -> None:
    """This function prints the rules for RPS."""
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
    # Does another part of this program need to access this information?
    # IF YES, YOU MUST HAVE A RETURN STATEMENT
    # IF NO, A RETURN STATEMENT IS NOT REQUIRED

rules()

def playerChoice() -> str:
    """Allows the player to choose rock, paper, or scissors."""
    playerChoice = input("Time to Choose. Rock, Paper, or Scissors?\n").lower()
    if playerChoice != "rock" and playerChoice != "paper" and playerChoice != "scissors":
        playerChoice = input("Try again. Rock, Paper, or Scissors?\n").lower()
        if playerChoice != "rock" and playerChoice != "paper" and playerChoice != "scissors":
            print("Ladies and Gentlemen, let's give a warm round of applause for the person who thinks they are above the rules.")
            exit()
        print(f"You have thrown {playerChoice}.")
    else:
         print(f"You have thrown {playerChoice}.")
    return playerChoice

def cpuChoice() -> str:
    """Allows the CPU to randomly choose rock, paper, or scissors."""
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
    print(f"The CPU threw {cpuChoice}.\n")
    return cpuChoice

def pickWinner(playerChoice:str,cpuChoice:str) -> str: # playerChoice and cpuChoice are both ARGUMENTS, they will be string values.
    """This function uses the player and CPU choices to decide a winner."""
    if playerChoice == "rock" and cpuChoice == "paper":
        print(f"The CPU threw {cpuChoice} and you threw {playerChoice}.")
        print("You lost this round, you suck!")
        return "CPU Wins"
    elif playerChoice == "rock" and cpuChoice == "scissors":
        print(f"The CPU threw {cpuChoice} and you threw {playerChoice}.")
        print("You win this round, what a genius everybody.")
        return "Player Wins"
    elif playerChoice == "rock" and cpuChoice == "rock":
        print(f"The CPU threw {cpuChoice} and you threw {playerChoice}.")
        print("You tied with the CPU, run it back.")
        return "Draw"
    elif playerChoice == "paper" and cpuChoice == "rock":
        print(f"The CPU threw {cpuChoice} and you threw {playerChoice}.")
        print("You win this round, what a genius everybody..")
        return "Player Wins"
    elif playerChoice == "paper" and cpuChoice == "paper":
        print(f"The CPU threw {cpuChoice} and you threw {playerChoice}.")
        print("You tied with the CPU, run it back.")
        return "Draw"
    elif playerChoice == "paper" and cpuChoice == "scissors":
        print(f"The CPU threw {cpuChoice} and you threw {playerChoice}.")
        print("You lost this round, you suck!")
        return "CPU Wins"
    elif playerChoice == "scissors" and cpuChoice == "rock":
        print(f"The CPU threw {cpuChoice} and you threw {playerChoice}.")
        print("You lost this round, you suck!")
        return "CPU Wins"
    elif playerChoice == "scissors" and cpuChoice == "paper":
        print(f"The CPU threw {cpuChoice} and you threw {playerChoice}.")
        print("You win this round, what a genius everybody.")
        return "Player Wins"
    elif playerChoice == "scissors" and cpuChoice == "scissors":
        print(f"The CPU threw {cpuChoice} and you threw {playerChoice}.")
        print("You tied with the CPU, run it back.")
        return "Draw"
    else:
        print("The game broke :/\n Restart and Try Again.")
        exit()
        return "Game Bug"
    # return statements exit a function

def score(winner:str) -> int:
    """This function uses the winner to update the score for the CPU, Draws, and Player score."""
    if winner == "Player Wins":
        score = 1
    elif winner == "CPU Wins":
        score = 1
    elif winner == "Draw":
        score = 0
    return score

def matchWinner(playerScore: int, cpuScore: int) -> bool:

    """This function determines if a player has won the game or not by scoring 5 points"""
    if playerScore >= 5:
        print("You've won.... for now.\n")
        return True
    elif cpuScore >= 5:
        print("Just as I thought, you couldn't beat the CPU.\n")
        return True
    else: # No winner yet
        return False

def playGame(playerScore: int, cpuScore: int) -> None:
    """This function will use all the other functions to play RPS."""
    while True:
        cpuPick = cpuChoice()
        playerPick = playerChoice()
        roundWinner = pickWinner(playerPick, cpuPick)
        if roundWinner == "Player Wins":
            playerScore += score(roundWinner)
        if roundWinner == "CPU Wins":
            cpuScore += score(roundWinner)

        print(f"\nYou have a score of {playerScore}.")
        print(f"The CPU has a score of {cpuScore}.\n")

        if matchWinner(playerScore, cpuScore) == True:
            break

playGame(playerScore, cpuScore)