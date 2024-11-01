# Aizhamal, Chris
# Oct 31, 2024
# a guessing program that will take a number from the user and guess a randomly generated number

# Imports the random module
import random

def guessing_game():

# Generate a random number between 1 and 10
target_number = random.randint(1, 10)
guess = None
attempts = 0  # Number of attempts it took to guess the number

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 10.")
while True: #Starts loop to allow multiple guesses
    try:
        user_guess = int(input("Enter your guess: ")) # Promts user for there guess
        attempts +=1 #Increase the attempt counter
        if user_guess == guess_number:
                print (f"Hurray! you guessed the number {guess_number} in {attempts} attempts.")
                break

