def main():
    while True:
        user_input = input("Enter your height in inches (or press Enter to quit): ")

        # Stop the program if the user presses Enter without input
        if user_input == "":
            print("Goodbye! Exiting the program.")
            break

        # Validate input to ensure it's a number
        if not user_input.isdigit():
            print("Invalid input. Please enter a valid height in inches.")
            continue  # Restart the loop

        # Convert input to integer
        user_height = int(user_input)

        print("Your Height:", user_height)
        print("The minimum height to ride the roller coaster is 48 inches.")

        # Check if the user is tall enough
        if user_height >= 48:
            print("You are tall enough to ride!\n")
        else:
            print("You are not tall enough to ride.\n")

# This provided line is required at the end of Python file to call the main() function.
if __name__ == '__main__':
    main()
