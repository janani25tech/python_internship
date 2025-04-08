import random

def number_guesser():
    print("Welcome to the Number Guesser!")
    try:
        lower = int(input("Enter the lower limit: "))
        upper = int(input("Enter the upper limit: "))
        number = random.randint(lower, upper)
        print(f"Guess the number between {lower} and {upper}")

        while True:
            guess = int(input("Your guess: "))
            if guess < number:
                print("Too low!")
            elif guess > number:
                print("Too high!")
            else:
                print("Well done! You guessed the number!")
                break
    except ValueError:
        print("Invalid input. Please enter numeric values.")

# Run the game
number_guesser()
