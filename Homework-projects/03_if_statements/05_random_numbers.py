import random

IN_NUMBERS: int = 10
MIN_VALUE: int = 1
MAX_VALUE: int = 100


def main():

    for _ in range(IN_NUMBERS):
        value = random.randint(MIN_VALUE, MAX_VALUE)
        print(value ,end=' ')
    print()


    
# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
