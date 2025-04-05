AFFIRMATION: str = "You are amazing!"


def main():
    print("Please type the following affirmation: " + AFFIRMATION)

    user_feedback = input("=>")
    while user_feedback != AFFIRMATION:
        print("That was not the affirmation.")
        print("Please type the following affirmation: " + AFFIRMATION)
        user_feedback = input()
    print("Great job! You are amazing!")



# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
