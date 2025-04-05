def main():

    num1: int = int(input("Enter 1st No."))
    num2: int = int(input("Enter 2nd No."))

    def sum_of_2(num1: int, num2: int):
        return num1 + num2
    result = sum_of_2(num1, num2)
    print(f"The sum of two given no. is : {result}")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
