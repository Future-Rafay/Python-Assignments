def shorten_list(lst: list) -> None:
    while len(lst) > 3:
        removed_elem_list = [lst.pop(0) for _ in range(3)]
        print("Removed elements:", removed_elem_list)
    print("List after shortening:", lst)

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
    shorten_list(lst)



# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()