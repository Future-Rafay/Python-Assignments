def get_last_element(lst):
    """Returns the first element of a list."""
    if lst:  # Check if the list is not empty
        return lst[-1]  # Return the last element of the list
    else:   # If the list is empty, return None or an appropriate message
        return None


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

    get_last_element(lst)
    print("Last element of the list:", get_last_element(lst))


    # This provided line is required at the end of
    # Python file to call the main() function.
if __name__ == '__main__':
    main()
