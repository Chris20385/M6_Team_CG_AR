# Aizhamal, Chris
# Oct 31, 2024
# a guessing program that will take a number from the user and guess a randomly generated number

# Imports the random module
import random

def guessing_game():

# Generate a random number between 1 and 10
target_number = random.randint(1, 10)
guess = None
attempts = 3  # Set the number of allowed attempts

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 10.")
print("You have 3 attempts to guess the correct number.")

