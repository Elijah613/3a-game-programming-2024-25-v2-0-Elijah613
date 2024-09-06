# Data Types and Operators, Elijah Reed, v0.4

# Fundamental Data Types
# String - str - Sequence of letters, numbers, spaces, or other characters.
# Strings in Python are inside or '' or " "

# Boolean - bool - True or False values.

# Float - float - any number value with a decimal, +/-, including 0.

# Integers - int - any whole number, +/-, including 0.

# Data types are stored in VARIABLES.
# A variable is basially a named container to put data in it.
# VARIABLE NAMES SHOULD TELL YOU WHAT DATA IS BEING STORED
# VARIABLES CANNOT START WITH A NUMBER
# camelCaseVariableNames
# snake_case_variable_names

# DECLARING VARIABLES AND ASSINGING VALUES

high_score = 100000 # int data types

car_speed = 10.50 # float data type, miles per hour

has_axe = True # boolean date type
is_purple = False # boolean date type

player_name = "Elijah Reed" # string data type
power_up = "Computer" # string data type

# ASSIGN NEW VALUES
player_name = "Sage" # string data type
car_speed = 4.20

# DATA CAN CHANGE, BE CAREFUL.
has_axe = 5.0

# Printing Data Types
newInt = 3
newFloat = 4.0
newString = "Roblox"
newBool = False

print(type(newInt))
print(type(newFloat))
print(type(newString))
print(type(newBool))

# printing variables to Console / Screen
print(player_name)
print(is_purple)
print(high_score)
print(car_speed)

# printing variables and expression to console / screen
print(high_score + 2000)
print(5 * 9)
print(high_score)


# PRINTING VARIABLES INSIDE OF STRINGS
print(f"Hello {player_name}. Your high score is {high_score}.\n") 

# ARTTHMETIC OPERATORS
my_int = 26
my_float = 3.41
my_num = 0

# addition
my_int = 9 + 10
my_float = 2.0 + 6.21

my_int = my_int + 5

my_num = my_int + my_float
# When you add an int and a float together, the answer becomes a float

# subtraction
my_num = my_int - my_float
my_int = my_float - 1.25

# Multiplication
my_num = my_int * my_float

# Division
my_num = my_int / my_float # first is numerator, second num is denominator

# MODULUS (MODULO) % -- Returns REMAINDER after dividing.
# MOST COMMON USE FOR MODULUS IS DETERMING EVEN / ODD NUMBERS.
num_students = 6
num_slices_pizza = 35

left_overs = num_slices_pizza % num_students
print(left_overs)

# EXPONENTS **
num_squared = 5 ** 2 # 5 is the base, 2 is the exponent.

# FLOOR-DIVISION // -- Divides, THROWS OUT ANY DECIMAL.
my_num = my_int // my_float

# Addition-Assignment Operator - Mostly used for counters.
my_num = 5
my_num = my_num + 1 # Old-School Method
my_num += 1 # New Hotness
my_num *= 1
my_num /= 1

# COMPARISON OPERATORS
# IS-EQUAL-TO == Are the two values equal to each other?
# Returns True or False based on evaluation
# x = 6
# print(x == 5)

# # NOT-EQUAL-TO != Are the two values NOT equal?
# print(x != 12)

# #GREATER THAN/ GREATER-THAN-OR-EQUAL TO
# print(5 > 3) #Greater Than
# print(12 >= 2)

# #LESS THAN/ LESS-THAN-OR-EQUAL TO
# print(5 < 3) # Less Than
# print(12 <= 2) # Less Than or Equal To



# LOGICAL OPERATORS
# and -- ALL CONDITIONS MUST BE TRUE FOR ENTIRE STATEMENT TO BE TRUE
age = 44
height = 70
eyeColor = "Brown"

# In order to ride the Teacups, you must be at least 18 years old and 50" tall.
print(age >= 18 and height >= 60)
print(age >= 18 and height >= 60 and eyeColor == "Blue")
# ALWAYS CHECK FOR THE LEAST-LIKELY TO BE TRUE CONDITION FIRST
print(defeatedboss == True and level > 5 and hasBlueKey == True)

# not -- RETURNS THE OPPOSITE VALUE OF THE STATEMENT
a = 5
print()


# IDENTITY OPERATORS
g = 1.0
h = 1.0
i = g
print(g is h)
print(i is h)
print(i is not 1.0)
print(i is not g)

# MEMBERSHIP OPERATORS
fruits = ["apple", "banana", "tomato"]
print("banana" in fruits)
print("potato" in fruits)


