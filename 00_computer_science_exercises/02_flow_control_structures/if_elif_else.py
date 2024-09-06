# Flow Control Strutures, Elijah Reed, v0.0
# Making Computer Programs Make Decisions

temperature = 199.35
color = "Purple"
height = 7
likesPineappleOnPizza = True
studied = False

# SINGLE DECISION POINT - if statement
# if CONDITIONAL_EXPRESSION: <-- This will use a COMPARION OPERATOR 99% of the time.
    # runThisCode IF the CONDITIONAL_EXPRESSION is True

if temperature > 100:
    print("It is hot as the sun outside.\n")

if height >= 7:
    print("Wow, isn't he tall?\n")

# CHEAT CODE FOR IF STATEMENTS THAT USE BOOLEANS
if likesPineappleOnPizza:
    print("Booooo!\n")

# What if we want something different to happen?
if color == "Purple": # COMMON ERROR FOR STUDENTS IS USING = instead of ==.
    print("Purple is my favorite color too.\n")
else:
    print("That color sucks!\n")

if studied == True:
    print("That test was easy.")
else:
    print("I think I bombed that test.")



