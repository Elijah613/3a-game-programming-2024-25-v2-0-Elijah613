# Looooooops, Elijah Reed, v0.0
import random # import the random module for us to use.

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
# for i in range(10): # range is 0 - 9
#     print(i)
# # Might not always want to start at 0.
# for i in range(10, 100):
#     print(i)

# Not want to count by 1 -- RARE
# for i in range(10, 100, 5): # 10 = start, 100 - 1 = stop, 5 = # to count by
#     print(i)

# # Sometimes you're not done writing the loops.
# for i in range(10):
#     pass # tells Python this loop isn't finished, don't freak out.

# while loops -- Musical chairs
playerScore = 0
counter = 0
while playerScore < 100: # Run as long as this is True
    print(f"Starting: {playerScore}")
    playerScore += random.randint(1, 10)
    print(f"After: {playerScore}")
    counter += 1
print(f"Counter: {counter}")
    

