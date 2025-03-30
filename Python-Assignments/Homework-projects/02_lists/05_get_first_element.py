def get_first_element(lst):
    """Returns the first element of a list."""
    if lst:  # Check if the list is not empty
        return lst[0]


def get_list():
    # Convert the message to a list of characters
    lst = []
    elem: str = input(
        "Please enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)
        elem: str = input(
            "Please enter an element of the list or press enter to stop. ")
    return lst


def main():

    lst = get_list()
    print("List :", lst)

    get_first_element(lst)
    print("First element of the list:", get_first_element(lst))


    # This provided line is required at the end of
    # Python file to call the main() function.
if __name__ == '__main__':
    main()
