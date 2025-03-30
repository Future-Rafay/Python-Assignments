def main():
    # Prompt the user to enter a temperature in Fahrenheit
    user_input: float = float(input("Enter temperature in Fahrenheit: "))

    # Convert Fahrenheit to Celsius
    def convert_to_celsius(degrees_fahrenheit: float) -> float:
        return (degrees_fahrenheit - 32) * 5.0 / 9.0  # Ensure floating-point division

    # Get the result
    result: float = convert_to_celsius(user_input)

    # Print the output
    print(f"Temperature: {user_input}F = {result:.2f}C")

if __name__ == "__main__":
    main()
