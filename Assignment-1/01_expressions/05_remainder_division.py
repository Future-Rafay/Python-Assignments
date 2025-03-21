def main():
    dividend: int = int(input("Enter The No. to be devided :"))
    divisor: int = int(input("Enter The No. to be divisor :"))

    qoutient = dividend // divisor
    remainder = dividend % divisor

    print(
        f"The result of this division is {qoutient} with a remainder of {remainder}"
    )


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
