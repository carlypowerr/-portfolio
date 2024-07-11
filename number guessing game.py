import random

def number_guessing_game():
    number = random.randint(1, 10)

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 10. Can you guess it?")

    while True:
        guess = int(input("Enter your guess: "))

        if guess < number:
            print("Too low, try again!")
        elif guess > number:
            print("Too high, try again!")
        else:
            print("Congratulations! You guessed the number!")
            break

    print(f"The number was {number}. Play again if you'd like!")

# Let's play the game!
number_guessing_game()