# Dragon Realm, Elijah Reed, v0.2

import random
import time
import datetime

# SAVING DATA TO A FILE
# STEP 1 -- Create the file name to use.
# logFileName = "dragonRealmLog" + str(time.time()) + ".txt"
logFileName = "dragonRealmLog.txt"
# Examplle: dragonRealmLog1132AM.txt

# STEP 2 -- Create / OPen the file to save the data.
saveData = open(logFileName, "a")
# FILE MODES
# "x" CREATES FILE, IF FILE EXISTS, EXIT WITH ERROR MESSAGE.
# "w" CREATES FILE, IF FILE EXISTS, ERASE AND OVERWRITE FILE CONTENTS.
# "a" CREATES FILE, IF FILE EXISTS, APPEND DATA TO THE FILE.

saveData.write("GAME STARTED" + " " + str(datetime.datetime.now()) + "\n")

sanity = 100
items = 0
hasUSB = False
hasCoffee = False
hasPen = False
knowsAddress = False
hasKnife = False

def displayIntro():

    print("""
    
You find yourself in a twisted office building, there is two rooms in front of you
that lead to unknown horrors. Your memory is fuzzy and you can't remember the way 
out. Guess you have to rely on instinct.
    
    """)

def chooseDoor():
    doors = ''
    while doors != '1' and doors != '2':
        print('Which room will you go into? (1 or 2)')
        doors = input("\n")
    return doors

def checkRoom(chosenRoom, sanity):
    print('You approach the door...')
    time.sleep(1)
    print('It is strangely familiar...')
    time.sleep(1)
    print("There's a drawer under the desk...")
    time.sleep(1)
    print("You open it and...")
    time.sleep(1)

    safeRoom = random.randint(1, 2)

    if chosenRoom == str(safeRoom):
        print('You find some old items and a note.')
        time.sleep(1)
        print('The note says "Only take two." Who wrote this?')

    else:
        print('IT came out of the drawer and grabs you!')
        time.sleep(1)
        print("That room was corrupted. You're losing sanity.\n")
        sanity -= 20
        print(f"You have {sanity} sanity left.")

def roomScenarioComputer(hasUSB: bool, sanity):
    print('In this room, there is a computer that might work.')
    time.sleep(1)

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
        knowsAddress = True
        return hasKnife and knowsAddress
    elif hasUSB == False:
        print('You turned on the computer... nothing happened.')
        print('The computer crashed, oh well.\n')

    print("Upon leaving the room, you spot the stairs")
    print("Head on down, I'm sure nothing bad will happen.")
    stairTrip = random.randint(1,2)
    if stairTrip == 1:
        print("You made down the stairs, nice job :)")
    elif stairTrip == 2:
        print("You fell through the stairs, how???")
        sanity -= 20
        print(f"You have {sanity} sanity left, be careful.")
    print("You found the exit... where to now?")
    print("Upon leaving the OFFICE, you notice something...")
    print("The CITY is ruined, everything is abandoned, twisted and dark... what happened?")

def roomScenarioWarehouse(knowsAddress: bool, hasKnife: bool, hasPen: bool):
    if knowsAddress == True:
        print("You decide to go to that address you found on that old computer.")
        print("It's a WAREHOUSE...")
        print("Head inside, you never know what awaits.")
        print("While you're looking around, IT jumps out at you.")
        print("IT is the most grotesque thing you've ever seen.")

    elif knowsAddress == False:
        print("Might as well look around the city.")

playAgain = 'yes'

while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    roomNumber = chooseDoor()
    checkRoom(roomNumber, sanity)
    while items != 2:
        print('Take an item.')
        itemChoice = input('The [P]en and paper, the [U]SB, or the [C]offee on the desk.\n').upper()
        if itemChoice == "P":
            hasPen = True
            print("Write down your feelings with this glorious pen, I'm sure that will help you.")
        elif itemChoice == "U":
            hasUSB = True
            print("Guess you have to find a computer then.")
        elif itemChoice == "C":
            hasCoffee = True
            print("What is coffee going to do? Make you jittery?")
        items += 1

    print("You grabbed: ")
    if hasPen:
        print("- A pen.")
        saveData.write("The player chose the pen.")
    if hasUSB:
        print("- The USB.")
        saveData.write("The player chose the USB.")
    if hasCoffee:
        print("- Coffee.")
        saveData.write("The player chose coffee.")

    print('You have your garbage, now proceed.\n')
    roomScenarioComputer(hasUSB)
    print('Do you want to play again? (yes or no)\n')
    playAgain = input()

# CLOSE THE FILE
saveData.write("END OF GAME LOG\n\n")
saveData.close()

