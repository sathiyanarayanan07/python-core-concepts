import random

def guess_game():
    number_to_guess = random.randint(1,20)
    attempts = 5

    print("I'm thinking  of a number between 1 and 20.")

    for i in range(attempts):
        guess = int(input(f"Attempt {i+1}: Enter your guess:"))

        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")

        else:
            print(F"correct! you found it in {i+1} tries.")
            return
        
    print(f"Game over! The number was{number_to_guess}")

guess_game()