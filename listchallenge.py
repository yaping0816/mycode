#!/usr/bin/python3

heroes= ["Spiderman", "Batman", "Black Panther", "Wonder Woman", "Storm"]

# PART 1
# Print out your favorite character from this list! The output would look something like:
# My favorite character is Black Panther!
print(f"My favorite character is {heroes[0]}!")

# PART 2
# Ask the user to pick a number between 1 and 100.
# Convert the input into an integer.
favnum = input("what's your favorite number?\n>")
print(int(favnum))

nums= [1, -5, 56, 987, 0]

# PART 3
# check out https://docs.python.org/3/library/functions.html or go to Google
# use a built-in function to find which integer in nums is the biggest.
# then, print out that number!
print(max(nums))
