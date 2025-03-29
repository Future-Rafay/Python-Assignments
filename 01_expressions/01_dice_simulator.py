import random

# DICE SIMULATOR

DICE_SIDES = 6

# Function to roll the dice

def roll_dice() -> int:
    # Generate a random number between 1 and 6
    dice1: int = random.randint(1, DICE_SIDES)
    # Generate a random number between 1 and 6
    dice2: int = random.randint(1, DICE_SIDES)
    total: int = dice1 + dice2
    print(f"Total of this Roll : {total}")


def main():
    roll_dice()
    roll_dice()
    roll_dice()


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
