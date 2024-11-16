# Functions Practice by Elijah Reed, v0.0

import random


def helloWorldMulti(): # FUNCTION STRUCTURE
    """This function will output Hello, World! in a language the user choose.""" # DOCSTRING
    # print a list of languages to the screen, at least three but no more than five.
    print("""
    Welcome to the Hello World Translator
    The available language choices are:
    [E]nglish
    [S]panish
    [J]apanese
    """)

# allow the user to select (input) a choice for the language
language = input("What language do you want?\n Please type the first letter of the language you want.\n").upper()
if language == "S":
    print("Hola, Mundo!")
elif language == "E":
    print("Hello, World!")
else:
    print("Konichiwa, Sekai!")

#helloWorldMulti()

# function to 