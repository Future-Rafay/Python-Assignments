def add_three_copies_to_list(my_list , message):
    """
    Adds three copies of the list to itself.
    :param my_list: The list to be modified.
    :return: None
    """
    for _ in range(3):
        my_list.append(message)

def main():
    message = input("Enter a message: ")
    # Convert the message to a list of characters
    my_list = []
    print("List before adding copies:", my_list)
    # Add three copies of the list to itself
    add_three_copies_to_list(my_list, message)
    print("List after adding copies:", my_list)


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()