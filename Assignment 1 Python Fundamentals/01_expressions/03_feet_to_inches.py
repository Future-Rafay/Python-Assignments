INCHES_IN_FOOT = 12


def convert_to_feet(feet: float):
    return print(f"{feet} feet = {feet * INCHES_IN_FOOT} inches")


def main():
    feet: float = float(input("Enter The Feet To Convert To Inches :"))
    print(convert_to_feet(feet))


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
