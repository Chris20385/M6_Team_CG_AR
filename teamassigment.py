# Aizhamal, Cristian
# Oct 31, 2024
# a guessing program that will take a number from the user and guess a randomly generated number

# Imports the random module
import random

def guessing_game():
guess_number = random.randint(1, 10) # Generate a random number between 1 and 10
attempts = 0  # Number of attempts it took to guess the number

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 10.")
while True: #Starts loop to allow multiple guesses
    try:
        user_guess = int(input("Enter your guess: ")) # Promts user for there guess
        attempts +=1 #Increase the attempt counter
        if user_guess == guess_number: # Checks if guess is correct
                print (f"Hurray! You guessed the number {guess_number} in {attempts} attempts.")
                break # Exits loop only if the guess is correct
        else:
            if user_guess < guess_number: # Checks if the guess is lower than the target number
                print("Go higher, try again")
            else:
                    print("Lower try again")
        except ValueError:
            print("Enter a valid number")

