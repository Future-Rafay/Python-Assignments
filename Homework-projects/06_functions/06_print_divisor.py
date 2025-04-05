def print_divisor(n):
    """Prints all divisors of n."""
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=' ')
    return None


def main():
    num = int(input("Enter a number: "))
    print(f"The divisors of {num} are:")
    print_divisor(num)
    print()  # for a new line after printing divisors


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
