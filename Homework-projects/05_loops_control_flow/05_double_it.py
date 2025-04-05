def main():
    MAX_LIMIT: int = 1000

    current_value: int = int(input("Enter a number: "))
    while current_value < MAX_LIMIT:
        print(current_value, end=", ")
        current_value = current_value * 2


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
