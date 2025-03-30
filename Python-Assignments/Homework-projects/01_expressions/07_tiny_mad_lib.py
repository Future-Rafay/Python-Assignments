def main():
    # Asking user for inputs
    adjective = input("Please type an adjective and press enter: ")
    noun = input("Please type a noun and press enter: ")
    verb = input("Please type a verb and press enter: ")

    # Printing the fun sentence
    print("\nCode in Place is fun. I learned to program and used Python to make my", 
          f"{adjective} {noun} {verb}!")

# Calling the main function
if __name__ == "__main__":
    main()
