def main():
    lst = []
    elem = input(
        "Enter a elem to add in list or press enter to stop: ")
    while elem != "":
        lst.append(elem)
        elem = input(
            "Enter a elem to add in list or press enter to stop: ")
    print("List :", lst)
    print(f"Your list has {len(lst)} elements.")


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()