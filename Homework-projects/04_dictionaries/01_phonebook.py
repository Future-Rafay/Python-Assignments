def add_to_phonebook(phonebook: dict) -> None:
    """Adds a name and phone number to the phonebook."""
    name = input("Enter name: ").lower()
    phone_number = input("Enter phone number: ")
    phonebook[name] = phone_number
    print(f"Added {name}: {phone_number}")


def search_in_phonebook(phonebook: dict) -> None:
    """Searches for a name in the phonebook."""
    name = input("Enter name to search: ").lower()
    if name in phonebook:
        print(f"{name}: {phonebook[name]}")

    else:
        print(f"{name} not found in the phonebook.")


def delete_from_phonebook(phonebook: dict) -> None:
    """Deletes a name and phone number from the phonebook."""
    name = input("Enter name to delete: ")
    if name in phonebook:
        del phonebook[name]
        print(f"Deleted {name} from the phonebook.")
    else:
        print(f"{name} not found in the phonebook.")


def show_phonebook(phonebook: dict) -> None:
    """Displays all entries in the phonebook."""
    if not phonebook:
        print("Phonebook is empty.")
    else:
        for name, phone_number in phonebook.items():
            print(f"{name}: {phone_number}")


def show_menu() -> None:
    """Displays the menu options."""
    print("1. Add a contact")
    print("2. Search for a contact")
    print("3. Delete a contact")
    print("4. Show all contacts")
    print("5. Quit")


def main():
    phonebook: dict = {}

    # welcome

    print("Welcome to the Phonebook!")
    print("You can add, search, delete, and show contacts.")
    print("Press 5 to quit the program.")

    while True:
        show_menu()
        action = input(
            "Choose an action :")
        if action == "5":
            print("Goodbye!")
            break

        elif action == "4":
            show_phonebook(phonebook)

        elif action == "3":
            delete_from_phonebook(phonebook)

        elif action == "2":
            search_in_phonebook(phonebook)

        elif action == "1":
            add_to_phonebook(phonebook)


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
