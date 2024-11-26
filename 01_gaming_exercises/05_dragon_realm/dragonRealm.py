# Dragon Realm, Elijah Reed, v0.7
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

evidence = 0
sanity = 100
items = 0
hasUSB = False
hasTea = False
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

def checkRoom(chosenRoom):
    evidence = 0
    sanity = 100

    print('\nYou approach the door...')
    time.sleep(waitTime)
    print('It is strangely familiar...')
    time.sleep(waitTime)
    print("There's a drawer under the desk...")
    time.sleep(waitTime)
    print("You open it and...")
    time.sleep(waitTime)

    safeRoom = random.randint(1, 2)

    if chosenRoom == str(safeRoom):
        print('You find some old items and a note.')
        time.sleep(waitTime)
        print('The note says "Only take two." Who wrote this?')
        time.sleep(waitTime)
        saveData.write("The player entered the safe room.\n")

    else:
        print('IT came out of the drawer and grabs you!')
        time.sleep(waitTime)
        print("You shake IT free but it cut your arm and left some dark substance.\n")
        time.sleep(waitTime)
        evidence += 1
        sanity -= 20
        print(f"You have {sanity} sanity left.\n")
        time.sleep(waitTime)
        print("IT disappeared and there's some items in the drawer.")
        time.sleep(waitTime)
        saveData.write("The player entered the dangerous room.\n")

def roomScenarioComputer(hasUSB: bool):
    print('In this room, there is a computer that might work.')
    time.sleep(waitTime)

    if hasUSB == True:
        print('You put the USB in the computer...')
        time.sleep(waitTime)
        print("Records of different employees show up, you've seen these names before")
        time.sleep(waitTime)
        print("There's an address listed under the name, you should probably go there.")
        time.sleep(waitTime)
        print('The computer crashed, oh well.\n')
        time.sleep(waitTime)
        knowsAddress = True
    elif hasUSB == False:
        print('You turned on the computer... nothing happened.')
        time.sleep(waitTime)
        print('The computer crashed, oh well.\n')
        time.sleep(waitTime)

    print("Upon leaving the room, you spot the stairs.")
    time.sleep(waitTime)
    print("Head on down, the exit has to be down there.")
    time.sleep(waitTime)
    print("You find the exit... where to now?")
    time.sleep(waitTime)
    print("Upon leaving the OFFICE, you notice something...")
    time.sleep(waitTime)
    print("The CITY is ruined, everything is abandoned, twisted and dark... what happened?\n")
    time.sleep(waitTime)
    return knowsAddress

def roomScenarioWarehouse(knowsAddress, hasPen, sanity, evidence):
    if knowsAddress == True:
        saveData.write("The player went to the warehouse.\n")
        print("You decide to go to that address you found on that old computer.")
        time.sleep(waitTime)
        print("It's a WAREHOUSE...")
        time.sleep(waitTime)
        print("Head inside, you never know what awaits.")
        time.sleep(waitTime)
        print("While you're looking around, IT jumps out at you.")
        time.sleep(waitTime)
        print("IT is the most grotesque thing you've ever seen.")
        time.sleep(waitTime)
        print("IT's aura is filled with bloodlust, I don't think it plans to keep you alive!")
        time.sleep(waitTime)
        print("IT charges you!")
        time.sleep(waitTime)
        print("IT jumped at you and used some strange power on you!\n")
        time.sleep(waitTime)
        print("-- You are seeing your past, your friends, your kids... where did they all go? --")
        time.sleep(waitTime)
        print("-- Will you be able to get out of this nightmare? How can you escape? --\n")
        time.sleep(waitTime)
        print("You snap back to reality, quickly get away before IT attacks you again!")
        time.sleep(waitTime)
        sanity -= 40
        print("You made it out of the WAREHOUSE, you should draw what it looks like in case you need evidence.")
        time.sleep(waitTime)
        if hasPen == True:
            print("You draw IT, this mediocre drawing may come in handy.")
            time.sleep(waitTime)
            evidence += 1
            saveData.write("The player drew the monster.\n")
        elif hasPen == False:
            print("You don't have a pen, nevermind.")
            time.sleep(waitTime)
            saveData.write("The player didn't draw the monster.\n")
        print("After everything that happened in there, you might as well look around the city.\n")
        time.sleep(waitTime)

    elif knowsAddress == False:
        print("Might as well look around the city.")
        time.sleep(waitTime)
        saveData.write("The player didn't go to the warehouse.\n")

def roomScenarioCity(sanity, evidence, hasTea):
    if hasTea == True:
        print("Before exploring, you should drink your tea.")
        sanity += 10
    elif hasTea == False:
        print("Only if you had something to drink...")

    trust = 0

    time.sleep(waitTime)
    print("While wandering around the city, you find a INFO STAND.")
    time.sleep(waitTime)
    print("The guy at the stand notices you.")
    time.sleep(waitTime)
    print("??? - Can I help you?")
    time.sleep(waitTime)
    print("You - How do I get out of here?!")
    time.sleep(waitTime)
    print("??? - What's wrong? You don't like it here? Hahaha!")
    time.sleep(waitTime)
    print("You - NO I DON'T LIKE IT HERE! I'M BEING CHASED DOWN BY SOME VOID FREAK!")
    time.sleep(waitTime)
    print("??? - Listen buddy, I've seen some weird people around here but I'm not gonna believe that.")
    time.sleep(waitTime)
    print("??? - I see some dark thing running around but I'm older than I look, my eyes are getting bad.")
    time.sleep(waitTime)
    print("You - Well IT's definetly real! How do I get out of here?")
    time.sleep(waitTime)
    print("??? - I would tell you if you weren't crazy.")
    time.sleep(waitTime)
    print("You - I'M NOT CRAZY.")
    time.sleep(waitTime)
    if sanity >= 50:
        print("??? - I mean... you seem normal but still..")
        trust += 5
    elif sanity < 50:
        print("??? - Look at you, you're all jittery and twitchy.")


    time.sleep(waitTime)
    print("??? - If this so-called \"void freak\" exists, then I need proof.")
    time.sleep(waitTime)

    if evidence == 1:
        trust += 1
        print("??? - Interesting...")
    elif evidence == 2:
        trust += 2
        print("??? - That's a nasty cut... what is that dark stuff?")
        time.sleep(waitTime)
        print("??? - That drawing... I have seen that running around.")
    


playAgain = 'yes'

while playAgain == 'yes' or playAgain == 'y':
    waitTime = int(input("Enter how long you want to wait for the text to print. 1 - 4 Seconds."))
    time.sleep(waitTime)

    displayIntro()
    roomNumber = chooseDoor()
    checkRoom(roomNumber)
    while items != 2:
        print('Take an item.')
        itemChoice = input('The [P]en and paper, the [U]SB, or the [T]ea on the desk.\n').upper()
        if itemChoice == "P":
            hasPen = True
            print("Write down your feelings with this glorious pen, I'm sure that will help you.")
        elif itemChoice == "U":
            hasUSB = True
            print("Guess you have to find a computer then.")
        elif itemChoice == "T":
            hasTea = True
            print("Tea is a wonderful drink, but how will it be useful?")
        items += 1

    print("You grabbed: ")
    if hasPen:
        print("- A pen.")
        saveData.write("The player chose the pen.\n")
    if hasUSB:
        print("- The USB.")
        saveData.write("The player chose the USB.\n")
    if hasTea:
        print("- Tea.")
        saveData.write("The player chose Tea.\n")

    print('You have your garbage, now proceed.\n')
    knowsAddress = roomScenarioComputer(hasUSB)
    roomScenarioWarehouse(knowsAddress, hasPen, sanity, evidence)
    roomScenarioCity(sanity, evidence, hasTea)
    print('Do you want to play again? (yes or no)\n')
    playAgain = input()

# CLOSE THE FILE
saveData.write("END OF GAME LOG\n\n")
saveData.close()

