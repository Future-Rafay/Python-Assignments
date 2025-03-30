def double_list(numbers):
    return [number * 2 for number in numbers]

def main():
    # Read input as a string
    input_numbers = input("Please type a list of numbers separated by commas and press enter: ")

    # Convert the list of strings to a list of integers
    numbers = [int(num.strip()) for num in input_numbers.split(",") if num.strip().isdigit()]

    # Check if numbers list is not empty
    if not numbers:
        print("Error: No valid numbers entered.")
        return

    doubled_list : list = double_list(numbers)
    print(f"The sum of the numbers is: {doubled_list}")


if __name__ == '__main__':
    main()