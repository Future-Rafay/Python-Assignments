def chaotic_counting():
    for i in range(1, 11):
        if done():
            return
        else:
            print(i, end=' ')


def done():
    import random
    DONE_LIKELIHOOD = 0.1  # 10% chance to finish
    return random.random() < DONE_LIKELIHOOD 


def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("\nI stopped counting because I felt like it.")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
