# Dragon Realm, Elijah Reed, v0.9
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

saveData.write("\nGAME STARTED" + " " + str(datetime.datetime.now()) + "\n")


sanity = 100
items = 0
hasUSB = False
hasTea = False
hasLetterOpener = False
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
        print("You shake IT free but it cut your arm.\n")
        time.sleep(waitTime)
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

def roomScenarioWarehouse(knowsAddress, hasLetterOpener, sanity):
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
        print("You made it out of the WAREHOUSE.")
        time.sleep(waitTime)
        print("After everything that happened in there, you might as well look around the city.\n")
        time.sleep(waitTime)

    elif knowsAddress == False:
        print("Might as well look around the city.")
        time.sleep(waitTime)
        saveData.write("The player didn't go to the warehouse.\n")

def roomScenarioCity(sanity, hasTea):
    if hasTea == True:
        print("Before exploring, you should drink your tea.")
        sanity += 10
    elif hasTea == False:
        print("Only if you had something to drink...")

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

def checkEnding(sanity):
    if sanity == 40:
        print("??? - Have you seen yourself?! You look insane!")
        time.sleep(waitTime)
        print("??? - Get out of my sight.")
        time.sleep(waitTime)
        print("He won't let you leave, however you aren't satisfied with that.")
        time.sleep(waitTime)
        print("You - LET ME OUT OF THIS PRISON!")
        time.sleep(waitTime)
        print("IT heard your screams.")
        time.sleep(waitTime)
        print("??? - Stop your complaining, it's not that ba-")
        time.sleep(waitTime)
        print("IT killed him, and IT wants you next!")
        print("- The Worst Ending -")

    elif sanity == 50:
        print("??? - I can see it in your eyes, you can't be ok in the head.")
        time.sleep(waitTime)
        print("??? - I'm sorry but I can't tell you how to leave.")
        time.sleep(waitTime)
        print("You must just survive in this dimension.")
        time.sleep(waitTime)
        print("You live out the rest of your days fending IT off.")
        print("- The Survival Ending -")

    elif sanity == 60:
        print("??? - I can tell you've been through alot, so I'll tell you.")
        time.sleep(waitTime)
        print("??? - Follow these instructions to the letter.")
        time.sleep(waitTime)
        print("The mysterious man tells you how to escape...")
        time.sleep(waitTime)
        print("After finding the way out, you wake up!")
        time.sleep(waitTime)
        print("You're in a hospital laying in bed!")
        time.sleep(waitTime)
        print("You were in a coma this whole time?!")
        time.sleep(waitTime)
        print("You - THIS CAN'T BE!")
        time.sleep(waitTime)
        print("Relax, you're going insane!")
        time.sleep(waitTime)
        print("You - IT WAS REAL, IT WAS ALL REAL!")
        time.sleep(waitTime)
        print("Doctor - Sir, calm down, anything you saw wasn't real!")
        time.sleep(waitTime)
        print("You - AAAAAHHHHHHH")
        time.sleep(waitTime)
        print("You went insane.")
        print("- The Insane Ending -")

    elif sanity == 70:
        print("You seem trustworthy... fine, I'll tell you.")
        time.sleep(waitTime)
        print("After you follow his instructions, you find a strange door.")
        time.sleep(waitTime)
        print("Upon entering, you wake up!")
        time.sleep(waitTime)
        print("It was all a big nightmare, you were in a coma.")
        time.sleep(waitTime)
        print("You wake up in a hospital, the doctors are suprised to see your conscienceness.")
        time.sleep(waitTime)
        print("You have a stabbing headache and your brain feels like it's on fire.")
        time.sleep(waitTime)
        print("The doctors take you to Intensive Care.")
        time.sleep(waitTime)
        print("You live out the rest of your days in and out the hospital due to your head, it could be worse.")
        print("- The Mentally Ill ending -")

    elif sanity == 80:
        print("After you follow his instructions, you find a strange door.")
        time.sleep(waitTime)
        print("Upon entering, you wake up!")
        time.sleep(waitTime)
        print("It was all a big nightmare, you were in a coma.")
        time.sleep(waitTime)
        print("You wake up in a hospital, the doctors are suprised to see your conscienceness.")
        time.sleep(waitTime)
        print("As the doctors tried to explain what happened, everything you saw is so... confusing.")
        time.sleep(waitTime)
        print("You can't even hear their voices, you just keep thinking about IT.")
        time.sleep(waitTime)
        print("IT was so strange, yet you feel a connection to it.")
        print("- The Confused Ending -")

    elif sanity >= 90:
        print("??? - Yea I can tell, you are determined to leave, without a trace of rage, sadness, or doubt.")
        time.sleep(waitTime)
        print("??? - Here's how you leave.")
        time.sleep(waitTime)
        print("Upon following the instructions, you find a strange door.")
        time.sleep(waitTime)
        print("When you enter, you wake up! You were in a coma.")
        time.sleep(waitTime)
        print("The doctors are suprised to see you wake up and you are so relieved you made it out.")
        time.sleep(waitTime)
        print("After brain analysis, you haven't changed.")
        time.sleep(waitTime)
        print("You tell the doctors everything you saw and experienced without sparing any details.")
        time.sleep(waitTime)
        print("They explain to you and your wife how after a severe car accident after leaving your OFFICE job,")
        print("you were sent in a coma for 3 years and your wife passed.")
        time.sleep(waitTime)
        print("It makes sense, the OFFICE is were you worked.")
        time.sleep(waitTime)
        print("The CITY is the last thing you saw before you crashed.")
        time.sleep(waitTime)
        print("Whatever was chasing you down didn't want you to leave.")
        time.sleep(waitTime)
        print("Everything makes sense now, that thing... IT was your wife.")
        print("- The Best Ending -")
    
playAgain = 'yes'

while playAgain == 'yes' or playAgain == 'y':
    waitTime = int(input("Enter how long you want to wait for the text to print. 1 - 4 Seconds."))
    time.sleep(waitTime)

    displayIntro()
    roomNumber = chooseDoor()
    checkRoom(roomNumber)
    while items != 2:
        print('Take an item.')
        itemChoice = input('The [L]etter Opener, the [U]SB, or the [T]ea on the desk.\n').upper()
        if itemChoice == "L":
            hasLetterOpener = True
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
        print("- A Letter Opener.")
        saveData.write("The player chose the Letter Opener.\n")
    if hasUSB:
        print("- The USB.")
        saveData.write("The player chose the USB.\n")
    if hasTea:
        print("- Tea.")
        saveData.write("The player chose Tea.\n")

    print('You have your garbage, now proceed.\n')
    knowsAddress = roomScenarioComputer(hasUSB)
    roomScenarioWarehouse(knowsAddress, hasPen, sanity)
    roomScenarioCity(sanity, hasTea)
    checkEnding(sanity)
    print('Do you want to play again? (yes or no)\n')
    playAgain = input()

# CLOSE THE FILE
saveData.write("END OF GAME LOG\n\n")
saveData.close()

