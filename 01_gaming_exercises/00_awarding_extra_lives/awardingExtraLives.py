# Awarding Extra Lives, Elijah Reed, v0.0

lives = 3

# Allow the user to input the score AS AN INTEGER
# If score is 10000 or less
    # Lose a Life
# If score is > 10000 but less than 100001
    # Give 1 Extra Life
# If score is > 100000
    # Give 2 Extra Lives

# Output the score and number of lives to the screen.

score = int(input("Please type your score and press ENTER\n"))


if score <= 10000:
    lives += -1 # Take away a Life
elif score < 100001:
    lives += 1 # Add one Life
elif score > 100000:
    lives += 2 # Add two Lives

print(f"\nWith a score of {score}, you now have {lives} lives.\n")

    