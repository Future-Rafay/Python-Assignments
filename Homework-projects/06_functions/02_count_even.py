def get_list_from_user():
    lst = []
    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        if user_input == "":
            break
        try:
            number = int(user_input)
            lst.append(number)
        except ValueError:
            print("Please enter a valid integer.")
    return lst


def count_even_numbers(lst):
    count: int = 0
    for number in lst:
        if number % 2 == 0:
            count += 1
    return count


def main():
    numbers = get_list_from_user()
    even_count = count_even_numbers(numbers)
    print(f"The number of even integers is: {even_count}")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
