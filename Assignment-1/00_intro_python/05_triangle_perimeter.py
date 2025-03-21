def main():
    side1: float = float(input("Enter the Length of Side 1: "))
    side2: float = float(input("Enter the Length of Side 2: "))
    side3: float = float(input("Enter the Length of Side 3: "))
    print("")
    perimeter: float = f"The perimeter of the triangle is {side1 + side2 + side3}"
    print(perimeter)


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
