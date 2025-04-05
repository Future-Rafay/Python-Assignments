def add_many_numbers(numbers: list) -> int:
    total_so_far = 0
    for number in numbers:
        total_so_far += number
    return total_so_far


def main():
    # Read input as a string
    input_numbers = input("Please type a list of numbers separated by commas and press enter: ")

    # Convert the list of strings to a list of integers
    numbers = [int(num.strip()) for num in input_numbers.split(",") if num.strip().isdigit()]

    # Check if numbers list is not empty
    if not numbers:
        print("Error: No valid numbers entered.")
        return

    sum_of_numbers = add_many_numbers(numbers)
    print(f"The sum of the numbers is: {sum_of_numbers}")


if __name__ == "__main__":
    main()
