"""
Problem Statement
Guess My Number

I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high

Enter a new number: 25 Your guess is too low

Enter a new number: 40 Your guess is too low

Enter a new number: 45 Your guess is too low

Enter a new number: 48 Congrats! The number was: 48

"""

import random

random_num = random.randint(1, 100)


def main():
    attempts = 0
    while True:
        user_guess = int(input("Guess a number between 1 and 100: "))
        attempts += 1

        if user_guess < random_num:
            print("Too low!")
            print()
        elif user_guess > random_num:
            print("Too high!")
        else:
            print(
                f"Congratulations! You guessed the number in {attempts} attempts.")
            break

# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()

