# Looooooops, Elijah Reed, v0.0

# TWO TYPES OF LOOPS
# for <-- Used when you know how many loops you'll need.
# while <-- Used when you do not know how many loops you'll need. 

# for loop is like Go Fish, you search each card for what the player asked.
# while loop is like musical chairs, you move around until the music stops.

# EACH TRIP THROUGH THE ENTIRE LOOP IS CALLED AN iteration
# "iterate through the list" means use a for loop

# for loops Example -- Iterating a List
# fruits = ["apple", "banana", "strawberry", "tomato"]
# for eachFruit in fruits:
#     print(eachFruit)

# continue keyword -- Skips the current iteration and then finishes the loop.  
# fruits = ["apple", "banana", "strawberry", "tomato"]
# for eachFruit in fruits:
#     if eachFruit == "banana":
#         continue
#     print(eachFruit)

# break keyword -- Immediately exit the loop.  
# fruits = ["apple", "banana", "strawberry", "tomato"]
# for eachFruit in fruits:
#     if eachFruit == "banana":
#         break
#     print(eachFruit)

# for loops using range(). range(x) is EXCLUSIVE, it starts at 0 and ends at x - 1
for i in range(10): # range is 0 - 9
    print(i)


