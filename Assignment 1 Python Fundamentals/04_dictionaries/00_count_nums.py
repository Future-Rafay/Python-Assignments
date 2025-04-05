def user_input() -> list:
    numbers: list = []
    while True:

        user_input = input("Enter a number: ")

        if user_input == "":
            count_numbers(numbers)
            break

        try:
            numbers.append(int(user_input))
        except ValueError:
            print("Please enter a valid number.")
            continue


def count_numbers(numbers: list) -> dict:
    count_dict = {}
    for number in numbers:
        if number in count_dict:
            count_dict[number] += 1
        else:
            count_dict[number] = 1
    print_occurrences(count_dict)


def print_occurrences(count_dict: dict):
    for number, count in count_dict.items():
        print(f"{number} appears {count} times.")


def main():
    user_input()


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':

    main()
