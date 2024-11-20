# Dragon Realm, Elijah Reed, v0.5
# Awesome job so far!  If you have any finishing touches please add them. 

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
evidence = 0
items = 0
hasUSB = False
hasCoffee = False
hasPen = False
knowsAddress = False

def displayIntro():

    print("""
    
You find yourself in a twisted office building, there is two identical rooms in front of you
that lead to unknown horrors. Your memory is fuzzy and you can't remember the way out. 
Guess you have to rely on instinct.
    
    """)

def chooseDoor():
    doors = ''
    while doors != '1' and doors != '2':
        print('Which room will you go into? (1 or 2)')
        doors = input("\n")
    return doors

def checkRoom(chosenRoom, sanity, evidence):
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
        saveData.write("The player entered the safe room.")

    else:
        print('IT came out of the drawer and grabs you!')
        time.sleep(1)
        print("You shake IT free but it cut your arm and left some dark substance.\n")
        evidence += 1
        sanity -= 20
        print(f"You have {sanity} sanity left.\n")
        print("IT disappeared and there's some items in the drawer.")
        saveData.write("The player entered the dangerous room.")

def roomScenarioComputer(hasUSB: bool, knowsAddress: bool):
    print('In this room, there is a computer that might work.')
    time.sleep(1)

    if hasUSB == True:
        print('You put the USB in the computer...')
        time.sleep(1)
        print("Records of different employees show up, you've seen these names before")
        time.sleep(1)
        print("There's an address listed under the name, you should probably go there.")
        time.sleep(1)
        print('The computer crashed, oh well.\n')
        time.sleep(1)
        knowsAddress = True
    elif hasUSB == False:
        print('You turned on the computer... nothing happened.')
        print('The computer crashed, oh well.\n')

    print("Upon leaving the room, you spot the stairs")
    time.sleep(1)
    print("Head on down, the exit has to be down there.")
    time.sleep(1)
    print("You find the exit... where to now?")
    time.sleep(1)
    print("Upon leaving the OFFICE, you notice something...")
    time.sleep(1)
    print("The CITY is ruined, everything is abandoned, twisted and dark... what happened?")
    return knowsAddress

def roomScenarioWarehouse(knowsAddress: bool, hasPen: bool, sanity: int, evidence: int):
    if knowsAddress == True:
        saveData.write("The player went to the warehouse.")
        print("You decide to go to that address you found on that old computer.")
        time.sleep(1)
        print("It's a WAREHOUSE...")
        time.sleep(1)
        print("Head inside, you never know what awaits.")
        time.sleep(1)
        print("While you're looking around, IT jumps out at you.")
        time.sleep(1)
        print("IT is the most grotesque thing you've ever seen.")
        time.sleep(1)
        print("IT's aura is filled with bloodlust, I don't think it plans to keep you alive!")
        time.sleep(1)
        print("IT charges you!")
        time.sleep(1)
        print("IT jumped at you and used some strange power on you!")
        time.sleep(1)
        print("-- You are seeing your past, your friends, your kids... where did they all go? --")
        time.sleep(1)
        print("-- Will you be able to get out of this nightmare? How can you escape? --")
        time.sleep(1)
        print("You snap back to reality, quickly get away before IT attacks you again!")
        time.sleep(1)
        sanity -= 40
        print("You made it out of the WAREHOUSE, you should draw what it looks like in case you need evidence.")
        if hasPen == True:
            print("You draw IT, this mediocre drawing may come in handy.")
            evidence += 1
            saveData.write("The player drew the monster.")
        elif hasPen == False:
            print("You don't have a pen, nevermind.")
            saveData.write("The player didn't draw the monster.")
        time.sleep(1)
        print("After everything that happened in there, you might as well look around the city.")

    elif knowsAddress == False:
        print("Might as well look around the city.")
        saveData.write("The player didn't go to the warehouse.")

playAgain = 'yes'

while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    roomNumber = chooseDoor()
    checkRoom(roomNumber, sanity, evidence)
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
        saveData.write("The player chose the pen.\n")
    if hasUSB:
        print("- The USB.")
        saveData.write("The player chose the USB.\n")
    if hasCoffee:
        print("- Coffee.")
        saveData.write("The player chose coffee.\n")

    print('You have your garbage, now proceed.\n')
    roomScenarioComputer(hasUSB, sanity, knowsAddress)
    roomScenarioWarehouse(knowsAddress, hasPen, sanity, evidence)
    print('Do you want to play again? (yes or no)\n')
    playAgain = input()

# CLOSE THE FILE
saveData.write("END OF GAME LOG\n\n")
saveData.close()

