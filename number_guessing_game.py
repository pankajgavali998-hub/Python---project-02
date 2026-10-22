
import random

def number_guessing_game():
    secret_number = random.randint(1, 10)
    attempts = 0

    print("Welcome to Number Guessing Game!")
    print("Guess a number between 1 and 10.")

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 10:
                print("Please enter a number from 1 to 10.")
            elif guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print("Congratulations! You guessed correctly.")
                print("Number of attempts:", attempts)
                break

        except ValueError:
            print("Invalid input! Please enter a number.")

number_guessing_game()
