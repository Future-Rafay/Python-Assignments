def main():
    seconds: int = int(
        input("Enter The Amount of Seconds to Convert into Year :"))

    year = seconds / 31536025.919999998
    print(f"{seconds} sec = {year:.2f} years")

    DAYS_PER_YEAR: int = 365
    HOURS_PER_DAY: int = 24
    MIN_PER_HOUR: int = 60
    SEC_PER_MIN: int = 60

    # We can get the number of seconds per year by multiplying the handy constants above!
    print("There are " + str(DAYS_PER_YEAR * HOURS_PER_DAY *
          MIN_PER_HOUR * SEC_PER_MIN) + " seconds in a year!")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
