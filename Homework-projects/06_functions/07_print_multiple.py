def print_multiple(message, repeats):
    for _ in range(1, repeats + 1):
        print(message, end=' ')
    return None


def main():
    message = input("Enter a message: ")
    repeats = int(input("How many times to print? "))
    print(f"Printing '{message}' {repeats} times:")
    print_multiple(message, repeats)


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
