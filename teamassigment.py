# Aizhamal, Chris
# Oct 31, 2024
# a guessing program that will take a number from the user and guess a randomly generated number

# Imports the random module
import random

def guessing_game():

# Generate a random number between 1 and 10
    target_number = random.randint(1, 10)
    attempts = 0 # Number of attempts to guess
    print("Welcome to the guessing game. Are you ready!")
