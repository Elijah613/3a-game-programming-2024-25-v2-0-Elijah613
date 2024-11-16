# Dragon Realm, Elijah Reed, v0.1

import random
import time

items = 0
hasUSB = False
hasCoffee = False
hasPen = False
hasKnife = False

def displayIntro():

    print("""
    
You find yourself in a twisted office building, there is two rooms in front of you
that lead to unknown horrors. Your memory is fuzzy and you can't remember the way 
out of the office. Guess you have to rely on instinct.
    
    """)

def chooseDoor():
    doors = ''
    while doors != '1' and doors != '2':
        print('Which room will you go into? (1 or 2)')
        doors = input("\n")
    return doors

def checkRoom(chosenRoom):
    print('You approach the door...')
    time.sleep(2)
    print('It is strangely familiar...')
    time.sleep(2)
    print("There's a drawer under the desk...")
    time.sleep(2)
    print("You open it and...")
    time.sleep(2)

    safeRoom = random.randint(1, 2)

    if chosenRoom == str(safeRoom):
        print('You find some old items and a note.')
        time.sleep(2)
        print('The note says "Only take two." Who wrote this?')

    else:
        print('IT came out of the drawer and grabs you!')
        time.sleep(2)
        print('That room was corrupted. You went insane.\n')
        exit()

def chooseItems(items: int):
    while items < 2:
        print('Take an item.')
        itemChoice = input('The [P]en and paper, the [U]SB, or the [C]offee on the desk.\n').upper()
        if itemChoice == "P":
            hasPen = True
            print("Write down your feelings with this glorious pen, I'm sure that will help you.")
            return hasPen
        elif itemChoice == "U":
            hasUSB = True
            print("Guess you have to find a computer then.")
            return hasUSB
        elif itemChoice == "C":
            hasCoffee = True
            print("What is coffee going to do? Make you jittery?")
            return hasCoffee
        items += 1
    print('You have your garbage, now proceed.\n')

def roomScenario(hasUSB: bool):
    print('In this room, there is a computer that might work.')
    time.sleep(2)

    if hasUSB == True:
        print('You put the USB in the computer...')
        time.sleep(2)
        print("Records of different employees show up, you've seen these names before")
        print("There's an address listed under the name, you should probably go there.")
        time.sleep(2)
        print("The USB twisted into a knife... weird.")
        print('The computer crashed, oh well.\n')
        time.sleep(2)
        hasKnife = True
        return hasKnife
    elif hasUSB == False:
        print('You turned on the computer... nothing happened.')
        print('The computer crashed, oh well.\n')

playAgain = 'yes'

while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    roomNumber = chooseDoor()
    checkRoom(roomNumber)
    chooseItems(items)
    roomScenario(hasUSB)
    print('Do you want to play again? (yes or no)\n')
    playAgain = input()