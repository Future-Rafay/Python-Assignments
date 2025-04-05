def main():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    def average(a, b):
        return (a + b) / 2

    print(f"The average of {num1} and {num2} is: {average(num1, num2)}")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
