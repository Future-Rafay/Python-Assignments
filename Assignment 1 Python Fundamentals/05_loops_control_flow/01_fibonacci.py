def main():
    MAX_NUM: int = 1000

    current_term = 0
    next_term = 1

    while current_term <= MAX_NUM:
        print(current_term, end=", ")
        term_after_next_term = current_term + next_term
        current_term = next_term
        next_term = term_after_next_term


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
